"""
Script de FastAPI
In Python 3.12

"""

import logging
from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI

from database import Base, engine
from routers import inventories, orders, products

logger = logging.getLogger(__name__)  # SET UP A LOGGER OBJECT
handler = logging.StreamHandler()  # ADD A STREAM HANDLER TO THE LOGGER OBJECT
logger.addHandler(handler)
# Set the logging level
logger.setLevel(logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Connect to the database and create tables if they don't exist
    with engine.begin() as conn:
        Base.metadata.create_all(bind=conn)
    yield
    # Shutdown: Dispose of the engine
    engine.dispose()


app = FastAPI(
    openapi_url="/api/v1/openapi.json",
    title="FastApi Test",
    version="0.1",
    description="My description",
    lifespan=lifespan,
)

api_vx = APIRouter(prefix="/api/v1")

# ROUTERS
api_vx.include_router(products.router)
api_vx.include_router(inventories.router)
api_vx.include_router(orders.router)

app.include_router(api_vx)

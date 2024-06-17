"""
ROUTER FOR PRODUCTS
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from models import Product
from schemas import ProductRequestModel, ProductResponseModel

router = APIRouter(prefix="/products", tags=["Products"])


@router.post(
    "/",
    summary="Create a new product",
    status_code=status.HTTP_200_OK,
    response_model=ProductResponseModel,
)
async def create_product(product: ProductRequestModel, db: Session = Depends(get_db)):
    """
    SERVICIO PARA AGREGAR UN PRODUCTO A LA BASE DE DATOS.

    BODY:
        {
          "name": "string",
          "stock": int
        }
    """
    db_product = Product(name=product.name, stock=product.stock)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

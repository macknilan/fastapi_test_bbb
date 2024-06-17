# MODELOS DE BASE DE DATOS

import uuid

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from database import Base


class Product(Base):
    """
    CLASE QUE REPRESENTA LA TABLA DE PRODUCTOS EN LA BASE DE DATOS.
    """

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    sku = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4, nullable=False)
    stock = Column(Integer)


class Order(Base):
    """
    CLASE QUE REPRESENTA LA TABLA DE ORDENES EN LA BASE DE DATOS.
    """

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    order_number = Column(
        UUID(as_uuid=True), unique=True, default=uuid.uuid4, nullable=False
    )
    supplier_name = Column(String(50), nullable=False)

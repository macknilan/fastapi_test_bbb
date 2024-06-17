"""
ROUTER FOR ORDERS
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from models import Order, Product
from schemas import OrderCreateModel, OrderResponseModel

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post(
    "/",
    summary="Create a new purchase order",
    status_code=status.HTTP_200_OK,
    response_model=OrderResponseModel,
)
async def add_order(order: OrderCreateModel, db: Session = Depends(get_db)):
    """
    SERVICIO PARA HACER UNA ORDEN DE COMPRA DE UN PRODUCTO
    """
    db_order = Order(supplier_name=order.supplier_name)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    db_product = Product(
        name=order.purchased_product.name, stock=order.purchased_product.stock
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_order

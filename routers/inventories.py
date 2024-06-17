"""
ROUTER FOR INVENTORIES
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models import Product
from schemas import ProductRequestPatchModel, ProductResponseModel

router = APIRouter(prefix="/inventories", tags=["Inventories"])


@router.patch(
    "/product/{product_id}",
    summary="Increase the stock of a product",
    status_code=status.HTTP_200_OK,
    response_model=ProductResponseModel,
)
async def add_more_product(
    product_id: int, product: ProductRequestPatchModel, db: Session = Depends(get_db)
):
    """SERVICIO PARA AUMENTAR EL STOCK DE UN PRODUCTO EN LA BASE DE DATOS.

    BODY:
        {
          "name": "string", <- NO REQUERIDO
          "stock": 20
        }
    """
    db_product = db.query(Product).get(product_id)

    if db_product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not fount."
        )

    db_product.stock += product.stock
    db.commit()
    db.refresh(db_product)

    return db_product

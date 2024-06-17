# PYDANTIC MODELS FOR THE API
import uuid
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class StockValidator:
    """CLASE HEREDABLE PARA VALIDAR EL ATRIBUTO -stock- DE LA TABLA -Products-"""

    @field_validator("stock")
    def stock_is_valid(cls, v):
        if v < 10:
            print(
                ",.-~*´¨¯¨`*·~-.¸-(_SE A AGREGADO UN PRODUCTO CON UN STOCK MENOR A 10._)-,.-~*´¨¯¨`*·~-.¸"
            )
        return v


class ProductBaseModel(BaseModel, StockValidator):
    name: str
    stock: int


class ProductRequestModel(ProductBaseModel):
    name: str = Field(
        title="Product Name",
        description="Name of the product",
        min_length=3,
        max_length=50,
    )
    stock: int = Field(
        title="Stock",
        description="Number of items in stock",
        default=100,
    )


class ProductResponseModel(ProductBaseModel):
    id: int
    name: str
    sku: uuid.UUID
    stock: int

    class ConfigDict:
        from_attributes = True


class ProductRequestPatchModel(ProductBaseModel, StockValidator):
    """
    CLASE PARA VALIDAR PATCH REQUEST
    """

    stock: int = Field(
        title="Stock",
        description="How many items to add to the stock",
        default=100,
    )
    name: Optional[str] = None


class OrderBaseModel(BaseModel):
    order_number: uuid.UUID


class OrderCreateModel(OrderBaseModel):
    supplier_name: str
    purchased_product: ProductRequestModel


class OrderResponseModel(OrderBaseModel):
    id: int
    order_number: uuid.UUID

    class ConfigDict:
        from_attributes = True

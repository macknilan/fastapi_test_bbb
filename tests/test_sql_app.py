# TESTING PARA LOS SERVICIOS

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, get_db
from main import app

# SE CONFIGURA LA BASE DE DATOS EN MEMORIA PARA PRUEBAS
DATABASE_URL = "postgresql://test_fast_api_user:Pase de entrada de test_fast_api_user@localhost:5432/test_fast_api_db"

engine = create_engine(
    DATABASE_URL,
    echo=True,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# DEPENDENCIA PARA SOBREESCRIBIR LA DEPENDENCIA get_db EN EL APP PRINCIPAL
def override_get_db():
    database = TestingSessionLocal()
    try:
        yield database
    finally:
        database.close()


# SE SOBREESCRIBE LA DEPENDENCIA get_db EN EL APP PRINCIPAL
app.dependency_overrides[get_db] = override_get_db

# CONFIGURACIÓN EL CLIENTE DE PRUEBAS
client = TestClient(app)


def test_create_item():
    """
    PRUEBA PARA EL SERVICIO DE CREACIÓN DE PRODUCTOS.
    """
    response = client.post(
        "/api/v1/products/", json={"name": "Nieve de limón No 1", "stock": 100}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Nieve de limón No 1"
    assert data["stock"] == 100
    assert "sku" in data
    assert "id" in data


def test_add_more_product():
    """
    PRUEBA PARA EL SERVICIO DE AUMENTAR EL STOCK DE UN PRODUCTO.
    """
    product_id = 1
    response = client.patch(
        f"/api/v1/inventories/product/{product_id}", json={"stock": 100}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == product_id


def test_add_order():
    """
    TODO:
    """
    response = client.post(
        "/api/v1/orders/",
        json={
            "order_number": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "supplier_name": "Proveedor de fresa No 1",
            "purchased_product": {"name": "Nieve de fresa No 2", "stock": 100},
        },
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == 1


def setup() -> None:
    # CREAR LAS TABLAS EN LA BASE DE DATOS DE PRUEBAS
    Base.metadata.create_all(bind=engine)


def teardown() -> None:
    # ELIMINAR LAS TABLAS DE LA BASE DE DATOS DE PRUEBAS
    Base.metadata.drop_all(bind=engine)

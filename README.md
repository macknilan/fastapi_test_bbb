


## Descripción

Pasos para ejecutar el proyecto.


## Requerimientos

- Clonar el repositorio
- Dentro del proyecto crear ambiente virtual

```bash
python3 -m venv ~/ruta-de-carpeta-donde-se-desea-la-carpeta/coppel_test
```

- Activar ambiente virtual

```bash
source ~/ruta-de-carpeta-donde-se-desea-la-carpeta/coppel_test/bin/activate
```

Instalar en el ambiente virtual las dependencias para el proyecto

```bash
pip install -r requirements.txt
```

La practica esta realizada con el framework FastAPI, para correr el proyecto ejecutar el siguiente comando

```bash
uvicorn main:app --reload --port 8000 --host 127.0.0.1
```

## Endpoints

Para poder consultar los endpoints de la API, se puede acceder a la documentación de la misma en la siguiente URL

1. http://127.0.0.1:8000/docs
2. http://127.0.0.1:8000/redoc



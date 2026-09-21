# Biblioteca Docker

![Python tests](https://github.com/<tu-usuario>/<tu-repo>/actions/workflows/python-tests.yml/badge.svg)
![Docker build](https://github.com/<tu-usuario>/<tu-repo>/actions/workflows/docker.yml/badge.svg)

Proyecto de biblioteca con Flask, SQLAlchemy y Docker.

## Requisitos

- Docker
- Docker Compose
- Python 3.12

## Ejecutar con Docker Compose

```bash
docker compose up --build
```

La aplicación queda disponible en:

```bash
http://localhost:5000
```

## Ejecutar pruebas localmente

```bash
cd app
pip install -r requirements.txt
pytest app/test -q
```

## Estructura

- `app/` - aplicación Flask
- `docker-compose.yml` - configuración de servicios
- `.github/workflows/` - workflows de CI/CD

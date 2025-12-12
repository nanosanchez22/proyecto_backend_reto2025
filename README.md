# API tareas - Reto 2025

Mini backend hecho con FastAPI + SQLAlchemy. Expone registro/login con JWT y CRUD de tareas con borrado logico.

## Correr con Docker
Requisitos: Docker Desktop.
```bash
git clone https://github.com/nanosanchez22/proyecto_backend_reto2025.git
cd proyecto_backend_reto2025
docker compose up --build
```
La API queda en `http://localhost:8000` (Swagger en `/docs`). Para apagarla usa `docker compose down`.

## Correr local (opcional)
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
set DATABASE_URL=postgresql+psycopg2://usuario:password@localhost:5432/reto_backend
set JWT_SECRET=cambia_este_valor
set JWT_EXPIRE_MINUTES=60
uvicorn app.main:app --reload
```

## Endpoints utiles
- `POST /auth/register` crea usuarios.
- `POST /auth/login` recibe `{ "email": "...", "password": "..." }` y devuelve `access_token`.
- `/tasks` (GET/POST/PUT/DELETE) maneja las tareas del usuario autenticado, eliminando de forma logica (`is_active=False`).

## Como probar rapido
```bash
# registro
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"demo@example.com\",\"password\":\"secret\"}"

# login
TOKEN=$(curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"demo@example.com\",\"password\":\"secret\"}" | jq -r .access_token)

# crear tarea
curl -X POST http://localhost:8000/tasks/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"Primera tarea\"}"
```

En Swagger: ejecuta `/auth/login`, copia el token y pegalo en el boton **Authorize** (Bearer). Con eso podes probar el resto del CRUD.

## Tecnologias
- Python 3.11
- FastAPI + Uvicorn
- SQLAlchemy ORM
- PostgreSQL (driver `psycopg2-binary`)
- JWT con `python-jose` y hashing con `passlib[bcrypt]`

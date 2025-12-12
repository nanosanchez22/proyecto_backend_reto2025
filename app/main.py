from fastapi import FastAPI

from .database import Base, engine
from .routers import auth, tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Reto Backend 2025")

app.include_router(auth.router)
app.include_router(tasks.router)


@app.get("/")
def root():
    return {"message": "API operativa"}

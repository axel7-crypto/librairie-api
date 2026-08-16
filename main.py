from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine, Base
from models import model
from routers import auteur
from routers import livre
from routers import client
from routers import commande
from routers import auth
import os

origines_autorisees = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auteur.router)
app.include_router(livre.router)
app.include_router(client.router)
app.include_router(commande.router)
app.include_router(auth.router)
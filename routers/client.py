from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from db.database import get_db
from schemas import schema
from crud import crud
from auth.security import utilisateur_courant


router = APIRouter(
    prefix="/clients", 
    tags= ["Clients"]
)

#CREER UNE RESSOURCE
@router.post("/", response_model=schema.ClientResponse)
def creer_client(Client: schema.ClientCreate, db: Session = Depends(get_db), utilisateur: dict = Depends(utilisateur_courant)):
    return crud.creer_client(db, Client)

#RECUPERER UNE RESSOURCE
@router.get("/", response_model=list[schema.ClientResponse])
def lister_clients(skip: int = 0, limit: int = 10, nom: Optional[str] = None, db: Session = Depends(get_db)):
    return crud.lister_clients(db, skip, limit, nom)


@router.get("/{id_client}", response_model=schema.ClientResponse)
def obtenir_client(id_client: int, db: Session = Depends(get_db)):
    resultat = crud.obtenir_client(db, id_client)
    if resultat is None:
        raise HTTPException(status_code=404, detail="Client introuvable")
    return resultat

#MODIFIER UNE RESSOURCE
@router.put("/{id_client}", response_model=schema.ClientResponse)
def modifier_client(id_client: int, client: schema.ClientCreate, db: Session = Depends(get_db), utilisateur: dict = Depends(utilisateur_courant)):
    resultat = crud.modifier_client(db, id_client, client)
    if resultat is None:
        raise HTTPException(status_code=404, detail="Client introuvable")
    return resultat


#SUPPRIMER UNE RESSOURCE
@router.delete("/{id_client}")
def supprimer_client(id_client: int, db: Session = Depends(get_db), utilisateur: dict = Depends(utilisateur_courant)):
    resultat = crud.supprimer_client(db, id_client)
    if resultat is None:
        raise HTTPException(status_code=404, detail="Client introuvable")
    return {"message": f"Client {id_client} supprimé"}
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from db.database import get_db
from schemas import schema
from crud import crud
from auth.security import utilisateur_courant, admin_requis


router = APIRouter(prefix="/auteurs", tags=["Auteurs"])

#CREER UNE RESSOURCE
@router.post("/", response_model=schema.AuteurResponse)
def creer_auteur(auteur: schema.AuteurCreate, db: Session = Depends(get_db), utilisateur: dict = Depends(utilisateur_courant)):
    return crud.creer_auteur(db, auteur)

#RECUPERER UNE RESSOURCE
@router.get("/", response_model=list[schema.AuteurResponse])
def lister_auteurs(skip: int = 0, limit: int = 10, nom: Optional[str] = None, db: Session = Depends(get_db)):
    return crud.lister_auteurs(db, skip, limit, nom)



@router.get("/{id_auteur}", response_model=schema.AuteurResponse)
def obtenir_auteur(id_auteur: int, db: Session = Depends(get_db)):
    resultat = crud.obtenir_auteur(db, id_auteur)
    if resultat is None:
        raise HTTPException(status_code=404, detail="Auteur introuvable")
    return resultat

#MODIFIER UNE RESSOURCE
@router.put("/{id_auteur}", response_model=schema.AuteurResponse)
def modifier_auteur(id_auteur: int, auteur: schema.AuteurCreate, db: Session = Depends(get_db), utilisateur: dict = Depends(admin_requis)):
    resultat = crud.modifier_auteur(db, id_auteur, auteur)
    if resultat is None:
        raise HTTPException(status_code=404, detail="Auteur introuvable")
    return resultat


#SUPPRIMER UNE RESSOURCE
@router.delete("/{id_auteur}")
def supprimer_auteur(id_auteur: int, db: Session = Depends(get_db), utilisateur: dict = Depends(admin_requis)):
    resultat = crud.supprimer_auteur(db, id_auteur)
    if resultat is None:
        raise HTTPException(status_code=404, detail="Auteur introuvable")
    return {"message": f"Auteur {id_auteur} supprimé"}




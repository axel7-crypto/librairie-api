from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from db.database import get_db
from schemas import schema
from crud import crud
from auth.security import utilisateur_courant, admin_requis

router = APIRouter(
    prefix="/livres", 
    tags= ["Livres"]
)

#CREER UNE RESSOURCE
@router.post("/", response_model=schema.LivreResponse)
def creer_livre(livre: schema.LivreCreate, db: Session = Depends(get_db), utilisateur: dict = Depends(utilisateur_courant)):
    return crud.creer_livre(db, livre)


#RECUPERER UNE RESSOURCE
@router.get("/", response_model=list[schema.LivreResponse])
def lister_livres(skip: int = 0, limit: int = 10, titre: Optional[str] = None, db: Session = Depends(get_db)):
    return crud.lister_livres(db, skip, limit, titre)

@router.get("/{id_livre}", response_model=schema.LivreAvecAuteur)
def obtenir_livre(id_livre: int, db: Session = Depends(get_db)):
    resultat = crud.obtenir_livre(db, id_livre)
    if resultat is None:
        raise HTTPException(status_code=404, detail="Livre introuvable")
    return resultat

#MODIFIER UNE RESSOURCE
@router.put("/{id_livre}", response_model=schema.LivreResponse)
def modifier_livre(id_livre: int, livre: schema.LivreCreate, db: Session = Depends(get_db), utilisateur: dict = Depends(admin_requis)):
    resultat = crud.modifier_livre(db, id_livre, livre)
    if resultat is None:
        raise HTTPException(status_code=404, detail="Livre introuvable")
    return resultat



#SUPPRIMER UNE RESSOURCE
@router.delete("/{id_livre}")
def supprimer_livre(id_livre: int, db: Session = Depends(get_db), utilisateur: dict = Depends(admin_requis)):
    resultat = crud.supprimer_livre(db, id_livre)
    if resultat is None:
        raise HTTPException(status_code=404, detail="Livre introuvable")
    return {"message": f"Livre {id_livre} supprimé"}
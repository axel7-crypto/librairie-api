from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from schemas import schema
from crud import crud
from auth.security import utilisateur_courant, admin_requis


router = APIRouter(
    prefix="/commandes", 
    tags= ["Commandes"]
)

#CREER UNE RESSOURCE
@router.post("/", response_model=schema.CommandeResponse)
def creer_commande(Commande: schema.CommandeCreate, db: Session = Depends(get_db), utilisateur: dict = Depends(utilisateur_courant)):
    return crud.creer_commande(db, Commande)

#RECUPERER UNE RESSOURCE
@router.get("/", response_model=list[schema.CommandeResponse])
def lister_commandes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.lister_commandes(db, skip, limit)

@router.get("/{id_commande}", response_model=schema.CommandeAvecClient)
def obtenir_commande(id_commande: int, db: Session = Depends(get_db)):
    resultat = crud.obtenir_commande(db, id_commande)
    if resultat is None:
        raise HTTPException(status_code=404, detail="Commande introuvable")
    return resultat

#MODIFIER UNE RESSOURCE
@router.put("/{id_commande}", response_model=schema.CommandeResponse)
def modifier_commande(id_commande: int, commande: schema.CommandeCreate, db: Session = Depends(get_db), utilisateur: dict = Depends(admin_requis)):
    resultat = crud.modifier_commande(db, id_commande, commande)
    if resultat is None:
        raise HTTPException(status_code=404, detail="Commande introuvable")
    return resultat


#SUPPRIMER UNE RESSOURCE
@router.delete("/{id_commande}")
def supprimer_commande(id_commande: int, db: Session = Depends(get_db), utilisateur: dict = Depends(admin_requis)):
    resultat = crud.supprimer_commande(db, id_commande)
    if resultat is None:
        raise HTTPException(status_code=404, detail="Commande introuvable")
    return {"message": f"Commande {id_commande} supprimé"}
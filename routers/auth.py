from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from schemas import schema
from models import model
from auth.security import hacher_mot_de_passe, creer_token, verifier_mot_de_passe, utilisateur_courant, admin_requis
from auth.security import verifier_mot_de_passe
from fastapi.security import OAuth2PasswordRequestForm



router = APIRouter(prefix="/auth", tags=["Authentification"])

@router.post("/register", response_model=schema.Token)
def inscription(utilisateur: schema.UtilisateurCreate, db: Session = Depends(get_db)):
    existant = db.query(model.Utilisateur).filter(model.Utilisateur.email == utilisateur.email).first()
    if existant:
        raise HTTPException(status_code=400, detail="Email déjà utilisé")

    nouvel_utilisateur = model.Utilisateur(
        email=utilisateur.email,
        mot_de_passe_hache=hacher_mot_de_passe(utilisateur.mot_de_passe)
    )
    db.add(nouvel_utilisateur)
    db.commit()

    token = creer_token(nouvel_utilisateur.email, nouvel_utilisateur.role)
    return {"access_token": token, "token_type": "bearer"}

 
@router.post("/login", response_model=schema.Token)
def connexion(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    utilisateur_existant = db.query(model.Utilisateur).filter(model.Utilisateur.email == form_data.username).first()
    if not utilisateur_existant or not verifier_mot_de_passe(form_data.password, utilisateur_existant.mot_de_passe_hache):
        raise HTTPException(status_code=401, detail="Email ou mot de passe incorrect")

    token = creer_token(utilisateur_existant.email, utilisateur_existant.role)
    return {"access_token": token, "token_type": "bearer"}


@router.delete("/me")
def supprimer_mon_compte(db: Session = Depends(get_db), utilisateur: dict = Depends(utilisateur_courant)):
    utilisateur_existant = db.query(model.Utilisateur).filter(model.Utilisateur.email == utilisateur["email"]).first()
    if utilisateur_existant is None:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")

    db.delete(utilisateur_existant)
    db.commit()
    return {"message": "Compte supprimé avec succès"}



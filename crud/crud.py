from sqlalchemy.orm import Session
from typing import Optional
from models import model
from schemas import schema

#CREER UNE RESSOURCE
def creer_auteur(db: Session, auteur: schema.AuteurCreate):
    nouvel_auteur = model.Auteur(
        nom=auteur.nom,
        prenom=auteur.prenom,
        nationalite=auteur.nationalite
    )
    db.add(nouvel_auteur)
    db.commit()
    db.refresh(nouvel_auteur)
    return nouvel_auteur


def creer_livre(db: Session, livre: schema.LivreCreate):
    nouveau_livre = model.Livre(
        id_auteur=livre.id_auteur,
        titre=livre.titre,
        prix=livre.prix,
        date_de_parution=livre.date_de_parution
    )
    db.add(nouveau_livre)
    db.commit()
    db.refresh(nouveau_livre)
    return nouveau_livre


def creer_client(db: Session, client: schema.ClientCreate):
    nouveau_client = model.Client(
        nom=client.nom,
        prenom=client.prenom,
        email=client.email,
        date_inscription=client.date_inscription
    )
    db.add(nouveau_client)
    db.commit()
    db.refresh(nouveau_client)
    return nouveau_client


def creer_commande(db: Session, Commande: schema.CommandeCreate):
    nouvelle_commande = model.Commande(
        date_de_commande=Commande.date_de_commande,
        quantite=Commande.quantite,
        id_client=Commande.id_client,
        id_livre=Commande.id_livre
    )
    db.add(nouvelle_commande)
    db.commit()
    db.refresh(nouvelle_commande)
    return nouvelle_commande


#RECUPERER UNE RESSOURCE
def lister_auteurs(db: Session, skip: int = 0, limit: int = 10, nom: Optional[str] = None):
    requete = db.query(model.Auteur)
    if nom:
        requete = requete.filter(model.Auteur.nom.ilike(f"%{nom}%"))
    return requete.offset(skip).limit(limit).all()

def obtenir_auteur(db: Session, id_auteur: int):
    return db.query(model.Auteur).filter(model.Auteur.id_auteur == id_auteur).first()


def lister_clients(db: Session, skip: int = 0, limit: int = 10, nom: Optional[str] = None):
    requete = db.query(model.Client)
    if nom:
        requete = requete.filter(model.Client.nom.ilike(f"%{nom}%"))
    return requete.offset(skip).limit(limit).all()

def obtenir_client(db: Session, id_client: int):
    return db.query(model.Client).filter(model.Client.id_client == id_client).first()



def lister_commandes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(model.Commande).offset(skip).limit(limit).all()

def obtenir_commande(db: Session, id_commande: int):
    return db.query(model.Commande).filter(model.Commande.id_commande == id_commande).first()



def lister_livres(db: Session, skip: int = 0, limit: int = 10, titre: Optional[str] = None):
    requete = db.query(model.Livre)
    if titre:
        requete = requete.filter(model.Livre.titre.ilike(f"%{titre}%"))
    return requete.offset(skip).limit(limit).all()


def obtenir_livre(db: Session, id_livre: int):
    return db.query(model.Livre).filter(model.Livre.id_livre == id_livre).first()

#MODIFIER UNE RESSOURCE
def modifier_auteur(db: Session, id_auteur: int, auteur: schema.AuteurCreate):
    auteur_existant = db.query(model.Auteur).filter(model.Auteur.id_auteur == id_auteur).first()
    if auteur_existant is None:
        return None

    auteur_existant.nom = auteur.nom
    auteur_existant.prenom = auteur.prenom
    auteur_existant.nationalite = auteur.nationalite

    db.commit()
    db.refresh(auteur_existant)
    return auteur_existant


def modifier_client(db: Session, id_client: int, client: schema.ClientCreate):
    client_existant = db.query(model.Client).filter(model.Client.id_client == id_client).first()
    if client_existant is None:
        return None

    client_existant.nom = client.nom
    client_existant.prenom = client.prenom
    client_existant.email = client.email
    client_existant.date_inscription = client.date_inscription
    db.commit()
    db.refresh(client_existant)
    return client_existant


def modifier_commande(db: Session, id_commande: int, commande: schema.CommandeCreate):
    commande_existante = db.query(model.Commande).filter(model.Commande.id_commande == id_commande).first()
    if commande_existante is None:
        return None

    commande_existante.date_de_commande = commande.date_de_commande
    commande_existante.quantite = commande.quantite
    commande_existante.id_client = commande.id_client
    commande_existante.id_livre = commande.id_livre
    db.commit()
    db.refresh(commande_existante)
    return commande_existante


def modifier_livre(db: Session, id_livre: int, livre: schema.LivreCreate):
    livre_existant = db.query(model.Livre).filter(model.Livre.id_livre == id_livre).first()
    if livre_existant is None:
        return None

    livre_existant.titre = livre.titre
    livre_existant.prix = livre.prix
    livre_existant.date_de_parution = livre.date_de_parution
    livre_existant.id_auteur = livre.id_auteur
    db.commit()
    db.refresh(livre_existant)
    return livre_existant


#SUPPRIMER UNE RESSOURCE
def supprimer_auteur(db: Session, id_auteur: int):
    auteur_existant = db.query(model.Auteur).filter(model.Auteur.id_auteur == id_auteur).first()
    if auteur_existant is None:
        return None
    db.delete(auteur_existant)
    db.commit()
    return auteur_existant


def supprimer_livre(db: Session, id_livre: int):
    livre_existant = db.query(model.Livre).filter(model.Livre.id_livre == id_livre).first()
    if livre_existant is None:
        return None
    db.delete(livre_existant)
    db.commit()
    return livre_existant


def supprimer_client(db: Session, id_client: int):
    client_existant = db.query(model.Client).filter(model.Client.id_client == id_client).first()
    if client_existant is None:
        return None
    db.delete(client_existant)
    db.commit()
    return client_existant


def supprimer_commande(db: Session, id_commande: int):
    commande_existante = db.query(model.Commande).filter(model.Commande.id_commande == id_commande).first()
    if commande_existante is None:
        return None
    db.delete(commande_existante)
    db.commit()
    return commande_existante
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class Auteur(Base):
    __tablename__ = "auteur"
    id_auteur = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    nationalite = Column(String)

    livre = relationship("Livre", back_populates="auteur")

class Livre(Base):
    __tablename__ = "livre"
    id_livre= Column(Integer, primary_key=True, index=True)
    titre= Column(String, nullable=False)
    prix= Column(Float, nullable=False)
    date_de_parution= Column(Date)
    id_auteur= Column(Integer, ForeignKey("auteur.id_auteur"))

    auteur = relationship("Auteur", back_populates="livre")
    commande = relationship("Commande", back_populates="livre")



class Client(Base):
    __tablename__ = "client"
    id_client= Column(Integer, primary_key=True, index=True)
    nom= Column(String, nullable=False)
    prenom= Column(String, nullable=False)
    email= Column(String, nullable=False)
    date_inscription= Column(Date)

    commande = relationship("Commande", back_populates="client")


class Commande(Base):
    __tablename__ = "commande"
    id_commande= Column(Integer, primary_key=True, index=True)
    date_de_commande= Column(Date)
    quantite= Column(Integer, nullable=False)
    id_client= Column(Integer, ForeignKey("client.id_client"))
    id_livre = Column(Integer, ForeignKey("livre.id_livre"))
    
    client = relationship("Client", back_populates="commande")
    livre = relationship("Livre", back_populates="commande")


class Utilisateur(Base):
    __tablename__ = "utilisateur"
    id_utilisateur = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique =True, nullable=False)
    mot_de_passe_hache = Column(String, nullable=False)
    role = Column(String, nullable=False, default="utilisateur")
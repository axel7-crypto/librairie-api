from pydantic import BaseModel, Field, EmailStr, field_validator
from datetime import date

class AuteurBase(BaseModel):
    nom: str
    prenom: str
    nationalite: str | None = None

class AuteurCreate(AuteurBase):
    pass

class AuteurResponse(AuteurBase):
    id_auteur: int

    class Config:
        from_attributes = True

   

class LivreBase(BaseModel):
    id_auteur: int
    titre: str
    prix: float = Field(gt=0)
    date_de_parution: date

    @field_validator("date_de_parution")
    @classmethod
    def verifier_date_parution(cls, valeur):
        if valeur > date.today():
            raise ValueError("La date de parution ne peut pas être dans le futur")
        return valeur
     

class LivreCreate(LivreBase):
    pass

class LivreResponse(LivreBase):
    id_livre: int

    class Config:
        from_attributes = True


class LivreAvecAuteur(LivreBase):
    id_livre: int
    auteur: AuteurResponse

    class Config:
        from_attributes = True


class ClientBase(BaseModel):
    nom: str
    prenom: str
    email: EmailStr
    date_inscription: date

class ClientCreate(ClientBase):
    pass

class ClientResponse(ClientBase):
    id_client: int

    class Config:
        from_attributes = True



class CommandeBase(BaseModel):
    date_de_commande: date
    quantite: int = Field(gt=0)
    id_client: int
    id_livre: int

class CommandeCreate(CommandeBase):
    pass

class CommandeResponse(CommandeBase):
    id_commande: int

    class Config:
        from_attributes = True


class CommandeAvecClient(CommandeBase):
    id_commande: int
    client: ClientResponse

    class Config:
        from_attributes = True

class CommandeAvecLivre(CommandeBase):
    id_commande: int
    livre: LivreResponse

    class Config:
        from_attributs = True
          
class UtilisateurCreate(BaseModel):
    email: EmailStr
    mot_de_passe: str


class Token(BaseModel):
    access_token: str
    token_type: str



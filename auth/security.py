from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
import os
from dotenv import load_dotenv


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
EXPIRATION_MINUTES = int(os.getenv("EXPIRATION_MINUTES"))


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def hacher_mot_de_passe(mot_de_passe : str) -> str :
    return pwd_context.hash(mot_de_passe)

def verifier_mot_de_passe(mot_de_passe: str, mot_de_passe_hache: str) -> bool:
    return pwd_context.verify(mot_de_passe, mot_de_passe_hache)

def creer_token(email: str, role: str) -> str:
    expiration = datetime.now(timezone.utc) + timedelta(minutes=EXPIRATION_MINUTES)
    payload = {"sub": email, "role": role, "exp": expiration}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def utilisateur_courant(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        role = payload.get("role")
        if email is None:
            raise HTTPException(status_code=401, detail="Token invalide")
        return {"email": email, "role": role}
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalide")


def admin_requis(utilisateur: dict = Depends(utilisateur_courant)):
    if utilisateur["role"] != "admin":
        raise HTTPException(status_code=403, detail="Accès réservé aux administrateurs")
    return utilisateur
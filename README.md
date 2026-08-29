#  Librairie API

API REST complète développée avec **FastAPI** pour la gestion d'une librairie — auteurs, livres, clients et commandes — avec authentification, autorisations, validation métier, tests automatisés et déploiement en production.

🔗 **Documentation interactive en ligne** : [librairie-api-librairie-api.up.railway.app/docs](https://librairie-api-librairie-api.up.railway.app/docs)


---

## Fonctionnalités

- **CRUD complet** sur 4 tables reliées (`Auteur`, `Livre`, `Client`, `Commande`)
- **Authentification JWT** — inscription, connexion, protection des routes
- **Autorisations par rôle** — utilisateur connecté / administrateur
- **Validation métier** avec Pydantic — contraintes numériques (`Field`), format email (`EmailStr`), validateurs personnalisés
- **Pagination** (`skip` / `limit`) et **filtres de recherche**
- **Relations imbriquées** dans les réponses (ex : un livre renvoyé avec les infos complètes de son auteur)
- **Tests automatisés** avec `pytest`, sur une base de données dédiée aux tests
- **Conteneurisation** avec Docker et Docker Compose
- **Variables d'environnement** séparées dev/production
- **CORS** configuré pour la communication avec un frontend
- **CI/CD** — tests exécutés automatiquement à chaque push via GitHub Actions
- **Déploiement en production** sur Railway

---

## Stack technique

| Domaine | Outils |
|---|---|
| Langage | Python 3.13 |
| Framework | FastAPI |
| Base de données | PostgreSQL |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Authentification | JWT (python-jose, passlib/bcrypt) |
| Tests | pytest, httpx |
| Conteneurisation | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| Déploiement | Railway |

---

## Structure du projet

```
backend/
├── db/            # Connexion à la base de données
├── models/        # Modèles SQLAlchemy (tables)
├── schemas/       # Schemas Pydantic (validation des données)
├── crud/          # Logique d'accès à la base de données
├── routers/       # Routes de l'API
├── auth/          # Authentification et sécurité (JWT)
├── tests/         # Tests automatisés
├── Dockerfile
├── docker-compose.yml
└── main.py        # Point d'entrée de l'application
```

---

## Installation en local

### Prérequis

- Python 3.13
- PostgreSQL
- Docker (optionnel, pour lancer via conteneurs)

### Étapes

```bash
# Cloner le dépôt
git clone https://github.com/axel7-crypto/librairie-api.git
cd librairie-api

# Créer et activer un environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Configurer les variables d'environnement
cp .env.example .env
# Puis éditer .env avec ses propres valeurs

# Lancer l'API
uvicorn main:app --reload
```

L'API est alors accessible sur `http://127.0.0.1:8000`, la documentation interactive sur `http://127.0.0.1:8000/docs`.

### Avec Docker

```bash
docker compose up --build
```

### Lancer les tests

```bash
python3 -m pytest -v
```

---

## Modèle de données

Le projet s'appuie sur 4 entités principales :

- **Auteur** — `id_auteur`, `nom`, `prenom`, `nationalite`
- **Livre** — `id_livre`, `titre`, `prix`, `date_de_parution`, `id_auteur` (clé étrangère)
- **Client** — `id_client`, `nom`, `prenom`, `email`, `date_inscription`
- **Commande** — `id_commande`, `date_de_commande`, `quantite`, `id_client`, `id_livre`

Ainsi qu'une table **Utilisateur** dédiée à l'authentification (email, mot de passe haché, rôle).

---

## À propos

Une API REST complète pour la gestion d'une librairie (auteurs, livres, clients, commandes), construite avec FastAPI et PostgreSQL. Le projet couvre l'ensemble du cycle de développement backend : modélisation des données (MERISE), CRUD complet avec relations, authentification JWT, autorisations par rôle, validation des entrées, pagination et filtres de recherche, tests automatisés (pytest), conteneurisation Docker, intégration continue (GitHub Actions) et déploiement en production sur Railway.

**Auteur** : Axel Kouakou — [GitHub](https://github.com/axel7-crypto)

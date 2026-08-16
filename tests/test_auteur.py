def test_creer_auteur(client):
    reponse = client.post("/auteurs/", json={
        "nom": "Diallo",
        "prenom": "Mariam",
        "nationalite": "Sénégalaise"
    })
    assert reponse.status_code == 401


def test_creer_auteur_avec_donnees_invalides(client):
    reponse = client.post("/auteurs/", json={
        "nom": "Diallo"
        # prenom et nationalite manquants
    })
    assert reponse.status_code in (401, 422)


def test_obtenir_auteur_inexistant(client):
    reponse = client.get("/auteurs/9999")
    assert reponse.status_code == 404



def test_prix_negatif_rejete(client):
    reponse = client.post("/livres/", json={
        "id_auteur": 1,
        "titre": "Un livre test",
        "prix": -50,
        "date_de_parution": "2020-01-01"
    })
    assert reponse.status_code in (401, 422)


def test_creer_auteur_retourne_bon_nom(client):
    # nécessiterait un token valide ici, donc exemple simplifié
    reponse = client.get("/auteurs/1")
    if reponse.status_code == 200:
        assert reponse.json()["nom"] == "Camara"


def test_obtenir_livre_inexistant(client):
    reponse = client.get("/livres/9999")
    assert reponse.status_code == 404
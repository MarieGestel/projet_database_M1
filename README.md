# projet_database_M1

=> Lancer l'application Docker
=> Lancer Docker via le terminal:
docker compose up

=> Dans dossier projet ou tests, lancer:
docker compose run my-python-app pytest bash

=> pour vérifier la lecture des test:
docker compose run my-python-app pytest

Rappel CONVENTION:
-> dans le fichier test 
    - Bien écrire les fonctions en débutant par test
    - le fichier ne doit pas s'appeller test.py (ex: test_api.py)

-> pour pouvoir se déplacer dans les dossiers, mettre un fichier __init__.py seulement dans le dossier tests et non dans le dossier source
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
### Pour cloner le dossier, prendre la clé SSH
git clone git@github.com:MarieGestel/projet_database_M1.git


### Make sure your postgresql server is running before runing code below
### Make sure also your Flask server is running.
### f3623bde9430 ==> faire docker ps pour voir l'ID du container de postegresql
docker exec -it f3623bde9430 bash 

psql -U user -d mydb

### Si la table n'existe pas, la créer
CREATE DATABASE mydb; 

### After that, you need to create a table
CREATE TABLE tv_news ( id SERIAL PRIMARY KEY, date VARCHAR(120) NOT NULL, title VARCHAR(120) NOT NULL, url VARCHAR(500) NOT NULL, media VARCHAR(50) NOT NULL);

### Pour voir la table
\dt 

### Pour afficher les données qui sont dans la table
SELECT * FROM tv_news; 

### Copie de mon fichier csv de mon local vers le container 
docker cp drought-tv-news.csv f3623bde9430:/drought-tv-news.csv

### Ensuite je copie les données dans la table. 
COPY tv_news(date, title, url, media) FROM '/drought-tv-news.csv' DELIMITER ',' CSV HEADER;

### S'il envoi une erreur disant que la taille d'une colonne est petite, le code ci-dessous permet de le modifier.
ALTER TABLE tv_news ALTER COLUMN title TYPE VARCHAR(255);


### Manipulation de Git:
- git pull
- git status
- git add nom du fichier
- git add .
- git commit -m ‘’message’’
- git push




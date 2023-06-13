docker cp drought-tv-news.csv postgres:13.6:/drought-tv-news.csv©docker exec -it postgres bash
psql -U user -d mydb
CREATE TABLE tv_news(id SERIAL PRIMARY KEY, date VARCHAR(120), media VARCHAR(200), title VARCHAR(500), url VARCHAR(500));
\copy tv_news(date, media, title, url) FROM 'drought-tv-news.csv' DELIMITER ',' CSV HEADER;
COPY tv_news(date, media, title, url) FROM 'drought-tv-news.csv' DELIMITER ',' CSV HEADER;
Select * from tv_news
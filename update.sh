echo 'Start updating';
cp db.sqlite3 ./dumps/db.sqlite3;

echo 'Building';
docker build --force-rm -t meme ./meme-django;

echo 'Runing';
docker run --rm -it -v `pwd`/db.sqlite3:/app/db.sqlite3 -p 8080:8000 meme;

echo 'Updated';
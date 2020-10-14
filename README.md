# django_app
docker-compose build --no-cache

docker-compose run python ./manage.py makemigrations

docker-compose run python ./manage.py migrate

docker-compose run python ./manage.py createsuperuser

docker-compose up -d

-------./.env----------
DEBUG=1
SECRET_KEY=xxxxxxxxxxx
MYSQL_DATABASE=xxxxxx
MYSQL_USER=xxxx
MYSQL_PASSWORD=xxxx
MYSQL_HOST=xxxx

API_KEY=xxxxxx
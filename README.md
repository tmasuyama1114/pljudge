# django_app
# https://qiita.com/kenkono/items/6221ad12670d1ae8b1dd
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

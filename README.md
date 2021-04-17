## はじめに
このアプリは Python の Web フレームワークである Django をベースに作られた Web アプリです。  
Django/Nginx/MySQL それぞれを Docker コンテナで稼働させます。  

## 事前準備
#### .env ファイルの作成
環境変数は **.env** ファイルとして読み込ませます。  
プロジェクト直下に **.env** ファイルを作成し、以下のように各パラメータを記述してください。
(API_KEY については後述)

```.env
DEBUG=1
SECRET_KEY=xxxxxxxxxxx
MYSQL_DATABASE=xxxxxx
MYSQL_USER=xxxx
MYSQL_PASSWORD=xxxx
MYSQL_HOST=xxxx
API_KEY=xxxxxx
```

#### API Key の取得
このアプリでは **Financial Modeling Prep** より米国株の情報を API で取得しています。  
本リポジトリ内のアプリを使用したい方は [公式サイト](https://financialmodelingprep.com/login) にユーザ登録 (無料) し、API キーを取得してください。
API の使用方法については [Financial Modeling Prep API Documentation](https://financialmodelingprep.com/developer/docs/#Company-Profile) を参照してください。  


## コンテナの起動方法

Docker を使用できる環境で以下のコマンドを入力してください。

```
$ docker-compose build --no-cache
$ docker-compose run python ./manage.py makemigrations
$ docker-compose run python ./manage.py migrate
$ docker-compose run python ./manage.py createsuperuser
$ docker-compose up -d
```

ブラウザに "127.0.0.1" と入力すればアプリのトップページが表示されます。
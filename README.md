# pythonTestTask

To run locally:

```
git clone git@github.com:mihailBz/pythonTestTask.git
cd pythonTestTask
```
Create .env.dev file:
```
#.env.dev
DEBUG=1
SECRET_KEY=secret
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=postgres
SQL_USER=postgres
SQL_PASSWORD=postgres
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```

Run:
```
docker-compose up -d --build
```
And open http://localhost:8000/


Postman API documentation: https://documenter.getpostman.com/view/16456229/Tzm6kayW

Deployed app on Heroku: https://dry-falls-05090.herokuapp.com/

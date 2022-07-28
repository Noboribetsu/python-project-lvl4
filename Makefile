start:
	poetry run python manage.py runserver 0.0.0.0:8000

migrate:
	poetry run python manage.py migrate

deploy:
	git push heroku main

lint:
	poetry run flake8 .

messages:
	poetry run django-admin makemessages -l ru

compilemessages:
	poetry run django-admin compilemessages 
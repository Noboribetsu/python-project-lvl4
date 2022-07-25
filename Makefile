start:
	poetry run python manage.py runserver 0.0.0.0:8000

migrate:
	poetry run python manage.py migrate

deploy:
	git push heroku main
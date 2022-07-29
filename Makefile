start:
	poetry run python manage.py runserver 0.0.0.0:8000

migrate:
	poetry run python manage.py migrate

deploy:
	git push heroku main

lint:
	poetry run flake8 .

test:
	poetry run python manage.py test

test-coverage:
	poetry run coverage run manage.py test task_manager	
	poetry run coverage html
	poetry run coverage report
messages:
	poetry run django-admin makemessages -l ru

compilemessages:
	poetry run django-admin compilemessages 
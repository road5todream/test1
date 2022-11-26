run:
	poetry run python manage.py runserver

messages:
	poetry run django-admin makemessages -l ru

compile:
	poetry run django-admin compilemessages

migrate:
	poetry run python manage.py migrate

makemigrate:
	poetry run ./manage.py makemigrations

shell:
	poetry run python manage.py shell

test:
	poetry run ./manage.py test

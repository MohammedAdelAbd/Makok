.PHONY: install
install:
	poetry install

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: makemigrations
makemigrations:
	poetry run python manage.py makemigrations

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: run-server
run-server:
	poetry run python manage.py runserver

.PHONY: superuser
superuser:
	poetry run python manage.py createsuperuser

.PHONY: update
update: install migrate install-pre-commit;

.PHONY: up-dependencies-only
up-dependencies-only:
	if not exist .env type nul > .env
	docker compose -f docker-compose.dev.yml up --force-recreate db

bootstrap:
	docker build --file docker/local.Dockerfile --pull --tag bot:local .
	docker compose run --rm bot alembic upgrade head

up: bootstrap
	docker compose up

down:
	docker compose down

shell:
	docker compose run --rm bot bash

lint:
	flake8 app
	black --check app

fmt:
	black app
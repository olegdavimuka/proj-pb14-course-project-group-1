bootstrap:
	docker build --file docker/local.Dockerfile --pull --tag bot:local .
	docker compose run --rm bot alembic upgrade head

up: bootstrap
	docker compose up

down:
	docker compose down --volumes

shell:
	docker compose run --rm --remove-orphans --build bot bash

lint:
	docker compose run --rm bot bash ops/lint.sh

fmt:
	docker compose run --rm --volume ./app/:/usr/src/app/app/ bot bash ops/fmt.sh

test:
	docker compose run --rm --volume ./app/:/usr/src/app/app/ bot pytest app/tests/
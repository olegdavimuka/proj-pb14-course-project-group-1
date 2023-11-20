bootstrap:
	docker build --file docker/local.Dockerfile --pull --tag bot:local .

up: bootstrap
	docker compose up

down: 
	docker compose down

shell:
	docker compose run --rm bot bash
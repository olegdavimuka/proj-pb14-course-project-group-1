bootstrap:
	docker build --file docker/local.Dockerfile --pull --tag bot .

up: 
	docker run bot
.PHONY: build start

build:
	docker-compose build bot

start:
	docker-compose run --rm --service-ports bot
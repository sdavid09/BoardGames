build:
	docker build . -t boardgames:latest
	docker build ./config/ -t nginxcustom:latest
clean:
	docker rmi boardgames
deploy:
	docker-compose up -d

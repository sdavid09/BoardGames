build:
	docker build . -t boardgames:latest
	docker build ./config/ -t nginxcustom:latest
clean:
	docker rmi boardgames
	docker rmi nginxcustom
deploy:
	docker-compose up -d

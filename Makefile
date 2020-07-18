build:
	docker build . -t boardgames:latest
	docker build ./config/ -t nginxcustom:latest
clean:
	docker rmi boardgames
	docker rmi nginxcustom
deploy:
	docker-compose up -d
dev:
	python3 -m pipenv run python ./src/Site/manage.py runserver
test:
	python .\src\Site\manage.py test chess -v 2

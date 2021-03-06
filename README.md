# Board Games
Board Games is a web app to play games with friends. 
Supported Games:
* Chess

## Installation
Use the package manager [pipenv](https://pypi.org/project/pipenv/) to install dependencies.

```bash
pipenv install --dev
```
## Build 
```bash
make build
```
## Dev
Run Django Dev Server : ( python manage.py runserver )
```bash
make dev
```
Untrack settings.py
git update-index --assume-unchanged path/to/file
git update-index --no-assume-unchanged path/to/file

## Deploy
Run docker-compose
```bash
make deploy

```
## Tests
```bash
nosetests -v
```
## Contributing
* Shobin David

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.txt)

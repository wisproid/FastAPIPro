# {{cookiecutter.project_slug}}
{{cookiecutter.description}}

# Quick Start
```
cd {{cookiecutter.project_slug}}
```
```
virtualenv .venv --py 310
```
```
source .venv/bin/active
```
```
pip install -e .
```
```
docker compose -f docker-compose-dev.yaml up
```
```
nano .env
```
```

```
```
dotenv run python -m granian --interface asgi iotbe.main:app --host 0.0.0.0 --port 8080 --access-log
```
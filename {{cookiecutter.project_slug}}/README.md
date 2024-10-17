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
openssl rand -hex 32
```
```
nano .env
```
```
DATABASE_URL="postgresql+asyncpg://postgres:postgres@127.0.0.1:5454/{{cookiecutter.project_slug}}"
JWT_SECRET_KEY="<opensslkey>"
JWT_ALGORITHM="HS256"
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=1440
```
```
dotenv run alembic revision --autogenerate
```
```
dotenv run alembic upgrade head
```
```
dotenv run python -m granian --interface asgi {{cookiecutter.project_slug}}.main:app --host 0.0.0.0 --port 8080 --access-log
```
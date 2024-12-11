```
pip3 install cookiecutter
```
```
pip3 install uv
```
```
uv sync
```
--
```
dotenv run alembic revision --autogenerate
```
```
dotenv run alembic upgrade head
```

Get JWT Token
```
dotenv run python script_generate_token.py <username> <type>
```

Generate JWT Secret Key
```
openssl rand -hex 32
```

Create .env file
```
touch .env
```

Enable granian reload on dev
```
uv pip install "granian[reload]"
```

Run on dev
```
docker compose -f docker-compose-dev.yaml up
dotenv run python -m granian --interface asgi {{cookiecutter.project_slug}}.main:app --host 0.0.0.0 --port 8080 --access-log --reload --url-path-prefix /api/v1
```

** Deployment
Replace <project_name> in the github action yaml
```
- name: Define App Name
  run: |
    echo "APP_NAME=<project_name>" >> $GITHUB_ENV
    echo $\{\{ env.APP_NAME \}\}

- name: Define K8S namespace
  run: |
    echo "TARGET_NAMESPACE=<project_name>-dev-ns" >> $GITHUB_ENV
    echo $\{\{ env.TARGET_NAMESPACE \}\}
```

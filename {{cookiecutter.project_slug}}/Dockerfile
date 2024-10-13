FROM python:3.10.15-alpine3.20
ARG PORT=8080
ENV PYHTONUNBUFFERED=1

WORKDIR /app
COPY ./alembic-docker.ini ./alembic.ini
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./dist/*.whl .
RUN pip install *.whl --no-cache-dir

EXPOSE $PORT
ENV PORT=$PORT
CMD ["python", "-m", "granian", "--interface", "asgi", "{{cookiecutter.project_slug}}.main:app", "--host", "0.0.0.0", "--port", "$PORT", "--access-log"]
FROM python:3.12.7-alpine3.20 AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Change the working directory to the `app` directory
WORKDIR /app

# Install dependencies for nuitka
RUN apk update && apk add gcc libc-dev
# Install dependencies for app
RUN uv venv && uv pip install nuitka
COPY pyproject.toml .
COPY uv.lock .
RUN uv sync --frozen --no-install-project --compile-bytecode

# Copy the project into the intermediate image
ADD . .

###########################################################
# Just sync the project
RUN uv sync --frozen --compile-bytecode --no-editable
###########################################################
# OR
############################################################
# # Build project to package
# RUN uv build && uv pip install dist/*.whl
############################################################

FROM python:3.12.7-alpine3.20
WORKDIR /app
COPY --from=builder --chown=app:app /app/.venv /app/.venv
COPY alembic.ini .
COPY migrations ./migrations

EXPOSE 8080
CMD [".venv/bin/python", "-m", "granian", "--interface", "asgi", "{{cookiecutter.project_slug}}.main:app", "--host", "0.0.0.0", "--port", "8080", "--access-log", "--url-path-prefix", "/api/v2"]
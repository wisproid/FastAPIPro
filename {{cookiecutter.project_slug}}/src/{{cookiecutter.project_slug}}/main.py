from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import HTMLResponse, ORJSONResponse
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import pkg_resources

from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

import secrets

from time import time
from datetime import datetime

from {{cookiecutter.project_slug}}.routes import websocket_route
from {{cookiecutter.project_slug}}.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Construct the object
    # object = Object()
    # Load to app state
    # ex. app.states.object
    yield
    # Deconstruct the object
    # ex. await object.close()

version = pkg_resources.require(__package__)[0].version
app = FastAPI(
    title=__package__, 
    version=version, 
    lifespan=lifespan, 
    docs_url=None,
    redoc_url=None,
    openapi_url = None,
)

app.include_router(websocket_route.router)

# ## CORS
# origins = [
#     "*",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get("/", include_in_schema=False)
async def get():
    return HTMLResponse("It's work!")

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """
    This middleware adds a process time header to each API response.
    The value of the header is the time it took to process the request in milliseconds.
    """
    start_time = time()
    response = await call_next(request)
    process_time = round((time() - start_time) * 1000)
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.head("/healthcheck")
@app.get("/healthcheck")
async def get_healthcheck(request: Request):
    return ORJSONResponse(
        content={
            "status": "ok",
            "message": datetime.now().isoformat(),
            "version": version,
        }
    )

security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, settings.DOCS_BASIC_AUTH_USERNAME)
    correct_password = secrets.compare_digest(credentials.password, settings.DOCS_BASIC_AUTH_PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.get("/docs", include_in_schema=False)
async def get_swagger_documentation(_username: str = Depends(get_current_username)):
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


@app.get("/redoc", include_in_schema=False)
async def get_redoc_documentation(_username: str = Depends(get_current_username)):
    return get_redoc_html(openapi_url="/openapi.json", title="docs")


@app.get("/openapi.json", include_in_schema=False)
async def openapi(_username: str = Depends(get_current_username)):
    return get_openapi(title=app.title, version=app.version, routes=app.routes)
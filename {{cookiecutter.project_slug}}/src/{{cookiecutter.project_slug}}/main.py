from fastapi import FastAPI
from fastapi.responses import HTMLResponse, ORJSONResponse
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import pkg_resources

from time import time
from datetime import datetime

from {{cookiecutter.project_slug}}.routes import websocket_serv, gateway_pixii
from {{cookiecutter.project_slug}}.utils.websocket_html_client import html

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
app = FastAPI(title=__package__, version=version, lifespan=lifespan)

app.include_router(websocket_serv.router)

## CORS
origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def get():
    return HTMLResponse(html)

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
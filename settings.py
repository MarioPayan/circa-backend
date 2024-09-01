from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from vars import origins


def config_app(app: FastAPI) -> FastAPI:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["*"],
    )

    return app

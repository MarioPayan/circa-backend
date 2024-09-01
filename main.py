from fastapi import FastAPI
from settings import config_app
from routes import router

app = FastAPI()
app = config_app(app)
app.include_router(router)

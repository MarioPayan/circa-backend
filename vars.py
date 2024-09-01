import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")
origins = os.getenv("ORIGINS").split(",")

base_url = f"{host}:{port}" if port else host

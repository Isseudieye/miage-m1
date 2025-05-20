from fastapi import FastAPI
import os

name = os.getenv('NAME', 'World')

name = "Idy"

app = FastAPI()


@app.get("/")
def read_root():
    return f"Hello {name}! We are learning Docker"

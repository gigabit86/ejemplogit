#Api con FastAPI

from fastapi import FastAPI
from fastapi.responses import FileResponse
from datetime import datetime


app = FastAPI()


@app.get("/hello")
def hello():
    return {"message": "Hello World"}
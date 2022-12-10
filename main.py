from fastapi import FastAPI
from db.database import engine
from db import models

app = FastAPI()


@app.get("/")
def test_the_app():
    return "test is running"

models.Base.metadata.create_all(engine)
from routers import user
from fastapi import FastAPI
from db.database import engine
from db import models

app = FastAPI()
app.include_router(user.router)


@app.get("/")
def test_the_app():
    return "test is running"


models.Base.metadata.create_all(engine)

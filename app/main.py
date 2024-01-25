from fastapi import Depends
from fastapi.responses import HTMLResponse
from app import app
import auth


@app.get("/")
async def root():
    return {"message": "Hello World"}

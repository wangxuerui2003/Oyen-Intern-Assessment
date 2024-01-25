from fastapi import Depends, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from app import app, templates
from typing import Annotated
from auth import User, get_current_user


@app.get("/", response_class=HTMLResponse)
async def index(
    request: Request,
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user is None:
        # User is not authenticated, redirect to the login page
        return RedirectResponse(url="/login")
    return templates.TemplateResponse(
        request=request, name="index.html"
    )


@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse(
        request=request, name="login.html"
    )


@app.post("/logout")
def logout(response: Response):
    response.delete_cookie(key="access_token")
    return {"message": "Logged out"}
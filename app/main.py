from fastapi import FastAPI, Depends, HTTPException, Request, Response, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from auth import ACCESS_TOKEN_EXPIRE_MINUTES, User, authenticate_user, get_current_user, create_access_token
from sqlalchemy.orm import Session
from models import schemas
from models import crud
from models.database import get_db, engine
from models import models
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone


models.Base.metadata.create_all(bind=engine)


# The FastAPI app object
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(
    request: Request,
    current_user: Annotated[User, Depends(get_current_user)]
):
    '''
        This page needs authorization to access
    '''

    if current_user is None:
        # User is not authenticated, redirect to the login page
        return RedirectResponse(url="/login")
    name = current_user.full_name
    if name == '':
        name = current_user.username

    return templates.TemplateResponse(
        request=request, name="index.html", context={'name': name}
    )


@app.get("/login")
async def login(
    request: Request,
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user is not None:
        return RedirectResponse(url="/")
    return templates.TemplateResponse(
        request=request, name="login.html"
    )


@app.post("/logout")
def logout(response: Response):
    response.delete_cookie(key="access_token")
    return {"message": "Logged out"}


@app.get("/register")
async def register_page(
    request: Request,
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user is not None:
        return RedirectResponse(url="/")
    return templates.TemplateResponse(
        request=request, name="register.html"
    )


@app.post("/register", response_model=schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)


@app.post("/token")
def login_for_access_token(
    response: Response,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    # set the cookie to expire in 30 mins
    cookie_exp_time = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    response.set_cookie(
        key="access_token",
        value=f"Bearer {access_token}",
        httponly=True,
        expires=cookie_exp_time,
        max_age=ACCESS_TOKEN_EXPIRE_MINUTES * 60
    )

    return {"message": "Token has been set in the HttpOnly cookie"}

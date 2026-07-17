from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from src.lib.db import get_db
from src.schemas.auth import SignupRequest, SigninRequest, UserResponse, TokenResponse
from src.controllers.auth_controller import signup_user, signin_user

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def signup(user: SignupRequest, db: Session = Depends(get_db)):
    return signup_user(user, db)


@auth_router.post("/signin", response_model=TokenResponse)
def signin(credentials: SigninRequest, response: Response, db: Session = Depends(get_db)):
    return signin_user(credentials, response, db)

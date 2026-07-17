from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session

from src.lib.Models.user import UserInfo
from src.lib.security import hash_password, verify_password, create_access_token
from src.schemas.auth import SignupRequest, SigninRequest, UserResponse, TokenResponse


def signup_user(user: SignupRequest, db: Session):
    existing_user = db.query(UserInfo).filter(UserInfo.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists",
        )

    new_user = UserInfo(
        name=user.name,
        email=user.email,
        password_hash=hash_password(user.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def signin_user(credentials: SigninRequest, response: Response, db: Session):
    user = db.query(UserInfo).filter(UserInfo.email == credentials.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    if not verify_password(credentials.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    access_token = create_access_token(data={"sub": user.email, "user_id": user.id})

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        samesite="lax",
        secure=False,
        max_age=3600,
    )

    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse(id=user.id, name=user.name, email=user.email),
    )
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from src.lib.db import get_db
from src.lib.Models.user import UserInfo
from src.lib.security import hash_password, verify_password, create_access_token
from src.schemas.auth import SignupRequest, SigninRequest, UserResponse, TokenResponse

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def signup(user: SignupRequest, db: Session = Depends(get_db)):
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


@auth_router.post("/signin", response_model=TokenResponse)
def signin(credentials: SigninRequest, response: Response, db: Session = Depends(get_db)):
    # 1. Look up user
    user = db.query(UserInfo).filter(UserInfo.email == credentials.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    # 2. Verify password
    if not verify_password(credentials.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    # 3. Create JWT token
    access_token = create_access_token(data={"sub": user.email, "user_id": user.id})

    # 4. Set token in httpOnly cookie (not accessible via JS — more secure)
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,       # prevents JS access
        samesite="lax",      # CSRF protection
        secure=False,        # set True in production (HTTPS only)
        max_age=3600,        # 1 hour in seconds
    )

    # 5. Also return token in response body for API clients
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse(id=user.id, name=user.name, email=user.email),
    )

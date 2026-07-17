from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from src.lib.db import Base, engine
from src.lib.Models.user import UserInfo  # ensures model is registered with Base
from src.routes.auth_routes import auth_router

# Create all tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "FastAPI is running 🚀"}

@app.get("/test-db")
def test_db():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "Database Connected Successfully ✅"}
    except Exception as e:
        return {"status": "Connection Failed ❌", "error": str(e)}
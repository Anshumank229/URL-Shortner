from fastapi import FastAPI
from app.core.config import settings
from app.core.database import engine, Base
from app.auth import router as auth_router
from app.models import User, ShortURL, Click

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": f"Welcome to {settings.APP_NAME}", "status": "running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

from fastapi import FastAPI,Depends,HTTPException
from core.config import APP_NAME
from sqlalchemy.orm import Session
from sqlalchemy import text
from database.session import get_db
from sqlalchemy.exc import SQLAlchemyError
import logging

logger = logging.getLogger(__name__)

app = FastAPI(title=APP_NAME)

@app.get("/")
def health():
    return  {"status": 200,"msg": "Welcome to DocuVault"}

@app.get("/health/db")
def dbHealth(db: Session =Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected"
        }

    except SQLAlchemyError as e:
        logger.exception("Database connectivity issue")
        raise HTTPException(status_code=503, detail="Database connection problem")
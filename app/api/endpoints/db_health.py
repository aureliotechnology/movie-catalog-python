from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import text  # Certifique-se de importar corretamente
from app.db.database import get_db

router = APIRouter()

@router.get("/db-health", tags=["Health Check"])
def database_health_check(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1"))  # Correção Garantida
        if result.scalar():  # Verifica se o banco respondeu corretamente
            return {"status": "ok", "message": "Database is connected"}
        return {"status": "error", "message": "No response from database"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

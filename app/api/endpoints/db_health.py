from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db

router = APIRouter()

@router.get("/db-health", tags=["Health Check"])
def database_health_check(db: Session = Depends(get_db)):
    try:
        db.execute("SELECT 1")  # Executa uma consulta simples
        return {"status": "ok", "message": "Database is connected"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

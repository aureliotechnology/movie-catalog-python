from fastapi import FastAPI
import sys
sys.path.append("/app")

from app.api.endpoints import health, db_health

app = FastAPI(title="Movie Catalog API", version="1.0.0")

# Registrar os health-checks
app.include_router(health.router, prefix="/api")
app.include_router(db_health.router, prefix="/api")

@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to Movie Catalog API"}

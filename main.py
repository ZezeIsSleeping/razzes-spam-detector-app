from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy import text
from config import engine
from app.routers.predictspam_router import (router as predictspam_router)
from app.routers.web_router import router as web_router

app = FastAPI(
    title="Intelligent Text Analysis System",
    description=(
        "Sistem analisis teks SMS untuk "
        "klasifikasi ham dan spam"
        ),
    version="1.0.0"
)

# Mengaktifkan file CSS dan aset statis
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# Router API untuk prediksi dan CRUD
app.include_router(predictspam_router)

# Router halaman web
app.include_router(web_router)

@app.get("/health/database")
def check_database():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {
            "status": "success",
            "message": "Koneksi PostgreSQL berhasil"
        }
    except Exception:
        return {
        "status": "error",
        "message": "Koneksi PostgreSQL gagal"
        }
from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

from database import Base, engine, SessionLocal
from models import Job
from schemas import CertificateRequest
from certificate_generator import generate_certificate

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bulk Certificate Generator API")
os.makedirs("certificates", exist_ok=True)

@app.get("/")
def home():
    return {"message": "Bulk Certificate Generator API"}

@app.post("/generate")
def generate_certificates(data: CertificateRequest):
    db = SessionLocal()
    job = Job(status="processing")
    db.add(job)
    db.commit()
    db.refresh(job)

    generated_files = []
    for recipient in data.recipients:
        filename = recipient.name.replace(" ", "_") + ".pdf"
        filepath = f"certificates/{filename}"
        generate_certificate(recipient.name, recipient.course, filepath)
        generated_files.append(filename)

    job.status = "completed"
    db.commit()

    return {"job_id": job.id, "status": job.status, "files": generated_files}

@app.get("/status/{job_id}")
def check_status(job_id: int):
    db = SessionLocal()
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        return {"message": "Job not found"}
    return {"job_id": job.id, "status": job.status}

@app.get("/download/{filename}")
def download_certificate(filename: str):
    filepath = f"certificates/{filename}"
    if os.path.exists(filepath):
        return FileResponse(filepath, media_type="application/pdf", filename=filename)
    return {"message": "File not found"}

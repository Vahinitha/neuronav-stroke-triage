import os
import uuid
import datetime
from typing import Optional
from fastapi import FastAPI, UploadFile, File, Form, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv

load_dotenv()

from schemas import (
    StrokeTriageResult,
    Hospital,
    HospitalAlertRequest,
    HospitalAlertResponse,
    MedicalRecordAnalysisResult
)
from presets import CLINICAL_PRESETS
from gemini_service import GeminiTriageService
from maps_service import MapsService

app = FastAPI(
    title="NeuroNav: Stroke & Neurological Triage Assistant",
    description="Emergency pre-hospital stroke triage assistant powered by Google Gemini multimodal video/audio parsing.",
    version="1.0.0"
)

# Enable CORS for local Vite development server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory store for hospital alerts (simulating hospital CT bay booking system)
ACTIVE_HOSPITAL_ALERTS = []

@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "NeuroNav Emergency Neurological Triage Engine",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "gemini_ready": bool(os.getenv("GEMINI_API_KEY")),
        "google_maps_ready": bool(os.getenv("GOOGLE_MAPS_API_KEY"))
    }

@app.get("/api/presets")
async def get_presets():
    """Returns available clinical test presets for 1-click verification."""
    return CLINICAL_PRESETS

@app.get("/api/hospitals")
async def get_hospitals(
    lat: Optional[float] = 37.7749,
    lng: Optional[float] = -122.4194,
    requires_thrombectomy: bool = False,
    x_maps_key: Optional[str] = Header(None)
):
    """Returns nearest Comprehensive Stroke Centers (CSC) and Primary Stroke Centers (PSC)."""
    maps_service = MapsService(api_key=x_maps_key)
    hospitals = await maps_service.get_nearby_stroke_centers(
        lat=lat,
        lng=lng,
        requires_thrombectomy=requires_thrombectomy
    )
    return hospitals

@app.post("/api/triage", response_model=StrokeTriageResult)
async def perform_triage(
    video: Optional[UploadFile] = File(None),
    audio: Optional[UploadFile] = File(None),
    bystander_text: Optional[str] = Form(None),
    last_known_well_minutes: Optional[int] = Form(None),
    patient_age: Optional[int] = Form(None),
    patient_gender: Optional[str] = Form(None),
    preset_id: Optional[str] = Form(None),
    api_key: Optional[str] = Form(None),
    x_gemini_key: Optional[str] = Header(None)
):
    """
    Multimodal stroke triage endpoint.
    Processes video of facial asymmetry, audio of speech slurring, and bystander text against BE-FAST.
    """
    key_to_use = api_key or x_gemini_key or os.getenv("GEMINI_API_KEY")
    triage_service = GeminiTriageService(api_key=key_to_use)

    video_bytes = None
    video_mime = None
    if video:
        video_bytes = await video.read()
        video_mime = video.content_type or "video/mp4"

    audio_bytes = None
    audio_mime = None
    if audio:
        audio_bytes = await audio.read()
        audio_mime = audio.content_type or "audio/wav"

    result = await triage_service.analyze_multimodal(
        video_bytes=video_bytes,
        video_mime=video_mime,
        audio_bytes=audio_bytes,
        audio_mime=audio_mime,
        bystander_text=bystander_text,
        last_known_well_minutes=last_known_well_minutes,
        patient_age=patient_age,
        patient_gender=patient_gender,
        preset_id=preset_id
    )

    return result

@app.post("/api/analyze-medical-record", response_model=MedicalRecordAnalysisResult)
async def analyze_medical_record(
    file: Optional[UploadFile] = File(None),
    chronic_notes: Optional[str] = Form(None),
    patient_age: Optional[int] = Form(None),
    patient_gender: Optional[str] = Form(None),
    api_key: Optional[str] = Form(None),
    x_gemini_key: Optional[str] = Header(None)
):
    """
    Analyzes uploaded medical files (discharge notes, MRI/CT reports, prescriptions)
    and patient chronic history for long-term neurological suffering.
    Returns diagnostic summary, actionable advice, critical precautions, and prescriptions.
    """
    key_to_use = api_key or x_gemini_key or os.getenv("GEMINI_API_KEY")
    triage_service = GeminiTriageService(api_key=key_to_use)

    file_bytes = None
    file_mime = None
    file_name = None
    if file:
        file_bytes = await file.read()
        file_mime = file.content_type or "application/pdf"
        file_name = file.filename

    result = await triage_service.analyze_medical_record(
        file_bytes=file_bytes,
        file_mime=file_mime,
        file_name=file_name,
        chronic_notes=chronic_notes,
        patient_age=patient_age,
        patient_gender=patient_gender
    )
    return result

@app.post("/api/hospital-alert", response_model=HospitalAlertResponse)
async def alert_hospital(payload: HospitalAlertRequest):
    """
    Pre-arrival Code Stroke hospital dispatch and CT scanner reservation.
    Simulates direct emergency department / CT scanner pre-notification.
    """
    alert_id = f"ALERT-CS-{uuid.uuid4().hex[:6].upper()}"
    ct_suite = "CT Suite 2 (Emergency Dedicated Gantry)" if payload.lvo_risk == "HIGH" else "CT Suite 1"

    instructions = [
        "Patient en route via EMS priority 1 with pre-arrival BE-FAST protocol assessment.",
        f"CT Scanner pre-cleared for non-contrast brain CT + CT Angiography (CTA head/neck).",
        "Stroke Neurology attending and interventional radiology fellowship alerted.",
        "Door-to-CT target: < 15 minutes; Door-to-Needle target: < 45 minutes.",
        "IV line primed for intravenous thrombolysis (tPA / Tenecteplase) if hemorrhagic etiology excluded."
    ]

    response_record = HospitalAlertResponse(
        alert_id=alert_id,
        status="CONFIRMED_CT_PREPPED",
        hospital_name=payload.hospital_id,
        ct_suite_assigned=ct_suite,
        neurology_team_alerted=True,
        door_to_ct_target_minutes=12,
        confirmation_timestamp=datetime.datetime.utcnow().isoformat() + "Z",
        hospital_instructions=instructions
    )

    ACTIVE_HOSPITAL_ALERTS.insert(0, {
        "alert": response_record.model_dump(),
        "payload": payload.model_dump()
    })

    return response_record

@app.get("/api/hospital-alerts/active")
async def get_active_alerts():
    """Returns currently active pre-arrival stroke alerts for the hospital ER console view."""
    return ACTIVE_HOSPITAL_ALERTS

# Serve frontend build if dist folder exists (for containerized Cloud Run deployment)
frontend_dist_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend", "dist"))
if os.path.isdir(frontend_dist_path):
    app.mount("/assets", StaticFiles(directory=os.path.join(frontend_dist_path, "assets")), name="assets")

    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str):
        index_file = os.path.join(frontend_dist_path, "index.html")
        file_path = os.path.join(frontend_dist_path, full_path)
        if full_path and os.path.isfile(file_path):
            return FileResponse(file_path)
        return FileResponse(index_file)

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)

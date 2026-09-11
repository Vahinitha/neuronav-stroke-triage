from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class BEFASTItem(BaseModel):
    item: str = Field(..., description="B (Balance), E (Eyes), F (Face), A (Arms), S (Speech), or T (Time)")
    name: str = Field(..., description="Full clinical protocol name, e.g., 'Facial Droop / Asymmetry'")
    detected: bool = Field(..., description="Whether acute neurological deficit is detected")
    severity: str = Field(..., description="NORMAL, MILD, MODERATE, or SEVERE")
    confidence: float = Field(..., description="Confidence score from 0.0 to 1.0")
    clinical_findings: str = Field(..., description="Detailed clinical observation from multimodal parser")
    landmark_indicators: List[str] = Field(default_factory=list, description="Specific visual or acoustic landmarks")

class ForeheadSparingAnalysis(BaseModel):
    pattern: str = Field(..., description="CENTRAL_UMN_STROKE, PERIPHERAL_LMN_BELLS_PALSY, or SYMMETRICAL_NORMAL")
    forehead_wrinkles_spared: bool = Field(..., description="True if bilateral forehead wrinkling / eyebrow raise is preserved (characteristic of cortical stroke due to bilateral innervation); False if upper face is paralyzed (Bell's palsy)")
    eyebrow_elevation_symmetry_percent: int = Field(default=95, description="Symmetry percentage of upper facial movement (0-100)")
    clinical_explanation: str = Field(..., description="Pathophysiological differentiation between central cortical stroke and peripheral Bell's palsy")
    differential_recommendation: str = Field(..., description="Actionable recommendation based on forehead sparing finding")

class HypoglycemiaAlert(BaseModel):
    alert_triggered: bool = Field(default=True, description="Always highlighted as hypoglycemia is the #1 stroke mimic")
    prompt_message: str = Field(default="If a glucometer is available, check blood sugar immediately before transport.", description="Audio/visual prompt message")
    target_range: str = Field(default="70-140 mg/dL (Urgent intervention if < 60 mg/dL / 3.3 mmol/L)", description="Normal clinical glucose range")
    action_if_low: str = Field(default="If blood glucose < 60 mg/dL and patient is conscious, administer fast-acting oral glucose / juice. If drowsy, await EMS for IV Dextrose.", description="Action protocol")

class PupilGazeAnalysis(BaseModel):
    anisocoria_detected: bool = Field(..., description="True if pupils are unequal (potential sign of intracranial hemorrhage / herniation)")
    gaze_deviation_detected: bool = Field(..., description="True if forced conjugate gaze deviation is observed")
    hemorrhage_risk_flag: bool = Field(..., description="True if pupillary/gaze signs strongly suggest hemorrhage over ischemia")
    clinical_note: str = Field(..., description="Explanation of the pupillary and oculomotor findings")

class HospitalRouting(BaseModel):
    recommended_center_type: str = Field(..., description="COMPREHENSIVE_STROKE_CENTER (CSC) or PRIMARY_STROKE_CENTER (PSC)")
    psc_eta_mins: int = Field(..., description="Estimated travel time to nearest Primary Stroke Center")
    csc_eta_mins: int = Field(..., description="Estimated travel time to nearest Comprehensive Stroke Center")
    routing_rationale: str = Field(..., description="Explanation of why CSC vs PSC was chosen based on LVO risk and transport times")

class StrokeTriageResult(BaseModel):
    triage_id: str = Field(..., description="Unique triage session ID")
    timestamp: str = Field(..., description="ISO 8601 timestamp")
    overall_score: int = Field(..., description="BE-FAST score from 0 to 6 (higher indicates higher acute stroke probability)")
    nihss_estimated_score: Optional[int] = Field(default=None, description="Pre-hospital estimated National Institutes of Health Stroke Scale (NIHSS) score from 0 to 42")
    triage_tier: str = Field(..., description="CRITICAL_CODE_STROKE, URGENT_EVALUATION, or LOW_RISK_MONITOR")
    stroke_probability_percent: int = Field(..., description="Calculated stroke probability percentage (0-100)")
    lvo_risk: str = Field(..., description="Large Vessel Occlusion risk: HIGH, MODERATE, or LOW")
    primary_suspected_condition: str = Field(..., description="Primary suspected diagnosis (e.g., Acute Ischemic Stroke - MCA territory)")
    differential_diagnoses: List[str] = Field(default_factory=list, description="Differential diagnoses (e.g., Hemorrhagic Stroke, TIA, Bell's Palsy, Todd's Paresis)")
    time_window_status: str = Field(..., description="Within tPA window (<=4.5h), Thrombectomy window (<=24h), or Unknown/Extended")
    last_known_well_minutes_ago: Optional[int] = Field(None, description="Minutes elapsed since patient was last seen normal")
    befast_breakdown: List[BEFASTItem] = Field(..., description="Detailed breakdown across all 6 BE-FAST parameters")
    forehead_sparing: ForeheadSparingAnalysis = Field(..., description="Forehead-sparing analysis differentiating Bell's palsy vs Central stroke")
    pupil_gaze_analysis: Optional[PupilGazeAnalysis] = Field(default=None, description="Analysis of pupillary symmetry and gaze deviation for hemorrhage risk")
    hypoglycemia_alert: HypoglycemiaAlert = Field(default_factory=HypoglycemiaAlert, description="Hypoglycemia stroke mimic prompt")
    critical_advisories: List[str] = Field(default_factory=list, description="Urgent medical alerts (e.g. DO NOT administer aspirin before CT)")
    sbar_ems_script: Dict[str, str] = Field(..., description="Situation, Background, Assessment, Recommendation format for 911/EMS call")
    bystander_stabilization_steps: List[str] = Field(default_factory=list, description="Prioritized step-by-step calming instructions for bystander")
    hospital_routing: Optional[HospitalRouting] = Field(default=None, description="Calculated routing decision between PSC and CSC")
    ems_handoff_link: Optional[str] = Field(default=None, description="Secure shareable URL containing the clinical payload for EMS dispatch")
    recommended_destination: str = Field(..., description="COMPREHENSIVE_STROKE_CENTER (CSC) or PRIMARY_STROKE_CENTER (PSC)")
    ai_engine_used: str = Field(default="Gemini 1.5 Pro Multimodal", description="AI model or simulation engine")

class Hospital(BaseModel):
    id: str
    name: str
    certification: str
    address: str
    distance_miles: float
    drive_time_minutes: int
    ct_scanner_status: str
    thrombectomy_capable: bool
    tpa_ready: bool
    phone: str
    lat: float
    lng: float

class HospitalAlertRequest(BaseModel):
    triage_id: str
    hospital_id: str
    patient_age: Optional[int] = None
    patient_gender: Optional[str] = None
    estimated_arrival_minutes: int
    triage_tier: str
    befast_score: int
    lvo_risk: str
    last_known_well_minutes_ago: Optional[int] = None
    sbar_summary: str

class HospitalAlertResponse(BaseModel):
    alert_id: str
    status: str
    hospital_name: str
    ct_suite_assigned: str
    neurology_team_alerted: bool
    door_to_ct_target_minutes: int
    confirmation_timestamp: str
    hospital_instructions: List[str]

class PrescriptionItem(BaseModel):
    drug_name: str = Field(..., description="Generic & Brand name (e.g. Clopidogrel / Plavix)")
    dosage: str = Field(..., description="Dosage and frequency (e.g. 75 mg orally once daily)")
    class_category: str = Field(..., description="Drug class (e.g. Antiplatelet agent)")
    purpose: str = Field(..., description="Clinical indication in secondary stroke prevention")
    instructions_and_precautions: str = Field(..., description="Key clinical administration instructions & precautions")

class MedicalRecordAnalysisResult(BaseModel):
    analysis_id: str
    timestamp: str
    file_name: Optional[str] = None
    patient_chronic_summary: str = Field(..., description="Clinical summary of patient's chronic condition")
    identified_conditions: List[str] = Field(default_factory=list, description="Extracted chronic conditions and diagnoses")
    diagnostic_findings: List[str] = Field(default_factory=list, description="Key neuroimaging, lab, or clinical findings")
    advices: List[str] = Field(default_factory=list, description="Personalized rehabilitation and lifestyle advice")
    precautions: List[str] = Field(default_factory=list, description="Safety precautions, contraindications, and red-flag alerts")
    prescriptions: List[PrescriptionItem] = Field(default_factory=list, description="Evidence-based secondary prevention medication regimen")
    specialist_recommendations: List[str] = Field(default_factory=list, description="Follow-up specialty recommendations")
    disclaimer: str = Field(
        default="AI Clinical Advisory Support: This analysis is for educational and clinical decision-support purposes. All medications and dosages must be reviewed and prescribed by the patient's attending physician.",
        description="Clinical safety disclaimer"
    )

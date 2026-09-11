from typing import List, Dict, Any

CLINICAL_PRESETS: List[Dict[str, Any]] = [
    {
        "id": "acute_mca_stroke",
        "title": "Severe Acute Stroke (Right Hemiplegia & Aphasia)",
        "subtitle": "58-year-old male, sudden onset 25 mins ago, severe facial droop and speech slurring",
        "badge": "CODE STROKE - HIGH LVO RISK",
        "badge_color": "red",
        "patient": {
            "age": 58,
            "gender": "Male",
            "last_known_well_minutes": 25,
            "medical_history": "Hypertension, Atrial Fibrillation"
        },
        "bystander_description": "We were eating lunch together and he suddenly dropped his fork from his right hand. When I asked what happened, his speech was completely garbled, and the right side of his face slumped down. He can barely raise his right arm.",
        "sample_video_description": "5-second clip: Patient attempts to smile and raise eyebrows. Bilateral forehead wrinkling is preserved with symmetrical eyebrow elevation. Right oral commissure severely drooping. Upper face spared (Upper Motor Neuron Central Stroke pattern).",
        "sample_audio_transcript": "Patient attempts repeat phrase 'You can't teach an old dog new tricks' -> Severe dysarthria and expressive aphasia.",
        "simulated_triage": {
            "overall_score": 5,
            "triage_tier": "CRITICAL_CODE_STROKE",
            "stroke_probability_percent": 94,
            "lvo_risk": "HIGH",
            "primary_suspected_condition": "Acute Ischemic Stroke (Left MCA Stem Territory)",
            "differential_diagnoses": [
                "Intracerebral Hemorrhage (Left Basal Ganglia)",
                "Acute Ischemic Stroke with Large Vessel Occlusion (LVO)",
                "Hypoglycemic Hemiparesis (Rule out via immediate finger-stick glucose)"
            ],
            "time_window_status": "Golden Hour - Within IV tPA Window (<=4.5h) & EVT Thrombectomy Window (<=24h)",
            "last_known_well_minutes_ago": 25,
            "forehead_sparing": {
                "pattern": "CENTRAL_UMN_STROKE",
                "forehead_wrinkles_spared": True,
                "eyebrow_elevation_symmetry_percent": 94,
                "clinical_explanation": "Central Upper Motor Neuron (UMN) pattern: Bilateral cortico-bulbar innervation to frontalis muscle preserves bilateral eyebrow elevation and forehead wrinkling, while lower face exhibits marked unilateral droop. This confirms acute cortical stroke and firmly rules out peripheral Bell's palsy.",
                "differential_recommendation": "Bell's Palsy ruled out. Non-contrast head CT and emergent CTA required immediately for Large Vessel Occlusion (LVO)."
            },
            "hypoglycemia_alert": {
                "alert_triggered": True,
                "prompt_message": "If a glucometer is available, check blood sugar immediately before transport.",
                "target_range": "70-140 mg/dL (Urgent intervention if < 60 mg/dL / 3.3 mmol/L)",
                "action_if_low": "Severe hypoglycemia is the #1 stroke mimic. If blood sugar < 60 mg/dL and patient is conscious, administer fast-acting glucose immediately. If altered, await EMS for IV Dextrose."
            },
            "befast_breakdown": [
                {
                    "item": "B",
                    "name": "Balance & Coordination",
                    "detected": True,
                    "severity": "MODERATE",
                    "confidence": 0.88,
                    "clinical_findings": "Acute unsteadiness and inability to maintain upright seated trunk stability, leaning toward affected right side.",
                    "landmark_indicators": ["Truncal instability", "Rightward lateral lean", "Loss of postural equilibrium"]
                },
                {
                    "item": "E",
                    "name": "Eyes & Vision",
                    "detected": True,
                    "severity": "MILD",
                    "confidence": 0.82,
                    "clinical_findings": "Subtle left conjugate gaze preference observed, consistent with hemispheric cortical lesion.",
                    "landmark_indicators": ["Conjugate horizontal gaze preference to the left", "Sluggish pupillary saccades"]
                },
                {
                    "item": "F",
                    "name": "Facial Droop / Symmetry",
                    "detected": True,
                    "severity": "SEVERE",
                    "confidence": 0.98,
                    "clinical_findings": "Profound right-sided lower facial droop. Forehead wrinkles bilaterally spared on eyebrow raise (Upper Motor Neuron Central Stroke pattern).",
                    "landmark_indicators": ["Right oral commissure depression -8.2mm", "Forehead wrinkling spared (Central UMN)", "Bell's palsy excluded"]
                },
                {
                    "item": "A",
                    "name": "Arm Drift & Motor Power",
                    "detected": True,
                    "severity": "SEVERE",
                    "confidence": 0.95,
                    "clinical_findings": "Rapid right arm pronation and downward drift within 3 seconds of elevation. Left arm maintains stable posture against gravity.",
                    "landmark_indicators": ["Right arm pronator drift > 45°", "Inability to maintain 90° shoulder flexion", "Unilateral motor asymmetry"]
                },
                {
                    "item": "S",
                    "name": "Speech & Language",
                    "detected": True,
                    "severity": "SEVERE",
                    "confidence": 0.96,
                    "clinical_findings": "Marked expressive dysphasia and heavy dysarthria. Incomplete articulation of target sentence with phonemic distortion and reduced acoustic velocity.",
                    "landmark_indicators": ["Speech rate reduced to 42 WPM", "Severe consonant slurring / lingual deficit", "Expressive language struggle"]
                },
                {
                    "item": "T",
                    "name": "Time / Last Known Well",
                    "detected": True,
                    "severity": "CRITICAL",
                    "confidence": 0.99,
                    "clinical_findings": "Onset witnessed 25 minutes ago. Patient is in the hyper-acute 'Golden Hour' phase. Immediate reperfusion therapy eligible pending emergency non-contrast head CT.",
                    "landmark_indicators": ["LKW: 25 mins ago", "Window: < 4.5 hrs (tPA / Tenecteplase eligible)", "Window: < 24 hrs (Endovascular thrombectomy eligible)"]
                }
            ],
            "critical_advisories": [
                "HYPOGLYCEMIA CHECK: If a glucometer is available, check blood sugar immediately before transport (severe hypoglycemia is the #1 stroke mimic).",
                "ABSOLUTE CONTRAINDICATION: DO NOT administer aspirin, NSAIDs, or oral blood thinners until non-contrast head CT excludes intracerebral hemorrhage!",
                "ASPIRATION RISK: Keep strictly NPO (nothing by mouth) - NO water, food, or medication due to impaired swallow reflex.",
                "PATIENT POSITIONING: Keep head elevated 30 degrees unless hypotensive; if vomiting occurs, place immediately into left lateral recovery position.",
                "TIME CAPTURE: Confirm exact time as Last Known Well with EMS arriving team."
            ],
            "sbar_ems_script": {
                "situation": "Code Stroke priority call: 58-year-old male with acute right hemiparesis, severe lower facial droop with forehead sparing, and expressive aphasia.",
                "background": "Onset witnessed 25 minutes ago. History of hypertension and AFib. Forehead wrinkling spared (Bell's palsy ruled out).",
                "assessment": "NeuroNav BE-FAST Score is 5/6 with HIGH risk of Large Vessel Occlusion (LVO). Within 4.5h tPA and 24h thrombectomy windows. Rule out hypoglycemia mimic via finger-stick.",
                "recommendation": "Dispatch EMS priority 1 ALS unit with pre-notification to nearest Comprehensive Stroke Center for direct CT scanner room bypass."
            },
            "bystander_stabilization_steps": [
                "1. If a glucometer is available, check blood sugar immediately before transport (severe low blood sugar mimics a stroke).",
                "2. Keep the patient lying down with their head slightly elevated on a low pillow (about 30 degrees). Keep them calm and warm.",
                "3. DO NOT give them any water, juice, food, or pills. Swallowing muscles may be paralyzed and fluid can choke their lungs.",
                "4. DO NOT give aspirin! If this is a bleeding stroke, aspirin can cause catastrophic hemorrhaging.",
                "5. If the patient feels sick or begins to vomit, turn their entire body onto their left side (recovery position) to keep the airway clear.",
                "6. Unlock the front door, turn on outdoor lights, secure any pets, and gather the patient's prescription pill bottles ready for the paramedics."
            ],
            "recommended_destination": "COMPREHENSIVE_STROKE_CENTER"
        }
    },
    {
        "id": "bells_palsy_mimic",
        "title": "Isolated Peripheral Facial Palsy (Bell's Palsy Mimic)",
        "subtitle": "42-year-old female, woke up with right facial weakness including inability to wrinkle forehead or close eye",
        "badge": "STROKE MIMIC - PERIPHERAL BELL'S PALSY",
        "badge_color": "emerald",
        "patient": {
            "age": 42,
            "gender": "Female",
            "last_known_well_minutes": 180,
            "medical_history": "Recent viral upper respiratory infection"
        },
        "bystander_description": "She woke up this morning and noticed her right eye wouldn't close completely, and her right forehead has no wrinkles. Her arms and legs are completely normal, she has no confusion, and she speaks clearly.",
        "sample_video_description": "5-second clip: Patient attempts full facial expressions. Right eye fails to close (lagophthalmos). Right forehead wrinkles absent on eyebrow raise. Complete peripheral 7th cranial nerve paralysis pattern.",
        "sample_audio_transcript": "Patient repeats phrase cleanly: 'You can't teach an old dog new tricks.' Phonation and cadence normal.",
        "simulated_triage": {
            "overall_score": 1,
            "triage_tier": "LOW_RISK_MONITOR",
            "stroke_probability_percent": 12,
            "lvo_risk": "LOW",
            "primary_suspected_condition": "Idiopathic Peripheral Facial Nerve Palsy (Bell's Palsy Mimic)",
            "differential_diagnoses": [
                "Bell's Palsy (Cranial Nerve VII Lower Motor Neuron Lesion)",
                "Ramsay Hunt Syndrome",
                "Stroke Mimic (Central cortical stroke ruled out by total frontalis forehead involvement)"
            ],
            "time_window_status": "Subacute (Noted on waking)",
            "last_known_well_minutes_ago": 180,
            "forehead_sparing": {
                "pattern": "PERIPHERAL_LMN_BELLS_PALSY",
                "forehead_wrinkles_spared": False,
                "eyebrow_elevation_symmetry_percent": 18,
                "clinical_explanation": "Peripheral Lower Motor Neuron (LMN) pattern: Total unilateral paralysis of the entire right facial half, including the frontalis muscle (forehead cannot wrinkle) and orbicularis oculi (inability to close eye). Because central cortical strokes spare the forehead, this complete unilateral involvement strongly rules out acute ischemic stroke and confirms a peripheral Bell's palsy mimic.",
                "differential_recommendation": "High probability Bell's palsy stroke mimic. Non-emergent neurological care for eye lubrication, corneal taping, and early oral corticosteroid initiation."
            },
            "hypoglycemia_alert": {
                "alert_triggered": True,
                "prompt_message": "If a glucometer is available, check blood sugar immediately before transport.",
                "target_range": "70-140 mg/dL",
                "action_if_low": "Confirm blood sugar is within normal range to exclude metabolic mimicry."
            },
            "befast_breakdown": [
                {
                    "item": "B",
                    "name": "Balance & Coordination",
                    "detected": False,
                    "severity": "NORMAL",
                    "confidence": 0.95,
                    "clinical_findings": "Normal gait and coordination reported, intact cerebellar signs.",
                    "landmark_indicators": ["Normal stability"]
                },
                {
                    "item": "E",
                    "name": "Eyes & Vision",
                    "detected": True,
                    "severity": "MILD",
                    "confidence": 0.91,
                    "clinical_findings": "Inability to close right eyelid completely (lagophthalmos). Visual acuity intact.",
                    "landmark_indicators": ["Right incomplete eyelid closure", "Bell's phenomenon present"]
                },
                {
                    "item": "F",
                    "name": "Facial Droop / Symmetry",
                    "detected": True,
                    "severity": "MODERATE",
                    "confidence": 0.94,
                    "clinical_findings": "Complete unilateral right facial weakness affecting both UPPER and LOWER facial quadrants (forehead wrinkles abolished). Lower motor neuron pattern diagnostic of peripheral Bell's palsy.",
                    "landmark_indicators": ["Right frontalis paralysis (forehead paralyzed)", "Peripheral VII nerve distribution", "Central stroke ruled out"]
                },
                {
                    "item": "A",
                    "name": "Arm Drift & Motor Power",
                    "detected": False,
                    "severity": "NORMAL",
                    "confidence": 0.98,
                    "clinical_findings": "Both arms maintain full antigravity posture symmetrically for > 10 seconds without pronator drift.",
                    "landmark_indicators": ["Symmetrical arm elevation", "No pronation"]
                },
                {
                    "item": "S",
                    "name": "Speech & Language",
                    "detected": False,
                    "severity": "NORMAL",
                    "confidence": 0.97,
                    "clinical_findings": "Speech is fluent and grammatically correct. Normal vocal inflection and consonant articulation.",
                    "landmark_indicators": ["Clean acoustic spectrogram", "Normal word rate"]
                },
                {
                    "item": "T",
                    "name": "Time / Last Known Well",
                    "detected": False,
                    "severity": "NORMAL",
                    "confidence": 0.92,
                    "clinical_findings": "Onset upon waking. Non-emergent stroke window; outpatient neurological follow-up recommended.",
                    "landmark_indicators": ["Non-emergent stroke window"]
                }
            ],
            "critical_advisories": [
                "FOREHEAD PARALYSIS: Inability to wrinkle the forehead confirms peripheral Bell's palsy rather than a central brain stroke.",
                "CORNEAL PROTECTION: Protect the open eye with lubricating artificial tears and an eye patch to prevent corneal ulceration.",
                "HYPOGLYCEMIA EXCLUSION: If a glucometer is available, check blood sugar immediately before transport."
            ],
            "sbar_ems_script": {
                "situation": "Stroke Mimic evaluation: 42-year-old female presenting with acute right peripheral facial weakness.",
                "background": "Noticed upon waking today. Forehead wrinkling is completely absent (characteristic of Cranial Nerve VII Bell's palsy). No limb or speech deficit.",
                "assessment": "Findings characteristic of peripheral Bell's Palsy (LMN). Low likelihood of acute cortical stroke.",
                "recommendation": "Urgent Care or Outpatient Neurological evaluation for clinical confirmation and corneal care."
            },
            "bystander_stabilization_steps": [
                "1. If a glucometer is available, check blood sugar immediately before transport.",
                "2. Reassure the individual: Involvement of the forehead wrinkling strongly suggests a peripheral nerve issue (Bell's palsy) rather than a stroke.",
                "3. Protect the right eye: Apply lubricating artificial eye drops and tape the eye closed gently during sleep if needed.",
                "4. Contact your primary care clinic or urgent care center today for prompt prescription medical evaluation."
            ],
            "recommended_destination": "PRIMARY_STROKE_CENTER"
        }
    },
    {
        "id": "tia_mild_deficit",
        "title": "Suspected TIA / Acute Minor Neurological Event",
        "subtitle": "64-year-old female, brief 10-minute episode of right hand weakness and mild word-finding hesitation",
        "badge": "URGENT - TIA / HIGH RECURRENCE RISK",
        "badge_color": "amber",
        "patient": {
            "age": 64,
            "gender": "Female",
            "last_known_well_minutes": 15,
            "medical_history": "Type 2 Diabetes, Hyperlipidemia"
        },
        "bystander_description": "My mother was talking on the telephone and dropped the phone. She said her right arm felt numb like 'pins and needles' and she hesitated when trying to say her grandchildren's names. Her face looks slightly tired on the right side.",
        "sample_video_description": "5-second clip: Patient smiles; subtle flattening of the right nasolabial fold. Symmetrical forehead wrinkling on eyebrow raise.",
        "sample_audio_transcript": "Patient attempts repeat phrase with mild articulation hesitation.",
        "simulated_triage": {
            "overall_score": 2,
            "triage_tier": "URGENT_EVALUATION",
            "stroke_probability_percent": 68,
            "lvo_risk": "MODERATE",
            "primary_suspected_condition": "Transient Ischemic Attack (TIA) vs Minor Acute Ischemic Stroke",
            "differential_diagnoses": [
                "Transient Ischemic Attack (Carotid territory)",
                "Severe Hypoglycemic Mimic (Patient has Type 2 Diabetes)",
                "Minor Lacunar Infarct"
            ],
            "time_window_status": "Acute Onset - Within 15 Minutes (High 48-Hour Stroke Recurrence Window)",
            "last_known_well_minutes_ago": 15,
            "forehead_sparing": {
                "pattern": "CENTRAL_UMN_STROKE",
                "forehead_wrinkles_spared": True,
                "eyebrow_elevation_symmetry_percent": 90,
                "clinical_explanation": "Central pattern: Forehead wrinkling bilaterally intact with subtle lower facial asymmetry. Consistent with vascular TIA.",
                "differential_recommendation": "Rule out hypoglycemia immediately (patient is diabetic). Prompt emergency evaluation for high ABCD2 secondary stroke risk."
            },
            "hypoglycemia_alert": {
                "alert_triggered": True,
                "prompt_message": "If a glucometer is available, check blood sugar immediately before transport.",
                "target_range": "70-140 mg/dL (Critical: Patient is diabetic, rule out neuroglycopenia)",
                "action_if_low": "If blood glucose < 60 mg/dL, treat hypoglycemia immediately as it may fully reverse the symptoms."
            },
            "befast_breakdown": [
                { "item": "B", "name": "Balance", "detected": False, "severity": "NORMAL", "confidence": 0.85, "clinical_findings": "Normal posture.", "landmark_indicators": ["Midline alignment"] },
                { "item": "E", "name": "Eyes", "detected": False, "severity": "NORMAL", "confidence": 0.89, "clinical_findings": "Normal pursuit.", "landmark_indicators": ["Normal gaze"] },
                { "item": "F", "name": "Face", "detected": True, "severity": "MILD", "confidence": 0.79, "clinical_findings": "Mild right nasolabial flattening with preserved forehead wrinkles.", "landmark_indicators": ["Subtle asymmetry", "Forehead spared"] },
                { "item": "A", "name": "Arms", "detected": True, "severity": "MILD", "confidence": 0.81, "clinical_findings": "Mild pronation drift on right upper extremity.", "landmark_indicators": ["Mild pronator drift"] },
                { "item": "S", "name": "Speech", "detected": True, "severity": "MILD", "confidence": 0.78, "clinical_findings": "Minor word-finding hesitation.", "landmark_indicators": ["Latency in verbal initiation"] },
                { "item": "T", "name": "Time", "detected": True, "severity": "URGENT", "confidence": 0.95, "clinical_findings": "Symptoms began 15 mins ago.", "landmark_indicators": ["LKW: 15m ago"] }
            ],
            "critical_advisories": [
                "CHECK BLOOD GLUCOSE: If a glucometer is available, check blood sugar immediately before transport (patient is diabetic).",
                "DO NOT DELAY EVALUATION even if symptoms fluctuate or disappear.",
                "DO NOT DRIVE to the hospital in a personal vehicle."
            ],
            "sbar_ems_script": {
                "situation": "Urgent TIA/Stroke evaluation: 64-year-old diabetic female with fluctuating right arm weakness and mild dysarthria.",
                "background": "Onset 15 minutes ago. History of Type 2 Diabetes. Forehead movement preserved.",
                "assessment": "BE-FAST Score 2/6. Check blood glucose immediately to exclude hypoglycemia mimic.",
                "recommendation": "EMS transport to nearest Primary Stroke Center."
            },
            "bystander_stabilization_steps": [
                "1. If a glucometer is available, check blood sugar immediately before transport.",
                "2. Have the patient sit in a supportive, comfortable armchair.",
                "3. Do not attempt to drive the patient yourself; wait for EMS paramedics.",
                "4. Note down exact start time."
            ],
            "recommended_destination": "PRIMARY_STROKE_CENTER"
        }
    },
    {
        "id": "normal_baseline",
        "title": "Normal Baseline (Healthy Control)",
        "subtitle": "35-year-old male, transient anxiety sensation, fully symmetrical examination",
        "badge": "ALL CLEAR - NORMAL BE-FAST",
        "badge_color": "emerald",
        "patient": {
            "age": 35,
            "gender": "Male",
            "last_known_well_minutes": 5,
            "medical_history": "None"
        },
        "bystander_description": "Felt sudden dizziness after standing up quickly, worried about stroke. Facial expression is normal, speech is completely clear, arms hold up strong.",
        "sample_video_description": "5-second clip: Patient smiles broadly; full symmetrical elevation of bilateral oral commissures, equal nasolabial fold depth, symmetrical forehead furrowing.",
        "sample_audio_transcript": "Crisp phonation, robust acoustic waveform.",
        "simulated_triage": {
            "overall_score": 0,
            "triage_tier": "LOW_RISK_MONITOR",
            "stroke_probability_percent": 2,
            "lvo_risk": "LOW",
            "primary_suspected_condition": "Normal Neurological Assessment (Probable Benign Orthostatic Dizziness / Anxiety)",
            "differential_diagnoses": [
                "Benign Orthostatic Hypotension",
                "Vasovagal response",
                "Hyperventilation"
            ],
            "time_window_status": "No Acute Deficit Detected",
            "last_known_well_minutes_ago": 5,
            "forehead_sparing": {
                "pattern": "SYMMETRICAL_NORMAL",
                "forehead_wrinkles_spared": True,
                "eyebrow_elevation_symmetry_percent": 99,
                "clinical_explanation": "Bilateral symmetrical facial movement across both upper (frontalis) and lower (oral commissure) facial zones. Zero facial droop.",
                "differential_recommendation": "No evidence of Central Stroke or Bell's Palsy."
            },
            "hypoglycemia_alert": {
                "alert_triggered": True,
                "prompt_message": "If a glucometer is available, check blood sugar immediately before transport.",
                "target_range": "70-140 mg/dL",
                "action_if_low": "Ensure patient is hydrated and has normal blood glucose."
            },
            "befast_breakdown": [
                { "item": "B", "name": "Balance", "detected": False, "severity": "NORMAL", "confidence": 0.98, "clinical_findings": "Normal posture.", "landmark_indicators": ["Symmetrical"] },
                { "item": "E", "name": "Eyes", "detected": False, "severity": "NORMAL", "confidence": 0.99, "clinical_findings": "Equal pupils.", "landmark_indicators": ["Normal gaze"] },
                { "item": "F", "name": "Face", "detected": False, "severity": "NORMAL", "confidence": 0.99, "clinical_findings": "Completely symmetrical smile and forehead.", "landmark_indicators": ["Symmetry index 99%"] },
                { "item": "A", "name": "Arms", "detected": False, "severity": "NORMAL", "confidence": 0.99, "clinical_findings": "No pronator drift.", "landmark_indicators": ["Normal strength"] },
                { "item": "S", "name": "Speech", "detected": False, "severity": "NORMAL", "confidence": 0.99, "clinical_findings": "Normal articulation.", "landmark_indicators": ["Clear cadence"] },
                { "item": "T", "name": "Time", "detected": False, "severity": "NORMAL", "confidence": 0.99, "clinical_findings": "No focal acute deficit.", "landmark_indicators": ["Normal baseline"] }
            ],
            "critical_advisories": [
                "No signs of acute stroke detected at this time.",
                "If a glucometer is available, check blood sugar immediately before transport.",
                "If any new numbness or slurring appears, call 911 immediately."
            ],
            "sbar_ems_script": {
                "situation": "Normal baseline neurological screen: 35-year-old male with transient lightheadedness.",
                "background": "No prior conditions.",
                "assessment": "BE-FAST score 0/6. Normal motor and speech.",
                "recommendation": "Hydration, rest, outpatient check if dizziness recurs."
            },
            "bystander_stabilization_steps": [
                "1. If a glucometer is available, check blood sugar immediately before transport.",
                "2. Have the person sit down calmly and drink a glass of water.",
                "3. Rest for 10 minutes until lightheadedness subsides."
            ],
            "recommended_destination": "PRIMARY_STROKE_CENTER"
        }
    }
]

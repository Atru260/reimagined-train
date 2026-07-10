from  datetime import datetime

from pydantic import BaseModel

class Metadata(BaseModel):
    request_id: str
    timestamp: str | datetime
    model_name: str
    processing_time_ms: float
    schema_version: str

class Summary(BaseModel):
    author: str
    subject: str
    brief: str

class Symptom(BaseModel):
    name: str
    severity: str
    status: str
    certainty: str

class Medication(BaseModel):
    name: str
    dose: str
    frequency: str

class Condition(BaseModel):
    name: str
    diagnosis_date: str
    status: str

class Allergy(BaseModel):
    name: str
    severity: str

class LaboratoryValue(BaseModel):
    name: str
    value: str

class Procedure(BaseModel):
    name: str
    date: str

class LifestyleFactor(BaseModel):
    name: str
    status: str


class TemporalInformation(BaseModel):
    onset: str
    duration: str
    progression: str
    timeline_events: list[str]

class Observation(BaseModel):
    finding: str
    evidence: str
    confidence: float

class Uncertainty(BaseModel):
    missing_information: list[str]
    ambiguous_terms: list[str]

class ClinicalEntities(BaseModel):
    symptoms: list[Symptom]
    medications: list[Medication]
    conditions: list[Condition]
    procedures: list[Procedure]
    laboratory_values: list[LaboratoryValue]
    allergies: list[Allergy]
    lifestyle_factors: list[LifestyleFactor]

class AnalysisResponse(BaseModel):
    metadata: Metadata
    summary: Summary
    entities: ClinicalEntities
    temporal_information: TemporalInformation
    observations: list[Observation]
    uncertainty: Uncertainty
    raw_text: str

class AnalysisRequest(BaseModel):
    text: str
from pydantic import BaseModel

from typing import Any, Optional
from src.models.scores import SkillDetails


class ResumeMetrics(BaseModel):
    resume_name: Optional[str] = ""
    skills_matched: float
    skill_details: SkillDetails


class ResumeQueryResult(BaseModel):
    query: str
    answer: str


class MultipleResumeQueryResultData(BaseModel):
    filename: str
    answer: Optional[str] = ""


class MultipleResumeQueryResult(BaseModel):
    query: str
    results: list[MultipleResumeQueryResultData]


class ExtractedSkillsSummary(BaseModel):
    filename: Optional[str] = ""
    skills: list[str]


class MutipleResumeMatchResultData(BaseModel):
    job_description: ExtractedSkillsSummary
    resumes: list[ResumeMetrics]


class CommonResponse(BaseModel):
    success: bool = True
    status_code: int = 200
    message: Optional[str] = ""
    data: Optional[Any]

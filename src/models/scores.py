from pydantic import BaseModel


class SkillDetails(BaseModel):
    # has_required_experience: bool
    skills: list[str]
    matching_skills: list[str]
    # missing_skills: list[str]


class SkillCounts(BaseModel):
    matching_skills_count: int
    # missing_skills_count: int

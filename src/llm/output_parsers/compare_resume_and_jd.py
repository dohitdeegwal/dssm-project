from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from src.llm.prompts.templates.compare_resume_and_jd import (
    present_skills_prompt_text,
    matching_skills_prompt_text,
    missing_skills_prompt_text,
)

candidate_skills_schema = ResponseSchema(
    name="skills",
    description=present_skills_prompt_text,
)

matching_skills_schema = ResponseSchema(
    name="matching_skills",
    description=matching_skills_prompt_text,
)

missing_skills_schema = ResponseSchema(
    name="missing_skills",
    description=missing_skills_prompt_text,
)

skill_matching_respose_schemas = [
    matching_skills_schema,
    missing_skills_schema,
    candidate_skills_schema,
]

output_parser = StructuredOutputParser.from_response_schemas(
    skill_matching_respose_schemas
)

format_instructions = output_parser.get_format_instructions()

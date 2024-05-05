from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser

from src.llm.query_templates.exctract_skills_from_content import (
    extract_skills_promt_text,
)

skills_schema = ResponseSchema(
    name="skills",
    description=extract_skills_promt_text,
)

response_schemas = [skills_schema]

output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

format_instructions = output_parser.get_format_instructions()

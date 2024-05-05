from fastapi import UploadFile
from src.models.responses import ResumeQueryResult
from src.llm.chat.single_resume import query_resume_vector
from src.utils.load_file_content import generate_vectors_from_file_content
from src.llm.query_templates.query_resume import system_template, vector_query_template


from src.llm.output_parsers.query_resume import (
    output_parser,
    format_instructions
)


async def run_query_on_resume_vector(query: str, resume_file: UploadFile):
    docsearch_index = await generate_vectors_from_file_content(
        resume_file=resume_file
    )

    result = await query_resume_vector(
        docsearch_index=docsearch_index,
        response_format_instructions=format_instructions,
        system_template=system_template,
        vector_query_human_template=vector_query_template,
        query=query,
    )

    parsed_result = output_parser.parse(result)

    return ResumeQueryResult(query=query, **parsed_result)

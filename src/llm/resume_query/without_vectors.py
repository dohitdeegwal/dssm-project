from typing import Annotated
from fastapi import Form, UploadFile
from src.models.responses import ResumeQueryResult
from src.llm.chat.single_resume import (
    query_resume_content,
)
from src.utils.load_file_content import (
    get_file_content_from_memory,
)

from src.llm.query_templates.query_resume import (
    human_template_query_with_resume,
    system_template,
)
from src.llm.query_templates.exctract_skills_from_content import (
    human_template
)

from src.llm.output_parsers.query_resume import (
    output_parser,
    format_instructions,
)


async def run_query_on_resume_content(query: str, resume_content: str):

    result = await query_resume_content(
        resume_content=resume_content,
        query_content=query,
        system_template=system_template,
        human_template=human_template_query_with_resume,
        response_format_instructions=format_instructions,
    )

    parsed_result = output_parser.parse(result.content)

    return ResumeQueryResult(query=query, **parsed_result)


async def run_query_on_resume_file(
    query: Annotated[str, Form()], resume_file: UploadFile
):
    resume_content = await get_file_content_from_memory(file=resume_file)
    resume_query_result = await run_query_on_resume_content(
        query=query, resume_content=resume_content
    )

    return resume_query_result

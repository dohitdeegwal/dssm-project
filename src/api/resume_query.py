from typing import Annotated
from fastapi import APIRouter, Form, HTTPException, UploadFile, status

from src.llm.resume_query.multiple_files import (
    run_query_on_multiple_resumes,
)
from src.models.responses import MultipleResumeQueryResult, ResumeQueryResult
from src.llm.resume_query.with_vetcors import (
    run_query_on_resume_vector,
)
from src.llm.resume_query.without_vectors import (
    run_query_on_resume_file,
)
from src.settings import settings
from src.utils.enums import ResumeQueryTypes

router = APIRouter(
    tags=["Query on resumes"],
)


@router.post(
    "/resume-query",
    summary="Run a custom query on provided resume",
    description="""
    `query_type` can either be `with_vectors` or `without_vectors`
    """,
    response_model=ResumeQueryResult,
)
async def query_resume(
    resume_file: UploadFile,
    query: Annotated[str, Form()],
    query_type: ResumeQueryTypes = ResumeQueryTypes.without_vectors,
):
    if query_type == ResumeQueryTypes.with_vectors:
        return await run_query_on_resume_vector(
            query=query, resume_file=resume_file
        )
    else:
        return await run_query_on_resume_file(
            query=query, resume_file=resume_file
        )


@router.post(
    "/resume-query-bulk",
    summary="Run a custom query on multiple resumes",
    response_model=MultipleResumeQueryResult,
)
async def query_multiple_resume(
    query: Annotated[str, Form()],
    resume_files: list[UploadFile],
    query_type: ResumeQueryTypes = ResumeQueryTypes.without_vectors,
):
    if len(resume_files) > settings.MAX_FILES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Number of files is too large",
        )
    return await run_query_on_multiple_resumes(
        query=query, resume_files=resume_files, query_type=query_type
    )

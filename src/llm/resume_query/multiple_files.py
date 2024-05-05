from fastapi import UploadFile
from PyPDF2.errors import EmptyFileError, PdfReadError

from src.llm.resume_query.with_vetcors import (
    run_query_on_resume_vector,
)
from src.llm.resume_query.without_vectors import (
    run_query_on_resume_file,
)
from src.models.responses import (
    MultipleResumeQueryResult,
    MultipleResumeQueryResultData,
    ResumeQueryResult,
)
from src.utils.enums import ResumeQueryTypes


async def run_query_on_multiple_resumes(
    query: str, resume_files: list[UploadFile], query_type: ResumeQueryTypes
):
    results = []
    for resume_file in resume_files:
        try:
            if query_type == ResumeQueryTypes.with_vectors:
                result: ResumeQueryResult = await run_query_on_resume_vector(
                    query=query, resume_file=resume_file
                )
            else:
                result: ResumeQueryResult = await run_query_on_resume_file(
                    query=query, resume_file=resume_file
                )
        except EmptyFileError:
            print(f"Empty file: {resume_file.filename}")
            result.answer = "Empty File"
        except PdfReadError as e:
            print(e)
            result.answer = "Error while reading the PDF"

        results.append(
            MultipleResumeQueryResultData(
                filename=resume_file.filename, answer=result.answer
            )
        )

    return MultipleResumeQueryResult(query=query, results=results)

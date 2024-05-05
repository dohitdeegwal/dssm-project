from typing import Annotated
from fastapi import APIRouter, Form, UploadFile

from src.llm.resume_match.match_resume_list import (
    match_resumes_with_jd_content,
)
from src.models.responses import (
    CommonResponse,
    ExtractedSkillsSummary,
    ResumeMetrics,
    MutipleResumeMatchResultData,
)

# from src.llm.resume_match.match_resume_list import (
#     match_resumes_with_jd,
# )


from src.llm.chat.chat_query import extract_skills
from src.utils.load_file_content import get_file_content_from_memory
from src.utils.common import get_match_rate

router = APIRouter(prefix="/match", tags=["Match resumes to JD"])


@router.post(
    "/resume-jd-file",
    summary="Match a list of resume files against a job description file",
    response_model=CommonResponse,
)
async def match_resume_list_with_jd_file(
    job_description_file: UploadFile, resume_files: list[UploadFile]
):
    """
    Currently we are using chat-gpt3.5 turbo model to extract skills from
    jd & resume and perform match rate on skills

    files accepted  .docx, .pdf
    """

    try:
        jd_file_content = await get_file_content_from_memory(
            file=job_description_file
        )
        result = await match_resumes_with_jd_content(
            jd_content_str=jd_file_content,
            resume_files=resume_files,
            job_description_filename=job_description_file.filename,
        )

    except Exception as e:
        result = CommonResponse(
            success=False, status_code=500, message=str(e), data=None
        )

    return result


@router.post(
    "/resume-jd-str",
    response_model=CommonResponse,
    summary="Match a list of resume files against a job description string",
    response_model_exclude_unset=True,
)
async def match_resume_list_with_jd_content(
    job_description_string: Annotated[str, Form()],
    resume_files: list[UploadFile],
):
    try:
        result = await match_resumes_with_jd_content(
            jd_content_str=job_description_string, resume_files=resume_files
        )

    except Exception as e:
        result = CommonResponse(
            success=False, status_code=500, message=str(e), data=None
        )

    return result

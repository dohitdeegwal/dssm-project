from fastapi import HTTPException, status, UploadFile

from src.llm.chat.chat_query import extract_skills
from src.models.responses import (
    CommonResponse,
    ExtractedSkillsSummary,
    # MutipleResumeMatchResult,
    MutipleResumeMatchResultData,
    ResumeMetrics,
)
from src.utils.common import get_match_rate
from src.utils.load_file_content import get_file_content_from_memory


async def match_resumes_with_jd_content(
    jd_content_str: str,
    resume_files: list[UploadFile],
    job_description_filename: str = "",
):
    jd_parsed_result = await extract_skills(jd_content_str)

    # No skills found in job description
    if not jd_parsed_result["skills"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No skills found in job description",
        )

    if not job_description_filename:
        job_description_skills_summary = ExtractedSkillsSummary(
            skills=jd_parsed_result["skills"],
        )
    else:
        job_description_skills_summary = ExtractedSkillsSummary(
            filename=job_description_filename,
            skills=jd_parsed_result["skills"],
        )

    resume_metrics_list = []
    for resume in resume_files:
        res_file_content = await get_file_content_from_memory(file=resume)
        res_parsed_result = await extract_skills(res_file_content)

        matched = get_match_rate(
            job_skills=jd_parsed_result["skills"],
            resume_skills=res_parsed_result["skills"],
        )

        resume_metric = {
            "resume_name": resume.filename,
            "skills_matched": matched["skills_matched"],
            "skill_details": {
                "skills": res_parsed_result["skills"],
                "matching_skills": matched["matching_skills"],
            },
        }
        resume_metrics_list.append(resume_metric)

    resume_metrics_list = sorted(
        resume_metrics_list,
        key=lambda x: x["skills_matched"],
        reverse=True,
    )

    data = MutipleResumeMatchResultData(
        job_description=job_description_skills_summary,
        resumes=resume_metrics_list,
    )
    result = CommonResponse(data=data)

    return result


# async def match_resumes_with_jd(
#     resume_files: list[UploadFile],
#     job_description_file: UploadFile,
# ):
#     all_resume_results: list[ResumeMetrics] = []

#     jd_skills = await extract_skills_from_file(file=job_description_file)

#     for resume_file in resume_files:

#         resume_skills = await extract_skills_from_file(file=resume_file)

#         current_resume_metrics = await generate_resume_metrics(
#             job_description_content=jd_skills.skills,
#             resume_content=resume_skills.skills,
#         )

#         current_resume_metrics.resume_name = resume_file.filename

#         all_resume_results.append(current_resume_metrics)

#     all_resume_results = sorted(
#         all_resume_results,
#         key=lambda x: x['skills_matched'],
#         reverse=True
#     )

#     data = MutipleResumeMatchResultData(
#         job_description=jd_skills, resumes=all_resume_results
#     )

#     return MutipleResumeMatchResult(data=data)

from fastapi import UploadFile

from src.models.extract_skills import ExtractedSkillsSummary
from src.models.responses import (
    MutipleResumeMatchResult,
    MutipleResumeMatchResultData,
    ResumeMetrics,
)
# from src.llm.services.chat.extract_skills_from_jd import (
#     get_skills_extraction_chat_result,
# )

# from src.llm.prompts.templates.exctract_skills_from_content import (
#     human_template,
#     system_template,
# )
# from src.llm.prompts.output_parsers.extract_skills import (
#     format_instructions,
#     output_parser,
# )
# from src.llm.services.resume_match.score_resume import generate_resume_metrics




# async def match_resumes_with_jd(
#     resume_files: list[UploadFile],
#     job_description_file: UploadFile,
# ):
#     all_resume_results: list[ResumeMetrics] = []

#     jd_skills = await extract_skills(file=job_description_file)

#     for resume_file in resume_files:

#         resume_skills = await extract_skills_from_file(file=resume_file)

#         current_resume_metrics = await generate_resume_metrics(
#             job_description_content=jd_skills.skills,
#             resume_content=resume_skills.skills,
#         )

#         current_resume_metrics.resume_name = resume_file.filename

#         all_resume_results.append(current_resume_metrics)

    

#     data = MutipleResumeMatchResultData(
#         job_description=jd_skills, resumes=all_resume_results
#     )

#     return MutipleResumeMatchResult(data=data)

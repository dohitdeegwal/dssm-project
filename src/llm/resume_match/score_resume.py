from src.models.responses import ResumeMetrics
from src.models.scores import SkillDetails, SkillCounts
from src.llm.services.chat.single_resume import query_resume_content
from src.llm.prompts.templates.compare_resume_and_jd import (
    human_template,
    system_template,
)
from src.llm.prompts.output_parsers.compare_resume_and_jd import (
    format_instructions,
    output_parser,
)


def calculate_resume_score(skill_details: SkillDetails):

    skill_counts = SkillCounts(
        matching_skills_count=len(skill_details.matching_skills),
    )

    matched_skills_count = skill_counts.matching_skills_count

    return matched_skills_count


async def generate_resume_metrics(
    job_description_content: list[str], resume_content: list[str]
):
    result = await query_resume_content(
        resume_content=resume_content,
        query_content=job_description_content,
        system_template=system_template,
        human_template=human_template,
        response_format_instructions=format_instructions,
    )

    parsed_result = output_parser.parse(result.content)

    parsed_skill_details = SkillDetails(**parsed_result)
    matched_skills_count = calculate_resume_score(parsed_skill_details)

    return ResumeMetrics(
        skills_matched=matched_skills_count, skill_details=parsed_skill_details
    )

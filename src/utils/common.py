def get_match_rate(job_skills: list[str], resume_skills: list[str]) -> dict:

    job_skills = {skill.lower() for skill in job_skills}
    resume_skills = {skill.lower() for skill in resume_skills}

    matching_skills = job_skills.intersection(resume_skills)
    skills_matched = (len(matching_skills) / len(job_skills)) * 100

    return {
        "matching_skills": matching_skills,
        "skills_matched": float("{:.2f}".format(skills_matched)),
    }

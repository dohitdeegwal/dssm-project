system_template = """You are an expert in human resources and you are an expert \
    at extracting required skills from the text of a job description or a resume.
    Do not assume a skill if it is not present. We do not want extra skills.
    You may return an empty list if nothing is found in the provided text.
    Never assume any examples of your own, even if nothing sensible is mentioned in the text.
    """

# These prompt texts are also used by the output parser
extract_skills_promt_text = "what are the technical mentioned in the text provided?\
        Output it as a list of strings, if any. Return empty list if no technical skills are mentioned or if the text is just lorem ipsum."


human_template = f"""\
For the following text, extract the following information:
skills: {extract_skills_promt_text}

Be as concise as possible. Consider only technical skills.
Split the muti technology skills into individual technologies, if present.
Return empty list if no skills are mentioned.

Format the output as JSON with the following keys:
skills

"""

human_template += """\
text: {content}

{format_instructions}"""

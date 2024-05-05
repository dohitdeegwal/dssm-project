system_template = "You are an expert in human resources and you are an expert \
    at querying the resume based on given questions, including questions on the work experience, skills and educational qualifications."


base_query_template = """
    Please answer the question based on the provided resume.
    The QUESTION part starts with === 'QUESTION:' === and ends with === 'END QUESTION' ===.

    === 'QUESTION:' ===
    {query_content}
    === 'END QUESTION' ===
"""

formatting_template = """
    Format the result with the following key:
    answer

    Tips: Make sure you answer in the right format. Try to account for abbreviations. For example GCP is equivalent to Google Cloud Platform. Also account for spelling errors You can even break down the skills to match individual technologies mentioned in each skill.

    {format_instructions}
    """

vector_query_template = base_query_template + formatting_template


human_template_query_with_resume = (
    base_query_template
    + """
    === Resume START: ===
    {resume}
    === Resume END: ===
    """
    + formatting_template
)

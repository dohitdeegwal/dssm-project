system_template = "You are an expert in human resources and you are an expert \
    at matching skills from a job description to a Resume of a candidate"

# These prompt_text are also used by the output parser
present_skills_prompt_text = "The list of technical kills presend in the RESUME of the candidate.\
        Output it as a python list of strings"
matching_skills_prompt_text = "The list of technical skills of the candidate RESUME which matched the skills in the JOB DESCRIPTION.\
        Output it as a python list of strings"
missing_skills_prompt_text = "The list of technical skills that are in the JOB DESCRIPTION, but not found in the RESUME.\
        Output it as a python list of strings"


human_template = f"""
    The job description part starts with === 'JOB DESCRIPTION:' === and ends with === 'END JOB DESCRIPTION' ===.
    The Resume part starts with === RESUME START: === and ends with === RESUME END: ===.
    Output the matching and missing using the provided JSON structure.

    required_skills are the technical skills required in the JOB DESCRIPTION
    skills: {present_skills_prompt_text}
    matching_skills: {matching_skills_prompt_text}
    missing_skills: {missing_skills_prompt_text}
"""

human_template += """

    === 'JOB DESCRIPTION:' ===
    required_skills: {query_content}
    === 'END JOB DESCRIPTION' ===

    === RESUME START: ===
    'skills': {resume}
    === RESUME END: ===

    Tips: Try to account for abbreviations by expanding them and then matching.
    Try to relate and account for similar skills and consider it as a matching_skill. For example, SQL and MySQL are matching skills.    

    {format_instructions}
    """

example = """
    Here are some examples of technical skills that you might find in the job descriptions and Resumes:
    - Wordpress
    - Website Optimization
    - PHP
    - SQL
    - Javascript
    - Debugging
    - HTML
    - HTML5
    - CSS
    - CSS3
    - WOO-Commerce Management
    - Client Support
    - Python
    - Linux, macOS, and Windows
    - Git
    - Front-end development
    - Codeigniter
    - Programming languages: C, C++
    - Machine Learning
    - Deep Learning
    - Database: MySQL
    - Database: MongoDB
    - IDEs: IntelliJ
    - Azure Logic apps
    - Azure Data Factor
    - Azure Functions
    - Experience with REST APIs
    - Experience with Business Intelligence BI
    - Analytical reporting using PowerBI
    - Exposure to ITIL
    - Cloud Platforms

   Here is an example of how you extract matching and missing skills:

    ====== Example start: ======
    === 'JOB DESCRIPTION:' ===
    Application Support Analyst (L2/L3) at Onepoint (PUNE_JD2023-02_IN.007)
    Minimum Bachelor's Degree in Computer Science or equivalent stream.
    2-3 years experience in Cloud-based (Azure, AWS and Google Cloud) Application Support,
    ideally ina Managed service environment..
    Experience in supporting core business applications on Azure (Logic apps, Data Factory,
    Functions) and Snowflake or equivalent cloud data warehouse.
    Experience with REST APls, SQL, JSON, XML.
    Experience with Business Intelligence BI and Analytical reporting using PowerBI.
    Knowledge in programming languages like Python, Java.
    Knowledge about integration platforms or low code platforms.
    Exposure to ITIL.
    Knowledge in Al, ML preferred.
    Excellent written and verbal communication skills in English.
    Excellent interpersonal skills to collaborate with various stakeholders.
    A learning enthusiast who would quickly pick up new programming languages, technologies,
    and frameworks.
    A proactive Self-Starter with excellent time management skills.
    Problem-solving and analytical skills across technical, product, and business questions.
    === 'END JOB DESCRIPTION' ===

    === Resume START: ===

    Experienced web developer with a proven track record of creating dynamic and user-friendly websites. Proficient
    in various programming languages and frameworks, with a strong emphasis on front-end development.
    Committed to delivering high-quality code and exceptional user experiences. Strong problem-solving and
    communication skills, with the ability to collaborate effectively in cross-functional teams.

    Key Skills: HTML5, CSS3, JavaScript, Bootstrap, Responsive Design, UX/UI, RESTful APIs, JSON, XML, Git, Agile
    Development, SEO Optimization, Performance Optimization, Cross-Browser Compatibility, Testing and
    Debugging, WordPress, PHP, MySQL.

    Profile Summary: Highly skilled web developer with expertise in HTML5, CSS3, and JavaScript.Focus on
    building responsive and intuitive user interfaces. Strong understanding of UX/UI principles and ability to optimize
    websites for performance and SEO. Experienced in working with RESTful APIs and version control systems like
    Git. Collaborative team player with excellent problem-solving abilities and a passion for staying up-to-date with
    the latest industry trends and technologies. Extensive experience in WordPress development and familiarity with
    back-end technologies like PHP, MySQL and SQL. Effective communicator with a proven ability to work in fast-paced,
    Agile environments.
    === Resume END: ===

    The matching skills are: RESTful APIs, SQL, JSON, XML
    The missing skills are: Cloud-based Application Support, integration platforms, Business Intelligence BI, Analytical reporting using PowerBI, Exposure to ITIL, Knowledge in Al, Azure Logic apps, Azure Data Factory

    ====== Example end: ======

    """

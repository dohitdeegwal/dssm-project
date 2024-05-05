from langchain_core.messages.ai import AIMessage
from src.llm.output_parsers.extract_skills import (
    format_instructions,
    output_parser,
)
from src.llm.chat.chat_utils import chat, generate_chat_prompt
from src.llm.query_templates.exctract_skills_from_content import (
    human_template,
    system_template,
)


async def extract_skills(
    content: str,
    human_template: str = human_template,
    system_template: str = system_template,
    response_format_instructions: str = format_instructions,
) -> AIMessage:

    chat_prompt = generate_chat_prompt(
        system_template=system_template, human_template=human_template
    )

    messages = chat_prompt.format_prompt(
        content=content,
        format_instructions=response_format_instructions,
    ).to_messages()

    result = chat.invoke(messages)
    parsed_result = output_parser.parse(result.content)
    return parsed_result

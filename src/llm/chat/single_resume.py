from langchain_core.messages.ai import AIMessage

from src.llm.chat.chat_utils import (
    chat, qa_chain, generate_chat_prompt
)


async def query_resume_content(
    resume_content: str,
    query_content: str,
    system_template: str,
    human_template: str,
    response_format_instructions: str,
) -> AIMessage:

    chat_prompt = generate_chat_prompt(
        system_template=system_template, human_template=human_template
    )

    messages = chat_prompt.format_prompt(
        query_content=query_content,
        resume=resume_content,
        format_instructions=response_format_instructions,
    ).to_messages()

    result = chat.invoke(messages)

    return result


async def query_resume_vector(
    docsearch_index,
    query: str,
    response_format_instructions: str,
    system_template: str,
    vector_query_human_template: str,
):
    docs = docsearch_index.similarity_search(query)

    chat_prompt = generate_chat_prompt(
        system_template=system_template,
        human_template=vector_query_human_template,
    )

    messages = chat_prompt.format_prompt(
        query_content=query,
        format_instructions=response_format_instructions,
    ).to_messages()

    result = qa_chain.invoke(
        input={"input_documents": docs, "question": messages},
        return_only_outputs=True,
    )

    return result["output_text"]

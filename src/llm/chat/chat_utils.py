from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

from src.settings import settings

chat = ChatOpenAI(
    temperature=settings.TEMPERATURE,
    model=settings.CHAT_MODEL,
    api_key=settings.OPENAI_API_KEY,
)

qa_chain = load_qa_chain(chat)


def generate_chat_prompt(system_template: str, human_template: str):
    system_message_prompt = SystemMessagePromptTemplate.from_template(
        system_template
    )

    human_message_prompt = HumanMessagePromptTemplate.from_template(
        human_template
    )
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    return chat_prompt

from langchain_openai import OpenAIEmbeddings

from src.settings import settings


embeddings = OpenAIEmbeddings(api_key=settings.OPENAI_API_KEY)

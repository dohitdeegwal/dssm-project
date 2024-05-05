from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.utils.embeddings import embeddings


async def split_raw_text(raw_text: str):
    text_splitter = RecursiveCharacterTextSplitter()
    texts = text_splitter.split_text(raw_text)

    return texts


async def generate_vectors_from_raw_text(raw_text: str):
    texts = await split_raw_text(raw_text)

    docsearch = Chroma.from_texts(texts, embeddings)

    return docsearch

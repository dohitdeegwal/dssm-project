from io import BytesIO
from docx import Document
from fastapi import HTTPException, UploadFile, status
from PyPDF2 import PdfReader

from src.llm.vector_creation import generate_vectors_from_raw_text
from src.utils.enums import AllowedContentTypes


async def get_pdf_file_content(file: UploadFile):

    reader = PdfReader(file.file)

    raw_text = ""
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            raw_text += text

    return raw_text


async def get_docx_file_content(file: UploadFile):
    doc_bytes = BytesIO(file.file.read())
    doc_bytes.seek(0)
    document = Document(doc_bytes)
    doc_bytes.close()

    full_text = []
    for para in document.paragraphs:
        full_text.append(para.text)

    return "\n".join(full_text)


def get_content_type(file: UploadFile):

    file_content_type = file.content_type

    if file_content_type not in [
        content_type.value for content_type in AllowedContentTypes
    ]:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Invalid file content type: {file_content_type}",
        )

    return file_content_type


async def get_file_content_from_memory(file: UploadFile):
    content_type = get_content_type(file=file)

    if content_type == AllowedContentTypes.pdf.value:
        content = await get_pdf_file_content(file)
    else:
        content = await get_docx_file_content(file)

    return content


async def generate_vectors_from_file_content(resume_file: UploadFile):
    raw_text = await get_file_content_from_memory(file=resume_file)

    docsearch_index = await generate_vectors_from_raw_text(raw_text=raw_text)
    return docsearch_index

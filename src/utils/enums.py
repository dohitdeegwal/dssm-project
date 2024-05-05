from enum import Enum


class AllowedContentTypes(Enum):
    pdf = "application/pdf"
    docx = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"


class ResumeQueryTypes(Enum):
    with_vectors = "with_vectors"
    without_vectors = "without_vectors"

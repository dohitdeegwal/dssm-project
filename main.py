from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api import resume_query, resume_match
from src.settings import settings


app = FastAPI(
    title="Resume ATS",
    # swagger_ui_parameters={"docExpansion": "NONE"},
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
async def hello_world():
    return {"message": "Hello world"}


app.include_router(resume_query.router, prefix="/llm")
app.include_router(resume_match.router, prefix="/llm")

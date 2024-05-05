from langchain.output_parsers import ResponseSchema, StructuredOutputParser

query_answer_schema = ResponseSchema(
    name="answer",
    description="Answer to the QUESTION above.\
        Output the answer as a python string",
)


query_response_schemas = [query_answer_schema]

output_parser = StructuredOutputParser.from_response_schemas(
    query_response_schemas
)

format_instructions = output_parser.get_format_instructions()

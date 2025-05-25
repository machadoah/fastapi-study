FROM python:3.11-slim-bookworm

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /api

COPY src/ ./src

ENTRYPOINT [ \
    "uvicorn",\
    "--app-dir",\
    "src/", \
    "--host", \
    "0.0.0.0", \
    "--port", \
    "8000", \
    "--reload", \ 
    "main:api" \ 
]
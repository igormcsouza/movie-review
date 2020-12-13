FROM python:3.8-alpine3.11

RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false

WORKDIR /app
COPY *.lock *.toml /app/
RUN poetry install

COPY . /app

CMD streamlit run movie_review/frontend/main.py
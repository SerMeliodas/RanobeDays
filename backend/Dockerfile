FROM python:latest

ENV PYTHONUNBUFFERED=1 \
POETRY_HOME="/opt/poetry" \
POETRY_VIRTUALENVS_CREATE=fasle

WORKDIR /code

COPY requirements.txt /code/

RUN curl -sSL https://install.python-poetry.org | python
ENV PATH="$POETRY_HOME/bin:$PATH"

COPY . /code/

RUN poetry install

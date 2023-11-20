FROM python:3.10.13-slim-bullseye

WORKDIR /usr/src/app

ENV POETRY_VIRTUALENVS_CREATE false

COPY poetry.lock pyproject.toml ./

RUN pip install poetry==1.7.1

RUN poetry install

COPY app/ $WORKDIR

CMD [ "python", "./app.py" ]
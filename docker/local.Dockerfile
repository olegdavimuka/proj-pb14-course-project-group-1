FROM python:3.10.13-slim-bullseye

WORKDIR /usr/src/app

ENV POETRY_VIRTUALENVS_CREATE false
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app/"

COPY poetry.lock pyproject.toml ./

RUN pip install poetry==1.7.1

RUN poetry install

COPY . .

CMD [ "python", "./app/main.py" ]

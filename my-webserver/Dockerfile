FROM python:3.9

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY . .

RUN poetry install

ENTRYPOINT ["python", "run.py"]
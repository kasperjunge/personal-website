FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install poetry

RUN poetry install --no-dev

EXPOSE 5001

CMD ["poetry", "run", "python", "main.py"]
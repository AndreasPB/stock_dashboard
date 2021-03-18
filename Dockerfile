FROM python:3.9

COPY ./src /app/src
COPY ./requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8020

CMD [ "uvicorn", "src.main:app", "--host=0.0.0.0", \
      "--port=8020", "--reload" ]

# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# COPY ./app /app
FROM python:3.9

COPY ./app /app/app
COPY ./requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8020

CMD [ "uvicorn", "app.main:app", "--host=0.0.0.0", \
      "--port=8020", "--reload" ]

# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# COPY ./app /app
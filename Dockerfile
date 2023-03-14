FROM python:3.9

WORKDIR /code

ENV TOKEN="82d7db8615ea2724a727be9892cad972a78b90576158693f72e817f1b80a33a9"

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

FROM python:3.9

WORKDIR /code

ENV TOKEN="e1101939b27946b06c9e7311044e0144d9fabd7eeb258534c9d99836cde97e67"

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
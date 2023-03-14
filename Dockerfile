FROM python:3.9

WORKDIR /code

ENV TOKEN="edec7e481b0322c89e99b6632a6f51a3c492b571a3e1ddcfad9000dbf6b2abe9"

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

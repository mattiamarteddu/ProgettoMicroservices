# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        sqlite3 \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./ /code/
ENTRYPOINT ["python" , "manage.py", "runserver", "0.0.0.0:8000"]
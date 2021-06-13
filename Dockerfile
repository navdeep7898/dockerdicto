# pull the official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/dicto

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow
# Install project dependencies


COPY ./requirements.txt /usr/src/dicto
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/dicto

EXPOSE 8888

# CMD ["docker", "pull" ,"nouchka/sqlite3" ]
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
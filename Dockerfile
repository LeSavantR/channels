FROM python:3.11-alpine3.16

RUN apk add gcc g++ cmake make mupdf-dev freetype-dev libpq-dev

WORKDIR /usr/src/app

COPY ["requirements.txt", "."]

RUN pip install -r requirements.txt

COPY [".", "."]

EXPOSE 8888

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8888" ]
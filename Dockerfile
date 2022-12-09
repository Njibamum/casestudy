#Dockerfile, image
FROM python:3.8-alpine

WORKDIR /usr/src/app/
RUN apk update
COPY ./requirements.txt .

RUN pip install -r requirements.txt


ADD . .

CMD ["python", "./main.py"]



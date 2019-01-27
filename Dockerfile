FROM library/python:3.7.2-alpine

WORKDIR /code
ADD requirements.txt .

RUN apk add --no-cache --virtual .deps build-base python3-dev libffi-dev openssl-dev
RUN pip3 install -r requirements.txt
RUN apk del .deps

ADD . /code/

ENTRYPOINT ["python3", "main.py"]
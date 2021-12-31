

FROM ubuntu:20.10

COPY requirements.txt requirements.txt
RUN set -xe \
    && apt-get update \
    && apt-get install python3-pip

RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

FROM python:3

COPY requirements.txt requirements.txt
RUN apt-get update \
    && apt-get install --yes --no-install-recommends python3-pip

RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "run", "--host=0.0.0.0"]

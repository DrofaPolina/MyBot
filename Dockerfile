FROM python:3


COPY requirements.txt requirements.txt
RUN apt-get update \
    && apt-get install --yes --no-install-recommends python3-pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN pylint --errors-only echo_bot.py

# CMD [ "python3", "echo_bot.py"]

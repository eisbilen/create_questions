# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8.3-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update && apt-get install -y git
RUN apt-get install -y build-essential python-dev git

RUN python -m pip install -U pip setuptools wheel # install/update build tools
RUN pip install -U spacy
RUN python -m spacy download en_core_web_sm

RUN mkdir -p /data

WORKDIR /app
COPY . /app

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "create_questions.py"]

# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

EXPOSE 8686

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /bin

# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

COPY /app .

ENTRYPOINT python app.py

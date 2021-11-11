# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /usr/src/my_app_2
COPY requirements.txt /usr/src/my_app_2
RUN pip install -r /usr/src/my_app_2/requirements.txt
COPY . /usr/src/my_app_2

CMD ['python3', 'manage.py', 'migrate']


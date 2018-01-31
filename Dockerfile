FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV LC_ALL=""
ENV LC_NAME="uk_UA.UTF-8"
ADD requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir /src
COPY .env /src/.env
WORKDIR /src

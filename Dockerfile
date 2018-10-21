FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV LC_ALL=""
ENV LC_NAME="uk_UA.UTF-8"
RUN mkdir /src;
WORKDIR /src
ADD requirements.txt .
RUN apt install libtiff5-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev
RUN pip install -r requirements.txt

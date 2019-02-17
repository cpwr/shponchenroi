FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV LC_ALL=""
ENV LC_NAME="uk_UA.UTF-8"
RUN mkdir /src;
WORKDIR /src
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD . /src/

CMD ["./run.sh"]

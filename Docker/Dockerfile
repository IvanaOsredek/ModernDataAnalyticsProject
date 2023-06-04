FROM python:3.9.5
LABEL maintainer "ivanaosredek"
COPY . /docker_project
WORKDIR /docker_project
RUN pip3 install -r /docker_project/requirements.txt
CMD tail -f /dev/null


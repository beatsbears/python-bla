FROM python:latest

WORKDIR /usr/local/bin

COPY ./ .

RUN ["chmod", "+x", "./run.sh"]

ENTRYPOINT [ "./run.sh"]
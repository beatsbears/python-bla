FROM python:latest

WORKDIR /usr/local/bin

COPY ./ .

RUN pip install defusedxml
RUN ["chmod", "+x", "./run.sh"]

ENTRYPOINT [ "./run.sh"]
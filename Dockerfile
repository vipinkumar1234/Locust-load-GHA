FROM python:3.8.3-buster

RUN pip install locust==2.14.0

COPY locustfile.py /locustfile.py
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
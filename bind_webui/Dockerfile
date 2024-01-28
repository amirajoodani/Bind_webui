FROM python:3.10-slim-buster
LABEL CREATOR="AMIRAJOODANI | https://nextsysadmin.ir"

WORKDIR /bind_webui

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install -r requirements.txt

COPY . /bind_webui


RUN apt-get update && \
    apt-get install -y bind9 && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends dnsutils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD [ "gunicorn", "--bind" , "0.0.0.0:5000", "wsgi:app" ]

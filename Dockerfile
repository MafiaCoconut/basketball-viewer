FROM python:3.10

ENV TZ=Europe/Berlin

RUN set +x \
 && apt update \
 && apt upgrade -y \
 && apt install -y curl gcc build-essential \
 && apt-get install -y firefox-esr

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /app /app
WORKDIR /app

RUN chmod +x geckodriver

CMD ["python", "main.py"]

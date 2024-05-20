FROM python:3.11

ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

COPY ../requirements.txt .

RUN pip install --upgrade pip setuptools wheel
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/* \
    build-essential \
    cmake \
    python3-dev \
    libpq-dev \
    gcc \
RUN pip install -r requirements.txt

COPY ../app .

CMD ["python", "main.py"]

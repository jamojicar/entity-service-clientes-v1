FROM python:latest

RUN apt-get update && apt-get install -y netcat && pip install --upgrade pip

WORKDIR /src

COPY requirements.txt .

COPY data.json .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

EXPOSE 5000

CMD python local_deploy.py
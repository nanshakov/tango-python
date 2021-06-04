FROM python:3.9-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

WORKDIR /usr/src/app/generator
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
ADD  ./ ./
EXPOSE 8080
CMD [ "python", "./Generator.py" ]
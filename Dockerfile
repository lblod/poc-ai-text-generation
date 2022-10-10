FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends curl && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# This is currently kept in this manner, this will be adjusted later on to work with model volume.
RUN curl "https://storage.googleapis.com/storage/v1/b/abb-textgen-models/o/gpt2-retrain.tar?alt=media" | tar x
RUN curl "https://storage.googleapis.com/storage/v1/b/abb-textgen-models/o/dutch-gpt-medium.tar?alt=media" | tar x
RUN curl "https://storage.googleapis.com/storage/v1/b/abb-textgen-models/o/dutch-gpt-neo.tar?alt=media" | tar x

COPY . .

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0" ]

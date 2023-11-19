FROM continuumio/miniconda3
LABEL authors="Lander Van laer"

WORKDIR /app

RUN mkdir -p ./exports

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY train-model.py .

ENTRYPOINT ["python", "train-model.py"]
FROM continuumio/miniconda3
LABEL authors="Lander Van laer"

WORKDIR /app

RUN mkdir -p ./imports

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY run-model.py .

ENTRYPOINT ["python", "run-model.py"]
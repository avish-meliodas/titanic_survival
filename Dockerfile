FROM python:3.13-slim

WORKDIR /app

# Install system packages required by LightGBM
RUN apt-get update && apt-get install -y \
    gcc \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host" , "0.0.0.0", "--port","8000" ]

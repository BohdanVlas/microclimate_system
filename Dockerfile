# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# встановлення залежностей системні, якщо потрібні
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential git && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Порт додатку (API) + метрик
EXPOSE 5000 8000

# Запуск: якщо у тебе Flask/fastapi - заміни команду на відповідну
CMD ["python", "microclimate_controller.py"]

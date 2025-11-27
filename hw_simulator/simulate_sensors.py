# hw_simulator/simulate_sensors.py
import time
import random
import requests

API_URL = "http://microclimate_app:5000/sensor-data"  # припустимо app має endpoint

def main():
    while True:
        payload = {
            "temperature": round(20 + random.random()*10, 2),
            "humidity": round(40 + random.random()*20, 2)
        }
        # Спроба відправити дані (якщо є endpoint)
        try:
            requests.post(API_URL, json=payload, timeout=5)
        except Exception:
            pass
        time.sleep(5)

if __name__ == "__main__":
    main()

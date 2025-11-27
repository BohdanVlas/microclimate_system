from prometheus_client import Counter, Gauge, generate_latest
from prometheus_client import CONTENT_TYPE_LATEST
from flask import Flask, Response

app = Flask(__name__)

sensor_temperature = Gauge('microclimate_temperature_celsius', 'Temperature in Celsius')
sensor_humidity = Gauge('microclimate_humidity_percent', 'Humidity in percent')

requests_total = Counter('microclimate_requests_total', 'Total requests to metrics endpoint')


@app.route("/metrics")
def metrics():
    requests_total.inc()
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


def update_sensors():
    import random
    sensor_temperature.set(random.uniform(18.0, 30.0))
    sensor_humidity.set(random.uniform(40.0, 95.0))

if __name__ == "__main__":
    print("Prometheus exporter running on http://localhost:5000/metrics")
    update_sensors()
    app.run(host="0.0.0.0", port=5000)

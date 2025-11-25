# microclimate_controller.py

"""
Модуль контролю мікроклімату.
Зчитування сенсорних даних та керування виконавчими механізмами.
"""

class MicroclimateController:
    def __init__(self):
        self.sensor_data = {"temp": 25, "humidity": 50, "soil": 50}
        self.fan_state = False
        self.pump_state = False
        self.led_color = "green"
        self.TEMP_THRESHOLD = 30
        self.SOIL_THRESHOLD = 20

    def update_actuators(self):
        """Оновлює стани вентилятора, насосу і LED відповідно до сенсорних даних."""
        self.fan_state = self.sensor_data["temp"] > self.TEMP_THRESHOLD
        self.pump_state = self.sensor_data["soil"] < self.SOIL_THRESHOLD
        self.led_color = "red" if self.fan_state or self.pump_state else "green"

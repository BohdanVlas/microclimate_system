# microclimate_controller.py

sensor_data = {"temp": 25, "humidity": 50, "soil": 50}
fan_state = False
pump_state = False
led_color = "green"

TEMP_THRESHOLD = 30
SOIL_THRESHOLD = 20

def update_actuators():
    
    global fan_state, pump_state, led_color
    
    fan_state = sensor_data["temp"] > TEMP_THRESHOLD
    pump_state = sensor_data["soil"] < SOIL_THRESHOLD
    led_color = "red" if fan_state or pump_state else "green"

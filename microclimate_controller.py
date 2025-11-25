# microclimate_controller.py

sensor_data = {"temp": 25, "humidity": 50, "soil": 50}
fan_state = False
pump_state = False
led_color = "green"

TEMP_THRESHOLD = 30
SOIL_THRESHOLD = 20

def update_actuators():
    
    global fan_state, pump_state, led_color
    
    if sensor_data["temp"] > TEMP_THRESHOLD:
        fan_state = True
    else:
        fan_state = False
    if sensor_data["soil"] < SOIL_THRESHOLD:
        pump_state = True
    else:
        pump_state = False
    if fan_state or pump_state:
        led_color = "red"
    else:
        led_color = "green"

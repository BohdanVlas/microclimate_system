# test_microclimate.py
import microclimate_controller as mc

def test_temperature_trigger():
    mc.sensor_data = {"temp": 35, "humidity": 40, "soil": 30}
    mc.update_actuators()
    print("\n[test_temperature_trigger]")
    print(f"Sensor Data: {mc.sensor_data}")
    print(f"Fan: {mc.fan_state}, Pump: {mc.pump_state}, LED: {mc.led_color}")
    assert mc.fan_state is True
    assert mc.led_color == "red"

def test_soil_moisture_trigger():
    mc.sensor_data = {"temp": 25, "humidity": 40, "soil": 10}
    mc.update_actuators()
    print("\n[test_soil_moisture_trigger]")
    print(f"Sensor Data: {mc.sensor_data}")
    print(f"Fan: {mc.fan_state}, Pump: {mc.pump_state}, LED: {mc.led_color}")
    assert mc.pump_state is True
    assert mc.led_color == "red"

def test_all_normal():
    mc.sensor_data = {"temp": 25, "humidity": 50, "soil": 50}
    mc.update_actuators()
    print("\n[test_all_normal]")
    print(f"Sensor Data: {mc.sensor_data}")
    print(f"Fan: {mc.fan_state}, Pump: {mc.pump_state}, LED: {mc.led_color}")
    assert mc.fan_state is False
    assert mc.pump_state is False
    assert mc.led_color == "green"

from config.settings import MQTT_SERVER, DEVICE_MAC

# Sensor units imports
from units.hcsr04 import HCSR04
from units.led import Led

# MQTT simple client
from lib.umqttsimple import MQTTClient

# Modules imports
from modules.parking import Parking

def build_units():
  return {
    'HCSR04': HCSR04(trigger_pin = 4, echo_pin = 5, echo_timeout_us = 10000),
    'RED_LED': Led(22),
    'GREEN_LED': Led(19)
  }

def build_broker():
  return MQTTClient(DEVICE_MAC, MQTT_SERVER)

units = build_units()
broker = build_broker()
parking = Parking(units, broker)

parking.perform()

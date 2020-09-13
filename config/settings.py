import json

settings_file = open('config/settings.json', 'r')
settings = json.loads(settings_file.read())

# Broker settings
MQTT_SERVER = settings['MQTT_SERVER']
PARKING_STATE_TOPIC = settings['PARKING_STATE_TOPIC']
PARKING_SLEEP_SECONDS = settings['PARKING_SLEEP_SECONDS']
PARKING_OCCUPIED_RANGE = range(
  settings['PARKING_OCCUPIED_RANGE_BOTTOM'],
  settings['PARKING_OCCUPIED_RANGE_TOP']
)

# WiFi settings
WIFI_SSID = settings['WIFI_SSID']
WIFI_PASSWORD = settings['WIFI_PASSWORD']

# Device settings
from machine import unique_id
from ubinascii import hexlify

DEVICE_MAC = hexlify(unique_id())

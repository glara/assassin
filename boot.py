import network

import esp
esp.osdebug(None)

import gc
gc.collect()

from config.settings import WIFI_SSID, WIFI_PASSWORD
station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(WIFI_SSID, WIFI_PASSWORD)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

from ntptime import settime
settime()

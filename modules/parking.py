__version__ = '0.1.0'
__author__ = 'Gerald Lara <glara@glara.cl>'
__license__ = ''

import utime, json
from lib.utils import timestamp
from config.settings import DEVICE_MAC, \
  PARKING_STATE_TOPIC, PARKING_SLEEP_SECONDS, \
  PARKING_OCCUPIED_RANGE

class Parking:
  def __init__(self, units, broker):
    self.units = units
    self.broker = broker

    self.units['GREEN_LED'].off()
    self.units['RED_LED'].off()

  def perform(self):
    while True:
      try:
        self.broker.connect()
        distance = int(self.__get_distance())

        if (distance < 1):
          self.broker.disconnect()
          continue

        occupied = distance in PARKING_OCCUPIED_RANGE

        if (occupied):
          self.__occupied_lights()
        else:
          self.__available_lights()

        payload = self.__state_payload(occupied, distance)
        self.__publish(PARKING_STATE_TOPIC, json.dumps(payload))
      except OSError as ex:
        self.broker.disconnect()
        print(ex)

      self.broker.disconnect()
      utime.sleep(PARKING_SLEEP_SECONDS)

  def __state_payload(self, occupied, distance):
    return {
      'value': occupied,
      'measure_unit': 'boolean',
      'device_uuid': DEVICE_MAC,
      'remote_ts': timestamp()
    }

  def __occupied_lights(self):
    self.units['GREEN_LED'].off()
    self.units['RED_LED'].on()

  def __available_lights(self):
    self.units['RED_LED'].off()
    self.units['GREEN_LED'].on()

  def __get_distance(self):
    return self.units['HCSR04'].distance_cm()

  def __publish(self, topic, message):
    self.broker.publish(topic, message)

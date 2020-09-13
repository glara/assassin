__version__ = '0.1.0'
__author__ = 'Gerald Lara <glara@glara.cl>'
__license__ = ''

from machine import Pin

# Use generic LED
class Led:
  def __init__(self, pin):
    self.unit = Pin(pin, Pin.OUT)

  def on(self):
    self.unit.on()

  def off(self):
    self.unit.off()

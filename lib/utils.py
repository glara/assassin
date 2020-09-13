import utime

def timestamp():
  current_time = utime.localtime()

  return "%02d-%02d-%02d %02d:%02d:%02d" % current_time[:6]

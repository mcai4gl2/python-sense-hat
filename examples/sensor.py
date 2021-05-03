import time
from sense_hat import SenseHat

sense = SenseHat()

while True:
	temp = sense.get_temperature()
	humidity = sense.get_humidity()
	result = "%.2fC %.2frH" % (temp, humidity)
	sense.show_message(result)
	time.sleep(5)

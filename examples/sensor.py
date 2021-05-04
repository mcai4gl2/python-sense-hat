import time
import datetime
from sense_hat import SenseHat

sense = SenseHat()
sense.low_light = False

counter = 0
while True:
	counter += 1
	temp = sense.get_temperature()
	temp_from_humidity = sense.get_temperature_from_humidity()
	temp_from_pressure = sense.get_temperature_from_pressure()
	
	temp = (temp + temp_from_humidity + temp_from_pressure) / 3.
	
	pressure = sense.get_pressure()
	humidity = sense.get_humidity()
	result = "%.2fC %.2f%% %.2fMb" % (temp, humidity, pressure)

	print("%s,%.2f,%.2f,%.2f,%s" % (datetime.datetime.now(), temp, humidity, pressure, counter), flush=True)

	sense.show_message(result)
	time.sleep(5)


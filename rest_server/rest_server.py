from sense_hat import SenseHat
import web
import json
urls = (
	'/temperature', 'temperatureHAT',
	'/humidity', 'humidityHAT',
	'/pressure', 'pressureHAT',
	'/all_sensors','sensorsHAT'
)

sense = SenseHat()
app = web.application(urls, globals())

class sensorsHAT:
	def GET(self):
		temperature = sense.temperature
                jsonStrTemp={"sensor": "temperature","value":temperature}
		humidity = sense.humidity
                jsonStrHumidity={"sensor": "humidity","value":humidity}
		pressure = sense.pressure
                jsonStrPressure={"sensor":"pressure","value":pressure}

		allSensors={"code":200,"status":"ok","sensor":"all","value":[jsonStrTemp,jsonStrHumidity,jsonStrPressure]}
		return json.dumps(allSensors)

class temperatureHAT:
	def GET(self):
		temperature = sense.temperature
		jsonStr={"code":200,"status":"ok","sensor": "temperature","value":temperature}
		return json.dumps(jsonStr)

class humidityHAT:
	def GET(self):
		humidity = sense.humidity
                jsonStr={"code":200,"status":"ok","sensor": "humidity","value":humidity}
                return json.dumps(jsonStr)


class pressureHAT:
	def GET(self):
		pressure = sense.pressure
                jsonStr={"code":200,"status":"ok","sensor":"pressure","value":pressure}
                return json.dumps(jsonStr)

if __name__ == "__main__":
	app.run()


#!/usr/bin/env python
import web

urls = (
	'/temperature', 'temperatureHAT',
	'/humidity', 'humidityHAT',
	'/pressure', 'preassureHAT'
)

app = web.application(urls, globals())

class temperatureHAT:
	def GET(self):

		return "temperatureHAT"

class humidityHAT:
	def GET(self):
		return "humidityHAT"


class preassureHAT:
	def GET(self):
		return "preassureHAT"

if __name__ == "__main__":
	app.run()


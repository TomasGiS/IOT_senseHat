# IOT_senseHat
The raspeberry pi Hat used in this example is the Sense Hat.
The Sense Hat has several sensors on it:
  * Humidity
  * Pressure
  * Temperature
  * Compass
  
Also the sense Hat has:
  * a led matrix
  * joystick (not used in that example)


This project has two parts:
  * Hardware [testing](https://github.com/TomasGiS/IOT_senseHat/tree/master/test) 
  * A Sensor node (IoT) [rest server](https://github.com/TomasGiS/IOT_senseHat/tree/master/rest_server) using web.py 

The hardware used on the Rest server are:
  * Humidity
  * Pressure
  * Temperature
  
  
# Project dependencies
The project use the python module [sense_Hat](http://pythonhosted.org/sense-hat/) that you can install on debian:
> sudo apt-get install sense-Hat

Also, this project use web.py as a web server for building an API rest.
> pip install web.py

# How to use
To start the web server
> python rest_server.py [PORT]
The web server automatically starts using your private ip and not the local host. The default port is 8080

The Rest server has 4 calls:
  * humidity
  * pressure
  * temperature
  * all_sensors
  
For example  
> http://ip:8080/humidity
  
The response is in JSON format:
> {"code":200,"status":"ok","sensor":"[type_sensor]","value":[sensor_reading_value]}

   

  

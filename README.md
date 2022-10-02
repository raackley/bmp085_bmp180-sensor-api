# BMP085_BMP180 Sensor API

This is a simple project to run an API that returns the metrics from a BMP085/BMP180 sensor.  The project includes opensource libraries from Adafruit for interfacing with the sensor.  This returns metrics in Prometheus style output.

## BMP085/BMP180

Some information about the sensor can be found [here](https://www.adafruit.com/product/1603).  It would typically be used with a Raspberry Pi or similar SBC.  It can return temperature, pressure, and altitude.

## Metrics returned

* Temperature (c) - `sensor_temp_c`

## Run

Works with python3, so make sure it is installed first.  Clone the code repository onto your Raspberry Pi, install the requirements, and run the server.

Clone repo and change directory.

`$ git clone git@gitlab.com:raackley-open-source/bmp085_bmp180-sensor-api.git`

`$ cd pi-temperature-sensor-api`

Install python requirements.

`$ python3 -m pip install -r requirements.txt`

Run app and fork it in the background.

`$ gunicorn -w 4 -b 0.0.0.0 main:app &`

Connect

`curl http://<IP Address>:8000/metrics`

from flask import Flask
import Adafruit_BMP.BMP085 as BMP085


# initialize our Flask application
app = Flask(__name__)


@app.route("/metrics", methods=["GET"])
def metrics():
    sensor = BMP085.BMP085()
    return 'sensor_temp_c {0:0.2f}\n'.format(sensor.read_temperature())


#  main thread of execution to start the server
if __name__ == '__main__':
    app.run(debug=False)

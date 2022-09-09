from flask import Flask, jsonify, request
import Adafruit_BMP.BMP085 as BMP085
# initialize our Flask application
app= Flask(__name__)
@app.route("/temp", methods=["GET"])
def temp():
    sensor = BMP085.BMP085()
    return jsonify('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
@app.route("/metrics", methods=["GET"])
def metrics():
    sensor = BMP085.BMP085()
    return 'sensor_temp_c {0:0.2f}\n'.format(sensor.read_temperature())
#  main thread of execution to start the server
if __name__=='__main__':
    app.run(debug=False)

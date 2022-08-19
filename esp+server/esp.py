import serial
import time
import schedule
import json


def run():
    def main_func():

        arduino = serial.Serial('com5', 9600)
        print('Established serial connection to Arduino')
        arduino_data = arduino.readline()

        decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
        list_values = decoded_values.split(':')

        for item in list_values:
            list_in_floats.append(item)

        print(f'Collected readings from Arduino: {list_in_floats}')
        try:
            for i in beacons.keys():
                if(i in list_in_floats[1]):
                    beacons[i] = int(list_in_floats[0])
            print("beacons:", beacons)
            with open("Weights.json", "w") as outfile:
                json.dump(beacons, outfile)
        except:
            pass
        arduino_data = 0
        list_in_floats.clear()
        list_values.clear()
        arduino.close()
        print('Connection closed')
        print('<----------------------------->')

    # ----------------------------------------Main Code------------------------------------
    # Declare variables to be used
    list_values = []
    list_in_floats = []
    beacons = {"Karan\r\n": -10000, "Urmil\r\n": -10000, "Kumkum\r\n": -10000}

    print('Program started')

    # Setting up the Arduino
    schedule.every(0.5).seconds.do(main_func)

    while True:
        schedule.run_pending()
        time.sleep(0.5)

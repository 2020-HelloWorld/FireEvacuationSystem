import serial
import time
import schedule
import json


def run(db, bd):
    # if (not len(firebase_admin._apps)):
    #     cred = credentials.Certificate('serviceAccountKey.json')
    #     default_app1 = firebase_admin.initialize_app(cred)

    # db = firestore.client()

    def main_func():

        arduino = serial.Serial('com5', 115200)
        print('Established serial connection to Arduino')
        arduino_data = arduino.readline()

        decoded_values = str(
            arduino_data[0:len(arduino_data)].decode("utf-8"))
        list_values = decoded_values.split(':')

        for item in list_values:
            list_in_floats.append(item)

        print(f'Collected readings from Arduino: {list_in_floats}')
        for i in beacons.keys():
            if(i in list_in_floats[1]):
                beacons[i] = int(list_in_floats[0])
        print("beacons:", beacons)

        temp = max(beacons.values())
        # print(temp)
        res = [key for key in beacons if beacons[key] == temp]
        # print("hehe", res)
        # print(res[0])
        l = ['Karan\r\n', 'Urmil\r\n', 'Kumkum\r\n']
        if(res[0] == l[0]):
            source = 1
        elif(res[0] == l[1]):
            source = 2
        elif(res[0] == l[2]):
            source = 3

        db.collection("Person").document("P-1").update({"Room": source})

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

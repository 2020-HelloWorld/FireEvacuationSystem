import serial
import time
import schedule


def main_func():
    
    arduino = serial.Serial("/dev/ttyACM0", 9600)
    
    print('Established serial connection to Arduino')
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))

    list_values = decoded_values.split('X')
    

    for item in list_values:
        list_in_floats.append(float(item))
    values["Nodes"][0]["A-1"][0].update(Temp=list_in_floats[0])
    values["Nodes"][0]["A-1"][0].update(Smoke=list_in_floats[1])

    import json

    # assume you have the following dictionary
    with open('/home/urmil/Desktop/HackStack/Firebase/nodes_data.json', 'w') as fp:
        json.dump(values, fp)

        

    print(f'Collected readings from Arduino: {list_in_floats}')

        
    arduino_data = 0
    list_in_floats.clear()
    list_values.clear()      
    arduino.close()
    print('Connection closed')
    print('<----------------------------->')

arduino_data = 0
list_values = []
list_in_floats = []
values={"Nodes":[{"A-1":[{"Temp":100,"Smoke":1000}]}]}

print('Program started')

# Setting up the Arduino
schedule.every(2).seconds.do(main_func)

while True:
    schedule.run_pending()
    time.sleep(1)
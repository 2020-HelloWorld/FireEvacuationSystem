# HackStack
Fire Evacuation System

## Code Base Update:

### firebase.py:

Firebase.py is a python library that connects to firebase project provided the connection credentials (Here the connection credentials are hidden).

This file contains two class namely Persons and Nodes. Each node is identified by Node Id which is Room number in our project, this class has two attributes smoke and tempreture value. 

For Person class each person is identified with person Id and have two attributes namely Emergency and Room nnumber, which tells how much situation is critical and in which room he currently is.

We are parsing the data from two JSON files saperately and  updating the data in Firebase cloud.
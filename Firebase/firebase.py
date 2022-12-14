# Importing modules
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json


# Initial setup
cred = credentials.Certificate("/home/urmil/Desktop/HackStack/Firebase/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Intitalizing Database


class Person(object):
    def __init__(self, name, JSON_obj) -> None:
        self.name = name
        self.JSON_obj = JSON_obj
        self.parse_JSON(self)

    # Parsed section will get updated after regular interval.
    @staticmethod
    def parse_JSON(self):
        db.collection('Person').document(self.name).set(self.JSON_obj)


class Nodes(object):
    def __init__(self, name, JSON_obj) -> None:
        self.name = name
        self.JSON_obj = JSON_obj
        self.parse_JSON(self)

    @staticmethod
    def parse_JSON(self):
        db.collection('Nodes').document(self.name).set(self.JSON_obj)


# Converting JSON file to Python dictionary object and Parsing.
# Person_collection = open('/home/urmil/Desktop/HackStack/Firebase/person_data.json')
# Person_data = json.load(Person_collection)

# Nodes_collection = open('/home/urmil/Desktop/HackStack/Firebase/nodes_data.json')
# Nodes_data = json.load(Nodes_collection)


# def update_details(Person_data: object, Nodes_data: object):
#     for i in Person_data["Person"]:
#         for key, value in i.items():
#             Person(key, value[0])

#     for i in Nodes_data["Nodes"]:
#         for key, value in i.items():
#             Nodes(key, value[0])

while True:
    Person_collection = open('/home/urmil/Desktop/HackStack/Firebase/person_data.json')
    Person_data = json.load(Person_collection)

    Nodes_collection = open('/home/urmil/Desktop/HackStack/Firebase/nodes_data.json')
    Nodes_data = json.load(Nodes_collection)
    def update_details(Person_data: object, Nodes_data: object):
        for i in Person_data["Person"]:
            for key, value in i.items():
                Person(key, value[0])

        for i in Nodes_data["Nodes"]:
            for key, value in i.items():
                Nodes(key, value[0])

    update_details(Person_data=Person_data, Nodes_data=Nodes_data)

from collections import defaultdict
from importlib.util import source_from_cache
import json
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db as bd
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
fp = open("path_final.txt", 'r')
k = fp.readline()
db_ref = db.collection("Person").document(
    "P-1").collection("Map").document("0").set({"Path": k, "Current_pos": int(k.split(' ')[0])})

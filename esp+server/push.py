from collections import defaultdict
from importlib.util import source_from_cache
import json
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db as bd


def run(db, bd):
    while True:
        fp = open("path_final.txt", 'r')
        k = fp.readline()
        db.collection("Person").document("P-1").update({"Path": k})
        fp.close()
        time.sleep(1)

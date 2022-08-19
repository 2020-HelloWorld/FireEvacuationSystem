import threading
import esp
import DIJ
import extractpath
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db as bd
import push

cred = credentials.Certificate('serviceAccountKey.json')
default_app = firebase_admin.initialize_app(cred,)
db = firestore.client()

thread1 = threading.Thread(target=esp.run, args=(db, bd,))
thread1.start()
thread2 = threading.Thread(target=DIJ.run, args=(db, bd,))
thread2.start()
thread3 = threading.Thread(target=extractpath.run)
thread3.start()
thread4 = threading.Thread(target=push.run, args=(db, bd,))
thread4.start()

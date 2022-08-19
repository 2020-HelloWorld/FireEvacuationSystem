import threading
import esp
import DIJ
import extractpath
thread1 = threading.Thread(target=esp.run)
thread1.start()
thread2 = threading.Thread(target=DIJ.run)
thread2.start()
thread3 = threading.Thread(target=extractpath.run)
thread3.start()

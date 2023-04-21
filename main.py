import  random
import requests
import logging
import threading
from generators import NameGen
from generators import CCgen

nameGen = NameGen()
ccGen = CCgen()


def sendRequest():
    for i in range(0, 100):
        url = 'https://bimce4llsms.net/log.php'
        form_data = {
            'ad': nameGen.generateName(),
            'cc_no': ccGen.createCCno(),
            'cc_date': ccGen.creteCCDate(),
            'cc_cvv': ccGen.createCVV(),
            'balance': '75'}
        server = requests.post(url, data=form_data)
        output = server.text
        print("The payload ive sent \n", form_data)
        print('The response from the server is: \n', output)

thread1 = threading.Thread(target=sendRequest())

thread2 = threading.Thread(target=sendRequest())

thread3 = threading.Thread(target=sendRequest())
thread4 = threading.Thread(target=sendRequest())
thread5 = threading.Thread(target=sendRequest())




thread3.start()
thread2.start()
thread1.start()


thread1.join()
thread2.join()
thread3.join()

import random
from datetime import datetime
from time import sleep

from settings import collection


"""
This script generates random integer values between 0 and 100 and stores them in a MongoDB database, 
along with a server-generated timestamp. 
"""
while True:
    data = {
        'timestamp': datetime.now(),
        'value': random.randint(0, 100)
    }
    collection.insert_one(data)
    print(data)
    sleep(10)

__author__ = 'matthias'
import time

from tcp import *
from data import *

data = LaserData()

client = TCP()

for i in range(100,120):
    data.count_trigger = i

    client.send_client(data)
    time.sleep(0.5)
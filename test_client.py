__author__ = 'matthias'

from tcp import *
from data import *

SERVER = "131.225.237.31"
PORT = 33487

data = LaserData()
client = TCP(SERVER, PORT)

for i in range(100,120):
    data.count_trigger = i

    client.send_client(data)
    time.sleep(0.5)
__author__ = 'matthias'

from tcp import *
from data import *

#SERVER = "131.225.237.31"
#PORT = 33487

data = LaserData()
#client = TCP(SERVER, PORT)
client = TCP()

while client.start_clinet() is False:
    time.sleep(1)

for i in range(100,250):
    data.count_trigger = i
    client.send_client(data)
    time.sleep(1)

client.stop_client()
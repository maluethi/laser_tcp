__author__ = 'matthias'
from tcp import *
from data import *


server = TCP()
data = LaserData()

server.start_server()
for i in range(100):
    data = server.recv_server()

    print data
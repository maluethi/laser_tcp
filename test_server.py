__author__ = 'matthias'

from tcp import *
from data import *

SERVER = "131.225.237.31"
PORT = 33487

data = LaserData()
server = TCP(SERVER, PORT)

server.start_server()
for i in range(100):
    data = server.recv_server()

    print data
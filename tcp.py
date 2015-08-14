__author__ = 'matthias'

import socket
import sys

from data import *

DEBUG = False
class TCP(object):
    def __init__(self, server_name="localhost", port=10000):
        self.server_address = (server_name, port)
        self.laser_data = LaserData()


    def start_server(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(self.server_address)
        self.sock.listen(1)
        self.connection, self.client_address = self.sock.accept()


    def stop_server(self):
        self.connection.close()
        self.sock.shutdown()
        self.sock.close()

    def recv_server(self):

        print >> sys.stderr, 'waiting for a connection'
        try:
            print >> sys.stderr, 'client connected:', self.client_address
            data = self.connection.recv(60)
            if DEBUG:
                print >> sys.stderr, 'received "%s"' % data
            self.laser_data.fill(self.laser_data.unpack(data))
        finally:
            pass

        return self.laser_data

    def start_clinet(self):
        """ This starts a client connection  """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("", 10002))
        try:
            self.sock.connect(self.server_address)
        except Exception as e:
            print "Could not connect to server: " + str(e)
            return False
        return True

    def stop_client(self):
        self.sock.shutdown(1)
        self.sock.close()

    def send_client(self, data):
        self.laser_data = data
        packed_data = self.laser_data.pack()
        try:
            message = packed_data
            print >> sys.stderr, 'sending "%s"' % message
            self.sock.sendall(message)

            #data = self.sock.recv(len("OK"))
            #print >> sys.stderr, 'received "%s"' % data
        except Exception as e:
            print "Could not send data to server: " + str(e)
            print "trying to reopen the connection: "

            reconnected = False
            while reconnected is False:
                try:
                    reconnected = self.start_clinet()
                except Exception as e2:
                    print "error: " + str(e2)

                time.sleep(1)



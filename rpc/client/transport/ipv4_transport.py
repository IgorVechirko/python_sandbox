from rpc.client.transport.transport import Transport
from rpc.loger import Logger
from rpc.types.transport_type import TransportType
from rpc.client.protocol.protocol import Protocol
from rpc.client.transport.transport_task import TransportTask

import threading
import socket

class IPv4Transport(Transport):
    
    def __init__(self, protocol: Protocol):
        Transport.__init__(self, TransportType.IPv4, protocol)
        self._socket = None
        return

    def start(self, connection_params = {}):

        if(not "address" in connection_params):
            raise Exception("There's no IPv4 address")
        if(not "port" in connection_params):
            raise Exception("There's no IPv4 port")

        address = connection_params["address"]
        port = connection_params["port"]
        
        Logger.info("Connecting to: {}:{}...".format(address, port))

#        try:
#            self._socket = socket.create_connection((address,port))
#        except Exception as err:
#            raise Exception(err.args, "Can't connect to : {}:{}".format(address,port))

        Transport.start(self)


    def send_task(self, task: TransportTask):
        
        return

    def recv_loop(self, finish_loop_eve: threading.Event):
        return
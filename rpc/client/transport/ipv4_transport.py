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

    def start(self, connection_params = {}) -> bool:
        address = connection_params["address"]
        port = connection_params["port"]
        
        try:
            self._socket = socket.create_connection((address,port))
        finally:
            Logger.error("Can't connect to address: ", address, ":", port);
            return False

        if(self._socket == None):
            Logger.error("Can't connect to address: ", address, ":", port);
            return False

        return Transport.start(self)

    def send_task(self, task: TransportTask):
        
        return

    def recv_loop(self, finish_loop_eve: threading.Event):
        return
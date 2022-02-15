from rpc.client.transport.transport import Transport
from rpc.types.transport_type import TransportType

class IPv4Transport(Transport):
    
    def __init__(self):
        Transport.__init__(self, TransportType.IPv4)
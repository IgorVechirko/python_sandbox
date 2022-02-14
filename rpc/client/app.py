from rpc.client.factory import Factory
from rpc.client.protocol.protocol import ProtocolType
from rpc.client.transport.transport_type import TransportType

g_rpc_protocl = ProtocolType.JSON
g_transport_type = TransportType.IPv4


class App:
    
    def __init__(self):
        self.protocol_type = ProtocolType.JSON
        self.transport_info = TransportInfo()
        #self.input_method = Console()
        #self.transport = IPv4Transport()


        #if self.protocol_type == ProtocolType.UNDEF:
        #    print("Undefined protocol type")
        #    sys.exit(1)

        #self.transport = self.create_transport(self.transport_info)
        #if self.transport == None:
        #    print("Can't create transport")
        #    sys.exit(1)
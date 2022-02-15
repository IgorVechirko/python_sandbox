from rpc.client.protocol.serializer import Serializer
from rpc.types.protocol import ProtocolType

class JSONSerializer(Serializer):

    def __init__(self):
        Serializer.__init__(self, ProtocolType.JSON)
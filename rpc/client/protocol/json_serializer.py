from rpc.client.protocol.serializer import Serializer
from rpc.client.protocol.protocol import ProtocolType

class JSONSerializer(Serializer):

    def __init__(self):
        super(ProtocolType.JSON)
from rpc.client.protocol.parser import Parser
from rpc.client.protocol.protocol import ProtocolType

class JSONParser(Parser):
    def __init__(self):
        super(ProtocolType.JSON)
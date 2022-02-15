from rpc.client.protocol.parser import Parser
from rpc.types.protocol import ProtocolType

class JSONParser(Parser):
    def __init__(self):
        Parser.__init__(self,ProtocolType.JSON)
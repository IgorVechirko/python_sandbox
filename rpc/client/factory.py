from rpc.loger import Logger

from rpc.client.protocol.protocol import ProtocolType
from rpc.client.protocol.json_serializer import JSONSerializer
from rpc.client.protocol.json_parser import JSONParser

from rpc.client.transport.transport_type import TransportType
from rpc.client.transport.ipv4_transport import IPv4Transport

from rpc.client.io_method.console import Console

class Factory:
    def creat_serializer(self, protocol_type = ProtocolType.UNDEF) -> Serializer:
        if(protocol_type == ProtocolType.JSON):
            return JSONSerializer(protocol_type)
        else:
            Logger.error("Can't construct serializer type: ", protocol_type)
            return None

    def create_pareser(self, protocol_type = ProtocolType.UNDEF) -> Parser:
        if(protocol_type == ProtocolType.JSON):
            return JSONParser(protocol_type)
        else:
            Logger.error("Can't construct parser type: ", protocol_type)
            return None

    def create_transport(self, transport_type) -> Transport:
        if(transport_type == TransportType.IPv4):
            return IPv4Transport(transport_type)
        else:
            Logger.error("Can't construct transport type: ", transport_type)
            return None
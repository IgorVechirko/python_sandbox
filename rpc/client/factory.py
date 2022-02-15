from rpc.loger import Logger

from rpc.types.protocol import ProtocolType
from rpc.client.protocol.serializer import Serializer
from rpc.client.protocol.json_serializer import JSONSerializer
from rpc.client.protocol.parser import Parser
from rpc.client.protocol.json_parser import JSONParser

from rpc.types.transport_type import TransportType
from rpc.client.transport.transport import Transport
from rpc.client.transport.ipv4_transport import IPv4Transport

from rpc.client.io_method.io_method import IOMethod
from rpc.types.io_type import IOType
from rpc.client.io_method.console import Console

class Factory:
    def creat_serializer(protocol_type = ProtocolType.UNDEF) -> Serializer:
        if(protocol_type == ProtocolType.JSON):
            return JSONSerializer()
        else:
            Logger.error("Can't construct serializer type: ", protocol_type)
            return None

    def create_pareser(protocol_type = ProtocolType.UNDEF) -> Parser:
        if(protocol_type == ProtocolType.JSON):
            return JSONParser()
        else:
            Logger.error("Can't construct parser type: ", protocol_type)
            return None

    def create_transport(transport_type) -> Transport:
        if(transport_type == TransportType.IPv4):
            return IPv4Transport()
        else:
            Logger.error("Can't construct transport type: ", transport_type)
            return None

    def create_io_method(io_type) -> IOMethod:
        if(io_type == IOType.CONSOLE):
            return Console()
        else:
            Logger.error("Can't construct ioMethod type: ", io_type)
            return None

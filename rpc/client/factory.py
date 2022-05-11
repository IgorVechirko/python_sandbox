from rpc.loger import Logger
from rpc import utils

from rpc.types.protocol import ProtocolType
from rpc.client.protocol.protocol import Protocol
from rpc.client.protocol.json_protocol import JsonProtocol

from rpc.types.transport_type import TransportType
from rpc.client.transport.transport import Transport
from rpc.client.transport.ipv4_transport import IPv4Transport

from rpc.client.io_method.io_method import IOMethod
from rpc.types.io_type import IOType
from rpc.client.io_method.cli_args import CliArgs

class Factory:

    def create_protocol(self, protocol_type: ProtocolType) -> Protocol:
        if(protocol_type == ProtocolType.JSON):
            return JsonProtocol()
        else:
            Logger.error("Can't construct parser type: ", protocol_type)
            return None

    def create_transport(self, transport_type: TransportType, protocol: Protocol) -> Transport:
        if(transport_type == TransportType.IPv4):
            return IPv4Transport(protocol)
        else:
            Logger.error("Can't construct transport type: ", transport_type)
            return None

    def create_io_method(self, io_type: IOType) -> IOMethod:
        if(io_type == IOType.CLI_ARGUMENTS):
            return CliArgs()
        else:
            Logger.error("Can't construct ioMethod type: ", io_type)
            return None

from rpc import utils
from rpc.loger import Logger
from rpc.client.factory import Factory
from rpc.types.protocol import ProtocolType
from rpc.types.transport_type import TransportType
from rpc.types.io_type import IOType

g_rpc_protocl = ProtocolType.JSON
g_transport_type = TransportType.IPv4
g_io_type = IOType.CONSOLE


class App:
    
    def __init__(self):
        self._serializer = Factory.creat_serializer(g_rpc_protocl);
        utils.fatal_none(self._serializer)
        self._parser = Factory.create_pareser(g_rpc_protocl);
        utils.fatal_none(self._parser)

        self._transport = Factory.create_transport(g_transport_type)
        utils.fatal_none(self._transport)

        self._io_method = Factory.create_io_method(g_io_type)
        utils.fatal_none(self._io_method)


    def run(self):
        while(True):
            input = self._io_method.get_input()
            Logger.error("Get input: ", input)
            Logger.error("Procedure: ", self._io_method.get_procedure(input))


from rpc import utils

from rpc.loger import Logger
from rpc.types.protocol import ProtocolType
from rpc.types.transport_type import TransportType
from rpc.types.io_type import IOType

from rpc.client.factory import Factory
from rpc.client.configuration import Configuration

import time



class App:
    
    def __init__(self):

        config = self._configuration = Configuration()
        config._protocol = ProtocolType.JSON
        config._transport_type = TransportType.IPv4
        config._io_type = IOType.CLI_ARGUMENTS
        config._transport_params["address"] = "127.0.0.1"
        config._transport_params["port"] = 9999

        factory = self._factory = Factory()

        self._protocol = factory.create_protocol(config._protocol);
        utils.fatal_none(self._protocol)

        self._transport = factory.create_transport(config._transport_type, self._protocol)
        utils.fatal_none(self._transport)

        self._io_method = factory.create_io_method(config._io_type, self._transport)
        utils.fatal_none(self._io_method)


    def run(self):
        try:
            self._io_method.start()
        except Exception as err:
            raise Exception(err.args, "Can't connect transport")

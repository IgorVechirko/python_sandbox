from rpc.types.io_type import IOType
from rpc.types.protocol import ProtocolType
from rpc.types.transport_type import TransportType

class Configuration:
    def __init__(self):
        self._io_type = IOType.UNDEF
        self._protocol = ProtocolType.UNDEF
        self._transport_type = TransportType.UNDEF
        self._transport_params = {}

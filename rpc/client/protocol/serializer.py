from rpc import utils
from rpc.client.protocol.protocol import ProtocolType

class Serializer:
    def __init__(self, protocol_type = ProtocolType.UNDEF):
        self._protocol_type = protocol_type

    def procedure_to_data(self, procedure) -> bytearray:
        utils.unimpl_meth()
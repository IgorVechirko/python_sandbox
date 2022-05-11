from rpc import utils
from rpc.types.protocol import ProtocolType
from rpc.types.procedure import Procedure, ProcedureResponse

class Protocol:
    def __init__(self, protocol_type: ProtocolType):
        self._protocol_type = protocol_type
        return

    def serialize_to_bytearray(self, procedure: Procedure) -> bytearray:
        utils.unimpl_meth()
        return

    def parse_from_bytearray(slef, bytes: bytearray) -> ProcedureResponse:
        utils.unimpl_meth()
        return
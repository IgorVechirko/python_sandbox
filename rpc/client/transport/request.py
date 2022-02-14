from rpc import utils
from rpc.client.procedure.procedure import Procedure

class Request:
    def __init__(self, procedure = Procedure(), serializer = Serializer()):
        self._serializer = serializer
        self._procedure = procedure

    def header_data(self) -> bytearray:
        utils.unimpl_meth()

    def pdu_data(self) -> bytearray:
        utils.unimpl_meth()
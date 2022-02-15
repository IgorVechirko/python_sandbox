from rpc import utils

class Serializer:
    def __init__(self, protocol_type):
        self._protocol_type = protocol_type

    def procedure_to_data(self, procedure) -> bytearray:
        utils.unimpl_meth()
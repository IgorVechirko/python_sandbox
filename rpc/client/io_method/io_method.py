from rpc import utils
from rpc.types.procedure from

class IOMethod:
    def __init__(self, io_type):
        self._io_type = io_type

    def get_procedure(self, io_type):
        utils.unimpl_meth()

    def put_result(self, result):
        utils.unimpl_meth()
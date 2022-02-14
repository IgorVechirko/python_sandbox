from rpc import utils
from rpc.client.io_method.io_type import IOType

class IOMethod:
    def get_procedure(self, io_type = IOType.UNDEF):
        self._io_type = io_type

    def put_result(self, result):
        utils.unimpl_meth()
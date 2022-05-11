from rpc import utils
from rpc.types.io_type import IOType
from rpc.types.procedure import Procedure, ProcedureResponse


class IOMethod:
    def __init__(self, io_type: IOType):
        self._io_type = io_type

    def put_procedure(self, procedure: Procedure, resp_handler):
        pass

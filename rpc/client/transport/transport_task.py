from rpc import utils
from rpc.types.procedure import Procedure, ProcedureResponse

class TransportTask:
    def __init__(self, procedure: Procedure, response_handler):
        self._procedure = procedure
        self._procedure_response = ProcedureResponse()
        self._response_handler = response_handler
        self._result = 0
        #rpc version
        #rpc protocol
        #procedure id
        #msg size

        #response structure
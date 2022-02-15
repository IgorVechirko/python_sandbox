from rpc import utils
from rpc.client.procedure.procedure import ProcedureResult

class Parser:
    def __init__(self, protocol_type):
        self._protocol_type = protocol_type

    def parse_response(response_data) -> ProcedureResult:
        utils.unimpl_meth()
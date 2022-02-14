from rpc.client.transport.request import Request
from rpc.client.protocol.parser import Parser

class Response:
    def __init__(self, request = Request(), parser = Parser()):
        self._request = request
        self._parser = parser

    def procedure_result() -> ProcedureResult:
        utils.unimpl_meth()
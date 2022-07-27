from rpc import utils
from rpc.types.io_type import IOType
from rpc.types.procedure import Procedure, ProcedureResponse
from rpc.client.transport.transport import Transport
from rpc.loger import Logger


class IOMethod:
    def __init__(self, io_type: IOType, transport: Transport):
        self._io_type = io_type
        self._transport = transport

    def start(self):
        Logger.info("IO start")

    def put_procedure(self, procedure: Procedure, resp_handler):
        Logger.info("Send {} procedure, with {} params".format(procedure._name, procedure._params))

        self._transport.send_procedure(procedure, resp_handler)

from rpc import utils
from rpc.client.transport.transport_type import TransportType

class Transport:
    def __init__(self, transport_type = TransportType.UNDEF):
        self._transport_type = transport_type

    def send_request(self, request):
        utils.unimpl_meth()
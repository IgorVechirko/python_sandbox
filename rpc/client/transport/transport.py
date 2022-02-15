from rpc import utils

class Transport:
    def __init__(self, transport_type):
        self._transport_type = transport_type

    def send_request(self, request):
        utils.unimpl_meth()
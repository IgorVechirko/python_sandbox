import sys
from enum import Enum
import utils

from loger import Logger

class ProtocolType(Enum):
    UNDEF = 0
    JSON = 1

class TransportType(Enum):
    UNDEF = 0
    IPv4 = 1


class Procedure:
    def __init__(self, name = "", params = {}):
        self._name = name
        self._params = params

class ProcedureResult:
    def __init__(self, result_fields = {}):
        self._result_fields = result_fields

class Serializer:
    def __init__(self, protocol_type = ProtocolType.UNDEF):
        self._protocol_type = protocol_type

    def procedure_to_data(self, procedure) -> bytearray:
        utils.unimplement_method()

class JSONSerializer(Serializer):
    pass

class Request:
    def __init__(self, procedure = Procedure(), serializer = Serializer()):
        self._serializer = serializer
        self._procedure = procedure

    def header_data(self) -> bytearray:
        utils.unimplement_method()

    def pdu_data(self) -> bytearray:
        utils.unimplement_method()

class Transport:
    def __init__(self, transport_type = TransportType.UNDEF):
        self._transport_type = transport_type

    def send_request(self, request):
        utils.unimplement_method()

class IPv4Transport(Transport):
    pass


class Parser:
    def __init__(self, protocol_type = ProtocolType.UNDEF):
        self._protocol_type = protocol_type

    def parse_response(response_data) -> ProcedureResult:
        utils.unimplement_method()

class JSONParser(Parser):
    pass

class Response:
    def __init__(self, request = Request(), parser = Parser()):
        self._request = request
        self._parser = parser

    def procedure_result() -> ProcedureResult:
        utils.unimplement_method()


class IOMethod:
    def get_procedure(self):
        utils.unimplement_method()

    def put_result(self, result):
        utils.unimplement_method()
    
class Console(IOMethod):
    def get_procedure(self):
        method = sys.argv[1]
        params = {}
        
        cli_arg_indx = 2
        while cli_arg_indx < len(sys.argv):
            find_pos = sys.argv[cli_arg_indx].find("--")
            
            if find_pos != -1:
                param_name = sys.argv[cli_arg_indx][find_pos+2:]
                
                if len(sys.argv) >= cli_arg_indx+2:
                    find_pos = sys.argv[cli_arg_indx+1].find("--")
                    
                    if find_pos == -1:
                        params[param_name] = sys.argv[cli_arg_indx+1]
                        cli_arg_indx+=2
                    else:
                        params[param_name] = ""
                        cli_arg_indx+=1
                else:
                    params[param_name] = ""
                    cli_arg_indx+=1
            else:
                print("Wrong parameter notation")
                break
        
        return (method, params)

    def put_result(self, result):
        print(result)

class Factory:
    def creat_serializer(self, protocol_type = ProtocolType.UNDEF) -> Serializer:
        utils.unimplement_method()

    def create_pareser(self, protocol_type = ProtocolType.UNDEF) -> Parser:
        utils.unimplement_method()

    def create_transport(self, transport_type) -> Transport:
        utils.unimplement_method()

class App:
    
    def __init__(self):
        self.protocol_type = ProtocolType.JSON
        #self.transport_info = TransportInfo()
        self.input_method = Console()
        self.transport = IPv4Transport()

        if self.protocol_type == ProtocolType.UNDEF:
            print("Undefined protocol type")
            sys.exit(1)

        #self.transport = self.create_transport(self.transport_info)
        if self.transport == None:
            print("Can't create transport")
            sys.exit(1)

    def create_transport(self, transport_info) -> Transport:
        return Transport()
    
    def create_serializer(self):
        pass



app = App()
print(app.input_method.get_procedure())

import sys
import enum

class ProtocolType(enum.Enum):

    UNDEF = 0
    JSON = 1

class TransportInfo:
    pass

class Header:

    def __init__(self):
        self.data_size = 0
        self.protocol_type = ProtocolType.UNDEF
        data = bytearray()

class Serializer:
    pass

class Request:

    def __init__(self, serializer):
        self.header = Header()
        self.serializer = serializer

class Response:
    pass

class Transport:
    
    def send_request(self, request, completer):
        pass

class IOMethod:
    
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

class App:
    
    def __init__(self):
        
        self.protocol_type = ProtocolType.JSON
        self.transport_info = TransportInfo()
        self.input_method = IOMethod()

        if self.protocol_type == ProtocolType.UNDEF:
            print("Undefined protocol type")
            sys.exit(1)

        self.transport = self.create_transport(self.transport_info)
        if self.transport == None:
            print("Can't create transport")
            sys.exit(1)

    def create_transport(self, transport_info) -> Transport:
        return Transport()
    
    def create_serializer(self):
        pass


class Pet:
    def __init__(self):
        print("Pet constructed")

    def voice(self):
        pass

class Dog(Pet):
    def __init__(self):
        Pet.__init__(super)
        print("Dog constructed")

    def voice(self):
        print("Waf Waf Waf")

class Cat(Pet):
    def __init__(self):
        Pet.__init__(self)
        print("Cat constructed")

    def voice(self):
        print("Mayu mayu mayu")


#app = App()
#print(app.input_method.get_procedure())

pets = (Dog(), Cat(), Pet())

for pet in pets:
    pet.voice()


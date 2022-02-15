from rpc.client.io_method.io_method import IOMethod
from rpc.types.io_type import IOType

class Console(IOMethod):
    def __init__(self):
        IOMethod.__init__(self, IOType.CONSOLE)

    def get_input(self) -> str:
        return "first --second third"


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
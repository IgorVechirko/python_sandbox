from rpc.client.app import App

app = App()

def print_complex_except(except_args):
    for arg in except_args:
        if type(arg) is str:
            print(arg)
        elif isinstance(arg, tuple):
            print_complex_except(arg)

try:
	app.run()
except Exception as err:
    print_complex_except(err.args)

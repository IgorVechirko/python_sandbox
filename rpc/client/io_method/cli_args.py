from rpc.client.io_method.io_method import IOMethod
from rpc.types.io_type import IOType

class CliArgs(IOMethod):

	def __init__(self):
		IOMethod.__init__(self, IOType.CLI_ARGUMENTS)
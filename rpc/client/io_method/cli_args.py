import argparse

from rpc.client.io_method.io_method import IOMethod
from rpc.types.io_type import IOType
from rpc.client.transport.transport import Transport
from rpc.loger import Logger


class CliArgs(IOMethod):

    def __init__(self, transport: Transport):
        IOMethod.__init__(self, IOType.CLI_ARGUMENTS, transport)

    def start(self):
        Logger.info("Start cli_args IoMethod")

        parser = argparse.ArgumentParser()
        parser.add_argument("command")
        parser.add_argument("args", nargs=argparse.REMAINDER)
        Logger.info(parser.parse_args("first --second val --third val".split()))

        #Logger.info(parser.parse_args())

        IOMethod.start(self)
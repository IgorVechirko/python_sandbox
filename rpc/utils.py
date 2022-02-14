import sys

from rpc.loger import Logger

def unimpl_meth():
	Logger.error("Unimplemented method");
	sys.exit(1)
import sys

from rpc.loger import Logger

def unimpl_meth():
	Logger.error("Unimplemented method");
	sys.exit(1)

def fatal_none(val):
	if(val == None):
		Logger.error("result valut is NONE")
		sys.exit(1)
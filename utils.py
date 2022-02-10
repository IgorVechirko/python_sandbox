import sys

from loger import Logger

def unimplement_method():
	Logger.error("Unimplemented method");
	sys.exit(1)
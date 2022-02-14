
class Logger(object):
    '''Layer for user to controll logging output'''

    def debug(msg, *args, **kwargs):
        print(msg.format(args, kwargs))

    def info(msg, *args, **kwargs):
        print(msg.format(args, kwargs))

    def warning(msg, *args, **kwargs):
        print(msg.format(args, kwargs))

    def error(msg, *args, **kwargs):
        print(msg.format(args, kwargs))
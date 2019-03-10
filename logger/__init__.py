from strategy import ConsoleLogger


class Logger(object):
    def __init__(self, strategy=None):
        if not strategy:
            self.strategy = ConsoleLogger()
        else:
            self.strategy = strategy

    def log(self, text):
        self.strategy.log(text)


logger = Logger()

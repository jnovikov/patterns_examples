from strategy import ConsoleLogger, FileLogger
from logger import logger


class Logger(object):
    instance = None

    def __init__(self):
        self.strategy = ConsoleLogger()
        Logger.instance = self
        if Logger.instance:
            raise ValueError("Already exists")

    def log(self, text):
        self.strategy.log(text)

    @staticmethod
    def get():
        if Logger.instance:
            return Logger.instance
        else:
            i = Logger()
            return i


# l = Logger.get()
# l.strategy = FileLogger("log.txt")
logger.strategy = FileLogger("log.txt")


class Calculator(object):
    @staticmethod
    def add(a, b):
        # log = Logger.get()
        # log.log("a + b = " + str(a + b))
        logger.log("a + b = " + str(a + b))
        return a + b

    @staticmethod
    def sub(a, b):
        # log = Logger.get()
        # log.log("a - b = " + str(a - b))
        logger.log("a - b = " + str(a - b))
        return a - b


Calculator.add(10, 20)
Calculator.sub(20, 10)

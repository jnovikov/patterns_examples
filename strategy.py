class LoggerStrategy(object):
    def log(self, text):
        raise NotImplementedError("Implement log")


class ConsoleLogger(LoggerStrategy):
    def log(self, text):
        print(text)


class FileLogger(LoggerStrategy):
    def __init__(self, filename):
        self.filename = filename

    def log(self, text):
        f = open(self.filename, 'a')
        f.write(text + '\n')
        f.close()


class CompositeLogger(LoggerStrategy):
    def __init__(self, log1, log2):
        self.log1 = log1
        self.log2 = log2

    def log(self, text):
        self.log1.log(text)
        self.log2.log(text)


class Application(object):
    def __init__(self, logger):
        self.logger = logger

    def calc_sum(self, a, b):
        message = "Started calculation " + str(a) + " + " + str(b)
        self.logger.log(message)
        s = a + b
        message = str(a) + " + " + str(b) + " = " + str(s)
        self.logger.log(message)
        return s


log1 = FileLogger("log.txt")
a = Application(log1)
print(a.calc_sum(1, 2))
a.logger = ConsoleLogger()
print(a.calc_sum(-1, 1))

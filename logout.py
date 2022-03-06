from logging import getLogger, StreamHandler, DEBUG ,handlers, Formatter

class Logger:
    def __init__(self, name=__name__):
        self.logger = getLogger(__name__)
        #formatter = Formatter("[%(asctime)s] [%(process)d] [%(name)s] [%(levelname)s] %(message)s")
        formatter = Formatter("[%(asctime)s] %(message)s")
        handler = StreamHandler()
        handler.setLevel(DEBUG)
        handler.setFormatter(formatter)
        self.logger.setLevel(DEBUG)
        #コンソール出力不要のなためコメントアウト
        #self.logger.addHandler(handler)
        self.logger.propagate = False

        handler = handlers.RotatingFileHandler(filename = 'xlsx2pdf.log')
        #                                               maxBytes = 1048576,
        #                                             backupCount = 3)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self,msg):
        self.logger.info(msg)
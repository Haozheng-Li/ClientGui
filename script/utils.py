import time
import logging
from PySide6.QtCore import QFileInfo

logging.basicConfig(level=logging.INFO)


def Log(func):
    def InnerFunction(*args, **kwargs):
        begin_time = time.time()
        logging.debug(' Begin func: {}'.format(func.__name__))
        result = func(*args, **kwargs)
        logging.debug(' End func: {}, time consuming: {}s'.format(func.__name__, time.time()-begin_time))
        return result
    return InnerFunction


def getRootPath():
    return QFileInfo(__file__).absolutePath() + '/../'
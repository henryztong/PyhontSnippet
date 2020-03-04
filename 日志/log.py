import os
import sys
import datetime
from logging import getLogger, INFO, Formatter
from cloghandler import ConcurrentRotatingFileHandler
reload(sys)
sys.setdefaultencoding('utf8')


def get_log_object(file_name=None):
    if not os.path.isdir('log'):
        os.mkdir('log')
    if not file_name:
        file_name = os.path.basename(sys.argv[0]).replace('.py', '')
        # print(os.path.basename(__file__).replace('.py', ''))
        # print(os.path.basename(sys.argv[0]).replace('.py', ''))
    log_file_name = '%s-%s.log' % (file_name, datetime.date.today())
    log_full_file_name = os.path.join('log', log_file_name)

    log = getLogger()
    rotateHandler = ConcurrentRotatingFileHandler(
        log_full_file_name, "a", 0, 0, 'utf-8')

    datefmt_str = '%Y-%m-%d %H:%M:%S'
    format_str = "[%(asctime)s - %(levelname)s - %(filename)s - LINE:%(lineno)d] %(message)s"
    formatter = Formatter(format_str, datefmt_str)
    rotateHandler.setFormatter(formatter)
    log.addHandler(rotateHandler)
    log.setLevel(0)
    return log


log = get_log_object()

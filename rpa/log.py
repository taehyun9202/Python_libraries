import logging
from datetime import datetime
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')
# logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
# logging.debug('!!!')
# logging.info('ready')
# logging.warning('need update')
# logging.error('error occured')
# logging.critical('serious error')


# leave log in terminal and file
logFormatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger()
# set log level
logger.setLevel(logging.DEBUG)

# stream (terminal)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# file
filename = datetime.now().strftime('mylogfile_%Y%m%d%H%M%S.log')
filehandler = logging.FileHandler(filename, encoding='utf-8')
filehandler.setFormatter(logFormatter)
logger.addHandler(filehandler)

logger.debug('test start')
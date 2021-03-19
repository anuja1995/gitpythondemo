import logging
from logging.handlers import TimedRotatingFileHandler
from loggers.sample_logger_proj.mydbhandler import MyDBHandler   # customer Handler

# logging.basicConfig(filename='sample.log',filemode='a', level=logging.INFO,
#                     format='%(funcName)s- %(lineno)d - %(asctime)s %(created)f -%(module)s- %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  #generic for medium

# redirect your output to console
consoleHandler = logging.StreamHandler()     # console flush out the memory
consoleHandler.setLevel(logging.INFO)   # only for console
consoleHandler.setFormatter(logging.Formatter('%(funcName)s- %(lineno)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s'))

# if we use only one log file for loggers, for larger applications it might create problem
fileHandler = logging.FileHandler(filename='file_handler_log.log') # redirect your output to file_handler_log file
fileHandler.setLevel(logging.INFO) # only for file
fileHandler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d - %(funcName)s'))

# redirect output the file but on the basis of time
timeFileHandler = TimedRotatingFileHandler('timeFileHandler.log',when='M',backupCount=10)
timeFileHandler.setLevel(logging.INFO)
timeFileHandler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d - %(funcName)s'))

# redirect your lg to database

dbHandler = MyDBHandler()
dbHandler.setLevel(logging.INFO)
dbHandler.setFormatter(logging.Formatter('%(levelname)s - %(message)s - %(lineno)d  - %(created)s - %(funcName)s'))

logger.addHandler(consoleHandler)   #   Console
logger.addHandler(fileHandler)      #   timeFileHandler --> one file only
logger.addHandler(timeFileHandler)  #   timeFileHandler file --> per minute new file  --> only 10 files holds in backup.
                                    # if 11th file is generated 1st file will be deleted
logger.addHandler(dbHandler)        # database handler

import time
def function_one():
    # while True:
    for item in range(1000000):
        logger.info('this is info msg-20')
        logger.debug('this is debug msg-10')
        logger.warning('this is warning msg-30')
        logger.error('this is error msg-40')
        logger.critical('this is critical msg-50')
        time.sleep(2)  # every 2 seconds--> 1 iteration. 30 iteration 1 file generated
        logger.info('Iteration No :'+str(item))
        # ch = input('Do you want to continue..')
        # if ch.lower() in ('yes','y'):
        #     continue
        # else:
        #     break

if __name__ == '__main__':
    function_one()
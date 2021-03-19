import logging
import sys

# Using Handlers

# Create a custom logger
logger = logging.getLogger(__name__)  #own logger

# create Handlers
c_handler = logging.StreamHandler()  #Handler 1
f_handler = logging.FileHandler('file.log') # Handler 2

# set level
c_handler.setLevel(logging.WARNING)  # set level for handler 1
f_handler.setLevel(logging.ERROR)  # set level for handler 2

# create a formatters and add into handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')  # formatter 1
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # formatter 2
c_handler.setFormatter(c_format)  # assing formatter 1 to handler 1
f_handler.setFormatter(f_format) # assign formatter 2 to handler 2

# add handler to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is warning')
logger.error('This is error')




sys.exit(0)

# ----------------------------------------------------------------------------------------------------

# Classes and Functions -- Logger,LogRecord,Handler,Formatter

# logger = logging.getLogger('example_logger')
# logging.warning('This is a warning')
# OR
logger = logging.getLogger('example_logger')
logging.basicConfig(format=f'{logger} : %(message)s',level=logging.WARNING)
logging.warning('This is a warning')

# ----------------------------------------------------------------------------------------------------
# Capturing Stack Traces
a=5
b=0

try:
    c = a/b
except Exception as e:
    # logging.error("Exception Occured",exc_info=True)
    # OR
    logging.exception('Exception Occured')

    # logging.error('Exception Occured')  # only returns--> ERROR:root:Exception occurred
# ----------------------------------------------------------------------------------------------------
# Logging Variable Data

name = 'john'
logging.error('%s raised an error', name)
logging.error(f'{name} raised an error')

# ----------------------------------------------------------------------------------------------------
# Formatting the Output
# logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
# logging.warning('This is warning')

# logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
# logging.info('Admin logged in')

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt= '%d-%b-%y %H:%M:%S')
logging.warning('Admin logged out')

# ---------------------------------------------------------------------------------------------------------
# Basic Configurations

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('this will get logged to a file')

# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This will get logged')

# ---------------------------------------------------------------------------
# The Logging Module

# logging.debug('This is a debug message')
# logging.info('This is a info message')
# logging.warning('This is a warning message')
# logging.error('This is a error message')
# logging.critical('This is a critical message')
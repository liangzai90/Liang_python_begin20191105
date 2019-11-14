print("-----一个使用了 logging 的程序----")

import logging
logging.basicConfig(level=logging.INFO, filename='mylog.log')

logging.info("Starting program")
logging.info('Trying to drive 1 by 0')
print(1/0)
logging.info("The division successed")
logging.info("Ending program")

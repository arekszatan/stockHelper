import logging
from datetime import datetime
from mainFront import start_application

if __name__ == "__main__":
    logName = 'log/' + datetime.today().strftime('%Y_%m_%d_logging.log')
    logging.basicConfig(level=logging.DEBUG, filename=logName, filemode='w',
                        format='%(asctime)s::%(levelname)s >>> %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')
    logging.info('Starting application stockHelper...')
    start_application()

import control as c
import logging
ENC = 'utf-8'
FORMAT_INFO = '%(asctime)s, %(module)s, %(funcName)s, %(name)s, --> %(message)s'

logging.basicConfig(format=FORMAT_INFO, filename='DZ/DZ_8/log_info.txt',
                    filemode='a', encoding=ENC, level=logging.INFO, datefmt='%m/%d/%Y %H:%M:%S')
c.click_button()


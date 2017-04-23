''' Fast logging by Oksovskii,  Phonphey'''

import logging  # импорт библиотеки logging

# Задаём формат выводимой строки
logging.basicConfig(
    format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level=logging.DEBUG)

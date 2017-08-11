#/usr/bin/env python
#coding=utf-8

import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
    datafmt = "%a, %d %b %Y %H:%M:%S",
    filename = "test.log",
    filemode = 'a'
)
logging.debug("dubug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")

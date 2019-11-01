import logging


def debug(nm, msg):
    logging.getLogger(nm).debug(msg)


def info(nm, msg):
    logging.getLogger(nm).info(msg)


def error(nm, msg):
    logging.getLogger(nm).error(msg)

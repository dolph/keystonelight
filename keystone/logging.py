# vim: tabstop=4 shiftwidth=4 softtabstop=4

"""Wrapper for built-in logging module."""

from __future__ import absolute_import

import functools
import logging
import pprint

from logging.handlers import SysLogHandler
from logging.handlers import WatchedFileHandler

# A list of things we want to replicate from logging.
# levels
CRITICAL = logging.CRITICAL
FATAL = logging.FATAL
ERROR = logging.ERROR
WARNING = logging.WARNING
WARN = logging.WARN
INFO = logging.INFO
DEBUG = logging.DEBUG
NOTSET = logging.NOTSET


# methods
getLogger = logging.getLogger
debug = logging.debug
info = logging.info
warning = logging.warning
warn = logging.warn
error = logging.error
exception = logging.exception
critical = logging.critical
log = logging.log

# classes
root = logging.root
Formatter = logging.Formatter

# handlers
StreamHandler = logging.StreamHandler
WatchedFileHandler = WatchedFileHandler
SysLogHandler = SysLogHandler


def log_debug(f):
  @functools.wraps(f)
  def wrapper(*args, **kw):
    logging.debug('%s(%s, %s) ->', f.func_name, str(args), str(kw))
    rv = f(*args, **kw)
    logging.debug(pprint.pformat(rv, indent=2))
    logging.debug('')
    return rv
  return wrapper

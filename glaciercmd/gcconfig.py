import logging
import os
from ConfigParser import SafeConfigParser
from ConfigParser import NoOptionError

class GCConfig(SafeConfigParser):
  _error_messages = []

  def __init__(self):
    SafeConfigParser.__init__(self)

    conf_file = os.path.expanduser('~/.glaciercmd')
    if os.path.isfile(conf_file):
      self.read(conf_file)
    else:
      self._error_messages.append("Could not locate the .glaciercmd configuration file.")

  def has_errors(self):
    required_options = ['aws_key', 'aws_secret']

    for required_option in required_options:
      try:
        self.get('configuration', required_option)
      except NoOptionError:
        self._error_messages.append("The configuration key '{0}' was not found in the configuration file.".format(required_option))

    return len(self._error_messages) > 0

  def log_errors(self):
    for error_message in self._error_messages:
      logging.error(error_message)

import logging 
import sys

from glaciercmd.gcconfig import GCConfig

def run():
  logging.basicConfig(format="%(asctime)s %(levelname)s %(module)s: %(message)s", level=logging.DEBUG)

  config = GCConfig()
  if config.has_errors():
    config.log_errors()
    sys.exit(1)

if __name__ == '__main__':
  run()

import logging

def run():
  logging.basicConfig(format="%(asctime)s %(levelname)s %(module)s: %(message)s", level=logging.DEBUG)

if __name__ == '__main__':
  run()

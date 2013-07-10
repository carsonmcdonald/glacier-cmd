import logging 
import sys
import argparse
import glob
import os

from glaciercmd.gcconfig import GCConfig

def load_commands():
  commands = []

  command_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'command_*.py')
  command_files = glob.glob(command_dir)
  for command_file in command_files:
    command = __import__("glaciercmd.{0}".format(os.path.splitext(os.path.basename(command_file))[0]), globals(), locals(), ['command_init'])
    commands.append(command.command_init())

  return commands

def run():
  logging.basicConfig(format="%(asctime)s %(levelname)s %(module)s: %(message)s", level=logging.INFO)

  commands = load_commands()

  config = GCConfig()
  if config.has_errors():
    config.log_errors()
    sys.exit(1)

  parser = argparse.ArgumentParser(add_help=False)
  parser.add_argument('args', nargs='*')

  parsed_args = parser.parse_args()

  found_command = False
  for command in commands:
    if command.accept(parsed_args.args):
      command.execute(parsed_args.args, config)
      found_command = True

  if not found_command:
    logging.error('No valid command found.');

if __name__ == '__main__':
  run()

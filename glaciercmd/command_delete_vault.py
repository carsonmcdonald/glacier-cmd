import boto
from boto.glacier.exceptions import UnexpectedHTTPResponseError

class CommandDeleteVault(object):

  def execute(self, args, config):
    glacier_connection = boto.connect_glacier(aws_access_key_id=config.get('configuration', 'aws_key'), aws_secret_access_key=config.get('configuration', 'aws_secret'))

    try:
      vault = glacier_connection.get_vault(args[2])
    except:
      vault = None

    if vault is None:
      print "Vault named '{}' does not exist.".format(args[2])
    else:
      try:
        vault = glacier_connection.delete_vault(args[2])
        print "Vault deleted: '{}'".format(args[2])
      except UnexpectedHTTPResponseError as error:
        print "Vault can not be deleted:\n\t {}".format(error)

  def accept(self, args):
    return len(args) >= 3 and args[0] == 'delete' and args[1] == 'vault'

  def help(self):
    return "delete vault <vault name>"

def command_init():
  return CommandDeleteVault()

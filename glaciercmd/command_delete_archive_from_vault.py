import boto
from boto.glacier.exceptions import UnexpectedHTTPResponseError

class CommandDeleteArchiveFromVault(object):

  def execute(self, args, config):
    glacier_connection = boto.connect_glacier(aws_access_key_id=config.get('configuration', 'aws_key'), aws_secret_access_key=config.get('configuration', 'aws_secret'))

    try:
      vault = glacier_connection.get_vault(args[4])
    except:
      vault = None

    if vault is None:
      print "Vault named '{}' does not exist.".format(args[4])
    else:
      try:
        vault.delete_archive(args[2])
        print "Archive deleted: '{}'".format(args[2])
      except UnexpectedHTTPResponseError as error:
        print "Archive can not be deleted:\n\t {}".format(error)

  def accept(self, args):
    return len(args) >= 4 and args[0] == 'delete' and args[1] == 'archive' and args[3] == 'from'

  def help(self):
    return "delete archive <archive name> from <vault name>"

def command_init():
  return CommandDeleteArchiveFromVault()

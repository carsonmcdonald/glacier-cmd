import boto
import datetime

class CommandCreateInventoryJobForVault(object):

  def execute(self, args, config):
    glacier_connection = boto.connect_glacier(aws_access_key_id=config.get('configuration', 'aws_key'), aws_secret_access_key=config.get('configuration', 'aws_secret'))

    try:
      vault = glacier_connection.get_vault(args[5])
    except:
      vault = None

    if vault is None:
      print "Vault named '{}' does not exist.".format(args[5])
    else:
      job_id = vault.retrieve_inventory()
      print "Inventory job initiated with ID {}".format(job_id)

  def accept(self, args):
    return len(args) >= 6 and args[0] == 'create' and args[1] == 'inventory' and args[2] == 'job' and args[3] == 'for' and args[4] == 'vault'

  def help(self):
    return "create inventory job for vault <vault name>"

def command_init():
  return CommandCreateInventoryJobForVault()

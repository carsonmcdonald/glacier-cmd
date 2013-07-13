import boto

class CommandVaultInfo(object):

  def execute(self, args, config):
    glacier_connection = boto.connect_glacier(aws_access_key_id=config.get('configuration', 'aws_key'), aws_secret_access_key=config.get('configuration', 'aws_secret'))

    try:
      vault = glacier_connection.get_vault(args[2])
      print "Vault info:\n\tname={}\n\tarn={}\n\tcreation_date={}\n\tlast_inventory_date={}\n\tsize={}\n\tnumber_of_archives={}".format(vault.name, vault.arn, vault.creation_date, vault.last_inventory_date, vault.size, vault.number_of_archives)
    except:
      print "Vaule named '{}' does not exist.".format(args[2])

  def accept(self, args):
    return len(args) >= 3 and args[0] == 'vault' and args[1] == 'info'

def command_init():
  return CommandVaultInfo()

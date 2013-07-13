import boto

class CommandCreateVault(object):

  def execute(self, args, config):
    glacier_connection = boto.connect_glacier(aws_access_key_id=config.get('configuration', 'aws_key'), aws_secret_access_key=config.get('configuration', 'aws_secret'))

    try:
      vault = glacier_connection.get_vault(args[2])
    except:
      vault = None

    if vault is None:
      vault = glacier_connection.create_vault(args[2])
      print "Vault created:\n\tname={}\n\tarn={}\n\tcreation_date={}\n\tlast_inventory_date={}\n\tsize={}\n\tnumber_of_archives={}".format(vault.name, vault.arn, vault.creation_date, vault.last_inventory_date, vault.size, vault.number_of_archives)
    else:
      print "Vaule named '{}' already exists.".format(args[2])

  def accept(self, args):
    return len(args) >= 3 and args[0] == 'create' and args[1] == 'vault'

def command_init():
  return CommandCreateVault()

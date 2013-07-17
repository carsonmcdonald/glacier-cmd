import boto

class CommandListVaults(object):

  def execute(self, args, config):
    glacier_connection = boto.connect_glacier(aws_access_key_id=config.get('configuration', 'aws_key'), aws_secret_access_key=config.get('configuration', 'aws_secret'))

    for index, vault in enumerate(glacier_connection.list_vaults()):
      print "{}.\tname={}\n\tarn={}\n\tcreation_date={}\n\tlast_inventory_date={}\n\tsize={}\n\tnumber_of_archives={}".format(index+1, vault.name, vault.arn, vault.creation_date, vault.last_inventory_date, vault.size, vault.number_of_archives)

  def accept(self, args):
    return len(args) >= 2 and args[0] == 'list' and args[1] == 'vaults'

  def help(self):
    return "list vaults"

def command_init():
  return CommandListVaults()

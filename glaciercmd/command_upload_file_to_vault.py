import boto

class CommandUploadFileToVault(object):

  def execute(self, args, config):
    glacier_connection = boto.connect_glacier(aws_access_key_id=config.get('configuration', 'aws_key'), aws_secret_access_key=config.get('configuration', 'aws_secret'))

    try:
      vault = glacier_connection.get_vault(args[5])
    except:
      vault = None

    if vault is None:
      print "Vault named '{}' does not exist.".format(args[5])
    else:
      archive_id = vault.upload_archive(args[2])
      print "Upload archive id: {}".format(archive_id)

  def accept(self, args):
    return len(args) >= 6 and args[0] == 'upload' and args[1] == 'file' and args[3] == 'to' and args[4] == 'vault'

def command_init():
  return CommandUploadFileToVault()

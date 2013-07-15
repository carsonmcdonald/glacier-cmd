import boto
import time
import os

from boto.dynamodb2.table import Table
from boto.dynamodb2.layer1 import DynamoDBConnection

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

      dynamo_connection=DynamoDBConnection(aws_access_key_id=config.get('configuration', 'aws_key'), aws_secret_access_key=config.get('configuration', 'aws_secret'))
      archive_id_table = Table(config.get('configuration', 'dynamodb_table'), connection=dynamo_connection)
      archive_id_table.put_item(data={
            'Archive ID': archive_id,
            'Filename': os.path.abspath(args[2]),
            'Upload Timestamp': int(time.time())
      })

  def accept(self, args):
    return len(args) >= 6 and args[0] == 'upload' and args[1] == 'file' and args[3] == 'to' and args[4] == 'vault'

def command_init():
  return CommandUploadFileToVault()

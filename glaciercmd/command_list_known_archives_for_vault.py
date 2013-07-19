import boto
import datetime

from boto.dynamodb2.table import Table
from boto.dynamodb2.table import HashKey
from boto.dynamodb2.layer1 import DynamoDBConnection

class CommandListKnownArchivesForVault(object):

  def execute(self, args, config):
    glacier_connection = boto.connect_glacier(aws_access_key_id=config.get('configuration', 'aws_key'), aws_secret_access_key=config.get('configuration', 'aws_secret'))

    try:
      vault = glacier_connection.get_vault(args[5])
    except:
      vault = None

    if vault is None:
      print "Vault named '{}' does not exist.".format(args[5])
    else:
      dynamo_connection = DynamoDBConnection(aws_access_key_id=config.get('configuration', 'aws_key'), aws_secret_access_key=config.get('configuration', 'aws_secret'))
      archive_id_table = Table(config.get('configuration', 'dynamodb_table'), connection=dynamo_connection, schema=[HashKey('Account ID')])

      count = 1
      for archive in archive_id_table.scan():
        time_str = datetime.datetime.fromtimestamp(archive['upload_timestamp']).strftime('%d, %b %Y')
        print "{}.\tFilename: {}\n\tTimestamp: {}\n\tArchive ID: {}".format(count, archive['filename'], time_str, archive['archive_id'])
        count += 1

  def accept(self, args):
    return len(args) >= 6 and args[0] == 'list' and args[1] == 'known' and args[2] == 'archives' and args[3] == 'for' and args[4] == 'vault'

  def help(self):
    return "list known archives for vault <vault name>"

def command_init():
  return CommandListKnownArchivesForVault()

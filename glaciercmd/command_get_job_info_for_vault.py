import boto

from boto.glacier.exceptions import UnexpectedHTTPResponseError

class CommandGetJobInfoForVault(object):

  def execute(self, args, config):
    glacier_connection = boto.connect_glacier(aws_access_key_id=config.get('configuration', 'aws_key'), aws_secret_access_key=config.get('configuration', 'aws_secret'))

    try:
      vault = glacier_connection.get_vault(args[6])
    except:
      vault = None

    if vault is None:
      print "Vault named '{}' does not exist.".format(args[6])
    else:
      try:
        job = vault.get_job(args[3])
        print "Job info:\n\tAction: {}\n\tArchive Id: {}\n\tArchive Size:{}\n\tCompleted: {}\n\tCompletion Date: {}\n\tCreation Date: {} \n\tInventory Size: {}\n\tDescription: {}\n\tJobID: {}\n\tSNSTopic: {}\n\tStatus Code: {}\n\tStatus Message: {}\n".format(job.action, job.archive_id, job.archive_size, job.completed, job.completion_date, job.creation_date, job.inventory_size, job.description, job.id, job.sns_topic, job.status_code, job.status_message)
      except UnexpectedHTTPResponseError as error:
        print "Job '{}' can not be found:\n\t {}".format(args[3], error)

  def accept(self, args):
    return len(args) >= 7 and args[0] == 'get' and args[1] == 'job' and args[2] == 'info' and args[4] == 'for' and args[5] == 'vault'

  def help(self):
    return "get job info <job id> for vault <vault name>"

def command_init():
  return CommandGetJobInfoForVault()

import boto

class CommandListJobsForVault(object):

  def execute(self, args, config):
    glacier_connection = boto.connect_glacier(aws_access_key_id=config.get('configuration', 'aws_key'), aws_secret_access_key=config.get('configuration', 'aws_secret'))

    try:
      vault = glacier_connection.get_vault(args[4])
    except:
      vault = None

    if vault is None:
      print "Vault named '{}' does not exist.".format(args[4])
    else:
      jobs = vault.list_jobs()
      if not jobs:
        print "No jobs found for {}".format(args[4])
      else:
        count = 1
        for job in jobs:
          print "{}. Job info:\n\tAction: {}\n\tArchive Id: {}\n\tArchive Size:{}\n\tCompleted: {}\n\tCompletion Date: {}\n\tCreation Date: {} \n\tInventory Size: {}\n\tDescription: {}\n\tJobID: {}\n\tSNSTopic: {}\n\tStatus Code: {}\n\tStatus Message: {}\n".format(count, job.action, job.archive_id, job.archive_size, job.completed, job.completion_date, job.creation_date, job.inventory_size, job.description, job.id, job.sns_topic, job.status_code, job.status_message)
          count += 1

  def accept(self, args):
    return len(args) >= 5 and args[0] == 'list' and args[1] == 'jobs' and args[2] == 'for' and args[3] == 'vault'

  def help(self):
    return "list jobs for vault <vault name>"

def command_init():
  return CommandListJobsForVault()

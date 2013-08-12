glacier-cmd
===========

AWS Glacier command line client

*Work in progress...*

## Configuration

The configuration for this tool needs to be located in a file called
.glaciercmd in your home directory with the following format:


```
[configuration]
aws_key:<your aws api key>
aws_secret:<your aws secret>
dynamodb_table:<DynamoDB table to use>
```

## Options

- `list vaults` List available vaults.
- `create vault <vault name>` Create a vault with the given name.
- `delete vault <vault name>` Delete the vault with the given name.
- `vault info <vault name>` Get information on the vault with the given name.
- `upload file <file name> to vault <vault name>` Upload a file to the given vault.
- `delete archive <archive id> from <vault name>` Delete an archive from the given vault.
- `list known archives for vault <vault name>` List known archives from the given vault.
- `create inventory job for vault <vault name>` Create an inventory job for the given vault.
- `list jobs for vault <vault name>` List current jobs for the given vault.

## License

MIT - See the LICENSE file

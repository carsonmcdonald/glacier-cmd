glacier-cmd
===========

AWS Glacier command line client

## Configuration

The configuration for this tool needs to be located in a file called
.glaciercmd in your home directory with the following format:


```
[configuration]
aws_key:<your aws api key>
aws_secret:<your aws secret>
```

## Options

- `list vaults` List available vaults.
- `create vault <vault name>` Create a vault with the given name.

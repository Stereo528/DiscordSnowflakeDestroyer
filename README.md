# DiscordSnowflakeDestroyer
Deletes Slash Command Snowflakes via the Discord API

## Config
Rename the `example.config.toml` to `config.toml`
example layout:
```toml
#these are random numbers/letters, they should not be anything actual in this example
applicationID = "172387129379144236"
botToken = "The 70 Character Token" #leaving this one completely out for obvious reasons (I hope)
guildID = "289789237982032478"
```
## How It Works
- Using the `requests` library it makes it a call to `https://discord.com/api/v10/applications/{appID}/guilds/{guildID}/commands` or 
`https://discord.com/api/v10/applications/{appID}/commands` to get a list of all of the commands. 
- It will then print out the ID, Name, and Description
of all commands listed. 
- Then you run it again this time calling the delete command, which will list all commands previously gotten in the last run
allowing you to copy and paste the ID, then deleting the command

## Plans
- while loop until user types `done` in the get/delete prompt

OR

- typing `get`, and prompting for guild/global, will then proceed automatically into the `delete` prompt, and continues to run that until you type done
in the guild/global prompt


## Credits
Thanks to [@asoji](https://github.com/asoji) for the initial requests code to the Discord API!

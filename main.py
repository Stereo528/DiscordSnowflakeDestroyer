import requests, tomli, json

print("Welcome to DSD!")
with open("config.toml", "rb") as f:
    config = tomli.load(f)
gd = input("Get or Delete Snowflakes? (g(et)/d(el)): ")

appID = config["applicationID"]
guildID = config["guildID"]
botToken = config["botToken"]

if gd.lower() == "g" or gd.lower() == "get":
    url = f"https://discord.com/api/v10/applications/{appID}/guilds/{guildID}/commands"

    gluidOrGlobal = input("Get snowflakes for a Guild (default) or Global? (Guild/Global): ")

    if gluidOrGlobal.lower() == "global":
        url = f"https://discord.com/api/v10/applications/{appID}/commands"
    else:
        print("Using default option: Guild\n")

    headers = {"Authorization": f"Bot {botToken}"}

    response = requests.request("GET", url, headers=headers)

    if response.status_code == 200:
        print(f"Success! Response: {response.status_code}\n")
        with open("snowflakes.json", "w") as f:
            json.dump(response.json(), f, indent=4)

    with open("snowflakes.json", "r") as f:
        snowflakes = json.load(f)

    for snowflake in snowflakes:
        print("Name: " + snowflake["name"])
        print("Description: " + snowflake["description"])
        print("ID: " + snowflake["id"] + "\n")

if gd.lower() == "d" or gd.lower() == "del":
    print("")
    with open("snowflakes.json") as f:
        snowflakes = json.load(f)

    for snowflake in snowflakes:
        if snowflake == "":
            continue
        print("Name: " + snowflake["name"])
        print("Description: " + snowflake["description"])
        print("ID: " + snowflake["id"] + "\n")
    print("These are the snowflakes you can delete, and are listed in the snowflakes.json file created when you ran the `get` command.\n")

    guildOrGlobal = input("Delete snowflakes for a Guild (default) or Global? (Guild/Global): ")

    snowflakeID = input("Enter snowflake ID to delete: ")

    url = f"https://discord.com/api/v10/applications/{appID}/guilds/{guildID}/commands/{snowflakeID}"

    if guildOrGlobal.lower() == "global":
        url = f"https://discord.com/api/v10/applications/{appID}/commands/{snowflakeID}"

    headers = {"Authorization": f"Bot {botToken}"}

    print(url)

    response = requests.request("DELETE", url, headers=headers)

    if response.status_code == 200 or response.status_code == 204:
        print("Success!")
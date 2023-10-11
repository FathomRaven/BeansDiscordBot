import discord
import json

# Stored in the main folder, not in the utility folder
file_path = "./data.json"

async def write_storage(guild: discord.Guild, key :str, value):
	print(f"In {guild.id}, {key} was set to {value}")
	
	# Try to open file
	# It may be better to make setup.sh create the file by default, and remove this check.
	try: 
		with open(file_path, "r") as file:
			data = json.load(file)
	except FileNotFoundError:
		data = {}

	data[str(guild.id)] = {
		key: value
	}

	# Write back to the file
	with open(file_path, "w") as file:
		json.dump(data, file, indent=4)


async def read_storage(guild: discord.Guild, key: str):
	try: 
		with open(file_path, "r") as file:
			data = json.load(file)
	except FileNotFoundError:
		data = {}

	return data[str(guild.id)]

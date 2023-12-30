import discord
import json

# Stored in the main folder, not in the utility folder
file_path = "./data.json"

# Write some kind of data to the JSON file
async def write_storage(guild: discord.Guild, key :str, value):
	print(f"In {guild.id}, {key} was set to {value}")
	
	# Try to open file
	# It may be better to make setup.sh create the file by default, and remove this check.
	try: 
		with open(file_path, "r") as file:
			data = json.load(file)
	except FileNotFoundError:
		data = {}
		return

	data[str(guild.id)] = {
		key: value
	}

	# Write back to the file
	with open(file_path, "w") as file:
		json.dump(data, file, indent=4)

# Read back data from the JSON file
async def read_storage(guild: discord.Guild, key: str):
	# Check if the file exists
	try: 
		with open(file_path, "r") as file:
			data = json.load(file)
	except FileNotFoundError:
		data = {}
		return data

	return data[str(guild.id)][key]

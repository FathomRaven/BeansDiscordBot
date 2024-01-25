import discord
import json
from discord.ext import commands

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

	data[str(guild.id)][key] = value

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

def get_member(ctx: commands.context, get_author=True, get_by_mentions=True, get_by_name=True):
	member = None
	if(get_author):
		member = ctx.message.author

	if(get_by_mentions and ctx.message.mentions):
		member = ctx.message.mentions[0]
	
	if(get_by_name):
		args = ctx.message.content.split(" ")
		if(len(args) > 1):
			member_by_name = ctx.guild.get_member_named(args[1])
			if(member_by_name != None):
				member = member_by_name

	return member

async def send_error_message(ctx: commands.context, error_message="Encountered an error!"):
	embed = discord.Embed(
		title="Error!",
		color=discord.Color(0xff0000),
		description=error_message
	)

	await ctx.send(embed=embed)
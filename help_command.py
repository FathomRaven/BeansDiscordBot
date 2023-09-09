from typing import Any, List, Mapping, Optional # Not sure what this does! I never said my code was GOOD after all
import discord
from discord.ext import commands
from discord.ext.commands.cog import Cog
from discord.ext.commands.core import Command

class Help(commands.DefaultHelpCommand):

	# Some python class nonsense
	def __init__(self, **options: Any) -> None:
		super().__init__(**options)

	# Send general help
	async def send_bot_help(self, mapping):
		# Create the embed
		embed = discord.Embed(title="Bot Help", description="List of available groups and their commands:")

		# Add each cog to embed
		for cog, commands in mapping.items():
			if cog is None:
				continue

			command_list = [f"`{command.name}`" for command in commands]
			cog_name = cog.qualified_name if cog.qualified_name != "default" else "No Category"
			embed.add_field(name=cog_name, value=", ".join(command_list), inline=False)

		await self.get_destination().send(embed=embed)
	
	# Send help for a single cog
	async def send_cog_help(self, cog):
		embed = discord.Embed(title=f"{cog.qualified_name} Commands", description="List of commands in this cog:")

		for command in cog.get_commands():
			embed.add_field(name=command.name, value=command.help or "No description", inline=False)

		await self.get_destination().send(embed=embed)

	# Send help for a single command
	# TODO: Add more information to this
	async def send_command_help(self, command):
		embed = discord.Embed(title=f"{command.name.capitalize()} command")

		await self.get_destination().send(embed=embed)		
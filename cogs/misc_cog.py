import random
import requests

import discord
from discord.ext import commands
from utility.get_member import get_member

class Misc(commands.Cog):
	"""Some little random commands"""
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def say(self, ctx):
		"""Make the bot say what you just said!"""
		message_content = ctx.message.content.split(" ")
		message_content.pop(0)
		message_content = " ".join(message_content)

		await ctx.message.delete()

		if(random.randrange(1, 101) > 90):
			embed = discord.Embed(
				title=ctx.message.author.display_name + " tried to say:",
				description=message_content
			)

			await ctx.send(embed=embed)
			return

		if not message_content:
			await ctx.send("Cannot send an empty message!")
			return

		await ctx.send(message_content)
	
	@commands.command()
	async def ping(self, ctx):
		"""Ping the bot to test if it's online"""
		await ctx.send("Pong!")
		await ctx.message.add_reaction('🏓')

	@commands.command()
	async def avatar(self, ctx):
		"""Get the avatar of yourself or others!"""
		member = get_member(ctx)

		if(not member.avatar):
			embed = discord.Embed(
				title="Error!",
				description="User has no avatar!"
			)

			await ctx.send(embed=embed)
			return

		embed = discord.Embed(
			title=member.display_name + "'s avatar",
			color=member.top_role.color
		)

		embed.set_image(url=member.avatar.url)

		await ctx.send(embed=embed)

	@commands.command()
	async def define(self, ctx, arg):
		"""Define a word!"""
		response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + str(arg))
		if(response.status_code != 200):
			await ctx.send("Error in getting word! Are you sure it exists?")
			return
		
		data = response.json()[0]
		embed = discord.Embed(
			title=f"{data['word'].capitalize()} definitions",
			description="",
		).set_footer(text=f"Source: {data['sourceUrls'][0]}")
		for definition in data["meanings"][0]["definitions"]:
			embed.description += f"{definition['definition'].capitalize()}\n\n"

		await ctx.send(embed=embed)
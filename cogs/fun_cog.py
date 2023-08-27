import discord
import random
from discord.ext import commands

class Fun(commands.Cog):
	"""Funny joke commands"""
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def gay(self, ctx):
		percentage = random.randrange(1, 101)
		status_bar = ""
		for i in range(round(percentage/10)):
			status_bar += "🟪"
		for i in range(10 - round(percentage/10)):
			status_bar += "⬛"
		
		embed = discord.Embed(
			title="Gay status of: " + ctx.message.author.display_name,
			description= str(percentage) + "%" + " gay" + "\n" + status_bar,
			color=discord.Color(0x5e5e5e)
		)

		if(percentage >= 90):
			embed.description += "\nWow, thats a really high score!"
			embed.color = discord.Color(0xff00d0)

		await ctx.send(embed=embed)
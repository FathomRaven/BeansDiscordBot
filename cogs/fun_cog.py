import discord
import random
from discord.ext import commands

from utility.get_member import get_member

class Fun(commands.Cog):
	"""Funny joke commands"""
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def gay(self, ctx):
		"""See just how gay you and your friends are"""
		percentage = random.randrange(1, 101)
		status_bar = ""
		member = get_member(ctx)

		# Makes a status bar (misleading name)
		for i in range(round(percentage/10)):
			status_bar += "🟪"
		for i in range(10 - round(percentage/10)):
			status_bar += "⬛"
		
		embed = discord.Embed(
			title="Gay status of: " + member.display_name, # Display name includes nicknames
			description= str(percentage) + "%" + " gay" + "\n" + status_bar,
			color=discord.Color(0x5e5e5e)
		)

		if(member.avatar):
			embed.set_thumbnail(url=member.avatar.url)

		if(percentage >= 90):
			embed.description += "\nWow, thats a really high score!"
			embed.color = discord.Color(0xff00d0)

		await ctx.send(embed=embed)
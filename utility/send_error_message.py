import discord
from discord.ext import commands

async def send_error_message(ctx: commands.context, error_message="Encountered an error!"):
	embed = discord.Embed(
		title="Error!",
		color=discord.Color(0xff0000),
		description=error_message
	)

	await ctx.send(embed=embed)
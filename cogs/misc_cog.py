from discord.ext import commands

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

		await ctx.send(message_content)
	
	@commands.command()
	async def ping(self, ctx):
		await ctx.send("Pong!")
		await ctx.message.add_reaction('🏓')
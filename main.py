# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import dotenv_vault
import os

from cogs.misc_cog import Misc

dotenv_vault.load_dotenv()

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='z', description=description, intents=intents)

@bot.event
async def on_ready():
    await bot.add_cog(Misc(bot))
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


bot.run(os.getenv("TOKEN"))
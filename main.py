# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import dotenv_vault
import os

from cogs.misc_cog import Misc
from cogs.fun_cog import Fun
from help_command import Help

dotenv_vault.load_dotenv()

description = '''
Beans

A bot thats occasionally useful, and (even more rarely), funny
'''

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=os.getenv("PREFIX"), description=description, intents=intents, help_command=Help())

@bot.check
async def check(ctx: commands.Context):
    if "@here" in ctx.message.content or "@everyone" in ctx.message.content:
        await ctx.send("Nice try")
        return False
    return True

@bot.event
async def on_ready():
    await bot.add_cog(Misc(bot))
    await bot.add_cog(Fun(bot))
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


bot.run(os.getenv("TOKEN"))
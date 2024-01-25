# Bot needs member permissions and message permissions

import discord
from discord.ext import commands

# Dotenv includes
import dotenv
import os

# All commands and cogs
from cogs.misc_cog import Misc
from cogs.fun_cog import Fun
from help_command import Help

dotenv.load_dotenv()

description = '''
Beans

A bot thats occasionally useful, and (even more rarely), funny
'''

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=os.getenv("PREFIX"), description=description, intents=intents, help_command=Help())

# Run a check to prevent mass pings
# TODO: Add in a check for role pings as well
@bot.check
async def check(ctx: commands.Context):
    if "@here" in ctx.message.content or "@everyone" in ctx.message.content:
        await ctx.send("Nice try")
        return False
    return True

# Ready the bot, and load all cogs
@bot.event
async def on_ready():
    await bot.add_cog(Misc(bot))
    await bot.add_cog(Fun(bot))
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    game = discord.Game(f"in {len(bot.guilds)} servers | {os.getenv('PREFIX')}help")
    await bot.change_presence(status=discord.Status.online, activity=game)

# Access the token using env
bot.run(os.getenv("TOKEN"))
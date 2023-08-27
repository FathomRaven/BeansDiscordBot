import discord
from discord.ext import commands

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
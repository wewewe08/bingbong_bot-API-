import discord
import datetime
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import ConversionError

class Administrator(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Administrator is ready.')

    @commands.command(pass_context = True)
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        embed = discord.Embed(
            colour = discord.Colour.purple(),
            timestamp = datetime.datetime.utcnow(),
            title = "user kicked!"
        )
        embed.set_thumbnail(url = member.avatar_url)
        embed.set_footer(text = f'requested by {ctx.author.name}', icon_url = ctx.author.avatar_url)
        embed.add_field(name = f'get out of here, {member}!', value = f'reason: {reason}', inline = False)
        channel = await member.create_dm()
        await member.kick(reason=reason)
        await ctx.send(embed = embed)
        await channel.send(embed = embed)
        print('user kicked')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('> **please specify who to kick.**')

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        embed = discord.Embed(
            colour = discord.Colour.purple(),
            timestamp = datetime.datetime.utcnow(),
            title = "user banned!"
        )
        embed.set_thumbnail(url = member.avatar_url)
        embed.set_footer(text = f'requested by {ctx.author.name}', icon_url = ctx.author.avatar_url)
        embed.add_field(name = f'{member} was banned!', value = f'reason: {reason}', inline = False)
        channel = await member.create_dm()
        await member.ban(reason=reason)
        await ctx.send(embed = embed)
        await channel.send(embed = embed)
        print('user banned')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('> **please specify who to ban.**')

    @commands.command()
    @commands.has_permissions(administrator = True) 
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} was unbanned!')
            print('user unbanned')

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('> **please specify who to unban.**')

    @commands.command(pass_context = True)
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit = amount)
        await ctx.send(f'>>> **messages cleared! :soap:**\n{amount} messages cleared in {ctx.channel.mention}.')

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('> **please specify an amount of messages to clear.**')

def setup(client):
    client.add_cog(Administrator(client))

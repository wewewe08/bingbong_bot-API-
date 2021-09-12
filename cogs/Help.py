import discord
import datetime
from discord.ext import commands
from discord.utils import get

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help is ready.")

    @commands.group(name = "help", invoke_without_command = True)
    async def helpcommand(self, ctx):
        author = ctx.message.author
        embed = discord.Embed(
            colour = discord.Colour.purple(),
            title = 'COMMANDS',
            timestamp = datetime.datetime.utcnow(),
        )
        embed.set_footer(text = f'requested by {ctx.author.name}', icon_url = ctx.author.avatar_url)
        embed.add_field(name = '**.help**', value = "lists every category of commands.", inline = False)
        embed.add_field(name = '**.help serverinfo**', value = "lists commands that deals with server info.", inline = False)
        embed.add_field(name = '**.help admin**', value = "lists the commands for admins.", inline = False)
        embed.add_field(name = '**.help fun**', value = "lists all the fun commands.", inline = False)
        embed.add_field(name = '**.help osu**', value = "lists the commands for osu.", inline = False)
        embed.add_field(name = '**.help league**', value = "lists the commands for league.", inline = False)
        await ctx.send('> **the prefix for bing bong is "."**')
        await ctx.send(embed = embed)

    @helpcommand.command(name = "serverinfo")
    async def server_info_subcommand(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.purple(),
            title = 'SERVER INFO',
            timestamp = datetime.datetime.utcnow(),
        )
        embed.set_footer(text = f'requested by {ctx.author.name}', icon_url = ctx.author.avatar_url)
        embed.add_field(name = '**.ping**', value = "returns the bot's latency.", inline = False)
        embed.add_field(name = '**.info [@user]**', value = "lists the information of a user.", inline = False)
        await ctx.send(embed = embed)

    @helpcommand.command(name = "admin")
    async def admin_subcommand(self, ctx):
        author = ctx.message.author
        embed = discord.Embed(
            colour = discord.Colour.purple(),
            title = 'ADMINISTRATOR',
            timestamp = datetime.datetime.utcnow(),
        )
        embed.set_footer(text = f'requested by {ctx.author.name}', icon_url = ctx.author.avatar_url)
        embed.add_field(name = '**.kick [user]**', value = "kicks a user.", inline = False)
        embed.add_field(name = '**.ban [user]**', value = "bans a user.", inline = False)
        embed.add_field(name = '**.unban [user]**', value = "unbans a user.", inline = False)
        embed.add_field(name = '**.clear [# of messages]**', value = "clears an amount of messages.", inline = False)
        await ctx.send(embed = embed)

    @helpcommand.command(name = "fun")
    async def fun_subcommand(self, ctx):
        author = ctx.message.author
        embed = discord.Embed(
            colour = discord.Colour.purple(),
            title = 'FUN',
            timestamp = datetime.datetime.utcnow(),
        )
        embed.set_footer(text = f'requested by {ctx.author.name}', icon_url = ctx.author.avatar_url)
        embed.add_field(name = '**.8ball [question]**', value = "ask the bot a question.", inline = False)
        embed.add_field(name = '**.say [message]**', value = "make the bot say something.", inline = False)
        embed.add_field(name = '**.cat**', value = "sends you a random cat photo.", inline = False)
        embed.add_field(name = '**.dog**', value = "sends you a random dog photo.", inline = False)
        embed.add_field(name = '**.corgi**', value = "sends you a random corgi photo.", inline = False)
        await ctx.send(embed = embed)

    @helpcommand.command(name = "osu")
    async def music_subcommand(self, ctx):
        author = ctx.message.author
        embed = discord.Embed(
            colour = discord.Colour.purple(),
            title = 'osu',
            timestamp = datetime.datetime.utcnow(),
        )
        embed.set_footer(text = f'requested by {ctx.author.name}', icon_url = ctx.author.avatar_url)
        embed.add_field(name = '**.osu [username]**', value = "displays the info of an osu user.", inline = False)
        await ctx.send(embed = embed)
        
    @helpcommand.command(name = "league")
    async def music_subcommand(self, ctx):
        author = ctx.message.author
        embed = discord.Embed(
            colour = discord.Colour.purple(),
            title = 'league',
            timestamp = datetime.datetime.utcnow(),
        )
        embed.set_footer(text = f'requested by {ctx.author.name}', icon_url = ctx.author.avatar_url)
        embed.add_field(name = '**.league [username]**', value = "displays the info of a league user.", inline = False)
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Help(client))

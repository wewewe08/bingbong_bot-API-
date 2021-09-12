import discord
import datetime
from discord.ext import commands

class ServerInfo(commands.Cog):
    def __init__(self, client):
        self.client = client
    #events
    @commands.Cog.listener()
    async def on_ready(self):
        print('ServerInfo is ready.')

    #commands
    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.purple(),
            timestamp = datetime.datetime.utcnow(),
            title = 'PONG!',
        )
        embed.set_footer(text = f'requested by {ctx.author.name}', icon_url = ctx.author.avatar_url)
        embed.add_field(name = 'latency', value = f'{round(self.client.latency*1000)}ms', inline = False)
        await ctx.send(embed = embed)

    @commands.command()
    async def info(self, ctx, member: discord.Member):
        roles = [role for role in member.roles]
        embed = discord.Embed(
            color=discord.Colour.purple(),
            timestamp = datetime.datetime.utcnow(),
        )
        embed.set_author(name=f'{member}', icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name = "**ID**", value = member.id)
        embed.add_field(name = "**nicknames**", value = member.display_name)
        embed.add_field(name = "**created at**", value = member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name = "**joined at**", value = member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name = f"**roles ({len(roles)})**", value = " ".join([role.mention for role in roles]))
        embed.add_field(name = "**top role**", value = member.top_role.mention)
        embed.add_field(name = "**bot?**", value = member.bot)
        embed.add_field(name = "**status**", value = str(member.status))
        embed.add_field(name = "**activity**", value = str(member.activity))
        embed.set_footer(text=f'requested by {ctx.author.name}', icon_url = ctx.author.avatar_url)
        await ctx.send(content=None, embed=embed)


#setups
def setup(client):
    client.add_cog(ServerInfo(client))

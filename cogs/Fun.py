import discord
import random
import aiohttp
import asyncio
import datetime
#import requests
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun is ready.")

    @commands.command()
    async def say(self, ctx, *, arg):
        await ctx.send(f"> {arg}")

    @commands.command(aliases = ["8ball"])
    async def _8ball(self, ctx, *, question):
        responses = ['idk about that one.',
                     'thats a no.', 'yes.', 'no.', '100% yes.']
        if question.endswith("?"):
            await ctx.send(f'>>> **question:** {question}\n**answer:** {random.choice(responses)}')
        else:
            await ctx.send("> **that isn't a question!**")

    @commands.command()
    async def cat(self, ctx: commands.Context):
        async with aiohttp.ClientSession(loop=ctx.bot.loop) as session:
            async with session.get("https://aws.random.cat/meow") as r:
                data = await r.json()
            embed = discord.Embed(
                color = discord.Colour.purple(),
            )
            embed.set_image(url=data['file'])
            embed.set_footer(text=f'requested by {ctx.author.name}', icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)

    @commands.command()
    async def dog(self, ctx:commands.Context):
        async with aiohttp.ClientSession(loop=ctx.bot.loop) as session:
            async with session.get("https://random.dog/woof.json") as r:
                data = await r.json()
                data = data['url']
            embed = discord.Embed(
                color = discord.Colour.purple(),
                time = datetime.datetime.utcnow(),
                title = "here's a picture of a random dog!"
            )
            embed.set_image(url=data)
            embed.set_footer(text=f'requested by {ctx.author.name}', icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)

    @commands.command()
    async def corgi(self, ctx:commands.Context):
        async with aiohttp.ClientSession(loop=ctx.bot.loop) as session:
            async with session.get("https://dog.ceo/api/breed/corgi/cardigan/images/random") as r:
                data = await r.json()
                data = data['message']
            embed = discord.Embed(
                color = discord.Colour.purple(),
                title = "here's a picture of a random dog!"
            )
            embed.set_image(url=data)
            embed.set_footer(text=f'requested by {ctx.author.name}', icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Fun(client))

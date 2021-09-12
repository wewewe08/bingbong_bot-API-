import discord
import os
import asyncio
import json
import aiohttp
import datetime
#import requests
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import ConversionError
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN
from riotwatcher import LolWatcher, ApiError

#riotwatcher variables
LEAGUE_KEY = os.getenv("LEAGUE_KEY")
lol_watcher = LolWatcher(LEAGUE_KEY)
myRegion = "na1"

OSU_KEY = os.getenv("OSU_KEY")
url = f"https://osu.ppy.sh/api/get_user?k={OSU_KEY}="

class WebRequests(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("WebRequests are ready.")
    
    @commands.command()
    async def league(self, ctx:commands.Context, *, userName: str):
        player = lol_watcher.summoner.by_name(myRegion, userName)
        playerRankedStats = lol_watcher.league.by_summoner(myRegion, player['id'])

        username  = str(player['name'])
        summonerLevel = str(player['summonerLevel'])
        profile = "https://ddragon.leagueoflegends.com/cdn/11.14.1/img/profileicon/" + str(player['profileIconId']) + ".png"
        tierLevel = playerRankedStats[0]['tier']
        rank = playerRankedStats[0]['rank']
        wins = playerRankedStats[0]['wins']
        losses = playerRankedStats[0]['losses']

        print(tierLevel)

        embed = discord.Embed(
            color = discord.Colour.purple(),
            title = "LEAGUE PROFILE",
            )
        embed.set_thumbnail(url = profile)
        embed.add_field(name = "**username**", value = username)
        embed.add_field(name = "**level**", value = summonerLevel)
        embed.add_field(name = "**rank**", value = tierLevel + " " + rank)
        embed.add_field(name = "**wins**", value = wins)
        embed.add_field(name = "**losses**", value = losses)
        embed.set_footer(text=f'requested by {ctx.author.name}', icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

        try:
            response = lol_watcher.summoner.by_name(myRegion, 'this_is_probably_not_anyones_summoner_name')
            rankedResponse = lol_watcher.league.by_summoner(myRegion, player['id'])
        except ApiError as err:
            if err.response.status_code == 429:
                print('We should retry in {} seconds.'.format(err.response.headers['Retry-After']))
                print('this retry-after is handled by default by the RiotWatcher library')
                print('future requests wait until the retry-after time passes')
            elif err.response.status_code == 404:
                print('Summoner with that ridiculous name not found.')
            else:
                raise

    @commands.command()
    async def osu(self, ctx:commands.Context, *, userName: str):
        async with aiohttp.ClientSession(loop = ctx.bot.loop) as session:
            async with session.get(url+ userName) as r:
                data = await r.json()
                print(data)
                username = data[0]['username']
                userid = data[0]['user_id']
                profile = "https://a.ppy.sh/" + userid
                joindate = data[0]['join_date']
                joinr = joindate.split(" ")
                pprank = data[0]['pp_rank']
                accuracy = data[0]['accuracy']
                rounded = Decimal(str(accuracy)).quantize(Decimal('1.11'), rounding=ROUND_HALF_UP)
                country = data[0]['country']
                countryrank = data[0]['pp_country_rank']
                ppraw = data[0]['pp_raw']
            embed = discord.Embed(
                color = discord.Colour.purple(),
                title = "OSU PROFILE",
            )
            embed.set_thumbnail(url = profile)
            embed.add_field(name = "**username**", value = username)
            embed.add_field(name = "**join date**", value = joinr[0])
            embed.add_field(name = "**pp rank**", value = "#" + pprank)
            embed.add_field(name = "**country rank**", value = "#" + countryrank)
            embed.add_field(name = "**pp raw**", value = ppraw)
            embed.add_field(name = "**accuracy**", value = f"{rounded}%")
            embed.add_field(name = "**country**", value = country)
            embed.set_footer(text=f'requested by {ctx.author.name}', icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)

#setups
def setup(client):
    client.add_cog(WebRequests(client))

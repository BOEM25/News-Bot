# Modules & Libraries
import discord
import json

from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client 
    
    @commands.command()
    async def test(self, ctx):
        # creating webhooks: webhook = await ctx.channel.create_webhook(name="test")
        # webhooks = await ctx.guild.webhooks() returns list of webhooks ids, use that to loop through the list to get the url, if 
        pass

    @commands.command()
    async def news_chan(self, ctx, news_source=None):
        """
        the data layout is
        {
            "news_source1": [{"url": "webhook_url", "webhook_id": 123}, {"url": "webhook_url", "webhook_id": 123}]
            "news_source2": [{"url": "webhook_url", "webhook_id": 123}, {"url": "webhook_url", "webhook_id": 123}]
        }
        if in a channel where a webhook for newsbot is already made we don't want to make another one, so we must check with ctx.guild.webhooks
        could save webhooks per server but thats ineffecient for posting messages per news source
        """
        pass

def setup(client):
    client.add_cog(Commands(client))
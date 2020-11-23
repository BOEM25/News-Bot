# Modules & Libraries
import discord
import json
import asyncio
import time
import requests

from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client 
    
    @commands.command()
    async def test(self, ctx):
        # creating webhooks: webhook = await ctx.channel.create_webhook(name="test")
        # webhooks = await ctx.channel.webhooks() returns list of webhooks objects, use that to loop through the list to get the url, if 
        webhooks = await ctx.channel.webhooks()
        with open('./data/news_channels.json', 'r') as news_channels:
            json_channels = json.load(news_channels)
        await ctx.send(webhooks)
        for i in webhooks:
            pass # Loop through the webhook list

        temp = []
        for i in json_channels:
            temp.append(i)
        await ctx.send(temp)
        pass

    @commands.command()
    async def news_chan(self, ctx, news_source=None):
        start = time.time()
        """
        the data layout is, i think, optimal??

        # webhooks.json
        "webhooks": {
            "news_source1": [{"url": "webhook_url", "webhook_id": 123}, {"url": "webhook_url", "webhook_id": 123}]
            "news_source2": [{"url": "webhook_url", "webhook_id": 123}, {"url": "webhook_url", "webhook_id": 123}]
        }

        # news_channels.json
        "news_source1": {
            "name": "Test",
            "desc": "Lorem Ipsum, not sure whether this is a good structure, may rewrite",
            "id": 1
        }

        if in a channel where a webhook for newsbot is already made we don't want to make another one, so we must check with ctx.guild.webhooks
        could save webhooks per server but thats ineffecient for posting messages per news source
        

        Is this perfect? Eh, works

        If two users execute the command at nearly the exact same time it will overwrite the first one
        Soooo, REST api webserver that isnt async but fast to prevent that stuff???
        Or a different storage format

        f.close() seems to fix it? Nvm
        """
        with open('./data/news_channels.json', 'r') as news_channels:
            json_channels = json.load(news_channels)
        
        for i in json_channels:
            if news_source.lower() == i:
                await ctx.send("in list", delete_after=12)
                webhooks = await ctx.channel.webhooks()
                check = False # Boolean that will change if a webhook for this channel already exist, due to the 10 webhook limit stuff
                    
                try:
                    with open('./data/webhooks.json', 'r') as f:
                        json_webhooks = json.load(f)
                        f.close()

                except Exception:
                    json_webhooks = {}

                for p in webhooks:
                    for o in json_webhooks:
                        for x in json_webhooks[o]:
                            if p.url == x:
                                check = True

                if check != True:
                    try:
                        webhook = await ctx.channel.create_webhook(name=i)
                        await ctx.send(webhook, delete_after=12)
                    except Exception as e:
                        await ctx.send(e, delete_after=12)

                    try:
                        json_webhooks[i].append(webhook.url)
                    except:
                        json_webhooks[i] = [webhook.url]
                else:
                    try:
                        if p.url in json_webhooks[i]:
                            pass
                        else:
                            json_webhooks[i].append(p.url)
                    except:
                        json_webhooks[i] = [p.url]

                with open('./data/webhooks.json', 'w') as f:
                    json.dump(obj=json_webhooks, fp=f, indent=4)

        finish = time.time() - start
        await ctx.send(f"{finish} seconds")
        requests.post("http://localhost:5000/", data=json_webhooks)
        pass

    @commands.command()
    async def remove_chan(self, ctx, news_source=None):
        pass

def setup(client):
    client.add_cog(Commands(client))
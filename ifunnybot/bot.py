import json
import time
import requests as r

import discord
from discord.ext import tasks

from ifunnybot.ifunny import Post

class IFunnyBot(discord.Bot):
    def __init__(self, description=None, *args, **options):

        intents = discord.Intents.default()

        intents.message_content = True

        super().__init__(description, intents=intents, *args, **options)

        self.add_listener(self.fetch_media_link, "on_message")
    
    async def fetch_media_link(self, message: discord.Message):
        
        can_embed = False 

        for role in message.author.roles:
            if role.permissions.embed_links:
                can_embed = True
        
        if not can_embed:
            return
        
        if "https://ifunny.co/" not in message.content:
            return

        media_url = Post(message.content).fetch_media_url()

        await message.reply(media_url)


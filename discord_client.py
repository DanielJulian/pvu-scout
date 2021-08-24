import discord

prefix = 'scout'

class DiscordClient(discord.Client):
            
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if self.user.id != message.author.id:
            if message.content.startswith(prefix + " farm refresh"):
                self.lookup_farm_refresh(message)
                self.send_message("yeeee")

    async def send_message(self, message):
        text_channels = self.guilds[0].text_channels
        for channel in text_channels:
            if channel.id == 879373144077512714:
                await channel.send(message)
    
    async def send_embed(self, message):
        text_channels = self.guilds[0].text_channels
        for channel in text_channels:
            if channel.id == 879373144077512714:
                await channel.send(embed=message)

    
    def lookup_farm_refresh(self, message):
        farm_address = message.split(" ")[-1]

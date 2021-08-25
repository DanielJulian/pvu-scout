import discord
import io
import csv
from discord import File


prefix = '/scout'

class DiscordClient(discord.Client):

    database = None

    def set_database(self, database):
        self.database = database
            
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if self.user.id != message.author.id:
            if message.content.startswith(prefix + " refresh file"):
                refresh_file = self.get_refresh_file()
                await self.send_file(refresh_file)

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
    
    async def send_file(self, thefile):
        text_channels = self.guilds[0].text_channels
        for channel in text_channels:
            if channel.id == 879373144077512714:
                await channel.send("Here is the file", file=File(fp=thefile, filename="plants.csv"))

    def get_refresh_file(self):
        all_plants = self.database.select_all_plants()
        csv_file = self.build_file(all_plants)
        return csv_file

    def build_file(self, plants):
        buffer = io.StringIO()
        writer = csv.writer(buffer)
        writer.writerow(['id', 'water_end_time', 'url'])
        for plant in plants:
            plant_id = plant['id']
            water_end_time = str(plant['water_end_time']) if plant['water_end_time'] else ""
            url =  "https://marketplace.plantvsundead.com/farm#/farm/" + plant_id
            writer.writerow([plant_id, water_end_time, url])
        buffer.seek(0)
        return buffer

    #def lookup_farm_refresh(self, message):
    #    farm_address = message.split(" ")[-1]

from discord import Embed
import time

class Manager():
    
    queue = None
    discord_client = None

    def __init__(self, queue, discord_client):
      self.queue = queue
      self.discord_client = discord_client


    def start_plants_monitor(self):
      discord_loop = self.discord_client.loop
      while True:
          time.sleep(5)
          plant_tuple = self.queue.get()
          plant = plant_tuple[1]

          # TODO If the waterEndTime is equal or less than 1 minute, post it to discord, else, put it back to the queue.
          # https://stackoverflow.com/questions/49835742/how-to-send-a-message-with-discord-py-without-a-command
          print(1)
          discord_loop.create_task(self.discord_client.send_message(plant['waterEndTime']))

          embed = Embed(title="Plant Refresh", description="A plant is about to refresh", colour=0x0000FF)
          embed.add_field(name="URL", value=plant['url'], inline=False)
          embed.add_field(name="Refresh Time", value=plant['waterEndTime'], inline=False)
          embed.set_author(name="PVU Scout")
          embed.set_footer(text="Salu2")
          discord_loop.create_task(self.discord_client.send_embed(embed))

          print(2)
from discord import Embed
from datetime import datetime
import traceback
import time

class Manager():
    
    queue = None
    discord_client = None

    def __init__(self, queue, discord_client):
      self.queue = queue
      self.discord_client = discord_client


    def start_plants_monitor(self):
      # queue.put((123,{'water_end_time': datetime.now() + timedelta(minutes=2), 'url': 'https://www.google.com.ar/'}))
      discord_loop = self.discord_client.loop
      while True:
        try:
          time.sleep(5)
          plant_tuple = self.queue.get()
          plant = plant_tuple[2]

          # TODO If the water_end_time is equal or less than 1 minute, post it to discord, else, put it back to the queue.
          if ((plant['water_end_time'] - datetime.now()).total_seconds() <= 60):
            print("Sending message to discord: ", plant)
            url = "https://marketplace.plantvsundead.com/farm#/farm/" + plant['id']
            embed = Embed(title="Plant Refresh", description="A plant is about to refresh", colour=0x0000FF)
            embed.add_field(name="URL", value=url, inline=False)
            embed.add_field(name="Refresh Time", value=plant['water_end_time'], inline=False)
            embed.set_author(name="PVU Scout")
            embed.set_footer(text="Salu2")
            discord_loop.create_task(self.discord_client.send_embed(embed))
            print("Message sent")
          else:
            self.queue.put(plant_tuple)
        except Exception as e:
          traceback.print_exc()
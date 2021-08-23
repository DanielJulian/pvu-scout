import asyncio
import time

class Manager():
    
    queue = None
    discord_client = None

    def __init__(self, queue, discord_client):
      self.queue = queue
      self.discord_client = discord_client


    def start_plants_monitor(self):
        while True:
            time.sleep(5)
            plant_tuple = self.queue.get()
            plant = plant_tuple[1]
            print(plant)
            asyncio.run(self.discord_client.send_message(plant['waterEndTime']))
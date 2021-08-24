from discord_client import DiscordClient
from plant_api import get_plant_data
from queue import PriorityQueue
from manager import Manager
from db.database import Database
import _thread
import asyncio
import time
from datetime import datetime
from datetime import timedelta


def main():
    # Initialize Database
    database = Database()

    # Insert plant id file in the database
    insert_plant_file_into_db(database)

    # Initialize priority queue
    queue = PriorityQueue()

    # Connect Discord Bot
    discord_client = DiscordClient()
    _thread.start_new_thread(start_discord_client, (discord_client,))

    # Feed priority queue with plants that didnt yet reset from database
    feed_queue_with_yet_to_refresh_plants_db(database, queue)
    
    # Fetch outdated plants, update database and feed priority queue with new plants refresh times
    refresh_outdated_plants(database, queue)

    # Initialize Manager
    manager = Manager(queue, discord_client)
    _thread.start_new_thread(manager.start_plants_monitor, ())

    # Infinite Loop
    while True:
        time.sleep(5000)


def refresh_outdated_plants(database, queue):
    print("About to refresh outdated plants")
    plant_list = database.select_already_refreshed_plants()
    print(len(plant_list), "outdated plants found.")
    for reduced_plant_list in split_list_in_n_parts(plant_list, 500):
        _thread.start_new_thread(fetch_plants_data, (database, reduced_plant_list, queue,))

def fetch_plants_data(database, plant_list, queue):
    for plant_id in plant_list:
        plant_data = get_plant_data(plant_id)
        if plant_data:
            print(plant_data)
            database.insert_plant(plant_data)
            queue.put((plant_data['waterEndTime'].timestamp(), plant_data))
    print("Done fetching Data")
    
def start_discord_client(discord_client):
    discord_client.run("ODc5MTg4MDc5NDk0MjAxNDE0.YSMFtA.pXE9j1rwiBU-r5bdHHowSLMtAfI") 

def split_list_in_n_parts(list, chunk_size):
    return [list[i:i + chunk_size] for i in range(0, len(list), chunk_size)]

def insert_plant_file_into_db(database):
    print("Inserting plant ids from file")
    count = 0
    with open("plant_id_list.txt") as plant_file:
        ids = plant_file.readlines()
        for id in ids:
            database.insert_plant({'id':id.strip()})
            count+=1
    print("Plants inserted:", count)

def feed_queue_with_yet_to_refresh_plants_db(database, queue):
    print("Querying DB for yet to refresh plants")
    plants = database.select_yet_to_refresh_plants()
    print(len(plants), "plants fetched")
    for plant in plants:
        queue.put((datetime.strptime(plant['waterEndTime'].split(".")[0], '%Y-%m-%d %H:%M:%S').timestamp(), plant))

main()
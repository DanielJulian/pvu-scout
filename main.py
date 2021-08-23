from discord_client import DiscordClient
from plant_api import get_plant_data
from queue import PriorityQueue
from manager import Manager
import _thread
import asyncio

def main():
    
    # Initialize priority queue
    queue = PriorityQueue()

    # Connect Discord Bot
    discord_client = DiscordClient()
    _thread.start_new_thread(start_discord_client, (discord_client,))
    


    # Fetch plants data and feed priority queue
    fetch_plants_data(queue)
    # queue.put((123,{'waterEndTime': 5, 'url': 'https://www.google.com.ar/'}))

    # Initialize Manager
    manager = Manager(queue, discord_client)
    _thread.start_new_thread(manager.start_plants_monitor, ())


    while True:
        continue


"""
{
    "status": 0,
    "data": [
        {
            "_id": "61073690ed983ae55eca3df6",
            "stage": "farming",
            "ownerId": "0x9cd4ddf0744723f8f89a68f83d88e9a6ba4e9691",
            "landId": 1026,
            "plantId": 1000711402,
            "plantUnitId": 10007114,
            "plantType": 1,
            "plantElement": "fire",
            "createdAt": "2021-08-02T00:04:32.933Z",
            "updatedAt": "2021-08-21T16:41:12.266Z",
            "__v": 0,
            "harvestTime": "2021-08-23T01:57:07.342Z",
            "rate": {
                "le": 414,
                "hours": 48
            },
            "startTime": "2021-08-21T01:57:07.342Z",
            "land": {
                "elements": {
                    "fire": 1,
                    "water": 0,
                    "ice": 0,
                    "wind": 0,
                    "electro": 0,
                    "parasite": 1,
                    "light": 1,
                    "dark": 0,
                    "metal": 0
                },
                "capacity": {
                    "plant": 30,
                    "motherTree": 5
                },
                "landId": 1026,
                "x": -9,
                "y": 16,
                "totalOfElements": 3,
                "rarity": 2
            },
            "plant": {
                "farmConfig": {
                    "le": 414,
                    "hours": 48
                },
                "stats": {
                    "type": "fire",
                    "hp": 0,
                    "defPhysics": 0,
                    "defMagic": 0,
                    "damagePhysics": 314,
                    "damageMagic": 0,
                    "damagePure": 0,
                    "damageHpLoss": 0,
                    "damageHpRemove": 0
                },
                "type": 1,
                "iconUrl": "https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/7_1.png",
                "rarity": 0,
                "synergy": {
                    "requirement": 5,
                    "description": "This land is immune to: Tsunami, Hurricanne, Snowy, Rain, Cold Wave, Winter Storm."
                }
            },
            "activeTools": [
                {
                    "count": 1,
                    "_id": "611e140d1cd6d595f0708f2f",
                    "id": 2,
                    "type": "POT",
                    "startTime": "2021-08-02T00:07:32.970Z",
                    "endTime": "2021-09-01T00:07:32.970Z"
                },
                {
                    "count": 915,
                    "_id": "611e140d1cd6d595f0708f31",
                    "id": 3,
                    "type": "WATER",
                    "endTime": "2021-08-21T23:13:00.353Z",
                    "startTime": "2021-08-21T00:13:00.353Z"
                }
            ],
            "isTempPlant": false,
            "hasSynergy": true,
            "needWater": false,
            "hasSeed": false,
            "hasCrow": false,
            "pausedTime": null,
            "inGreenhouse": false,
            "count": 52
        },
        {
            "_id": "61073767ed983a5d31ca3e99",
            "stage": "farming",
            "ownerId": "0x9cd4ddf0744723f8f89a68f83d88e9a6ba4e9691",
            "landId": 1026,
            "plantId": 1001314802,
            "plantUnitId": 10013148,
            "plantType": 1,
            "plantElement": "parasite",
            "createdAt": "2021-08-02T00:08:07.852Z",
            "updatedAt": "2021-08-21T16:42:18.282Z",
            "__v": 0,
            "harvestTime": "2021-08-23T05:36:14.597Z",
            "rate": {
                "le": 948,
                "hours": 120
            },
            "startTime": "2021-08-17T06:12:59.385Z",
            "land": {
                "elements": {
                    "fire": 1,
                    "water": 0,
                    "ice": 0,
                    "wind": 0,
                    "electro": 0,
                    "parasite": 1,
                    "light": 1,
                    "dark": 0,
                    "metal": 0
                },
                "capacity": {
                    "plant": 30,
                    "motherTree": 5
                },
                "landId": 1026,
                "x": -9,
                "y": 16,
                "totalOfElements": 3,
                "rarity": 2
            },
            "plant": {
                "farmConfig": {
                    "le": 948,
                    "hours": 120
                },
                "stats": {
                    "type": "parasite",
                    "hp": 0,
                    "defPhysics": 0,
                    "defMagic": 0,
                    "damagePhysics": 148,
                    "damageMagic": 0,
                    "damagePure": 0,
                    "damageHpLoss": 0,
                    "damageHpRemove": 0
                },
                "type": 1,
                "iconUrl": "https://pvuresources.s3.ap-southeast-2.amazonaws.com/icon/plant/13_1.png",
                "rarity": 0,
                "synergy": {
                    "requirement": 10,
                    "description": "All plants/trees (except parasite) productivity is increased by 20%."
                }
            },
            "activeTools": [
                {
                    "count": 1,
                    "_id": "611e14101cd6d595f0709001",
                    "id": 2,
                    "type": "POT",
                    "startTime": "2021-08-02T00:08:12.894Z",
                    "endTime": "2021-09-01T00:08:12.894Z"
                },
                {
                    "count": 463,
                    "_id": "611e14101cd6d595f0709003",
                    "id": 3,
                    "type": "WATER",
                    "endTime": "2021-08-22T07:12:59.385Z",
                    "startTime": "2021-08-21T06:12:59.385Z"
                }
            ],
            "isTempPlant": false,
            "hasSynergy": true,
            "needWater": false,
            "hasSeed": false,
            "hasCrow": false,
            "pausedTime": null,
            "inGreenhouse": false,
            "count": 75
        }
    ],
    "total": 510
}

"""


def fetch_plants_data(queue):
    plant_data = get_plant_data("6107492d24f6e7bbc4d23e22")

    if plant_data:
        print(plant_data)
        queue.put((plant_data['waterEndTime'].timestamp(), plant_data))
    
def start_discord_client(discord_client):
    discord_client.run("ODc5MTg4MDc5NDk0MjAxNDE0.YSMFtA.pXE9j1rwiBU-r5bdHHowSLMtAfI")

main()
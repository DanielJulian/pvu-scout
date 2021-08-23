from discord_client import DiscordClient
from plant_api import get_plant_data
from queue import PriorityQueue
from manager import Manager
import _thread
import asyncio
from datetime import datetime
from datetime import timedelta


plant_list = [
        "6107e80ffd5f7332d14eaee5",
        "6107e839fd5f7327204eaf87",
        "6107e99e2586b489e1408a26",
        "6107e9ba8ff48ed090b05a42",
        "6107e9c88ff48e4007b05a74",
        "6107e9d58ff48ef87fb05aa2",
        "6107ea9e2586b448b6408d38",
        "6107ead5fd5f733e7e4eb81d",
        "6107eb03b4acb9da0c3c9850",
        "6107eb27b4acb9409c3c98cf",
        "6107ef488ff48e46e9b06b2e",
        "6107ef79fd5f73032d4ec68d",
        "6107f22a4fff3335756d3b68",
        "6107f24c058111c03e12b587",
        "610806381280702e29bcf67b",
        "610806545abbe7851f382f7a",
        "6108066e1280703f2ebcf6fa",
        "610806ae1f7b6f452d1d0f5e",
        "610806db1f7b6f79de1d0fe6",
        "610806f31f7b6f9a5f1d102a",
        "6108074c8e7e9b7601a21651",
        "610820a33fffaa5614c2981e",
        "610820bb620c367e145cfb31",
        "610820d5620c3665fe5cfbcb",
        "61082119ae6dd13c009fed56",
        "61082164df29fd42fc2c502e",
        "610821833fffaa3321c29cf8",
        "610821a5620c365b3e5d006d",
        "610821cd3fffaaaa65c29e1d",
        "610821f2620c36165d5d0194",
        "6108222d3fffaa9560c29fcd",
        "6108276cae6dd1b82fa00be5",
        "6108276eae6dd101eea00beb",
        "6108276fdf29fdfb792c6c74",
        "61082a2f3fffaa037ac2c2f1",
        "61082a2fae6dd118f3a01530",
        "61082a34620c368d205d2568",
        "61082a35620c3602475d256a",
        "61082a353fffaa6de7c2c2fb",
        "61082a87ae6dd142eba015fd",
        "61082aaadf29fd773a2c76c2",
        "61082aab3fffaa4dc9c2c43a",
        "61082aac3fffaa4df3c2c43c",
        "61082b03620c36b4675d2715",
        "61082b063fffaa46d1c2c50e",
        "61082b81620c36570c5d2853",
        "61082d143fffaa7074c2c8a7",
        "61082e65620c368e845d2d83",
        "61082f0edf29fdce602c7f56",
        "61082f0f620c36f6655d2ec3",
        "61082f11df29fdb71d2c7f5d",
        "6108359d620c3614a15d38e0",
        "6108364fae6dd165b9a029f7",
        "610837754b9fb270162476ab",
        "61084bff4b9fb22b43248605",
        "61084c49ae6dd1427ca03c07",
        "61084c78df29fdfbb82c9e3d",
        "61084c794b9fb29bb824869f",
        "61084c7aae6dd1ebb2a03c41",
        "61084f57ae6dd107a3a0403e",
        "61084f9dae6dd14c81a0409c",
        "610850e9df29fd0d2f2ca535",
        "61085d5fae6dd144f4a050e3",
        "61085ee0620c365d335d6248",
        "61085ee14b9fb2116a249c70",
        "610860efae6dd13623a05375",
        "6108616f620c36f23c5d6425",
        "6109b49aae6dd1431ca1d154",
        "6109b4beb4e392028e37e49b",
        "6109b4d0d24ad367dfea17f9",
        "6109b61b1e804eb92606b79a",
        "6109b633ae6dd1729fa1d223",
        "6109b638ae6dd1ef1fa1d224",
        "6109b63eae6dd1028fa1d226",
        "6109b64230e3bc0e4d8c071e",
        "6109b647205c3193a9d436ea",
        "610a8a57be41bc00220081b4",
        "610a9fbe728db2001bee02ce",
        "610a9fc246fe570029524046",
        "610aa009d17c3b0030a36561",
        "610aa00d15601c0023e17e8c",
        "610aa42cd4954b001cc55a64",
        "610aeab7413910001cd3f08a",
        "610aecc1bd50fb001c570688",
        "610aef1ab8eff7001c3f2376",
        "610bc783808f716bb0818313",
        "610bc8f8728a1debaf6e786e",
        "610bd9a3edc04331afb3a95f",
        "610bd9f1b848256b19699085",
        "610bdac0492a51fe89ee7d8e",
        "610bdbd98a964088166d4e93",
        "610bdbe75ee06d6c84bd43eb",
        "610bdc3f808f719890819dfe",
        "610bdc6ca40349992640c950",
        "610bdcb8528a2eb3e990ca98",
        "610c028cbc0ff9001d02844a",
        "610ea82fc43d47001dcfdd59",
        "610ea8739453950022a9dee8",
        "61103a11c132e7001d75bc47",
        "6111dbb5707adf001c8b39c7",
        "6111dbc3707adf001c8b39db",
        "6113374bca4e0e001bc5e6e4",
        "611337551838db002a8d6599",
        "61133758a78a4b001cfb6f1d",
        "611337a5923e02001ccb4a5c",
        "611337e4e149750022aa958c",
        "611337eca433b0001bbbc79f",
        "611337f3923e02001ccb4a91",
        "611493feca2197be12c0484b",
        "611494f85050432f34880ae2",
        "611499e4b7c32f39ea82aad6",
        "6115e508f130cb0012a6235d",
        "6115e527c601750012fee5f7",
        "6115ea4acfef67001ca9395b",
        "6115ed3669cbf30012dc6a13",
        "611695a26fd2720012c1411c",
        "611742c54a3dcd0019d9cbf7",
        "611742c9b586700019a641b6",
        "611742e6bad442001ae76bd4",
        "6117cca58927e90013964c0f",
        "6119a611fa07d40019b759c7",
        "6119a63e48e4130019fbef98",
        "6119a8142fc4ff001a8aa7ab",
        "6119a893200a2a0012e764ef",
        "6119ad5ea59b18001b96fc0c",
        "6119b0a880eba00019f91b55",
        "6119b0ad07c4a6001d66a304",
        "611ebc42f09fca001a0fa640",
        "611ebd92ffe738001badd2d0",
        "611ebd968215b8001394ef0d",
        "611ebe43f09fca001a0fb57a",
        "611ebe477d1fed001ac55da7",
        "611ebe6d38c9990019abf9f3",
        "611ec2889cd088001a74fd3d",
        "611ec28c9e200900132b5223",
        "611ec3a81472ea001494313f",
        "611eebe4cb460f001425438a",
        "611eecd380230e0014beebf8",
        "61208e975bdc4a0019a8dc47",
        "61208e9915c0b50012dfed11",
        "61208e9cefcb44001baa2d01",
        "61208e9e1cdf3e001a14a798",
        "61208ea031f6af00137c5745",
        "61208ea213966f0012c60ed2",
        "61208eaeb4723d0019d8e941",
        "61208eb03d51fb0012a1a2ae",
        "61208eb2e0d0b3001912dc42",
        "61208eb5b4d355001412093e",
        "61208eb8624ac5001aaaeef9",
        "61208f1993ac7d0019582043",
        "61208f1c979dd20012c48c95",
        "61208f1faeeeea0012220f85",
        "61208f3e4803690019f68e3e",
        "61208f551bbbb3001b0f7c65",
        "61208f5767c71f001b6689ba",
        "61208f5dd9800a0013192b9e",
        "61208f601bbbb3001b0f7c74",
        "61208f623d51fb0012a1a38e",
        "61208f6513966f0012c60fb6",
        "61208f693d51fb0012a1a39d",
        "61208f6ed4d779001262e7a2",
        "61208f71eac1ad001971ce60",
        "61208f7715c0b50012dfee28",
        "612090707ced38001309fcd0",
        "612090741bbbb3001b0f7dac",
        "6120907b93ac7d00195821cc",
        "6120908179ab15001bcaffd4",
        "612090aa624ac5001aaaf14d",
        "612090b0efcb44001baa2fa3",
        "61209103d9800a0013192d0a",
        "6120910615c0b50012dfefd0",
        "6120910a47234b00127415b2",
        "6120910c3fdea3001441756b",
        "61209111eac1ad001971d03f",
        "612091153d51fb0012a1a53d",
        "61209119763fce001aaaab3a",
        "6120911e13966f0012c6119f",
        "61209123343bf30019f2ac07",
        "6120912507212500192c5e20",
        "6120912ba71abe001251df89",
        "6120912f343bf30019f2ac1e",
        "61209133f6f7c400137ddb3e",
        "61209137f32ece0016ef332b",
        "6120916bb501fb00128de2ff",
        "6120916d6273e0001c4f00bc",
        "6120916f5c6efd001a78c91b",
        "612091711bbbb3001b0f7e8b",
        "61209173e8d32e001a74e68e",
        "61209174ea1c7f0013352517",
        "61209177126ce80012121bb6",
        "612091c147234b00127416be",
        "612091c315c0b50012dff0da",
        "612175135d444a0019701a20",
        "6121757d38039b001aa8fb09"
    ]

def main():
    
    # Initialize priority queue
    queue = PriorityQueue()

    # Connect Discord Bot
    discord_client = DiscordClient()
    _thread.start_new_thread(start_discord_client, (discord_client,))
    


    # Fetch plants data and feed priority queue
    _thread.start_new_thread(fetch_plants_data, (queue,))
    # queue.put((123,{'waterEndTime': datetime.now() + timedelta(minutes=2), 'url': 'https://www.google.com.ar/'}))

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
    for plant_id in plant_list:
        plant_data = get_plant_data(plant_id)

        if plant_data:
            print(plant_data)
            queue.put((plant_data['waterEndTime'].timestamp(), plant_data))
    
def start_discord_client(discord_client):
    discord_client.run("ODc5MTg4MDc5NDk0MjAxNDE0" + ".YSMFtA.pXE9j1rwiBU-r5bdHHowSLMtAfI")

main()
import requests
import traceback
from datetime import datetime, timedelta

plant_base_url = 'https://backend-farm.plantvsundead.com/farms/'

headers = {
        "sec-ch-ua":"\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
        "Accept":"application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Authorization": "Bearer Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwdWJsaWNBZGRyZXNzIjoiMHg2MmFkNWE5YzQxNjY2Mzc0ZTQ1OWRlNjJiZmVhMjBmOGNlZTc0NjY1IiwibG9naW5UaW1lIjoxNjI5NjQyMDc5ODkwLCJjcmVhdGVEYXRlIjoiMjAyMS0wOC0xOSAxNTo1NjoxNSIsImlhdCI6MTYyOTY0MjA3OX0.Kg5mbW0ySOm7zf_JIm35pNw4HMTq2qfpnmpZj5y8noA"
    }

def get_plant_data(plant_id):

    url = plant_base_url + plant_id
    response = requests.get(url, headers=headers)
    data = dict()
    try:
        if (response.status_code == 503):
            print("API Unavailable")
            return None
        
        if (response.status_code == 504):
            print("Timeout")
            return None

        if (response.status_code == 502):
            print("Bad Gateway")
            return None

        jsonresponse = response.json()

        if (jsonresponse['status'] == 0): # status = 0 -> OK
            data['id'] = plant_id
            water_end_time = jsonresponse['data']['activeTools'][1]['endTime'].replace("T", " ").split(".")[0]
            data['water_end_time'] = datetime.strptime(water_end_time, '%Y-%m-%d %H:%M:%S') - timedelta(hours=3)

    except Exception as e:
        print(response)
        traceback.print_exc()
        return None
        
    return data
    



def get_farm_data(plant_id):

    url = 'https://backend-farm.plantvsundead.com/farms/other/0xe4e2fe2da648aedb4b06f0829b8d2c4a01b12d80?limit=10&offset=40'
    
    params = {
        "limit": 10,
        "offset": 40
    }
    headers = {
        "sec-ch-ua":"\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
        "Accept":"application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwdWJsaWNBZGRyZXNzIjoiMHg2MmFkNWE5YzQxNjY2Mzc0ZTQ1OWRlNjJiZmVhMjBmOGNlZTc0NjY1IiwibG9naW5UaW1lIjoxNjI5NjQyMDc5ODkwLCJjcmVhdGVEYXRlIjoiMjAyMS0wOC0xOSAxNTo1NjoxNSIsImlhdCI6MTYyOTY0MjA3OX0.Kg5mbW0ySOm7zf_JIm35pNw4HMTq2qfpnmpZj5y8noA"
    }

    response = requests.get(url, headers=headers, params=params).json()

    print(response)
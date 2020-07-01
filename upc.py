import requests
from endpoints import BASE_URL

def update_upc(upcId,header,payload):
    url = f'{BASE_URL}/v2/super-admin/upcs/{upcId}'

    response = requests.patch(url,headers=header,data=payload)

    response.raise_for_status()

    if response.status_code == 200:
        print(f'{upcId} Updated')
        return True
    else:
        print(f'{upcId} Update Failed')
        return False

    
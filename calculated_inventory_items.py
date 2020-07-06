import requests
from endpoints import BASE_URL

def update_calculated_inventory_item(calculated_inventory_item_uuid,header,payload):
    url = f'{BASE_URL}/v2/admin/calculated-inventory-items/{calculated_inventory_item_uuid}'

    response = requests.patch(url,headers=header,data=payload)

    response.raise_for_status()

    if response.status_code == 200:
        print(f'{calculated_inventory_item_uuid} Updated')
        return True
    else:
        print(f'{calculated_inventory_item_uuid} Update Failed')
        return False
    
def get_calulated_inventory_item(calculated_inventory_item_uuid,header):
    url = f'{BASE_URL}/v2/admin/calculated-inventory-items/{calculated_inventory_item_uuid}'
    
    response = requests.get(url,headers=header)
    response.raise_for_status()
    return response.json()
from tokens import read_token,write_new_token
from upc import update_upc,get_upc
from inventory_items import update_inventory_item,get_inventory_item
from calculated_inventory_items import update_calculated_inventory_item, get_calulated_inventory_item
import csv

def update(input_file):
    header = {'x-access-token': read_token()}
    errors = []

    with open(input_file,'r') as f:
        reader = csv.reader(f)
        for line in reader:
            uuid = line[0]

            #Task specific body for info to be updated
            body = {}

            if not update_upc(uuid,header,body):
                errors.append(uuid)
        
        return errors 

if __name__ == '__main__':
    input_file = input('Enter path to input csv file: ')
    update(input_file)
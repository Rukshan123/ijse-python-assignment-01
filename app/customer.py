import sys
import json
import os
from pprint import pprint

__db_location__ = "db"
__customer_folder__  =  f"{__db_location__}/customer"
__customer_last_id__  =  f"{__db_location__}/customer/customer_id.db"

def cus_init(arguments):
 
    def db():
        os.makedirs(__customer_folder__)

    section = arguments[0]
    if section == "init":
        command = arguments[1]
        params = arguments[2:]
        if command == "db":
            db()

class Customer:
    def __init__(customer):
        if os.path.exists(__customer_last_id__):
            with open(__customer_last_id__, "r") as last_id_f:
                customer.last_id = int(last_id_f.readline()) 
        else:
            customer.last_id = 0

    def save(customer):
        id = customer.last_id+1 

        # save db customer
        _data_ = {
            "id" : id,
            "name" : customer.name,
            "address" : customer.address,
            "salary" : customer.salary,
            "phone" : customer.phone
            
        }
        with open(f"{__customer_folder__}/{id}.db","w") as customer_file:
            json.dump(_data_ ,customer_file)
     
        customer.last_id +=1
        with open(__customer_last_id__,"w") as f:
            f.write(str(customer.last_id))



def customer_save(name,address, salary, phone): 
    customer = Customer()
    customer.name = name
    customer.address = address
    customer.salary = salary
    customer.phone = phone
    
    customer.save()
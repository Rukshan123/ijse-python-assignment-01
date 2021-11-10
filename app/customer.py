import sys
import json
import os
from pprint import pprint

__db_location__ = "db"
__customer_folder__  =  f"{__db_location__}/customer"
__customer_last_id__  =  f"{__db_location__}/customer_id.db"

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

    def get(self,  id):
        Customer.__get_customer_by_path(self,f"{__customer_folder__}/{id}.db")


    def __get_customer_by_path(customer, path):
         with open(path , "r") as customer_file:  
            _data_ = json.load(customer_file)
            customer.id = _data_["id"]
            customer.name = _data_["name"]
            customer.address = _data_["address"]
            customer.salary = _data_["salary"]
            customer.phone = _data_["phone"]
        

    def all(self):
        # Get all fil names
        customer_file_names = os.listdir(__customer_folder__)
        customers = []
          # append to array
        for customer_file_name in customer_file_names:
            customer = Customer()
            Customer.__get_customer_by_path(customer,f"{__customer_folder__}/{customer_file_name}")
            
            customers.append(customer)
        return customers


    def search(self,key,value):
        customer = self.all()
        result_customer = []
        for customer in customer:
            customer_value = getattr(customer,key)
            if customer_value == value:
                result_customer.append(customer)
        return result_customer      


    def __repr__(self):
        return f"id:{self.id},name:{self.name},address:{self.address},salary:{self.salary},phone:{self.phone}" 

    def __str__(self):
        return f"id:{self.id},name:{self.name},address:{self.address},salary:{self.salary},phone:{self.phone}" 



def customer_save(name,address, salary, phone): 
    customer = Customer()
    customer.name = name
    customer.address = address
    customer.salary = salary
    customer.phone = phone
    
    customer.save()

def customer_all():
    customer = Customer()
    customers = customer.all()
    pprint(customers)

def customer_view(id):
    customer = Customer()
    customer.get(id)
    print(customer.id, customer.name, customer.address, customer.salary, customer.phone)

def customer_search(key,value):
    customer = Customer()
    results = customer.search(key,value)
    pprint(results)
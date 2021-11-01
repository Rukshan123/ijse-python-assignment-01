import sys
import json
import os
from pprint import pprint

__db_location__ = "db"
__session_file__  = f"{__db_location__}/session.db"
__item_folder__  =  f"{__db_location__}/item"
__item_last_id__  =  f"{__db_location__}/item_id.db"

def init(arguments):

    def db():
        os.makedirs(__item_folder__)

    section = arguments[0]
    if section == "init":
        command = arguments[1]
        params = arguments[2:]
        if command == "db":
            db()

def login(username):
    user = username 
    f = open(__session_file__,"w")
    f.write(username)
    f.close()

def __get_logged_user():
    f = open(__session_file__,"r") 
    username = f.readline()
    return username

def view():
    username = __get_logged_user()
    print(username)


class Item:
    def __init__(item):
        if os.path.exists(__item_last_id__):
            with open(__item_last_id__, "r") as last_id_f:
                item.last_id = int(last_id_f.readline()) 
        else:
            item.last_id = 0  

    def save(item):
        id = item.last_id+1 

        # save db items
        _data_ = {
            "id" : id,
            "name" : item.name,
            "price" : item.price,
            "sellingPrice" : item.selling_price
        }
        with open(f"{__item_folder__}/{id}.db","w") as item_file:
            json.dump(_data_ ,item_file)
        # print(item.last_id)

        # save next Id
        item.last_id +=1
        with open(__item_last_id__,"w") as f:
            f.write(str(item.last_id))



def item_create(name,price, selling_price): 
    item = Item()
    item.name = name
    item.price = price
    item.selling_price = selling_price
    
    item.save()


if __name__=="__main__":
    arguments = sys.argv[1:]
    init(arguments)
    section = arguments[0]
    command = arguments[1]
    params = arguments[2:]

    if section == "user":
         if command == "login":
             login(*params )
         elif command == "view":
             view() 
    elif section == "item":
         if command == "create":
              item_create(*params)

    
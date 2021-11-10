import sys
import json
import os
from pprint import pprint
from app.item import init
from app.item import login
from app.item import view
from app.item import item_create
from app.item import item_all
from app.item import item_view
from app.item import item_search

from app.customer import cus_init
from app.customer import customer_save
from app.customer import customer_all
from app.customer import customer_view



if __name__=="__main__":
    arguments = sys.argv[1:]
    init(arguments)
    cus_init(arguments)
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
         elif command  == "all":
              item_all()
         elif command  == "view":
              item_view(*params)
         elif command  == "search":
              item_search(*params)
    elif section == "customer":
         if command == "save":
              customer_save(*params)
         elif command  == "all":
              customer_all()
         elif command  == "view":
              customer_view(*params)


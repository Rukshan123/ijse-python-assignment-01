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
         elif command  == "all":
              item_all()
         elif command  == "view":
              item_view(*params)

    
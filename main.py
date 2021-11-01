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

    
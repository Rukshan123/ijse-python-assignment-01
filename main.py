import sys
import json
import os
from pprint import pprint

__db_location__ = "db"
__session_file__  = f"{__db_location__}/session.db"
__item_folder__  =  f"{__db_location__}/item"
__item_last_id__  =  f"{__db_location__}/item_id.db"
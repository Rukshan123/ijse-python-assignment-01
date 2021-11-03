import sys
import json
import os
from pprint import pprint

__db_location__ = "db"
__session_file__  = f"{__db_location__}/session.db"
__customer_folder__  =  f"{__db_location__}/customer"
__customer_last_id__  =  f"{__db_location__}/customer_id.db"
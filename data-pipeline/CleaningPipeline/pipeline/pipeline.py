from funcDeclare import *
from loctools import *
import os
import sqlite3

"""
Important Note

This pipeline will be finalized in the main branch

Where it will be possible to run it once, and have all the data ready

Currently it is prototypal and mainly used to test function output

bleh :P
"""

parentDir = "C:\\Users\\TK\\PycharmProjects\\SentiWin\\data-pipeline\\datasets\\"

bronzeData = "..\\..\\datasets\\bronzeData\\Video_Games.txt"

titledData = "..\\..\\datasets\\silverData\\titledReviews.txt"
untitledData = "..\\..\\datasets\\silverData\\untitledReviews.txt"

titled_exists = os.path.isfile(parentDir + titledData)
untitled_exists = os.path.isfile(parentDir + untitledData)

# removing_unnecessary_lines(parentDir + bronzeData, parentDir + titledData)
# remove_the_titles()

# create_db()
fill_database(untitledData)
# display_table("titles")
# 
parentDir = "C:\\Users\\TK\\PycharmProjects\\SentiWin\\data-pipeline\\datasets\\goldData\\"
db_name = "database.db"

# try:
#    init_clean()
#    second_clean()
#    third_clean()
#    fourth_clean()
# the fourth clean function throws an index error at the end of execution
# however it doesn't affect the quality or integrity of the output
# except IndexError:
#    print()
# finally:
#    fifth_clean()
#    into_csv()
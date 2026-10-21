from funcDeclare import *
import os

"""
Important Note

This pipeline will be finalized in the main branch

Where it will be possible to run it once, and have all the data ready

Currently it is prototypal and mainly used to test function output

bleh :P
"""

parentDir = "C:\\Users\\TK\\PycharmProjects\\SentiWin\\data-pipeline\\datasets\\"

bronzeData = "..\\..\\datasets\\bronze-data\\Video_Games.txt"
bronze1k = "..\\..\\datasets\\bronze-data\\Video_Games1k.txt"
titled1k = "..\\..\\datasets\\silver-data\\titledReviews1k.txt"
untitled1k = "..\\..\\datasets\\silver-data\\untitledReviews1k.txt"

urGold1k = "..\\..\\datasets\\gold-data\\urGold1k.csv"

titledData = "..\\..\\datasets\\silver-data\\titledReviews.txt"
untitledData = "..\\..\\datasets\\silver-data\\untitledReviews.txt"

titled_exists = os.path.isfile(parentDir + titledData)
untitled_exists = os.path.isfile(parentDir + untitledData)

# removing_unnecessary_lines(parentDir + bronzeData, parentDir + titledData)
# remove_the_titles()

# create_db()
# fill_database(untitledData)
# display_table("titles")

truncate_file_tooled(bronzeData, bronze1k, 1000)
removing_unnecessary_lines(bronze1k, titled1k, 1)
pyremove_titles(titled1k, untitled1k)

pycsv_ready(untitled1k, urGold1k, "title", "reviews")

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
from funcDeclare import *
from loctools import *
import os

parentDir = "C:\\Users\\TK\\PycharmProjects\\SentiWin\\data-pipeline\\datasets\\"

bronzeData = "..\\..\\datasets\\bronzeData\\Video_Games.txt"

titledData = "..\\..\\datasets\\silverData\\titledReviews.txt"
untitledData = "..\\..\\datasets\\silverData\\untitledReviews.txt"

titled_exists = os.path.isfile(parentDir + titledData)
untitled_exists = os.path.isfile(parentDir + untitledData)

# removing_unnecessary_lines(parentDir + bronzeData, parentDir + titledData)
remove_the_titles()

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
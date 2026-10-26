from funcDeclare import *
import os

"""

The pipeline is supposed to:
    1. Make the necessary base files: vg1k...
    2. Handle each one of them, and turn them into csvs

"""

parentDir = "C:\\Users\\TK\\PycharmProjects\\SentiWin\\data-pipeline\\datasets\\"

bronzeData = "bronze-data\\Video_Games.txt"

bronze1k = "bronze-data\\Video_Games1k.txt"
bronze10k = "bronze-data\\Video_Games10k.txt"
bronze_scnd10k =  "bronze-data\\Video_Games_scnd_10k.txt"

titled_rev_1k = "silver-data\\titledReviews1k.txt"
titled_rev_10k = "silver-data\\titledReviews10k.txt"
titled_rev_scnd10k = "silver-data\\titledReviews_scnd10k.txt"

score_price_1k = "silver-data\\scorePrice1k.txt"
score_price_10k = "silver-data\\scorePrice10k.txt"
score_price_scnd10k = "silver-data\\scorePrice_scnd1k.txt"

untitled_rev_1k = "silver-data\\untitledReviews1k.txt"
untitled_rev_10k = "silver-data\\untitledReviews10k.txt"
untitled_rev_scnd10k = "silver-data\\untitledReviews_scnd10k.txt"

untitled_score_1k = "silver-data\\untitledScore1k.txt"
untitled_score_10k = "silver-data\\untitledScore10k.txt"
untitled_score_scnd10k = "silver-data\\untitledScore_scnd10k.txt"

untitled_rev_Gold1k = "gold-data\\untitledRev_Gold1k.csv"
untitled_rev_Gold10k = "gold-data\\untitledRev_Gold10k.csv"
untitled_rev_Gold_scnd10k = "gold-data\\untitledRev_Gold_scnd10k.csv"

untitled_score_Gold_1k = "silver-data\\untitledScore_Gold1k.txt"
untitled_score_Gold_10k = "silver-data\\untitledScore_Gold10k.txt"
untitled_score_Gold_scnd10k = "silver-data\\untitledScore_Gold_scnd10k.txt"

titledData = "silver-data\\titledReviews.txt"
untitledData = "silver-data\\untitledReviews.txt"

titled_exists = os.path.isfile(parentDir + titledData)
untitled_exists = os.path.isfile(parentDir + untitledData)

truncate_file_tooled(bronzeData, bronze1k, 0, 1000)
rm_unwanted_lines(bronze1k, titled_rev_1k, 1)
pyremove_titles(titled_rev_1k, untitled_rev_1k)

pycsv_ready(untitled_rev_1k, untitled_rev_Gold1k, "title", "reviews")

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
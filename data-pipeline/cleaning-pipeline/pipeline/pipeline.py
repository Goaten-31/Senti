from module import *

"""
The pipeline is supposed to:
    1. Make the necessary base files: vg1k...
    2. Handle each one of them, and turn them into csvs

The file path and method definitions are found in module.py
"""


truncate_file_tooled(bronzeData, bronze1k, 0, 1000)
truncate_file_tooled(bronzeData, bronze10k, 0, 10000)


rm_unwanted_lines(bronze1k, titled_rev_1k, 'tirev')
rm_unwanted_lines(bronze10k, titled_rev_10k, 'tirev')

pyremove_titles(titled_rev_1k, untitled_rev_1k)
pyremove_titles(titled_rev_10k, untitled_rev_10k)

pycsv_ready(untitled_rev_1k, untitled_rev_Gold1k, "title", "reviews")
pycsv_ready(untitled_rev_10k, untitled_rev_Gold10k, "title", "reviews")
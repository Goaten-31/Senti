import itertools as it
from os import path
import os
# import loctools as lt


def find_error(func):
    def inner():
        try:
            func()
        except Exception as e:
            print(f"Error found in {func.__name__}, Type: {type(e)}, Detail: {e}")
    return inner

#truncating the file into smaller sizes

def truncate_file_tooled(input_file: str, output_file: str, starting_line: int, ending_line: int):
    with open(input_file, 'r') as infile, open(output_file, 'w+') as outfile:

            for line_number, line in enumerate(infile, start=1):
                
                if starting_line <= line_number:
                    outfile.write(line)
                    
                    if line_number >= ending_line and not line.strip():
                        break
                        
                else:
                    continue

#clearing out all the unneeded lines

def title_review_filter(s):
    if 'product/title' in s or 'review/text' in s:
        return False
    return True

def title_price_score_filter(s):
    if 'product/title' in s or 'product/price' in s or 'review/score' in s:
        return False
    return True

def rm_unwanted_lines(input_file_path, output_file_path, filter_function):
    match filter_function:
        case 'tirev':
            filter_function = title_review_filter
        case 'tiprsc':
            filter_function = title_price_score_filter
    try:
        with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
            part = it.islice(infile, 5100359)
            outfile.writelines(it.filterfalse(filter_function, part))
        return 0
    except Exception as e:
        print(f"Error in rm_unwanted_lines. Details: {e}")
        return 1

def pyremove_titles(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        for line in infile:
            outfile.writelines(line[line.index(' ') + 1: ])

def pycsv_ready(input_file_path, output_file_path, *args):
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        
        for i, arg in enumerate(args, start=1):
            if i % len(args) == 0:
                outfile.write(f"{arg}," + '\n')
            else:
                outfile.write(f"{arg},")
                
        for line_index, line in enumerate(infile, start=1):
            line = line.replace('\n', ',')
            
            if line_index % len(args) == 0:
                line = line.replace('"', '')
                outfile.write(line.replace(',', ';') + '\n')
            else:
                outfile.write(line)


# Definition of file paths

init_step = os.getcwd() + os.sep + os.pardir
parentDir = str(os.path.normpath(init_step + os.sep + os.pardir) + '/datasets/')

bronzeData = parentDir + "dataDump\\Video_Games.txt"

bronze1k = parentDir + "bronze-data\\Video_Games1k.txt"
bronze10k = parentDir + "bronze-data\\Video_Games10k.txt"
bronze_scnd10k =  parentDir + "bronze-data\\Video_Games_scnd_10k.txt"

titled_rev_1k = parentDir + "silver-data\\titledReviews1k.txt"
titled_rev_10k = parentDir + "silver-data\\titledReviews10k.txt"
titled_rev_scnd10k = parentDir + "silver-data\\titledReviews_scnd10k.txt"

score_price_1k = parentDir + "silver-data\\scorePrice1k.txt"
score_price_10k = parentDir + "silver-data\\scorePrice10k.txt"
score_price_scnd10k = parentDir + "silver-data\\scorePrice_scnd1k.txt"

untitled_rev_1k = parentDir + "silver-data\\untitledReviews1k.txt"
untitled_rev_10k = parentDir + "silver-data\\untitledReviews10k.txt"
untitled_rev_scnd10k = parentDir + "silver-data\\untitledReviews_scnd10k.txt"

untitled_score_1k = parentDir + "silver-data\\untitledScore1k.txt"
untitled_score_10k = parentDir + "silver-data\\untitledScore10k.txt"
untitled_score_scnd10k = parentDir + "silver-data\\untitledScore_scnd10k.txt"

untitled_rev_Gold1k = parentDir + "gold-data\\untitledRev_Gold1k.csv"
untitled_rev_Gold10k = parentDir + "gold-data\\untitledRev_Gold10k.csv"
untitled_rev_Gold_scnd10k = parentDir + "gold-data\\untitledRev_Gold_scnd10k.csv"

untitled_score_Gold_1k = parentDir + "gold-data\\untitledScore_Gold1k.csv"
untitled_score_Gold_10k = parentDir + "gold-data\\untitledScore_Gold10k.csv"
untitled_score_Gold_scnd10k = parentDir + "gold-data\\untitledScore_Gold_scnd10k.csv"

titledData = "silver-data\\titledReviews.txt"
untitledData = "silver-data\\untitledReviews.txt"

#These are relics of an ancient time
"""
def remove_the_titles(batch : int):
    try:
        lt.remove_titles(batch)
        return 0
    except Exception as e:
        print(f"Error in the first step of processing. Removing Titles. Details: {e}")
        return 1

def add_the_commas(batch : int, reset : int):
    try:
        lt.add_commas(batch, reset)
        return 0
    except Exception as e:
        print(f"Error in the first step of processing. Adding Commas. Details: {e}")
        return 1
"""
import itertools as it
import sqlite3 as db
import os
import loctools as lt

#truncating the file into smaller sizes
def truncate_file(starting_line: int, ending_line: int, name_of_file: str):
    with open('../raw-Data/Video_Games.txt', 'r') as outerFile:
        counter = 0

        for line in outerFile:
                counter += 1
                if starting_line <= counter:
                    with open(f"../truncatedData/{name_of_file}.txt", 'a') as innerFile:
                        innerFile.writelines(line)
                        if counter >= ending_line and not line.strip():
                            break
                else:
                    continue
    return counter + 1


def truncate_file_tooled(input_file: str, output_file: str):
    with open(f'../raw-Data/{input_file}.txt', 'r') as infile, open(f'../txtData/{output_file}.txt', 'w+') as outfile:
        for line_number, line in enumerate(infile, start=1):
            outfile.write(line)

            if line_number >= 100 and not line.strip():
                break

#clearing out all the unneeded lines
def title_review_filter(s):
    if 'product/title' in s or 'review/text' in s:
        return False
    return True

def title_price_score_filter(s):
    if 'product/title' in s or 'product/price' in s or 'review/score' in s:
        return False
    return True

def removing_unnecessary_lines(input_file_path, output_file_path, filter_function):
    try:
        with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
            part = it.islice(infile, 5100359)
            outfile.writelines(it.filterfalse(filter_function, part))
        return 0;
    except Exception as e:
        print(f"Error in the first step of processing. Details: {e}")
        return 1;

#Here the paths should be written explicitly, but I'll get to it
def remove_the_titles(batch : int):
    try:
        lt.remove_titles(batch)
        return 0;
    except Exception as e:
        print(f"Error in the first step of processing. Removing Titles. Details: {e}")
        return 1;

def add_the_commas(batch : int, reset : int):
    try:
        lt.add_commas(batch, reset)
        return 0;
    except Exception as e:
        print(f"Error in the first step of processing. Adding Commas. Details: {e}")
        return 1;

def create_db():

    parentDir = "C:\\Users\\TK\\PycharmProjects\\SentiWin\\data-pipeline\\datasets\\goldData\\"
    db_name = "database.db"
    
    conn = db.connect(parentDir + db_name)

    cur = conn.cursor()


    conn.execute("CREATE TABLE titles(title TEXT);")
    conn.execute("CREATE TABLE reviews(review TEXT);")
        
    conn.commit()

    conn.close()

def fill_database(file_path):
    parentDir = "C:\\Users\\TK\\PycharmProjects\\SentiWin\\data-pipeline\\datasets\\goldData\\"
    db_name = "database.db"
    
    conn = db.connect(parentDir + db_name)

    index = 1
    with open(file_path, "r") as infile:
        for line in infile:
            if index % 2:
                conn.execute(
                """
                INSERT INTO reviews (review) VALUES (?);
                """, (line,)
                )
                conn.commit()
            else:
                conn.execute(
                """
                INSERT INTO title (title) VALUES (?);
                """, (line,)
                )
                conn.commit()
            index += 1

    conn.close()

def display_table(table_name):

    parentDir = "C:\\Users\\TK\\PycharmProjects\\SentiWin\\data-pipeline\\datasets\\goldData\\"
    db_name = "database.db"
    
    conn = db.connect(parentDir + db_name)
    
    a= conn.execute(f"PRAGMA table_info('{table_name}')")
    
    for i in a:
    
         print(i)

    conn.commit()
    
    conn.close()
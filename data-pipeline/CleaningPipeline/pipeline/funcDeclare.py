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
def full_check(s):
    if 'product/title' in s or 'review/text' in s:
        return False
    return True

def removing_unnecessary_lines(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
            part = it.islice(infile, 5100359)
            outfile.writelines(it.filterfalse(full_check, part))
        return 0;
    except Exception as e:
        print(f"Error in the first step of processing. Details: {e}")
        return 1;

#Here the paths should be written explicitly, but I'll get to it
def remove_the_titles():
    try:
        lt.remove_titles()
        return 0;
    except Exception as e:
        print(f"Error in the first step of processing. Details: {e}")
        return 1;


def create_db(file_path):
    
    db_name = "database.db"
    
    conn = db.connect(db_name)

    cur = conn.cursor()

    if not os.path.isfile(db_name):
    
        cur.execute("""
            CREATE TABLE titles(
                title TEXT
            )
            CREATE TABLE reviews(
                review TEXT
            );
            """)

    with open(file_path, "w") as infile:
        for line, index in enumerate(infile, start=1):
            if index % 2:
                conn.execute(f"INSERT INTO reviews VALUES {line}")
            else:
                conn.execute(f"INSERT INTO title VALUES {line}")
                
        
    conn.commit()

    conn.close()
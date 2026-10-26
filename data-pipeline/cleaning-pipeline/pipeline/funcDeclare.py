import itertools as it
# import loctools as lt

#truncating the file into smaller sizes

def truncate_file_tooled(input_file: str, output_file: str, starting_line: int, ending_line: int):
    with open(input_file, 'r') as infile, open(output_file, 'w+') as outfile:
        
        for line_number, line in enumerate(infile, start=1):
            
            if starting_line <= line_number and line.strip():
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
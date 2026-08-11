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

#clearing out all the unneeded lines
def init_clean():
    with open('../raw-Data/Video_Games.txt', 'r') as f:
        for line in f:
            if 'profileName' in line or 'userId' in line or 'productId' in line:
                continue
            if 'review/time' in line:
                continue
            with open('txtData/preProc0.txt', 'a+') as f:
                f.writelines(line)

#removing the labels
def second_clean():
    with open('txtData/preProc0.txt', 'r') as f:
        for line in f:
            if ':' in line:
                line = line[line.index(':')+1:]
            with open('txtData/preProc1.txt', 'a+') as f:
                f.writelines(line)

#first reformat to turn into a csv
def third_clean():
    with open('txtData/preProc1.txt', 'r') as f:
        for line in f:
            if line.strip() == '':
                line = line.replace('\n', '\n')
            else:
                line = line.replace('\n', ',')
            with open('txtData/preProc2.txt', 'a+') as f:
                f.writelines(line)

#second reformat
def fourth_clean():
    with open('txtData/preProc2.txt', 'r') as f:
        for line in f:
            line_list = list(line)
            line_list.pop(-2)
            line = "".join(line_list)
            with open('txtData/preProc3.txt', 'a+') as f:
                f.writelines(line)

def get_sixth_comma_index(text):
    index = -1
    for _ in range(5):
        index = text.find(',', index + 1)
        if index == -1:
            return -1
    return index


#removing all the unneeded commas, now file is ready for csv
def fifth_clean():
    with open('txtData/preProc3.txt', 'r') as f:
        for line in f:
            new_line = line[get_sixth_comma_index(line):].replace(',', '')
            line = line[:get_sixth_comma_index(line)] + ',' + new_line
            with open('txtData/preProc4.txt', 'a+') as f:
                f.writelines(line)

#writing the cleaned data into the csv
def into_csv():
    with open('../cleanData/workingDataset.csv', 'a+') as f:
        f.writelines('pTitle, pPrice, rHelpfulness, rScore, rSummary, rText' + '\n')
    with open('txtData/preProc4.txt', 'r') as f:
        for line in f:
            with open('../cleanData/workingDataset.csv', 'a+') as f:
                f.writelines(line)
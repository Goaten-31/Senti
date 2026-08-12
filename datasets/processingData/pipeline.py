from funcDeclare import *
import os


if 'initCleaned.txt' not in os.listdir('../workingData/'):
    tooled_init_clean()

if 'initCleaned.txt' in os.listdir('../workingData/'):
    pass

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
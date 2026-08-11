from funcDeclare import *

stop_repeat = ['n', 'N', 'no', 'No', 'nO', 'NO']
valid_choice = stop_repeat + ['y', 'Y', 'yes', 'Yes', 'yEs', 'yeS', 'YEs', 'yES', 'YeS', 'YES']
choice_repeat = ''

while choice_repeat not in stop_repeat:
    try:
        starting_line = int(input("Enter the starting line: "))
    except ValueError:
        print('Please enter a number')
        starting_line = int(input("Enter the starting line: "))

    try:
        ending_line = int(input("Enter the ending line: "))
    except ValueError:
        print('Please enter a number')
        ending_line = int(input("Enter the ending line: "))

    name_of_file = input("Enter the name of the file: ")

    next_staring_line = truncate_file(starting_line, ending_line, name_of_file)
    print(f"The next starting line is: {next_staring_line}")
    choice_repeat = input("Do you want to truncate another file? (y/n): ")

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
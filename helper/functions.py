from print_color import print 

def get_valid_index_to_manupilate(array):
    index_selection = input("Please enter item index to select: ")
    while True:
        try:
            index = int(index_selection)
            if 0 <= index <= len(array):
                return index
            else:
                print("Input invalid", color = 'red')
                index_selection = input("please enter a valid option: ")
        except:
            print("Input invalid", color = 'red')
            index_selection = input("please enter a valid option: ")


def print_options(class_name):
    for item in class_name:
        print(f'{item.value} - {item.name}')


def delete_all_confirm():
    print("This action will clear all the data. Do you wish to proceed", color='red')
    while True:
        confirmation = input("please enter y/n: ")
        if confirmation.lower() == 'y':
            return True
        elif confirmation.lower() == 'n':
            return False
        else:
            print("input invalid", color='red')
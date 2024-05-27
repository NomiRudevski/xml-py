from enum import Enum
import xml.etree.ElementTree as ET
from print_color import print
from helper.functions import get_valid_index_to_manupilate, print_options, delete_all_confirm

animals = []
root = ''

class Actions(Enum):
    SHOW = 1
    ADD = 2
    UPDATE = 3
    DELETE = 4
    INFO = 5
    CLEARDATA = 6
    EXIT = 7


def load_data_from_xml():
    global root
    try:
        tree = ET.parse('data.xml')
        root = tree.getroot()
        return True
    except:
        return False
    

def set_up_data():
    if load_data_from_xml():
        global animals
        data = []
        for element in root:
            children_data = {}
            for child in element:
                children_data[child.tag] = child.text
            data.append(children_data)
        animals = data
    else: animals = []

def show_all_animals():
    print('____________________________________', color = 'cyan')
    for i, animal in enumerate(animals):
        print(f'{i+1} - {animal["specie"]} |{animal["name"]} | {animal["age"]}', color = 'cyan')
    print('____________________________________', color = 'cyan')

def add_new_animal():
    print("please enter new animal ditails:", color = 'yellow')
    animals.append({"specie" : input("specie: "), "name" : input("name: "), "age" : input("age: ")})
    print("Added succesfuly!", color = 'green')

def update_animal_data():
    if animals == []: return print("no available animals", color='red')
    show_all_animals()
    user_selection = get_valid_index_to_manupilate(animals) -1
    animals[user_selection] = {"specie" : input("specie: "), "name" : input("name: "), "age" : input("age: ")}
    print("Updated succesfuly!", color = 'green')

def delete_animal():
    if animals == []: return print("no available animals", color='red')
    show_all_animals()
    user_selection = get_valid_index_to_manupilate(animals) -1
    print("deleted succesfuly!", color='red')
    animals.pop(user_selection)

def info_how_many():
    print(f'There are {len(animals)} animals in the zoo!', color='yellow')

def clear_all_data():
    global animals
    if delete_all_confirm():
        animals = []
        print("All data cleared", color='red')
    else: print("Deleting was canseled", color='red')


def save_to_xml(data, filename):
    root = ET.Element("root")

    for entry in data:
        item_element = ET.Element("item")
        
        for key, value in entry.items():
            child_element = ET.SubElement(item_element, key)
            child_element.text = value

        root.append(item_element)

    tree = ET.ElementTree(root)
    tree.write(filename)


def close_program():
    save_to_xml(animals, 'data.xml')
    print("All chages have been saved!", color='magenta')
    exit()

if __name__ == "__main__":
    load_data_from_xml()
    set_up_data()
    while True:
        print_options(Actions)
        user_input = Actions(get_valid_index_to_manupilate(Actions))
        if user_input == Actions.SHOW: show_all_animals()
        if user_input == Actions.ADD: add_new_animal()
        if user_input == Actions.UPDATE: update_animal_data()
        if user_input == Actions.DELETE: delete_animal()
        if user_input == Actions.INFO: info_how_many()
        if user_input == Actions.CLEARDATA: clear_all_data()
        if user_input == Actions.EXIT: close_program()
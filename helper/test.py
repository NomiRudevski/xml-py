import xml.etree.ElementTree as ET

tree = ET.parse('data.xml')
root = tree.getroot()
animals = []


def get_all():
    global animals
    data = []
    for element in root:
        children_data = {}
        for child in element:
            children_data[child.tag] = child.text
        data.append(children_data)
    animals = data


get_all()
# animals = get_all()
print(animals)

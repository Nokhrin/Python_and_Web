"""
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.
"""


"""
проверка

Sample Input:

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Sample Output:

A : 3
B : 1
C : 2


######################
[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]

Ответ:

A : 5
B : 1
C : 4
D : 2
E : 1
F : 3
"""
import json

# json_input = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
json_input = '[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]'

json_data = json.loads(json_input)
# json_data = json.loads(input())
# print(json_data)


def count_children(element: str, data_scheme: dict, visited=None):
    """count occurrences in parents list"""
    if visited is None:
        visited = set()
    visited.add(element)
    for node in data_scheme[element] - visited:
        count_children(node, data_scheme, visited)
    return visited



# convert from json to dictionary
# initialize count dictionary
input_dict = {}
parent_children_dict = {}

for element in json_data:
    name = element['name']
    parents = element['parents']
    input_dict[name] = parents
    if name not in parent_children_dict.keys():
        parent_children_dict[name] = []

# convert child-parents dictionary to parent-children dictionary
for element in json_data:
    for child in parent_children_dict.keys():
        if child in element['parents']:
            parent_children_dict[child].append(element['name'])


# convert list to sets
for parent, children in parent_children_dict.items():
    parent_children_dict[parent] = set(children)

# count children of each object
children_count_dict = {}
for parent in parent_children_dict.keys():
    children_count_dict[parent] = len(count_children(parent, parent_children_dict))

# sort the dictionary
sorted_keys = [key for key in input_dict.keys()]
sorted_keys.sort()
children_count_dict_sorted = {key: children_count_dict[key] for key in sorted_keys}

for k, v in children_count_dict_sorted.items():
    print(f'{k} : {v}')

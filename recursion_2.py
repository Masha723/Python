"""
a function dict_travel() takes one argument - nested_dicts.

nested_dicts - a dictionary containing numbers, strings or dictionaries as values, which, in turn,
also contain numbers, strings or dictionaries as values; nesting could be arbitrary

The function should output all the key-value pairs of the nested dictionary, as well as the values
of all its sub-dictionaries. When displaying the values of sub-dictionaries, it lists the names of
all keys, starting from the top level, separating them with dots.

For example, in the dictionary:

{'name': 'Arthur', 'grades': {'math': 4, 'chemistry': 3}}

the value 4 should be output in the following format: grades.math: 4
"""


def dict_travel(nested_dicts,s=''):
    for k, v in sorted(nested_dicts.items()):
        if type(v) == dict:
            dict_travel(v, s + f'{k}.')
        else:
            print(f'{s}{k}: {v}')

#Test samples



data1 = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

dict_travel(data1)

data2 = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}

dict_travel(data2)

data3 = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}

dict_travel(data3)

data4 = {'firstname': 'Alyson', 'lastname': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}

dict_travel(data4)

data5 = {'firstname': 'Maria', 'lastname': 'Les', 'birthdate': {'day': 10, 'month': 'October', 'year': 1993},
        'address': {'streetaddress': '3484 Wisconsin ave, apt.432', 'city': {'region': 'Maryland',
        'type': 'city', 'cityname': 'Chevy Chase'}, 'zipcode': '20815'}}

dict_travel(data5)

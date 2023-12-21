"""
The function get_all_values() takes two arguments: nested_dicts and key.

nested_dicts - a dictionary containing arbitrary objects or dictionaries as values.
key - hashable object.

The function determines all the values that match the key in the nested_dicts dictionary
and in all its nested dictionaries, and return them as a set. If key is not in any dictionary,
the function must return an empty set.

"""
def get_all_values(nested_dicts,key):
    s=set()
    if key in nested_dicts:
        s.add(nested_dicts[key])
    for k, v in nested_dicts.items():
        if type(v) == dict:
            value = get_all_values(v, key)    
            if value is not None:
                s.update(value)
    return s
"""
Test samples
"""

my_dict = {'users': {'Mikle': {'grades': [4, 4, 3], 'top_grade': 4}, 'Sofia': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(*sorted(result))

my_dict = {'Mikle': {'hobby': 'hiking', 'drink': 'coffee'}, 'Sofia': {'hobby': 'drawing'}}
result = get_all_values(my_dict, 'hobby')

print(*sorted(result))

my_dict = {
           'Mikle': {'hobby': 'hiking', 'drink': 'coffee'}, 
           'Sofia': {'hobby': 'drawing'},
           'Antony': {
                   'hobby': 'CS',
                   'sister':
                       {
                         'name': 'Anna',
                         'hobby': 'TV',
                         'age': 14
                       }
                   }
           }

result = get_all_values(my_dict, 'hobby')
print(*sorted(result))

my_dict = {
           'Miklw': {'hobby': 'hiking', 'drink': 'coffee'}, 
           'Sofia': {'hobby': 'drawing'},
           'Antony': {
                   'hobby': 'CS',
                   'sister':
                       {
                         'name': 'Anna',
                         'hobby': 'TV',
                         'age': 14
                       }
                   }
           }

result = get_all_values(my_dict, 'age')
print(*result)

my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Mikle': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(*sorted(result))


my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'coffee'}, 'Mikle': {'hobby': 'basejumping'}}
result = get_all_values(my_dict, 'hobby')

print(*sorted(result))



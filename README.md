# python-dict2dot

Python Dictionary to **Dot notation**

Published on
[GitHub](https://github.com/nandoabreu/python-dict2dot) and 
[PyPi](https://pypi.org/project/python-dict2dot/).  

This implementation admits dot notation to access dictionaries **and nested dictionaries**. 

In order to expose a dot notated dict, its immediate parent will be changed to replace 
the dictionary to a new object, meaning that only the mutable types **dict** and **list** 
will be changed, once a dictionary child is found.


## Installation
To install through pip, run:
```shell
pip install dict2dot
```


## Basic usage

```python
from dict2dot import Dict2Dot

my_dict = {'dogs': {'breeds': ['Golden Retriever', 'Labrador Retriever']}}
my_d2d = Dict2Dot(my_dict)

print(my_d2d.dogs.breeds)
# ['Golden Retriever', 'Labrador Retriever']

print(my_d2d.dogs.breeds == my_dict['dogs']['breeds'])
# True

print(my_d2d.dogs.breeds[-1] == my_dict['dogs']['breeds'][-1])
# True
```


## Update and advanced operations

```python
from dict2dot import Dict2Dot

famous_dict = {'id': 6, 'names': {'first': 'Janelle', 'last': 'Monáe'}, 'pronouns': ['They', 'Them']}
famous_d2d = Dict2Dot(famous_dict)
famous_d2d.names.update({'full': 'Janelle Monáe Robinson'})
famous_d2d.pronouns.append('Their')
print(famous_d2d)
# {'id': 6, 'names': {'first': 'Janelle', 'last': 'Monáe', 'full': 'Janelle Monáe Robinson'}, 'pronouns': ['They', 'Them', 'Their']}

family_dict = {'elder': [{'child_1': [], 'child_2': [{'grandchild_2_1': []}, {'grandchild_2_2': []}]}]}
family = Dict2Dot(family_dict)
family.elder[0].child_1.extend(['has two dogs', 'has a bird'])
family.elder[0].child_2[-1].grandchild_2_2.append('has 1 dog')
print(family)
# {'elder': [{'child_1': ['has two dogs', 'has a bird'], 'child_2': [{'grandchild_2_1': []}, {'grandchild_2_2': ['has 1 dog']}]}]}

print(type(family))
# <class 'dict2dot.Dict2Dot'>

print(type(family.dict()))
# <class 'dict'>

other_dot2dict = Dict2Dot()
other_dot2dict.a_new_key = 'a new value'
print(other_dot2dict.a_new_key)
# a new value
```


## Autocomplete

Using Python Shell/REPL, autocomplete should respond. Assign a variable to a Dict2Dot dictionary 
instantiation and use the <tab> to autocomplete the dictionary keys after the dot:
```python
from dict2dot import Dict2Dot
d2d = Dict2Dot({'dogs': {'breeds': ['Golden Retriever']}})
d2d.dogs.bre  # hit the <tab> key to complete "breeds"
```

Note: autocomplete will not respond inside a list.
```python
from dict2dot import Dict2Dot
d2d = Dict2Dot({'name': {'first': 'First name'}, 'parents': [{'mom': "Mom's name"}, {'dad': "Dad's name"}]})
d2d.name.fir  # hitting <tab> autocompletes "first"
d2d.name.paren  # hitting <tab> autocompletes "parents"
d2d.parents[0].mom  # no autocomplete available
```


## Documentation

Please try from command line:
```shell
python -c "import dict2dot; print(dict2dot.__doc__)"
```

Documentation can also be found in [docs](docs).


## ToDo

- [ ] Read child dictionaries in parent iterators other than list or dict
- [ ] Remove keys and nested keys previously set
- [ ] Add recursing limitation option
- [ ] Add a tree exhibition of the keys
- [ ] Try to enable autocomplete for nested D2D in lists: `d2d.parents[0].mom`
- [ ] Update documentation (in the "docs" dir)

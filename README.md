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
```


## Update and advanced operations

```python
from dict2dot import Dict2Dot

famous_dict = {'id': 6, 'names': {'first': 'Janelle', 'last': 'Monáe'}, 'pronouns': ['They', 'Them']}
famous_d2d = Dict2Dot(famous_dict)
famous_d2d.names.update({'full': 'Janelle Monáe Robinson'})
famous_d2d.pronouns.append('Their')
# {'first': 'Janelle', 'last': 'Monáe', 'full': 'Janelle Monáe Robinson'}

family_dict = {'elder': [{'child_1': [], 'child_2': [{'grandchild_2_1': []}, {'grandchild_2_2': []}]}]}
family = Dict2Dot(family_dict)
#

other_dot2dict = Dict2Dot()
other_dot2dict.a_new_key = 'a new value'
print(other_dot2dict.dict())
# {'a_new_key': 'a new value'}
```


## Autocomplete

Using Python Shell/REPL, autocomplete should respond. Assign a variable to a Dict2Dot dictionary 
instantiation and use the <tab> to autocomplete the dictionary keys after the dot:
```shell
python
```
```python
from dict2dot import Dict2Dot
d2d = Dict2Dot({'dogs': {'breeds': ['Golden Retriever']}})
d2d.dogs.bre  # hit the <tab> key to complete "breeds"
```


## Documentation

Please try from python console:
```python
from dict2dot import Dict2Dot
help(Dict2Dot)
```

Or try from command line:
```shell
python -c "import dict2dot; print(dict2dot.__doc__)"
```

Documentation can also be found in [docs](docs).


## ToDo

- [ ] Add escape option, as vars() in SimpleNamespace
  - [ ] Could be `dict(Dict2Dot({'id': 6}))`
- [ ] Add recursing limitation option
- [ ] Expose parsed attributes to autocomplete (*)
- [ ] Remove elements from class
- [ ] Read and change child dictionaries in parent iterators other than list or dict
- [ ] Improve documentation

(*) Auto complete:
```python
from dict2dot import Dict2Dot
d = Dict2Dot({'id': 6, 'names': {'first': 'Janelle', 'last': 'Monáe'}, 'pronouns': ['They', 'Them']})
# d. (and tab twice)
dir(d)
```

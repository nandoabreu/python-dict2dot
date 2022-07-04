#! /usr/bin/env python3
from inspect import currentframe, getframeinfo
from sys import exit

import dict2dot

log = dict2dot.Logger().get_logger()


obj = None
log.debug(f'********** Test {obj}')
d2d = dict2dot.Dict2Dot(obj)
log.debug('*** repr: {}: {}'.format(type(repr(d2d)).__name__, repr(d2d)))
log.debug('*** str: {}: {}'.format(type(d2d).__name__, d2d))
log.debug('*** dict(): {}: {}'.format(type(d2d.dict()).__name__, d2d.dict()))

obj = {}
log.debug(f'********** Test {obj}')
d2d = dict2dot.Dict2Dot(obj)
# var.update({'name': 'variable'})

obj = {'description': 'Python Dictionary to Dot notation'}
log.debug(f'********** Test {obj}')
d2d = dict2dot.Dict2Dot(obj)
log.debug('*** repr: {}: {}'.format(type(repr(d2d)).__name__, repr(d2d)))
log.debug('*** str: {}: {}'.format(type(d2d).__name__, d2d))
log.debug('*** dict(): {}: {}'.format(type(d2d.dict()).__name__, d2d.dict()))
d2d.description == obj['description'] or log.error(f'!!!!!!!!!! Assertion error on {repr(d2d)} !!!!!!!!!!')

obj = {'pet': {'genus': 'Canis', 'name': 'Bono', 'breed': 'Golden Retriever'}}
log.debug(f'********** Test {obj}')
d2d = dict2dot.Dict2Dot(obj)
log.debug('*** repr: {}: {}'.format(type(repr(d2d)).__name__, repr(d2d)))
log.debug('*** str: {}: {}'.format(type(d2d).__name__, d2d))
log.debug('*** dict(): {}: {}'.format(type(d2d.dict()).__name__, d2d.dict()))
isinstance(d2d.pet, dict2dot.Dict2Dot) or log.error(f'!!!!!!!!!! Assertion error on {repr(d2d)} !!!!!!!!!!')
d2d.pet.breed == obj['pet']['breed'] or log.error(f'!!!!!!!!!! Assertion error on {repr(d2d)} !!!!!!!!!!')

obj = {'dogs': {'breeds': ['Golden Retriever', 'Labrador Retriever']}, 'cats': {'breeds': ['Bombay']}}
log.debug(f'********** Test {obj}')
d2d = dict2dot.Dict2Dot(obj)

obj = {
    'name': {'first': 'First name', 'last': 'Family name'},
    'parents': [{'mom': 'Mother\' name'}, {'dad': 'Father\' name'}]
}
log.debug(f'********** Test {obj}')
d2d = dict2dot.Dict2Dot(obj)

# log.debug(my_d2d.dogs.breeds)
# ['Golden Retriever', 'Labrador Retriever']

# log.debug(my_d2d.dogs.breeds == my_dict['dogs']['breeds'])
# exit()


log.debug(f'********** Test updates from None')
d2d = dict2dot.Dict2Dot()
# var.update({'name': 'variable'})

log.debug(f'********** Test updates on nested dict and list')
obj = {'id': 6, 'names': {'first': 'Janelle', 'last': 'Monáe'}, 'pronouns': ['They', 'Them']}
d2d = dict2dot.Dict2Dot(obj)
# d2d.names.update({'full': 'Janelle Monáe Robinson'})
# d2d.pronouns.append('Their')
# assert d2d.names.first == 'Janelle'
# assert d2d.pronouns[-1] == 'Their'

log.debug(f'********** Test updates on deep nested objects')
obj = {'pets': [{'species': 'Canis familiaris', 'names': [{'Bono': {'age': 6}}, {'Gaia': {'age': 5}}]}]}
d2d = dict2dot.Dict2Dot(obj)
# family.elder[0].append({'grandchild_1_1': {}})

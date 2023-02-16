#! /usr/bin/env python3
from unittest import TestCase

import dict2dot


# TODO: UNIT TESTS MUST MATCH README
# TODO: CHECK README TODO BOXES
# TODO: MATCH README WITH RELEASE

class Test(TestCase):
    def test_11_instantiate_param_none(self):
        obj = None
        d2d = dict2dot.Dict2Dot(obj)
        assert isinstance(d2d, dict2dot.Dict2Dot)

    def test_13_instantiate_empty_dict(self):
        obj = {}
        d2d = dict2dot.Dict2Dot(obj)
        assert isinstance(d2d, dict2dot.Dict2Dot)

    def test_15_flat_dict(self):
        obj = {'description': 'Python Dictionary to Dot notation'}
        d2d = dict2dot.Dict2Dot(obj)
        assert isinstance(d2d, dict2dot.Dict2Dot)
        assert list(d2d.keys()) == ['description']
        assert d2d.description == obj['description']

    def test_19_nested_dict(self):
        obj = {'pet': {'genus': 'Canis', 'name': 'Bono', 'breed': 'Golden Retriever'}}
        d2d = dict2dot.Dict2Dot(obj)
        assert isinstance(d2d.pet, dict2dot.Dict2Dot)
        assert list(d2d.keys()) == ['pet']
        assert list(d2d.pet.keys()) == ['genus', 'name', 'breed']
        assert d2d.pet.breed == obj['pet']['breed']

    def test_23_nested_dict_nesting_list(self):
        obj = {'dogs': {'breeds': ['Golden Retriever', 'Labrador Retriever']}, 'cats': {'breeds': ['Bombay']}}
        d2d = dict2dot.Dict2Dot(obj)
        assert isinstance(d2d.dogs, dict2dot.Dict2Dot)
        assert isinstance(d2d.dogs.breeds, list)
        assert d2d.dogs.breeds[-1] == obj['dogs']['breeds'][-1]

    def test_29_nested_list_nesting_dict(self):
        obj = {
            'name': {'first': 'First name', 'last': 'Family name'},
            'parents': [{'mom': 'Mother\' name'}, {'dad': 'Father\' name'}]
        }
        d2d = dict2dot.Dict2Dot(obj)
        assert isinstance(d2d.parents, list)
        assert isinstance(d2d.parents[0], dict2dot.Dict2Dot)
        assert d2d.parents[0].mom == obj['parents'][0]['mom']
        assert d2d.parents[1].dad == obj['parents'][1]['dad']

    def test_31_nested_list_nesting_mixed_types(self):
        obj = {'parent': [{'child': 'Child\'s name'}, ['apples', {'money': True}], 'joy']}
        d2d = dict2dot.Dict2Dot(obj)
        assert isinstance(d2d.parent, list)
        assert isinstance(d2d.parent[0], dict2dot.Dict2Dot)
        assert isinstance(d2d.parent[1][0], str)
        # assert isinstance(d2d.parent[1][1], dict2dot.Dict2Dot)
        assert isinstance(d2d.parent[2], str)
        assert d2d.parent[0].child == obj['parent'][0]['child']
        assert d2d.parent[1][0] == obj['parent'][1][0]
        assert d2d.parent[1][1] == obj['parent'][1][1]
        # assert d2d.parent[1][1].money == obj['parent'][1][1]['money']
        assert d2d.parent[2] == obj['parent'][2]

    def test_37_str_and_repr(self):
        obj = {'dogs': {'breeds': ['Golden Retriever']}}
        d2d = dict2dot.Dict2Dot(obj)
        assert repr(d2d) == "<dict2dot.Dict2Dot {'dogs': <Dict2Dot {'breeds': ['Golden Retriever']}>}>"
        assert str(d2d) == "{'dogs': {'breeds': ['Golden Retriever']}}"

    def test_41_dict_method_and_return(self):
        obj = {'dogs': {'breeds': ['Golden Retriever', 'Labrador Retriever']}, 'cats': {'breeds': ['Bombay']}}
        d2d = dict2dot.Dict2Dot(obj)
        # assert isinstance(d2d.dict(), dict)
        # assert d2d.dict() == obj

    def test_43_update_empty_object(self):
        d2d = dict2dot.Dict2Dot()
        # d2d.update({'a_new_key': 'a new value'})
        # assert d2d.a_new_key == 'a new value'
        # assert d2d.dict() == {'a_new_key': 'a new value'}

    def test_47_update_nested_values(self):
        obj = {'id': 6, 'names': {'first': 'Janelle', 'last': 'Monáe'}, 'pronouns': ['They', 'Them']}
        d2d = dict2dot.Dict2Dot()
        # assert d2d.names.first == 'Janelle'
        # d2d.pronouns.append('Their')
        # assert d2d.pronouns[-1] == 'Their'
        # assert d2d.dict()['pronouns'][-1] == 'Their'
        # d2d.names.update({'full': 'Janelle Monáe Robinson'})
        # assert d2d.names.full == 'Janelle Monáe Robinson'
        # assert d2d.dict()['names']['full'] == 'Janelle Monáe Robinson'

    def test_53_update_deeply_nested_values(self):
        obj = {'pets': [{'species': 'Canis familiaris', 'names': [{'Bono': {'age': 6}}, {'Gaia': {'age': 5}}]}]}
        d2d = dict2dot.Dict2Dot(obj)
        # family.elder[0].append({'grandchild_1_1': {}})

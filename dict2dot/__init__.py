#! /usr/bin/env python3
"""
Python Dictionary to Dot notation (class) package

This implementation admits dot notation to access dictionaries **and nested dictionaries**.


Basic usage:

    python

    from dict2dot import Dict2Dot
    obj = {'pet': {'genus': 'Canis', 'name': 'Bono', 'breed': 'Golden Retriever'}}
    d2d = Dict2Dot(obj)
    print(d2d.pet.breed)
"""
from json import loads

from .Logger import Logger


class Dict2Dot(dict):
    def __init__(self, obj: dict = None, depth: int = 0, debug: bool = False):  # todo: debug defaults to False
        self._log = Logger(log_level='DEBUG' if debug else 'WARNING').get_logger()
        self._depth = depth

        self._id = int(str(id(self))[-3:])
        self._log.debug('{}{} depth {}, id {} for {}: {}'.format(
            "  " * depth, self.__class__.__name__, depth, self._id, type(obj).__name__.upper(), obj
        ))

        clone = obj.copy() if isinstance(obj, dict) else {}
        super().__init__(clone)

        self._log.debug(f'{"  " * depth}Request object set')
        self._set(clone, depth)

    def __getattr__(self, key):
        return self[key]

    def _set(self, obj, depth: int = 0):
        self._log.debug(f'{"  " * depth}Start {type(obj).__name__.upper()} object parse')
        self._log.debug(f'{"  " * depth}Start LOOP over keys {obj.keys()}')

        for key, value in obj.items():
            self._log.debug(f'{"  " * depth}Start SET key {key}')
            msg = '{}{} has {} as value type -- '.format("  " * depth, key, type(value).__name__.upper())

            if isinstance(value, dict):
                msg += 'RECURSE'
                self._log.debug(msg)
                self[key] = Dict2Dot(value, depth + 1)
                super().__setattr__(key, self[key])
                continue

            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if isinstance(item, dict):
                        value[i] = Dict2Dot(item, depth + 1)
                        # TODO: Try to autocomplete nested in lists (i.e.: "mom" `d2d.parents[0].mom`)

            msg += 'SET {} as {} in instance {}'.format(key, value, self._id)
            self._log.debug(msg)
            self[key] = value
            super().__setattr__(key, self[key])
            self._log.debug(f'{"  " * depth}Ended key {key} set')

        self._log.debug(f'{"  " * depth}Ended object {type(obj).__name__.upper()} parse')

    def dict(self) -> dict:
        return loads(str(self).replace("'", '"'))

    def tree(self, sort: bool = True) -> None:
        print('[TBI Warning] The "tree" method is to be implemented')

    def __str__(self) -> str:
        res = super().__repr__()
        return res\
            .replace(f'<{self.__class__.__name__} ', '')\
            .replace('}>', '}')

    def __repr__(self) -> str:
        name = '{}.{}'.format(self.__module__, self.__class__.__name__) if not self._depth else self.__class__.__name__
        return '<{} {}>'.format(name, super().__repr__())

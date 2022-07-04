#! /usr/bin/env python3
"""
Python Dictionary to Dot notation (class) package

This implementation admits dot notation to access dictionaries **and nested dictionaries**.


Basic usage:
    from dict2dot import Dict2Dot

    obj = {'pet': {'genus': 'Canis', 'name': 'Bono', 'breed': 'Golden Retriever'}}
    d2d = dict2dot.Dict2Dot(obj)
    print(d2d.pet.breed)
"""
from json import loads

from .Logger import Logger


class Dict2Dot(dict):
    """
    Dict2Dot class: "the main class"

    Arguments:
        (dictionary, optional): A pre-existent dictionary may be passed
    """
    def __init__(self, obj: (dict, list) = None, depth: int = 0, debug: bool = True):  # todo: debug defaults to False
        self.log = Logger(log_level='DEBUG' if debug else 'WARNING').get_logger()

        _id = int(str(id(self))[-3:])
        self.log.debug('{}{} depth {}, id {} for {}: {}'.format(
            "  " * depth, self.__class__.__name__, depth, _id, type(obj).__name__.upper(), obj
        ))

        clone = obj
        if isinstance(obj, (dict, list)):
            clone = obj.copy()
            if isinstance(clone, dict):
                super().__init__(clone.copy())

        self.log.debug(f'{"  " * depth}Request object set')
        self._set(clone, depth)

    def __getattr__(self, key):
        return self[key]

    def _set(self, obj, depth: int = 0):
        self.log.debug(f'{"  " * depth}Start {type(obj).__name__.upper()} object parse')

        # keys = list(obj.keys()) if isinstance(obj, dict) else range(len(obj)) if isinstance(obj, list) else []
        keys = obj.items() if isinstance(obj, dict) else enumerate(obj) if isinstance(obj, list) else None

        if not keys:
            self.log.debug(f'{"  " * depth}Object has NO keys: MAY need set')

        else:
            self.log.debug(f'{"  " * depth}Start LOOP over keys {keys}')

            for key, value in keys:
                self.log.debug(f'{"  " * depth}Start SET key {key}')
                msg = '{}{} has {} as value type'.format("  " * depth, key, type(value).__name__.upper())
                # todo: JUST GOT A MOUSE FREEZE WITH THE MAIN LOGIC SELECTED
                # todo: AFTER REBOOTING THE IDE, LOGIC WAS GONE
                # todo: NEED TO CREATE IT AGAIN

                self.log.debug(f'{"  " * depth}Ended key {key} set')

        self.log.debug(f'{"  " * depth}Ended object {type(obj).__name__.upper()} parse')

    def dict(self) -> dict:
        return loads('{}'.format(super().__repr__().replace("'", '"')))

    def tree(self, sort: bool = True) -> None:
        # pairs = list(super().items())
        # if sort:
        #     pairs.sort()
        #
        # for key, value in pairs:
        #     print(f'# chack instance of {key}: {type(value)}')
        #     if isinstance(value, Dict2Dot):
        #         print(key)
        #         value.tree()
        #     else:
        #         print('{}: {!r} ({})'.format(key, value, type(value).__name__))
        pass

    def __str__(self) -> str:
        return super().__repr__()

    def __repr__(self) -> str:
        return '<{}.{} {}>'.format(self.__module__, self.__class__.__name__, super().__repr__())

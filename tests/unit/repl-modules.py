#! /usr/bin/env python
from sys import modules as imported_modules
from importlib import import_module, reload
from datetime import datetime as dt


project_modules = {
    'dict2dot': {'object': None, 'classes': ('Dict2Dot',)},
}

if not any([m in project_modules for m in imported_modules]):
    for mod_name in project_modules:
        exec(f'{mod_name} = import_module("{mod_name}")')
        exec(f'project_modules[mod_name]["object"] = {mod_name}')


def reload_module():
    for mod_name in project_modules:
        reload(project_modules[mod_name]["object"])

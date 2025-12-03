import os
from help_pkg.config import *
from help_pkg.handlers import *
from typing import Any, AnyStr, List, Dict, Tuple, Union, Optional, Callable
from importlib import reload as rel
from rich.pretty import pprint
from os import chdir, getcwd, system, remove, mkdir, listdir


@os_exceptions
class Helper:

    def __init__(self, *args: List[str], path: str = None):
        self.path = path
        self.mkf = lambda file: open(file, 'w').close()
        self.names = [arg for arg in args if isinstance(arg, str) and arg not in os.listdir()]
        if self.names:
            list(map(self.mkf, self.names))

    def _folder(self, path: str):
        mkdir(path)
        pprint(f'create -- [directory]: {path}')
        
    def _dir(self):
        pprint(f'current-directory: {getcwd()}')

    def _list(self):
        pprint(f'directory files-list: {listdir()}')

    def redir(self, new_path: str):
        chdir(new_path)
        pprint(f'redirected -- [path]: {new_path}')

    def _start(self, command: str):
        system(command)

    def _del(self, path: str):
        remove(path)
        pprint(f'deleted -- [file]: {path}')
        
    @property
    def back(self) -> str:
        self.path = PATH
        return self.path
        
    def __repr__(self) -> str:
        return (f'Helper: {STRINGS["info"]}\n'
            f'help-reference: {STRINGS["help_msg"]}\n'
            f'actual method-list: {[key for key in __class__.__dict__.keys() if not key.startswith("__")]}')
        

       


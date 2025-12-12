from modules import *
from mixins import rt
from custom_types import Any, AnyList, DictList, StrList, Content, Union, Callable


class ContentType(BaseModel):
    content: Content

class StandardType(BaseModel):
    any_list: AnyList

class TypeCheсker(BaseModel):
    string_list: StrList
    dict_list: DictList


    
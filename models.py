from rich_tabler.modules import BaseModel # type: ignore
from rich_tabler.custom_types import AnyList, DictList, StrList, Content # type: ignore


class ContentType(BaseModel): # type: ignore
    content: Content

class StandardType(BaseModel): # type: ignore
    any_list: AnyList

class TypeChecker(BaseModel): # type: ignore
    string_list: StrList
    dict_list: DictList


    
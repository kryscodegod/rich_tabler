from rich_tabler.models import * # type: ignore
from loguru import logger
from functools import wraps
from typing import Union, Callable

logger.remove()

logger.add( 
    RichHandler(rich_tracebacks=True, markup=True), # type: ignore
    format = '{message}',
    level='INFO'
    )


stringify = lambda _list: list(map(str, _list))

get_valid_attrs = lambda kwr: {key: value for key, value in kwr.items() if hasattr(Table(), key)} # type: ignore

def checked(func: Callable):

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
           logger.info(f"'run': {True}, 'file': {__name__}")
           console.print(Panel(f'[blue] execute-function: [red]{func.__name__}')) # type: ignore
           
           return func(*args, **kwargs)
        
        except ValidationError: # type: ignore
           pass
        except Exception as error_message:
           logger.error(f'[red]WARNING! [green]{error_message}')

    return wrapper

@checked
def check_type(strings: StrList, records: DictList) -> TypeCheсker | None: # type: ignore
    return TypeCheсker(string_list=strings, dict_list=records) # type: ignore
    
@checked
def check_other_types(strings: AnyList, contents: Content) -> Union[StandardType, ContentType] | None: # type: ignore
    return StandardType(any_list=strings) and ContentType(content=contents) # type: ignore
        

def content_handler(
        names: StrList, # type: ignore
        table: Table, # type: ignore
        container: Container, # type: ignore
        color: str | None = None,
            ) -> None:
    
    if check_type(names, container):
        for name in names:
            table.add_column(name, style=color)

        for item in container:
            table.add_row(*[str(item[i]) for i in names]) # type: ignore

    elif check_other_types(names, container):
        for name in names:
            table.add_column(name, style=color)
            
        for item in container:
            table.add_row(*stringify(item))

    else:
        console.print(rt.warn) # type: ignore



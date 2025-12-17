from rich_tabler.modules import console # type: ignore
from rich_tabler.main import rt, TableMaker # type: ignore
from rich_tabler.custom_types import StrList, DictList # type: ignore


class ExampleTableDemo(TableMaker):
    def __init__(
            self,
            names: StrList,
            container: DictList | None = None,
            title: str | None = None,
            color: str | None = None,
            ):
        super().__init__(names, container=container, title=title, color=color)

    def __call__(self, mod='default'):
        if mod == 'default':
           console.print(self.get_table, justify='center')
        else:
            rt()
    
    def __str__(self) -> str:
        return rt.info
    
def demo() -> None:
    names = ['id', 'name', 'status']
    content = [{'id': 1, 'name': 'Kristy', 'status': 'author'}]
    ext  = ExampleTableDemo(names, content, title='[magenta]author', color='cyan')
    console.log(ext)
    ext(mod='none')
    console.rule('[bold magenta]example-table')
    ext()
    
if __name__ == '__main__':
    demo()

    
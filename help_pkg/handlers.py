import os

def os_cls_wrapper(method):
    def overload(self, *args, **kwargs):
        try:
            method(self, *args, **kwargs)
        except os.error as err:
            print(f'OS-Error exception <char: {err}>')
    return overload

        
def os_exceptions(cls):
    for key in cls.__dict__.keys():
        if key in ['_folder', 'redir', '_start', '_del']:
            attr = getattr(cls, key)
            setattr(cls, key, os_cls_wrapper(attr))
    return cls



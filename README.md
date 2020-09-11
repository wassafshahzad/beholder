# Description:
A python dectorater to enforce type checks on your python functions for your stupid colleagues who pass int type when you clearly told them to pass string.
ヽ(ಠ_ಠ)ノ

You can define parameter and return types for your python functions using type hints (check them out here : https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) and the watcher decorator over them to handle the dirty work.

Currently we only support positional arguments only and single return types but will add support for keyword arguments and mutiple return types.

Raise and issue in the gitrepo if you find any bugs or need a feature.

## Pypi Link:
The package can be found on
> https://pypi.org/project/design-patterns-WS/1.0.0/


## Types Checking Supported for
> Positional Parameters

> Single return types

> User defined data types

# Example

```python

from beholder import watcher


@watcher
def f():  # Will work as normal
    return "pass"

@watcher
def f1(a:str,b): #Will be typed checked and will raise TypeError if types do not match
    return "pass"
@watcher
def f2(a:str,b:int):
    return "pass":

@watcher
def f3()>str: #Will raise a type error due to return type not matching function definition
    return 1

@watcher    
def f4(a:str)->str:
    return "pass"

if __name__ == "__main__":
    f4(1)
    f2("s",1)
    f2(1,1)
  
```



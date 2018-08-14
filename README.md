# CLPB
Command Line Progress Bar for Python 3.x

## Installation
```
pip install clpb
```

## Examples
```
>>> from clpb import ProgressBar
>>> items_length = 69
>>> pb = ProgressBar(0, items_length)
>>> pb.initial_print()
...     pb.current_print(i+1)
Progress |████████████████████████████████████████| 100.0% Complete
```
```
>>> from clpb import ProgressBar
>>> items_length = 69
>>> pb = ProgressBar(0, items_length, fill='#')
>>> pb.initial_print()
...     pb.current_print(i+1)
Progress |########################################| 100.0% Complete
```

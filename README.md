# Pysharper
All in one python resharper, used to fix code smells and increase your code's speed. This is still being developed on currently.

## Software Architecture Used
Pysharper uses n-tier architecture and multiple different patterns including domain driven design (DDD).

## Features
Pysharper's features range from changing dictionaries to classes, convert lists to tuples if the object has never been appended to. Pysharper also helps save less RAM and fix errors that IDEs do not pick up on.

## CLI Entrypoint
```bash

python pysharper.py --file examples/inputs/codesmell_one.py --output examples/outputs/codefix_one.py

```

```
usage: pysharper.py [-h] [-f <file>] [-o [<file>]]

options:
  -h, --help            show this help message and exit
  -f <file>, --file <file>
                        target file to run pysharper on
  -o [<file>], --output [<file>]
                        output file to put the finished refactored code
```

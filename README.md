# Autoconfp

Snippet that lets Pythons `configparser` auto-guess types in a specified order.

## Usage:

```
from acp import AutoConfigParser

conf = AutoConfigParser()
conf.read_string("[mysection]\n"
                 "firstoption=yes\n"
                 "secondoption=3.0\n"
                 "thirdoption=18")

for option in conf.options('mysection'):
    parsed_val = conf.get('mysection', option)
    print("%s: %s (%s)" % (option, parsed_val, type(parsed_val)))
```

Result:

```
firstoption: True (<class 'bool'>)
secondoption: 3.0 (<class 'float'>)
thirdoption: 18 (<class 'int'>)
```

The default guess order is `int`, `float`, `boolean`, `str`, you can change it
by setting `conf.try_order`

```
conf.try_order = (str,)
for option in conf.options('mysection'):
    parsed_val = conf.get('mysection', option)
    print("%s: %s (%s)" % (option, parsed_val, type(parsed_val)))
```

```
firstoption: yes (<class 'str'>)
secondoption: 3.0 (<class 'str'>)
thirdoption: 18 (<class 'str'>)
```

That's all.

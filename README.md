# What's this

Pipe-like built-in functions.

# Usage

```python
from bpipe2 import *
data = [1, 2, 3, 4]
sum_ = data | Sum()
prod = data | Reduce(lambda x, y: x*y)
print(sum_, prod, data | Len())
```
# Note

- This version does not override builtins but you have use `Map()` insteaf of `map()` (for example). [bpipe](https://github.com/mavnt/bpipe/) overrides builtins but it's less safe.
- You can use both `>>` and `|`

# Credits

Inspired by [Pipe](https://github.com/JulienPalard/Pipe).
from functools import reduce


class bpipe2(object):
    def __init__(
        self,
        function_,
        filter_map_lambda_reduce=None,
        enumerate_start=None,
        eval_args=None,
        int_base=None,
        zip_other=None,
    ):
        self.function_ = function_
        self.filter_map_lambda_reduce = filter_map_lambda_reduce
        self.enumerate_start = enumerate_start
        self.eval_args = eval_args
        self.int_base = int_base
        self.zip_other = zip_other

    def __ror__(self, other):
        if self.filter_map_lambda_reduce is not None:
            return self.function_(self.filter_map_lambda_reduce, other)
        if self.enumerate_start is not None:
            return self.function_(other, self.enumerate_start)
        if self.eval_args is not None:
            return self.function_(other, *self.eval_args)
        if self.int_base is not None:
            return self.function_(other, self.int_base)
        if self.zip_other is not None:
            return self.function_(other, self.zip_other)
        return self.function_(other)

    def __rrshift__(self, other):
        return self.__ror__(other)


def Abs():
    return bpipe2(abs)


assert abs(-3) == -3 | Abs()


def All():
    return bpipe2(all)


assert all([True, True, False]) == [True, True, False] | All()
assert all([True, True, False]) == [True, True, False] >> All()


def Any():
    return bpipe2(any)


assert any([True, True, False]) == [True, True, False] | Any()
assert any([True, True, False]) == [True, True, False] >> Any()


def Ascii():
    return bpipe2(ascii)


assert ascii("hello") == "hello" | Ascii()
assert ascii("hello") == "hello" >> Ascii()


def Bin():
    return bpipe2(bin)


assert bin(2) == 2 | Bin()
assert bin(2) == 2 >> Bin()


def Bool():
    return bpipe2(bool)


assert bool(1) == 1 | Bool()
assert bool(1) == 1 >> Bool()


# breakpoint - skipped
# bytearray - skipped
# bytes - skipped


def Callable():
    return bpipe2(callable)


assert callable(Callable) == Callable | Callable()
assert callable(Callable) == Callable >> Callable()


def Chr():
    return bpipe2(chr)


assert chr(10) == 10 | Chr()
assert chr(10) == 10 >> Chr()


# classmethod - skipped
# compile - skipped
# complex - skipped
# delattr - skipped
# dir - skipped
# divmod - skipped


def Enumerate(start=0):
    return bpipe2(enumerate, enumerate_start=start)


assert list(enumerate(range(100))) == list(range(100) | Enumerate())
assert list(enumerate(range(100), start=3)) == list(range(100) | Enumerate(start=3))
assert list(enumerate(range(100))) == list(range(100) >> Enumerate())
assert list(enumerate(range(100), start=3)) == list(range(100) >> Enumerate(start=3))


def Eval():
    return bpipe2(eval)


assert 4 == eval("2+2") == "2+2" | Eval()
assert 4 == eval("2+2") == "2+2" >> Eval()


# exec - skipped


def Filter(f: callable):
    return bpipe2(filter, filter_map_lambda_reduce=f)


assert list(filter(lambda x: x % 2 == 0, range(100))) == list(
    range(100) | Filter(lambda x: x % 2 == 0)
)


def Float():
    return bpipe2(float)


assert float(3) == 3 | Float()


# format - skipped


def Frozenset():
    return bpipe2(frozenset)


assert frozenset(range(100)) == range(100) | Frozenset()


# getattr - skipped
# globals - skipped
# hasattr - skipped


def Hash():
    return bpipe2(hash)


assert hash(1) == 1 | Hash()


def Hex():
    return bpipe2(hex)


assert hex(1) == 1 | Hex()


def Id():
    return bpipe2(id)


assert id(hex) == hex | Id()


# input - skipped


def Int(base=None):
    if base is None:
        return bpipe2(int)
    else:
        return bpipe2(int, int_base=base)


assert int("3") == "3" | Int()
assert int("10", base=2) == "10" | Int(base=2) == 2
assert int(3) == 3 | Int()


# isinstance - skipped
# issubclass - skipped
# iter - skipped


def Len():
    return bpipe2(len)


assert len(list(range(100))) == list(range(100)) | Len()


def List():
    return bpipe2(list)


# locals - skipped


def Map(f):
    return bpipe2(map, filter_map_lambda_reduce=f)


assert list(map(lambda x: x % 2 == 0, range(100))) == list(
    range(100) | Map(lambda x: x % 2 == 0)
)


def Max():
    return bpipe2(max)


# memoryview - skipped


def Min():
    return bpipe2(min)


_a = [1, 2, 3, 4, 5]
assert max(_a) == _a | Max() == 5
assert min(_a) == _a | Min() == 1


# next - skipped
# object - skipped


def Oct():
    return bpipe2(oct)


assert oct(3) == 3 | Oct()


# object - skipped
# open - skipped


def Ord():
    return bpipe2(ord)


assert ord("c") == "c" | Ord()


# pow - skipped
# print - skipped
# property - skipped
# range - skipped
# repr - skipped


def Reversed():
    return bpipe2(reversed)


assert list(reversed(_a)) == _a | Reversed() | List()
assert list(reversed(_a)) == _a >> Reversed() >> List()


# round - skipped


def Set():
    return bpipe2(set)


# setattr - skipped
# slice - skipped


def Sorted():
    return bpipe2(sorted)


# staticmethod - skipped


def Str():
    return bpipe2(str)


def Sum():
    return bpipe2(sum)


# super - skipped


def Tuple():
    return bpipe2(tuple)


def Type():
    return bpipe2(type)


# vars - skipped


def Zip(b):
    return bpipe2(zip, zip_other=b)


_a, _b = [1, 2], [11, 22]
assert list(zip(_a, _b)) == _a | Zip(_b) | List()
assert list(zip(_a, _b)) == _a >> Zip(_b) >> List()


# __import__ - skipped


# extra
def Reduce(f: callable):
    return bpipe2(reduce, filter_map_lambda_reduce=f)


assert (
    reduce(lambda x, y: x + y, [1, 2, 3])
    == 6
    == [1, 2, 3] >> Reduce(lambda x, y: x + y)
)


def main():
    pass


if __name__ == "__main__":
    main()

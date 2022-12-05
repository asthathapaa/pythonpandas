Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
10/2
5.0
10//2
5
5/2
2.5
7/2
3.5
8/5
1.6
11/2
5.5
11//2
5
12/2
6.0
12//2
6
13/8
1.625
13//8
1
9/2
4.5
9//2
4
4*2
8
4**2
16
5*2
10
5**2
25
1*2
2
1**2
1
name="python programming"

type(name)
<class 'str'>
dir(name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
name.count
<built-in method count of str object at 0x0000021CB5BE8260>
name.count()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    name.count()
TypeError: count() takes at least 1 argument (0 given)
name.count(p)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    name.count(p)
NameError: name 'p' is not defined
name.count(1)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    name.count(1)
TypeError: must be str, not int
name.count("p")
2
name.count("o")
2
name.count(" ")
1
name.count("P")
0
NAME.COUNT("p")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    NAME.COUNT("p")
NameError: name 'NAME' is not defined
name.count("i")
1
name.count("0")
0
name.count("z")
0
name.count("@")
0
name.count("OP")
0
name.count("pro")
1
name.count("L")
0
name.count("program")
1
dir(name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
name.upper
<built-in method upper of str object at 0x0000021CB5BE8260>
help(name.upper)
Help on built-in function upper:

upper() method of builtins.str instance
    Return a copy of the string converted to uppercase.

help(name.count)
Help on built-in function count:

count(...) method of builtins.str instance
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.

name.upper()
'PYTHON PROGRAMMING'
help(name.lower)
Help on built-in function lower:

lower() method of builtins.str instance
    Return a copy of the string converted to lowercase.

name.lower()
'python programming'
help(name.split)
Help on built-in function split:

split(sep=None, maxsplit=-1) method of builtins.str instance
    Return a list of the substrings in the string, using sep as the separator string.
    
      sep
        The separator used to split the string.
    
        When set to None (the default value), will split on any whitespace
        character (including \\n \\r \\t \\f and spaces) and will discard
        empty strings from the result.
      maxsplit
        Maximum number of splits (starting from the left).
        -1 (the default value) means no limit.
    
    Note, str.split() is mainly useful for data that has been intentionally
    delimited.  With natural text that includes punctuation, consider using
    the regular expression module.

help(name.title)
Help on built-in function title:

title() method of builtins.str instance
    Return a version of the string where each word is titlecased.
    
    More specifically, words start with uppercased characters and all remaining
    cased characters have lower case.

name.title(p)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    name.title(p)
NameError: name 'p' is not defined
help(name.casefold)
Help on built-in function casefold:

casefold() method of builtins.str instance
    Return a version of the string suitable for caseless comparisons.

name.casefold()
'python programming'
age=18
dir
<built-in function dir>
type(age)
<class 'int'>
dir(age)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
name.count(1)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    name.count(1)
TypeError: must be str, not int
help(name.count)
Help on built-in function count:

count(...) method of builtins.str instance
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.

name.count("1")
0
name.count("18")
0
help(age.imag)
Help on int object:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |  
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |  
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |  
 |  Built-in subclasses:
 |      bool
 |  
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __bool__(self, /)
 |      True if self else False
 |  
 |  __ceil__(...)
 |      Ceiling of an Integral returns itself.
 |  
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __float__(self, /)
 |      float(self)
 |  
 |  __floor__(...)
 |      Flooring an Integral returns itself.
 |  
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |  
 |  __format__(self, format_spec, /)
 |      Default object formatter.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |  
 |  __int__(self, /)
 |      int(self)
 |  
 |  __invert__(self, /)
 |      ~self
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __neg__(self, /)
 |      -self
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __pos__(self, /)
 |      +self
 |  
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __round__(...)
 |      Rounding an Integral returns itself.
 |      
 |      Rounding with an ndigits argument also returns an integer.
 |  
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |  
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(self, /)
 |      Returns size in memory, in bytes.
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __truediv__(self, value, /)
 |      Return self/value.
 |  
 |  __trunc__(...)
 |      Truncating an Integral returns itself.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  as_integer_ratio(self, /)
 |      Return integer ratio.
 |      
 |      Return a pair of integers, whose ratio is exactly equal to the original int
 |      and with a positive denominator.
 |      
 |      >>> (10).as_integer_ratio()
 |      (10, 1)
 |      >>> (-10).as_integer_ratio()
 |      (-10, 1)
 |      >>> (0).as_integer_ratio()
 |      (0, 1)
 |  
 |  bit_count(self, /)
 |      Number of ones in the binary representation of the absolute value of self.
 |      
 |      Also known as the population count.
 |      
 |      >>> bin(13)
 |      '0b1101'
 |      >>> (13).bit_count()
 |      3
 |  
 |  bit_length(self, /)
 |      Number of bits necessary to represent self in binary.
 |      
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |  
 |  conjugate(...)
 |      Returns self, the complex conjugate of any int.
 |  
 |  to_bytes(self, /, length, byteorder, *, signed=False)
 |      Return an array of bytes representing an integer.
 |      
 |      length
 |        Length of bytes object to use.  An OverflowError is raised if the
 |        integer is not representable with the given number of bytes.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        `sys.byteorder' as the byte order value.
 |      signed
 |        Determines whether two's complement is used to represent the integer.
 |        If signed is False and a negative integer is given, an OverflowError
 |        is raised.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  from_bytes(bytes, byteorder, *, signed=False) from builtins.type
 |      Return the integer represented by the given array of bytes.
 |      
 |      bytes
 |        Holds the array of bytes to convert.  The argument must either
 |        support the buffer protocol or be an iterable object producing bytes.
 |        Bytes and bytearray are examples of built-in objects that support the
 |        buffer protocol.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        `sys.byteorder' as the byte order value.
 |      signed
 |        Indicates whether two's complement is used to represent the integer.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  denominator
 |      the denominator of a rational number in lowest terms
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  numerator
 |      the numerator of a rational number in lowest terms
 |  
 |  real
 |      the real part of a complex number

help(age.denominator)

name="python programming"
len(name)
18
help(len)
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

name.len
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    name.len
AttributeError: 'str' object has no attribute 'len'

name.len(8)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    name.len(8)
AttributeError: 'str' object has no attribute 'len'
name[0]
'p'
name[-1]
'g'
name[g]
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    name[g]
NameError: name 'g' is not defined
name[-6]
'a'
name[1]
'y'
name[-1]
'g'
name[-13]
'n'
name[-17]
'y'
name[-18]
'p'
name[-16]
't'
name[18]
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    name[18]
IndexError: string index out of range
name[17]
'g'
name[0]
'p'
name[0:2]
'py'
name[0:5]
'pytho'
name[7:18]
'programming'
name[0:3]
'pyt'
name[8:11]
'rog'
name[-6:-8]
''
name[-8:-6]
'gr'
name[-10;-6]
SyntaxError: invalid syntax
name[-10:-6]
'rogr'
name[-10:-7]
'rog'
name[8:12]
'rogr'
name[3:7]
'hon '
name[2:5]
'tho'
name[2:6]
'thon'
name[-17:-14]
'yth'
name[-16:-12]
'thon'
name[0: ]
'python programming'
name[5: }
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
name[5: ]
'n programming'
name[1: ]
'ython programming'
name[-1: ]
'g'
name[-17: ]
'ython programming'
name[ : ]
'python programming'
name[ :-1]
'python programmin'
name[ :0]
''
name[ :-7]
'python prog'
name[0:2:10]
'p'
name[1:2:10]
'y'
name[0::2]
'pto rgamn'
name[1::0]
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    name[1::0]
ValueError: slice step cannot be zero
name[1::5]
'y rn'
name[1::17]
'y'
name[1::6]
'ypm'
name[1::7}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
name[1::7]
'yri'
name[0:10:2]
'pto r'
name[0]
'p'
name[10]
'g'
name[0:15:5]
'png'
name[0::]
'python programming'
name[0:]
'python programming'
name[0;]
SyntaxError: invalid syntax
name[0:: ]
'python programming'
name[0::1]
'python programming'
name[-13:10:-2]
''
name[-13:-5:-2]
''
name[-2:-12]
''
name[-2::-12]
'no'
name[-2:-13]
''
name[-2:-1]
'n'
name[-8:-1]
'grammin'
name[-1:-5]
''
name[-9:-1]
'ogrammin'
name[-12:-17]
''
name[-12:0]
''
name[0:7]
'python '
name[7:0]
''
name[-17::-12]
'y'
name[0::-2]
'p'
name[::-1]
'gnimmargorp nohtyp'
name[::}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
name[::]
'python programming'
dir(name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
name[::-6]
'grn'
name[::-2]
'gimropnhy'
yes=true
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    yes=true
NameError: name 'true' is not defined. Did you mean: 'True'?
yes=True
yes=False
yes=Hello
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    yes=Hello
NameError: name 'Hello' is not defined
'p' in name
True
'p' not in name
False
"o" in name
True
"python" in name
True
"hello" in name
False
'o' is name
False
'p' is name
False
"python" is name
False
"python programming" is name
False
'python programming' is name
False
"python" not in name
False
'python' not in name
False
'Python' not in name
True
"python" in name
True
'p' is name
False
'P' is name
False
'p' is not name
True
'P' is not namew
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    'P' is not namew
NameError: name 'namew' is not defined. Did you mean: 'name'?
'P' is not name
True
"python" is name
False
"Python" is name
False
name is "python programming"
False
name is "python"
False
>>> is name "python"
SyntaxError: invalid syntax
>>> is "python" name
SyntaxError: invalid syntax
>>> Is "python" name
SyntaxError: invalid syntax
>>> is"python' name
SyntaxError: unterminated string literal (detected at line 1)
>>> is "python" name?
SyntaxError: invalid syntax
>>> name is "python"?
SyntaxError: incomplete input
>>> name is "python" ?
SyntaxError: incomplete input
>>> name is " python programming"
False
>>> name="python"
>>> name="programming"
>>> is name "python programming"
SyntaxError: invalid syntax
>>> name is "python programming"
False
>>> name=im
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    name=im
NameError: name 'im' is not defined. Did you mean: 'id'?
>>> name="im"
>>> name="im"
>>> name is "im"
True
>>> name="python"
>>> name="python"
>>> name is "python"
True
>>> age=90
>>> age=90
>>> age is 90
True

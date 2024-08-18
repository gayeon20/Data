---
title: "[Python] 입출력 (Input & Output)"
excerpt: 
categories:
  - Python
tags:
  - Python
  - Input-Output
last_modified_at: 2024-04-11T15:10:55+09:00
link: 
상위 항목: "[[python_home|파이썬 (Python)]]"
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

---

- 프로그램의 출력을 표현하는 여러 가지 방법이 있습니다; 사람이 일기에 적합한 형태로 데이터를 인쇄할 수도 있고, 나중에 사용하기 위해 파일에 쓸 수도 있습니다.

## 장식적인 출력 포매팅

- 지금까지 값을 작성하는 두 가지 방법을 살펴봤습니다: 표현식 문과 [`print()`](https://docs.python.org/ko/3.12/library/functions.html#print “print”) 함수. (세 번째 방법은 파일 객체의 [`write()`](https://docs.python.org/ko/3.12/library/io.html#io.TextIOBase.write “io.TextIOBase.write”) 메서드를 사용하는 것인데, 표준 출력 파일은 `sys.stdout`으로 참조할 수 있습니다. 이에 대한 자세한 내용은 라이브러리 참조를 참조하세요.)
- 종종 단순히 스페이스로 구분된 값을 인쇄하는 것보다 출력 형식을 더 많이 제어해야 하는 경우가 있습니다. 출력을 포맷하는 데는 여러 가지 방법이 있습니다.
- [포맷 문자열 리터럴](https://docs.python.org/ko/3.12/tutorial/inputoutput.html#tut-f-strings)을 사용하려면, 시작 인용 부호 또는 삼중 인용 부호 앞에 `f` 또는 `F` 를 붙여 문자열을 시작하십시오. 이 문자열 안에서, `{` 및 `}` 문자 사이에, 변수 또는 리터럴 값을 참조할 수 있는 파이썬 표현식을 작성할 수 있습니다.
  
```python
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
```

- 문자열의 [`str.format()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.format “str.format”) 메서드는 더 많은 수작업이 필요합니다. 여전히 `{` 및 `}`를 사용하여 변수를 대체할 위치를 표시하고 자세한 서식 지정 지시문을 제공할 수 있지만, 서식을 지정할 정보도 제공해야 합니다. 다음 코드 블록에는 변수 서식을 지정하는 방법에 대한 두 가지 예가 나와 있습니다:

```python
>>> yes_votes = 42_572_654
>>> total_votes = 85_705_149
>>> percentage = yes_votes / total_votes
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
```

`yes_votes`가 공백으로 채워지고 음수인 경우에만 음수 기호가 붙는 것을 볼 수 있습니다. 이 예에서는 소수점 이하 2자리와 퍼센트 기호가 뒤에 오는 `퍼센트`에 100을 곱한 값도 출력합니다(자세한 내용은 [포맷 명세 미니 언어](https://docs.python.org/ko/3.12/library/string.html#formatspec)를 참조하세요).

- 마지막으로, 문자열 슬라이싱 및 이어붙이기 연산을 사용하여 상상할 수 있는 모든 배치를 만듦으로써, 모든 문자열 처리를 스스로 수행할 수 있습니다. 문자열형에는 주어진 열 너비로 문자열을 채우는 데 유용한 연산을 수행하는 몇 가지 메서드가 있습니다.
- 장식적인 출력이 필요하지 않고 단지 디버깅을 위해 일부 변수를 빠르게 표시하려면, [`repr()`](https://docs.python.org/ko/3.12/library/functions.html#repr "repr") 또는 [`str()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str "str") 함수를 사용하여 모든 값을 문자열로 변환할 수 있습니다.
- [`str()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str "str") 함수는 어느 정도 사람이 읽기에 적합한 형태로 값의 표현을 돌려주게 되어있습니다. 반면에 [`repr()`](https://docs.python.org/ko/3.12/library/functions.html#repr "repr") 은 인터프리터에 의해 읽힐 수 있는 형태를 만들게 되어있습니다 (또는 그렇게 표현할 수 있는 문법이 없으면 [`SyntaxError`](https://docs.python.org/ko/3.12/library/exceptions.html#SyntaxError "SyntaxError") 를 일으키도록 구성됩니다). 사람이 소비하기 위한 특별한 표현이 없는 객체의 경우, [`str()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str "str") 는 [`repr()`](https://docs.python.org/ko/3.12/library/functions.html#repr "repr") 과 같은 값을 돌려줍니다. 많은 값, 숫자들이나 리스트와 딕셔너리와 같은 구조들, 은 두 함수를 쓸 때 같은 표현을 합니다. 특별히, 문자열은 두 가지 표현을 합니다.

```python
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '…'
>>> print(s)
The value of x is 32.5, and y is 40000…
>>> # The repr() of a string adds string quotes and backslashes:
>>> hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
>>> repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
```

- [`string`](https://docs.python.org/ko/3.12/library/string.html#module-string "string: Common string operations.") 모듈에는 문자열에 값을 치환하는 또 다른 방법을 제공하는 [`Template`](https://docs.python.org/ko/3.12/library/string.html#string.Template "string.Template") 클래스가 포함되어 있습니다. `$x`와 같은 자리 표시자를 사용하고 이것들을 딕셔너리에서 오는 값으로 치환하지만, 포매팅에 대한 제어를 훨씬 덜 제공합니다.

### 포맷 문자열 리터럴

- [포맷 문자열 리터럴](https://docs.python.org/ko/3.12/reference/lexical_analysis.html#f-strings)(간단히 f-문자열이라고도 합니다)은 문자열에 `f` 또는 `F` 접두어를 붙이고 표현식을 `{expression}`로 작성하여 문자열에 파이썬 표현식의 값을 삽입할 수 있게 합니다.
- 선택적인 포맷 지정자가 표현식 뒤에 올 수 있습니다. 이것으로 값이 포맷되는 방식을 더 정교하게 제어할 수 있습니다. 다음 예는 원주율을 소수점 이하 세 자리로 반올림합니다.

```python
>>> import math
>>> print(f'The value of pi is approximately {math.pi:f}.')
The value of pi is approximately 3.142.
```

- `':'` 뒤에 정수를 전달하면 해당 필드의 최소 문자 폭이 됩니다. 열을 줄 맞춤할 때 편리합니다.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
…     print(f'{name:10} ==> {phone:10d}')
…
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```

- 다른 수정자를 사용하면 포맷되기 전에 값을 변환할 수 있습니다. `'!a'`는 [`ascii()`](https://docs.python.org/ko/3.12/library/functions.html#ascii "ascii")를, `'!s'`는 [`str()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str "str")을, `'!r'`는 [`repr()`](https://docs.python.org/ko/3.12/library/functions.html#repr "repr")을 적용합니다.:

```python
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```

The `=` specifier can be used to expand an expression to the text of the expression, an equal sign, then the representation of the evaluated expression:

>>>

>>> bugs = 'roaches'
>>> count = 13
>>> area = 'living room'
>>> print(f'Debugging {bugs=} {count=} {area=}')
Debugging bugs='roaches' count=13 area='living room'

See [self-documenting expressions](https://docs.python.org/ko/3.12/whatsnew/3.8.html#bpo-36817-whatsnew) for more information on the `=` specifier. For a reference on these format specifications, see the reference guide for the [포맷 명세 미니 언어](https://docs.python.org/ko/3.12/library/string.html#formatspec).

### 7.1.2. 문자열 format() 메서드[](https://docs.python.org/ko/3.12/tutorial/inputoutput.html#the-string-format-method "Link to this heading")

[`str.format()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.format "str.format") 메서드의 기본적인 사용법은 이런 식입니다:

>>>

>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"

중괄호와 그 안에 있는 문자들 (포맷 필드라고 부른다) 은 [`str.format()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.format "str.format") 메서드로 전달된 객체들로 치환됩니다. 중괄호 안의 숫자는 [`str.format()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.format "str.format") 메서드로 전달된 객체들의 위치를 가리키는데 사용될 수 있습니다.

>>>

>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam

[`str.format()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.format "str.format") 메서드에 키워드 인자가 사용되면, 그 값들은 인자의 이름을 사용해서 지정할 수 있습니다.

>>>

>>> print('This {food} is {adjective}.'.format(
…       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.

위치와 키워드 인자를 자유롭게 조합할 수 있습니다:

>>>

>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
…                                                    other='Georg'))
The story of Bill, Manfred, and Georg.

나누고 싶지 않은 정말 긴 포맷 문자열이 있을 때, 포맷할 변수들을 위치 대신에 이름으로 지정할 수 있다면 좋을 것입니다. 간단히 딕셔너리를 넘기고 키를 액세스하는데 대괄호 `'[]'` 를 사용하면 됩니다.

>>>

>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
…       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678

This could also be done by passing the `table` dictionary as keyword arguments with the `**` notation.

>>>

>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678

This is particularly useful in combination with the built-in function [`vars()`](https://docs.python.org/ko/3.12/library/functions.html#vars "vars"), which returns a dictionary containing all local variables:

>>>

>>> table = {k: str(v) for k, v in vars().items()}
>>> message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])
>>> print(message.format(**table))
__name__: __main__; __doc__: None; __package__: None; __loader__: …

As an example, the following lines produce a tidily aligned set of columns giving integers and their squares and cubes:

>>>

>>> for x in range(1, 11):
…     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
…
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000

[`str.format()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.format "str.format") 를 사용한 문자열 포매팅의 완전한 개요는 [포맷 문자열 문법](https://docs.python.org/ko/3.12/library/string.html#formatstrings) 을 보세요.

### 7.1.3. 수동 문자열 포매팅[](https://docs.python.org/ko/3.12/tutorial/inputoutput.html#manual-string-formatting "Link to this heading")

여기 같은 제곱수와 세제곱수 표를 수동으로 포매팅했습니다:

>>>

>>> for x in range(1, 11):
…     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
…     # Note use of 'end' on previous line
…     print(repr(x*x*x).rjust(4))
…
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000

([`print()`](https://docs.python.org/ko/3.12/library/functions.html#print "print") 의 동작 방식으로 인해 각 칼럼 사이에 스페이스 하나가 추가되었음에 유의하세요: 항상 인자들 사이에 스페이스를 추가합니다.)

문자열 객체의 [`str.rjust()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.rjust "str.rjust") 메서드는 왼쪽에 스페이스를 채워서 주어진 폭으로 문자열을 우측 줄 맞춤합니다. 비슷한 메서드 [`str.ljust()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.ljust "str.ljust") 와 [`str.center()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.center "str.center") 도 있습니다. 이 메서드들은 어떤 것도 출력하지 않습니다, 단지 새 문자열을 돌려줍니다. 입력 문자열이 너무 길면, 자르지 않고, 변경 없이 그냥 돌려줍니다; 이것이 열 배치를 엉망으로 만들겠지만, 보통 값에 대해 거짓말을 하게 될 대안보다는 낫습니다. (정말로 잘라내기를 원한다면, 항상 슬라이스 연산을 추가할 수 있습니다, `x.ljust(n)[:n]` 처럼.)

다른 메서드도 있습니다, [`str.zfill()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.zfill "str.zfill"). 숫자 문자열의 왼쪽에 0을 채웁니다. 플러스와 마이너스 부호도 이해합니다:

>>>

>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'

### 7.1.4. 예전의 문자열 포매팅[](https://docs.python.org/ko/3.12/tutorial/inputoutput.html#old-string-formatting "Link to this heading")

The % operator (modulo) can also be used for string formatting. Given `format % values` (where _format_ is a string), `%` conversion specifications in _format_ are replaced with zero or more elements of _values_. This operation is commonly known as string interpolation. For example:

>>>

>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.

더 자세한 내용은 [printf 스타일 문자열 포매팅](https://docs.python.org/ko/3.12/library/stdtypes.html#old-string-formatting) 섹션에 나옵니다.

## 7.2. 파일을 읽고 쓰기[](https://docs.python.org/ko/3.12/tutorial/inputoutput.html#reading-and-writing-files "Link to this heading")

[`open()`](https://docs.python.org/ko/3.12/library/functions.html#open "open") returns a [file object](https://docs.python.org/ko/3.12/glossary.html#term-file-object), and is most commonly used with two positional arguments and one keyword argument: `open(filename, mode, encoding=None)`

>>>

>>> f = open('workfile', 'w', encoding="utf-8")

첫 번째 인자는 파일 이름을 담은 문자열입니다. 두 번째 인자는 파일이 사용될 방식을 설명하는 몇 개의 문자들을 담은 또 하나의 문자열입니다. _mode_ 는 파일을 읽기만 하면 `'r'`, 쓰기만 하면 `'w'` (같은 이름의 이미 존재하는 파일은 삭제됩니다) 가 되고, `'a'` 는 파일을 덧붙이기 위해 엽니다; 파일에 기록되는 모든 데이터는 자동으로 끝에 붙습니다. `'r+'` 는 파일을 읽고 쓰기 위해 엽니다. _mode_ 인자는 선택적인데, 생략하면 `'r'` 이 가정됩니다.

Normally, files are opened in _text mode_, that means, you read and write strings from and to the file, which are encoded in a specific _encoding_. If _encoding_ is not specified, the default is platform dependent (see [`open()`](https://docs.python.org/ko/3.12/library/functions.html#open "open")). Because UTF-8 is the modern de-facto standard, `encoding="utf-8"` is recommended unless you know that you need to use a different encoding. Appending a `'b'` to the mode opens the file in _binary mode_. Binary mode data is read and written as [`bytes`](https://docs.python.org/ko/3.12/library/stdtypes.html#bytes "bytes") objects. You can not specify _encoding_ when opening file in binary mode.

텍스트 모드에서, 읽을 때의 기본 동작은 플랫폼 의존적인 줄 종료 (유닉스에서 `\n`, 윈도우에서 `\r\n`) 를 단지 `\n` 로 변경하는 것입니다. 텍스트 모드로 쓸 때, 기본 동작은 `\n` 를 다시 플랫폼 의존적인 줄 종료로 변환하는 것입니다. 이 파일 데이터에 대한 무대 뒤의 수정은 텍스트 파일의 경우는 문제가 안 되지만, `JPEG` 이나 `EXE` 파일과 같은 바이너리 데이터를 망치게 됩니다. 그런 파일을 읽고 쓸 때 바이너리 모드를 사용하도록 주의하세요.

파일 객체를 다룰 때 [`with`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#with) 키워드를 사용하는 것은 좋은 습관입니다. 혜택은 도중 예외가 발생하더라도 스위트가 종료될 때 파일이 올바르게 닫힌다는 것입니다. `with` 를 사용하는 것은 동등한 [`try`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#try)-[`finally`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#finally) 블록을 쓰는 것에 비교해 훨씬 짧기도 합니다:

>>>

>>> with open('workfile', encoding="utf-8") as f:
…     read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True

[`with`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#with) 키워드를 사용하지 않으면, `f.close()` 를 호출해서 파일을 닫고 사용된 시스템 자원을 즉시 반납해야 합니다.

경고

 

`with` 키워드를 사용하거나 `f.close()`를 호출하지 않고 `f.write()`를 호출하면 프로그램이 성공적으로 종료되더라도 `f.write()`의 인자가 디스크에 완전히 기록되지 않을 **수** 있습니다.

파일 객체가 닫힌 후에는, [`with`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#with) 문이나 `f.close()` 를 호출하는 경우 모두, 파일 객체를 사용하려는 시도는 자동으로 실패합니다.

>>>

>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.

### 7.2.1. 파일 객체의 매소드[](https://docs.python.org/ko/3.12/tutorial/inputoutput.html#methods-of-file-objects "Link to this heading")

이 섹션의 나머지 예들은 `f` 라는 파일 객체가 이미 만들어졌다고 가정합니다.

파일의 내용을 읽으려면, `f.read(size)` 를 호출하는데, 일정량의 데이터를 읽고 문자열 (텍스트 모드 에서) 이나 바이트열 (바이너리 모드에서) 로 돌려줍니다. _size_ 는 선택적인 숫자 인자입니다. _size_ 가 생략되거나 음수면 파일의 내용 전체를 읽어서 돌려줍니다; 파일의 크기가 기계의 메모리보다 두 배 크다면 여러분이 감당할 문제입니다. 그렇지 않으면 최대 _size_ 문자(텍스트 모드에서)나 _size_ 바이트(바이너리 모드에서)를 읽고 돌려줍니다. 파일의 끝에 도달하면, `f.read()` 는 빈 문자열 (`''`) 을 돌려줍니다.

>>>

>>> f.read()
'This is the entire file.\n'
>>> f.read()
''

`f.readline()` 은 파일에서 한 줄을 읽습니다; 개행 문자 (`\n`) 는 문자열의 끝에 보존되고, 파일이 개행문자로 끝나지 않는 때에만 파일의 마지막 줄에서만 생략됩니다. 이렇게 반환 값을 모호하지 않게 만듭니다; `f.readline()` 가 빈 문자열을 돌려주면, 파일의 끝에 도달한 것이지만, 빈 줄은 `'\n'`, 즉 하나의 개행문자만을 포함하는 문자열로 표현됩니다.

>>>

>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''

파일에서 줄들을 읽으려면, 파일 객체에 대해 루핑할 수 있습니다. 이것은 메모리 효율적이고, 빠르며 간단한 코드로 이어집니다:

>>>

>>> for line in f:
…     print(line, end='')
…
This is the first line of the file.
Second line of the file

파일의 모든 줄을 리스트로 읽어 들이려면 `list(f)` 나 `f.readlines()` 를 쓸 수 있습니다.

`f.write(string)` 은 _string_ 의 내용을 파일에 쓰고, 출력된 문자들의 개수를 돌려줍니다.

>>>

>>> f.write('This is a test\n')
15

다른 형의 객체들은 쓰기 전에 변환될 필요가 있습니다 – 문자열 (텍스트 모드에서) 이나 바이트열 객체 (바이너리 모드에서) 로 –:

>>>

>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18

`f.tell()` 은 파일의 현재 위치를 가리키는 정수를 돌려주는데, 바이너리 모드의 경우 파일의 처음부터의 바이트 수로 표현되고 텍스트 모드의 경우는 불투명한 숫자입니다.

파일 객체의 위치를 바꾸려면, `f.seek(offset, whence)` 를 사용합니다. 위치는 기준점에 _offset_ 을 더해서 계산됩니다; 기준점은 _whence_ 인자로 선택합니다. _whence_ 값이 0이면 파일의 처음부터 측정하고, 1이면 현재 파일 위치를 사용하고, 2 는 파일의 끝을 기준점으로 사용합니다. _whence_ 는 생략될 수 있고, 기본값은 0이라서 파일의 처음을 기준점으로 사용합니다.

>>>

>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'

텍스트 파일에서는 (모드 문자열에 `b` 가 없이 열린 것들), 파일의 시작에 상대적인 위치 변경만 허락되고 (예외는 `seek(0, 2)` 를 사용해서 파일의 끝으로 위치를 변경하는 경우입니다), 올바른 _offset_ 값은 `f.tell()` 이 돌려준 값과 0뿐입니다. 그 밖의 다른 _offset_ 값은 정의되지 않은 결과를 낳습니다.

File objects have some additional methods, such as [`isatty()`](https://docs.python.org/ko/3.12/library/io.html#io.IOBase.isatty "io.IOBase.isatty") and [`truncate()`](https://docs.python.org/ko/3.12/library/io.html#io.IOBase.truncate "io.IOBase.truncate") which are less frequently used; consult the Library Reference for a complete guide to file objects.

### 7.2.2. [`json`](https://docs.python.org/ko/3.12/library/json.html#module-json "json: Encode and decode the JSON format.") 으로 구조적인 데이터를 저장하기[](https://docs.python.org/ko/3.12/tutorial/inputoutput.html#saving-structured-data-with-json "Link to this heading")

Strings can easily be written to and read from a file. Numbers take a bit more effort, since the [`read()`](https://docs.python.org/ko/3.12/library/io.html#io.TextIOBase.read "io.TextIOBase.read") method only returns strings, which will have to be passed to a function like [`int()`](https://docs.python.org/ko/3.12/library/functions.html#int "int"), which takes a string like `'123'` and returns its numeric value 123. When you want to save more complex data types like nested lists and dictionaries, parsing and serializing by hand becomes complicated.

Rather than having users constantly writing and debugging code to save complicated data types to files, Python allows you to use the popular data interchange format called [JSON (JavaScript Object Notation)](https://json.org/). The standard module called [`json`](https://docs.python.org/ko/3.12/library/json.html#module-json "json: Encode and decode the JSON format.") can take Python data hierarchies, and convert them to string representations; this process is called _serializing_. Reconstructing the data from the string representation is called _deserializing_. Between serializing and deserializing, the string representing the object may have been stored in a file or data, or sent over a network connection to some distant machine.

참고

 

JSON 형식은 데이터 교환을 위해 현대 응용 프로그램들이 자주 사용합니다. 많은 프로그래머가 이미 이것에 익숙하므로, 연동성을 위한 좋은 선택이 됩니다.

객체 `x` 가 있을 때, 간단한 한 줄의 코드로 그것의 JSON 문자열 표현을 볼 수 있습니다:

>>>

>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'

[`dump()`](https://docs.python.org/ko/3.12/library/json.html#json.dump "json.dump")라는 [`dumps()`](https://docs.python.org/ko/3.12/library/json.html#json.dumps "json.dumps") 함수의 변종은 객체를 [텍스트 파일](https://docs.python.org/ko/3.12/glossary.html#term-text-file) 로 직렬화합니다. 그래서 `f` 가 쓰기를 위해 열린 [텍스트 파일](https://docs.python.org/ko/3.12/glossary.html#term-text-file) 이면, 이렇게 할 수 있습니다:

json.dump(x, f)

To decode the object again, if `f` is a [binary file](https://docs.python.org/ko/3.12/glossary.html#term-binary-file) or [text file](https://docs.python.org/ko/3.12/glossary.html#term-text-file) object which has been opened for reading:

x = json.load(f)

참고

 

JSON files must be encoded in UTF-8. Use `encoding="utf-8"` when opening JSON file as a [text file](https://docs.python.org/ko/3.12/glossary.html#term-text-file) for both of reading and writing.

이 간단한 직렬화 테크닉이 리스트와 딕셔너리를 다룰 수 있지만, 임의의 클래스 인스턴스를 JSON 으로 직렬화하기 위해서는 약간의 수고가 더 필요합니다. [`json`](https://docs.python.org/ko/3.12/library/json.html#module-json "json: Encode and decode the JSON format.") 모듈의 레퍼런스는 이 방법에 대한 설명을 담고 있습니다.

더 보기

 

[`pickle`](https://docs.python.org/ko/3.12/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") - 피클 모듈

[JSON](https://docs.python.org/ko/3.12/tutorial/inputoutput.html#tut-json) 에 반해, _pickle_ 은 임의의 복잡한 파이썬 객체들을 직렬화할 수 있는 프로토콜입니다. 파이썬에 국한되고 다른 언어로 작성된 응용 프로그램들과 통신하는데 사용될 수 없습니다. 기본적으로 안전하지 않기도 합니다: 믿을 수 없는 소스에서 온 데이터를 역 직렬화할 때, 숙련된 공격자에 의해 데이터가 조작되었다면 임의의 코드가 실행될 수 있습니다.

---
## 참조
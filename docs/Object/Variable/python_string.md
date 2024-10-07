---
title: "[Python] 문자열 (String)"
excerpt: 
categories:
  - Python
tags:
  - Python
  - Object
  - Variable
  - String
last_modified_at: 2024-04-11T15:10:55+09:00
link: https://docs.python.org/ko/3.12/library/string.html#formatstrings
상위 항목: "[[python_variable|파이썬 변수 (Python Variable)]]"
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

---

- 파이썬의 텍스트 데이터는 [`str`](https://docs.python.org/ko/3.12/library/stdtypes.html#str "str"), 또는 _문자열 (strings)_, 객체를 사용하여 처리됩니다. 문자열은 유니코드 코드 포인트의 불변 [시퀀스](https://docs.python.org/ko/3.12/library/stdtypes.html#typesseq) 입니다. 

```python
s = "Hello"
print(s) # 결과: "Hello"

string = """
H
E
L
L
O
"""
print(string)
```

- 문자열 리터럴은 다양한 방법으로 작성됩니다:
  
  작은따옴표: `'"큰" 따옴표를 담을 수 있습니다'`
  Double quotes: `"allows embedded 'single' quotes"`
  삼중 따옴표: `'''세 개의 작은따옴표'''`, `"""세 개의 큰따옴표"""`

- 삼중 따옴표로 묶인 문자열은 여러 줄에 걸쳐있을 수 있습니다 - 연관된 모든 공백이 문자열 리터럴에 포함됩니다.
- 단일 표현식의 일부이고 그 들 사이에 공백만 있는 문자열 리터럴은 묵시적으로 단일 문자열 리터럴로 변환됩니다. 즉, `("spam " "eggs") == "spam eggs"`.
- 문자열은 [`str`](https://docs.python.org/ko/3.12/library/stdtypes.html#str "str") 생성자를 사용하여 다른 객체로부터 만들어질 수도 있습니다.
- 별도의 `char` 형이 없으므로 문자열을 인덱싱하면 길이가 1인 문자열이 생성됩니다. 
  즉, 비어 있지 않은 문자열 _s_ 의 경우, `s[0] == s[0:1]` 입니다.

```python
print("Hello," + "World") # 결과: "Hello, World"
print("Repeat " * 3) # 결과: "Repeat Repeat Repeat "
print("Hey, " + ("Fighting! " * 3) ) # 결과: Hey, Fighting! Fighting! Fighting! 
```

- 문자열에 `+` 를 사용하면 두 문자열을 합친 결과가 나타난다.
- 문자열에 `*` 를 사용하면 해당 문자열이 숫자만큼 반복된다.
- `()` 도 사용할 수 있다. 우선 순위는 숫자 연산의 `()` 와 같게 적용된다.
- 두 개 이상의 _문자열 리터럴_ (즉, 따옴표로 둘러싸인 것들) 가 연속해서 나타나면 자동으로 이어 붙여집니다.

```python
>>> 'Py' 'thon'
'Python'
```

- 이것은 오직 두 개의 리터럴에만 적용될 뿐 변수나 표현식에는 해당하지 않습니다:

```python
>>> prefix = 'Py'
>>> prefix 'thon'  # can't concatenate a variable and a string literal
  File "<stdin>", line 1
    prefix 'thon'
           ^^^^^^
SyntaxError: invalid syntax
>>> ('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
               ^^^^^
SyntaxError: invalid syntax
```

## 이스케이프 문자 (Escape String)
- 원래 의미를 탈출하는 문자, 특수한 역할을 하는 문자를 의미한다
- 예를 들어 "hello world"라는 따옴표까지 포함된 문장을 출력하고 싶을 때 print문 안에 입력하게 되면 기본으로 문장임을 타나내주는 따옴표가 있다. 하지만 이 따옴표는 출력되지 않고 hello world만 출력된다.

| escape character | 설명       |
| ---------------- | -------- |
| `\'`             | 작은따옴표 출력 |
| `\"`             | 큰따옴표 출력  |
| `\\`             | 백슬래시 출력  |
| `\?`             | 물음표 출력   |
| `\n`             | 줄 바꿈     |
| `\t`             | 가로 탭     |
| `\v`             | 세로 탭     |
| `\b`             | 백스페이스    |
| `\r`             | 캐리지리턴    |


```python
S = "'를 나타낼 수 있습니다. \"를 나타내려면 쌍따옴표 앞에 역슬래시를 붙이세요."
STRING = '"를 나타낼 수 있습니다. \'를 나타내려면 홑따옴표 앞에 역슬래시를 붙이세요.'

print(S)
print(STRING)
```

`"` 로 문자열을 나타냈을 경우 안에 `'` 을 문자로 사용할 수 있다. `"` 를 나타내기 위해서는 `\"` 와 같이 `\` 를 붙여야 한다. (Escape String)
`'` 로 나타냈을 경우에는 안에 `"` 를 사용할 수 있다. `'` 를 나타내려면 마찬가지로 `\'` 로 사용해야 한다.

> `\` 를 사용하면 가독성이 떨어지므로 최대한 피해서 나타내는 것이 좋다.
> 또한 하나의 파일에서는 한 종류의 따옴표만 일관되게 사용하는 것이 유지보수에 용이하다.


## 인덱스 (Index)
```python
STRING = "Hello, World!"
print(STRING[2]) # 결과: l
```

String 타입에도 Index 를 사용할 수 있다. 해당 위치에 있는 문자가 반환된다.

```python
STRING = "Can't change"
STRING[3:5] = "" # 결과: 에러 발생
```

String 은 Immutable 타입이므로 Index 를 사용한 변경이 불가능하다.
String 의 값을 변경하기 위해선 새로운 객체를 생성해야 한다.

## 포맷 문자열 리터럴 (f-string)

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

- `=` 지정자는 표현식의 텍스트, 등호, 평가된 표현식의 표현으로 표현식을 확장하는 데 사용할 수 있습니다:

```python
>>> bugs = 'roaches'
>>> count = 13
>>> area = 'living room'
>>> print(f'Debugging {bugs=} {count=} {area=}')
Debugging bugs='roaches' count=13 area='living room'
```
- `=` 지정자에 대한 자세한 내용은 [자체 문서화 표현식](https://docs.python.org/ko/3.12/whatsnew/3.8.html#bpo-36817-whatsnew)을 참조하세요. 이러한 형식 명세에 대한 참조는 [형식 명세 미니 언어](https://docs.python.org/ko/3.12/library/string.html#formatspec) 참조 가이드를 참조하세요.

### 문자열 format() 메서드
- [`str.format()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.format "str.format") 메서드의 기본적인 사용법은 이런 식입니다:

```python
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```

- 중괄호와 그 안에 있는 문자들 (포맷 필드라고 부른다) 은 [`str.format()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.format "str.format") 메서드로 전달된 객체들로 치환됩니다. 중괄호 안의 숫자는 [`str.format()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.format "str.format") 메서드로 전달된 객체들의 위치를 가리키는데 사용될 수 있습니다.

```python
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```

- [`str.format()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.format "str.format") 메서드에 키워드 인자가 사용되면, 그 값들은 인자의 이름을 사용해서 지정할 수 있습니다.

```python
>>> print('This {food} is {adjective}.'.format(
…       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```

- 위치와 키워드 인자를 자유롭게 조합할 수 있습니다:

```python
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
…                                                    other='Georg'))
The story of Bill, Manfred, and Georg.
```

- 나누고 싶지 않은 정말 긴 포맷 문자열이 있을 때, 포맷할 변수들을 위치 대신에 이름으로 지정할 수 있다면 좋을 것입니다. 간단히 딕셔너리를 넘기고 키를 액세스하는데 대괄호 `'[]'` 를 사용하면 됩니다.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
…       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

- 이 작업은 `**` 표기법과 함께 키워드 인자로 `table` 사전을 전달하여 수행할 수도 있습니다.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

- 이는 모든 로컬 변수가 포함된 사전을 반환하는 기본 제공 함수 [`vars()`](https://docs.python.org/ko/3.12/library/functions.html#vars "vars")와 함께 사용하면 특히 유용합니다:

```python
>>> table = {k: str(v) for k, v in vars().items()}
>>> message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])
>>> print(message.format(**table))
__name__: __main__; __doc__: None; __package__: None; __loader__: …
```

- 예를 들어, 다음 줄은 정수와 그 정사각형 및 정육면체를 제공하는 깔끔하게 정렬된 열 집합을 생성합니다:

```python
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
```

- [`str.format()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.format "str.format") 를 사용한 문자열 포매팅의 완전한 개요는 [포맷 문자열 문법](https://docs.python.org/ko/3.12/library/string.html#formatstrings) 을 보세요.

### 수동 문자열 포매팅

- 여기 같은 제곱수와 세제곱수 표를 수동으로 포매팅했습니다:

```python
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
```

([`print()`](https://docs.python.org/ko/3.12/library/functions.html#print "print") 의 동작 방식으로 인해 각 칼럼 사이에 스페이스 하나가 추가되었음에 유의하세요: 항상 인자들 사이에 스페이스를 추가합니다.)

- 문자열 객체의 [`str.rjust()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.rjust "str.rjust") 메서드는 왼쪽에 스페이스를 채워서 주어진 폭으로 문자열을 우측 줄 맞춤합니다. 비슷한 메서드 [`str.ljust()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.ljust "str.ljust") 와 [`str.center()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.center "str.center") 도 있습니다. 이 메서드들은 어떤 것도 출력하지 않습니다, 단지 새 문자열을 돌려줍니다. 입력 문자열이 너무 길면, 자르지 않고, 변경 없이 그냥 돌려줍니다; 이것이 열 배치를 엉망으로 만들겠지만, 보통 값에 대해 거짓말을 하게 될 대안보다는 낫습니다. (정말로 잘라내기를 원한다면, 항상 슬라이스 연산을 추가할 수 있습니다, `x.ljust(n)[:n]` 처럼.)
- 다른 메서드도 있습니다, [`str.zfill()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.zfill "str.zfill"). 숫자 문자열의 왼쪽에 0을 채웁니다.

```python
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
```

### 예전의 문자열 포매팅 [(Guide)](https://docs.python.org/ko/3.12/library/stdtypes.html#old-string-formatting)

- 연산자(모듈로)는 문자열 서식 지정에도 사용할 수 있습니다. `형식 % 값`(여기서 format은 문자열)이 주어지면 format_의 `%` 변환 사양은 0개 이상의 값 요소로 대체됩니다. 이 연산을 일반적으로 문자열 보간이라고 합니다. 예를 들어

```python
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```

> 여기에 설명된 포맷 연산은 여러 가지 일반적인 오류를 (예를 들어 튜플과 딕셔너리를 올바르게 표시하지 못하는 것) 유발하는 다양한 문제점들이 있습니다. 새 [포맷 문자열 리터럴](https://docs.python.org/ko/3.12/reference/lexical_analysis.html#f-strings) 나 [`str.format()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.format "str.format") 인터페이스 혹은 [템플릿 문자열](https://docs.python.org/ko/3.12/library/string.html#template-strings) 을 사용하면 이러한 오류를 피할 수 있습니다. 이 대안들은 또한 텍스트 포매팅에 더욱 강력하고 유연하며 확장 가능한 접근법을 제공합니다.

- 문자열 객체는 한가지 고유한 내장 연산을 갖고 있습니다: `%` 연산자 (모듈로). 이것은 문자열 _포매팅_ 또는 _치환_ 연산자라고도 합니다. `format % values` 가 주어질 때 (_format_ 은 문자열입니다), _format_ 내부의 `%` 변환 명세는 0개 이상의 _values_ 의 요소로 대체됩니다. 이 효과는 C 언어에서 `sprintf()`를 사용하는 것과 비슷합니다.
- _format_ 이 하나의 인자를 요구하면, _values_ 는 하나의 비 튜플 객체 일 수 있습니다. [[5]](https://docs.python.org/ko/3.12/library/stdtypes.html#id16) 그렇지 않으면, _values_ 는 format 문자열이 지정하는 항목의 수와 같은 튜플이거나 단일 매핑 객체 (예를 들어, 딕셔너리) 이어야 합니다.
- 변환 명세는 두 개 이상의 문자를 포함하며 다음과 같은 구성 요소들을 포함하는데, 반드시 이 순서대로 나와야 합니다:
  
  1. `'%'` 문자: 명세의 시작을 나타냅니다.
  2. 매핑 키 (선택 사항): 괄호로 둘러싸인 문자들의 시퀀스로 구성됩니다 (예를 들어, `(somename)`).
  3. 변환 플래그 (선택 사항): 일부 변환 유형의 결과에 영향을 줍니다.
  4. 최소 필드 폭 (선택 사항): `'*'` (애스터리스크) 로 지정하면, 실제 폭은 _values_ 튜플의 다음 요소에서 읽히고, 변환할 객체는 최소 필드 폭과 선택적 정밀도 뒤에 옵니다.
  5. 정밀도 (선택 사항): `'.'` (점) 다음에 정밀도가 옵니다. `'*'` (애스터리스크) 로 지정하면, 실제 정밀도는 _values_ 튜플의 다음 요소에서 읽히고, 변환할 값은 정밀도 뒤에 옵니다.
  6. 길이 수정자 (선택 사항).
  7. 변환 유형.

- 오른쪽 인자가 딕셔너리 (또는 다른 매핑 형) 인 경우, 문자열에 있는 변환 명세는 _반드시_ `'%'` 문자 바로 뒤에 그 딕셔너리의 매핑 키를 괄호로 둘러싼 형태로 포함해야 합니다. 매핑 키는 포맷할 값을 매핑으로 부터 선택합니다. 예를 들어:

```python
>>> print('%(language)s has %(number)03d quote types.' %
…       {'language': "Python", "number": 2})
Python has 002 quote types.
```

- 이 경우 `*` 지정자를 사용할 수 없습니다 (순차적인 매개변수 목록이 필요하기 때문입니다).
- 변환 플래그 문자는 다음과 같습니다:

| 플래그   | 뜻                                                        |
| ----- | -------------------------------------------------------- |
| `'#'` | 값 변환에 “대체 형식” (아래에 정의되어있습니다) 을 사용합니다.                    |
| `'0'` | 변환은 숫자 값의 경우 0으로 채웁니다.                                   |
| `'-'` | 변환된 값은 왼쪽으로 정렬됩니다 (둘 다 주어지면 `'0'` 변환보다 우선 합니다).          |
| `' '` | (스페이스) 부호 있는 변환 때문에 만들어진 양수 앞에 빈칸을 남겨둡니다 (음수면 빈 문자열입니다). |
| `'+'` | 부호 문자 (`'+'` or `'-'`) 가 변환 앞에 놓입니다 (`' '` 플래그에 우선합니다).  |

- 길이 수정자 (`h`, `l`, `L`) 를 제공할 수는 있지만, 파이썬에서 필요하지 않기 때문에 무시됩니다 – 예를 들어 `%ld` 는 `%d` 와 같습니다. 변환 유형은 다음과 같습니다:

| 변환    | 뜻                                                                                                             | 노트  |
| ----- | ------------------------------------------------------------------------------------------------------------- | --- |
| `'d'` | 부호 있는 정수 십진 표기.                                                                                               |     |
| `'i'` | 부호 있는 정수 십진 표기.                                                                                               |     |
| `'o'` | 부호 있는 8진수 값.                                                                                                  | (1) |
| `'u'` | 쓸데없는 유형 – `'d'` 와 같습니다.                                                                                       | (6) |
| `'x'` | 부호 있는 16진수 (소문자).                                                                                             | (2) |
| `'X'` | 부호 있는 16진수 (대문자).                                                                                             | (2) |
| `'e'` | 부동 소수점 지수 형식(소문자).                                                                                            | (3) |
| `'E'` | 부동 소수점 지수 형식(대문자).                                                                                            | (3) |
| `'f'` | 부동 소수점 십진수 형식입니다.                                                                                             | (3) |
| `'F'` | 부동 소수점 십진수 형식입니다.                                                                                             | (3) |
| `'g'` | 부동소수점 형식입니다. 지수가 -4 미만이거나 정밀도보다 작으면 소문자 지수 형식을 사용하고, 그렇지 않으면 소수점 형식을 사용합니다.                                   | (4) |
| `'G'` | 부동 소수점 형식입니다. 지수가 -4 미만이거나 정밀도보다 작으면 대문자 지수 형식을 사용하고, 그렇지 않으면 소수점 형식을 사용합니다.                                  | (4) |
| `'c'` | 단일 문자 (정수 또는 길이 1인 문자열을 허용합니다).                                                                               |     |
| `'r'` | 문자열 ([`repr()`](https://docs.python.org/ko/3.12/library/functions.html#repr "repr")을 사용하여 파이썬 객체를 변환합니다).     | (5) |
| `'s'` | 문자열 ([`str()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str "str") 을 사용하여 파이썬 객체를 변환합니다).        | (5) |
| `'a'` | 문자열 ([`ascii()`](https://docs.python.org/ko/3.12/library/functions.html#ascii "ascii") 를 사용하여 파이썬 객체를 변환합니다). | (5) |
| `'%'` | 인자는 변환되지 않고, 결과에 `'%'` 문자가 표시됩니다.                                                                             |     |


> [!NOTE]
> 1. 대체 형식은 첫 번째 숫자 앞에 선행 8진수 지정자 (`'0o'`)를 삽입합니다.
> 2. 대체 형식은 첫 번째 숫자 앞에 선행 `'0x'` 또는 `'0X'` (`'x'` 나 `'X'` 유형 중 어느 것을 사용하느냐에 따라 달라집니다) 를 삽입합니다.
> 3. 대체 형식은 그 뒤에 숫자가 나오지 않더라도 항상 소수점을 포함합니다.
>     정밀도는 소수점 이하 자릿수를 결정하며 기본값은 6입니다.
> 4. 대체 형식은 결과에 항상 소수점을 포함하고 뒤에 오는 0은 제거되지 않습니다.
>     정밀도는 소수점 앞뒤의 유효 자릿수를 결정하며 기본값은 6입니다.
> 5. 정밀도가 `N` 이라면, 출력은 `N` 문자로 잘립니다.
> 6. [**PEP 237**](https://peps.python.org/pep-0237/)을 참조하세요.

- 파이썬 문자열은 명시적인 길이를 가지고 있으므로, `%s` 변환은 문자열의 끝이 `'\0'` 이라고 가정하지 않습니다.
> 버전 3.1에서 변경: 절댓값이 1e50 을 넘는 숫자에 대한 `%f` 변환은 더는 `%g` 변환으로 대체되지 않습니다.

## 내부 메소드
> [내장형 — Python 3.12.5 문서](https://docs.python.org/ko/3.12/library/stdtypes.html#textseq)

### `replace`

```python
# "A"를 "F"로 변환
message.replace("A", "F")
```

- `replace(FROM, TO)` 는 문자열에 존재하는 `FROM` 을 `TO` 로 바꿔준다.
- 문자열 내에 `FROM` 이 존재하지 않으면 오류가 발생한다.

### `str.count(_sub_[, _start_[, _end_]])`

- 범위 [_start_, _end_] 에서 부분 문자열 _sub_ 가 중첩되지 않고 등장하는 횟수를 돌려줍니다. 선택적 인자 _start_ 와 _end_ 는 슬라이스 표기법으로 해석됩니다.
- `sub`가 비어 있으면 문자열 길이에 1을 더한 문자 사이의 빈 문자열 수를 반환합니다.

### `str.find(_sub_[, _start_[, _end_]])`

- 부분 문자열 _sub_ 가 슬라이스 `s[start:end]` 내에 등장하는 가장 작은 문자열의 인덱스를 돌려줍니다. 선택적 인자 _start_ 와 _end_ 는 슬라이스 표기법으로 해석됩니다. _sub_ 가 없으면 `-1` 을 돌려줍니다.

> [!NOTE]
> - [`find()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.find "str.find") 메서드는 _sub_ 의 위치를 알아야 할 경우에만 사용해야 합니다. _sub_ 가 부분 문자열인지 확인하려면 [`in`](https://docs.python.org/ko/3.12/reference/expressions.html#in) 연산자를 사용하십시오:
> 
> ```python
> 'Py' in 'Python'
> True
> ```

### `str.index(_sub_[, _start_[, _end_]])`

- [`find()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.find "str.find") 과 비슷하지만, 부분 문자열을 찾을 수 없는 경우 [`ValueError`](https://docs.python.org/ko/3.12/library/exceptions.html#ValueError "ValueError") 를 일으킵니다.

### `join`

```python
# join()의 대상 문자열을 기준으로 합쳐준다.
phone_number_segments = ["010","0000","1111"]
print("-".join(phone_number_segments)) # 결과: "010-0000-1111"
```

- `join(TARGET)` 로 `TARGET` 의 구분자에 함수를 호출한 문자열을 삽입한다.

### `split`

```python
# '-' 기준으로 분리
phone_number.split("-")

# 공백을 기준으로 분리
address.split()
```

- `split(seperator)` 은 `seperator` 를 기준으로 문자열을 분리할 때 사용한다.

```python
message = "Hello World"
print(message.split(" "))
# 결과: ["Hello", "World"]
```
- 분리한 결과는 List 의 형태로 반환된다.

### `with`

```python
a = "Python is easy!"
print(a.startswith("Python")) # 결과: True
print(a.endswith("!")) # 결과: True
```

- `startswith()` 은 대상이 입력한 문자열로 시작하는지 확인한다.
- `endswith()` 은 대상이 입력한 문자열로 끝나는지 확인한다.

### `strip`

```python
message.strip()
```

- `strip()` 은 문자열 양 옆의 공백을 제거한다.
- 문자열 중간의 공백은 그대로 남는다.

### `lower` & `upper`
- `lower()` 는 영어를 모두 소문자로 변환한다.
- 예를 들어, 일부 유럽 언어에서는 특정 대문자 문자가 두 개 이상의 소문자 문자로 변환될 수 있습니다. 이러한 경우, `lower()` 메소드보다 [`casefold()`](vscode-file://vscode-app/c:/Users/skysk/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html "../../../.vscode/extensions/ms-python.vscode-pylance-2024.6.1/dist/typeshed-fallback/stdlib/builtins.pyi") 메소드가 더 정확한 소문자 변환을 제공합니다.
- `upper()` 는 영어를 모두 대문자로 변환한다.

### `str.casefold()`
- `casefold()` `lower()` 메소드와 유사하지만, 더 강력한 소문자 변환 기능을 제공하여 다양한 언어에서의 문자 변환에 있어 더욱 일관된 결과를 보장합니다. [`casefold()`](vscode-file://vscode-app/c:/Users/skysk/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html "../../../.vscode/extensions/ms-python.vscode-pylance-2024.6.1/dist/typeshed-fallback/stdlib/builtins.pyi")는 문자열을 정규화하여 대소문자 구분 없이 문자열 비교를 수행할 때 유용하게 사용됩니다.

### `str.capitalize()`
- `capitalize()` 는 앞 글자만 대문자로 바꾸고 나머지는 소문자로 바꾼다.

### `center`
- 길이 _width_ 인 문자열의 가운데에 정렬한 값을 돌려줍니다. 지정된 _fillchar_ (기본값은 ASCII 스페이스)을 사용하여 채웁니다. _width_ 가 `len(s)` 보다 작거나 같은 경우 원래 문자열이 반환됩니다.

### `endswith`

문자열이 지정된 _suffix_ 로 끝나면 `True` 를 돌려주고, 그렇지 않으면 `False` 를 돌려줍니다. _suffix_ 는 찾고자 하는 접미사들의 튜플이 될 수도 있습니다. 선택적 _start_ 가 제공되면 그 위치에서 검사를 시작합니다. 선택적 _end_ 를 사용하면 해당 위치에서 비교를 중단합니다.

### `str.format(_*args_, _**kwargs_)`
> [string — Common string operations — Python 3.12.5 문서](https://docs.python.org/ko/3.12/library/string.html#formatstrings)

- 문자열 포맷 연산을 수행합니다. 이 메서드가 호출되는 문자열은 리터럴 텍스트나 중괄호 `{}` 로 구분된 치환 필드를 포함할 수 있습니다. 각 치환 필드는 위치 인자의 숫자 인덱스나 키워드 인자의 이름을 가질 수 있습니다. 각 치환 필드를 해당 인자의 문자열 값으로 치환한 문자열의 사본을 돌려줍니다.
> 이전의 `printf` 보다는 `str.format()` 의 사용을 권장한다. 3.6 버전 이상부터는 f 문자열이 더 간편하다.

```python
"Hello, {}!".format('Chris')
```

- 문자열 내에 `{}` 를 입력 후 `format()` 으로 값을 입력할 수 있다.
- Python 에 추가된 f 문자열의 기능과 같다.

**Index**

```python
name = "Chris"
job = "PROGRAMMER"

print("Good {1}, {0}.".format(name, job))
```

- 숫자로 Index 를 지정하면 그 위치에 입력된다.

```python
name = "Chris"
job = "PROGRAMMER"

print("Good {n}, {j}.".format(n=name, j=job))
```

- Index 는 문자도 사용할 수 있다.

**Unpacking**

```python
print("{0} - {1} - {2}".format(*'ABC'))
print("{0} - {1} - {2}".format(*['A', 'B', 'C']))
```

- `*` 로 언패킹하여 값을 입력할 수 있다.

```python
print("{0[0]} - {0[1]} - {0[2]}".format(['A', 'B', 'C']))
print("{0[name]}".format({'name':'Chris', 'family-name':'Cho'}))
```

- List, Dictionary 등의 Collection 을 입력하고 Index `[]` 를 활용하는 것도 가능하다.

**Sort**

```python
print('{:<20}'.format('좌측 정렬'))
print('{:>20}'.format('우측 정렬'))
print('{:^20}'.format('중앙 정렬'))
print('{:%^20}'.format('중앙 정렬'))
```

- `:<` 으로 좌측 정렬을 할 수 있다.
- `:>` 으로 우측 정렬을 할 수 있다.
- `:^` 으로 중앙 정렬을 할 수 있다.
- 숫자는 글자 수를 의미한다. `:` 뒤에 원하는 글자를 입력하면 정렬할 때 빈 공간을 해당 글자로 채울 수 있다.

**Float**

```python
import math
print('원주율의 크기는 대략 {:f} 입니다.'.format(math.pi))
print('원주율의 크기는 대략 {:f} 입니다.'.format(math.pi))
```

- `f` 는 실수 타입을 의미한다.
- `` 와 같이 `.` 과 숫자를 입력하면 해당 자릿수까지 반올림해서 나타낼 수 있다.

```python
print('{:+f}; {:+f}'.format(3.14, -3.14))
print('{: f}; {: f}'.format(3.14, -3.14))
print('{:-f}; {:-f}'.format(3.14, -3.14))
```

- `:+f` 와 같이 `+` 를 붙이면 숫자의 기호가 나타난다.
- `: f` 와 같이 빈칸을 추가하면 `+` 기호는 공백으로 나타내고 `-` 기호만 나타난다.
- `:-f` 와 같이 `-` 를 붙이면 `+` 기호는 생략하고 `-` 기호만 나타낸다.

**Integer**

```python
print('정수: {0:d}; 16진수: {0:x}; 8진수: {0:o}; 2진수: {0:b}'.format(50))
print('정수: {0:d}; 16진수: {0:#x}; 8진수: {0:#o}; 2진수: {0:#b}'.format(50))
```

- `:d` 와 같이 `:` 에 해당 진수의 알파벳을 붙이면 그 진수로 변환할 수 있다.
- `:#x` 와 같이 진수 알파벳 앞에 `#` 을 붙이면 각 진수의 표준 접두어까지 나타낼 수 있다.
- 위 예시의 `0` 은 Index 를 나타낸다. 같은 숫자를 다양한 형태로 변환하기 위해 사용했다.

| 타입   | 설명                                                 |
| ---- | -------------------------------------------------- |
| b    | 2 진수                                                |
| c    | 문자                                                 |
| d    | 10 진수                                               |
| o    | 8 진수 (접두어: 0o)                                      |
| x    | 16 진수, 9 보다 큰 수에 대해서는 소문자 알파벳 사용 (접두어: 0x)           |
| X    | 16 진수, 9 보다 큰 수에 대해서는 대문자 알파벳 사용 (접두어: 0X)           |
| n    | 숫자, 기본적으로는 d 와 같다. 각 나라에 맞는 숫자 구분자를 넣기 위해 locale 사용 |
| None | 아무 것도 입력하지 않은 경우, d 와 같다.                           |

```python
print('{:,}'.format(10000000))
```

- `:,` 을 사용하면 숫자의 천 단위마다 구분자를 입력한다.

```python
print('{:%}'.format(5/12))
```

- `:%` 을 사용하면 비율을 백분율 (%) 로 나타낼 수 있다.

### `str.format_map(_mapping_)`

- `str.format(**mapping)` 과 비슷하지만, [`dict`](https://docs.python.org/ko/3.12/library/stdtypes.html#dict "dict")로 복사되지 않고 `mapping` 을 직접 사용합니다. 예를 들어 `mapping` 이 dict 서브 클래스면 유용합니다:

```python
>>> class Default(dict):
…     def __missing__(self, key):
…         return key
…
>>> '{name} was born in {country}'.format_map(Default(name='Guido'))
'Guido was born in country'
```


### `str.encode(encoding='utf-8', errors='strict')`
- [`바이트`](https://docs.python.org/ko/3.12/library/stdtypes.html#bytes “바이트”)로 인코딩된 문자열을 반환합니다.
- _encoding_의 기본값은 'utf-8'입니다. 사용 가능한 값은 [표준 인코딩](https://docs.python.org/ko/3.12/library/codecs.html#standard-encodings)을 참조하세요.

- _errors_는 인코딩 오류 처리 방법을 제어합니다.기본값인 ``엄격``인 경우, ``유니코드 에러``(https://docs.python.org/ko/3.12/library/exceptions.html#UnicodeError “유니코드 에러”) 예외가 발생합니다. 다른 가능한 값으로는 ``무시``, ``대체``, ``xmlcharrefreplace``, ``백슬래시대체`` 및 [`codecs.register_error()`](https://docs.python.org/ko/3.12/library/codecs.html#codecs.register_error “codecs.register_error”)를 통해 등록된 다른 이름 등이 있습니다. 자세한 내용은 [에러 처리기](https://docs.python.org/ko/3.12/library/codecs.html#error-handlers)를 참조하세요.
- 성능상의 이유로 인코딩 오류가 실제로 발생하거나 [파이썬 개발 모드](https://docs.python.org/ko/3.12/library/devmode.html#devmode)가 활성화되어 있거나 [디버그 빌드](https://docs.python.org/ko/3.12/using/configure.html#debug-build)가 사는 한 _errors_ 값의 유효성을 검사하지 않습니다.

버전 3.1에서 변경: 키워드 인자 지원이 추가되었습니다.

버전 3.9에서 변경: The value of the _errors_ argument is now checked in [파이썬 개발 모드](https://docs.python.org/ko/3.12/library/devmode.html#devmode) and in [debug mode](https://docs.python.org/ko/3.12/using/configure.html#debug-build).

### `str.expandtabs(_tabsize=8_)`

- 모든 탭 문자들을 현재의 열과 주어진 탭 크기에 따라 하나나 그 이상의 스페이스로 치환한 문자열의 복사본을 돌려줍니다. 탭 위치는 _tabsize_ 문자마다 발생합니다 (기본값은 8이고, 열 0, 8, 16 등에 탭 위치를 지정합니다). 문자열을 확장하기 위해 현재 열이 0으로 설정되고 문자열을 문자 단위로 검사합니다. 문자가 탭 (`\t`) 이면, 현재 열이 다음 탭 위치와 같아질 때까지 하나 이상의 스페이스 문자가 삽입됩니다. (탭 문자 자체는 복사되지 않습니다.) 문자가 개행 문자 (`\n`) 또는 캐리지 리턴 (`\r`) 이면 복사되고 현재 열은 0으로 재설정됩니다. 다른 문자는 변경되지 않고 복사되고 현재 열은 인쇄할 때 문자가 어떻게 표시되는지에 관계없이 1씩 증가합니다.

```python
>>> '01\t012\t0123\t01234'.expandtabs()
'01      012     0123    01234'
>>> '01\t012\t0123\t01234'.expandtabs(4)
'01  012 0123    01234'
```

[string — Common string operations — Python 3.12.5 문서](https://docs.python.org/ko/3.12/library/string.html)


---
## 참조

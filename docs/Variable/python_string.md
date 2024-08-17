---
title: "[Python] 문자열 (String)"
excerpt: 
categories:
  - Python
tags:
  - Python
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

## f-문자열 (f-string)
> [2. 어휘 분석 — Python 3.12.5 문서](https://docs.python.org/ko/3.12/reference/lexical_analysis.html#f-strings)




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

---
title: "[Python] 파이썬"
excerpt: 
categories:
  - Python
tags:
  - Python
  - Comment
  - Operator
last_modified_at: 2024-04-11T15:10:55+09:00
link: https://docs.python.org/ko/3/
상위 항목:
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

**하위 항목**
- 
---

## 주석 (Comment)

```python
# 이 문장은 주석입니다.
```

- `#` 기호를 사용하여 주석을 작성할 수 있습니다.

## 변수 (Variable)
```python
variable = value
```

- 메모리에 존재하는 대상들을 객체라고 합니다.
- 데이터 값을 가리키는 객체, 가리키는 대상이 변할 수 있습니다.
- Python 에서는 Function, Class 등 모든 것을 객체로 나타냅니다.
- 변수에 저장된 값으로 스스로 판단하여 자료형을 지정합니다.


### 변수명 규칙

- 첫 글자는 반드시 영문 대소문자 혹은 `_` 로 시작해야 합니다. (`_` 시작은 특별한 경우에만 사용)
- 나머지 글자들은 영문자, 숫자 혹은 `_` 로 구성해야 합니다.
- 대소문자를 구분합니다.
- 길이에 대한 제약이 없습니다.
- `if`, `else` 와 같이 Python 에서 예약어 (Keyword) 로 사용하는 경우 변수명으로 사용할 수 없습니다.

> 짧게 축약하기보다는 변수명 자체가 의미를 갖는 것이 좋습니다.

### 변수 입력

- `a, b = (x, y)` 와 같이 tuple 을 이용하여 값을 입력할 수도 있습니다. `(a, b) = x, y` 도 가능합니다.
- `[a, b] = [x, y]` 처럼 list 를 이용하는 것도 가능합니다.
- `a = b = 'abc'` 처럼 여러 변수에 같은 값을 대입할 수 있습니다.
- `a, b = b, a` 로 변수 값을 변경할 수 있습니다. 가리키는 변수가 바뀌면서 주소도 서로 바뀝니다.

### 심화: 주소

- 변수가 저장된 주소는 `id(VARIABLE)` 로 확인할 수 있다.

```python
# 아래는 주소가 같게 나타난다.
a = [1,2,3]
b = a

# 아래는 주소가 달라진다.
b = a[:]

b = a.copy()

from copy import copy
b = copy(a)
```

- List, Tuple 등의 자료형의 경우 같은 객체를 가리키는 변수 중 하나의 값이 변하면 다른 변수도 값이 변하지만 변수의 주소는 똑같이 유지된다. (String, Number 는 주소도 달라진다.)
- 위 코드를 실행할 경우 `a` 와 `b` 가 가리키는 list 객체는 동일하며 둘 중 하나의 값이 변하기 전까지는 주소 역시 동일하다.
- `b = a[:]` 와 같이 Index 를 사용하여 선언할 경우 가리키는 값이 같더라도 주소는 다르게 나타난다. (`a` 자체가 아닌 `a` 의 내용을 복사하여 새로 선언하게 된다.)

```python
from copy import copy
copy()
```

- copy 함수, 모듈을 사용해도 주소가 다른 변수를 선언할 수 있다.

### 심화: 비교

```python
var1 = 'Python'
var2 = 'Python'

# 변수 데이터 값 비교
print(f"var1 == var2: {var1 == var2}") # True

# 객체 비교
print(f"var1 is var2: {var1 is var2}") # False

# 주소 비교
print(f"id(var1): {id(var1)}")
print(f"id(var2): {id(var2)}")
```

- `var1 = 'Python'` 는 `var1` 이라는 변수에 'Python' 이라는 값을 할당한다는 뜻이다. `var2` = `var1` 은 `var2` 에 `var1` 을 할당한다는 뜻이다. (순서가 중요하다.)
- `is` 로 같은 객체인지 비교할 수 있다. 값이 같더라도 두 변수가 서로 다른 메모리 주소에 저장되므로 서로 다른 객체이다.

> 위 예제를 실행했을 때 `var1` 과 `var2` 의 주소가 같게 나타나는 경우가 있다. 이는 Python 내에서 메모리 낭비를 최소화하기 위해 가능한 경우 같은 객체를 가리키도록 설계됐기 때문이다. 둘 중 하나의 변수 값을 변경하면 두 변수의 주소가 달라지므로 동작에 차이는 없다. 메모리 절약을 위한 Python 자체 기능이 있고, 이로 인해 발생하는 현상이라고만 알아두면 된다.

## 데이터 타입 (Data Type)
### 숫자 (Numeric)

```python
i = 12
print(i) # int, 결과: 12

f = 1.23
print(f) # float, 결과: 1.23
```

- Python 은 정수를 `int` 로 나타낸다. (나타낼 수 있는 최대 길이에 제한이 없다.)
- 실수 타입은 `float`, 복소수 타입은 `complex` 로 나타낸다.
- `-x` 와 같이 `-` 를 붙이면 음수로 나타낼 수 있다.

| 산술 연산자       | 의미                                |
| ------------ | --------------------------------- |
| `+`          | 덧셈                                |
| `-`          | 뺄셈                                |
| `*`          | 곱셈                                |
| `**`         | 제곱                                |
| `/`          | 나눗셈                               |
| `//`         | 몫                                 |
| `%`          | 나머지                               |
#### 대입 연산자 (Assignment Operator)
- 변수를 선언하고 값을 할당할 때 사용합니다.

| 연산자   | 내용                      |
| ----- | ----------------------- |
| `=`   | 좌변에 우변 값 할당             |
| `+=`  | 좌변 값에 우변 값을 더하여 할당      |
| `-=`  | 좌변 값에 우변 값을 빼서 할당       |
| `*=`  | 좌변 값에 우변 값을 곱해서 할당      |
| `/=`  | 좌변 값에 우변 값을 나눠서 할당      |
| `%=`  | 좌변 값을 우변 값으로 나눈 나머지 할당  |
| `//=` | 좌변 값을 우변 값으로 나눈 몫 할당    |
| `**=` | 좌변 값을 우변 값으로 지수 연산하여 할당 |

### 논리 (Boolean)

```python
b = True
print(b) # 결과: True
```

- 참과 거짓을 표현하는 데이터 타입, `bool` 로 나타낸다.
- 위 연산자의 결과에 따라 `True` 와 `False` 로 반환한다.
- `is`, `is not` 의 경우 단순히 값이 같은 것 뿐만 아니라 같은 메모리 주소에 할당된 같은 객체인지 확인한다.

| 비교 연산자 | 의미 |
| ---- | ---- |
| `x > y` | x 가 y 보다 큰지 여부 |
| `x >= y` | x 가 y 보다 크거나 같은지 여부 |
| `x < y` | x 가 y 보다 작은지 여부 |
| `x <= y` | x 가 y 보다 작거나 같은지 여부 |
| `x == y` | x 와 y 가 같은지 여부 |
| `x!= y` | x 와 y 가 다른지 여부 |
| `x is y` | x 와 y 가 같은 객체인지 여부 |
| `x is not y` | x 와 y 가 다른 객체인지 여부 |

| 논리 연산자 | 의미                   |
| ----------- | ---------------------- |
| `x or y`    | x 또는 y 가 `True` 인가? |
| `x and y`   | x 와 y 모두 `True` 인가? |
| `not x`     | x 가 `True` 라면 `False`, `False` 라면 `True` 를 반환한다.                       |



#### 심화: Any
- 반복 가능한 자료형의 모든 데이터에 대해 bool(x)가 True이면 True를 반환합니다. 이터러블이 비어 있으면 False를 반환합니다.

### 컬렉션 자료형 (Collection Data Type)
- 여러 값을 저장하는 자료형입니다. 반복 가능한 자료형 (Iterable)이라고도 합니다.
- 시퀀스 자료형과 비시퀀스 자료형이 있습니다.
- 시퀀스 자료형은 문자열형, 리스트형, 튜플형이 있고 비시퀀스형 자료형은 세트형, 딕셔너리형이 있습니다.

| 괄호의 종류 | 의미                                |
| ------ | --------------------------------- |
| `()`   | 무언가를 호출할 때 ==값을 전달하는 용도==로 사용합니다. |
| `[]`   | 대상에 ==인덱스로 접근==할 때 사용합니다.         |

#### 문자열 (String)

```python
hello = "Hello"
world = "World"
print(hello + world)
```
- 문자열끼리 덧셈을 실행하면 붙어있는 문자열이 출력됩니다.

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

데이터가 여러 문자로 구성된 타입, `str` 로 나타낸다.
다른 문자와 연결하거나 포함된 문자열의 길이를 확인할 수 있다.
`'` 또는 `"` 으로 감싸면 문자열로 인식된다.
여러 줄일 경우 `'''` 나 `"""` 로 감싸면 된다. 하지만 가독성이 떨어지므로 1 줄 씩 나타내는 것을 권장한다.


##### 이스케이프 문자 (Escape String)
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


##### `+` 연산자

```python
print("Hello," + "World") # 결과: "Hello, World"
print("Repeat " * 3) # 결과: "Repeat Repeat Repeat "
print("Hey, " + ("Fighting! " * 3) ) # 결과: Hey, Fighting! Fighting! Fighting! 
```

문자열에 `+` 를 사용하면 두 문자열을 합친 결과가 나타난다.
문자열에 `*` 를 사용하면 해당 문자열이 숫자만큼 반복된다.
`()` 도 사용할 수 있다. 우선 순위는 숫자 연산의 `()` 와 같게 적용된다.

##### 인덱스 (Index)
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

##### 심화: 함수
###### `len`

```python
print(len("Hello")) # 결과: 5
```

- `len(STRING)` 은 입력한 `STRING` 의 길이를 반환한다.

###### `replace`

```python
# "A"를 "F"로 변환
message.replace("A", "F")
```

- `replace(FROM, TO)` 는 문자열에 존재하는 `FROM` 을 `TO` 로 바꿔준다.
- 문자열 내에 `FROM` 이 존재하지 않으면 오류가 발생한다.

###### `join`

```python
# join()의 대상 문자열을 기준으로 합쳐준다.
phone_number_segments = ["010","0000","1111"]
print("-".join(phone_number_segments)) # 결과: "010-0000-1111"
```

- `join(TARGET)` 로 `TARGET` 의 구분자에 함수를 호출한 문자열을 삽입한다.

###### `split`

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

###### `with`

```python
a = "Python is easy!"
print(a.startswith("Python")) # 결과: True
print(a.endswith("!")) # 결과: True
```

- `startswith()` 은 대상이 입력한 문자열로 시작하는지 확인한다.
- `endswith()` 은 대상이 입력한 문자열로 끝나는지 확인한다.

###### `strip`

```python
message.strip()
```

- `strip()` 은 문자열 양 옆의 공백을 제거한다.
- 문자열 중간의 공백은 그대로 남는다.

###### Capitalize

- `lower()` 는 영어를 모두 소문자로 변환한다.
- `casefold()` `lower()` 메소드와 유사하지만, 더 강력한 소문자 변환 기능을 제공하여 다양한 언어에서의 문자 변환에 있어 더욱 일관된 결과를 보장합니다. [`casefold()`](vscode-file://vscode-app/c:/Users/skysk/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html "../../../.vscode/extensions/ms-python.vscode-pylance-2024.6.1/dist/typeshed-fallback/stdlib/builtins.pyi")는 문자열을 정규화하여 대소문자 구분 없이 문자열 비교를 수행할 때 유용하게 사용됩니다.
  예를 들어, 일부 유럽 언어에서는 특정 대문자 문자가 두 개 이상의 소문자 문자로 변환될 수 있습니다. 이러한 경우, `lower()` 메소드보다 [`casefold()`](vscode-file://vscode-app/c:/Users/skysk/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html "../../../.vscode/extensions/ms-python.vscode-pylance-2024.6.1/dist/typeshed-fallback/stdlib/builtins.pyi") 메소드가 더 정확한 소문자 변환을 제공합니다.
- `upper()` 는 영어를 모두 대문자로 변환한다.
- `capitalize()` 는 앞 글자만 대문자로 바꾸고 나머지는 소문자로 바꾼다.

###### Format

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


#### 리스트 (List)

```python
list_name = ["variable1", "variable2", 3, 4]
list_name.remove(3)
```

- `remove(variable)` 함수를 사용하면 `variable`을 list에서 제거할 수 있습니다.
```python
LIST_A = [1, True, "a"]
LIST_B = list([1, True, "a"])
print(LIST_A) # 결과: [1, True, "a"]
print(LIST_B) # 결과: [1, True, "a"]
```

- `list` 타입으로 `list()` 함수를 사용해도 생성할 수 있습니다.
- 여러 값을 동일 변수에 순차적으로 저장할 수 있습니다. 여러 타입의 변수를 한 번에 저장할 수 있습니다.
- 크기가 가변적으로 변하는 선형 리스트 성질을 갖고 있습니다.
- 일반적으로 동일한 (homogeneous) 데이터 타입으로 이루어진 항목들을 순차적으로 추출하는 용도로 사용합니다.

```python
LIST_EMPTY_A = []
LIST_EMPTY_B = list()
```

- `[]` 로 빈 배열을 할당하거나 `list()` 로 입력 없이 함수를 사용하면 빈 리스트가 생성됩니다.

| 메서드            | 설명                                                                                     |
| -------------- | -------------------------------------------------------------------------------------- |
| `append(x)`    | 리스트 마지막 요소 뒤에 값 `x` 추가                                                                 |
| `clear()`      | 리스트 모든 항목 삭제                                                                           |
| `copy()`       | 리스트 복사                                                                                 |
| `count(x)`     | 리스트의 `x` 항목 개수 반환                                                                      |
| `extend(i)`    | 리스트 마지막에 컬렉션 자료형 `i`를 추가                                                               |
| `index(x)`     | `x` 항목의 인덱스 번호 반환<br>같은 값이 여러 개 있을 경우 가장 앞에 있는 인덱스 반환<br>값이 존재하지 않을 경우 `ValueError` 발생 |
| `insert(i, x)` | 리스트의 `i` 인덱스에 `x` 삽입                                                                   |
| `pop()`        | 리스트 마지막 항목을 삭제하고 반환                                                                    |
| `remove(x)`    | 리스트에서 `x`를 제거<br>같은 값이 여러 개 있을 경우 가장 앞에 있는 값 제거                                        |
| `reverse()`    | 리스트의 위치를 역순으로 변경                                                                       |
| `sort()`       | 리스트 항목들을 정렬                                                                            |

##### 인덱스 (Index)
<img src="https://dschloe.github.io/img/python/basic_syntax/python-list-index.png" style="width: 600px" />
저장된 데이터는 자동으로 **색인(index)** 이 생긴다.
index는 좌측 기준 0부터 시작하며 음수를 사용할 경우 우측 기준 -1부터 시작한다.

```python
List = [1, 2, 3, 4, 5]
print(List[0:3]) # 결과: [1, 2, 3], List[:3]과 동일하다.
print(List[2:5]) # 결과: [3, 4, 5], List[2:]와 동일하다.
print(List[:]) # 결과: [1, 2, 3, 4, 5]
```

`[start:end]` 로 리스트의 여러 값을 indexing 할 수 있다.
`start` 는 indexing 을 시작할 index 를 나타낸다. 해당 위치의 값도 포함된다. index 를 지정하지 않으면 시작 위치 (0) 으로 지정된다.
`end` 는 indexing 을 마칠 index 를 나타낸다. 해당 위치의 값은 포함되지 않으므로 위의 `List[2:5]` 처럼 나타내려는 Index 보다 1 더 크게 지정해야 한다. index 를 지정하지 않으면 마지막 위치로 지정된다. (위의 경우 5 에 해당)

```python
List = [1, 2, 3, 4, 5]
List_copy = List
List_copy.append(6)
print(f"List_copy: {List_copy}") # 결과: [1, 2, 3, 4, 5, 6]
print(f"List: {List}") # 결과: [1, 2, 3, 4, 5, 6]

List_copy = List[:]
List_copy.remove(6)
print(f"List_copy: {List_copy}") # 결과: [1, 2, 3, 4, 5]
print(f"List: {List}") # 결과: [1, 2, 3, 4, 5, 6]
```

`List` [[#심화 주소|객체를 직접 할당]] 하면 같은 주소를 가리키면서 예상치 못한 문제가 발생할 수 있다.
`List[:]` 는 `List` 의 전체 값을 Indexing 한다. 이를 이용하여 복사에 사용할 수 있다.


```python
List = [1, 2, 3, 4, 5]
List[0] = 0
print(List) # 결과: [0, 2, 3, 4, 5]
```

Index 를 사용하여 기존 값을 변경할 수 있다.

```python
List = [1, 2, 3, 4, 5]
List[5] = 6 # 결과: Error
```

Index 를 벗어나는 값을 할당하려고 할 경우 에러가 발생한다.
새로운 값을 추가하기 위해서는 `append()` 함수를 사용해야 한다.

##### 리스트의 `+` 연산
```python
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(a+b) # 결과: [1, 2, 3, 4, 5, 6]
```

`+` 연산자로 두 리스트를 합친 새로운 객체를 생성할 수 있다.
기존 객체에 값을 더하려면 `extend()` 함수를 사용해야 한다.

##### 중첩 리스트

```python
NESTED_LIST = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(NESTED_LIST) # 결과: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

SUB_LIST1 = [1, 2, 3]
SUB_LIST2 = [4, 5, 6]
SUB_LIST3 = [7, 8, 9]
MAIN_LIST = [SUB_LIST1, SUB_LIST2, SUB_LIST3]
print(MAIN_LIST) # 결과: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

리스트 타입은 리스트 타입을 저장할 수 있다. 이를 중첩 리스트라 한다.

```python
NESTED_LIST = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(NESTED_LIST[1]) # 결과: [4, 5, 6]
print(NESTED_LIST[1][1]) # 결과: 5
```

중첩 리스트의 경우 Index `[]` 를 1 번 사용하면 내부의 리스트가 반환되고, `[][]` 와 같이 2 번 사용하면 반환된 리스트에서 Index 에 맞는 값을 가져온다.

##### 심화: 함수
###### `append`

```python
List = [1, 2, 3]
List.append(4)
print(List) # 결과: [1, 2, 3, 4]
```

- `append(INPUT)` 로 List 의 맨 뒤에 `INPUT` 을 추가할 수 있다.

###### `insert`

```python
List = [1, 2, 3, 4]
List.insert(2, 0)
print(List) # 결과: [1, 2, 0, 3, 4]
```

- `insert(INDEX, INPUT)` 로 특정 Index 에 값을 추가할 수 있다. `INDEX` 위치에 `INPUT` 을 추가한다.

###### `extend`

```python
List = [1, 2, 3]
additional_list = [4, 5, 6]
List.extend(additional_list)
print(List)
```

###### `remove`

```python
List = [1, 2, 3, 4, 1]
List.remove(1)
print(List) # 결과: [2, 3, 4, 1]
```

- `remove(INPUT)` 로 List 에 존재하는 `INPUT` 을 제거할 수 있다.
- Index 를 앞에서부터 탐색하여 가장 먼저 나오는 값을 제거한다.
- List 내에 존재하지 않는 값을 제거 시도할 경우 오류가 발생한다.

###### `pop`

```python
List = ["a", "b", "c", "d", "e"]
print(List.pop(3)) # 결과: "d"
```

- `pop(INDEX)` 로 `INDEX` 에 위치한 값을 제거하면서 동시에 반환할 수 있다.
- `INDEX` 를 입력하지 않으면 마지막 위치에 존재하는 값을 제거하고 반환한다.

###### `del`

```python
List = [1, 2, 3, 4, 5, 6]
del List[2]
print(List) # 결과: [1, 2, 4, 5, 6]
```

- `del <List>[INDEX]` 로 `List` 객체의 `INDEX` 위치에 있는 값을 제거할 수 있다.
- `pop` 과 달리 제거한 값을 반환하지 않는다.
- `remove` 는 제거할 값을 입력하고 `del` 은 제거할 Index 를 입력한다는 차이점이 있다.

###### `len`

```python
List = [1, 2, 3, 4, 5]
print(len(List)) # 결과: 5
```

- `len(LIST)` 을 사용하면 `LIST` 의 길이가 반환된다.




#### 튜플 (Tuple)

```python
TUPLE_A = '배트맨', 1989, '슈퍼맨II' , 1980
TUPLE_B = ('배트맨', 1989, '슈퍼맨II' , 1980)
TUPLE_C = tuple(['배트맨', 1989, '슈퍼맨II' , 1980])

print(TUPLE_A)
print(TUPLE_B)
print(TUPLE_C)

TUPLE_A[3] = 1981 # 에러 발생
```

- 처음 객체를 생성하면 이후에는 내부의 값 변경이 불가능한 자료 구조입니다. 값 변경이 불가능한 것 외에는 List 와 유사합니다.
- 일반적으로 서로 다른 (heterogeneous) 종류의 데이터 타입으로 이루어진 항목들을 변수에 바로 할당하는 Unpacking 이나 Indexing 용도로 사용합니다.
- 열거형 데이터가 필요할 때 값의 변경이 필요하지 않을 경우 List 보다 Tuple 타입을 사용하는 것이 속도가 빨라 성능에 더 유리합니다.
- `()` 로 감싸거나 괄호를 사용하지 않고 `,` 를 사용하여 Tuple 을 생성할 수 있으며 `tuple()`로도 생성할 수 있습니다.

```python
TUPLE_EMPTY_A = () # Tuple 타입
TUPLE_EMPTY_B = tuple() # Tuple 타입
TUPLE_A = 'Hello', # Tuple 타입
NOT_TUPLE = ('Hello') # String 타입
```

빈 Tuple 을 생성할 경우 `()` 만 할당하거나 `tuple()` 을 사용하면 된다.
하나의 값만 할당할 경우 끝에 `,` 를 사용해야 한다. `,` 를 붙이지 않거나 하나의 값에 `()` 를 사용할 경우 입력한 값의 타입으로 생성된다.

```python
TUPLE_A = [1, 2, 3], [4, 5, 6]
TUPLE_A[1][2] = 7
print(TUPLE_A) # 결과: [1, 2, 3], [4, 5, 7]
```

Tuple 에 포함된 값은 변경이 불가능하지만 리스트를 값으로 가질 경우 리스트 내부의 값은 변경할 수 있다.
Tuple 이 값으로 갖는 것은 List 의 주소이다. List 는 값이 변경한 자료 구조이므로 내부 값을 변경해도 Tuple 의 규칙에 위배되지 않는다.

##### Unpacking

```python
TUPLE_A = '배트맨', 1989, '슈퍼맨II' , 1980
a, b, c, d = TUPLE_A
print(a) # 결과: '배트맨'
print(b) # 결과: 1989
print(c) # 결과: '슈퍼맨II'
print(d) # 결과: 1980
```

위의 `TUPLE_A` 처럼 여러 값들을 하나의 변수에 할당하는 것을 **Packing**이라고 한다.
`a, b, c, d = TUPLE_A` 처럼 Packing 한 변수를 활용하여 여러 변수에 동시에 값을 할당하는 것을 **Unpacking**이라 한다.

#### 집합 (Set)

```python
SET = {'C++', 'Java', 'Python'}
SET_EMPTY = set()
```

Index 가 없으며 중복이 허용되지 않는 데이터 집합이다. Index 가 없으므로 순서가 존재하지 않는다. 주로 중복된 값을 제거할 때 사용한다.
`set()` 를 사용하거나 `{VALUE1, VALUE2}` 와 같이 `{}` 를 사용하여 생성할 수 없다.
Dictionary 의 생성 문법과 겹쳐서 `{}` 만으로는 빈 Set 를 생성할 수 없다. `set()` 로만 빈 Set 를 생성할 수 있다.

```python
SET_A = set('abacadaeafag') # 결과: {'a',' 'b, 'c', 'd', 'e', 'f', 'g'}
SET_B = set('alacazam') # 결과: {'a', 'l', 'c', 'z', 'm'}

print(SET_A | SET_B) # 합집합, 결과: {'g', 'm', 'a', 'b', 'l', 'd', 'z', 'c', 'f', 'e'}
print(SET_A & SET_B) # 교집합, 결과: {'a', 'c'}
print(SET_A - SET_B) # 차집합, 결과: {'g', 'b', 'd', 'f', 'e'}
print(SET_A ^ SET_B) # 여집합, 결과: {'g', 'm', 'l', 'd', 'z', 'e', 'f', 'b'}
```

수학의 합집합 (`|`), 교집합 (`&`), 차집합 (`-`), 여집합 (`^`) 을 구현할 수 있다.

| 메서드                     | 설명           |
| ----------------------- | ------------ |
| `add(값)`                | 값 추가         |
| `update([값1, 값2, ...])` | 여러 값 한 번에 추가 |
| `remove(값)`             | 특정 값 제거      |

#### 딕셔너리 (Dictionary)

```python
DICTIONARY_A = {'blue': 3, 'red': 4, 'green': 5}
DICTIONARY_B = dict([('brown', 3), ('gray', 7)])
DICTIONARY_C = dict(brown=3, gray=7)
DICTIONARY_EMPTY_A = {} # Dictionary 타입
DICTIONARY_EMPTY_B = dict() # Dictionary 타입
```

다른 언어에서는 Map 타입으로 부른다. String 타입이나 숫자 타입과 같이 변경 불가능한 타입 (Immutable) 을 Key 로 지정하여 Index 로 사용한다.
다른 타입처럼 숫자 Index 가 자동으로 적용되지 않으므로 순서가 존재하지 않는다.
Tuple 타입이 내부 값으로 변경 불가능한 타입 (Immutable) 의 값만 가질 경우 Key 로 사용할 수 있다. (List 등 변경 가능한 타입의 값을 가진다면 Key 로 사용할 수 없다. Key 는 변경되면 안되기 때문이다.)
`key:value` 와 같이 `:` 를 사용하여 표기한다. 각 쌓은 `,` 로 구분하며 `{}` 로 감싸서 선언한다. 혹은 `dict` 함수를 사용하여 생성할 수 있다. 이 경우 Key 와 Value 가 구분되도록 입력해야 한다.
숫자로는 값들을 구분하기 힘들 때 주로 사용한다. 단순한 숫자 Index 로도 충분할 경우 Dictionary 타입은 오히려 성능에 악영향을 준준다.

```python
DICTIONARY_A = {'blue': 3, 'red': 4, 'green': 5}
print(DICTIONARY_A['blue']) # 결과: 3

DICTIONARY_A['black'] = 1
print(DICTIONARY_A) # 결과: {'blue': 3, 'red': 4, 'green': 5, 'black' = 1}

del DICTIONARY_A['green']
print(DICTIONARY_A) # 결과: {'blue': 3, 'red': 4, 'black' = 1}

DICTIONARY_A['black'] = 5
print(DICTIONARY_A) # 결과: {'blue': 3, 'red': 4, 'black' = 5}
```

`DICTIONARY[KEY] = VALUE` 로 새로운 값을 추가할 수 있다.
`del DICTIONARY[KEY]` 로 `KEY` 를 갖는 쌍을 제거할 수 있다.
기존에 있던 `KEY` 에 새로운 값을 할당하면 기존 값을 변경할 수 있다.

```python
DICTIONARY_A = {'blue': 3, 'red': 4, 'green': 5}
print(3 in DICTIONARY_A) # 결과: False
```

`in` 을 사용할 경우 key 값을 기준으로 참/거짓을 판단한다.

### 타입 변환

```python
var1 = "Python"
print(type(var1)) # var1의 타입 반환: <class 'str'> 
```

`type()` 로 입력한 변수의 타입을 확인할 수 있다.

```python
i = int("123") # 결과: 123
s = str(123) # 결과: "123"
f = float("123.45") # 결과: 123.45
c = complex(1.1,2.2) # 결과: 1.1+2.2j
```

## 제어문 (Control)
Python 의 제어문은 다른 언어의 `{ }` 대신 `:` 과 **들여쓰기**로 처리합니다.

| 연산자 / 예약어  | 설명                |
| ---------- | ----------------- |
| x < y      | x 가 y 보다 작다.      |
| x > y      | x 가 y 보다 크다.      |
| x == y     | x 와 y 가 같다.       |
| x != y     | x 와 y 가 같지 않다.    |
| x >= y     | x 가 y 보다 크거나 같다.  |
| x <= y     | x 가 y 보다 작거나 같다.  |
| x or y     | x 또는 y 가 참이면 참    |
| x and y    | x 와 y 가 모두 참이면 참  |
| not x      | x 가 거짓이면 참        |
| x in A     | x 가 A 의 요소로 있으면 참 |
| x not in A | x 가 A 의 요소가 아니면 참 |

> [!NOTE] `in`
> 
> ```python
> LIST = [1, 2, 3, 4]
> print(2 in LIST) # 결과: True
> ```
> 
> - 열거형 데이터에는 `in` 을 사용할 수 있다. 해당 데이터에 입력한 값이 존재하면 `True`, 이외에는 `False` 를 반환한다.

### 조건문 (Condition)

#### `if`

```python
if 조건문:
	<실행할 문장>
elif 조건문:
	<실행할 문장>
elif 조건문:
	<실행할 문장>
else:
	<실행할 문장>
```

- if 문에 속하는 문장에는 모두 들여쓰기 (indentation) 를 해야 합니다. 들여쓰기 정도를 통일시켜야 합니다. (커뮤니티에서는 Spacebar 4 번을 권장합니다.)
- 위에서부터 조건을 확인하여 처음으로 만족한 블록만 실행합니다.
- 모든 조건을 만족하지 못했을 경우 `else` 블록이 실행됩니다.

```python
if 조건문1:
    if 조건문 2:
        <실행할 문장 1>
    <실행할 문장 2>
else:
    <실행할 문장 3>
```

- `if` 조건문 내에 또 다른 `if` 조건문을 사용할 수 있다.

```python
if 조건문: <실행할 문장>
<조건문이 참일 때 실행할 문장> if 조건문 else <조건문이 거짓일 때 실행할 문장>
```

- `if` 조건문을 한 줄로 나타내고 싶을 경우 위처럼 사용할 수 있다.

```python
message = "success" if score >= 60 else "failure" # 60 이상이면 success, 미만이면 failure가 할당
```

- 변수에 값을 할당할 때 `if` 조건문의 결과를 적용할 수 있다.

```python
if not line: break
```

- `if` 의 조건에 `not` 을 적용할 수 있다.

### 반복문 (Loop)

#### `while`

```python
while 조건문:
    실행할 문장1
    실행할 문장2
    실행할 문장3
```

- 조건문을 만족하는 동안 계속 실행한다. (조건문을 만족하지 않으면 한 번도 실행하지 않는다.)
- 조건문을 True 로 두면 무한 루프를 만들 수 있다. (Python IDLE 에서는 Ctrl + C 로 빠져나갈 수 있다.)

#### `for`

```python
for <value> in <iterable>:
	수행할 문장1
	수행할 문장2
```

- `<value>` 에 `list`, `tuple`, `string` 과 같은 `iterable` 에서 값들을 순서대로 `value` 에 대입하여 반복한다.
- 특히 `range` 함수와 함께 자주 쓰인다.

> [!NOTE] `range`
> `for` 반복문에 많이 사용된다. `for({start}, end, {step})` 의 문법을 갖는다.
>
> ```python
> range(5) # 0부터 4까지의 정수
> range(1, 10) # 1부터 9까지의 정수
> range(10, 1, -2) # 10부터 2까지 -2씩 감소
> ```

```python
for <value1> in <iterable1>:
    for <value2> in <iterable2>:
        실행할 문장
```

- `for` 반복문 역시 중첩으로 사용할 수 있다.

```python
# 리스트 내포
[표현식 for <value> in <iterable> if 조건문]

# 리스트 내포 (for 문 여러 개)
[표현식 for <value>1 in <iterable1> if 조건문1
표현식 for <value>2 in <iterable2> if 조건문2
표현식 for <value>n in <iterable3> if 조건문n]
```

- `for` 문을 이용하여 리스트에 값을 바로 입력할 수 있다. (리스트 내포)
- 하나의 리스트에 `for` 문을 여러 개 사용할 수도 있다.

```python
squares = []
for x in range(10):
	squares.append(x**2)

new_squares = [y**2 for y in range(10)]
```

- 리스트에 값을 입력할 경우 리스트 내포를 활용하는 것이 더 유리하다.
- 위에서 반복문이 종료된 후에도 `x` 에는 값 9 가 할당된 상태로 유지되며 메모리에 남아서 성능에 영향을 주거나 예상치 못한 버그를 일으킬 수 있다.
- 이에 비해 `y` 의 경우 `for` 반복문이 종료되면 메모리에서 해제되므로 성능 문제나 버그를 방지할 수 있다.

```python
SET = {x for x in 'abracadabra' if x not in 'abc'}
pairs = [(a, b) for a in A for b in B if a! = b]
```

- `SET` 처럼 `for` 문장도 한 줄로 표현할 수 있다.
- 또한 `pairs` 처럼 중첩 `for` 반복문도 한 줄로 나타낼 수 있다.

```python
DICT = {x: x**2 for x in (2, 4, 6)}
```

- Dictionary 타입도 `for` 반복문을 사용하여 생성할 수 있다. 단, `key:value` 를 어떻게 생성할 것인지 나타내야 한다.

#### `break`

```python
for value in range(5):
    if LIST[x] == "Yellow":
        break
		print("이 문장은 실행되지 않습니다.")
```

- `break` 를 실행하면 `iterable` 에 남아있는 값과 상관 없이 해당 반복문이 종료된다.

#### `continue`

```python
for value in range(5):
    if LIST[x] == "Yellow":
        continue
	print("continue가 실행되면 이 문장은 실행되지 않습니다.")
```

- `continue` 가 실행되면 해당 `value` 에 대한 반복문은 종료하고 `iterable` 의 다음 값을 `value` 에 대입하여 반복문을 이어간다.

#### `pass`

```python
for value in range(5):
    if LIST[x] == "Yellow":
        pass
	else:
		print("pass가 실행되지 않으면 이 문장이 실행됩니다.")
```

- `pass` 는 아무 문장도 실행하지 않는다. 특정 조건을 충족했을 때 아무 문장도 실행하지 말아야 할 경우에 주로 활용된다.


## 입출력
```python
variable = input("설명 메시지")
```
- `input`은 입력한 값을 문자열 (`str`) 타입으로 저장합니다.
- `"설명 메시지"`는 설명을 위해 출력할 메시지를 결정합니다.
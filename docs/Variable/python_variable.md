---
title: "[Python] 변수 (Variable)"
excerpt: 
categories:
  - Python
tags:
  - Python
  - Variable
  - Pointer
  - Data-Type
  - Data-Type-List
  - Data-Type-Tuple
  - Data-Type-Set
  - Data-Type-Dictionary
last_modified_at: 2024-04-11T15:10:55+09:00
link: 
상위 항목: "[[python_home|파이썬 (Python)]]"
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

**하위 항목**
- [[python_list|파이썬 리스트 (Python List)]]
- [[python_string|파이썬 문자열 (Python String)]]

---

```python
variable = value
```

- 메모리에 존재하는 대상들을 객체라고 합니다.
- 데이터 값을 가리키는 객체, 가리키는 대상이 변할 수 있습니다.
- Python 에서는 Function, Class 등 모든 것을 객체로 나타냅니다.
- 변수에 저장된 값으로 스스로 판단하여 자료형을 지정합니다.


## 변수명 규칙

- 첫 글자는 반드시 영문 대소문자 혹은 `_` 로 시작해야 합니다. (`_` 시작은 특별한 경우에만 사용)
- 나머지 글자들은 영문자, 숫자 혹은 `_` 로 구성해야 합니다.
- 대소문자를 구분합니다.
- 길이에 대한 제약이 없습니다.
- `if`, `else` 와 같이 Python 에서 예약어 (Keyword) 로 사용하는 경우 변수명으로 사용할 수 없습니다.

> 짧게 축약하기보다는 변수명 자체가 의미를 갖는 것이 좋습니다.

## 변수 입력

- `a, b = (x, y)` 와 같이 tuple 을 이용하여 값을 입력할 수도 있습니다. `(a, b) = x, y` 도 가능합니다.
- `[a, b] = [x, y]` 처럼 list 를 이용하는 것도 가능합니다.
- `a = b = 'abc'` 처럼 여러 변수에 같은 값을 대입할 수 있습니다.
- `a, b = b, a` 로 변수 값을 변경할 수 있습니다. 가리키는 변수가 바뀌면서 주소도 서로 바뀝니다.

### 논리 연산자 할당
- 논리 연산자 `and` 와 `or` 는 소위 _단락-회로(short-circuit)_ 연산자입니다: 인자들은 왼쪽에서 오른쪽으로 값이 구해지고, 결과가 결정되자마자 값 구하기는 중단됩니다. 예를 들어, `A` 와 `C` 가 참이고 `B` 가 거짓이면, `A and B and C` 는 표현식 `C` 의 값을 구하지 않습니다. 논리값이 아닌 일반 값으로 사용될 때, 단락-회로 연산자의 반환 값은 마지막으로 값이 구해진 인자입니다.
- 비교의 결과나 다른 논리 표현식의 결과를 변수에 대입할 수 있습니다. 예를 들어,

```python
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
```

- 파이썬에서, C와는 달리, 표현식 안에서의 대입은 [바다코끼리 연산자](https://docs.python.org/ko/3.12/faq/design.html#why-can-t-i-use-an-assignment-in-an-expression) `:=`를 사용하여 명시적으로 수행해야 합니다. C 프로그램에서 흔히 마주치는 부류의 문제들을 회피하도록 합니다: `==` 를 사용할 표현식에 `=` 를 입력하는 실수.

## 주소

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

## 객체 비교

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

<img src="https://dschloe.github.io/img/python/basic_syntax/python-list-index.png" style="width: 600px" />
- 저장된 데이터는 자동으로 **색인(index)** 이 생깁니다.
- index는 좌측 기준 0부터 시작하며 음수를 사용할 경우 우측 기준 -1부터 시작합니다.
- 인덱스 시작 위치의 값은 포함되지만 종료 위치의 값은 포함되지 않습니다.

```python
word[0:2]  # characters from position 0 (included) to 2 (excluded)
word[2:5]  # characters from position 2 (included) to 5 (excluded)
```

- 인덱스가 범위를 벗어날 경우 에러가 발생합니다.

```python
word[42]  # the word only has 6 characters
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

- 하지만, 범위를 벗어나는 슬라이스 인덱스는 에러가 발생하지 않고 빈 값으로 처리합니다.

```python
word[4:42]
'on'
word[42:]
''
```

#### 문자열 (String) [[python_string|(자세히 보기)]]
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

##### f-문자열 (f-string)
> [2. 어휘 분석 — Python 3.12.5 문서](https://docs.python.org/ko/3.12/reference/lexical_analysis.html#f-strings)

#### 리스트 (List) [[python_list|(자세히 보기)]]

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

```python
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(a+b) # 결과: [1, 2, 3, 4, 5, 6]
```

- `+` 연산자로 두 리스트를 합친 새로운 객체를 생성할 수 있습니다.
- 기존 객체에 값을 더하려면 `extend()` 함수를 사용해야 합니니다.

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
```python
List = [1, 2, 3, 4, 5]
print(List[0:3]) # 결과: [1, 2, 3], List[:3]과 동일하다.
print(List[2:5]) # 결과: [3, 4, 5], List[2:]와 동일하다.
print(List[:]) # 결과: [1, 2, 3, 4, 5]
```

- `[start:end]` 로 리스트의 여러 값을 indexing 할 수 있다.
  
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

- `List` [[#심화 주소|객체를 직접 할당]] 하면 같은 주소를 가리키면서 예상치 못한 문제가 발생할 수 있다.
- `List[:]` 는 `List` 의 전체 값을 Indexing 한다. 이를 이용하여 복사에 사용할 수 있다.

```python
List = [1, 2, 3, 4, 5]
List[0] = 0
print(List) # 결과: [0, 2, 3, 4, 5]
```

- Index 를 사용하여 기존 값을 변경할 수 있다.

```python
List = [1, 2, 3, 4, 5]
List[5] = 6 # 결과: Error
```

- Index 를 벗어나는 값을 할당하려고 할 경우 에러가 발생한다.
- 새로운 값을 추가하기 위해서는 `append()` 함수를 사용해야 한다.

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

- 리스트 타입은 리스트 타입을 저장할 수 있다. 이를 중첩 리스트라 한다.

```python
NESTED_LIST = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(NESTED_LIST[1]) # 결과: [4, 5, 6]
print(NESTED_LIST[1][1]) # 결과: 5
```

- 중첩 리스트의 경우 Index `[]` 를 1 번 사용하면 내부의 리스트가 반환되고, `[][]` 와 같이 2 번 사용하면 반환된 리스트에서 Index 에 맞는 값을 가져온다.



#### 튜플 (Tuple)
- 리스트와 문자열이 인덱싱과 슬라이싱 연산과 같은 많은 성질을 공유함을 보았습니다. 이것들은 _시퀀스_ 자료 형의 두 가지 예입니다 ([시퀀스 형 — list, tuple, range](https://docs.python.org/ko/3.12/library/stdtypes.html#typesseq) 를 보세요). 파이썬은 진화하는 언어이기 때문에, 다른 시퀀스 자료형이 추가될 수도 있습니다. 다른 표준 시퀀스 자료 형이 있습니다: _튜플_ 입니다.
- 튜플은 쉼표로 구분되는 여러 값으로 구성됩니다. 예를 들어:

```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
>>> u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
>>> t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
>>> v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```

- 여러분이 보듯이, 출력되는 튜플은 항상 괄호로 둘러싸입니다, 그래서 중첩된 튜플이 올바르게 해석됩니다; 종종 괄호가 필요하기는 하지만 (튜플이 더 큰 표현식의 일부일 때), 둘러싼 괄호와 함께 또는 없이 입력될 수 있습니다. 튜플의 개별 항목에 대입하는 것은 가능하지 않지만, 리스트 같은 가변 객체를 포함하는 튜플을 만들 수는 있습니다.

```python
TUPLE_A = '배트맨', 1989, '슈퍼맨II' , 1980
TUPLE_B = ('배트맨', 1989, '슈퍼맨II' , 1980)
TUPLE_C = tuple(['배트맨', 1989, '슈퍼맨II' , 1980])

print(TUPLE_A)
print(TUPLE_B)
print(TUPLE_C)

TUPLE_A[3] = 1981 # 에러 발생
```

- 처음 객체를 생성하면 이후에는 내부의 값 변경이 불가능한 자료 구조입니다. 값 변경이 불가능한 것 외에는 List 와 유사합니다. 튜플이 리스트처럼 보인다 하더라도, 이것들은 다른 상황에서 다른 목적으로 사용됩니다.
- 일반적으로 서로 다른 (heterogeneous) 종류의 데이터 타입으로 이루어진 항목들을 변수에 바로 할당하는 요소들은 언패킹이나 인덱싱 (또는 [`네임드 튜플`](https://docs.python.org/ko/3.12/library/collections.html#collections.namedtuple "collections.namedtuple") 의 경우는 어트리뷰트로도) 용도로 사용합니다.
  리스트는 [가변](https://docs.python.org/ko/3.12/glossary.html#term-mutable) 이고, 요소들은 보통 등질 적이고 리스트에 대한 이터레이션으로 액세스 됩니다.
- 열거형 데이터가 필요할 때 값의 변경이 필요하지 않을 경우 List 보다 Tuple 타입을 사용하는 것이 속도가 빨라 성능에 더 유리합니다.
- `()` 로 감싸거나 괄호를 사용하지 않고 `,` 를 사용하여 Tuple 을 생성할 수 있으며 `tuple()`로도 생성할 수 있습니다.
- 특별한 문제는 비었거나 하나의 항목을 갖는 튜플을 만드는 것입니다: 이 경우를 수용하기 위해 문법은 추가적인 예외 사항을 갖고 있습니다. 빈 튜플은 빈 괄호 쌍으로 만들어집니다; 하나의 항목으로 구성된 튜플은 값 뒤에 쉼표를 붙여서 만듭니다 (값 하나를 괄호로 둘러싸기만 하는 것으로는 충분하지 않습니다). 추합니다, 하지만 효과적입니다. 예를 들어:

```python
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
```

```python
TUPLE_EMPTY_A = () # Tuple 타입
TUPLE_EMPTY_B = tuple() # Tuple 타입
TUPLE_A = 'Hello', # Tuple 타입
NOT_TUPLE = ('Hello') # String 타입
```

- 빈 Tuple 을 생성할 경우 `()` 만 할당하거나 `tuple()` 을 사용하면 된다.
- 하나의 값만 할당할 경우 끝에 `,` 를 사용해야 한다. `,` 를 붙이지 않거나 하나의 값에 `()` 를 사용할 경우 입력한 값의 타입으로 생성된다.

```python
TUPLE_A = [1, 2, 3], [4, 5, 6]
TUPLE_A[1][2] = 7
print(TUPLE_A) # 결과: [1, 2, 3], [4, 5, 7]
```

- Tuple 에 포함된 값은 변경이 불가능하지만 리스트를 값으로 가질 경우 리스트 내부의 값은 변경할 수 있다.
- Tuple 이 값으로 갖는 것은 List 의 주소이다. List 는 값이 변경한 자료 구조이므로 내부 값을 변경해도 Tuple 의 규칙에 위배되지 않는다.



##### Unpacking

```python
TUPLE_A = '배트맨', 1989, '슈퍼맨II' , 1980
a, b, c, d = TUPLE_A
print(a) # 결과: '배트맨'
print(b) # 결과: 1989
print(c) # 결과: '슈퍼맨II'
print(d) # 결과: 1980
```

- 위의 `TUPLE_A` 처럼 여러 값들을 하나의 변수에 할당하는 것을 **Packing**이라고 합니다. 문장 `t = 12345, 54321, 'hello!'` 는 _튜플 패킹_ 의 예입니다: 값 `12345`, `54321`, `'hello!'` 는 함께 튜플로 패킹 됩니다. 반대 연산 또한 가능합니다:

```python
x, y, z = t
```

- `a, b, c, d = TUPLE_A` 처럼 Packing 한 변수를 활용하여 여러 변수에 동시에 값을 할당하는 것을 **Unpacking**이라 합니다. 시퀀스 언 패킹 이라고 불리고 오른쪽에 어떤 시퀀스가 와도 됩니다. 시퀀스 언 패킹은 등호의 좌변에 시퀀스에 있는 요소들과 같은 개수의 변수들이 올 것을 요구합니다. 다중 대입은 사실 튜플 패킹과 시퀀스 언 패킹의 조합일뿐이라는 것에 유의하세요.

#### 집합 (Set)

- 파이썬은 _집합_ 을 위한 자료 형도 포함합니다. 집합은 중복되는 요소가 없는 순서 없는 컬렉션입니다. 기본적인 용도는 멤버십 검사와 중복 항목 제거입니다. 집합 객체는 합집합, 교집합, 차집합, 대칭 차집합과 같은 수학적인 연산들도 지원합니다. 수학의 합집합 (`|`), 교집합 (`&`), 차집합 (`-`), 여집합 (`^`) 을 구현할 수 있습니다.
- 집합을 만들 때는 `{VALUE1, VALUE2}` 와 같이 중괄호 `{}`를 사용하거나 [`set()`](https://docs.python.org/ko/3.12/library/stdtypes.html#set "set") 함수를 사용할 수 있습니다. 

> [!warning] 
> - 빈 집합을 만들려면 `set()` 을 사용해야 합니다. `{}` 가 아닙니다; 후자는 빈 딕셔너리를 만듭니다.

- Index 가 없으며 중복이 허용되지 않는 데이터 집합입니다. Index 가 없으므로 순서가 존재하지 않습니다.
- Dictionary 의 생성 문법과 겹쳐서 `{}` 만으로는 빈 Set 를 생성할 수 없다. `set()` 로만 빈 Set 를 생성할 수 있다.

```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
>>>
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

- [[python_list|리스트 컴프리헨션]] 과 유사하게, 집합 컴프리헨션도 지원됩니다:

```python
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```

| 메서드                   | 설명           |
| --------------------- | ------------ |
| `add(값)`              | 값 추가         |
| `update([값1, 값2, …])` | 여러 값 한 번에 추가 |
| `remove(값)`           | 특정 값 제거      |


#### 딕셔너리 (Dictionary)
- 파이썬에 내장된 또 다른 유용한 데이터 유형은 dictionary입니다([매핑 형 - 딕셔너리](https://docs.python.org/ko/3.12/library/stdtypes.html#typesmapping) 참조). 딕셔너리는 다른 언어에서 Map 타입, “연관 메모리” 또는 “연관 배열”로 불리기도 합니다. 

```python
DICTIONARY_A = {'blue': 3, 'red': 4, 'green': 5}
DICTIONARY_B = dict([('brown', 3), ('gray', 7)])
DICTIONARY_C = dict(brown=3, gray=7)
DICTIONARY_EMPTY_A = {} # Dictionary 타입
DICTIONARY_EMPTY_B = dict() # Dictionary 타입
```

- 숫자 범위로 색인되는 시퀀스와 달리 딕셔너리는 key로 색인되며, 이는 어떤 불변의 유형이든 될 수 있습니다(문자열과 숫자는 항상 키가 될 수 있습니다). 문자열, 숫자 또는 튜플만 포함된 경우 튜플을 키로 사용할 수 있으며, 튜플에 직접 또는 간접적으로 변경 가능한 객체가 포함된 경우 키로 사용할 수 없습니다. 
  리스트는 인덱스 할당, 슬라이스 할당 또는 `append()` 및 `extend()`와 같은 메서드를 사용하여 제자리에서 수정할 수 있으므로 리스트를 키로 사용할 수 없습니다.
- 다른 타입처럼 숫자 Index 가 자동으로 적용되지 않으므로 순서가 존재하지 않습니다.
- `key:value` 와 같이 `:` 를 사용하여 표기합니다. 딕셔너리를 (한 딕셔너리 안에서) 키가 중복되지 않는다는 제약 조건을 가진 _키: 값_ 쌍의 집합으로 생각하는 것이 최선입니다. 
- 중괄호 쌍은 빈 딕셔너리를 만듭니다: `{}`. 각 쌍은 `,` 로 구분하며 `{}` 로 감싸서 선언합니다. 중괄호 안에 쉼표로 분리된 키:값 쌍들의 목록을 넣으면, 딕셔너리에 초기 키:값 쌍들을 제공합니다; 이것이 딕셔너리가 출력되는 방식이기도 합니다. 혹은 `dict` 함수를 사용하여 생성할 수 있습니다. 이 경우 Key 와 Value 가 구분되도록 입력해야 합니다.
- 숫자로는 값들을 구분하기 힘들 때 주로 사용합니다. 단순한 숫자 Index 로도 충분할 경우 Dictionary 타입은 오히려 성능에 악영향을 줍니다.
- 딕셔너리의 주 연산은 값을 키와 함께 저장하고 주어진 키로 값을 추출하는 것입니다. `del` 로 키:값 쌍을 삭제하는 것도 가능합니다. 이미 사용하고 있는 키로 저장하면, 그 키로 저장된 예전 값은 잊힙니다. 존재하지 않는 키로 값을 추출하는 것은 에러입니다.
- 딕셔러리에 `list(d)` 를 수행하면 딕셔너리에서 사용되고 있는 모든 키의 리스트를 삽입 순서대로 돌려줍니다 (정렬을 원하면 대신 `sorted(d)` 를 사용하면 됩니다). 하나의 키가 딕셔너리에 있는지 검사하려면, [`in`](https://docs.python.org/ko/3.12/reference/expressions.html#in) 키워드들 사용하세요.

```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```

- [`dict()`](https://docs.python.org/ko/3.12/library/stdtypes.html#dict "dict") 생성자는 키-값 쌍들의 시퀀스로 부터 직접 딕셔너리를 구성합니다.

```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

- 이에 더해, 딕셔너리 컴프리헨션은 임의의 키와 값 표현식들로 부터 딕셔너리를 만드는데 사용될 수 있습니다:

```python
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

- 키가 간단한 문자열일 때, 때로 키워드 인자들을 사용해서 쌍을 지정하기가 쉽습니다:

```python
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

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

- `DICTIONARY[KEY] = VALUE` 로 새로운 값을 추가할 수 있습니다.
- `del DICTIONARY[KEY]` 로 `KEY` 를 갖는 쌍을 제거할 수 있습니다.
- 기존에 있던 `KEY` 에 새로운 값을 할당하면 기존 값을 변경할 수 있습니다.

```python
DICTIONARY_A = {'blue': 3, 'red': 4, 'green': 5}
print(3 in DICTIONARY_A) # 결과: False
```

- `in` 을 사용할 경우 key 값을 기준으로 참/거짓을 판단합니다.


### 시퀀스와 다른 형들을 비교하기

- 시퀀스 객체들은 보통 같은 시퀀스 형의 다른 객체들과 비교될 수 있습니다. 비교는 _사전식_ 순서를 사용합니다: 
  
  먼저 첫 두 항목을 비교해서 다르면 이것이 비교의 결과를 결정합니다; 
  같으면, 다음 두 항목을 비교하고, 이런 식으로 어느 한 시퀀스가 소진될 때까지 계속합니다. 
  만약 비교되는 두 항목 자체가 같은 형의 시퀀스면, 사전식 비교가 재귀적으로 수행됩니다. 
  두 시퀀스의 모든 항목이 같다고 비교되면, 시퀀스들은 같은 것으로 취급됩니다. 한 시퀀스가 다른 하나의 머리 부분 서브 시퀀스면, 짧은 시퀀스가 작은 것입니다.
  
- 문자열의 사전식 배열은 개별 문자들의 순서를 정하는데 유니코드 코드 포인트 숫자를 사용합니다. 같은 형의 시퀀스들 간의 비교의 몇 가지 예는 이렇습니다:

```python
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```

- 서로 다른 형의 객체들을 `<` 나 `>` 로 비교하는 것은, 그 객체들이 적절한 비교 메서드들을 갖고 있을 때만 허락된다는 것에 유의하세요. 예를 들어, 서로 다른 숫자 형들은 그들의 숫자 값에 따라 비교됩니다. 그래서 0은 0.0과 같고, 등등. 그렇지 않으면, 임의의 순서를 제공하는 대신, 인터프리터는 [`TypeError`](https://docs.python.org/ko/3.12/library/exceptions.html#TypeError "TypeError") 를 일으킵니다.

### 타입 변환

```python
var1 = "Python"
print(type(var1)) # var1의 타입 반환: <class 'str'> 
```

- `type()` 로 입력한 변수의 타입을 확인할 수 있습니다.
- 아래와 같이 변환하려는 타입을 함수로 사용하여 변환할 수 있습니다.

```python
i = int("123") # 결과: 123
s = str(123) # 결과: "123"
f = float("123.45") # 결과: 123.45
c = complex(1.1,2.2) # 결과: 1.1+2.2j
```

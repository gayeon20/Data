---
title: "[Python] 제어문 (Control Statement)"
excerpt: 
categories:
  - Python
tags:
  - Python
  - Control
  - Condition
  - Loop
  - if
  - match
  - For
  - while
  - break
  - continue
  - pass
last_modified_at: 2024-04-11T15:10:55+09:00
link: 
상위 항목: "[[python_home|파이썬 (Python)]]"
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

---

- Python 의 제어문은 다른 언어의 `{ }` 대신 `:` 과 **들여쓰기**로 처리합니다.

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

- `while` 과 `if` 문 등 조건에는 비교뿐만 아니라 모든 연산자를 사용할 수 있습니다.
- 비교 연산자 `in`과 `not in`은 값이 컨테이너에 있는지 아닌지를 결정하는 멤버십 테스트입니다. 연산자 `is`와 `is not`는 두 객체가 실제로 동일한 객체인지 여부를 비교합니다. 모든 비교 연산자의 우선 순위는 모든 숫자 연산자보다 낮은 동일한 우선 순위를 갖습니다.
- 비교는 연쇄할 수 있습니다. 예를 들어, `a < b == c` 는, `a` 가 `b` 보다 작고, 동시에 `b` 가 `c` 와 같은지 검사합니다.
- 비교는 논리 연산자 `and` 와 `or` 를 사용해서 결합할 수 있고, 비교의 결과는 (또는 그 밖의 모든 논리 표현식은) `not` 으로 부정될 수 있습니다. 이것들은 비교 연산자보다 낮은 우선순위를 갖습니다. 이것 간에는 `not` 이 가장 높은 우선순위를 갖고, `or` 가 가장 낮습니다. 그래서 `A and not B or C` 는 `(A and (not B)) or C` 와 동등합니다. 여느 때처럼, 원하는 조합을 표현하기 위해 괄호를 사용할 수 있습니다.

> [!NOTE] `in`
> 
> ```python
> LIST = [1, 2, 3, 4]
> print(2 in LIST) # 결과: True
> ```
> 
> - 열거형 데이터에는 `in` 을 사용할 수 있다. 해당 데이터에 입력한 값이 존재하면 `True`, 이외에는 `False` 를 반환한다.

## 조건문 (Condition)

### `if`

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

### `match`
- [`match`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#match) 문은 표현식을 받아 그 값을 하나 이상의 대소문자 블록으로 주어진 연속 패턴과 비교합니다. 이는 표면적으로는 C, Java 또는 JavaScript(및 기타 여러 언어)의 switch 문과 비슷하지만, Rust나 Haskell 같은 언어의 패턴 매칭과 더 유사합니다. 일치하는 첫 번째 패턴만 실행되며 값에서 구성 요소(시퀀스 요소 또는 객체 속성)를 변수로 추출할 수도 있습니다.
- 가장 간단한 형태는 주제 값을 하나 이상의 리터럴과 비교하는 것입니다:

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```

- 마지막 블록에 주목하세요. “변수 이름” `_`은 _와일드카드_ 역할을 하며 절대 일치하지 않습니다. 대소문자가 일치하지 않으면 브랜치 중 어느 것도 실행되지 않습니다.
- '`|`(“또는”)를 사용하여 여러 리터럴을 하나의 패턴으로 결합할 수 있습니다:

```python
case 401 | 403 | 404:
    return "Not allowed"
```

- 패턴은 할당 풀기처럼 보일 수 있으며 변수를 바인딩하는 데 사용할 수 있습니다:

```python
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
```

- 이 패턴을 주의 깊게 살펴보세요! 첫 번째 패턴은 두 개의 리터럴이 있으며, 위에 표시된 리터럴 패턴의 확장으로 생각할 수 있습니다. 하지만 다음 두 패턴은 리터럴과 변수를 결합하고, 변수는 주어(`point`)의 값을 바인딩합니다. 네 번째 패턴은 두 개의 값을 캡처하므로 개념적으로 언패킹 할당 `(x, y) = point`와 유사합니다.
- 클래스를 사용하여 데이터를 구조화하는 경우 클래스 이름 뒤에 생성자와 유사한 인수 목록을 사용할 수 있지만 속성을 변수로 캡처할 수 있는 기능이 있습니다:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
```

- 속성의 순서를 제공하는 일부 내장 클래스(예: 데이터 클래스)와 함께 위치 매개변수를 사용할 수 있습니다. 클래스에서 `__match_args__` 특수 속성을 설정하여 패턴에서 속성의 특정 위치를 정의할 수도 있습니다. 이 속성이 (“x”, “y”)로 설정되어 있으면 다음 패턴은 모두 동일합니다(모두 `y` 속성을 `var` 변수에 바인딩):

```python
Point(1, var)
Point(1, y=var)
Point(x=1, y=var)
Point(y=var, x=1)
```

- 패턴을 읽는 권장 방법은 어떤 변수가 무엇에 설정되는지 이해하기 위해 할당의 왼쪽에 배치하는 것의 확장된 형태로 패턴을 보는 것입니다. 위의 `var`와 같은 독립형 이름만 일치 문으로 할당됩니다. 점으로 구분된 이름(예: `foo.bar`), 속성 이름(위의 `x=` 및 `y=`) 또는 클래스 이름(위의 `Point`처럼 옆에 '(…)'로 인식됨)은 절대로 할당되지 않습니다.
- 패턴은 임의로 중첩될 수 있습니다. 예를 들어 `__match_args__`가 추가된 짧은 포인트 목록이 있다면 다음과 같이 일치시킬 수 있습니다:

```python
class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")
```

- 패턴에 `if` 절을 추가할 수 있는데, 이를 “가드”라고 합니다. 가드가 거짓이면 `match`는 계속해서 다음 대소문자 블록을 시도합니다. 가드가 평가되기 전에 값 캡처가 수행된다는 점에 유의하세요:

```python
match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")
```

- 이 문장의 다른 주요 기능도 몇 가지 있습니다
  
  - 할당 언패킹과 마찬가지로 튜플 패턴과 리스트 패턴은 정확히 동일한 의미를 가지며 실제로 임의의 시퀀스와 일치합니다. 중요한 예외는 이터레이터나 문자열과 일치하지 않는다는 점입니다.
  - 시퀀스 패턴은 확장 언패킹을 지원합니다: `[x, y, *rest]`와 `(x, y, *rest)`는 언패킹 할당과 유사하게 작동합니다. `*` 뒤의 이름은 `_`일 수도 있으므로 `(x, y, *_)`는 나머지 항목을 바인딩하지 않고 최소 두 항목의 시퀀스와 일치합니다.
  - 매핑 패턴: “대역폭“: b, ‘지연 시간’: l}`은 사전에서 `”대역폭“`과 `”지연 시간"` 값을 캡처합니다. 시퀀스 패턴과 달리 추가 키는 무시됩니다. rest`와 같은 언패킹도 지원됩니다. (하지만 `**_`는 중복될 수 있으므로 허용되지 않습니다.)
  - 하위 패턴은 `as` 키워드를 사용하여 캡처할 수 있습니다:
    
    case (Point(x1, y1), Point(x2, y2) as p2): …
    
    는 입력의 두 번째 요소를 `p2`로 캡처합니다 (입력이 두 점의 시퀀스인 경우).
  - 대부분의 리터럴은 같음을 기준으로 비교되지만, 싱글톤 `True`, `False`, `None`은 동일성을 기준으로 비교됩니다.
  - 패턴은 명명된 상수를 사용할 수 있습니다. 이러한 상수는 캡처 변수로 해석되지 않도록 점으로 구분된 이름이어야 합니다:
    
```python
from enum import Enum
class Color(Enum):
	RED = 'red'
	GREEN = 'green'
	BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
	case Color.RED:
		print("I see red!")
	case Color.GREEN:
		print("Grass is green")
	case Color.BLUE:
		print("I'm feeling the blues :(")
```

- 더 자세한 설명과 추가 예시는 튜토리얼 형식으로 작성된 [**PEP 636**](https://peps.python.org/pep-0636/)을 참조하세요.

## 반복문 (Loop)

### `while`

```python
while 조건문:
    실행할 문장1
    실행할 문장2
    실행할 문장3
```

- 조건문을 만족하는 동안 계속 실행한다. (조건문을 만족하지 않으면 한 번도 실행하지 않는다.)
- 조건문을 True 로 두면 무한 루프를 만들 수 있다. (Python IDLE 에서는 Ctrl + C 로 빠져나갈 수 있다.)

### `for`

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

### `break`

```python
for value in range(5):
    if LIST[x] == "Yellow":
        break
		print("이 문장은 실행되지 않습니다.")
```

- `break` 를 실행하면 `iterable` 에 남아있는 값과 상관 없이 해당 반복문이 종료된다.

### `continue`

```python
for value in range(5):
    if LIST[x] == "Yellow":
        continue
	print("continue가 실행되면 이 문장은 실행되지 않습니다.")
```

- `continue` 가 실행되면 해당 `value` 에 대한 반복문은 종료하고 `iterable` 의 다음 값을 `value` 에 대입하여 반복문을 이어간다.

### `pass`

```python
for value in range(5):
    if LIST[x] == "Yellow":
        pass
	else:
		print("pass가 실행되지 않으면 이 문장이 실행됩니다.")
```

- `pass` 는 아무 문장도 실행하지 않는다. 특정 조건을 충족했을 때 아무 문장도 실행하지 말아야 할 경우에 주로 활용된다.

### 컬렉션 자료형 처리
- 딕셔너리를 반복할 때 [`items()`](https://docs.python.org/ko/3.12/library/stdtypes.html#dict.items “dict.items”) 메서드를 사용하여 키와 해당 값을 동시에 검색할 수 있습니다.

```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
…     print(k, v)
…
gallahad the pure
robin the brave
```

- 시퀀스를 루핑할 때, [`enumerate()`](https://docs.python.org/ko/3.12/library/functions.html#enumerate "enumerate") 함수를 사용하면 위치 인덱스와 대응하는 값을 동시에 얻을 수 있습니다.

```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
…     print(i, v)
…
0 tic
1 tac
2 toe
```

- 둘이나 그 이상의 시퀀스를 동시에 루핑하려면, [`zip()`](https://docs.python.org/ko/3.12/library/functions.html#zip "zip") 함수로 엔트리들의 쌍을 만들 수 있습니다.

```python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
…     print('What is your {0}?  It is {1}.'.format(q, a))
…
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

- 시퀀스를 거꾸로 루핑하려면, 먼저 정방향으로 시퀀스를 지정한 다음에 [`reversed()`](https://docs.python.org/ko/3.12/library/functions.html#reversed "reversed") 함수를 호출하세요.

```python
>>> for i in reversed(range(1, 10, 2)):
…     print(i)
…
9
7
5
3
1
```

- 정렬된 순서로 시퀀스를 루핑하려면, [`sorted()`](https://docs.python.org/ko/3.12/library/functions.html#sorted "sorted") 함수를 사용해서 소스를 변경하지 않고도 정렬된 새 리스트를 받을 수 있습니다.

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
…     print(i)
…
apple
apple
banana
orange
orange
pear
```

- 시퀀스에 대해 [`set()`](https://docs.python.org/ko/3.12/library/stdtypes.html#set "set")을 사용하면 중복 요소를 제거합니다. 시퀀스에 대해 [`set()`](https://docs.python.org/ko/3.12/library/stdtypes.html#set "set")과 [`sorted()`](https://docs.python.org/ko/3.12/library/functions.html#sorted "sorted")를 함께 사용하는 것은 시퀀스의 고유 한 요소를 정렬된 순서로 루핑하는 관용적 방법입니다.

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
…     print(f)
…
apple
banana
orange
pear
```

- 때로 루프를 돌고 있는 리스트를 변경하고픈 유혹을 느낍니다; 하지만, 종종, 대신 새 리스트를 만드는 것이 더 간단하고 더 안전합니다.

```python
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
…     if not math.isnan(value):
…         filtered_data.append(value)
…
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```


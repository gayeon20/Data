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

## 연산자 (Operator)
### 산술 연산자 (Arithmetic Operator)
| 연산자  | 내용         |
| ---- | ---------- |
| `+`  | 덧셈         |
| `-`  | 뺄셈         |
| `*`  | 곱셈         |
| `/`  | 나눗셈        |
| `%`  | 나눗셈의 나머지   |
| `//` | 나눗셈의 몫     |
| `**` | 지수 연산 (제곱) |
### 비교 연산자 (Comparison Operator)
| 연산자  | 내용                |
| ---- | ----------------- |
| `>`  | 좌변이 더 크면 True     |
| `<`  | 우변이 더 크면 True     |
| `>=` | 좌변이 같거나 더 크면 True |
| `<=` | 우변이 같거나 더 크면 True |
| `==` | 두 변이 같으면 True     |
| `!=` | 두 변이 다르면 True     |

### 논리 연산자 (Logic Operator)
| 연산자   | 내용                        |
| ----- | ------------------------- |
| `and` | 두 논리 값이 모두 참이면 True       |
| `or`  | 두 논리 값 중 하나라도 참이면 True    |
| `not` | 반대 논리값 반환 (True -> False) |
### 대입 연산자 (Assignment Operator)
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
|       |                         |
### 괄호

| 괄호의 종류 | 의미                                       |
| ------ | ---------------------------------------- |
| `()`   | 무언가를 호출할 때 ==값을 전달하는 용도==로 사용합니다.        |
| `[]`   | 대상에 ==인덱스로 접근==할 때 사용합니다.                |
| `{}`   | 여러 줄의 코드 블록을 만들 때 사용합니다. (Python에서는 미사용) |

## 제어문 (Control)
Python 의 제어문은 다른 언어의 `{ }` 대신 `:` 과 **들여쓰기**로 처리합니다.

| 연산자 / 예약어 | 설명 |
| ---- | ---- |
| x < y | x 가 y 보다 작다. |
| x > y | x 가 y 보다 크다. |
| x == y | x 와 y 가 같다. |
| x!= y | x 와 y 가 같지 않다. |
| x >= y | x 가 y 보다 크거나 같다. |
| x <= y | x 가 y 보다 작거나 같다. |
| x or y | x 또는 y 가 참이면 참 |
| x and y | x 와 y 가 모두 참이면 참 |
| not x | x 가 거짓이면 참 |
| x in A | x 가 A 의 요소로 있으면 참 |
| x not in A | x 가 A 의 요소가 아니면 참 |

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

`pass` 는 아무 문장도 실행하지 않는다. 특정 조건을 충족했을 때 아무 문장도 실행하지 말아야 할 경우에 주로 활용된다.



## 변수
```python
variable = value
```

## 문자열
```python
message = "Hello World"
print(message.split(" "))
```
- `split(구분자)` 함수를 실행하면 입력한 문자열에 포함된 `구분자`를 기준으로 값을 나누어서 리스트로 반환합니다.

```python
hello = "Hello"
world = "World"
print(hello + world)
```
- 문자열끼리 덧셈을 실행하면 붙어있는 문자열이 출력됩니다.

## 리스트
```python
# 인덱스는 0부터 시작합니다.
list_name = ["variable1", "variable2", 3, 4]

# Index 0:  "variable1"
# Index 1:  "variable2"
# Index 2:  3
# Index 3:  4
```

- 길이는 `len()` 함수로 출력할 수 있습니다.

```python
list_name = ["variable1", "variable2", 3, 4]
list_name.remove(3)
```

- `remove(variable)` 함수를 사용하면 `variable`을 list에서 제거할 수 있습니다.


## 입출력
```python
variable = input("설명 메시지")
```
- `input`은 입력한 값을 문자열 (`str`) 타입으로 저장합니다.
- `"설명 메시지"`는 설명을 위해 출력할 메시지를 결정합니다.
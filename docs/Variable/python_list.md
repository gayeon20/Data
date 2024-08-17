---
title: "[Python] 리스트 (List)"
excerpt: 
categories:
  - Python
tags:
  - Python
  - Variable
  - Data-Type-List
last_modified_at: 2024-04-11T15:10:55+09:00
link: 
상위 항목: "[[python_variable|파이썬 변수 (Python Variable)]]"
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

---

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

## 인덱스 (Index)

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



## 중첩 리스트

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

## 리스트를 스택으로 사용하기
- 목록 메서드를 사용하면 목록을 스택으로 매우 쉽게 사용할 수 있으며, 마지막으로 추가된 요소가 검색된 첫 번째 요소(“라스트 인, 퍼스트 아웃”)가 됩니다. 스택의 맨 위에 항목을 추가하려면 `append()`를 사용합니다. 스택의 맨 위에서 항목을 검색하려면 명시적 인덱스 없이 `pop()`을 사용합니다. 예를 들어

```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```

## 리스트를 큐로 사용하기
- 리스트를 큐로 사용하는 것도 가능한데, 처음으로 넣은 요소가 처음으로 꺼내지는 요소입니다 (“first-in, first-out”); 하지만, 리스트는 이 목적에는 효율적이지 않습니다. 리스트의 끝에 덧붙이거나, 끝에서 꺼내는 것은 빠르지만, 리스트의 머리에 덧붙이거나 머리에서 꺼내는 것은 느립니다 (다른 요소들을 모두 한 칸씩 이동시켜야 하기 때문입니다).
- 큐를 구현하려면, 양 끝에서의 덧붙이기와 꺼내기가 모두 빠르도록 설계된 [`collections.deque`](https://docs.python.org/ko/3.12/library/collections.html#collections.deque "collections.deque") 를 사용하세요. 예를 들어:

```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

## 리스트 컴프리헨션

- 리스트 컴프리헨션은 리스트를 만드는 간결한 방법을 제공합니다. 흔한 용도는, 각 요소가 다른 시퀀스나 이터러블의 멤버들에 어떤 연산을 적용한 결과인 리스트를 만들거나, 어떤 조건을 만족하는 요소들로 구성된 서브 시퀀스를 만드는 것입니다.
- 예를 들어, 제곱수의 리스트를 만들고 싶다고 가정하자, 이런 식입니다:

```python
>>> squares = []
>>> for x in range(10):
…     squares.append(x**2)
…
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

- 이것은 `x` 라는 이름의 변수를 만들고 (또는 덮어쓰고) 루프가 종료된 후에도 남아있게 만든다는 것에 유의하세요. 어떤 부작용도 없이, 제곱수의 리스트를 이런 식으로 계산할 수 있습니다:

```python
squares = list(map(lambda x: x**2, range(10)))
```

또는, 이렇게 할 수도 있습니다:

```python
squares = [x**2 for x in range(10)]
```

이것이 더 간결하고 읽기 쉽습니다.

- 리스트 컴프리헨션은 표현식과 그 뒤를 따르는 `for` 절과 없거나 여러 개의 `for` 나 `if` 절들을 감싸는 대괄호로 구성됩니다. 그 결과는 새 리스트인데, `for` 와 `if` 절의 문맥에서 표현식의 값을 구해서 만들어집니다. 예를 들어, 이 리스트 컴프리헨션은 두 리스트의 요소들을 서로 같지 않은 것끼리 결합합니다:

```python
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

그리고, 이것은 다음과 동등합니다:

```python
>>> combs = []
>>> for x in [1,2,3]:
…     for y in [3,1,4]:
…         if x != y:
…             combs.append((x, y))
…
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

- 두 코드 조각에서 [`for`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#for) 와 [`if`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#if) 문의 순서가 같음에 유의하세요.
- 표현식이 튜플이면 (즉 앞의 예에서 `(x, y)`), 반드시 괄호로 둘러싸야 합니다.

```python
>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x**2 for x in range(6)]
  File "<stdin>", line 1
    [x, x**2 for x in range(6)]
     ^^^^^^^
SyntaxError: did you forget parentheses around the comprehension target?
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

- 리스트 컴프리헨션은 복잡한 표현식과 중첩된 함수들을 포함할 수 있습니다:

```python
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

## 중첩된 리스트 컴프리헨션
- 리스트 컴프리헨션의 첫 표현식으로 임의의 표현식이 올 수 있는데, 다른 리스트 컴프리헨션도 가능합니다.
  다음과 같은 길이가 4인 리스트 3개의 리스트로 구현된 3x4 행렬의 예를 봅시다:

```python
>>> matrix = [
…     [1, 2, 3, 4],
…     [5, 6, 7, 8],
…     [9, 10, 11, 12],
… ]
```

- 다음 리스트 컴프리헨션은 행과 열을 전치 시킵니다:

```python
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

- 이전 섹션에서 살펴본 것처럼 내부 목록 이해도는 그 뒤에 오는 [`for`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#for)의 컨텍스트에서 평가되므로 이 예제는 다음과 같습니다:

```python
>>> transposed = []
>>> for i in range(4):
…     transposed.append([row[i] for row in matrix])
…
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

이것은 다시 다음과 같습니다:

```python
>>> transposed = []
>>> for i in range(4):
…     # the following 3 lines implement the nested listcomp
…     transposed_row = []
…     for row in matrix:
…         transposed_row.append(row[i])
…     transposed.append(transposed_row)
…
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

- 실제 세상에서는, 복잡한 흐름문보다 내장 함수들을 선호해야 합니다. 이 경우에는 [`zip()`](https://docs.python.org/ko/3.12/library/functions.html#zip "zip") 함수가 제 역할을 할 수 있습니다:

```python
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

- 이 줄에 나오는 애스터리스크에 대한 자세한 내용은 [인자 목록 언 패킹](https://docs.python.org/ko/3.12/tutorial/controlflow.html#tut-unpacking-arguments) 을 보세요.

## `del` 문
- 목록에서 값 대신 인덱스가 주어지면 항목을 제거하는 방법이 있습니다: [`del`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#del) 문입니다. 이 방법은 값을 반환하는 [[#list.pop([i])|pop()]] 메서드와는 다릅니다. 
- `del` 문은 목록에서 슬라이스를 제거하거나 전체 목록을 지우는 데에도 사용할 수 있습니다(앞서 빈 목록을 슬라이스에 할당하여 수행한 것처럼). 예를 들어

```python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```

[`del`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#del) 는 변 자체를 삭제하는데에도 사용될 수 있습니다:

```python
del a
```

- 이후에 이름 `a` 를 참조하는 것은 에러입니다 (적어도 다른 값이 새로 대입되기 전까지). 뒤에서 [`del`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#del) 의 다른 용도를 보게 됩니다.


## 내부 메소드
- 목록만 수정하는 삽입, 제거 또는 정렬과 같은 메서드에는 반환값이 출력되지 않고 기본값인 None을 반환합니다. 이는 파이썬의 모든 가변 데이터 구조에 적용되는 설계 원칙입니다.
- 또 한 가지 주목할 점은 모든 데이터를 정렬하거나 비교할 수 있는 것은 아니라는 점입니다. 예를 들어 [None, 'hello', 10]은 정수는 문자열과 비교할 수 없고 None은 다른 유형과 비교할 수 없으므로 정렬되지 않습니다. 또한 정의된 순서 관계가 없는 타입도 있습니다. 예를 들어 `3+4j < 5+7j`는 유효한 비교가 아닙니다.


### `list.append(x)`

- 리스트의 끝에 항목을 더합니다. `a[len(a):] = [x]` 와 동등합니다.

```python
List = [1, 2, 3]
List.append(4)
print(List) # 결과: [1, 2, 3, 4]
```

### `list.extend(iterable)`

- 리스트의 끝에 이터러블의 모든 항목을 덧붙여서 확장합니다. `a[len(a):] = iterable` 와 동등합니다.

```python
List = [1, 2, 3]
additional_list = [4, 5, 6]
List.extend(additional_list)
print(List)
```

### `list.insert(i, x)`

- 주어진 위치에 항목을 삽입합니다. 첫 번째 인자는 삽입되는 요소가 갖게 될 인덱스입니다. 그래서 `a.insert(0, x)` 는 리스트의 처음에 삽입하고, `a.insert(len(a), x)` 는 `a.append(x)` 와 동등합니다.

```python
List = [1, 2, 3, 4]
List.insert(2, 0)
print(List) # 결과: [1, 2, 0, 3, 4]
```


### `list.remove(x)`

- 리스트에서 값이 _x_ 와 같은 첫 번째 항목을 삭제합니다. 그런 항목이 없으면 [`ValueError`](https://docs.python.org/ko/3.12/library/exceptions.html#ValueError "ValueError")를 일으킵니다.`

```python
List = [1, 2, 3, 4, 1]
List.remove(1)
print(List) # 결과: [2, 3, 4, 1]
```

- Index 를 앞에서부터 탐색하여 가장 먼저 나오는 값을 제거합니다.

> [!NOTE] `del list[i]`
> 
> - `del <List>[INDEX]` 로 `List` 객체의 `INDEX` 위치에 있는 값을 제거할 수 있습니다.
> - `pop` 과 달리 제거한 값을 반환하지 않습니다.
> - `remove` 는 제거할 값을 입력하고 `del` 은 제거할 Index 를 입력한다는 차이점이 있습니다.
> 
> ```python
> List = [1, 2, 3, 4, 5, 6]
> del List[2]
> print(List) # 결과: [1, 2, 4, 5, 6]
> ```

### `list.pop([i])`

- 목록에서 지정된 위치에 있는 항목을 제거하고 반환합니다. 인덱스가 지정되지 않은 경우 `a.pop()`은 목록의 마지막 항목을 제거하고 반환합니다. 목록이 비어 있거나 인덱스가 목록 범위를 벗어난 경우 [`IndexError`](https://docs.python.org/ko/3.12/library/exceptions.html#IndexError “IndexError”)를 발생시킵니다.

```python
List = ["a", "b", "c", "d", "e"]
print(List.pop(3)) # 결과: "d"
```

### `list.clear()`

- 리스트의 모든 항목을 삭제합니다. `del a[:]` 와 동등합니다.


### `list.index(_x_[, start[, end]])`
- 리스트에 있는 항목 중 값이 `x` 와 같은 첫 번째 것의 0부터 시작하는 인덱스를 돌려줍니다. 그런 항목이 없으면 [`ValueError`](https://docs.python.org/ko/3.12/library/exceptions.html#ValueError "ValueError") 를 일으킵니다.
- 선택적인 인자 `start` 와 `end` 는 슬라이스 표기법처럼 해석되고, 검색을 리스트의 특별한 서브 시퀀스로 제한하는 데 사용됩니다. 돌려주는 인덱스는 `start` 인자가 아니라 전체 시퀀스의 시작을 기준으로 합니다.

### `list.count(x)`
- 리스트에서 _x_ 가 등장하는 횟수를 돌려줍니다.

### `list.sort(*, key=None, reverse=False)`

- 리스트의 항목들을 제자리에서 정렬합니다 (인자들은 정렬 커스터마이제이션에 사용될 수 있습니다. 설명은 [`sorted()`](https://docs.python.org/ko/3.12/library/functions.html#sorted "sorted") 를 보세요).

### `list.reverse()`
- 리스트의 요소들을 제자리에서 뒤집습니다.

### `list.copy()`
- 리스트의 얕은 사본을 돌려줍니다. `a[:]` 와 동등합니다.



> [!example] 리스트 메서드 대부분을 사용하는 예
> ```python
> >>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
> >>> fruits.count('apple')
> 2
> >>> fruits.count('tangerine')
> 0
> >>> fruits.index('banana')
> 3
> >>> fruits.index('banana', 4)  # Find next banana starting at position 4
> 6
> >>> fruits.reverse()
> >>> fruits
> ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
> >>> fruits.append('grape')
> >>> fruits
> ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
> >>> fruits.sort()
> >>> fruits
> ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
> >>> fruits.pop()
> 'pear'
> ```
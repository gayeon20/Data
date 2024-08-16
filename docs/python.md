
## 연산자

| 연산자  | 뜻   |
| ---- | --- |
| `+`  | 덧셈  |
| `-`  | 뺄셈  |
| `*`  | 곱셈  |
| `**` | 제곱  |
| `/`  | 나눗셈 |
| `//` | 몫   |
| `%`  | 나머지 |

| 괄호의 종류 | 의미                                       |
| ------ | ---------------------------------------- |
| `()`   | 무언가를 호출할 때 ==값을 전달하는 용도==로 사용합니다.        |
| `[]`   | 대상에 ==인덱스로 접근==할 때 사용합니다.                |
| `{}`   | 여러 줄의 코드 블록을 만들 때 사용합니다. (Python에서는 미사용) |

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
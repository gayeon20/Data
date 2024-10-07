---
title: "[Python] 함수 (Function)"
excerpt: 
categories:
  - Python
tags:
  - Python
  - Object
  - Function
  - Arguments
last_modified_at: 2024-04-11T15:10:55+09:00
link: 
상위 항목: "[[python_object_temp|파이썬 객체 (Python Object)]]"
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

---

- 키워드 [`def`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#def)는 함수 정의를 시작합니다. 함수 이름과 괄호로 싸인 형식 매개변수들의 목록이 뒤따릅니다. 함수의 바디를 형성하는 문장들이 다음 줄에서 시작되고, 반드시 들여쓰기 되어야 합니다.
- 피보나치 수열을 임의의 한도까지 출력하는 함수를 만들 수 있습니다:

```python
>>> def fib(n):    # write Fibonacci series up to n
… """Print a Fibonacci series up to n."""
…     a, b = 0, 1
…     while a < n:
…         print(a, end=' ')
…         a, b = b, a+b
…     print()
…
>>> # Now call the function we just defined:
>>> fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
```

- 함수 바디의 첫 번째 문장은 선택적으로 문자열 리터럴이 될 수 있습니다; 이 문자열 리터럴은 함수의 도큐멘테이션 문자열, 즉 _독스트링 (docstring)_ 입니다. (독스트링에 대한 자세한 내용은 [도큐멘테이션 문자열](https://docs.python.org/ko/3.12/tutorial/controlflow.html#tut-docstrings) 에 나옵니다.) 독스트링을 사용해서 온라인이나 인쇄된 설명서를 자동 생성하거나, 사용자들이 대화형으로 코드를 열람할 수 있도록 하는 도구들이 있습니다; 여러분이 작성하는 코드에 독스트링을 첨부하는 것은 좋은 관습입니다, 그러니 버릇을 들이는 것이 좋습니다.
- 함수의 실행은 함수의 지역 변수들을 위한 새 심볼 테이블을 만듭니다. 좀 더 구체적으로, 함수에서의 모든 변수 대입들은 값을 지역 심볼 테이블에 저장합니다; 반면에 변수 참조는 먼저 지역 심볼 테이블을 본 다음, 전역 심볼 테이블을 본 후, 마지막으로 내장 이름들의 테이블을 살핍니다. 그래서, 참조될 수는 있다 하더라도, 전역 변수들과 둘러싸는 함수의 변수들은 함수 내에서 직접 값이 대입될 수 없습니다 (전역 변수를 [`global`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#global) 문으로 명시하거나 둘러싸는 함수의 변수를 [`nonlocal`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#nonlocal) 문으로 명시하지 않는 이상).
- 함수 호출로 전달되는 실제 매개변수들 (인자들)은 호출될 때 호출되는 함수의 지역 심볼 테이블에 만들어집니다; 그래서 인자들은 값에 의한 호출(call by value)로 전달됩니다 (값은 항상 객체의 값이 아니라 객체 참조입니다). 함수가 다른 함수를 호출할 때, 또는 자신을 재귀적으로 호출할 때, 그 호출을 위한 새 지역 심볼 테이블이 만들어집니다.
- 함수 정의는 함수 이름을 현재 심볼 테이블의 함수 객체와 연결합니다. 인터프리터는 해당 이름이 가리키는 객체를 사용자 정의 함수로 인식합니다. 다른 이름은 같은 함수 객체를 가리킬 수 있으며 함수에 액세스하는 데 사용될 수도 있습니다:
- 정해지지 않은 개수의 인자들로 함수를 정의하는 것도 가능합니다. 세 가지 형식이 있는데, 조합할 수 있습니다.

### 기본 인자 값
- 가장 쓸모 있는 형식은 하나나 그 이상 인자들의 기본값을 지정하는 것입니다. 정의된 것보다 더 적은 개수의 인자들로 호출될 수 있는 함수를 만듭니다. 예를 들어:

```python
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```

- 이 함수는 여러 가지 방법으로 호출될 수 있습니다:
  
  - 오직 꼭 필요한 인자만 전달해서: `ask_ok('정말 끝내길 원하세요?')`
  - 선택적 인자 하나를 제공해서: `ask_ok('파일을 덮어써도 좋습니까?', 2)`
  - 또는 모든 인자를 제공해서: `ask_ok('파일을 덮어써도 좋습니까?', 2, '자, 예나 아니요로만 답하세요!')`
  
- 이 예는 [`in`](https://docs.python.org/ko/3.12/reference/expressions.html#in) 키워드도 소개하고 있습니다. 시퀀스가 어떤 값을 가졌는지 아닌지를 검사합니다.
- 기본값은 함수 정의 시점에 _정의되고 있는_ 스코프에서 구해집니다, 그래서

```python
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
```

는 `5`를 인쇄합니다.

> [!important] 
> - 기본값은 오직 한 번만 값이 구해집니다. 이것은 기본값이 리스트나 딕셔너리나 대부분 클래스의 인스턴스와 같은 가변 객체일 때 차이를 만듭니다. 예를 들어, 다음 함수는 계속되는 호출로 전달된 인자들을 누적합니다:
> 
> ```python
> def f(a, L=[]):
>     L.append(a)
>     return L
> 
> print(f(1))
> print(f(2))
> print(f(3))
> ```
> 
> 다음과 같은 것을 인쇄합니다
> 
> ```python
> [1]
> [1, 2]
> [1, 2, 3]
> ```
> 
> - 연속된 호출 간에 기본값이 공유되지 않기를 원한다면, 대신 함수를 이런 식으로 쓸 수 있습니다:
> 
> ```python
> def f(a, L=None):
>     if L is None:
>         L = []
>     L.append(a)
>     return L
> ```
> 
### 키워드 인자

- 함수는 `kwarg=value` 형식의 [키워드 인자](https://docs.python.org/ko/3.12/glossary.html#term-keyword-argument) 를 사용해서 호출될 수 있습니다. 예를 들어, 다음 함수는:

```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
```

- 하나의 필수 인자(`voltage`)와 세 개의 선택적 인자 (`state`, `action`, `type`) 를 받아들입니다. 이 함수는 다음과 같은 방법 중 아무것으로나 호출될 수 있습니다.

```python
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
```

- 하지만 다음과 같은 호출들은 모두 올바르지 않습니다:

```python
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
```

- 함수 호출에서, 키워드 인자는 위치 인자 뒤에 나와야 합니다. 전달된 모든 키워드 인자는 함수가 받아들이는 인자 중 하나와 맞아야 하며 (예를 들어, `actor`는 `parrot` 함수의 올바른 인자가 아니다), 그 순서는 중요하지 않습니다. 이것들에는 필수 인자들도 포함됩니다 (예를 들어, `parrot(voltage=1000)` 도 올바릅니다). 어떤 인자도 두 개 이상의 값을 받을 수 없습니다. 여기, 이 제약 때문에 실패하는 예가 있습니다:


```python
>>> def function(a):
…     pass
…
>>> function(0, a=0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: function() got multiple values for argument 'a'
```

- `**name` 형식의 마지막 형식 매개변수가 존재하면, 형식 매개변수들에 대응하지 않는 모든 키워드 인자들을 담은 딕셔너리 ([매핑 형 — dict](https://docs.python.org/ko/3.12/library/stdtypes.html#typesmapping) 를 보세요) 를 받습니다. 이것은 `*name` (다음 서브섹션에서 설명합니다) 형식의 형식 매개변수와 조합될 수 있는데, 형식 매개변수 목록 밖의 위치 인자들을 담은 [튜플](https://docs.python.org/ko/3.12/tutorial/datastructures.html#tut-tuples)을 받습니다. (`*name`은 `**name` 앞에 나와야 합니다.) 예를 들어, 이런 함수를 정의하면:

```python
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
```

- 이런 식으로 호출될 수 있습니다:

```python
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
```

- 그리고 당연히 이렇게 인쇄합니다:

```text
-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.

It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
```

- 인쇄되는 키워드 인자들의 순서 함수 호출로 전달된 순서와 일치함이 보장됨에 주목하세요.

## 특수 매개 변수

- 기본적으로, 인자는 위치나 명시적인 키워드로 파이썬 함수에 전달될 수 있습니다. 가독성과 성능을 위해, 개발자가 항목이 위치, 위치나 키워드 또는 키워드로 전달되는지를 판단할 때 함수 정의만을 보면 되도록, 인자가 전달될 방법을 제한하면 좋습니다. 함수 정의는 다음과 같습니다:

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```

- 여기서 `/`와 `*`는 선택적입니다. 사용하면, 이 기호는 인자가 함수에 전달되는 방식에 따른 매개 변수의 종류를 나타냅니다: 위치 전용, 위치-키워드 및 키워드 전용. 키워드 매개 변수는 명명된(named) 매개 변수라고도 합니다.

### 위치-키워드(Positional-or-Keyword) 인자
- 함수 정의에 `/`와 `*`가 없으면, 인자를 위치나 키워드로 함수에 전달할 수 있습니다.

### 위치 전용 매개 변수

- 좀 더 자세하게 살펴보면, 특정 매개 변수를 _위치 전용_으로 표시할 수 있습니다. _위치 전용_이면, 매개 변수의 순서가 중요하며, 키워드로 매개 변수를 전달할 수 없습니다. 위치 전용 매개 변수는 `/` (슬래시) 앞에 놓입니다. `/`는 위치 전용 매개 변수를 나머지 매개 변수들로부터 논리적으로 분리하는 데 사용됩니다. 함수 정의에 `/`가 없으면, 위치 전용 매개 변수는 없습니다.
- `/` 다음의 매개 변수는 _위치-키워드_나 _키워드 전용_일 수 있습니다.

### 키워드 전용 인자
- 매개 변수를 키워드 인자로 전달해야 함을 나타내도록, 매개 변수를 _키워드 전용_으로 표시하려면, 첫 번째 _키워드 전용_ 매개 변수 바로 전에 인자 목록에 `*`를 넣으십시오.

#### 함수 예제

- `/`와 `*` 마커에 주의를 기울이는 다음 예제 함수 정의를 고려하십시오:

```python
>>> def standard_arg(arg):
…     print(arg)
…
>>> def pos_only_arg(arg, /):
…     print(arg)
…
>>> def kwd_only_arg(*, arg):
…     print(arg)
…
>>> def combined_example(pos_only, /, standard, *, kwd_only):
…     print(pos_only, standard, kwd_only)
```

- 첫 번째 함수 정의 `standard_arg`는 가장 익숙한 형식으로, 호출 규칙에 아무런 제한을 두지 않으며 인자는 위치나 키워드로 전달될 수 있습니다:

```python
>>> standard_arg(2)
2

>>> standard_arg(arg=2)
2
```

- 두 번째 함수 `pos_only_arg`는 함수 정의에 `/`가 있으므로 위치 매개 변수만 사용하도록 제한됩니다:

```python
>>> pos_only_arg(1)
1
```

```python
>>> pos_only_arg(arg=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'
```

- 세 번째 함수 `kwd_only_args`는 함수 정의에서 `*`로 표시된 키워드 인자만 허용합니다:

```python
>>> kwd_only_arg(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given

>>> kwd_only_arg(arg=3)
3
```

- 마지막은 같은 함수 정의에서 세 가지 호출 규칙을 모두 사용합니다:

```python
>>> combined_example(1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() takes 2 positional arguments but 3 were given

>>> combined_example(1, 2, kwd_only=3)
1 2 3

>>> combined_example(1, standard=2, kwd_only=3)
1 2 3

>>> combined_example(pos_only=1, standard=2, kwd_only=3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'
```

- 마지막으로, 위치 인자 `name`과 `name`을 키로 가지는 `**kwds` 사이에 잠재적인 충돌이 있는 이 함수 정의를 고려하십시오:

```
def foo(name, **kwds):
    return 'name' in kwds
```

- `'name'` 키워드는 항상 첫 번째 매개 변수에 결합하므로 `True`를 반환할 수 있는 호출은 불가능합니다. 예를 들면:

```python
>>> foo(1, **{'name': 2})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: foo() got multiple values for argument 'name'
```

- 그러나 `/`(위치 전용 인자)를 사용하면, `name`을 위치 인자로, 동시에 `'name'`을 키워드 인자의 키로 사용할 수 있으므로 가능합니다:

```python
>>> def foo(name, /, **kwds):
…     return 'name' in kwds
…
>>> foo(1, **{'name': 2})
True
```

- 즉, 위치 전용 매개 변수의 이름을 `**kwds`에서 모호함 없이 사용할 수 있습니다.

> [!summary] 
> - 사용 사례가 함수 정의에서 어떤 매개 변수를 사용할지 결정합니다:
> 
> ```python
> def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
> ```
> 
> - 매개 변수의 이름을 사용자가 사용할 수 없도록 하려면 위치 전용을 사용하십시오. 매개 변수 이름이 실제 의미가 없을 때, 함수가 호출될 때 인자의 순서를 강제하려고 할 때, 또는 일부 위치 매개 변수와 임의의 키워드를 받아들이고 싶을 때 유용합니다.
> - 이름이 의미가 있고 함수 정의가 이름을 명시적으로 지정함으로써 더 이해하기 쉬워지거나, 사용자가 전달되는 인자의 위치에 의존하지 못하도록 하려면 키워드 전용을 사용하십시오.
> - API의 경우, 향후 매개 변수의 이름이 수정될 때 비호환 API 변경이 발생하는 것을 방지하려면 위치 전용을 사용하십시오.

## 임의의 인자 목록
- 마지막으로, 가장 덜 사용되는 옵션은 함수가 임의의 개수 인자로 호출될 수 있도록 지정하는 것입니다. 이 인자들은 튜플로 묶입니다 ([튜플과 시퀀스](https://docs.python.org/ko/3.12/tutorial/datastructures.html#tut-tuples) 을 보세요). 가변 길이 인자 앞에, 없거나 여러 개의 일반 인자들이 올 수 있습니다.

```python
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
```

- 일반적으로 이러한 _변수_ 인수는 함수에 전달되는 나머지 입력 인수를 모두 퍼가기 때문에 공식 매개변수 목록에서 가장 마지막에 위치합니다. `*args` 매개변수 뒤에 오는 모든 공식 매개변수는 '키워드 전용' 인수가 되며, 이는 위치 인수가 아닌 키워드로만 사용할 수 있음을 의미합니다.

```python
>>> def concat(*args, sep="/"):
…     return sep.join(args)
…
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'
```

## 인자 목록 언 패킹
- 인자들이 이미 리스트나 튜플에 있지만, 분리된 위치 인자들을 요구하는 함수 호출을 위해 언 패킹 해야 하는 경우 반대 상황이 벌어집니다. 예를 들어, 내장 [`range()`](https://docs.python.org/ko/3.12/library/stdtypes.html#range "range") 함수는 별도의 `start`와 `stop` 인자를 기대합니다. 그것들이 따로 있지 않으면, 리스트와 튜플로부터 인자를 언 패킹하기 위해 `*`-연산자를 사용해서 함수를 호출하면 됩니다:

```python
>>> list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]
```

- 같은 방식으로 딕셔너리도 `**`-연산자를 써서 키워드 인자를 전달할 수 있습니다:

```python
>>> def parrot(voltage, state='a stiff', action='voom'):
…     print("-- This parrot wouldn't", action, end=' ')
…     print("if you put", voltage, "volts through it.", end=' ')
…     print("E's", state, "!")
…
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
```

## 람다 표현식

- [`lambda`](https://docs.python.org/ko/3.12/reference/expressions.html#lambda) 키워드들 사용해서 작고 이름 없는 함수를 만들 수 있습니다. 이 함수는 두 인자의 합을 돌려줍니다: `lambda a, b: a+b`. 함수 객체가 있어야 하는 곳이면 어디나 람다 함수가 사용될 수 있습니다. 문법적으로는 하나의 표현식으로 제한됩니다. 의미적으로는, 일반적인 함수 정의의 편의 문법일 뿐입니다. 중첩된 함수 정의처럼, 람다 함수는 둘러싸는 스코프에 있는 변수들을 참조할 수 있습니다:

```python
>>> def make_incrementor(n):
…     return lambda x: x + n
…
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
```

- 위의 예는 함수를 돌려주기 위해 람다 표현식을 사용합니다. 또 다른 용도는 작은 함수를 인자로 전달하는 것입니다:

```python
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

## 도큐멘테이션 문자열
- 여기에 도큐멘테이션 문자열의 내용과 포매팅에 관한 몇 가지 관례가 있습니다.
  - 첫 줄은 항상 객체의 목적을 짧고, 간결하게 요약해야 합니다. 간결함을 위해, 객체의 이름이나 형을 명시적으로 언급하지 않아야 하는데, 이것들은 다른 방법으로 제공되기 때문입니다 (이름이 함수의 작업을 설명하는 동사라면 예외입니다). 이 줄은 대문자로 시작하고 마침표로 끝나야 합니다.
  - 도큐멘테이션 문자열에 여러 줄이 있다면, 두 번째 줄은 비어있어서, 시각적으로 요약과 나머지 설명을 분리해야 합니다. 뒤따르는 줄들은 하나나 그 이상의 문단으로, 객체의 호출 규약, 부작용 등을 설명해야 합니다.
  - 파이썬 파서는 여러 줄 문자열 리터럴에서 들여쓰기를 제거하지 않기 때문에, 설명서를 처리하는 도구들은 필요하면 들여쓰기를 제거합니다. 이것은 다음과 같은 관례를 사용합니다. 문자열의 첫줄 _뒤에 오는_ 첫 번째 비어있지 않은 줄이 전체 도튜멘테이션 문자열의 들여쓰기 수준을 결정합니다. (우리는 첫 줄을 사용할 수 없는데, 일반적으로 문자열을 시작하는 따옴표에 붙어있어서 들여쓰기가 문자열 리터럴의 것을 반영하지 않기 때문입니다.) 이 들여쓰기와 “동등한” 공백이 문자열의 모든 줄의 시작 부분에서 제거됩니다. 덜 들여쓰기 된 줄이 나타나지는 말아야 하지만, 나타난다면 모든 앞부분의 공백이 제거됩니다. 공백의 동등성은 탭 확장 (보통 8개의 스페이스) 후에 검사됩니다.
- 여기 여러 줄 독스트링의 예가 있습니다:

```python
>>> def my_function():
… """Do nothing, but document it.
…
…     No, really, it doesn't do anything.
…     """
…     pass
…
>>> print(my_function.__doc__)
Do nothing, but document it.

    No, really, it doesn't do anything.
```

## 함수 어노테이션
- [함수 어노테이션](https://docs.python.org/ko/3.12/reference/compound_stmts.html#function) 은 사용자 정의 함수가 사용하는 형들에 대한 완전히 선택적인 메타데이터 정보입니다 (자세한 내용은 [**PEP 3107**](https://peps.python.org/pep-3107/) 과 [**PEP 484**](https://peps.python.org/pep-0484/) 를 보세요).
- [어노테이션](https://docs.python.org/ko/3.12/glossary.html#term-function-annotation)은 함수의 `__annotations__` 속성에 사전으로 저장되며 함수의 다른 부분에는 영향을 미치지 않습니다. 매개변수 어노테이션은 매개변수 이름 뒤에 콜론으로 정의되고 그 뒤에 어노테이션의 값으로 평가되는 표현식이 이어집니다. 반환 어노테이션은 매개변수 목록과 [`def`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#def) 문의 끝을 나타내는 콜론 사이에 리터럴 `->`와 식이 뒤에 오는 것으로 정의됩니다. 다음 예제에는 필수 인수, 선택적 인수 및 반환 값에 주석이 지정되어 있습니다:

```python
>>> def f(ham: str, eggs: str = 'eggs') -> str:
…     print("Annotations:", f.__annotations__)
…     print("Arguments:", ham, eggs)
…     return ham + ' and ' + eggs
…
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```


## 내장 함수
[내장 함수 — Python 3.12.5 문서](https://docs.python.org/ko/3.12/library/functions.html)

### `len`

```python
print(len("Hello")) # 결과: 5
```

- `len(variable)` 은 입력한 iterable 의 길이를 반환한다.

---

## 참조
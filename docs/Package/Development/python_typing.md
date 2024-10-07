---
title: "[Python] 타이핑 (Typing)"
excerpt: 
categories:
  - Python
tags:
  - Python-Library
  - Python-typing
last_modified_at: 2024-03-01T00:00:00-00:00
link: https://docs.python.org/ko/3.12/library/typing.html
상위 항목: "[[python_development|파이썬 개발 라이브러리 (Python Development Library)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

---
> [!NOTE]
> 파이썬 런타임은 함수와 변수 타입 어노테이션을 강제하지 않습니다. 이들은 타입 체커, IDE, 린터 등과 같은 서드파티 도구에서 사용될 수 있습니다.

이 모듈은 타입 힌트에 대한 런타임 지원을 제공합니다.

다음 함수를 고려해보세요:

```python
def surface_area_of_cube(edge_length: float) -> str:
    return f"The surface area of the cube is {6 * edge_length ** 2}."
```

`surface_area_of_cube` 함수는 타입 힌트 `edge_length: float`로 표시된 대로 float의 인스턴스로 예상되는 인수를 받습니다. 이 함수는 `-> str` 힌트로 표시된 대로 str의 인스턴스를 반환할 것으로 예상됩니다.

타입 힌트는 float나 str와 같은 단순한 클래스일 수 있지만, 더 복잡할 수도 있습니다. typing 모듈은 더 고급 타입 힌트의 어휘를 제공합니다.

새로운 기능들이 자주 typing 모듈에 추가됩니다. typing_extensions 패키지는 이러한 새 기능들을 이전 버전의 파이썬으로 백포트합니다.

> [!seealso]
> [“Typing cheat sheet”](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
> 타입 힌트의 빠른 개요 (mypy 문서에서 호스팅됨)
> 
> [the mypy docs](https://mypy.readthedocs.io/en/stable/index.html) 의 "Type System Reference" 섹션
> 파이썬 타이핑 시스템은 PEP를 통해 표준화되므로, 이 참조는 대부분의 파이썬 타입 체커에 광범위하게 적용되어야 합니다. (일부는 여전히 mypy에 특정될 수 있습니다.)
> 
> [“Static Typing with Python”](https://typing.readthedocs.io/en/latest/)
> 타입 시스템 기능, 유용한 타이핑 관련 도구 및 타이핑 모범 사례를 자세히 설명하는 커뮤니티에서 작성한 타입 체커에 구애받지 않는 문서.

## 파이썬 타입 시스템 명세 (Specification for the Python Type System)

파이썬 타입 시스템의 최신 정식 명세는 "Specification for the Python type system"에서 찾을 수 있습니다.

## 타입 별칭 (Type aliases)

타입 별칭은 TypeAliasType의 인스턴스를 생성하는 type 문을 사용하여 정의됩니다. 이 예제에서, Vector와 list[float]는 정적 타입 체커에 의해 동등하게 취급됩니다:

```python
type Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# 타입 검사를 통과합니다; float 리스트는 Vector로 간주됩니다.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
```

타입 별칭은 복잡한 타입 서명을 단순화하는 데 유용합니다. 예를 들면:

```python
from collections.abc import Sequence

type ConnectionOptions = dict[str, str]
type Address = tuple[str, int]
type Server = tuple[Address, ConnectionOptions]

def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    …

# 정적 타입 체커는 이전 타입 서명을 다음과 정확히 동등한 것으로 취급합니다.
def broadcast_message(
    message: str,
    servers: Sequence[tuple[tuple[str, int], dict[str, str]]]
) -> None:
    …
```

type 문은 파이썬 3.12에서 새로 도입되었습니다. 이전 버전과의 호환성을 위해, 타입 별칭은 단순 할당을 통해서도 생성할 수 있습니다:

```python
Vector = list[float]
```

또는 TypeAlias로 표시하여 이것이 일반 변수 할당이 아닌 타입 별칭임을 명시적으로 나타낼 수 있습니다:

```python
from typing import TypeAlias

Vector: TypeAlias = list[float]
```

## NewType

구별되는 타입을 생성하려면 NewType 헬퍼를 사용하세요:

```python
from typing import NewType

UserId = NewType('UserId', int)
some_id = UserId(524313)
```

정적 타입 체커는 새 타입을 원래 타입의 서브클래스인 것처럼 취급합니다. 이는 논리적 오류를 잡는 데 유용합니다:

```python
def get_user_name(user_id: UserId) -> str:
    …

# 타입 검사 통과
user_a = get_user_name(UserId(42351))

# 타입 검사 실패; int는 UserId가 아님
user_b = get_user_name(-1)
```

UserId 타입의 변수에 대해 여전히 모든 int 연산을 수행할 수 있지만, 결과는 항상 int 타입이 됩니다. 이는 int가 예상되는 모든 곳에 UserId를 전달할 수 있지만, 잘못된 방식으로 의도치 않게 UserId를 만들지 않도록 합니다:

```python
# 'output'은 'UserId'가 아닌 'int' 타입입니다
output = UserId(23413) + UserId(54341)
```

이러한 검사는 정적 타입 체커에 의해서만 강제된다는 점에 주의하세요. 런타임에 `Derived = NewType('Derived', Base)` 문은 Derived를 전달받은 매개변수를 즉시 반환하는 호출 가능한 객체로 만듭니다. 즉, `Derived(some_value)` 표현식은 새로운 클래스를 생성하거나 일반 함수 호출 이상의 오버헤드를 도입하지 않습니다.

더 정확히 말하면, `some_value is Derived(some_value)` 표현식은 런타임에 항상 True입니다.

Derived의 서브타입을 생성하는 것은 유효하지 않습니다:

```python
from typing import NewType

UserId = NewType('UserId', int)

# 런타임에 실패하고 타입 검사를 통과하지 못합니다
class AdminUserId(UserId): pass
```

그러나 '파생된' NewType을 기반으로 NewType을 생성하는 것은 가능합니다:

```python
from typing import NewType

UserId = NewType('UserId', int)

ProUserId = NewType('ProUserId', UserId)
```

그리고 ProUserId에 대한 타입 검사는 예상대로 작동합니다.

자세한 내용은 PEP 484를 참조하세요.

> [!NOTE]
> 타입 별칭의 사용은 두 타입이 서로 동등함을 선언한다는 것을 기억하세요. `type Alias = Original`을 하면 정적 타입 체커는 모든 경우에 Alias를 Original과 정확히 동등한 것으로 취급합니다. 이는 복잡한 타입 서명을 단순화하고 싶을 때 유용합니다.

반면에, NewType은 한 타입을 다른 타입의 서브타입으로 선언합니다. `Derived = NewType('Derived', Original)`은 정적 타입 체커가 Derived를 Original의 서브클래스로 취급하게 합니다. 이는 Original 타입의 값이 Derived 타입의 값이 예상되는 위치에서 사용될 수 없음을 의미합니다. 이는 런타임 비용을 최소화하면서 논리적 오류를 방지하려는 경우에 유용합니다.

> 버전 3.5.2에서 추가되었습니다.
> 버전 3.10에서 변경: NewType은 이제 함수가 아닌 클래스입니다. 결과적으로 일반 함수에 비해 NewType을 호출할 때 약간의 추가 런타임 비용이 있습니다.
> 버전 3.11에서 변경: NewType 호출의 성능이 파이썬 3.9 수준으로 복원되었습니다.

## 호출 가능한 객체에 주석 달기 (Annotating callable objects)

함수나 다른 [호출 가능한](https://docs.python.org/ko/3.12/glossary.html#term-callable) 객체는 [`collections.abc.Callable`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable") 또는 더 이상 사용되지 않는 [`typing.Callable`](https://docs.python.org/ko/3.12/library/typing.html#typing.Callable "typing.Callable")을 사용하여 주석을 달 수 있습니다. `Callable[[int], str]`는 [`int`](https://docs.python.org/ko/3.12/library/functions.html#int "int") 타입의 단일 매개변수를 받아 [`str`](https://docs.python.org/ko/3.12/library/stdtypes.html#str "str")을 반환하는 함수를 의미합니다.

예를 들어:

```python
from collections.abc import Callable, Awaitable

def feeder(get_next_item: Callable[[], str]) -> None:
    …  # 본문

def async_query(on_success: Callable[[int], None],
                on_error: Callable[[int, Exception], None]) -> None:
    …  # 본문

async def on_update(value: str) -> None:
    …  # 본문

callback: Callable[[str], Awaitable[None]] = on_update
```

구독 구문은 항상 정확히 두 개의 값, 즉 인수 목록과 반환 타입으로 사용되어야 합니다. 인수 목록은 타입 목록, [`ParamSpec`](https://docs.python.org/ko/3.12/library/typing.html#typing.ParamSpec "typing.ParamSpec"), [`Concatenate`](https://docs.python.org/ko/3.12/library/typing.html#typing.Concatenate "typing.Concatenate"), 또는 줄임표여야 합니다. 반환 타입은 단일 타입이어야 합니다.

리터럴 줄임표 `…`가 인수 목록으로 주어지면, 임의의 매개변수 목록을 가진 호출 가능한 객체가 허용됨을 나타냅니다:

```python
def concat(x: str, y: str) -> str:
    return x + y

x: Callable[…, str]
x = str     # 가능
x = concat  # 역시 가능
```

`Callable`은 가변 개수의 인수를 받는 함수, [오버로드된 함수](https://docs.python.org/ko/3.12/library/typing.html#overload), 또는 키워드 전용 매개변수가 있는 함수와 같은 복잡한 서명을 표현할 수 없습니다. 그러나 이러한 서명은 [`__call__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__call__ "object.__call__") 메서드가 있는 [`Protocol`](https://docs.python.org/ko/3.12/library/typing.html#typing.Protocol "typing.Protocol") 클래스를 정의하여 표현할 수 있습니다:

```python
from collections.abc import Iterable
from typing import Protocol

class Combiner(Protocol):
    def __call__(self, *vals: bytes, maxlen: int | None = None) -> list[bytes]: …

def batch_proc(data: Iterable[bytes], cb_results: Combiner) -> bytes:
    for item in data:
        …

def good_cb(*vals: bytes, maxlen: int | None = None) -> list[bytes]:
    …
def bad_cb(*vals: bytes, maxitems: int | None) -> list[bytes]:
    …

batch_proc([], good_cb)  # 가능
batch_proc([], bad_cb)   # 오류! 인수 2는 콜백의 이름과 종류가 다르기 때문에 호환되지 않는 타입입니다
```

다른 호출 가능한 객체를 인수로 받는 호출 가능한 객체는 [`ParamSpec`](https://docs.python.org/ko/3.12/library/typing.html#typing.ParamSpec "typing.ParamSpec")을 사용하여 매개변수 타입이 서로 의존적임을 나타낼 수 있습니다. 또한 해당 호출 가능한 객체가 다른 호출 가능한 객체에서 인수를 추가하거나 제거하는 경우 [`Concatenate`](https://docs.python.org/ko/3.12/library/typing.html#typing.Concatenate "typing.Concatenate") 연산자를 사용할 수 있습니다. 이들은 각각 `Callable[ParamSpecVariable, ReturnType]`과 `Callable[Concatenate[Arg1Type, Arg2Type, …, ParamSpecVariable], ReturnType]` 형태를 취합니다.

> 버전 3.10에서 변경: `Callable`이 이제 [`ParamSpec`](https://docs.python.org/ko/3.12/library/typing.html#typing.ParamSpec "typing.ParamSpec")과 [`Concatenate`](https://docs.python.org/ko/3.12/library/typing.html#typing.Concatenate "typing.Concatenate")를 지원합니다. 자세한 내용은 [**PEP 612**](https://peps.python.org/pep-0612/)를 참조하세요.

> [!seealso]
> [`ParamSpec`](https://docs.python.org/ko/3.12/library/typing.html#typing.ParamSpec "typing.ParamSpec")과 [`Concatenate`](https://docs.python.org/ko/3.12/library/typing.html#typing.Concatenate "typing.Concatenate")에 대한 문서는 `Callable`에서의 사용 예를 제공합니다.

## 제네릭 (Generics)

컨테이너에 보관된 객체에 대한 타입 정보를 일반적인 방식으로 정적으로 추론할 수 없기 때문에, 표준 라이브러리의 많은 컨테이너 클래스는 컨테이너 요소의 예상 타입을 나타내기 위해 구독을 지원합니다.

```python
from collections.abc import Mapping, Sequence

class Employee: …

# Sequence[Employee]는 시퀀스의 모든 요소가
# "Employee" 인스턴스여야 함을 나타냅니다.
# Mapping[str, str]은 매핑의 모든 키와 값이
# 문자열이어야 함을 나타냅니다.
def notify_by_email(employees: Sequence[Employee],
                    overrides: Mapping[str, str]) -> None: …
```

제네릭 함수와 클래스는 [타입 매개변수 구문](https://docs.python.org/ko/3.12/reference/compound_stmts.html#type-params)을 사용하여 매개변수화할 수 있습니다:

```python
from collections.abc import Sequence

def first[T](l: Sequence[T]) -> T:  # 함수는 TypeVar "T"에 대해 제네릭입니다
    return l[0]
```

또는 [`TypeVar`](https://docs.python.org/ko/3.12/library/typing.html#typing.TypeVar "typing.TypeVar") 팩토리를 직접 사용할 수 있습니다:

```python
from collections.abc import Sequence
from typing import TypeVar

U = TypeVar('U')                  # 타입 변수 "U" 선언

def second(l: Sequence[U]) -> U:  # 함수는 TypeVar "U"에 대해 제네릭입니다
    return l[1]
```

> 버전 3.12에서 변경: 제네릭에 대한 구문 지원은 Python 3.12에서 새로 추가되었습니다.

## 튜플에 주석 달기 (Annotating tuples)

Python의 대부분의 컨테이너에 대해, 타이핑 시스템은 컨테이너의 모든 요소가 동일한 타입일 것이라고 가정합니다. 예를 들어:

```python
from collections.abc import Mapping

# 타입 검사기는 ``x``의 모든 요소가 int여야 한다고 추론합니다
x: list[int] = []

# 타입 검사기 오류: ``list``는 단일 타입 인수만 허용합니다:
y: list[int, str] = [1, 'foo']

# 타입 검사기는 ``z``의 모든 키가 문자열이어야 하고,
# 모든 값이 문자열 또는 정수여야 한다고 추론합니다
z: Mapping[str, str | int] = {}
```

[`list`](https://docs.python.org/ko/3.12/library/stdtypes.html#list "list")는 하나의 타입 인수만 허용하므로, 타입 검사기는 위의 `y` 할당에 대해 오류를 발생시킬 것입니다. 마찬가지로, [`Mapping`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Mapping "collections.abc.Mapping")은 두 개의 타입 인수만 허용합니다: 첫 번째는 키의 타입을 나타내고, 두 번째는 값의 타입을 나타냅니다.

그러나 대부분의 다른 Python 컨테이너와 달리, 관용적인 Python 코드에서는 튜플이 모두 같은 타입이 아닌 요소를 가지는 것이 일반적입니다. 이러한 이유로, Python의 타이핑 시스템에서 튜플은 특별히 취급됩니다. [`tuple`](https://docs.python.org/ko/3.12/library/stdtypes.html#tuple "tuple")은 타입 인수를 여러 개 허용합니다:

```python
# 가능: ``x``는 길이가 1인 튜플에 할당되며, 유일한 요소는 int입니다
x: tuple[int] = (5,)

# 가능: ``y``는 길이가 2인 튜플에 할당됩니다;
# 첫 번째 요소는 int, 두 번째 요소는 str입니다
y: tuple[int, str] = (5, "foo")

# 오류: 타입 주석은 길이가 1인 튜플을 나타내지만,
# ``z``는 길이가 3인 튜플에 할당되었습니다
z: tuple[int] = (1, 2, 3)
```

임의의 길이를 가질 수 있고 모든 요소가 타입 `T`인 튜플을 나타내려면 `tuple[T, …]`를 사용하세요. 빈 튜플을 나타내려면 `tuple[()]`를 사용하세요. 주석으로 단순히 `tuple`을 사용하는 것은 `tuple[Any, …]`를 사용하는 것과 동일합니다:

```python
x: tuple[int, …] = (1, 2)
# 이러한 재할당은 가능합니다: ``tuple[int, …]``는 x가 임의의 길이를 가질 수 있음을 나타냅니다
x = (1, 2, 3)
x = ()
# 이 재할당은 오류입니다: ``x``의 모든 요소는 int여야 합니다
x = ("foo", "bar")

# ``y``는 오직 빈 튜플에만 할당될 수 있습니다
y: tuple[()] = ()

z: tuple = ("foo", "bar")
# 이러한 재할당은 가능합니다: 단순 ``tuple``은 ``tuple[Any, …]``와 동일합니다
z = (1, 2, 3)
z = ()
```

## 클래스 객체의 타입 (The type of class objects)

`C`로 주석이 달린 변수는 `C` 타입의 값을 받을 수 있습니다. 반면에, `type[C]`로 주석이 달린 변수는 클래스 자체인 값을 받을 수 있습니다 - 구체적으로, `C`의 클래스 객체를 받습니다. 예를 들어:

```python
a = 3         # ``int`` 타입을 가짐
b = int       # ``type[int]`` 타입을 가짐
c = type(a)   # 또한 ``type[int]`` 타입을 가짐
```

`type[C]`는 공변성을 가진다는 점에 주목하세요:

```python
class User: …
class ProUser(User): …
class TeamUser(User): …

def make_new_user(user_class: type[User]) -> User:
    # …
    return user_class()

make_new_user(User)      # 정상
make_new_user(ProUser)   # 또한 정상: ``type[ProUser]``는 ``type[User]``의 하위 타입
make_new_user(TeamUser)  # 여전히 정상
make_new_user(User())    # 오류: ``type[User]``를 예상했지만 ``User``를 받음
make_new_user(int)       # 오류: ``type[int]``는 ``type[User]``의 하위 타입이 아님
```

`type`에 대한 유일한 합법적인 매개변수는 클래스, `Any`, 타입 변수, 그리고 이러한 타입들의 유니온입니다. 예를 들어:

```python
def new_non_team_user(user_class: type[BasicUser | ProUser]): …

new_non_team_user(BasicUser)  # 정상
new_non_team_user(ProUser)    # 정상
new_non_team_user(TeamUser)   # 오류: ``type[TeamUser]``는 
                              # ``type[BasicUser | ProUser]``의 하위 타입이 아님
new_non_team_user(User)       # 또한 오류
```

`type[Any]`는 `type`과 동등하며, 이는 Python의 메타클래스 계층의 루트입니다.

## 제너레이터와 코루틴에 주석 달기 (Annotating generators and coroutines)

제너레이터는 제네릭 타입 `Generator[YieldType, SendType, ReturnType]`을 사용하여 주석을 달 수 있습니다. 예를 들어:

```python
def echo_round() -> Generator[int, float, str]:
    sent = yield 0
    while sent >= 0:
        sent = yield round(sent)
    return 'Done'
```

표준 라이브러리의 다른 많은 제네릭 클래스와 달리, `Generator`의 `SendType`은 공변성이나 불변성이 아닌 반공변성을 가진다는 점에 주목하세요.
제너레이터가 값을 일드(yield)하기만 하면, `SendType`과 `ReturnType`을 `None`으로 설정하십시오:

```python
def infinite_stream(start: int) -> Generator[int, None, None]:
    while True:
        yield start
        start += 1
```

또는, `Iterable[YieldType]`이나 `Iterator[YieldType]` 중 하나의 반환형을 갖는 것으로 제너레이터를 어노테이트 하십시오:

```python
def infinite_stream(start: int) -> Iterator[int]:
    while True:
        yield start
        start += 1
```

비동기 제너레이터도 비슷한 방식으로 처리되지만, `ReturnType` 타입 인자를 기대하지 않습니다 (`AsyncGenerator[YieldType, SendType]`):

```python
async def infinite_stream(start: int) -> AsyncGenerator[int, None]:
    while True:
        yield start
        start = await increment(start)
```

동기적인 경우와 마찬가지로, `AsyncIterable[YieldType]`과 `AsyncIterator[YieldType]`도 사용 가능합니다:

```python
async def infinite_stream(start: int) -> AsyncIterator[int]:
    while True:
        yield start
        start = await increment(start)
```

코루틴은 `Coroutine[YieldType, SendType, ReturnType]`을 사용하여 주석을 달 수 있습니다. 제네릭 인자는 `Generator`의 것과 일치합니다. 예를 들어:

```python
from collections.abc import Coroutine
c: Coroutine[list[str], str, int]  # 다른 곳에서 정의된 일부 코루틴
x = c.send('hi')                   # 'x'의 추론된 타입은 list[str]
async def bar() -> None:
    y = await c                    # 'y'의 추론된 타입은 int
```

## 사용자 정의 제네릭 형 (User-defined generic types)

사용자 정의 클래스는 제네릭 클래스로 정의 할 수 있습니다.

```python
from logging import Logger

class LoggedVar[T]:
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('%s: %s', self.name, message)
```

이 구문은 `LoggedVar` 클래스가 단일 타입 변수 `T`를 중심으로 매개변수화되었음을 나타냅니다. 이는 또한 클래스 본문 내에서 `T`를 유효한 타입으로 만듭니다.

제네릭 클래스는 암시적으로 `Generic`을 상속합니다. Python 3.11 이하 버전과의 호환성을 위해, 제네릭 클래스를 나타내기 위해 `Generic`을 명시적으로 상속하는 것도 가능합니다:

```python
from typing import TypeVar, Generic

T = TypeVar('T')

class LoggedVar(Generic[T]):
    …
```

제네릭 클래스는 `__class_getitem__()` 메서드를 가지고 있어, 런타임에 매개변수화될 수 있습니다 (아래의 `LoggedVar[int]`와 같이):

```python
from collections.abc import Iterable

def zero_all_vars(vars: Iterable[LoggedVar[int]]) -> None:
    for var in vars:
        var.set(0)
```

제네릭 타입은 여러 개의 타입 변수를 가질 수 있습니다. 모든 종류의 `TypeVar`가 제네릭 타입의 매개변수로 허용됩니다:

```python
from typing import TypeVar, Generic, Sequence

class WeirdTrio[T, B: Sequence[bytes], S: (int, str)]:
    …

OldT = TypeVar('OldT', contravariant=True)
OldB = TypeVar('OldB', bound=Sequence[bytes], covariant=True)
OldS = TypeVar('OldS', int, str)

class OldWeirdTrio(Generic[OldT, OldB, OldS]):
    …
```

`Generic`에 대한 각 형 변수 인자는 달라야 합니다. 그래서 이것은 잘못되었습니다:

```python
from typing import TypeVar, Generic
…

class Pair[M, M]:  # SyntaxError
    …

T = TypeVar('T')

class Pair(Generic[T, T]):   # 잘못됨
    …
```

제네릭 클래스는 다른 클래스로부터 상속받을 수도 있습니다:

```python
from collections.abc import Sized

class LinkedList[T](Sized):
    …
```

제네릭 클래스를 상속받을 때, 일부 타입 매개변수를 고정할 수 있습니다:

```python
from collections.abc import Mapping

class MyDict[T](Mapping[str, T]):
    …
```

이 경우 `MyDict`는 단일 매개 변수 `T`를 갖습니다.

타입 매개변수를 지정하지 않고 제네릭 클래스를 사용하면 각 위치에 대해 Any를 가정합니다. 다음 예에서 MyIterable은 제네릭이 아니지만 암시적으로 `Iterable[Any]`에서 상속받습니다:

```python
from collections.abc import Iterable

class MyIterable(Iterable): # Iterable[Any]와 동일
    …
```

사용자 정의 제네릭 타입 별칭도 지원됩니다. 예시:

```python
from collections.abc import Iterable

type Response[S] = Iterable[S] | int

# 여기서 반환 타입은 Iterable[str] | int와 동일합니다
def response(query: str) -> Response[str]:
    …

type Vec[T] = Iterable[tuple[T, T]]

def inproduct[T: (int, float, complex)](v: Vec[T]) -> T: # Iterable[tuple[T, T]]와 동일
    return sum(x*y for x, y in v)
```

하위 호환성을 위해 제네릭 타입 별칭은 단순 할당을 통해서도 생성할 수 있습니다:

```python
from collections.abc import Iterable
from typing import TypeVar

S = TypeVar("S")
Response = Iterable[S] | int
```

> 버전 3.7에서 변경: Generic에는 더는 사용자 정의 메타 클래스가 없습니다.
> 버전 3.12에서 변경: 제네릭과 타입 별칭에 대한 구문 지원은 버전 3.12에서 새롭게 추가되었습니다. 이전에는 제네릭 클래스가 Generic에서 명시적으로 상속받거나 기본 중 하나에 타입 변수를 포함해야 했습니다.

매개변수 표현식에 대한 사용자 정의 제네릭도 `[**P]` 형식의 매개변수 지정 변수를 통해 지원됩니다. 매개변수 지정 변수는 typing 모듈에 의해 특수화된 타입 변수로 취급되므로 동작은 위에서 설명한 타입 변수와 일관됩니다. 유일한 예외는 ParamSpec를 대체하기 위해 타입 목록을 사용할 수 있다는 것입니다:

```python
>>> class Z[T, **P]: …  # T는 TypeVar; P는 ParamSpec
…
>>> Z[int, [dict, float]]
__main__.Z[int, [dict, float]]
```

ParamSpec에 대해 제네릭한 클래스는 Generic에서 명시적 상속을 사용하여 생성할 수도 있습니다. 이 경우 **는 사용되지 않습니다:

```python
from typing import ParamSpec, Generic

P = ParamSpec('P')

class Z(Generic[P]):
    …
```

TypeVar와 ParamSpec의 또 다른 차이점은 매개변수 지정 변수가 하나만 있는 제네릭이 미학적 이유로 `X[[Type1, Type2, …]]` 형식과 `X[Type1, Type2, …]` 형식의 매개변수 목록을 모두 받아들인다는 것입니다. 내부적으로 후자는 전자로 변환되므로 다음은 동등합니다:

```python
>>> class X[**P]: …
…
>>> X[int, str]
__main__.X[[int, str]]
>>> X[[int, str]]
__main__.X[[int, str]]
```

ParamSpec가 있는 제네릭은 주로 정적 타입 검사를 위한 것이므로 일부 경우에 대체 후 올바른 `__parameters__`를 가지지 않을 수 있습니다.

버전 3.10에서 변경: Generic은 이제 매개변수 표현식에 대해 매개변수화될 수 있습니다. 자세한 내용은 ParamSpec와 PEP 612를 참조하세요.

사용자 정의 제네릭 클래스는 메타클래스 충돌 없이 ABC를 기본 클래스로 가질 수 있습니다. 제네릭 메타클래스는 지원되지 않습니다. 제네릭의 매개변수화 결과는 캐시되며, typing 모듈의 대부분의 타입은 해시 가능하고 동등성을 비교할 수 있습니다.

### Any 형

특수한 종류의 형은 Any입니다. 정적 형 검사기는 모든 형을 Any와 호환되는 것으로, Any를 모든 형과 호환되는 것으로 취급합니다.
이것은 Any 형의 값에 대해 어떤 연산이나 메서드 호출을 수행하고, 그것을 임의의 변수에 대입할 수 있다는 것을 의미합니다:

```python
from typing import Any

a: Any = None
a = []          # OK
a = 2           # OK

s: str = ''
s = a           # OK

def foo(item: Any) -> int:
    # 타입 검사를 통과합니다; 'item'은 어떤 타입이든 될 수 있으며,
    # 그 타입은 'bar' 메서드를 가질 수 있습니다
    item.bar()
    …
```

Any 타입의 값을 더 정확한 타입에 할당할 때는 타입 검사가 수행되지 않습니다. 예를 들어, 정적 타입 검사기는 s가 str 타입으로 선언되었고 런타임에 int 값을 받음에도 불구하고 a를 s에 할당할 때 오류를 보고하지 않았습니다!

또한, 반환형이나 매개변수 형이 없는 모든 함수는 묵시적으로 Any 기본값을 사용합니다:

```python
def legacy_parser(text):
    …
    return data

# 정적 타입 검사기는 위의 함수를 다음과 동일한 서명으로 취급합니다:
def legacy_parser(text: Any) -> Any:
    …
    return data
```

이 동작은 여러분이 동적으로 형이 지정되는 코드와 정적으로 형이 지정되는 코드를 혼합해야 할 때 Any를 탈출구로 사용할 수 있도록 합니다.

Any의 동작과 object의 동작을 대조하십시오. Any와 유사하게, 모든 형은 object의 서브 형입니다. 그러나, Any와는 달리, 그 반대는 사실이 아닙니다: object는 다른 모든 형의 서브 형이 아닙니다.

이것은 값의 형이 object일 때, 형 검사기가 그것에 대한 거의 모든 연산을 거부하고, 그것을 더 특수한 형의 변수에 대입(또는 그것을 반환 값으로 사용)하는 것이 형 에러임을 의미합니다. 예를 들면:

```python
def hash_a(item: object) -> int:
    # 타입 검사 실패; object에는 'magic' 메서드가 없습니다.
    item.magic()
    …

def hash_b(item: Any) -> int:
    # 타입 검사 통과
    item.magic()
    …

# int와 str이 object의 서브클래스이므로 타입 검사 통과
hash_a(42)
hash_a("foo")

# Any가 모든 타입과 호환되므로 타입 검사 통과
hash_b(42)
hash_b("foo")
```

값이 형 안전한 방식으로 모든 형이 될 수 있음을 표시하려면 object를 사용하십시오. 값이 동적으로 형이 지정됨을 표시하려면 Any를 사용하십시오.

## 명목적 대 구조적 서브 타이핑

처음에 PEP 484는 Python 정적 타입 시스템을 명목적 서브타이핑을 사용하는 것으로 정의했습니다. 이는 클래스 A가 클래스 B의 하위 클래스인 경우에만 A가 B가 예상되는 곳에서 허용된다는 것을 의미합니다.

이 요구 사항은 이전에 Iterable과 같은 추상 베이스 클래스에도 적용되었습니다. 이 접근 방식의 문제점은 이것을 지원하려면 클래스를 명시적으로 표시해야만 한다는 점입니다. 이는 파이썬답지 않고 관용적인 동적으로 형이 지정된 파이썬 코드에서 일반적으로 수행하는 것과는 다릅니다. 예를 들어, 이것은 PEP 484를 만족합니다:

```python
from collections.abc import Sized, Iterable, Iterator

class Bucket(Sized, Iterable[int]):
    …
    def __len__(self) -> int: …
    def __iter__(self) -> Iterator[int]: …
```

PEP 544는 사용자가 클래스 정의에서 명시적인 베이스 클래스 없이 위의 코드를 작성할 수 있게 함으로써 이 문제를 풀도록 합니다. 정적 형 검사기가 Bucket을 Sized와 Iterable[int]의 서브 형으로 묵시적으로 취급하도록 합니다. 이것은 구조적 서브 타이핑(또는 정적 덕 타이핑)으로 알려져 있습니다:

```python
from collections.abc import Iterator, Iterable

class Bucket:  # Note: no base classes
    …
    def __len__(self) -> int: …
    def __iter__(self) -> Iterator[int]: …

def collect(items: Iterable[int]) -> int: …
result = collect(Bucket())  # Passes type check
```

또한, 특별한 클래스 Protocol을 서브 클래싱 함으로써, 사용자는 새로운 사용자 정의 프로토콜을 정의하여 구조적 서브 타이핑을 완전히 누릴 수 있습니다 (아래 예를 참조하십시오).

## 모듈 내용

typing 모듈은 다음 클래스, 함수 및 데코레이터를 정의합니다.

### 특수 타이핑 프리미티브

#### 특수형 (Special types)

이들은 주석에서 타입으로 사용될 수 있습니다. `[]`를 사용한 구독을 지원하지 않습니다.

`typing.Any`

제한되지 않는 형을 나타내는 특수형.

- 모든 형은 Any와 호환됩니다.
- Any는 모든 형과 호환됩니다.

> 버전 3.11에서 변경: Any는 이제 기본 클래스로 사용될 수 있습니다. 이는 어디서나 덕 타이핑할 수 있거나 매우 동적인 클래스에 대한 타입 검사기 오류를 피하는 데 유용할 수 있습니다.

`typing.AnyStr`

제약된 타입 변수입니다.

정의:

```python
AnyStr = TypeVar('AnyStr', str, bytes)
```

AnyStr은 str 또는 bytes 인수를 받을 수 있지만 둘을 혼합할 수 없는 함수에 사용하기 위한 것입니다.

예를 들면:

```python
def concat(a: AnyStr, b: AnyStr) -> AnyStr:
    return a + b

concat("foo", "bar")    # OK, output has type 'str'
concat(b"foo", b"bar")  # OK, output has type 'bytes'
concat("foo", b"bar")   # Error, cannot mix str and bytes
```

이름에도 불구하고 AnyStr은 Any 타입과 아무 관련이 없으며 "모든 문자열"을 의미하지도 않습니다. 특히, AnyStr과 str | bytes는 서로 다르며 다른 사용 사례를 가집니다:

```python
# Invalid use of AnyStr:
# The type variable is used only once in the function signature,
# so cannot be "solved" by the type checker
def greet_bad(cond: bool) -> AnyStr:
    return "hi there!" if cond else b"greetings!"

# The better way of annotating this function:
def greet_proper(cond: bool) -> str | bytes:
    return "hi there!" if cond else b"greetings!"
```

`typing.LiteralString`

리터럴 문자열만 포함하는 특수 타입입니다.

모든 문자열 리터럴은 LiteralString과 호환되며, 다른 LiteralString도 마찬가지입니다. 그러나 단순히 str로 타입이 지정된 객체는 호환되지 않습니다. LiteralString 타입의 객체로 구성된 문자열도 LiteralString으로 허용됩니다.

예:

```python
def run_query(sql: LiteralString) -> None:
    …

def caller(arbitrary_string: str, literal_string: LiteralString) -> None:
    run_query("SELECT * FROM students")  # OK
    run_query(literal_string)  # OK
    run_query("SELECT * FROM " + literal_string)  # OK
    run_query(arbitrary_string)  # type checker error
    run_query(  # type checker error
        f"SELECT * FROM students WHERE name = {arbitrary_string}"
    )
```

LiteralString은 임의의 사용자 생성 문자열이 문제를 일으킬 수 있는 민감한 API에 유용합니다. 예를 들어, 위의 타입 검사기 오류를 생성하는 두 경우는 SQL 인젝션 공격에 취약할 수 있습니다.

자세한 내용은 PEP 675를 참조하세요.

버전 3.11에서 추가되었습니다.

`typing.Never`
`typing.NoReturn`

Never와 NoReturn은 바닥 타입을 나타내며, 이는 멤버가 없는 타입입니다.

이들은 sys.exit()와 같이 함수가 절대 반환하지 않음을 나타내는 데 사용될 수 있습니다:

```python
from typing import Never  # or NoReturn

def stop() -> Never:
    raise RuntimeError('no way')
```

또는 assert_never()와 같이 유효한 인수가 없어 절대 호출되어서는 안 되는 함수를 정의하는 데 사용될 수 있습니다:

```python
from typing import Never  # or NoReturn

def never_call_me(arg: Never) -> None:
    pass

def int_or_str(arg: int | str) -> None:
    never_call_me(arg)  # type checker error
    match arg:
        case int():
            print("It's an int")
        case str():
            print("It's a str")
        case _:
            never_call_me(arg)  # OK, arg is of type Never (or NoReturn)
```

Never와 NoReturn은 타입 시스템에서 동일한 의미를 가지며 정적 타입 검사기는 둘을 동등하게 취급합니다.

버전 3.6.2에서 추가: NoReturn이 추가되었습니다.

버전 3.11에서 추가: Never가 추가되었습니다.

`typing.Self`

현재 포함된 클래스를 나타내는 특수 타입입니다.

예를 들면:

```python
from typing import Self, reveal_type

class Foo:
    def return_self(self) -> Self:
        …
        return self

class SubclassOfFoo(Foo): pass

reveal_type(Foo().return_self())  # Revealed type is "Foo"
reveal_type(SubclassOfFoo().return_self())  # Revealed type is "SubclassOfFoo"
```

이 주석은 의미적으로 다음과 동등하지만, 더 간결한 방식입니다:

```python
from typing import TypeVar

Self = TypeVar("Self", bound="Foo")

class Foo:
    def return_self(self: Self) -> Self:
        …
        return self
```

일반적으로 위의 예시처럼 무언가가 `self`를 반환하면 반환 어노테이션으로 `Self`를 사용해야 합니다. `Foo.return_self`가 `"Foo"`를 반환하는 것으로 어노테이션되었다면, 타입 검사기는 `SubclassOfFoo.return_self`에서 반환된 객체를 `SubclassOfFoo`가 아닌 `Foo` 타입으로 추론할 것입니다.

다른 일반적인 사용 사례는 다음과 같습니다:

- `cls` 매개변수의 인스턴스를 반환하는 대체 생성자로 사용되는 `classmethod`들.

- 자기 자신을 반환하는 `__enter__()` 메서드에 어노테이션을 다는 경우.

클래스가 서브클래스화될 때 메서드가 서브클래스의 인스턴스를 반환한다고 보장할 수 없는 경우에는 `Self`를 반환 어노테이션으로 사용해서는 안 됩니다:

```python
class Eggs:
    # 여기서 Self는 잘못된 반환 어노테이션입니다,
    # 서브클래스에서도 항상 Eggs의 인스턴스를 반환하기 때문입니다
    def returns_eggs(self) -> "Eggs":
        return Eggs()
```

자세한 내용은 PEP 673을 참조하세요.

버전 3.11에서 추가되었습니다.

`typing.TypeAlias`

타입 별칭을 명시적으로 선언하기 위한 특별한 어노테이션입니다.

예를 들면:

```python
from typing import TypeAlias

Factors: TypeAlias = list[int]
```

`TypeAlias`는 특히 오래된 Python 버전에서 순방향 참조를 사용하는 별칭에 어노테이션을 달 때 유용합니다. 타입 검사기가 이를 일반 변수 할당과 구분하기 어려울 수 있기 때문입니다:

```python
from typing import Generic, TypeAlias, TypeVar

T = TypeVar("T")

# "Box"는 아직 존재하지 않으므로,
# Python 3.12 미만에서는 순방향 참조를 위해 따옴표를 사용해야 합니다.
# ``TypeAlias``를 사용하면 타입 검사기에게 이것이 문자열에 대한 변수 할당이 아닌
# 타입 별칭 선언임을 알려줍니다.
BoxOfStrings: TypeAlias = "Box[str]"

class Box(Generic[T]):
    @classmethod
    def make_box_of_strings(cls) -> BoxOfStrings: …
```

자세한 내용은 PEP 613을 참조하세요.

> 버전 3.10에서 추가되었습니다.
> 버전 3.12부터 폐지됨: TypeAlias는 순방향 참조를 기본적으로 지원하며 TypeAliasType의 인스턴스를 생성하는 type 문을 위해 폐지되었습니다. TypeAlias와 TypeAliasType이 비슷한 목적을 가지고 비슷한 이름을 가지고 있지만, 둘은 서로 다르며 후자가 전자의 타입이 아님에 주의하세요. TypeAlias의 제거는 현재 계획되어 있지 않지만, 사용자들은 type 문으로의 마이그레이션을 권장합니다.

#### 특수 형태 (Special forms)

이들은 어노테이션에서 타입으로 사용될 수 있습니다. 모두 `[]`를 사용한 서브스크립션을 지원하지만, 각각 고유한 구문을 가지고 있습니다.

`typing.Union`

유니온 타입; `Union[X, Y]`는 `X | Y`와 동등하며 X 또는 Y를 의미합니다.

유니온을 정의하려면 예를 들어 `Union[int, str]` 또는 단축형 `int | str`을 사용합니다. 단축형을 사용하는 것이 권장됩니다. 세부 사항:

- 인자는 타입이어야 하며 적어도 하나 있어야 합니다.

- 유니온의 유니온은 평탄화됩니다, 예를 들어:

  Union[Union[int, str], float] == Union[int, str, float]

- 단일 인자의 유니온은 사라집니다. 예를 들어:

  Union[int] == int  # 생성자는 실제로 int를 반환합니다

- 중복 인자는 건너뜁니다. 예를 들어:

  Union[int, str, int] == Union[int, str] == int | str

- 유니온을 비교할 때, 인자 순서는 무시됩니다, 예를 들어:

  Union[int, str] == Union[str, int]

- 유니온을 서브클래스화하거나 인스턴스화할 수 없습니다.

- `Union[X][Y]`라고 쓸 수 없습니다.

버전 3.7에서 변경: 런타임에 유니온의 명시적 서브클래스를 제거하지 않습니다.

버전 3.10에서 변경: 유니온은 이제 `X | Y`로 작성할 수 있습니다. 유니온 타입 표현식을 참조하세요.

`typing.Optional`

`Optional[X]`는 `X | None` (또는 `Union[X, None]`)과 동등합니다.

이는 기본값을 갖는 선택적 인자와 같은 개념이 아님에 유의하십시오. 단지 선택적이기 때문에 기본값을 갖는 선택적 인자가 타입 어노테이션에 `Optional` 한정자가 필요하지는 않습니다. 예를 들면:

```python
def foo(arg: int = 0) -> None:
    …
```

한편, 명시적인 `None` 값이 허용되면, 인자가 선택적인지와 관계없이 `Optional`을 사용하는 것이 적합합니다. 예를 들면:

```python
def foo(arg: Optional[int] = None) -> None:
    …
```

버전 3.10에서 변경: Optional은 이제 `X | None`으로 작성할 수 있습니다. 유니온 타입 표현식을 참조하세요.

`typing.Concatenate`

고차 함수에 어노테이션을 달기 위한 특별한 형식입니다.

`Concatenate`는 Callable 및 ParamSpec과 함께 사용하여 다른 호출 가능한 객체의 매개변수를 추가, 제거 또는 변환하는 고차 호출 가능한 객체에 어노테이션을 달 수 있습니다. 사용법은 `Concatenate[Arg1Type, Arg2Type, …, ParamSpecVariable]` 형식입니다. `Concatenate`는 현재 Callable의 첫 번째 인자로 사용될 때만 유효합니다. `Concatenate`의 마지막 매개변수는 ParamSpec 또는 줄임표(`…`)여야 합니다.

예를 들어, 데코레이트된 함수에 threading.Lock을 제공하는 데코레이터 `with_lock`에 어노테이션을 달 때, `Concatenate`를 사용하여 `with_lock`이 첫 번째 인자로 `Lock`을 받는 호출 가능한 객체를 예상하고 다른 타입 서명을 가진 호출 가능한 객체를 반환한다는 것을 나타낼 수 있습니다. 이 경우, ParamSpec은 반환된 호출 가능한 객체의 매개변수 타입이 전달된 호출 가능한 객체의 매개변수 타입에 의존한다는 것을 나타냅니다:

```python
from collections.abc import Callable
from threading import Lock
from typing import Concatenate

# 한 번에 하나의 스레드만 함수를 실행하도록 보장하기 위해 이 잠금을 사용합니다.
my_lock = Lock()

def with_lock[**P, R](f: Callable[Concatenate[Lock, P], R]) -> Callable[P, R]:
    '''잠금을 제공하는 타입 안전 데코레이터입니다.'''
    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        # 잠금을 첫 번째 인자로 제공합니다.
        return f(my_lock, *args, **kwargs)
    return inner

@with_lock
def sum_threadsafe(lock: Lock, numbers: list[float]) -> float:
    '''스레드 안전한 방식으로 숫자 리스트를 더합니다.'''
    with lock:
        return sum(numbers)

# 데코레이터 덕분에 잠금을 직접 전달할 필요가 없습니다.
sum_threadsafe([1.1, 2.2, 3.3])
```

버전 3.10에서 추가되었습니다.

참조:

- PEP 612 – 매개변수 명세 변수 (ParamSpec과 Concatenate를 도입한 PEP)
- ParamSpec
- 호출 가능한 객체에 어노테이션 달기

`typing.Literal`

"리터럴 타입"을 정의하기 위한 특별한 타이핑 형식입니다.

`Literal`은 타입 검사기에게 어노테이션이 달린 객체가 제공된 리터럴 중 하나와 동등한 값을 가짐을 나타내는 데 사용할 수 있습니다.

예를 들면:

```python
def validate_simple(data: Any) -> Literal[True]:  # 항상 True를 반환
    …

type Mode = Literal['r', 'rb', 'w', 'wb']
def open_helper(file: str, mode: Mode) -> str:
    …

open_helper('/some/path', 'r')      # 타입 검사 통과
open_helper('/other/path', 'typo')  # 타입 검사기에서 오류
```

Literal[…]은 서브 클래싱 될 수 없습니다. 실행 시간에는, 임의의 값이 Literal[…]에 대한 형 인자로 허용되지만, 형 검사기는 제한을 부과할 수 있습니다. 리터럴 형에 대한 자세한 내용은 PEP 586을 참조하십시오.

> 버전 3.8에 추가.
> 버전 3.9.1에서 변경: Literal은 이제 매개변수를 중복 제거합니다. Literal 객체의 동등성 비교는 더 이상 순서에 의존하지 않습니다. Literal 객체는 이제 매개변수 중 하나가 해시 가능하지 않은 경우 동등성 비교 중에 TypeError 예외를 발생시킵니다.

`typing.ClassVar`

클래스 변수를 표시하기 위한 특수 형 구조물.

PEP 526에서 소개된 것처럼, ClassVar로 감싼 변수 어노테이션은 주어진 어트리뷰트가 클래스 변수로 사용되도록 의도되었으며 해당 클래스의 인스턴스에 설정되어서는 안 됨을 나타냅니다. 용법:

```python
class Starship:
    stats: ClassVar[dict[str, int]] = {} # 클래스 변수
    damage: int = 10                     # 인스턴스 변수
```

ClassVar는 형만 받아들이며 더는 서브 스크립트 할 수 없습니다.

ClassVar는 클래스 자체가 아니므로, isinstance()나 issubclass()와 함께 사용하면 안 됩니다. ClassVar는 파이썬 실행 시간 동작을 변경하지 않지만, 제삼자 형 검사기에서 사용할 수 있습니다. 예를 들어, 형 검사기는 다음 코드를 에러로 표시 할 수 있습니다:

```python
enterprise_d = Starship(3000)
enterprise_d.stats = {} # 오류, 인스턴스에 클래스 변수 설정
Starship.stats = {}     # 이는 괜찮음
```

버전 3.5.3에 추가.

`typing.Final`

형 검사기에 최종 이름을 나타내기 위한 특수 형 구조물.

최종 이름은 어떤 범위에서도 재할당될 수 없습니다. 클래스 범위에서 선언된 최종 이름은 하위 클래스에서 재정의될 수 없습니다.

예를 들면:

```python
MAX_SIZE: Final = 9000
MAX_SIZE += 1  # 형 검사기에 의해 오류 보고됨

class Connection:
    TIMEOUT: Final[int] = 10

class FastConnector(Connection):
    TIMEOUT = 1  # 형 검사기에 의해 오류 보고됨
```

이러한 속성에 대한 실행 시간 검사는 없습니다. 자세한 내용은 PEP 591을 참조하십시오.

버전 3.8에 추가.

`typing.Required`

TypedDict 키를 필수로 표시하기 위한 특수 형 구조물.

이는 주로 total=False TypedDicts에 유용합니다. 자세한 내용은 TypedDict와 PEP 655를 참조하십시오.

버전 3.11에 추가.

 `typing.NotRequired`

TypedDict 키를 잠재적으로 누락될 수 있는 것으로 표시하기 위한 특수 형 구조물.

자세한 내용은 TypedDict와 PEP 655를 참조하십시오.

버전 3.11에 추가.

`typing.Annotated`

어노테이션에 컨텍스트별 메타데이터를 추가하기 위한 특수 형 형태.

주어진 형 T에 메타데이터 x를 추가하려면 어노테이션 Annotated[T, x]를 사용하십시오. Annotated를 사용하여 추가된 메타데이터는 정적 분석 도구나 런타임에서 사용될 수 있습니다. 런타임에서 메타데이터는 __metadata__ 속성에 저장됩니다.

라이브러리나 도구가 Annotated[T, x] 어노테이션을 만났을 때 메타데이터에 대한 특별한 로직이 없다면, 메타데이터를 무시하고 단순히 어노테이션을 T로 취급해야 합니다. 따라서 Annotated는 Python의 정적 타이핑 시스템 외의 목적으로 어노테이션을 사용하고자 하는 코드에 유용할 수 있습니다.

Annotated[T, x]를 어노테이션으로 사용하면 여전히 T의 정적 타입 검사가 가능합니다. 타입 검사기는 단순히 메타데이터 x를 무시할 것이기 때문입니다. 이런 면에서 Annotated는 타이핑 시스템의 범위를 벗어난 어노테이션을 추가하는 데 사용할 수 있지만 함수나 클래스에 대한 타입 검사를 완전히 비활성화하는 @no_type_check 데코레이터와는 다릅니다.

메타데이터를 어떻게 해석할지에 대한 책임은 Annotated 어노테이션을 만나는 도구나 라이브러리에 있습니다. Annotated 타입을 만나는 도구나 라이브러리는 메타데이터 요소들을 스캔하여 관심 있는 것인지 결정할 수 있습니다(예: isinstance()를 사용하여).

`Annotated[<type>, <metadata>]`

다음은 범위 분석을 수행할 때 Annotated를 사용하여 타입 어노테이션에 메타데이터를 추가하는 방법의 예시입니다:

```python
@dataclass
class ValueRange:
    lo: int
    hi: int

T1 = Annotated[int, ValueRange(-10, 5)]
T2 = Annotated[T1, ValueRange(-20, 3)]
```

구문의 세부사항:

- Annotated의 첫 번째 인자는 유효한 형이어야 합니다

- 여러 메타데이터 요소를 제공할 수 있습니다(Annotated는 가변 인자를 지원합니다):

```python
@dataclass
class ctype:
    kind: str

Annotated[int, ValueRange(3, 10), ctype("char")]
```

어노테이션을 소비하는 도구가 클라이언트가 하나의 어노테이션에 여러 메타데이터 요소를 추가할 수 있는지와 이러한 어노테이션을 어떻게 병합할지 결정합니다.

- Annotated는 최소 두 개의 인자로 구독되어야 합니다(Annotated[int]는 유효하지 않습니다)

- 메타데이터 요소의 순서는 보존되며 동등성 검사에 중요합니다:

```python
assert Annotated[int, ValueRange(3, 10), ctype("char")] != Annotated[
    int, ctype("char"), ValueRange(3, 10)
]
```

- 중첩된 Annotated 타입은 평탄화됩니다. 메타데이터 요소의 순서는 가장 안쪽 어노테이션부터 시작합니다:

```python
assert Annotated[Annotated[int, ValueRange(3, 10)], ctype("char")] == Annotated[
    int, ValueRange(3, 10), ctype("char")
]
```

- 중복된 메타데이터 요소는 제거되지 않습니다:

```python
assert Annotated[int, ValueRange(3, 10)] != Annotated[
    int, ValueRange(3, 10), ValueRange(3, 10)
]
```

- Annotated는 중첩 및 일반 별칭과 함께 사용할 수 있습니다:

```python
@dataclass
class MaxLen:
    value: int

type Vec[T] = Annotated[list[tuple[T, T]], MaxLen(10)]

# 타입 어노테이션에서 사용될 때, 타입 검사기는 "V"를
# Annotated[list[tuple[int, int]], MaxLen(10)]과 동일하게 취급합니다:
type V = Vec[int]
```

- Annotated는 언패킹된 TypeVarTuple과 함께 사용할 수 없습니다:

```python
type Variadic[*Ts] = Annotated[*Ts, Ann1]  # 유효하지 않음
```

이는 다음과 동등할 것입니다:

```python
Annotated[T1, T2, T3, …, Ann1]
```

여기서 T1, T2 등은 TypeVars입니다. 이는 유효하지 않습니다: Annotated에는 하나의 타입만 전달되어야 합니다.

- 기본적으로 get_type_hints()는 어노테이션에서 메타데이터를 제거합니다. 메타데이터를 보존하려면 include_extras=True를 전달하십시오:

```python
>>> from typing import Annotated, get_type_hints
>>> def func(x: Annotated[int, "metadata"]) -> None: pass
…
>>> get_type_hints(func)
{'x': <class 'int'>, 'return': <class 'NoneType'>}
>>> get_type_hints(func, include_extras=True)
{'x': typing.Annotated[int, 'metadata'], 'return': <class 'NoneType'>}
```

- 런타임에 Annotated 타입과 관련된 메타데이터는 __metadata__ 속성을 통해 검색할 수 있습니다:

```python
>>> from typing import Annotated
>>> X = Annotated[int, "very", "important", "metadata"]
>>> X
typing.Annotated[int, 'very', 'important', 'metadata']
>>> X.__metadata__
('very', 'important', 'metadata')
```

- 런타임에 Annotated로 감싸진 원래 타입을 검색하려면 __origin__ 속성을 사용하십시오:

```python
>>> from typing import Annotated, get_origin
>>> Password = Annotated[str, "secret"]
>>> Password.__origin__
<class 'str'>
```

- get_origin()을 사용하면 Annotated 자체를 반환한다는 점에 유의하십시오:

```python
>>> get_origin(Password)
<class 'typing.Annotated'>
```

> [!seealso]
> 
> **PEP 593** - 유연한 함수 및 변수 주석
> 표준 라이브러리에 `Annotated`를 도입한 PEP입니다.

> 버전 3.9에 추가되었습니다.

`typing.TypeGuard`

사용자 정의 타입 가드 함수를 표시하기 위한 특수 타이핑 구조입니다.

`TypeGuard`는 사용자 정의 타입 가드 함수의 반환 타입을 주석 처리하는 데 사용될 수 있습니다. `TypeGuard`는 단일 타입 인자만 받습니다. 런타임에 이렇게 표시된 함수는 불리언을 반환해야 합니다.

`TypeGuard`는 타입 좁히기의 이점을 목표로 합니다 - 정적 타입 검사기가 프로그램의 코드 흐름 내에서 표현식의 더 정확한 타입을 결정하는 데 사용하는 기술입니다. 일반적으로 타입 좁히기는 조건부 코드 흐름을 분석하고 좁히기를 코드 블록에 적용하여 수행됩니다. 여기서 조건식은 때때로 "타입 가드"라고 불립니다:

```python
def is_str(val: str | float):
    # "isinstance" 타입 가드
    if isinstance(val, str):
        # ``val``의 타입이 ``str``로 좁혀집니다
        …
    else:
        # 그렇지 않으면 ``val``의 타입이 ``float``로 좁혀집니다.
        …
```

때때로 사용자 정의 불리언 함수를 타입 가드로 사용하는 것이 편리할 수 있습니다. 이러한 함수는 정적 타입 검사기에 이 의도를 알리기 위해 `TypeGuard[…]`를 반환 타입으로 사용해야 합니다.

`-> TypeGuard`를 사용하면 정적 타입 검사기에게 주어진 함수에 대해 다음을 알립니다:

1. 반환값은 불리언입니다.
2. 반환값이 `True`이면 인수의 타입은 `TypeGuard` 내부의 타입입니다.

예를 들면:

```python
def is_str_list(val: list[object]) -> TypeGuard[list[str]]:
    '''리스트의 모든 객체가 문자열인지 확인합니다'''
    return all(isinstance(x, str) for x in val)

def func1(val: list[object]):
    if is_str_list(val):
        # ``val``의 타입이 ``list[str]``로 좁혀집니다.
        print(" ".join(val))
    else:
        # ``val``의 타입은 ``list[object]``로 유지됩니다.
        print("문자열 리스트가 아닙니다!")
```

`is_str_list`가 클래스 또는 인스턴스 메서드인 경우, `TypeGuard`의 타입은 두 번째 매개변수(`cls` 또는 `self` 다음)의 타입에 매핑됩니다.

간단히 말해서, `def foo(arg: TypeA) -> TypeGuard[TypeB]: …` 형태는 `foo(arg)`가 `True`를 반환하면 `arg`가 `TypeA`에서 `TypeB`로 좁혀짐을 의미합니다.

> [!NOTE]
> `TypeB`가 `TypeA`의 더 좁은 형태일 필요는 없습니다 - 심지어 더 넓은 형태일 수도 있습니다. 주요 이유는 `list`가 불변이기 때문에 후자가 전자의 하위 타입이 아님에도 불구하고 `list[object]`를 `list[str]`로 좁히는 것과 같은 작업을 허용하기 위해서입니다. 타입 안전한 타입 가드를 작성하는 책임은 사용자에게 있습니다.

`TypeGuard`는 타입 변수와도 작동합니다. 자세한 내용은 **PEP 647**을 참조하세요.

> 버전 3.10에 추가되었습니다.

`typing.Unpack`

개념적으로 객체가 언팩되었음을 표시하는 타이핑 연산자입니다.

예를 들어, 타입 변수 튜플에 언팩 연산자 `*`를 사용하는 것은 `Unpack`을 사용하여 타입 변수 튜플이 언팩되었음을 표시하는 것과 동일합니다:

```python
Ts = TypeVarTuple('Ts')
tup: tuple[*Ts]
# 실제로 다음과 같습니다:
tup: tuple[Unpack[Ts]]
```

실제로 `Unpack`은 [`typing.TypeVarTuple`](https://docs.python.org/ko/3.12/library/typing.html#typing.TypeVarTuple "typing.TypeVarTuple")과 [`builtins.tuple`](https://docs.python.org/ko/3.12/library/stdtypes.html#tuple "tuple") 타입의 맥락에서 `*`와 상호 교환적으로 사용될 수 있습니다. 이전 버전의 Python에서는 특정 위치에서 `*`를 사용할 수 없었기 때문에 `Unpack`이 명시적으로 사용되는 것을 볼 수 있습니다:

```python
# 이전 버전의 Python에서는 TypeVarTuple과 Unpack이
# `typing_extensions` 백포트 패키지에 위치합니다.
from typing_extensions import TypeVarTuple, Unpack

Ts = TypeVarTuple('Ts')
tup: tuple[*Ts]         # Python <= 3.10에서는 구문 오류!
tup: tuple[Unpack[Ts]]  # 의미적으로 동일하며 하위 호환성 있음
```

`Unpack`은 또한 [`typing.TypedDict`](https://docs.python.org/ko/3.12/library/typing.html#typing.TypedDict "typing.TypedDict")와 함께 함수 시그니처에서 `**kwargs`를 타이핑하는 데 사용될 수 있습니다:

```python
from typing import TypedDict, Unpack

class Movie(TypedDict):
    name: str
    year: int

# 이 함수는 두 개의 키워드 인수를 기대합니다 - `str` 타입의 `name`과
# `int` 타입의 `year`.
def foo(**kwargs: Unpack[Movie]): …
```

`**kwargs` 타이핑에 `Unpack`을 사용하는 방법에 대한 자세한 내용은 **PEP 692**를 참조하세요.

버전 3.11에 추가되었습니다.

#### 제네릭 타입 및 타입 별칭 구축 (Building generic types and type aliases)

다음 클래스들은 주석으로 직접 사용되어서는 안 됩니다. 이들의 의도된 목적은 제네릭 타입과 타입 별칭을 생성하기 위한 빌딩 블록이 되는 것입니다.

이러한 객체들은 특별한 구문(타입 매개변수 리스트와 `type` 문)을 통해 생성될 수 있습니다. Python 3.11 이전 버전과의 호환성을 위해, 아래에 문서화된 대로 전용 구문 없이도 생성될 수 있습니다.

`_class_ typing.Generic`

제네릭 타입을 위한 추상 기본 클래스입니다.

제네릭 타입은 일반적으로 클래스 이름 뒤에 타입 매개변수 목록을 추가하여 선언됩니다:

```python
class Mapping[KT, VT]:
    def __getitem__(self, key: KT) -> VT:
        …
        # 기타 등등.
```

이러한 클래스는 암시적으로 `Generic`을 상속합니다. 이 구문의 런타임 의미는 언어 참조에서 논의됩니다.

이 클래스는 다음과 같이 사용할 수 있습니다:

```python
def lookup_name[X, Y](mapping: Mapping[X, Y], key: X, default: Y) -> Y:
    try:
        return mapping[key]
    except KeyError:
        return default
```

여기서 함수 이름 뒤의 대괄호는 제네릭 함수를 나타냅니다.

하위 호환성을 위해 제네릭 클래스는 `Generic`을 명시적으로 상속하여 선언할 수도 있습니다. 이 경우 타입 매개변수는 별도로 선언되어야 합니다:

```python
KT = TypeVar('KT')
VT = TypeVar('VT')

class Mapping(Generic[KT, VT]):
    def __getitem__(self, key: KT) -> VT:
        …
        # 기타 등등.
```

`_class_ typing.TypeVar(_name_, _*constraints_, _bound=None_, _covariant=False_, _contravariant=False_, _infer_variance=False_)`

타입 변수입니다.

타입 변수를 구성하는 선호되는 방법은 제네릭 함수, 제네릭 클래스, 제네릭 타입 별칭을 위한 전용 구문을 통해서입니다:

```python
class Sequence[T]:  # T는 TypeVar입니다
    …
```

이 구문은 바운드 및 제약 타입 변수를 생성하는 데에도 사용할 수 있습니다:

```python
class StrSequence[S: str]:  # S는 str에 바운드된 TypeVar입니다
    …

class StrOrBytesSequence[A: (str, bytes)]:  # A는 str 또는 bytes로 제약된 TypeVar입니다
    …
```

그러나 원한다면 재사용 가능한 타입 변수를 수동으로 구성할 수도 있습니다:

```python
T = TypeVar('T')  # 어떤 것이든 될 수 있습니다
S = TypeVar('S', bound=str)  # str의 모든 하위 타입이 될 수 있습니다
A = TypeVar('A', str, bytes)  # 정확히 str 또는 bytes여야 합니다
```

타입 변수는 주로 정적 타입 검사기의 이점을 위해 존재합니다. 이들은 제네릭 타입의 매개변수뿐만 아니라 제네릭 함수 및 타입 별칭 정의를 위한 매개변수 역할을 합니다. 제네릭 타입에 대한 자세한 정보는 [`Generic`](https://docs.python.org/ko/3.12/library/typing.html#typing.Generic "typing.Generic")을 참조하세요. 제네릭 함수는 다음과 같이 작동합니다:

```python
def repeat[T](x: T, n: int) -> Sequence[T]:
    """x에 대한 n개의 참조를 포함하는 리스트를 반환합니다."""
    return [x]*n

def print_capitalized[S: str](x: S) -> S:
    """x를 대문자로 출력하고 x를 반환합니다."""
    print(x.capitalize())
    return x

def concatenate[A: (str, bytes)](x: A, y: A) -> A:
    """두 개의 문자열 또는 바이트 객체를 더합니다."""
    return x + y
```

타입 변수는 바운드되거나 제약될 수 있지만, 두 가지 모두일 수는 없습니다.

타입 변수의 가변성은 타입 파라미터 구문을 통해 생성되거나 `infer_variance=True`가 전달될 때 타입 체커에 의해 추론됩니다. 수동으로 생성된 타입 변수는 `covariant=True` 또는 `contravariant=True`를 전달하여 명시적으로 공변 또는 반공변으로 표시될 수 있습니다. 기본적으로 수동으로 생성된 타입 변수는 불변입니다. 자세한 내용은 PEP 484와 PEP 695를 참조하세요.

바운드된 타입 변수와 제약된 타입 변수는 여러 중요한 면에서 다른 의미를 가집니다. 바운드된 타입 변수를 사용한다는 것은 `TypeVar`가 가능한 가장 구체적인 타입을 사용하여 해결된다는 것을 의미합니다:

```python
x = print_capitalized('a string')
reveal_type(x)  # 드러난 타입은 str입니다

class StringSubclass(str):
    pass

y = print_capitalized(StringSubclass('another string'))
reveal_type(y)  # 드러난 타입은 StringSubclass입니다

z = print_capitalized(45)  # 오류: int는 str의 하위 타입이 아닙니다
```

타입 변수는 구체적인 타입, 추상 타입(ABC 또는 프로토콜), 심지어 타입의 유니온에도 바운드될 수 있습니다:

```python
# abs 메서드가 있는 모든 것이 가능합니다
def print_abs[T: SupportsAbs](arg: T) -> None:
    print("Absolute value:", abs(arg))

U = TypeVar('U', bound=str|bytes)  # str|bytes 유니온의 모든 하위 타입이 가능합니다
V = TypeVar('V', bound=SupportsAbs)  # abs 메서드가 있는 모든 것이 가능합니다
```

그러나 제약된 타입 변수를 사용한다는 것은 `TypeVar`가 주어진 제약 조건 중 정확히 하나로만 해결될 수 있다는 것을 의미합니다:

```python
a = concatenate('one', 'two')
reveal_type(a)  # 드러난 타입은 str입니다

b = concatenate(StringSubclass('one'), StringSubclass('two'))
reveal_type(b)  # StringSubclass가 전달되었음에도 불구하고 드러난 타입은 str입니다

c = concatenate('one', b'two')  # 오류: 타입 변수 'A'는 함수 호출에서 str 또는 bytes 중 하나일 수 있지만 둘 다일 수는 없습니다
```

런타임에 `isinstance(x, T)`는 TypeError를 발생시킵니다.

`__name__`

타입 변수의 이름입니다.

`__covariant__`

타입 변수가 명시적으로 공변으로 표시되었는지 여부입니다.

`__contravariant__`

타입 변수가 명시적으로 반공변으로 표시되었는지 여부입니다.

`__infer_variance__`

타입 변수의 가변성을 타입 체커가 추론해야 하는지 여부입니다.

버전 3.12에서 추가되었습니다.

`__bound__`

타입 변수의 바운드(있는 경우)입니다.

> 버전 3.12에서 변경: 타입 파라미터 구문을 통해 생성된 타입 변수의 경우, 바운드는 타입 변수가 생성될 때가 아니라 속성에 접근할 때만 평가됩니다(지연 평가 참조).

`__constraints__`

타입 변수의 제약 조건(있는 경우)을 포함하는 튜플입니다.

> 버전 3.12에서 변경: 타입 파라미터 구문을 통해 생성된 타입 변수의 경우, 제약 조건은 타입 변수가 생성될 때가 아니라 속성에 접근할 때만 평가됩니다(지연 평가 참조).

> 버전 3.12에서 변경: 이제 타입 변수는 PEP 695에서 도입된 타입 파라미터 구문을 사용하여 선언할 수 있습니다. `infer_variance` 매개변수가 추가되었습니다.

`_class_ typing.TypeVarTuple(_name_)`

타입 변수 튜플. 가변 제네릭을 가능하게 하는 특수한 형태의 타입 변수입니다.

타입 변수 튜플은 타입 파라미터 리스트에서 이름 앞에 단일 별표(`*`)를 사용하여 선언할 수 있습니다:

```python
def move_first_element_to_last[T, *Ts](tup: tuple[T, *Ts]) -> tuple[*Ts, T]:
    return (*tup[1:], tup[0])
```

또는 `TypeVarTuple` 생성자를 명시적으로 호출하여 선언할 수 있습니다:

```python
T = TypeVar("T")
Ts = TypeVarTuple("Ts")

def move_first_element_to_last(tup: tuple[T, *Ts]) -> tuple[*Ts, T]:
    return (*tup[1:], tup[0])
```

일반 타입 변수는 단일 타입으로 매개변수화를 가능하게 합니다. 반면에 타입 변수 튜플은 튜플로 감싼 임의의 수의 타입 변수처럼 작동하여 임의의 수의 타입으로 매개변수화를 허용합니다. 예를 들어:

```python
# T는 int에 바운드되고, Ts는 ()에 바운드됩니다
# 반환 값은 (1,)이며, 타입은 tuple[int]입니다
move_first_element_to_last(tup=(1,))

# T는 int에 바운드되고, Ts는 (str,)에 바운드됩니다
# 반환 값은 ('spam', 1)이며, 타입은 tuple[str, int]입니다
move_first_element_to_last(tup=(1, 'spam'))

# T는 int에 바운드되고, Ts는 (str, float)에 바운드됩니다
# 반환 값은 ('spam', 3.0, 1)이며, 타입은 tuple[str, float, int]입니다
move_first_element_to_last(tup=(1, 'spam', 3.0))

# 이는 타입 체크에 실패합니다(그리고 런타임에 실패합니다)
# tuple[()]이 tuple[T, *Ts]와 호환되지 않기 때문입니다
# (최소한 하나의 요소가 필요합니다)
move_first_element_to_last(tup=())
```

`tuple[T, *Ts]`에서 언패킹 연산자 `*`의 사용에 주목하세요. 개념적으로 `Ts`를 타입 변수의 튜플 `(T1, T2, …)`로 생각할 수 있습니다. 그러면 `tuple[T, *Ts]`는 `tuple[T, *(T1, T2, …)]`가 되어 `tuple[T, T1, T2, …]`와 동등합니다. (이전 버전의 Python에서는 이를 `Unpack` 대신 `Unpack[Ts]`로 작성할 수 있습니다.)

타입 변수 튜플은 항상 언패킹되어야 합니다. 이는 타입 변수 튜플을 일반 타입 변수와 구별하는 데 도움이 됩니다:

```python
x: Ts          # 유효하지 않음
x: tuple[Ts]   # 유효하지 않음
x: tuple[*Ts]  # 올바른 방법
```

타입 변수 튜플은 일반 타입 변수와 동일한 컨텍스트에서 사용할 수 있습니다. 예를 들어, 클래스 정의, 인수 및 반환 타입에서 사용할 수 있습니다:

```python
class Array[*Shape]:
    def __getitem__(self, key: tuple[*Shape]) -> float: …
    def __abs__(self) -> "Array[*Shape]": …
    def get_shape(self) -> tuple[*Shape]: …
```

타입 변수 튜플은 일반 타입 변수와 잘 결합될 수 있습니다:

```python
class Array[DType, *Shape]:  # 이는 괜찮습니다
    pass

class Array2[*Shape, DType]:  # 이것도 괜찮습니다
    pass

class Height: …
class Width: …

float_array_1d: Array[float, Height] = Array()     # 완전히 괜찮습니다
int_array_2d: Array[int, Height, Width] = Array()  # 네, 이것도 괜찮습니다
```

그러나 단일 타입 인수 또는 타입 파라미터 리스트에는 최대 하나의 타입 변수 튜플만 나타날 수 있습니다:

```python
x: tuple[*Ts, *Ts]            # 유효하지 않음
class Array[*Shape, *Shape]:  # 유효하지 않음
    pass
```

마지막으로, 언패킹된 타입 변수 튜플은 `*args`의 타입 주석으로 사용될 수 있습니다:

```python
def call_soon[*Ts](
    callback: Callable[[*Ts], None],
    *args: *Ts
) -> None:
    …
    callback(*args)
```

비 언패킹 주석 `*args: int`와 대조적으로 - 이는 모든 인자가 `int`임을 지정함 - `*args: *Ts`는 `*args`의 개별 인자 타입을 참조할 수 있게 합니다. 여기서 이를 통해 `call_soon`에 전달된 `*args`의 타입이 `callback`의 (위치) 인자 타입과 일치하는지 확인할 수 있습니다.

타입 변수 튜플에 대한 자세한 내용은 [PEP 646](https://peps.python.org/pep-0646/)을 참조하세요.

`__name__`
타입 변수 튜플의 이름입니다.

> 버전 3.11에서 추가되었습니다.
> 버전 3.12에서 변경: 이제 타입 변수 튜플은 [PEP 695](https://peps.python.org/pep-0695/)에서 도입한 [타입 매개변수](https://docs.python.org/ko/3.12/reference/compound_stmts.html#type-params) 구문을 사용하여 선언할 수 있습니다.

`_class_ typing.ParamSpec(_name_, _*_, _bound=None_, _covariant=False_, _contravariant=False_)`

매개변수 명세 변수. [타입 변수](https://docs.python.org/ko/3.12/library/typing.html#typevar)의 특수화된 버전입니다.

[타입 매개변수 목록](https://docs.python.org/ko/3.12/reference/compound_stmts.html#type-params)에서 매개변수 명세는 두 개의 별표(`**`)로 선언할 수 있습니다:

```python
type IntFunc[**P] = Callable[P, int]
```

Python 3.11 이전 버전과의 호환성을 위해 `ParamSpec` 객체는 다음과 같이 생성할 수도 있습니다:

```python
P = ParamSpec('P')
```

매개변수 명세 변수는 주로 정적 타입 검사기의 이점을 위해 존재합니다. 이들은 한 호출 가능 객체의 매개변수 타입을 다른 호출 가능 객체로 전달하는 데 사용됩니다 - 이는 고차 함수와 데코레이터에서 흔히 볼 수 있는 패턴입니다. 이들은 `Concatenate`에서 사용되거나 `Callable`의 첫 번째 인자로 사용되거나 사용자 정의 제네릭의 매개변수로 사용될 때만 유효합니다. 제네릭 타입에 대한 자세한 내용은 `Generic`을 참조하세요.

예를 들어, 함수에 기본 로깅을 추가하기 위해 함수 호출을 로깅하는 `add_logging` 데코레이터를 만들 수 있습니다. 매개변수 명세 변수는 타입 검사기에게 데코레이터로 전달된 호출 가능 객체와 그것이 반환하는 새로운 호출 가능 객체가 상호 의존적인 타입 매개변수를 가지고 있음을 알려줍니다:

```python
from collections.abc import Callable
import logging

def add_logging[T, **P](f: Callable[P, T]) -> Callable[P, T]:
    '''함수에 로깅을 추가하는 타입 안전 데코레이터.'''
    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        logging.info(f'{f.__name__} was called')
        return f(*args, **kwargs)
    return inner

@add_logging
def add_two(x: float, y: float) -> float:
    '''두 숫자를 더합니다.'''
    return x + y
```

`ParamSpec` 없이는 이전에 이를 주석 처리하는 가장 간단한 방법은 `Callable[…, Any]`로 바운드된 `TypeVar`를 사용하는 것이었습니다. 그러나 이는 두 가지 문제를 야기합니다:

1. 타입 검사기가 `inner` 함수를 타입 검사할 수 없습니다. `*args`와 `**kwargs`가 `Any`로 타입 지정되어야 하기 때문입니다.
2. `add_logging` 데코레이터의 본문에서 `inner` 함수를 반환할 때 `cast()`가 필요하거나 정적 타입 검사기가 `return inner`를 무시하도록 지시해야 합니다.

`args`

`kwargs
`
`ParamSpec`는 위치 매개변수와 키워드 매개변수를 모두 캡처하므로, `P.args`와 `P.kwargs`를 사용하여 `ParamSpec`을 구성 요소로 분할할 수 있습니다. `P.args`는 주어진 호출에서 위치 매개변수의 튜플을 나타내며 `*args`의 주석에만 사용해야 합니다. `P.kwargs`는 주어진 호출에서 키워드 매개변수와 그 값의 매핑을 나타내며 `**kwargs`의 주석에만 사용해야 합니다. 두 속성 모두 주석이 달린 매개변수가 범위 내에 있어야 합니다. 런타임에 `P.args`와 `P.kwargs`는 각각 `ParamSpecArgs`와 `ParamSpecKwargs`의 인스턴스입니다.

`__name__`

매개변수 명세의 이름입니다.

`covariant=True` 또는 `contravariant=True`로 생성된 매개변수 명세 변수는 공변 또는 반변 제네릭 타입을 선언하는 데 사용할 수 있습니다. `bound` 인자도 `TypeVar`와 유사하게 받아들입니다. 그러나 이러한 키워드의 실제 의미는 아직 결정되지 않았습니다.

> 버전 3.10에서 추가되었습니다.

> 버전 3.12에서 변경: 이제 매개변수 명세는 [PEP 695](https://peps.python.org/pep-0695/)에서 도입한 [타입 매개변수](https://docs.python.org/ko/3.12/reference/compound_stmts.html#type-params) 구문을 사용하여 선언할 수 있습니다.

> [!NOTE]
> 전역 범위에서 정의된 매개변수 명세 변수만 피클링될 수 있습니다.

> [!seealso]
> - [PEP 612](https://peps.python.org/pep-0612/) – 매개변수 명세 변수 (`ParamSpec`와 `Concatenate`를 도입한 PEP)
> - `Concatenate`
> - [호출 가능 객체에 주석 달기](https://docs.python.org/ko/3.12/library/typing.html#annotating-callables)

`typing.ParamSpecArgs`
`typing.ParamSpecKwargs`

`ParamSpec`의 인자와 키워드 인자 속성입니다. `ParamSpec`의 `P.args` 속성은 `ParamSpecArgs`의 인스턴스이고, `P.kwargs`는 `ParamSpecKwargs`의 인스턴스입니다. 이들은 런타임 내부 검사를 위한 것이며 정적 타입 검사기에는 특별한 의미가 없습니다.

이러한 객체 중 하나에 대해 `get_origin()`을 호출하면 원래의 `ParamSpec`가 반환됩니다:

```python
>>> from typing import ParamSpec, get_origin
>>> P = ParamSpec("P")
>>> get_origin(P.args) is P
True
>>> get_origin(P.kwargs) is P
True
```

> 버전 3.10에서 추가되었습니다.

`class typing.TypeAliasType(_name_, _value_, _*_, _type_params=()_)`

`type` 문을 통해 생성된 타입 별칭의 타입입니다.

예시:

```python
>>> type Alias = int
>>> type(Alias)
<class 'typing.TypeAliasType'>
```

> 버전 3.12에서 추가되었습니다.

`__name__`

타입 별칭의 이름:

```python
>>> type Alias = int
>>> Alias.__name__
'Alias'
```

`__module__
`
타입 별칭이 정의된 모듈:

```python
>>> type Alias = int
>>> Alias.__module__
'__main__'
```

`__type_params__`

타입 별칭의 타입 매개변수, 또는 별칭이 제네릭이 아닌 경우 빈 튜플:

```python
>>> type ListOrSet[T] = list[T] | set[T]
>>> ListOrSet.__type_params__
(T,)
>>> type NotGeneric = int
>>> NotGeneric.__type_params__
()
```

`__value__`

타입 별칭의 값입니다. 이는 [지연 평가](https://docs.python.org/ko/3.12/reference/executionmodel.html#lazy-evaluation)되므로 별칭 정의에 사용된 이름은 `__value__` 속성에 접근할 때까지 해결되지 않습니다:

```python
>>> type Mutually = Recursive
>>> type Recursive = Mutually
>>> Mutually
Mutually
>>> Recursive
Recursive
>>> Mutually.__value__
Recursive
>>> Recursive.__value__
Mutually
```

#### 기타 특수 지시자

이 함수들과 클래스들은 직접 어노테이션으로 사용되어서는 안 됩니다. 이들의 의도된 목적은 타입을 생성하고 선언하기 위한 구성 요소가 되는 것입니다.

class typing.NamedTuple

형 지정된 collections.namedtuple() 버전.

용법:

```python
class Employee(NamedTuple):
    name: str
    id: int
```

이것은 다음과 동등합니다:

```python
Employee = collections.namedtuple('Employee', ['name', 'id'])
```

필드에 기본값을 부여하려면, 클래스 바디에서 그 값을 대입할 수 있습니다:

```python
class Employee(NamedTuple):
    name: str
    id: int = 3

employee = Employee('Guido')
assert employee.id == 3
```

기본값이 있는 필드는 기본값이 없는 모든 필드 뒤에 와야 합니다.

결과 클래스는 필드 이름을 필드 타입에 매핑하는 딕셔너리를 제공하는 __annotations__ 라는 추가 속성을 갖습니다. (필드 이름은 _fields 속성에 있고 기본값은 _field_defaults 속성에 있으며, 둘 다 namedtuple() API의 일부입니다.)

NamedTuple 서브 클래스는 독스트링과 메서드도 가질 수 있습니다:

```python
class Employee(NamedTuple):
    """Represents an employee."""
    name: str
    id: int = 3

    def __repr__(self) -> str:
        return f'<Employee {self.name}, id={self.id}>'
```

NamedTuple 서브클래스는 제네릭일 수 있습니다:

```python
class Group[T](NamedTuple):
    key: T
    group: list[T]
```

이전 버전과 호환되는 사용법:

```python
# For creating a generic NamedTuple on Python 3.11
T = TypeVar("T")

class Group(NamedTuple, Generic[T]):
    key: T
    group: list[T]

# A functional syntax is also supported
Employee = NamedTuple('Employee', [('name', str), ('id', int)])
```

버전 3.6에서 변경: PEP 526 변수 어노테이션 문법 지원을 추가했습니다.

버전 3.6.1에서 변경: 기본값, 메서드 및 독스트링에 대한 지원을 추가했습니다.

버전 3.8에서 변경: _field_types와 __annotations__ 어트리뷰트는 이제 OrderedDict 인스턴스가 아닌 일반 딕셔너리입니다.

버전 3.9에서 변경: _field_types 어트리뷰트를 제거하고, 같은 정보를 가지는 더 표준적인 __annotations__ 어트리뷰트로 대체했습니다.

버전 3.11에서 변경: 제네릭 namedtuples에 대한 지원을 추가했습니다.

class typing.NewType(name, tp)

저비용 distinct 타입을 생성하기 위한 헬퍼 클래스입니다.

NewType은 타입 체커에 의해 고유한 타입으로 간주됩니다. 그러나 런타임에는 NewType을 호출하면 인수가 변경되지 않고 반환됩니다.

용법:

```python
UserId = NewType('UserId', int)  # Declare the NewType "UserId"
first_user = UserId(1)  # "UserId" returns the argument unchanged at runtime
```

__module__

새 타입이 정의된 모듈입니다.

__name__

새 타입의 이름입니다.

__supertype__

새 타입이 기반으로 하는 타입입니다.

버전 3.5.2에 추가되었습니다.

버전 3.10에서 변경: NewType은 이제 함수가 아닌 클래스입니다.

class typing.Protocol(Generic)

프로토콜 클래스의 기본 클래스입니다.

프로토콜 클래스는 다음과 같이 정의됩니다:

```python
class Proto(Protocol):
    def meth(self) -> int:
        …
```

이러한 클래스는 주로 구조적 서브 타이핑(정적 덕 타이핑)을 인식하는 정적 형 검사기와 함께 사용됩니다, 예를 들어:

```python
class C:
    def meth(self) -> int:
        return 0

def func(x: Proto) -> int:
    return x.meth()

func(C())  # Passes static type check
```

자세한 내용은 PEP 544를 참조하세요. runtime_checkable()로 장식된 프로토콜 클래스(나중에 설명됨)는 주어진 속성의 존재만을 확인하고 그들의 타입 서명을 무시하는 단순한 런타임 프로토콜로 작동합니다.

프로토콜 클래스는 제네릭일 수 있습니다, 예를 들어:

```python
class GenProto[T](Protocol):
    def meth(self) -> T:
        …
```

Python 3.11 이하 버전과 호환되어야 하는 코드에서는 제네릭 프로토콜을 다음과 같이 작성할 수 있습니다:

```python
T = TypeVar("T")

class GenProto(Protocol[T]):
    def meth(self) -> T:
        …
```

버전 3.8에 추가되었습니다.

@typing.runtime_checkable

프로토콜 클래스를 런타임 프로토콜로 표시합니다.

이러한 프로토콜은 isinstance()와 issubclass()와 함께 사용할 수 있습니다. 이것은 비 프로토콜 클래스에 적용될 때 TypeError를 발생시킵니다. 이것은 collections.abc에 있는 Iterable처럼 "한 가지만 잘하는" 것과 매우 유사한 단순한 구조적 검사를 허용합니다. 예를 들면:

```python
@runtime_checkable
class Closable(Protocol):
    def close(self): …

assert isinstance(open('/some/file'), Closable)

@runtime_checkable
class Named(Protocol):
    name: str

import threading
assert isinstance(threading.Thread(name='Bob'), Named)
```

참고

runtime_checkable()은 필요한 메서드나 속성의 존재만을 확인하며, 그들의 타입 서명이나 타입은 확인하지 않습니다. 예를 들어, ssl.SSLObject는 클래스이므로 Callable에 대한 issubclass() 검사를 통과합니다. 그러나 ssl.SSLObject.__init__ 메서드는 더 정보가 풍부한 메시지와 함께 TypeError를 발생시키기 위해서만 존재하므로, ssl.SSLObject를 호출(인스턴스화)하는 것은 불가능합니다.

참고

런타임 체크 가능한 프로토콜에 대한 isinstance() 검사는 비 프로토콜 클래스에 대한 isinstance() 검사에 비해 놀라울 정도로 느릴 수 있습니다. 성능에 민감한 코드에서는 구조적 검사를 위해 hasattr() 호출과 같은 대안적인 관용구를 사용하는 것을 고려하세요.

버전 3.8에 추가되었습니다.

버전 3.12에서 변경: 런타임 체크 가능한 프로토콜에 대한 isinstance() 검사의 내부 구현은 이제 속성을 찾기 위해 inspect.getattr_static()을 사용합니다(이전에는 hasattr()가 사용되었습니다). 결과적으로, 런타임 체크 가능한 프로토콜의 인스턴스로 간주되던 일부 객체들이 Python 3.12+에서는 더 이상 해당 프로토콜의 인스턴스로 간주되지 않을 수 있으며, 그 반대의 경우도 마찬가지입니다. 대부분의 사용자는 이 변경의 영향을 받지 않을 것입니다.

버전 3.12에서 변경: 런타임 체크 가능한 프로토콜의 멤버는 이제 클래스가 생성되자마자 런타임에 "동결"된 것으로 간주됩니다. 런타임 체크 가능한 프로토콜에 속성을 몽키 패치하는 것은 여전히 작동하지만, 객체를 프로토콜과 비교하는 isinstance() 검사에는 영향을 미치지 않습니다. 자세한 내용은 "Python 3.12의 새로운 기능"을 참조하세요.

클래스 typing.TypedDict(dict)

딕셔너리에 형 힌트를 추가하는 특수 구조. 실행 시간에 일반 `dict`입니다.

`TypedDict`는 모든 인스턴스가 각 키가 일관된 형의 값에 연관되는, 특정한 키 집합을 갖도록 기대되는 딕셔너리 형을 선언합니다. 이 기대는 실행 시간에는 검사되지 않고, 형 검사기에서만 강제됩니다. 사용법:

```python
class Point2D(TypedDict):
    x: int
    y: int
    label: str

a: Point2D = {'x': 1, 'y': 2, 'label': 'good'}  # OK
b: Point2D = {'z': 3, 'label': 'bad'}           # Fails type check

assert Point2D(x=1, y=2, label='first') == dict(x=1, y=2, label='first')
```

이 기능을 PEP 526을 지원하지 않는 이전 버전의 Python에서 사용할 수 있도록 하기 위해, `TypedDict`는 두 가지 추가적인 동등한 구문 형식을 지원합니다:

- 두 번째 인자로 리터럴 `dict`를 사용:
    
    ```python
    Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': str})
    ```
    
- 키워드 인자 사용:
    
    ```python
    Point2D = TypedDict('Point2D', x=int, y=int, label=str)
    ```
    
    버전 3.11에서 폐기됨, 버전 3.13에서 제거 예정: 키워드 인자 구문은 3.11에서 폐기되었으며 3.13에서 제거될 예정입니다. 정적 형 검사기에서도 지원되지 않을 수 있습니다.
    

키 중 일부가 유효한 식별자가 아닐 때, 예를 들어 키워드이거나 하이픈을 포함할 때는 함수형 구문을 사용해야 합니다. 예시:

```python
# SyntaxError 발생
class Point2D(TypedDict):
    in: int  # 'in'은 키워드
    x-y: int  # 하이픈이 있는 이름

# OK, 함수형 구문
Point2D = TypedDict('Point2D', {'in': int, 'x-y': int})
```

기본적으로 모든 키는 `TypedDict`에 존재해야 합니다. `NotRequired`를 사용하여 개별 키를 필수가 아닌 것으로 표시할 수 있습니다:

```python
class Point2D(TypedDict):
    x: int
    y: int
    label: NotRequired[str]

# 대체 구문
Point2D = TypedDict('Point2D', {'x': int, 'y': int, 'label': NotRequired[str]})
```

이는 `Point2D` `TypedDict`에서 `label` 키를 생략할 수 있음을 의미합니다.

`total=False`를 지정하여 모든 키를 기본적으로 필수가 아닌 것으로 표시할 수도 있습니다:

```python
class Point2D(TypedDict, total=False):
    x: int
    y: int

# 대체 구문
Point2D = TypedDict('Point2D', {'x': int, 'y': int}, total=False)
```

이는 `Point2D` `TypedDict`에서 모든 키를 생략할 수 있음을 의미합니다. 형 검사기는 `total` 인자의 값으로 리터럴 `False` 또는 `True`만 지원할 것으로 예상됩니다. `True`가 기본값이며, 클래스 본문에 정의된 모든 항목을 필수로 만듭니다.

`total=False` `TypedDict`의 개별 키는 `Required`를 사용하여 필수로 표시할 수 있습니다:

```python
class Point2D(TypedDict, total=False):
    x: Required[int]
    y: Required[int]
    label: str

# 대체 구문
Point2D = TypedDict('Point2D', {
    'x': Required[int],
    'y': Required[int],
    'label': str
}, total=False)
```

클래스 기반 구문을 사용하여 `TypedDict` 형이 하나 이상의 다른 `TypedDict` 형을 상속하는 것이 가능합니다. 사용법:

```python
class Point3D(Point2D):
    z: int
```

`Point3D`는 세 개의 항목을 가집니다: `x`, `y`, `z`. 이는 다음 정의와 동등합니다:

```python
class Point3D(TypedDict):
    x: int
    y: int
    z: int
```

`TypedDict`는 `Generic`을 제외한 비`TypedDict` 클래스를 상속할 수 없습니다. 예를 들어:

```python
class X(TypedDict):
    x: int

class Y(TypedDict):
    y: int

class Z(object): pass  # 비TypedDict 클래스

class XY(X, Y): pass  # OK

class XZ(X, Z): pass  # TypeError 발생
```

`TypedDict`는 제네릭일 수 있습니다:

```python
class Group[T](TypedDict):
    key: T
    group: list[T]
```

Python 3.11 이하와 호환되는 제네릭 `TypedDict`를 만들려면 `Generic`을 명시적으로 상속받으십시오:

```python
T = TypeVar("T")

class Group(TypedDict, Generic[T]):
    key: T
    group: list[T]
```

`TypedDict`는 주석 딕셔너리(주석 모범 사례에 대한 자세한 정보는 주석 모범 사례 참조), `__total__`, `__required_keys__`, 그리고 `__optional_keys__`를 통해 내부 검사할 수 있습니다.

#### __total__

`Point2D.__total__`은 `total` 인자의 값을 제공합니다. 예시:

```python
>>> from typing import TypedDict
>>> class Point2D(TypedDict): pass
>>> Point2D.__total__
True
>>> class Point2D(TypedDict, total=False): pass
>>> Point2D.__total__
False
>>> class Point3D(Point2D): pass
>>> Point3D.__total__
True
```

이 속성은 현재 `TypedDict` 클래스에 대한 `total` 인자의 값만을 반영하며, 클래스가 의미적으로 전체인지 여부는 반영하지 않습니다. 예를 들어, `__total__`이 `True`로 설정된 `TypedDict`는 `NotRequired`로 표시된 키를 가질 수 있거나, `total=False`로 설정된 다른 `TypedDict`를 상속받을 수 있습니다. 따라서 일반적으로 내부 검사를 위해 `__required_keys__`와 `__optional_keys__`를 사용하는 것이 더 좋습니다.

#### __required_keys__

버전 3.9에서 추가됨.

#### __optional_keys__

`Point2D.__required_keys__`와 `Point2D.__optional_keys__`는 각각 필수 및 비필수 키를 포함하는 `frozenset` 객체를 반환합니다.

`Required`로 표시된 키는 항상 `__required_keys__`에 나타나고 `NotRequired`로 표시된 키는 항상 `__optional_keys__`에 나타납니다.

Python 3.10 이하 버전과의 호환성을 위해, 상속을 사용하여 동일한 `TypedDict`에서 필수 및 비필수 키를 모두 선언하는 것도 가능합니다. 이는 `total` 인자에 대해 하나의 값으로 `TypedDict`를 선언한 다음, 다른 값의 `total`로 설정된 다른 `TypedDict`에서 상속받는 방식으로 수행됩니다:

```python
>>> class Point2D(TypedDict, total=False):
…     x: int
…     y: int
…
>>> class Point3D(Point2D):
…     z: int
…
>>> Point3D.__required_keys__ == frozenset({'z'})
True
>>> Point3D.__optional_keys__ == frozenset({'x', 'y'})
True
```

버전 3.9에서 추가됨.

참고

 

`from __future__ import annotations`가 사용되거나 주석이 문자열로 주어진 경우, `TypedDict`가 정의될 때 주석이 평가되지 않습니다. 따라서 `__required_keys__`와 `__optional_keys__`가 의존하는 런타임 내부 검사가 제대로 작동하지 않을 수 있으며, 속성의 값이 부정확할 수 있습니다.

추가 예제와 `TypedDict`를 사용하는 자세한 규칙은 PEP 589를 참조하십시오.

버전 3.8에서 추가됨.

버전 3.11에서 변경: 개별 키를 `Required` 또는 `NotRequired`로 표시하는 기능이 추가되었습니다. PEP 655를 참조하십시오.

버전 3.11에서 변경: 제네릭 `TypedDict` 지원이 추가되었습니다.


### 프로토콜

typing 모듈에서 제공하는 프로토콜들입니다. 모두 @runtime_checkable로 장식되어 있습니다.

class typing.SupportsAbs

반환형이 공변적(covariant)인 하나의 추상 메서드 __abs__를 가진 ABC.

class typing.SupportsBytes

하나의 추상 메서드 __bytes__를 가진 ABC.

class typing.SupportsComplex

하나의 추상 메서드 __complex__를 가진 ABC.

class typing.SupportsFloat

하나의 추상 메서드 __float__를 가진 ABC.

class typing.SupportsIndex

하나의 추상 메서드 __index__를 가진 ABC.

3.8 버전에서 추가됨.

class typing.SupportsInt

하나의 추상 메서드 __int__를 가진 ABC.

class typing.SupportsRound

반환형이 공변적(covariant)인 하나의 추상 메서드 __round__를 가진 ABC.

### IO 작업을 위한 ABC (ABCs for working with IO)

class typing.IO

class typing.TextIO

class typing.BinaryIO

제네릭 타입 IO[AnyStr]와 그 하위 클래스인 TextIO(IO[str])와 BinaryIO(IO[bytes])는 open()이 반환하는 것과 같은 I/O 스트림의 타입을 나타냅니다.

### 함수와 데코레이터 (Functions and decorators)

typing.cast(typ, val)

값을 형으로 변환합니다.

값을 변경하지 않고 반환합니다. 형 검사기에서는 반환 값이 지정된 형임을 나타내지만, 실행 시간에는 의도적으로 아무것도 확인하지 않습니다 (우리는 이것이 가능한 한 빠르기를 원합니다).

typing.assert_type(val, typ, /)

정적 타입 검사기에게 val이 typ의 추론된 타입을 가지고 있는지 확인하도록 요청합니다.

런타임에는 아무것도 하지 않습니다: 첫 번째 인수를 변경하지 않고 반환하며, 실제 인수의 타입에 관계없이 검사나 부작용이 없습니다.

정적 타입 검사기가 assert_type() 호출을 만나면, 값이 지정된 타입이 아닌 경우 오류를 발생시킵니다:

```python
def greet(name: str) -> None:
    assert_type(name, str)  # OK, name의 추론된 타입은 str
    assert_type(name, int)  # 타입 검사기 오류
```

이 함수는 스크립트에 대한 타입 검사기의 이해가 개발자의 의도와 일치하는지 확인하는 데 유용합니다:

```python
def complex_function(arg: object):
    # 복잡한 타입-축소 로직을 수행한 후,
    # 추론된 타입이 int가 되기를 희망합니다
    …
    # 타입 검사기가 우리의 함수를 올바르게 이해하는지 테스트합니다
    assert_type(arg, int)
```

3.11 버전에서 추가됨.

typing.assert_never(arg, /)

정적 타입 검사기에게 코드의 한 줄이 도달할 수 없음을 확인하도록 요청합니다.

예시:

```python
def int_or_str(arg: int | str) -> None:
    match arg:
        case int():
            print("It's an int")
        case str():
            print("It's a str")
        case _ as unreachable:
            assert_never(unreachable)
```

여기서 주석을 통해 타입 검사기는 마지막 case가 절대 실행될 수 없다고 추론할 수 있습니다. 왜냐하면 arg는 int나 str이고, 두 옵션 모두 이전 case에서 다뤄지기 때문입니다.

타입 검사기가 assert_never() 호출이 도달 가능하다고 판단하면 오류를 발생시킵니다. 예를 들어, arg의 타입 주석이 int | str | float였다면, 타입 검사기는 unreachable이 float 타입이라는 점을 지적하는 오류를 발생시킬 것입니다. assert_never 호출이 타입 검사를 통과하려면, 전달된 인수의 추론된 타입이 반드시 Never 타입이어야 하며 그 외에는 안 됩니다.

런타임에는 호출 시 예외를 발생시킵니다.

참고

 

정적 타입으로 도달 불가능한 코드와 완전성 검사에 대한 더 많은 정보는 Unreachable Code and Exhaustiveness Checking을 참조하세요.

3.11 버전에서 추가됨.

typing.reveal_type(obj, /)

정적 타입 검사기에게 표현식의 추론된 타입을 밝히도록 요청합니다.

정적 타입 검사기가 이 함수의 호출을 만나면, 인수의 추론된 타입과 함께 진단을 내보냅니다. 예를 들어:

```python
x: int = 1
reveal_type(x)  # 밝혀진 타입은 "builtins.int"
```

이는 타입 검사기가 특정 코드를 어떻게 처리하는지 디버그하고 싶을 때 유용할 수 있습니다.

런타임에 이 함수는 인수의 런타임 타입을 sys.stderr에 출력하고 인수를 변경하지 않고 반환합니다 (표현식 내에서 호출을 사용할 수 있게 함):

```python
x = reveal_type(1)  # "Runtime type is int" 출력
print(x)  # "1" 출력
```

런타임 타입이 타입 검사기가 정적으로 추론한 타입과 다를 수 있음 (더 구체적이거나 덜 구체적일 수 있음)에 주의하세요.

대부분의 타입 검사기는 reveal_type()을 어디서든 지원하며, 심지어 이름이 typing에서 임포트되지 않았더라도 지원합니다. 하지만 이름을 typing에서 임포트하면 런타임 오류 없이 코드를 실행할 수 있고 의도를 더 명확하게 전달할 수 있습니다.

3.11 버전에서 추가됨.

@typing.dataclass_transform(*, eq_default=True, order_default=False, kw_only_default=False, frozen_default=False, field_specifiers=(), **kwargs)

객체가 dataclass와 유사한 동작을 제공한다는 것을 표시하는 데코레이터입니다.

dataclass_transform은 클래스, 메타클래스, 또는 그 자체가 데코레이터인 함수를 장식하는 데 사용될 수 있습니다. @dataclass_transform()의 존재는 정적 타입 검사기에게 장식된 객체가 @dataclasses.dataclass와 유사한 방식으로 클래스를 변환하는 런타임 "마법"을 수행한다고 알려줍니다.

데코레이터 함수와 함께 사용하는 예:

```python
@dataclass_transform()
def create_model[T](cls: type[T]) -> type[T]:
    …
    return cls

@create_model
class CustomerModel:
    id: int
    name: str
```

기본 클래스에 사용:

```python
@dataclass_transform()
class ModelBase: …

class CustomerModel(ModelBase):
    id: int
    name: str
```

메타클래스에 사용:

```python
@dataclass_transform()
class ModelMeta(type): …

class ModelBase(metaclass=ModelMeta): …

class CustomerModel(ModelBase):
    id: int
    name: str
```

위의 내용을 한국어로 번역하겠습니다. 요청하신 조건을 지켜 번역하였습니다.

위에서 정의된 `CustomerModel` 클래스는 타입 검사기에서 [`@dataclasses.dataclass`]로 생성된 클래스와 유사하게 처리됩니다. 예를 들어, 타입 검사기는 이러한 클래스가 `id`와 `name`을 받는 `__init__` 메서드를 가지고 있다고 가정할 것입니다.

데코레이트된 클래스, 메타클래스, 또는 함수는 다음과 같은 bool 인자를 받을 수 있으며, 타입 검사기는 이들이 [`@dataclasses.dataclass`] 데코레이터에서와 동일한 효과를 가진다고 가정할 것입니다: `init`, `eq`, `order`, `unsafe_hash`, `frozen`, `match_args`, `kw_only`, 그리고 `slots`. 이러한 인자의 값(`True` 또는 `False`)은 정적으로 평가될 수 있어야 합니다.

`dataclass_transform` 데코레이터의 인자는 데코레이트된 클래스, 메타클래스, 또는 함수의 기본 동작을 사용자 정의하는 데 사용될 수 있습니다:

매개변수:

- **eq_default** (bool) – 호출자가 `eq` 매개변수를 생략한 경우 `True` 또는 `False`로 가정되는지를 나타냅니다. 기본값은 `True`입니다.

- **order_default** (bool) – 호출자가 `order` 매개변수를 생략한 경우 `True` 또는 `False`로 가정되는지를 나타냅니다. 기본값은 `False`입니다.

- **kw_only_default** (bool) – 호출자가 `kw_only` 매개변수를 생략한 경우 `True` 또는 `False`로 가정되는지를 나타냅니다. 기본값은 `False`입니다.

- **frozen_default** (bool) – 호출자가 `frozen` 매개변수를 생략한 경우 `True` 또는 `False`로 가정되는지를 나타냅니다. 기본값은 `False`입니다.

  버전 3.12에서 추가되었습니다.

- **field_specifiers** (tuple[Callable[…, Any], …]) – [`dataclasses.field()`]와 유사하게 필드를 설명하는 지원되는 클래스나 함수의 정적 목록을 지정합니다. 기본값은 `()`입니다.

- ****kwargs** (Any) – 가능한 미래의 확장을 위해 임의의 다른 키워드 인자가 허용됩니다.

타입 검사기는 필드 지정자에 대해 다음과 같은 선택적 매개변수를 인식합니다:

**필드 지정자에 대해 인식되는 매개변수**
|매개변수 이름|설명|
|---|---|
|`init`|필드가 합성된 `__init__` 메서드에 포함되어야 하는지를 나타냅니다. 지정되지 않은 경우, `init`의 기본값은 `True`입니다.|
|`default`|필드의 기본값을 제공합니다.|
|`default_factory`|필드의 기본값을 반환하는 런타임 콜백을 제공합니다. `default`와 `default_factory` 모두 지정되지 않은 경우, 해당 필드는 기본값이 없다고 가정되며 클래스 인스턴스화 시 값이 제공되어야 합니다.|
|`factory`|필드 지정자의 `default_factory` 매개변수의 별칭입니다.|
|`kw_only`|필드가 키워드 전용으로 표시되어야 하는지를 나타냅니다. `True`인 경우 필드는 키워드 전용이 됩니다. `False`인 경우 키워드 전용이 아닙니다. 지정되지 않은 경우, `dataclass_transform`으로 데코레이트된 객체의 `kw_only` 매개변수 값이 사용되며, 그것도 지정되지 않은 경우 `dataclass_transform`의 `kw_only_default` 값이 사용됩니다.|
|`alias`|필드의 대체 이름을 제공합니다. 이 대체 이름은 합성된 `__init__` 메서드에서 사용됩니다.|

런타임에 이 데코레이터는 데코레이트된 객체의 `__dataclass_transform__` 속성에 그 인자를 기록합니다. 다른 런타임 효과는 없습니다.

자세한 내용은 **PEP 681**을 참조하세요.

버전 3.11에서 추가되었습니다.

#### 오버로드 (overload)

오버로드된 함수와 메서드를 생성하기 위한 데코레이터입니다.

`@overload` 데코레이터는 여러 다른 인자 타입 조합을 지원하는 함수와 메서드를 설명할 수 있게 해줍니다. `@overload`로 데코레이트된 일련의 정의 뒤에는 정확히 하나의 `@overload`로 데코레이트되지 않은 정의(동일한 함수/메서드에 대해)가 따라와야 합니다.

`@overload`로 데코레이트된 정의는 타입 검사기의 이익을 위한 것일 뿐입니다. 왜냐하면 이들은 `@overload`로 데코레이트되지 않은 정의에 의해 덮어쓰여질 것이기 때문입니다. 한편, `@overload`로 데코레이트되지 않은 정의는 런타임에 사용되지만 타입 검사기에 의해 무시되어야 합니다. 런타임에 `@overload`로 데코레이트된 함수를 직접 호출하면 NotImplementedError가 발생합니다.

union이나 타입 변수를 사용하여 표현할 수 있는 것보다 더 정확한 타입을 제공하는 오버로드의 예시:

```python
@overload
def process(response: None) -> None:
    …
@overload
def process(response: int) -> tuple[int, str]:
    …
@overload
def process(response: bytes) -> str:
    …
def process(response):
    …  # 실제 구현은 여기에 들어갑니다
```

자세한 내용과 다른 타이핑 의미론과의 비교는 **PEP 484**를 참조하세요.

버전 3.11에서 변경: 오버로드된 함수는 이제 get_overloads()를 사용하여 런타임에 내성 검사할 수 있습니다.

#### get_overloads (get_overloads)

func에 대한 @overload로 데코레이트된 정의의 시퀀스를 반환합니다.

func는 오버로드된 함수의 구현에 대한 함수 객체입니다. 예를 들어, @overload 문서에서 process의 정의가 주어진 경우, get_overloads(process)는 정의된 세 가지 오버로드에 대한 세 개의 함수 객체의 시퀀스를 반환합니다. 오버로드가 없는 함수에 대해 호출된 경우, get_overloads()는 빈 시퀀스를 반환합니다.

get_overloads()는 런타임에 오버로드된 함수를 내성 검사하는 데 사용될 수 있습니다.

버전 3.11에서 추가되었습니다.

#### clear_overloads (clear_overloads)

내부 레지스트리에 등록된 모든 오버로드를 지웁니다.

이는 레지스트리가 사용한 메모리를 회수하는 데 사용될 수 있습니다.

버전 3.11에서 추가되었습니다.

#### 최종 (final)

최종 메서드와 최종 클래스를 나타내는 데코레이터입니다.

메서드를 @final로 데코레이트하는 것은 타입 검사기에게 해당 메서드가 서브클래스에서 오버라이드될 수 없음을 나타냅니다. 클래스를 @final로 데코레이트하는 것은 해당 클래스가 서브클래싱될 수 없음을 나타냅니다.

예를 들면:

```python
class Base:
    @final
    def done(self) -> None:
        …
class Sub(Base):
    def done(self) -> None:  # 타입 검사기에 의해 오류가 보고됩니다
        …

@final
class Leaf:
    …
class Other(Leaf):  # 타입 검사기에 의해 오류가 보고됩니다
    …
```

이러한 속성에 대한 실행 시간 검사는 없습니다. 자세한 내용은 **PEP 591**을 참조하십시오.

버전 3.8에서 추가되었습니다.

버전 3.11에서 변경: 데코레이터는 이제 장식된 객체에 `__final__` 속성을 `True`로 설정하려고 시도합니다. 따라서 `if getattr(obj, "__final__", False)`와 같은 검사를 실행 시간에 사용하여 객체 `obj`가 final로 표시되었는지 확인할 수 있습니다. 장식된 객체가 속성 설정을 지원하지 않는 경우 데코레이터는 예외를 발생시키지 않고 객체를 변경하지 않은 채로 반환합니다.

@typing.no_type_check

어노테이션이 형 힌트가 아님을 나타내는 데코레이터.

이것은 클래스나 함수 데코레이터로 작동합니다. 클래스와 함께 사용할 경우, 해당 클래스에 정의된 모든 메서드와 클래스에 재귀적으로 적용됩니다 (하지만 상위 클래스나 하위 클래스에 정의된 메서드에는 적용되지 않습니다). 타입 검사기는 이 데코레이터가 있는 함수나 클래스의 모든 어노테이션을 무시합니다.

`@no_type_check`는 장식된 객체를 그 자리에서 변경합니다.

@typing.no_type_check_decorator

다른 데코레이터에 `no_type_check()` 효과를 주는 데코레이터.

이것은 데코레이트 된 함수를 `no_type_check()`로 감싸는 무언가로 데코레이터를 감쌉니다.

@typing.override

서브클래스의 메서드가 상위 클래스의 메서드나 속성을 오버라이드하려는 의도임을 나타내는 데코레이터.

타입 검사기는 `@override`로 장식된 메서드가 실제로 아무것도 오버라이드하지 않는 경우 오류를 발생시켜야 합니다. 이는 기본 클래스가 변경될 때 자식 클래스에 대응하는 변경이 없을 경우 발생할 수 있는 버그를 방지하는 데 도움이 됩니다.

예를 들어:

```python
class Base:
    def log_status(self) -> None:
        …

class Sub(Base):
    @override
    def log_status(self) -> None:  # 정상: Base.log_status를 오버라이드함
        …

    @override
    def done(self) -> None:  # 타입 검사기가 오류를 보고함
        …
```

이 속성에 대한 런타임 검사는 없습니다.

데코레이터는 장식된 객체에 `__override__` 속성을 `True`로 설정하려고 시도합니다. 따라서 `if getattr(obj, "__override__", False)`와 같은 검사를 실행 시간에 사용하여 객체 `obj`가 오버라이드로 표시되었는지 확인할 수 있습니다. 장식된 객체가 속성 설정을 지원하지 않는 경우 데코레이터는 예외를 발생시키지 않고 객체를 변경하지 않은 채로 반환합니다.

자세한 내용은 PEP 698을 참조하세요.

> 버전 3.12에 추가됨.

`@typing.type_check_only`

런타임에 사용할 수 없는 클래스나 함수를 표시하는 데코레이터.

이 데코레이터 자체는 실행 시간에 사용할 수 없습니다. 주로, 구현이 비공개 클래스의 인스턴스를 반환할 때, 형 스텁 파일에 정의된 클래스를 표시하기 위한 용도입니다:

```python
@type_check_only
class Response:  # 비공개이거나 런타임에 사용할 수 없음
    code: int
    def get_header(self, name: str) -> str: …

def fetch_response() -> Response: …
```

비공개 클래스의 인스턴스를 반환하는 것은 좋지 않음에 유의하십시오. 일반적으로 그러한 클래스를 공개로 만드는 것이 바람직합니다.

### 인트로스펙션 도우미 (Introspection helpers)

`typing.get_type_hints(obj, globalns=None, localns=None, include_extras=False)`

함수, 메서드, 모듈 또는 클래스 객체에 대한 형 힌트가 포함된 딕셔너리를 반환합니다.

이는 종종 `obj.__annotations__`와 동일하지만, 이 함수는 어노테이션 딕셔너리에 다음과 같은 변경을 가합니다:

- 문자열 리터럴이나 `ForwardRef` 객체로 인코딩된 전방 참조는 globalns, localns, 그리고 (해당되는 경우) obj의 타입 매개변수 네임스페이스에서 평가하여 처리됩니다. globalns나 localns가 주어지지 않으면 obj로부터 적절한 네임스페이스 딕셔너리를 추론합니다.
- `None`은 `types.NoneType`으로 대체됩니다.
- `@no_type_check`가 obj에 적용된 경우 빈 딕셔너리가 반환됩니다.
- obj가 클래스 C인 경우, 이 함수는 C의 기본 클래스들의 어노테이션과 C에 직접 있는 어노테이션을 병합한 딕셔너리를 반환합니다. 이는 C.__mro__를 순회하고 __annotations__ 딕셔너리를 반복적으로 결합하여 수행됩니다. 메서드 해결 순서에서 더 앞서 나타나는 클래스의 어노테이션이 항상 더 뒤에 나타나는 클래스의 어노테이션보다 우선합니다.
- 이 함수는 include_extras가 True로 설정되지 않는 한, `Annotated[T, …]`의 모든 출현을 재귀적으로 T로 대체합니다 (자세한 내용은 Annotated 참조).

또한 어노테이션을 더 직접적으로 반환하는 저수준 함수인 `inspect.get_annotations()`를 참조하세요.


> [!NOTE]
> obj의 어노테이션에 있는 전방 참조 중 해결할 수 없거나 유효한 Python 코드가 아닌 것이 있다면, 이 함수는 `NameError`와 같은 예외를 발생시킬 것입니다. 예를 들어, 이는 전방 참조를 포함하는 가져온 타입 별칭이나 `if TYPE_CHECKING` 아래에서 가져온 이름들과 함께 발생할 수 있습니다.

> 버전 3.9에서 변경: PEP 593의 일부로 include_extras 매개변수가 추가되었습니다. 자세한 내용은 Annotated에 대한 문서를 참조하세요.
> 버전 3.11에서 변경: 이전에는 함수와 메서드 어노테이션에 대해 None과 같은 기본값이 설정된 경우 Optional[t]가 추가되었습니다. 이제 어노테이션은 변경되지 않고 반환됩니다.

`typing.get_origin(tp)`

타입의 구독되지 않은 버전을 가져옵니다: X[Y, Z, …] 형태의 타이핑 객체에 대해 X를 반환합니다.

X가 내장 또는 collections 클래스에 대한 타이핑 모듈 별칭인 경우, 원래 클래스로 정규화됩니다. X가 ParamSpecArgs 또는 ParamSpecKwargs의 인스턴스인 경우, 기본 ParamSpec를 반환합니다. 지원되지 않는 객체에 대해서는 None을 반환합니다.

예시:

```python
assert get_origin(str) is None
assert get_origin(Dict[str, int]) is dict
assert get_origin(Union[int, str]) is Union
assert get_origin(Annotated[str, "metadata"]) is Annotated
P = ParamSpec('P')
assert get_origin(P.args) is P
assert get_origin(P.kwargs) is P
```

> 버전 3.8에 추가됨.

`typing.get_args(tp)`

모든 대체가 수행된 타입 인수를 가져옵니다: X[Y, Z, …] 형태의 타이핑 객체에 대해 (Y, Z, …)를 반환합니다.

X가 다른 제네릭 타입에 포함된 유니온이나 Literal인 경우, 타입 캐싱으로 인해 (Y, Z, …)의 순서가 원래 인수 [Y, Z, …]의 순서와 다를 수 있습니다. 지원되지 않는 객체에 대해서는 ()를 반환합니다.

예시:

```python
assert get_args(int) == ()
assert get_args(Dict[int, str]) == (int, str)
assert get_args(Union[int, str]) == (int, str)
```

버전 3.8에 추가되었습니다.

`typing.is_typeddict(tp)`

타입이 TypedDict인지 확인합니다.

예를 들어:

```python
class Film(TypedDict):
    title: str
    year: int

assert is_typeddict(Film)
assert not is_typeddict(list | str)

# TypedDict는 타입된 딕셔너리를 생성하기 위한 팩토리이며,
# 그 자체로 타입된 딕셔너리가 아닙니다
assert not is_typeddict(TypedDict)
```

> 버전 3.10에 추가되었습니다.

`class typing.ForwardRef`

문자열 전방 참조의 내부 타이핑 표현에 사용되는 클래스입니다.

예를 들어, `List["SomeClass"]`는 암시적으로 `List[ForwardRef("SomeClass")]`로 변환됩니다. ForwardRef는 사용자가 직접 인스턴스화해서는 안 되지만, 내부 검사 도구에 의해 사용될 수 있습니다.


> [!NOTE]
> PEP 585 일반 타입 (예: list["SomeClass"])은 암시적으로 list[ForwardRef("SomeClass")]로 변환되지 않으며, 따라서 자동으로 list[SomeClass]로 해석되지 않습니다.

> 버전 3.7.4에 추가되었습니다.

### 상수 (Constant)

`typing.TYPE_CHECKING`

3rd 파티 정적 타입 검사기에 의해 True로 가정되는 특수 상수입니다. 런타임에는 False입니다.

사용법:

```python
if TYPE_CHECKING:
    import expensive_mod

def fun(arg: 'expensive_mod.SomeType') -> None:
    local_var: expensive_mod.AnotherType = other_fun()
```

첫 번째 어노테이션은 따옴표로 묶여야 합니다, "전방 참조"로 만들어서 인터프리터 실행 시간에 expensive_mod 참조를 숨깁니다. 지역 변수에 대한 형 어노테이션은 평가되지 않기 때문에, 두 번째 어노테이션을 따옴표로 묶을 필요는 없습니다.

> [!NOTE]
> `from __future__ import annotations`가 사용되면, 어노테이션은 함수 정의 시점에 평가되지 않습니다. 대신, `__annotations__`에 문자열로 저장됩니다. 이로 인해 어노테이션 주위에 따옴표를 사용할 필요가 없어집니다 (PEP 563 참조).

> 버전 3.5.2에 추가되었습니다.

### 폐지된 별칭 (Deprecated aliases)

이 모듈은 기존 표준 라이브러리 클래스에 대한 여러 폐지된 별칭을 정의합니다. 이들은 원래 []를 사용하여 이러한 일반 클래스를 매개변수화하기 위해 typing 모듈에 포함되었습니다. 그러나 Python 3.9에서 해당하는 기존 클래스가 []를 지원하도록 개선되면서 이 별칭들은 중복되었습니다 (PEP 585 참조).

중복된 타입들은 Python 3.9부터 폐지되었습니다. 그러나 별칭들이 언젠가 제거될 수 있지만, 현재 이러한 별칭들의 제거는 계획되어 있지 않습니다. 따라서 현재 인터프리터는 이러한 별칭들에 대해 폐지 경고를 발행하지 않습니다.

만약 이러한 폐지된 별칭들을 제거하기로 결정된다면, 제거 전 최소 두 번의 릴리스 동안 인터프리터가 폐지 경고를 발행할 것입니다. 이 별칭들은 최소한 Python 3.14까지는 폐지 경고 없이 typing 모듈에 남아있을 것이 보장됩니다.

타입 검사기는 검사 중인 프로그램이 최소 Python 버전 3.9 이상을 대상으로 한다면 폐지된 타입의 사용을 표시하도록 권장됩니다.

#### 내장 타입에 대한 별칭 (Aliases to built-in types)

`class typing.Dict(dict, MutableMapping[KT, VT])`

dict에 대한 폐지된 별칭입니다.
인수에 주석을 달 때는 dict나 typing.Dict 대신 Mapping과 같은 추상 컬렉션 타입을 사용하는 것이 좋습니다.

> 버전 3.9부터 폐지됨: builtins.dict가 이제 서브스크립팅 ([])을 지원합니다. PEP 585와 제네릭 에일리어스 형을 참조하세요.

`class typing.List(list, MutableSequence[T])`

list에 대한 폐지된 별칭입니다.
인수에 주석을 달 때는 list나 typing.List 대신 Sequence나 Iterable과 같은 추상 컬렉션 타입을 사용하는 것이 좋습니다.

> 버전 3.9부터 폐지됨: builtins.list가 이제 서브스크립팅 ([])을 지원합니다. PEP 585와 제네릭 에일리어스 형을 참조하세요.

`class typing.Set(set, MutableSet[T])`

builtins.set에 대한 폐지된 별칭입니다.
인수에 주석을 달 때는 set나 typing.Set 대신 collections.abc.Set과 같은 추상 컬렉션 타입을 사용하는 것이 좋습니다.

> 버전 3.9부터 폐지됨: builtins.set이 이제 서브스크립팅 ([])을 지원합니다. PEP 585와 제네릭 에일리어스 형을 참조하세요.

`class typing.FrozenSet(frozenset, AbstractSet[T_co])`

builtins.frozenset에 대한 폐지된 별칭입니다.

> 버전 3.9부터 폐지됨: builtins.frozenset이 이제 서브스크립팅 ([])을 지원합니다. PEP 585와 제네릭 에일리어스 형을 참조하세요.

`typing.Tuple`

tuple에 대한 폐지된 별칭입니다.
tuple과 Tuple은 타입 시스템에서 특별 취급됩니다; 자세한 내용은 튜플 주석 달기를 참조하세요.

> 버전 3.9부터 폐지됨: builtins.tuple이 이제 서브스크립팅 ([])을 지원합니다. PEP 585와 제네릭 에일리어스 형을 참조하세요.

`class typing.Type(Generic[CT_co])`

type에 대한 폐지된 별칭입니다.
타입 주석에서 type이나 typing.Type을 사용하는 방법에 대한 자세한 내용은 클래스 객체의 타입을 참조하세요.

> 버전 3.5.2에 추가되었습니다.
> 버전 3.9부터 폐지됨: builtins.type이 이제 서브스크립팅 ([])을 지원합니다. PEP 585와 제네릭 에일리어스 형을 참조하세요.


#TODO 
- [ ] 번역하기
#### Aliases to types in [`collections`](https://docs.python.org/ko/3.12/library/collections.html#module-collections "collections: Container datatypes")[](https://docs.python.org/ko/3.12/library/typing.html#aliases-to-types-in-collections "Link to this heading")

_class_ typing.DefaultDict(_collections.defaultdict, MutableMapping[KT, VT]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.DefaultDict "Link to this definition")

Deprecated alias to [`collections.defaultdict`](https://docs.python.org/ko/3.12/library/collections.html#collections.defaultdict "collections.defaultdict").

Added in version 3.5.2.

버전 3.9부터 폐지됨: [`collections.defaultdict`](https://docs.python.org/ko/3.12/library/collections.html#collections.defaultdict "collections.defaultdict") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.OrderedDict(_collections.OrderedDict, MutableMapping[KT, VT]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.OrderedDict "Link to this definition")

Deprecated alias to [`collections.OrderedDict`](https://docs.python.org/ko/3.12/library/collections.html#collections.OrderedDict "collections.OrderedDict").

Added in version 3.7.2.

버전 3.9부터 폐지됨: [`collections.OrderedDict`](https://docs.python.org/ko/3.12/library/collections.html#collections.OrderedDict "collections.OrderedDict") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.ChainMap(_collections.ChainMap, MutableMapping[KT, VT]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.ChainMap "Link to this definition")

Deprecated alias to [`collections.ChainMap`](https://docs.python.org/ko/3.12/library/collections.html#collections.ChainMap "collections.ChainMap").

Added in version 3.6.1.

버전 3.9부터 폐지됨: [`collections.ChainMap`](https://docs.python.org/ko/3.12/library/collections.html#collections.ChainMap "collections.ChainMap") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.Counter(_collections.Counter, Dict[T, int]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.Counter "Link to this definition")

Deprecated alias to [`collections.Counter`](https://docs.python.org/ko/3.12/library/collections.html#collections.Counter "collections.Counter").

Added in version 3.6.1.

버전 3.9부터 폐지됨: [`collections.Counter`](https://docs.python.org/ko/3.12/library/collections.html#collections.Counter "collections.Counter") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.Deque(_deque, MutableSequence[T]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.Deque "Link to this definition")

Deprecated alias to [`collections.deque`](https://docs.python.org/ko/3.12/library/collections.html#collections.deque "collections.deque").

Added in version 3.6.1.

버전 3.9부터 폐지됨: [`collections.deque`](https://docs.python.org/ko/3.12/library/collections.html#collections.deque "collections.deque") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

#### Aliases to other concrete types[](https://docs.python.org/ko/3.12/library/typing.html#aliases-to-other-concrete-types "Link to this heading")

> Deprecated since version 3.8, will be removed in version 3.13: The `typing.io` namespace is deprecated and will be removed. These types should be directly imported from `typing` instead.

_class_ typing.Pattern[](https://docs.python.org/ko/3.12/library/typing.html#typing.Pattern "Link to this definition")

_class_ typing.Match[](https://docs.python.org/ko/3.12/library/typing.html#typing.Match "Link to this definition")

Deprecated aliases corresponding to the return types from [`re.compile()`](https://docs.python.org/ko/3.12/library/re.html#re.compile "re.compile") and [`re.match()`](https://docs.python.org/ko/3.12/library/re.html#re.match "re.match").

These types (and the corresponding functions) are generic over [`AnyStr`](https://docs.python.org/ko/3.12/library/typing.html#typing.AnyStr "typing.AnyStr"). `Pattern` can be specialised as `Pattern[str]` or `Pattern[bytes]`; `Match` can be specialised as `Match[str]` or `Match[bytes]`.

Deprecated since version 3.8, will be removed in version 3.13: The `typing.re` namespace is deprecated and will be removed. These types should be directly imported from `typing` instead.

버전 3.9부터 폐지됨: [`re`](https://docs.python.org/ko/3.12/library/re.html#module-re "re: Regular expression operations.")의 클래스 `Pattern`과 `Match`는 이제 `[]`를 지원합니다. [**PEP 585**](https://peps.python.org/pep-0585/)와 [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias)을 참조하십시오.

_class_ typing.Text[](https://docs.python.org/ko/3.12/library/typing.html#typing.Text "Link to this definition")

Deprecated alias for [`str`](https://docs.python.org/ko/3.12/library/stdtypes.html#str "str").

`Text` is provided to supply a forward compatible path for Python 2 code: in Python 2, `Text` is an alias for `unicode`.

`Text`를 사용하여 값이 파이썬 2와 파이썬 3 모두와 호환되는 방식으로 유니코드 문자열을 포함해야 함을 나타내십시오:

def add_unicode_checkmark(text: Text) -> Text:
    return text + u' \u2713'

Added in version 3.5.2.

버전 3.11부터 폐지됨: Python 2 is no longer supported, and most type checkers also no longer support type checking Python 2 code. Removal of the alias is not currently planned, but users are encouraged to use [`str`](https://docs.python.org/ko/3.12/library/stdtypes.html#str "str") instead of `Text`.

#### Aliases to container ABCs in [`collections.abc`](https://docs.python.org/ko/3.12/library/collections.abc.html#module-collections.abc "collections.abc: Abstract base classes for containers")[](https://docs.python.org/ko/3.12/library/typing.html#aliases-to-container-abcs-in-collections-abc "Link to this heading")

_class_ typing.AbstractSet(_Collection[T_co]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.AbstractSet "Link to this definition")

Deprecated alias to [`collections.abc.Set`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Set "collections.abc.Set").

버전 3.9부터 폐지됨: [`collections.abc.Set`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Set "collections.abc.Set") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.ByteString(_Sequence[int]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.ByteString "Link to this definition")

이 형은 [`bytes`](https://docs.python.org/ko/3.12/library/stdtypes.html#bytes "bytes"), [`bytearray`](https://docs.python.org/ko/3.12/library/stdtypes.html#bytearray "bytearray") 및 바이트 시퀀스의 [`memoryview`](https://docs.python.org/ko/3.12/library/stdtypes.html#memoryview "memoryview") 형을 나타냅니다.

Deprecated since version 3.9, will be removed in version 3.14: Prefer [`collections.abc.Buffer`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Buffer "collections.abc.Buffer"), or a union like `bytes | bytearray | memoryview`.

_class_ typing.Collection(_Sized, Iterable[T_co], Container[T_co]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.Collection "Link to this definition")

Deprecated alias to [`collections.abc.Collection`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Collection "collections.abc.Collection").

Added in version 3.6.

버전 3.9부터 폐지됨: [`collections.abc.Collection`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Collection "collections.abc.Collection") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.Container(_Generic[T_co]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.Container "Link to this definition")

Deprecated alias to [`collections.abc.Container`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Container "collections.abc.Container").

버전 3.9부터 폐지됨: [`collections.abc.Container`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Container "collections.abc.Container") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.ItemsView(_MappingView, AbstractSet[tuple[KT_co, VT_co]]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.ItemsView "Link to this definition")

Deprecated alias to [`collections.abc.ItemsView`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.ItemsView "collections.abc.ItemsView").

버전 3.9부터 폐지됨: [`collections.abc.ItemsView`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.ItemsView "collections.abc.ItemsView") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.KeysView(_MappingView, AbstractSet[KT_co]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.KeysView "Link to this definition")

Deprecated alias to [`collections.abc.KeysView`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.KeysView "collections.abc.KeysView").

버전 3.9부터 폐지됨: [`collections.abc.KeysView`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.KeysView "collections.abc.KeysView") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.Mapping(_Collection[KT], Generic[KT, VT_co]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.Mapping "Link to this definition")

Deprecated alias to [`collections.abc.Mapping`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Mapping "collections.abc.Mapping").

버전 3.9부터 폐지됨: [`collections.abc.Mapping`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Mapping "collections.abc.Mapping") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.MappingView(_Sized_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.MappingView "Link to this definition")

Deprecated alias to [`collections.abc.MappingView`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.MappingView "collections.abc.MappingView").

버전 3.9부터 폐지됨: [`collections.abc.MappingView`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.MappingView "collections.abc.MappingView") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.MutableMapping(_Mapping[KT, VT]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.MutableMapping "Link to this definition")

Deprecated alias to [`collections.abc.MutableMapping`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.MutableMapping "collections.abc.MutableMapping").

버전 3.9부터 폐지됨: [`collections.abc.MutableMapping`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.MutableMapping "collections.abc.MutableMapping") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.MutableSequence(_Sequence[T]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.MutableSequence "Link to this definition")

Deprecated alias to [`collections.abc.MutableSequence`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.MutableSequence "collections.abc.MutableSequence").

버전 3.9부터 폐지됨: [`collections.abc.MutableSequence`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.MutableSequence "collections.abc.MutableSequence") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.MutableSet(_AbstractSet[T]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.MutableSet "Link to this definition")

Deprecated alias to [`collections.abc.MutableSet`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.MutableSet "collections.abc.MutableSet").

버전 3.9부터 폐지됨: [`collections.abc.MutableSet`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.MutableSet "collections.abc.MutableSet") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.Sequence(_Reversible[T_co], Collection[T_co]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.Sequence "Link to this definition")

Deprecated alias to [`collections.abc.Sequence`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence").

버전 3.9부터 폐지됨: [`collections.abc.Sequence`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.ValuesView(_MappingView, Collection[_VT_co]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.ValuesView "Link to this definition")

Deprecated alias to [`collections.abc.ValuesView`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.ValuesView "collections.abc.ValuesView").

버전 3.9부터 폐지됨: [`collections.abc.ValuesView`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.ValuesView "collections.abc.ValuesView") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

#### Aliases to asynchronous ABCs in [`collections.abc`](https://docs.python.org/ko/3.12/library/collections.abc.html#module-collections.abc "collections.abc: Abstract base classes for containers")[](https://docs.python.org/ko/3.12/library/typing.html#aliases-to-asynchronous-abcs-in-collections-abc "Link to this heading")

_class_ typing.Coroutine(_Awaitable[ReturnType], Generic[YieldType, SendType, ReturnType]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.Coroutine "Link to this definition")

Deprecated alias to [`collections.abc.Coroutine`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Coroutine "collections.abc.Coroutine").

See [Annotating generators and coroutines](https://docs.python.org/ko/3.12/library/typing.html#annotating-generators-and-coroutines) for details on using [`collections.abc.Coroutine`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Coroutine "collections.abc.Coroutine") and `typing.Coroutine` in type annotations.

Added in version 3.5.3.

버전 3.9부터 폐지됨: [`collections.abc.Coroutine`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Coroutine "collections.abc.Coroutine") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.AsyncGenerator(_AsyncIterator[YieldType], Generic[YieldType, SendType]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.AsyncGenerator "Link to this definition")

Deprecated alias to [`collections.abc.AsyncGenerator`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.AsyncGenerator "collections.abc.AsyncGenerator").

See [Annotating generators and coroutines](https://docs.python.org/ko/3.12/library/typing.html#annotating-generators-and-coroutines) for details on using [`collections.abc.AsyncGenerator`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.AsyncGenerator "collections.abc.AsyncGenerator") and `typing.AsyncGenerator` in type annotations.

Added in version 3.6.1.

버전 3.9부터 폐지됨: [`collections.abc.AsyncGenerator`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.AsyncGenerator "collections.abc.AsyncGenerator") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.AsyncIterable(_Generic[T_co]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.AsyncIterable "Link to this definition")

Deprecated alias to [`collections.abc.AsyncIterable`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.AsyncIterable "collections.abc.AsyncIterable").

Added in version 3.5.2.

버전 3.9부터 폐지됨: [`collections.abc.AsyncIterable`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.AsyncIterable "collections.abc.AsyncIterable") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.AsyncIterator(_AsyncIterable[T_co]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.AsyncIterator "Link to this definition")

Deprecated alias to [`collections.abc.AsyncIterator`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.AsyncIterator "collections.abc.AsyncIterator").

Added in version 3.5.2.

버전 3.9부터 폐지됨: [`collections.abc.AsyncIterator`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.AsyncIterator "collections.abc.AsyncIterator") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.Awaitable(_Generic[T_co]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.Awaitable "Link to this definition")

Deprecated alias to [`collections.abc.Awaitable`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Awaitable "collections.abc.Awaitable").

Added in version 3.5.2.

버전 3.9부터 폐지됨: [`collections.abc.Awaitable`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Awaitable "collections.abc.Awaitable") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

#### Aliases to other ABCs in [`collections.abc`](https://docs.python.org/ko/3.12/library/collections.abc.html#module-collections.abc "collections.abc: Abstract base classes for containers")[](https://docs.python.org/ko/3.12/library/typing.html#aliases-to-other-abcs-in-collections-abc "Link to this heading")

_class_ typing.Iterable(_Generic[T_co]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.Iterable "Link to this definition")

Deprecated alias to [`collections.abc.Iterable`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Iterable "collections.abc.Iterable").

버전 3.9부터 폐지됨: [`collections.abc.Iterable`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Iterable "collections.abc.Iterable") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.Iterator(_Iterable[T_co]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.Iterator "Link to this definition")

Deprecated alias to [`collections.abc.Iterator`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Iterator "collections.abc.Iterator").

버전 3.9부터 폐지됨: [`collections.abc.Iterator`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Iterator "collections.abc.Iterator") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

typing.Callable[](https://docs.python.org/ko/3.12/library/typing.html#typing.Callable "Link to this definition")

Deprecated alias to [`collections.abc.Callable`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable").

See [Annotating callable objects](https://docs.python.org/ko/3.12/library/typing.html#annotating-callables) for details on how to use [`collections.abc.Callable`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable") and `typing.Callable` in type annotations.

버전 3.9부터 폐지됨: [`collections.abc.Callable`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

버전 3.10에서 변경: `Callable` now supports [`ParamSpec`](https://docs.python.org/ko/3.12/library/typing.html#typing.ParamSpec "typing.ParamSpec") and [`Concatenate`](https://docs.python.org/ko/3.12/library/typing.html#typing.Concatenate "typing.Concatenate"). See [**PEP 612**](https://peps.python.org/pep-0612/) for more details.

_class_ typing.Generator(_Iterator[YieldType], Generic[YieldType, SendType, ReturnType]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.Generator "Link to this definition")

Deprecated alias to [`collections.abc.Generator`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Generator "collections.abc.Generator").

See [Annotating generators and coroutines](https://docs.python.org/ko/3.12/library/typing.html#annotating-generators-and-coroutines) for details on using [`collections.abc.Generator`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Generator "collections.abc.Generator") and `typing.Generator` in type annotations.

버전 3.9부터 폐지됨: [`collections.abc.Generator`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Generator "collections.abc.Generator") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.Hashable[](https://docs.python.org/ko/3.12/library/typing.html#typing.Hashable "Link to this definition")

Deprecated alias to [`collections.abc.Hashable`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Hashable "collections.abc.Hashable").

버전 3.12부터 폐지됨: Use [`collections.abc.Hashable`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Hashable "collections.abc.Hashable") directly instead.

_class_ typing.Reversible(_Iterable[T_co]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.Reversible "Link to this definition")

Deprecated alias to [`collections.abc.Reversible`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Reversible "collections.abc.Reversible").

버전 3.9부터 폐지됨: [`collections.abc.Reversible`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Reversible "collections.abc.Reversible") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.Sized[](https://docs.python.org/ko/3.12/library/typing.html#typing.Sized "Link to this definition")

Deprecated alias to [`collections.abc.Sized`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Sized "collections.abc.Sized").

버전 3.12부터 폐지됨: Use [`collections.abc.Sized`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Sized "collections.abc.Sized") directly instead.

#### Aliases to [`contextlib`](https://docs.python.org/ko/3.12/library/contextlib.html#module-contextlib "contextlib: Utilities for with-statement contexts.") ABCs[](https://docs.python.org/ko/3.12/library/typing.html#aliases-to-contextlib-abcs "Link to this heading")

_class_ typing.ContextManager(_Generic[T_co]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.ContextManager "Link to this definition")

Deprecated alias to [`contextlib.AbstractContextManager`](https://docs.python.org/ko/3.12/library/contextlib.html#contextlib.AbstractContextManager "contextlib.AbstractContextManager").

Added in version 3.5.4.

버전 3.9부터 폐지됨: [`contextlib.AbstractContextManager`](https://docs.python.org/ko/3.12/library/contextlib.html#contextlib.AbstractContextManager "contextlib.AbstractContextManager") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

_class_ typing.AsyncContextManager(_Generic[T_co]_)[](https://docs.python.org/ko/3.12/library/typing.html#typing.AsyncContextManager "Link to this definition")

Deprecated alias to [`contextlib.AbstractAsyncContextManager`](https://docs.python.org/ko/3.12/library/contextlib.html#contextlib.AbstractAsyncContextManager "contextlib.AbstractAsyncContextManager").

Added in version 3.6.2.

버전 3.9부터 폐지됨: [`contextlib.AbstractAsyncContextManager`](https://docs.python.org/ko/3.12/library/contextlib.html#contextlib.AbstractAsyncContextManager "contextlib.AbstractAsyncContextManager") now supports subscripting (`[]`). See [**PEP 585**](https://peps.python.org/pep-0585/) and [제네릭 에일리어스 형](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias).

## Deprecation Timeline of Major Features[](https://docs.python.org/ko/3.12/library/typing.html#deprecation-timeline-of-major-features "Link to this heading")

Certain features in `typing` are deprecated and may be removed in a future version of Python. The following table summarizes major deprecations for your convenience. This is subject to change, and not all deprecations are listed.

|Feature|Deprecated in|Projected removal|PEP/issue|
|---|---|---|---|
|`typing.io` and `typing.re` submodules|3.8|3.13|[bpo-38291](https://bugs.python.org/issue?@action=redirect&bpo=38291)|
|`typing` versions of standard collections|3.9|Undecided (see [Deprecated aliases](https://docs.python.org/ko/3.12/library/typing.html#deprecated-aliases) for more information)|[**PEP 585**](https://peps.python.org/pep-0585/)|
|[`typing.ByteString`](https://docs.python.org/ko/3.12/library/typing.html#typing.ByteString "typing.ByteString")|3.9|3.14|[gh-91896](https://github.com/python/cpython/issues/91896)|
|[`typing.Text`](https://docs.python.org/ko/3.12/library/typing.html#typing.Text "typing.Text")|3.11|Undecided|[gh-92332](https://github.com/python/cpython/issues/92332)|
|[`typing.Hashable`](https://docs.python.org/ko/3.12/library/typing.html#typing.Hashable "typing.Hashable") and [`typing.Sized`](https://docs.python.org/ko/3.12/library/typing.html#typing.Sized "typing.Sized")|3.12|Undecided|[gh-94309](https://github.com/python/cpython/issues/94309)|
|[`typing.TypeAlias`](https://docs.python.org/ko/3.12/library/typing.html#typing.TypeAlias "typing.TypeAlias")|3.12|Undecided|[**PEP 695**](https://peps.python.org/pep-0695/)|

---

## 예제

## 참조

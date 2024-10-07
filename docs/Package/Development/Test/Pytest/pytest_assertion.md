---
title: "[Pytest] 단언 (Assertion)"
excerpt: 
categories:
  - Pytest
tags:
  - Python
  - Python-Library
  - Test
  - Python-pytest
  - Pytest-assertion
last_modified_at: 2024-04-11T15:10:56+09:00
link: https://docs.pytest.org/en/stable/how-to/assert.html
상위 항목: "[[pytest_home|파이테스트 (Pytest)]]"
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

---

## assert 문으로 단언하기 (Asserting with the `assert` statement)
- `pytest`는 Python 테스트에서 기대값과 실제 값을 검증하기 위해 표준 Python `assert`를 사용할 수 있게 해줍니다. 예를 들어, 다음과 같이 작성할 수 있습니다:

```python
# test_assert1.py의 내용
def f():
    return 3

def test_function():
    assert f() == 4
```

이는 함수가 특정 값을 반환하는지 단언합니다. 이 단언이 실패하면 함수 호출의 반환 값을 볼 수 있습니다:

```sh
$ pytest test_assert1.py
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-8.x.y, pluggy-1.x.y
rootdir: /home/sweet/project
collected 1 item

test_assert1.py F                                                    [100%]

================================= FAILURES =================================
______________________________ test_function _______________________________

    def test_function():
>       assert f() == 4
E       assert 3 == 4
E        +  where 3 = f()

test_assert1.py:6: AssertionError
========================= short test summary info ==========================
FAILED test_assert1.py::test_function - assert 3 == 4
============================ 1 failed in 0.12s =============================
```

- `pytest`는 호출, 속성, 비교, 이항 및 단항 연산자를 포함한 가장 일반적인 하위 표현식의 값을 보여주는 기능을 지원합니다. ([pytest를 사용한 Python 실패 보고서 데모](https://docs.pytest.org/en/stable/example/reportingdemo.html#tbreportdemo) 참조). 이를 통해 내성 정보를 잃지 않으면서 관용적인 Python 구조를 보일러플레이트 코드 없이 사용할 수 있습니다.

다음과 같이 단언과 함께 메시지가 지정된 경우:

```python
assert a % 2 == 0, "값이 홀수입니다. 짝수여야 합니다."
```

이는 트레이스백에서 단언 내성과 함께 출력됩니다.

- 단언 내성에 대한 자세한 내용은 [단언 내성 세부 정보](https://docs.pytest.org/en/stable/how-to/assert.html#assert-details)를 참조하세요.

## 예상되는 예외에 대한 단언 (Assertions about expected exceptions)

- 예외 발생에 대한 단언을 작성하려면 다음과 같이 컨텍스트 매니저로 [`pytest.raises()`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.raises "pytest.raises")를 사용할 수 있습니다:

```python
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

- 실제 예외 정보에 접근해야 하는 경우 다음과 같이 사용할 수 있습니다:

```python
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:

        def f():
            f()

        f()
    assert "maximum recursion" in str(excinfo.value)
```

- `excinfo`는 실제 발생한 예외를 감싸는 [`ExceptionInfo`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.ExceptionInfo "pytest.ExceptionInfo") 인스턴스입니다. 주요 관심 속성은 `.type`, `.value`, `.traceback`입니다.
- `pytest.raises`는 예외 타입이나 그 하위 클래스와 일치한다는 점에 유의하세요(표준 `except` 문과 유사). 코드 블록이 정확한 예외 타입을 발생시키는지 확인하려면 명시적으로 확인해야 합니다:

```python
def test_foo_not_implemented():
    def foo():
        raise NotImplementedError

    with pytest.raises(RuntimeError) as excinfo:
        foo()
    assert excinfo.type is RuntimeError
```

- 함수가 [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "(Python v3.12에서)")를 발생시키더라도 [`pytest.raises()`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.raises "pytest.raises") 호출은 성공합니다. 왜냐하면 [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "(Python v3.12에서)")가 [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "(Python v3.12에서)")의 하위 클래스이기 때문입니다. 그러나 이어지는 `assert` 문에서 문제를 잡아낼 것입니다.

### 예외 메시지 매칭 (Matching exception messages)

- 예외의 문자열 표현에 대해 정규 표현식이 일치하는지 테스트하기 위해 컨텍스트 매니저에 `match` 키워드 매개변수를 전달할 수 있습니다(`unittest`의 `TestCase.assertRaisesRegex` 메서드와 유사):

```python
import pytest

def myfunc():
    raise ValueError("Exception 123 raised")

def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()
```

> [!NOTE]
> - `match` 매개변수는 [`re.search()`](https://docs.python.org/3/library/re.html#re.search "(Python v3.12에서)") 함수와 일치하므로 위의 예에서 `match='123'`도 작동했을 것입니다.
> - `match` 매개변수는 또한 [PEP-678](https://peps.python.org/pep-0678/) `__notes__`에 대해서도 일치합니다.
> 

### 예외 그룹 매칭 (Matching exception groups)

- [`ExceptionGroup`](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "(Python v3.12에서)")의 일부로 반환된 예외를 테스트하기 위해 [`excinfo.group_contains()`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.ExceptionInfo.group_contains "pytest.ExceptionInfo.group_contains") 메서드를 사용할 수도 있습니다:

```python
def test_exception_in_group():
    with pytest.raises(ExceptionGroup) as excinfo:
        raise ExceptionGroup(
            "Group message",
            [
                RuntimeError("Exception 123 raised"),
            ],
        )
    assert excinfo.group_contains(RuntimeError, match=r".* 123 .*")
    assert not excinfo.group_contains(TypeError)
```

선택적 `match` 키워드 매개변수는 [`pytest.raises()`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.raises "pytest.raises")와 동일한 방식으로 작동합니다.

- 기본적으로 `group_contains()`는 중첩된 `ExceptionGroup` 인스턴스의 모든 수준에서 일치하는 예외를 재귀적으로 검색합니다. 특정 수준에서만 예외를 일치시키려면 `depth` 키워드 매개변수를 지정할 수 있습니다. 최상위 `ExceptionGroup`에 직접 포함된 예외는 `depth=1`과 일치합니다.

```python
def test_exception_in_group_at_given_depth():
    with pytest.raises(ExceptionGroup) as excinfo:
        raise ExceptionGroup(
            "Group message",
            [
                RuntimeError(),
                ExceptionGroup(
                    "Nested group",
                    [
                        TypeError(),
                    ],
                ),
            ],
        )
    assert excinfo.group_contains(RuntimeError, depth=1)
    assert excinfo.group_contains(TypeError, depth=2)
    assert not excinfo.group_contains(RuntimeError, depth=2)
    assert not excinfo.group_contains(TypeError, depth=1)
```

> [!NOTE] 대체 형식 (레거시) (Alternate form (legacy))
> - 실행될 함수를 `*args`와 `**kwargs`와 함께 전달하는 대체 형식이 있습니다. [`pytest.raises()`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.raises "pytest.raises")는 인자와 함께 함수를 실행하고 주어진 예외가 발생하는지 단언합니다:
> 
> ```python
> def func(x):
>     if x <= 0:
>         raise ValueError("x는 0보다 커야 합니다")
> 
> pytest.raises(ValueError, func, x=-1)
> ```
> 
> - 리포터는 예외가 없거나 잘못된 예외와 같은 실패 시 도움이 되는 출력을 제공합니다.
> - 이 형식은 Python 언어에 `with` 문이 추가되기 전에 개발된 원래의 [`pytest.raises()`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.raises "pytest.raises") API였습니다. 오늘날 이 형식은 거의 사용되지 않으며, 컨텍스트 매니저 형식(`with` 사용)이 더 읽기 쉽다고 여겨집니다. 그럼에도 불구하고 이 형식은 완전히 지원되며 어떤 식으로도 더 이상 사용되지 않습니다.

### xfail 마크와 pytest.raises (xfail mark and pytest.raises)
- [pytest.mark.xfail](https://docs.pytest.org/en/stable/reference/reference.html#pytest-mark-xfail-ref)에 `raises` 인자를 지정하여 테스트가 단순히 예외를 발생시키는 것보다 더 구체적인 방식으로 실패하는지 확인할 수도 있습니다:

```python
def f():
    raise IndexError()

@pytest.mark.xfail(raises=IndexError)
def test_f():
    f()
```

이는 테스트가 `IndexError` 또는 그 하위 클래스를 발생시켜 실패하는 경우에만 "xfail"됩니다.

- `raises` 매개변수와 함께 [pytest.mark.xfail](https://docs.pytest.org/en/stable/reference/reference.html#pytest-mark-xfail-ref)을 사용하는 것은 수정되지 않은 버그를 문서화하거나(테스트가 "해야 할" 일을 설명하는 경우) 의존성의 버그를 문서화하는 데 더 적합할 수 있습니다.
- [`pytest.raises()`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.raises "pytest.raises")를 사용하는 것은 대부분의 경우 자신의 코드가 의도적으로 발생시키는 예외를 테스트하는 데 더 적합할 수 있습니다.

## 예상되는 경고에 대한 단언 (Assertions about expected warnings)

- [pytest.warns](https://docs.pytest.org/en/stable/how-to/capture-warnings.html#warns)를 사용하여 코드가 특정 경고를 발생시키는지 확인할 수 있습니다.

## 상황에 맞는 비교 활용하기 (Making use of context-sensitive comparisons)

- `pytest`는 비교를 만났을 때 상황에 맞는 정보를 제공하는 풍부한 지원을 제공합니다. 예를 들어:

```python
# test_assert2.py의 내용
def test_set_comparison():
    set1 = set("1308")
    set2 = set("8035")
    assert set1 == set2
```

이 모듈을 실행하면:

```sh
$ pytest test_assert2.py
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-8.x.y, pluggy-1.x.y
rootdir: /home/sweet/project
collected 1 item

test_assert2.py F                                                    [100%]

================================= FAILURES =================================
___________________________ test_set_comparison ____________________________

    def test_set_comparison():
        set1 = set("1308")
        set2 = set("8035")
>       assert set1 == set2
E       AssertionError: assert {'0', '1', '3', '8'} == {'0', '3', '5', '8'}
E
E         Extra items in the left set:
E         '1'
E         Extra items in the right set:
E         '5'
E         Use -v to get more diff

test_assert2.py:4: AssertionError
========================= short test summary info ==========================
FAILED test_assert2.py::test_set_comparison - AssertionError: assert {'0'…
============================ 1 failed in 0.12s =============================
```

여러 경우에 대해 특별한 비교가 이루어집니다:

- 긴 문자열 비교: 컨텍스트 차이가 표시됩니다
- 긴 시퀀스 비교: 첫 번째 실패 인덱스
- 딕셔너리 비교: 다른 항목

더 많은 예시는 [보고 데모](https://docs.pytest.org/en/stable/example/reportingdemo.html#tbreportdemo)를 참조하세요.

## 실패한 단언에 대한 자체 설명 정의하기 (Defining your own explanation for failed assertions)

- `pytest_assertrepr_compare` 훅을 구현하여 자체적인 상세 설명을 추가할 수 있습니다.

> [!NOTE] `pytest_assertrepr_compare(_config_, _op_, _left_, _right_)`
> 
> - 실패한 assert 표현식의 비교에 대한 설명을 반환합니다.
> - 사용자 정의 설명이 없는 경우 None을 반환하고, 그렇지 않으면 문자열 리스트를 반환합니다. 문자열은 줄바꿈으로 결합되지만 문자열 내의 모든 줄바꿈은 이스케이프 처리됩니다. 첫 번째 줄을 제외한 모든 줄은 약간 들여쓰기됩니다. 첫 번째 줄은 요약이 되도록 의도되었습니다.
> 
> 매개변수:
> - **config** ([_Config_](https://docs.pytest.org/en/stable/reference/reference.html#pytest.Config "pytest.Config")) – pytest 설정 객체.
> - **op** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")) – 연산자, 예: `"=="`, `"!="`, `"not in"`.
> - **left** ([_object_](https://docs.python.org/3/library/functions.html#object "(in Python v3.12)")) – 왼쪽 피연산자.
> - **right** ([_object_](https://docs.python.org/3/library/functions.html#object "(in Python v3.12)")) – 오른쪽 피연산자.
> 

> [!NOTE] conftest 플러그인에서의 사용 (Use in conftest plugins)
> - 모든 conftest 파일에서 이 훅을 구현할 수 있습니다. 주어진 항목에 대해 해당 항목의 디렉토리와 상위 디렉토리에 있는 conftest 파일만 참조됩니다.g

예를 들어 [conftest.py](https://docs.pytest.org/en/stable/reference/fixtures.html#conftest-py) 파일에 다음 훅을 추가하여 `Foo` 객체에 대한 대체 설명을 제공할 수 있습니다:

```python
# conftest.py의 내용
from test_foocompare import Foo

def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return [
            "Foo 인스턴스 비교:",
            f"   vals: {left.val} != {right.val}",
        ]
```

이제 다음과 같은 테스트 모듈이 주어졌을 때:

```python
# test_foocompare.py의 내용
class Foo:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val

def test_compare():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f2
```

- 테스트 모듈을 실행하고 conftest 파일에 정의된 사용자 정의 출력을 얻을 수 있습니다:

```sh
$ pytest -q test_foocompare.py
F                                                                    [100%]
================================= FAILURES =================================
_______________________________ test_compare _______________________________

    def test_compare():
        f1 = Foo(1)
        f2 = Foo(2)
>       assert f1 == f2
E       assert Foo 인스턴스 비교:
E            vals: 1 != 2

test_foocompare.py:12: AssertionError
========================= short test summary info ==========================
FAILED test_foocompare.py::test_compare - assert Foo 인스턴스 비교:
1 failed in 0.12s
```

## 단언 내부 조사 세부 사항 (Assertion introspection details)
- 실패한 단언에 대한 세부 정보 보고는 실행되기 전에 assert 문을 다시 작성함으로써 이루어집니다. 다시 작성된 assert 문은 단언 실패 메시지에 내부 조사 정보를 넣습니다. `pytest`는 테스트 수집 프로세스에 의해 직접 발견된 테스트 모듈만 다시 작성하므로, **테스트 모듈 자체가 아닌 지원 모듈의 assert는 다시 작성되지 않습니다**.
- 임포트된 모듈에 대해 수동으로 단언 다시 작성을 활성화하려면 임포트하기 전에 [register_assert_rewrite](https://docs.pytest.org/en/stable/how-to/writing_plugins.html#assertion-rewriting)를 호출하면 됩니다(루트 `conftest.py`가 이를 수행하기에 좋은 장소입니다).
- 자세한 내용은 Benjamin Peterson이 작성한 [pytest의 새로운 단언 다시 작성의 무대 뒤](http://pybites.blogspot.com/2011/07/behind-scenes-of-pytests-new-assertion.html)를 참조하세요.

### 단언 다시 작성은 파일을 디스크에 캐시합니다 (Assertion rewriting caches files on disk)

- `pytest`는 다시 작성된 모듈을 캐싱을 위해 디스크에 다시 씁니다. 이 동작을 비활성화할 수 있습니다(예: 파일을 많이 이동하는 프로젝트에서 오래된 `.pyc` 파일을 남기지 않기 위해). `conftest.py` 파일의 맨 위에 다음을 추가하면 됩니다:

```python
import sys

sys.dont_write_bytecode = True
```

단언 내부 조사의 이점은 여전히 얻을 수 있으며, 유일한 변경점은 `.pyc` 파일이 디스크에 캐시되지 않는다는 것입니다.
- 또한, 새로운 `.pyc` 파일을 쓸 수 없는 경우(예: 읽기 전용 파일 시스템이나 zip 파일) 다시 작성은 조용히 캐싱을 건너뜁니다.

### 단언 다시 작성 비활성화하기 (Disabling assert rewriting)

- `pytest`는 새로운 `pyc` 파일을 작성하기 위해 임포트 훅을 사용하여 임포트 시 테스트 모듈을 다시 작성합니다. 대부분의 경우 이는 투명하게 작동합니다. 그러나 임포트 기능을 직접 다루고 있다면 임포트 훅이 방해할 수 있습니다. 이 경우 두 가지 옵션이 있습니다:
	- 특정 모듈의 다시 작성을 비활성화하려면 해당 모듈의 docstring에 `PYTEST_DONT_REWRITE` 문자열을 추가합니다.
	- 모든 모듈의 다시 작성을 비활성화하려면 `--assert=plain`을 사용합니다.


---
## 참조
[Pytest Plugin List - pytest documentation](https://docs.pytest.org/en/stable/reference/plugin_list.html#plugin-list)
---
title: "[Pytest] 픽스처 (Fixtures)"
excerpt: 
categories:
  - Pytest
tags:
  - Python
  - Python-Library
  - Test
  - Python-pytest
  - Pytest-fixture
last_modified_at: 2024-04-11T15:10:56+09:00
link: https://docs.pytest.org/en/stable/how-to/assert.html
상위 항목: "[[pytest_home|파이테스트 (Pytest)]]"
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

---
- pytest fixture는 명시적이고 모듈화되며 확장 가능하도록 설계되었습니다.

## fixture란 무엇인가 (What fixtures are)

- 테스트에서 fixture는 테스트를 위한 정의된, 신뢰할 수 있고 일관된 컨텍스트를 제공합니다. 여기에는 환경(예: 알려진 매개변수로 구성된 데이터베이스) 또는 콘텐츠(예: 데이터셋)가 포함될 수 있습니다.
- Fixture는 테스트의 _준비_ 단계를 구성하는 단계와 데이터를 정의합니다([테스트의 구조](https://docs.pytest.org/en/stable/explanation/anatomy.html#test-anatomy) 참조). pytest에서 이들은 이 목적을 수행하는 함수로 정의됩니다. 또한 테스트의 _실행_ 단계를 정의하는 데 사용될 수 있습니다. 이는 더 복잡한 테스트를 설계하는 강력한 기술입니다.
- fixture에 의해 설정된 서비스, 상태 또는 기타 운영 환경은 인수를 통해 테스트 함수에서 접근합니다. 테스트 함수가 사용하는 각 fixture에 대해 일반적으로 테스트 함수 정의에 (fixture 이름을 따서 지은) 매개변수가 있습니다.
- 우리는 [`@pytest.fixture`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.fixture "pytest.fixture") 데코레이터를 사용하여 특정 함수가 fixture임을 pytest에 알릴 수 있습니다. 다음은 pytest의 fixture가 어떻게 생겼는지 보여주는 간단한 예시입니다:

```python
import pytest

class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

@pytest.fixture
def my_fruit():
    return Fruit("apple")

@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]

def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket
```

- 테스트가 단일 fixture로 제한될 필요는 없습니다. 원하는 만큼 많은 fixture에 의존할 수 있으며, fixture도 다른 fixture를 사용할 수 있습니다. 이는 pytest의 fixture 시스템이 정말 빛을 발하는 부분입니다.

## xUnit 스타일의 설정/해제 함수에 대한 개선 (Improvements over xUnit-style setup/teardown functions)
- pytest fixture는 클래식한 xUnit 스타일의 설정/해제 함수에 비해 극적인 개선을 제공합니다:
	- fixture는 명시적인 이름을 가지며 테스트 함수, 모듈, 클래스 또는 전체 프로젝트에서 사용을 선언함으로써 활성화됩니다.
	- fixture는 모듈 방식으로 구현되며, 각 fixture 이름은 다른 fixture를 사용할 수 있는 _fixture 함수_ 를 트리거합니다.
	- fixture 관리는 간단한 단위 테스트에서 복잡한 기능 테스트까지 확장되어, 구성 및 컴포넌트 옵션에 따라 fixture와 테스트를 매개변수화하거나 함수, 클래스, 모듈 또는 전체 테스트 세션 범위에서 fixture를 재사용할 수 있습니다.
	- 해체 로직은 사용된 fixture 수에 관계없이 쉽고 안전하게 관리될 수 있으며, 오류를 수동으로 주의 깊게 처리하거나 정리 단계의 순서를 미세하게 관리할 필요가 없습니다.
- 또한, pytest는 계속해서 [xunit 스타일 설정을 구현하는 방법](https://docs.pytest.org/en/stable/how-to/xunit_setup.html#xunitsetup)을 지원합니다. 선호하는 대로 두 스타일을 혼합하여 클래식 스타일에서 새로운 스타일로 점진적으로 이동할 수 있습니다. 또한 기존 [unittest.TestCase 스타일](https://docs.pytest.org/en/stable/how-to/unittest.html#unittest-testcase)에서 시작할 수도 있습니다.

## Fixture 오류 (Fixture errors)
- pytest는 주어진 테스트에 대한 모든 fixture를 선형 순서로 배치하여 어떤 fixture가 첫 번째, 두 번째, 세 번째 등으로 실행되는지 볼 수 있도록 최선을 다합니다. 하지만 이전 fixture에 문제가 있어 예외를 발생시키면 pytest는 해당 테스트에 대한 fixture 실행을 중지하고 테스트에 오류가 있다고 표시합니다.
- 테스트가 오류가 있다고 표시되면 테스트가 실패했다는 의미는 아닙니다. 단지 테스트가 의존하는 것 중 하나에 문제가 있어 테스트를 시도조차 할 수 없었다는 의미입니다.
- 이는 주어진 테스트에 대해 불필요한 의존성을 최대한 제거하는 것이 좋은 이유 중 하나입니다. 그렇게 하면 관련 없는 것의 문제로 인해 무엇이 문제가 있거나 없을 수 있는지에 대한 불완전한 그림을 갖게 되는 일이 없습니다. 다음은 설명을 돕기 위한 간단한 예시입니다:

```python
import pytest

@pytest.fixture
def order():
    return []

@pytest.fixture
def append_first(order):
    order.append(1)

@pytest.fixture
def append_second(order, append_first):
    order.extend([2])

@pytest.fixture(autouse=True)
def append_third(order, append_second):
    order += [3]

def test_order(order):
    assert order == [1, 2, 3]
```

- 만약 어떤 이유로 `order.append(1)`에 버그가 있어 예외를 발생시킨다면, `order.extend([2])` 또는 `order += [3]`에도 문제가 있는지 알 수 없을 것입니다. `append_first`가 예외를 던진 후에는 pytest가 `test_order`에 대해 더 이상 fixture를 실행하지 않을 것이며, `test_order` 자체를 실행하려고 시도조차 하지 않을 것입니다. 실행되었을 유일한 것들은 `order`와 `append_first`일 것입니다.

## 테스트 데이터 공유 (Sharing test data)
- 파일에서 테스트 데이터를 테스트에 사용할 수 있게 하려면, 테스트에서 사용할 이 데이터를 fixture에 로드하는 것이 좋은 방법입니다. 이는 pytest의 자동 캐싱 메커니즘을 활용합니다.
- 또 다른 좋은 접근 방식은 `tests` 폴더에 데이터 파일을 추가하는 것입니다. 테스트의 이 측면을 관리하는 데 도움이 되는 커뮤니티 플러그인도 있습니다. 예를 들어 [pytest-datadir](https://pypi.org/project/pytest-datadir)와 [pytest-datafiles](https://pypi.org/project/pytest-datafiles)가 있습니다.

## Fixture 정리에 대한 참고 사항 (A note about fixture cleanup)

- pytest는 [`SIGTERM`](https://docs.python.org/3/library/signal.html#signal.SIGTERM "(in Python v3.12)")과 `SIGQUIT` 신호에 대해 특별한 처리를 하지 않습니다([`SIGINT`](https://docs.python.org/3/library/signal.html#signal.SIGINT "(in Python v3.12)")는 [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "(in Python v3.12)")를 통해 Python 런타임에 의해 자연스럽게 처리됩니다). 따라서 Python 프로세스가 종료될 때(이러한 신호에 의해) 정리되는 것이 중요한 외부 리소스를 관리하는 fixture는 리소스를 누출할 수 있습니다.
- pytest가 fixture 정리를 수행하기 위해 이러한 신호를 처리하지 않는 이유는 신호 핸들러가 전역적이며, 이를 변경하면 실행 중인 코드에 간섭할 수 있기 때문입니다.
- 귀하의 스위트의 fixture가 이러한 시나리오에서 종료에 대해 특별한 주의가 필요한 경우, 가능한 해결 방법에 대해 이슈 트래커의 [이 댓글](https://github.com/pytest-dev/pytest/issues/5243#issuecomment-491522595)을 참조하세요.


## 픽스처 "요청하기" (Requesting fixtures)
- 기본적으로 테스트 함수는 필요한 픽스처를 인자로 선언하여 요청합니다.
- pytest가 테스트를 실행할 때, 해당 테스트 함수의 시그니처에 있는 매개변수를 살펴보고 동일한 이름을 가진 픽스처를 찾습니다. pytest가 이를 찾으면 해당 픽스처를 실행하고, 반환된 객체(있는 경우)를 캡처한 다음, 이 객체들을 테스트 함수의 인자로 전달합니다.

> [!example]
> ```python
> import pytest
> 
> class Fruit:
>     def __init__(self, name):
>         self.name = name
>         self.cubed = False
> 
>     def cube(self):
>         self.cubed = True
> 
> class FruitSalad:
>     def __init__(self, *fruit_bowl):
>         self.fruit = fruit_bowl
>         self._cube_fruit()
> 
>     def _cube_fruit(self):
>         for fruit in self.fruit:
>             fruit.cube()
> 
> # Arrange
> @pytest.fixture
> def fruit_bowl():
>     return [Fruit("apple"), Fruit("banana")]
> 
> def test_fruit_salad(fruit_bowl):
>     # Act
>     fruit_salad = FruitSalad(*fruit_bowl)
> 
>     # Assert
>     assert all(fruit.cubed for fruit in fruit_salad.fruit)
> ```
> 
> - 이 예시에서 `test_fruit_salad`는 `fruit_bowl`을 "**요청**"합니다(즉, `def test_fruit_salad(fruit_bowl):`). pytest가 이를 확인하면 `fruit_bowl` 픽스처 함수를 실행하고 반환된 객체를 `test_fruit_salad`의 `fruit_bowl` 인자로 전달합니다.
> - 이를 수동으로 수행한다면 대략 다음과 같을 것입니다:
> 
> ```python
> def fruit_bowl():
>     return [Fruit("apple"), Fruit("banana")]
> 
> def test_fruit_salad(fruit_bowl):
>     # Act
>     fruit_salad = FruitSalad(*fruit_bowl)
> 
>     # Assert
>     assert all(fruit.cubed for fruit in fruit_salad.fruit)
> 
> # Arrange
> bowl = fruit_bowl()
> test_fruit_salad(fruit_bowl=bowl)
> ```
> 

### 픽스처는 다른 픽스처를 **요청**할 수 있습니다 (Fixtures can **request** other fixtures)

- pytest의 가장 큰 강점 중 하나는 매우 유연한 픽스처 시스템입니다. 이를 통해 테스트에 대한 복잡한 요구사항을 더 간단하고 체계적인 함수로 축소할 수 있으며, 각 함수가 의존하는 것들만 설명하면 됩니다. 이에 대해서는 나중에 더 자세히 다루겠지만, 지금은 픽스처가 다른 픽스처를 어떻게 사용할 수 있는지 보여주는 간단한 예시를 들어보겠습니다:

```python
# contents of test_append.py
import pytest

# Arrange
@pytest.fixture
def first_entry():
    return "a"

# Arrange
@pytest.fixture
def order(first_entry):
    return [first_entry]

def test_string(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]
```

- 이 예시는 위의 예시와 동일하지만 거의 변경되지 않았습니다. pytest의 픽스처는 테스트와 마찬가지로 픽스처를 **요청**합니다. 테스트에 적용되는 모든 **요청** 규칙은 픽스처에도 동일하게 적용됩니다. 이 예시를 수동으로 수행한다면 다음과 같을 것입니다:

```python
def first_entry():
    return "a"

def order(first_entry):
    return [first_entry]

def test_string(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]

entry = first_entry()
the_list = order(first_entry=entry)
test_string(order=the_list)
```

### 픽스처는 재사용 가능합니다 (Fixtures are reusable)

- pytest의 픽스처 시스템을 강력하게 만드는 요소 중 하나는 일반적인 설정 단계를 정의하여 일반 함수처럼 반복해서 사용할 수 있다는 점입니다. 서로 다른 두 테스트가 같은 픽스처를 요청할 수 있으며, pytest는 각 테스트에 해당 픽스처의 결과를 개별적으로 제공합니다.
- 이는 테스트들이 서로 영향을 주지 않도록 하는 데 매우 유용합니다. 이 시스템을 사용하여 각 테스트가 새로운 데이터 세트를 받고 깨끗한 상태에서 시작하여 일관되고 반복 가능한 결과를 제공할 수 있도록 할 수 있습니다.
- 다음은 이것이 어떻게 유용할 수 있는지 보여주는 예시입니다:

```python
# contents of test_append.py
import pytest

# Arrange
@pytest.fixture
def first_entry():
    return "a"

# Arrange
@pytest.fixture
def order(first_entry):
    return [first_entry]

def test_string(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]

def test_int(order):
    # Act
    order.append(2)

    # Assert
    assert order == ["a", 2]
```

- 여기서 각 테스트는 `list` 객체의 고유한 복사본을 받게 되며, 이는 `order` 픽스처가 두 번 실행된다는 것을 의미합니다(`first_entry` 픽스처에 대해서도 마찬가지입니다). 이를 수동으로 수행한다면 다음과 같을 것입니다:

```python
def first_entry():
    return "a"

def order(first_entry):
    return [first_entry]

def test_string(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "b"]

def test_int(order):
    # Act
    order.append(2)

    # Assert
    assert order == ["a", 2]

entry = first_entry()
the_list = order(first_entry=entry)
test_string(order=the_list)

entry = first_entry()
the_list = order(first_entry=entry)
test_int(order=the_list)
```

### 테스트/픽스처는 한 번에 여러 픽스처를 **요청**할 수 있습니다 (A test/fixture can **request** more than one fixture at a time)

- 테스트와 픽스처는 한 번에 하나의 픽스처만 **요청**하는 것으로 제한되지 않습니다. 원하는 만큼 많은 픽스처를 요청할 수 있습니다. 다음은 이를 보여주는 또 다른 간단한 예시입니다:

```python
# contents of test_append.py
import pytest

# Arrange
@pytest.fixture
def first_entry():
    return "a"

# Arrange
@pytest.fixture
def second_entry():
    return 2

# Arrange
@pytest.fixture
def order(first_entry, second_entry):
    return [first_entry, second_entry]

# Arrange
@pytest.fixture
def expected_list():
    return ["a", 2, 3.0]

def test_string(order, expected_list):
    # Act
    order.append(3.0)

    # Assert
    assert order == expected_list
```

### 픽스처는 테스트당 여러 번 **요청**될 수 있습니다 (반환 값은 캐시됨) (Fixtures can be **requested** more than once per test (return values are cached))

- 픽스처는 같은 테스트 내에서 여러 번 **요청**될 수 있으며, pytest는 해당 테스트에 대해 이를 다시 실행하지 않습니다. 이는 의존적인 여러 픽스처에서 픽스처를 **요청**할 수 있고(심지어 테스트 자체에서도 다시), 이러한 픽스처가 한 번 이상 실행되지 않음을 의미합니다.

```python
# contents of test_append.py
import pytest

# Arrange
@pytest.fixture
def first_entry():
    return "a"

# Arrange
@pytest.fixture
def order():
    return []

# Act
@pytest.fixture
def append_first(order, first_entry):
    return order.append(first_entry)

def test_string_only(append_first, order, first_entry):
    # Assert
    assert order == [first_entry]
```

- 만약 **요청된** 픽스처가 테스트 중에 요청될 때마다 한 번씩 실행된다면, 이 테스트는 실패할 것입니다. `append_first`와 `test_string_only` 모두 `order`를 빈 리스트(즉, `[]`)로 볼 것이기 때문입니다. 하지만 `order`의 반환 값이 처음 호출된 후 캐시되었기 때문에(실행으로 인한 부작용과 함께), 테스트와 `append_first` 모두 같은 객체를 참조하고 있었고, 테스트는 `append_first`가 해당 객체에 미친 영향을 볼 수 있었습니다.

## 자동 사용 픽스처 (요청하지 않아도 되는 픽스처) (Autouse fixtures (fixtures you don't have to request))

- 때로는 모든 테스트가 의존할 것으로 알고 있는 픽스처(또는 여러 개의 픽스처)를 갖고 싶을 수 있습니다. "자동 사용" 픽스처는 모든 테스트가 자동으로 이를 **요청**하도록 만드는 편리한 방법입니다. 이는 많은 중복된 **요청**을 줄일 수 있고, 더 고급 픽스처 사용법도 제공할 수 있습니다(이에 대해서는 나중에 더 자세히 다루겠습니다).
- 픽스처의 데코레이터에 `autouse=True`를 전달하여 자동 사용 픽스처를 만들 수 있습니다. 다음은 이들이 어떻게 사용될 수 있는지 보여주는 간단한 예시입니다:

```python
# contents of test_append.py
import pytest

@pytest.fixture
def first_entry():
    return "a"

@pytest.fixture
def order(first_entry):
    return []

@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    return order.append(first_entry)

def test_string_only(order, first_entry):
    assert order == [first_entry]

def test_string_and_int(order, first_entry):
    order.append(2)
    assert order == [first_entry, 2]
```

- 이 예시에서 `append_first` 픽스처는 자동 사용 픽스처입니다. 자동으로 실행되기 때문에 두 테스트 모두 이 픽스처의 영향을 받습니다. 비록 어느 테스트도 이를 **요청**하지 않았지만 말입니다. 그렇다고 해서 **요청**할 수 없다는 뜻은 아닙니다. 단지 필수가 아니라는 의미입니다.

## 범위: 클래스, 모듈, 패키지 또는 세션 간 fixture 공유

- 네트워크 액세스가 필요한 fixture는 연결성에 의존하며 일반적으로 생성하는 데 시간이 많이 걸립니다. 이전 예제를 확장하여 [`@pytest.fixture`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.fixture "pytest.fixture") 호출에 `scope="module"` 매개변수를 추가하여 기존 SMTP 서버에 대한 연결을 생성하는 `smtp_connection` fixture 함수가 테스트 _모듈_ 당 한 번만 호출되도록 할 수 있습니다(기본값은 테스트 _함수_ 당 한 번 호출). 따라서 테스트 모듈의 여러 테스트 함수는 각각 동일한 `smtp_connection` fixture 인스턴스를 받아 시간을 절약합니다. `scope`에 가능한 값은 `function`, `class`, `module`, `package` 또는 `session`입니다.
- 다음 예제는 fixture 함수를 별도의 `conftest.py` 파일에 넣어 디렉토리의 여러 테스트 모듈의 테스트가 fixture 함수에 액세스할 수 있도록 합니다:

```python
# content of conftest.py
import smtplib

import pytest

@pytest.fixture(scope="module")
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
```

```python
# content of test_module.py

def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    assert 0  # 데모 목적

def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    assert response == 250
    assert 0  # 데모 목적
```

- 여기서 `test_ehlo`는 `smtp_connection` fixture 값이 필요합니다. pytest는 [`@pytest.fixture`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.fixture "pytest.fixture")로 표시된 `smtp_connection` fixture 함수를 발견하고 호출합니다. 테스트 실행은 다음과 같습니다:

```sh
$ pytest test_module.py
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-8.x.y, pluggy-1.x.y
rootdir: /home/sweet/project
collected 2 items

test_module.py FF                                                    [100%]

================================= FAILURES =================================
________________________________ test_ehlo _________________________________

smtp_connection = <smtplib.SMTP object at 0xdeadbeef0001>

    def test_ehlo(smtp_connection):
        response, msg = smtp_connection.ehlo()
        assert response == 250
        assert b"smtp.gmail.com" in msg
>       assert 0  # 데모 목적
E       assert 0

test_module.py:7: AssertionError
________________________________ test_noop _________________________________

smtp_connection = <smtplib.SMTP object at 0xdeadbeef0001>

    def test_noop(smtp_connection):
        response, msg = smtp_connection.noop()
        assert response == 250
>       assert 0  # 데모 목적
E       assert 0

test_module.py:13: AssertionError
========================= short test summary info ==========================
FAILED test_module.py::test_ehlo - assert 0
FAILED test_module.py::test_noop - assert 0
============================ 2 failed in 0.12s =============================
```

- 두 개의 `assert 0`가 실패하는 것을 볼 수 있으며, 더 중요한 것은 pytest가 추적에 들어오는 인수 값을 보여주기 때문에 **정확히 동일한** `smtp_connection` 객체가 두 테스트 함수에 전달되었음을 볼 수 있습니다. 결과적으로 `smtp_connection`을 사용하는 두 테스트 함수는 동일한 인스턴스를 재사용하기 때문에 하나의 테스트만큼 빠르게 실행됩니다.
- 세션 범위의 `smtp_connection` 인스턴스를 갖기로 결정한 경우 다음과 같이 간단히 선언할 수 있습니다:

```python
@pytest.fixture(scope="session")
def smtp_connection():
    # 반환된 fixture 값은 이를 요청하는 
    # 모든 테스트에서 공유됩니다
    …
```

### Fixture 범위
- Fixture는 테스트에서 처음 요청될 때 생성되며 `scope`에 따라 파괴됩니다:
  - `function`: 기본 범위로, fixture는 테스트 종료 시 파괴됩니다.
  - `class`: fixture는 클래스의 마지막 테스트 종료 시 파괴됩니다.
  - `module`: fixture는 모듈의 마지막 테스트 종료 시 파괴됩니다.
  - `package`: fixture는 fixture가 정의된 패키지의 마지막 테스트 종료 시 파괴되며, 여기에는 하위 패키지와 하위 디렉토리가 포함됩니다.
  - `session`: fixture는 테스트 세션 종료 시 파괴됩니다.

> Pytest는 한 번에 하나의 fixture 인스턴스만 캐시하므로, 매개변수화된 fixture를 사용할 때 pytest는 주어진 범위에서 fixture를 두 번 이상 호출할 수 있습니다.

### 동적 범위

- 일부 경우에는 코드를 변경하지 않고 fixture의 범위를 변경하고 싶을 수 있습니다. 이를 위해 `scope`에 호출 가능한 객체를 전달합니다. 이 호출 가능한 객체는 유효한 범위를 가진 문자열을 반환해야 하며 fixture 정의 중에 한 번만 실행됩니다. 이는 `fixture_name`(문자열)과 `config`(구성 객체)라는 두 개의 키워드 인수와 함께 호출됩니다.
- 이는 설정에 시간이 필요한 fixture를 다룰 때 특히 유용할 수 있습니다(예: Docker 컨테이너 생성). 명령줄 인수를 사용하여 다른 환경에 대해 생성된 컨테이너의 범위를 제어할 수 있습니다. 아래 예제를 참조하세요.

```python
def determine_scope(fixture_name, config):
    if config.getoption("--keep-containers", None):
        return "session"
    return "function"

@pytest.fixture(scope=determine_scope)
def docker_container():
    yield spawn_container()
```

## 정리/청소 (일명 Fixture 마무리)

- 테스트를 실행할 때 다른 테스트에 영향을 주지 않도록 정리하고 싶을 것입니다(또한 시스템을 부풀리는 테스트 데이터를 남기지 않도록). pytest의 fixture는 매우 유용한 정리 시스템을 제공하여 각 fixture가 자체적으로 정리하는 데 필요한 특정 단계를 정의할 수 있습니다. 이 시스템은 두 가지 방법으로 활용할 수 있습니다.

### 1. `yield` fixture (권장)
- "Yield" fixture는 `return` 대신 `yield`를 사용합니다. 이러한 fixture를 사용하면 다른 fixture와 마찬가지로 일부 코드를 실행하고 요청하는 fixture/테스트에 객체를 다시 전달할 수 있습니다. 유일한 차이점은 다음과 같습니다:

1. `return`이 `yield`로 교체됩니다.
2. 해당 fixture에 대한 정리 코드는 `yield` _이후에_ 배치됩니다.

- pytest가 fixture의 선형 순서를 파악하면 각 fixture를 반환하거나 yield할 때까지 실행한 다음 목록의 다음 fixture로 이동하여 동일한 작업을 수행합니다.
- 테스트가 완료되면 pytest는 fixture 목록을 _역순으로_ 다시 내려가면서 yield한 각 fixture를 가져와 `yield` 문 _이후에_ 있는 코드를 실행합니다.
- 간단한 예로 다음과 같은 기본 이메일 모듈을 고려해 보겠습니다:

```python
# content of emaillib.py
class MailAdminClient:
    def create_user(self):
        return MailUser()

    def delete_user(self, user):
        # 일부 정리 수행
        pass

class MailUser:
    def __init__(self):
        self.inbox = []

    def send_email(self, email, other):
        other.inbox.append(email)

    def clear_mailbox(self):
        self.inbox.clear()

class Email:
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body
```

- 한 사용자가 다른 사용자에게 이메일을 보내는 것을 테스트하고 싶다고 가정해 보겠습니다. 먼저 각 사용자를 만든 다음 한 사용자에서 다른 사용자로 이메일을 보내고 마지막으로 다른 사용자가 받은 편지함에 해당 메시지를 받았는지 확인해야 합니다. 테스트 실행 후 정리하려면 사용자를 삭제하기 전에 다른 사용자의 사서함을 비워야 할 가능성이 높습니다. 그렇지 않으면 시스템에서 불평할 수 있습니다.
- 다음과 같이 보일 수 있습니다:

```python
# content of test_emaillib.py
from emaillib import Email, MailAdminClient

import pytest

@pytest.fixture
def mail_admin():
    return MailAdminClient()

@pytest.fixture
def sending_user(mail_admin):
    user = mail_admin.create_user()
    yield user
    mail_admin.delete_user(user)

@pytest.fixture
def receiving_user(mail_admin):
    user = mail_admin.create_user()
    yield user
    user.clear_mailbox()
    mail_admin.delete_user(user)

def test_email_received(sending_user, receiving_user):
    email = Email(subject="안녕하세요!", body="어떻게 지내세요?")
    sending_user.send_email(email, receiving_user)
    assert email in receiving_user.inbox
```

- `receiving_user`가 설정 중 마지막으로 실행되는 fixture이기 때문에 정리 중에 첫 번째로 실행됩니다.
- 정리 측면에서 순서가 올바르더라도 안전한 정리를 보장하지 않을 위험이 있습니다. 이는 [안전한 정리](https://docs.pytest.org/en/stable/how-to/fixtures.html#safe-teardowns)에서 좀 더 자세히 다룹니다.

```sh
$ pytest -q test_emaillib.py
.                                                                    [100%]
1 passed in 0.12s
```

#### yield fixture에 대한 오류 처리
- yield fixture가 yield 전에 예외를 발생시키면 pytest는 해당 yield fixture의 `yield` 문 이후의 정리 코드를 실행하려고 시도하지 않습니다. 그러나 해당 테스트에 대해 이미 성공적으로 실행된 모든 fixture에 대해 pytest는 여전히 정상적으로 정리하려고 시도합니다.

### 2. 직접 파이널라이저 추가하기 (Adding finalizers directly)
- yield 픽스처가 더 깔끔하고 간단한 옵션으로 간주되지만, 다른 선택지도 있습니다. 바로 테스트의 [request-context](https://docs.pytest.org/en/stable/how-to/fixtures.html#request-context) 객체에 직접 "파이널라이저" 함수를 추가하는 것입니다. 이는 yield 픽스처와 비슷한 결과를 가져오지만, 약간 더 장황한 방식이 필요합니다.
- 이 접근 방식을 사용하려면, 정리 코드를 추가해야 하는 픽스처에서 [request-context](https://docs.pytest.org/en/stable/how-to/fixtures.html#request-context) 객체를 요청해야 합니다(다른 픽스처를 요청하는 것처럼). 그런 다음 정리 코드가 포함된 호출 가능한 객체를 해당 객체의 `addfinalizer` 메서드에 전달합니다.
- 그러나 주의해야 할 점이 있습니다. pytest는 파이널라이저가 추가되면 해당 픽스처가 파이널라이저를 추가한 후 예외를 발생시키더라도 파이널라이저를 실행합니다. 따라서 불필요할 때 파이널라이저 코드를 실행하지 않도록 하려면, 픽스처가 정리가 필요한 작업을 수행한 후에만 파이널라이저를 추가해야 합니다.
- 다음은 `addfinalizer` 메서드를 사용한 이전 예제의 모습입니다:

```python
# test_emaillib.py의 내용
from emaillib import Email, MailAdminClient

import pytest

@pytest.fixture
def mail_admin():
    return MailAdminClient()

@pytest.fixture
def sending_user(mail_admin):
    user = mail_admin.create_user()
    yield user
    mail_admin.delete_user(user)

@pytest.fixture
def receiving_user(mail_admin, request):
    user = mail_admin.create_user()

    def delete_user():
        mail_admin.delete_user(user)

    request.addfinalizer(delete_user)
    return user

@pytest.fixture
def email(sending_user, receiving_user, request):
    _email = Email(subject="Hey!", body="How's it going?")
    sending_user.send_email(_email, receiving_user)

    def empty_mailbox():
        receiving_user.clear_mailbox()

    request.addfinalizer(empty_mailbox)
    return _email

def test_email_received(receiving_user, email):
    assert email in receiving_user.inbox
```

- yield 픽스처보다 약간 길고 복잡하지만, 급할 때 사용할 수 있는 몇 가지 미묘한 차이점을 제공합니다.

```sh
$ pytest -q test_emaillib.py
.                                                                    [100%]
1 passed in 0.12s
```

#### 파이널라이저 순서에 대한 참고 (Note on finalizer order)

- 파이널라이저는 후입선출 순서로 실행됩니다. yield 픽스처의 경우, 가장 먼저 실행되는 정리 코드는 가장 오른쪽 픽스처, 즉 마지막 테스트 매개변수에서 나옵니다.

```python
# test_finalizers.py의 내용
import pytest

def test_bar(fix_w_yield1, fix_w_yield2):
    print("test_bar")

@pytest.fixture
def fix_w_yield1():
    yield
    print("after_yield_1")

@pytest.fixture
def fix_w_yield2():
    yield
    print("after_yield_2")
```

```sh
$ pytest -s test_finalizers.py
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-8.x.y, pluggy-1.x.y
rootdir: /home/sweet/project
collected 1 item

test_finalizers.py test_bar
.after_yield_2
after_yield_1

============================ 1 passed in 0.12s =============================
```

- 파이널라이저의 경우, 가장 먼저 실행되는 픽스처는 `request.addfinalizer`에 대한 마지막 호출입니다.

```python
# test_finalizers.py의 내용
from functools import partial
import pytest

@pytest.fixture
def fix_w_finalizers(request):
    request.addfinalizer(partial(print, "finalizer_2"))
    request.addfinalizer(partial(print, "finalizer_1"))

def test_bar(fix_w_finalizers):
    print("test_bar")
```

```sh
$ pytest -s test_finalizers.py
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-8.x.y, pluggy-1.x.y
rootdir: /home/sweet/project
collected 1 item

test_finalizers.py test_bar
.finalizer_1
finalizer_2

============================ 1 passed in 0.12s =============================
```

- 이는 yield 픽스처가 내부적으로 `addfinalizer`를 사용하기 때문입니다: 픽스처가 실행될 때, `addfinalizer`는 제너레이터를 재개하는 함수를 등록하고, 이는 차례로 정리 코드를 호출합니다.

## 안전한 정리 (Safe teardowns)

- pytest의 픽스처 시스템은 매우 강력하지만, 여전히 컴퓨터에 의해 실행되므로 우리가 던지는 모든 것을 안전하게 정리하는 방법을 스스로 파악할 수 없습니다. 주의하지 않으면 잘못된 위치에서 오류가 발생하여 테스트의 일부가 남겨질 수 있으며, 이는 빠르게 추가적인 문제를 일으킬 수 있습니다.
- 예를 들어, 다음 테스트를 고려해보세요 (위의 메일 예제를 기반으로 함):

```python
# test_emaillib.py의 내용
from emaillib import Email, MailAdminClient

import pytest

@pytest.fixture
def setup():
    mail_admin = MailAdminClient()
    sending_user = mail_admin.create_user()
    receiving_user = mail_admin.create_user()
    email = Email(subject="Hey!", body="How's it going?")
    sending_user.send_email(email, receiving_user)
    yield receiving_user, email
    receiving_user.clear_mailbox()
    mail_admin.delete_user(sending_user)
    mail_admin.delete_user(receiving_user)

def test_email_received(setup):
    receiving_user, email = setup
    assert email in receiving_user.inbox
```

- 이 버전은 훨씬 더 간결하지만, 읽기가 더 어렵고 픽스처 이름이 매우 설명적이지 않으며 픽스처들을 쉽게 재사용할 수 없습니다.
- 또한 더 심각한 문제가 있는데, 설정 단계 중 어느 하나라도 예외가 발생하면 정리 코드가 전혀 실행되지 않는다는 것입니다.
- `addfinalizer` 메서드를 yield 픽스처 대신 사용하는 것이 한 가지 옵션일 수 있지만, 이는 매우 복잡해지고 유지 관리가 어려워질 수 있습니다 (그리고 더 이상 간결하지 않을 것입니다).

```sh
$ pytest -q test_emaillib.py
.                                                                    [100%]
1 passed in 0.12s
```

### 안전한 픽스처 구조 (Safe fixture structure)

- 가장 안전하고 간단한 픽스처 구조는 각 픽스처가 하나의 상태 변경 작업만 수행하도록 제한하고, 이를 정리 코드와 함께 묶는 것입니다. [위의 이메일 예제](https://docs.pytest.org/en/stable/how-to/fixtures.html#yield-fixtures)에서 보여준 것처럼 말입니다.
- 상태 변경 작업이 실패하면서도 여전히 상태를 수정할 수 있는 가능성은 무시할 만합니다. 대부분의 이러한 작업은 [트랜잭션](https://en.wikipedia.org/wiki/Transaction_processing) 기반이기 때문입니다 (적어도 상태가 남겨질 수 있는 테스트 수준에서는). 따라서 성공적인 상태 변경 작업이 확실히 정리되도록, 이를 별도의 픽스처 함수로 이동하고 다른 잠재적으로 실패할 수 있는 상태 변경 작업과 분리한다면, 우리의 테스트는 테스트 환경을 원래 상태로 되돌릴 가능성이 가장 높아집니다.
- 예를 들어, 로그인 페이지가 있는 웹사이트가 있고 사용자를 생성할 수 있는 관리자 API에 접근할 수 있다고 가정해 봅시다. 우리의 테스트를 위해 다음을 수행하고자 합니다:

1. 관리자 API를 통해 사용자 생성
2. Selenium을 사용하여 브라우저 실행
3. 사이트의 로그인 페이지로 이동
4. 생성한 사용자로 로그인
5. 랜딩 페이지의 헤더에 사용자의 이름이 있는지 확인

- 우리는 시스템에 그 사용자를 남겨두거나 브라우저 세션을 계속 실행 상태로 두고 싶지 않을 것입니다. 따라서 이러한 것들을 생성하는 픽스처들이 스스로 정리하도록 해야 합니다.
- 다음은 이것이 어떻게 보일 수 있는지를 보여줍니다:

> 이 예제에서는 특정 픽스처들(즉, `base_url`과 `admin_credentials`)이 다른 곳에 존재한다고 가정합니다. 따라서 지금은 이들이 존재한다고 가정하고, 우리는 그저 그것들을 보고 있지 않은 것입니다.

```python
from uuid import uuid4
from urllib.parse import urljoin

from selenium.webdriver import Chrome
import pytest

from src.utils.pages import LoginPage, LandingPage
from src.utils import AdminApiClient
from src.utils.data_types import User

@pytest.fixture
def admin_client(base_url, admin_credentials):
    return AdminApiClient(base_url, **admin_credentials)

@pytest.fixture
def user(admin_client):
    _user = User(name="Susan", username=f"testuser-{uuid4()}", password="P4$$word")
    admin_client.create_user(_user)
    yield _user
    admin_client.delete_user(_user)

@pytest.fixture
def driver():
    _driver = Chrome()
    yield _driver
    _driver.quit()

@pytest.fixture
def login(driver, base_url, user):
    driver.get(urljoin(base_url, "/login"))
    page = LoginPage(driver)
    page.login(user)

@pytest.fixture
def landing_page(driver, login):
    return LandingPage(driver)

def test_name_on_landing_page_after_login(landing_page, user):
    assert landing_page.header == f"Welcome, {user.name}!"
```

- 의존성이 배치된 방식으로 인해 `user` 픽스처가 `driver` 픽스처보다 먼저 실행될지 불분명합니다. 하지만 그것은 괜찮습니다. 왜냐하면 이들은 원자적 작업이고, 따라서 테스트의 이벤트 순서는 여전히 [선형화 가능](https://en.wikipedia.org/wiki/Linearizability)하기 때문입니다. 하지만 중요한 것은, 어느 것이 먼저 실행되든 상관없이, 하나가 예외를 발생시키고 다른 하나는 그렇지 않았을 경우 어느 것도 뒤에 아무것도 남기지 않는다는 것입니다. `driver`가 `user`보다 먼저 실행되고 `user`가 예외를 발생시키면, 드라이버는 여전히 종료되고 사용자는 결코 생성되지 않았을 것입니다. 그리고 `driver`가 예외를 발생시켰다면, 드라이버는 결코 시작되지 않았을 것이고 사용자는 결코 생성되지 않았을 것입니다.


## 여러 `assert` 문을 안전하게 실행하기 (Running multiple `assert` statements safely)
- 때로는 모든 설정을 마친 후 여러 개의 assert를 실행하고 싶을 수 있습니다. 더 복잡한 시스템에서는 하나의 동작이 여러 가지 행동을 유발할 수 있기 때문에 이는 합리적입니다. pytest는 이를 처리하는 편리한 방법을 제공하며, 지금까지 다룬 내용의 상당 부분을 결합합니다.
- 필요한 것은 더 큰 범위로 단계를 올리고, **act** 단계를 autouse 픽스처로 정의한 다음, 모든 픽스처가 그 상위 범위를 대상으로 하도록 하는 것뿐입니다.
- [위의 예시](https://docs.pytest.org/en/stable/how-to/fixtures.html#safe-fixture-structure)를 가져와 조금 수정해 보겠습니다. 헤더의 환영 메시지를 확인하는 것 외에도 로그아웃 버튼과 사용자 프로필 링크를 확인하고 싶다고 가정해 보겠습니다.
- 모든 단계를 반복하지 않고도 여러 assert를 실행할 수 있도록 이를 구조화하는 방법을 살펴보겠습니다.

> 이 예시에서는 특정 픽스처(예: `base_url`과 `admin_credentials`)가 다른 곳에 존재한다고 가정합니다. 지금은 이들이 존재한다고 가정하고, 우리는 그것들을 보고 있지 않다고 생각하겠습니다.

```python
# contents of tests/end_to_end/test_login.py
from uuid import uuid4
from urllib.parse import urljoin

from selenium.webdriver import Chrome
import pytest

from src.utils.pages import LoginPage, LandingPage
from src.utils import AdminApiClient
from src.utils.data_types import User

@pytest.fixture(scope="class")
def admin_client(base_url, admin_credentials):
    return AdminApiClient(base_url, **admin_credentials)

@pytest.fixture(scope="class")
def user(admin_client):
    _user = User(name="Susan", username=f"testuser-{uuid4()}", password="P4$$word")
    admin_client.create_user(_user)
    yield _user
    admin_client.delete_user(_user)

@pytest.fixture(scope="class")
def driver():
    _driver = Chrome()
    yield _driver
    _driver.quit()

@pytest.fixture(scope="class")
def landing_page(driver, login):
    return LandingPage(driver)

class TestLandingPageSuccess:
    @pytest.fixture(scope="class", autouse=True)
    def login(self, driver, base_url, user):
        driver.get(urljoin(base_url, "/login"))
        page = LoginPage(driver)
        page.login(user)

    def test_name_in_header(self, landing_page, user):
        assert landing_page.header == f"Welcome, {user.name}!"

    def test_sign_out_button(self, landing_page):
        assert landing_page.sign_out_button.is_displayed()

    def test_profile_link(self, landing_page, user):
        profile_href = urljoin(base_url, f"/profile?id={user.profile_id}")
        assert landing_page.profile_link.get_attribute("href") == profile_href
```

- 메서드 시그니처에서 `self`를 참조하는 것은 형식적인 것일 뿐입니다. `unittest.TestCase` 프레임워크에서처럼 실제 테스트 클래스에 상태가 연결되어 있지 않습니다. 모든 것은 pytest 픽스처 시스템에 의해 관리됩니다.
- 각 메서드는 순서에 대해 걱정하지 않고 실제로 필요한 픽스처만 요청하면 됩니다. 이는 **act** 픽스처가 autouse 픽스처이고, 다른 모든 픽스처가 그 전에 실행되도록 했기 때문입니다. 더 이상 상태 변경이 일어나지 않으므로, 테스트는 다른 테스트의 발을 밟을 위험 없이 상태를 변경하지 않는 쿼리를 원하는 만큼 자유롭게 수행할 수 있습니다.
- `login` 픽스처도 클래스 내에 정의되어 있습니다. 이는 모듈의 다른 모든 테스트가 성공적인 로그인을 기대하지 않을 수 있고, **act**가 다른 테스트 클래스에 대해 조금 다르게 처리될 필요가 있기 때문입니다. 예를 들어, 잘못된 자격 증명을 제출하는 것에 대한 다른 테스트 시나리오를 작성하고 싶다면, 다음과 같은 내용을 테스트 파일에 추가하여 처리할 수 있습니다:

```python
class TestLandingPageBadCredentials:
    @pytest.fixture(scope="class")
    def faux_user(self, user):
        _user = deepcopy(user)
        _user.password = "badpass"
        return _user

    def test_raises_bad_credentials_exception(self, login_page, faux_user):
        with pytest.raises(BadCredentialsException):
            login_page.login(faux_user)
```

## 픽스처는 요청하는 테스트 컨텍스트를 검사할 수 있습니다 (Fixtures can introspect the requesting test context)

- 픽스처 함수는 [`request`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.FixtureRequest "_pytest.fixtures.FixtureRequest") 객체를 받아 "요청하는" 테스트 함수, 클래스 또는 모듈 컨텍스트를 검사할 수 있습니다. 이전의 `smtp_connection` 픽스처 예제를 더 확장하여, 우리의 픽스처를 사용하는 테스트 모듈에서 선택적 서버 URL을 읽어보겠습니다:

```python
# content of conftest.py
import smtplib

import pytest

@pytest.fixture(scope="module")
def smtp_connection(request):
    server = getattr(request.module, "smtpserver", "smtp.gmail.com")
    smtp_connection = smtplib.SMTP(server, 587, timeout=5)
    yield smtp_connection
    print(f"finalizing {smtp_connection} ({server})")
    smtp_connection.close()
```

- 우리는 `request.module` 속성을 사용하여 테스트 모듈에서 선택적으로 `smtpserver` 속성을 얻습니다. 다시 실행해도 크게 변한 것은 없습니다:

```sh
$ pytest -s -q --tb=no test_module.py
FFfinalizing <smtplib.SMTP object at 0xdeadbeef0002> (smtp.gmail.com)

========================= short test summary info ==========================
FAILED test_module.py::test_ehlo - assert 0
FAILED test_module.py::test_noop - assert 0
2 failed in 0.12s
```

- 실제로 모듈 네임스페이스에서 서버 URL을 설정하는 또 다른 테스트 모듈을 빠르게 만들어 보겠습니다:

```python
# content of test_anothersmtp.py

smtpserver = "mail.python.org"  # will be read by smtp fixture

def test_showhelo(smtp_connection):
    assert 0, smtp_connection.helo()
```

실행 결과:

```sh
$ pytest -qq --tb=short test_anothersmtp.py
F                                                                    [100%]
================================= FAILURES =================================
______________________________ test_showhelo _______________________________
test_anothersmtp.py:6: in test_showhelo
    assert 0, smtp_connection.helo()
E   AssertionError: (250, b'mail.python.org')
E   assert 0
------------------------- Captured stdout teardown -------------------------
finalizing <smtplib.SMTP object at 0xdeadbeef0003> (mail.python.org)
========================= short test summary info ==========================
FAILED test_anothersmtp.py::test_showhelo - AssertionError: (250, b'mail….
```

짜잔! `smtp_connection` 픽스처 함수가 모듈 네임스페이스에서 우리의 메일 서버 이름을 가져왔습니다.

## 마커를 사용하여 픽스처에 데이터 전달하기 (Using markers to pass data to fixtures)

- [`request`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.FixtureRequest "_pytest.fixtures.FixtureRequest") 객체를 사용하여 픽스처는 테스트 함수에 적용된 마커에도 접근할 수 있습니다. 이는 테스트에서 픽스처로 데이터를 전달하는 데 유용할 수 있습니다:

```python
import pytest

@pytest.fixture
def fixt(request):
    marker = request.node.get_closest_marker("fixt_data")
    if marker is None:
        # Handle missing marker in some way…
        data = None
    else:
        data = marker.args[0]

    # Do something with the data
    return data

@pytest.mark.fixt_data(42)
def test_fixt(fixt):
    assert fixt == 42
```

## 팩토리를 픽스처로 사용하기 (Factories as fixtures)

- "팩토리를 픽스처로" 패턴은 단일 테스트에서 픽스처의 결과가 여러 번 필요한 상황에서 도움이 될 수 있습니다. 데이터를 직접 반환하는 대신, 픽스처는 데이터를 생성하는 함수를 반환합니다. 이 함수는 테스트에서 여러 번 호출될 수 있습니다.
- 필요에 따라 팩토리에 매개변수를 둘 수 있습니다:

```python
@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {"name": name, "orders": []}

    return _make_customer_record

def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")
```
팩토리에 의해 생성된 데이터를 관리해야 하는 경우, 픽스처가 이를 처리할 수 있습니다:

```python
@pytest.fixture
def make_customer_record():
    created_records = []

    def _make_customer_record(name):
        record = models.Customer(name=name, orders=[])
        created_records.append(record)
        return record

    yield _make_customer_record

    for record in created_records:
        record.destroy()

def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")
```


## 픽스처 매개변수화 (Parametrizing fixtures)

- 픽스처 함수를 매개변수화할 수 있으며, 이 경우 여러 번 호출되어 의존적인 테스트 세트, 즉 이 픽스처에 의존하는 테스트들을 각각 실행합니다. 테스트 함수는 일반적으로 재실행되는 것을 인식할 필요가 없습니다. 픽스처 매개변수화는 여러 가지 방식으로 구성할 수 있는 컴포넌트에 대해 포괄적인 기능 테스트를 작성하는 데 도움이 됩니다.
- 이전 예제를 확장하여, 두 개의 `smtp_connection` 픽스처 인스턴스를 생성하도록 픽스처에 플래그를 지정할 수 있습니다. 이로 인해 해당 픽스처를 사용하는 모든 테스트가 두 번 실행됩니다. 픽스처 함수는 특별한 [`request`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.FixtureRequest "pytest.FixtureRequest") 객체를 통해 각 매개변수에 접근할 수 있습니다:

```python
# content of conftest.py
import smtplib

import pytest

@pytest.fixture(scope="module", params=["smtp.gmail.com", "mail.python.org"])
def smtp_connection(request):
    smtp_connection = smtplib.SMTP(request.param, 587, timeout=5)
    yield smtp_connection
    print(f"finalizing {smtp_connection}")
    smtp_connection.close()
```

- 주요 변경 사항은 [`@pytest.fixture`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.fixture "pytest.fixture")에 `params`를 선언한 것입니다. 이는 픽스처 함수가 실행되고 `request.param`을 통해 값에 접근할 수 있는 값 목록입니다. 테스트 함수 코드를 변경할 필요는 없습니다. 그럼 다시 실행해 봅시다:

```sh
$ pytest -q test_module.py
FFFF                                                                 [100%]
================================= FAILURES =================================
________________________ test_ehlo[smtp.gmail.com] _________________________

smtp_connection = <smtplib.SMTP object at 0xdeadbeef0004>

    def test_ehlo(smtp_connection):
        response, msg = smtp_connection.ehlo()
        assert response == 250
        assert b"smtp.gmail.com" in msg
>       assert 0  # for demo purposes
E       assert 0

test_module.py:7: AssertionError
________________________ test_noop[smtp.gmail.com] _________________________

smtp_connection = <smtplib.SMTP object at 0xdeadbeef0004>

    def test_noop(smtp_connection):
        response, msg = smtp_connection.noop()
        assert response == 250
>       assert 0  # for demo purposes
E       assert 0

test_module.py:13: AssertionError
________________________ test_ehlo[mail.python.org] ________________________

smtp_connection = <smtplib.SMTP object at 0xdeadbeef0005>

    def test_ehlo(smtp_connection):
        response, msg = smtp_connection.ehlo()
        assert response == 250
>       assert b"smtp.gmail.com" in msg
E       AssertionError: assert b'smtp.gmail.com' in b'mail.python.org\nPIPELINING\nSIZE 51200000\nETRN\nSTARTTLS\nAUTH DIGEST-MD5 NTLM CRAM-MD5\nENHANCEDSTATUSCODES\n8BITMIME\nDSN\nSMTPUTF8\nCHUNKING'

test_module.py:6: AssertionError
-------------------------- Captured stdout setup ---------------------------
finalizing <smtplib.SMTP object at 0xdeadbeef0004>
________________________ test_noop[mail.python.org] ________________________

smtp_connection = <smtplib.SMTP object at 0xdeadbeef0005>

    def test_noop(smtp_connection):
        response, msg = smtp_connection.noop()
        assert response == 250
>       assert 0  # for demo purposes
E       assert 0

test_module.py:13: AssertionError
------------------------- Captured stdout teardown -------------------------
finalizing <smtplib.SMTP object at 0xdeadbeef0005>
========================= short test summary info ==========================
FAILED test_module.py::test_ehlo[smtp.gmail.com] - assert 0
FAILED test_module.py::test_noop[smtp.gmail.com] - assert 0
FAILED test_module.py::test_ehlo[mail.python.org] - AssertionError: asser…
FAILED test_module.py::test_noop[mail.python.org] - assert 0
4 failed in 0.12s
```

- 두 개의 테스트 함수가 각각 두 번씩, 서로 다른 `smtp_connection` 인스턴스에 대해 실행된 것을 볼 수 있습니다. 또한 `mail.python.org` 연결에서는 두 번째 테스트가 `test_ehlo`에서 실패하는데, 이는 예상했던 것과 다른 서버 문자열이 도착했기 때문입니다.
- pytest는 매개변수화된 픽스처의 각 픽스처 값에 대한 테스트 ID 문자열을 생성합니다. 예를 들어, 위의 예제에서 `test_ehlo[smtp.gmail.com]`과 `test_ehlo[mail.python.org]`입니다. 이러한 ID는 `-k`와 함께 사용하여 실행할 특정 케이스를 선택할 수 있으며, 실패한 경우 특정 케이스를 식별하는 데도 사용됩니다. pytest를 `--collect-only`와 함께 실행하면 생성된 ID를 볼 수 있습니다.
- 숫자, 문자열, 불리언 및 `None`은 테스트 ID에 일반적인 문자열 표현이 사용됩니다. 다른 객체의 경우, pytest는 인수 이름을 기반으로 문자열을 만듭니다. `ids` 키워드 인수를 사용하여 특정 픽스처 값에 대한 테스트 ID에 사용되는 문자열을 사용자 정의할 수 있습니다:

```python
# content of test_ids.py
import pytest

@pytest.fixture(params=[0, 1], ids=["spam", "ham"])
def a(request):
    return request.param

def test_a(a):
    pass

def idfn(fixture_value):
    if fixture_value == 0:
        return "eggs"
    else:
        return None

@pytest.fixture(params=[0, 1], ids=idfn)
def b(request):
    return request.param

def test_b(b):
    pass
```

- 위의 예는 `ids`가 사용할 문자열 리스트이거나 픽스처 값으로 호출되어 사용할 문자열을 반환해야 하는 함수일 수 있음을 보여줍니다. 후자의 경우 함수가 `None`을 반환하면 pytest의 자동 생성 ID가 사용됩니다.
- 위의 테스트를 실행하면 다음과 같은 테스트 ID가 사용됩니다:

```sh
$ pytest --collect-only
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-8.x.y, pluggy-1.x.y
rootdir: /home/sweet/project
collected 12 items

<Dir fixtures.rst-223>
  <Module test_anothersmtp.py>
    <Function test_showhelo[smtp.gmail.com]>
    <Function test_showhelo[mail.python.org]>
  <Module test_emaillib.py>
    <Function test_email_received>
  <Module test_finalizers.py>
    <Function test_bar>
  <Module test_ids.py>
    <Function test_a[spam]>
    <Function test_a[ham]>
    <Function test_b[eggs]>
    <Function test_b[1]>
  <Module test_module.py>
    <Function test_ehlo[smtp.gmail.com]>
    <Function test_noop[smtp.gmail.com]>
    <Function test_ehlo[mail.python.org]>
    <Function test_noop[mail.python.org]>

======================= 12 tests collected in 0.12s ========================
```

## 매개변수화된 픽스처와 마크 사용하기 (Using marks with parametrized fixtures)

- [`pytest.param()`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.param "pytest.param")을 사용하여 [@pytest.mark.parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html#pytest-mark-parametrize)와 같은 방식으로 매개변수화된 픽스처의 값 세트에 마크를 적용할 수 있습니다.

예시:

```python
# content of test_fixture_marks.py
import pytest

@pytest.fixture(params=[0, 1, pytest.param(2, marks=pytest.mark.skip)])
def data_set(request):
    return request.param

def test_data(data_set):
    pass
```

이 테스트를 실행하면 값이 `2`인 `data_set`의 호출을 _건너뜁니다_:

```sh
$ pytest test_fixture_marks.py -v
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-8.x.y, pluggy-1.x.y -- $PYTHON_PREFIX/bin/python
cachedir: .pytest_cache
rootdir: /home/sweet/project
collecting … collected 3 items

test_fixture_marks.py::test_data[0] PASSED                           [ 33%]
test_fixture_marks.py::test_data[1] PASSED                           [ 66%]
test_fixture_marks.py::test_data[2] SKIPPED (unconditional skip)     [100%]

======================= 2 passed, 1 skipped in 0.12s =======================
```

## 모듈성: 픽스처 함수에서 픽스처 사용하기 (Modularity: using fixtures from a fixture function)

- 테스트 함수에서 픽스처를 사용하는 것 외에도, 픽스처 함수 자체가 다른 픽스처를 사용할 수 있습니다. 이는 픽스처의 모듈식 설계에 기여하며 프레임워크별 픽스처를 여러 프로젝트에서 재사용할 수 있게 합니다. 간단한 예로, 이전 예제를 확장하여 이미 정의된 `smtp_connection` 리소스를 넣을 `app` 객체를 인스턴스화할 수 있습니다:

```python
# content of test_appsetup.py

import pytest

class App:
    def __init__(self, smtp_connection):
        self.smtp_connection = smtp_connection

@pytest.fixture(scope="module")
def app(smtp_connection):
    return App(smtp_connection)

def test_smtp_connection_exists(app):
    assert app.smtp_connection
```

- 여기서 우리는 이전에 정의된 `smtp_connection` 픽스처를 받아 `App` 객체를 인스턴스화하는 `app` 픽스처를 선언합니다. 실행해 봅시다:

```sh
$ pytest -v test_appsetup.py
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-8.x.y, pluggy-1.x.y -- $PYTHON_PREFIX/bin/python
cachedir: .pytest_cache
rootdir: /home/sweet/project
collecting … collected 2 items

test_appsetup.py::test_smtp_connection_exists[smtp.gmail.com] PASSED [ 50%]
test_appsetup.py::test_smtp_connection_exists[mail.python.org] PASSED [100%]

============================ 2 passed in 0.12s =============================
```

- `smtp_connection`의 매개변수화로 인해 테스트는 두 개의 다른 `App` 인스턴스와 각각의 smtp 서버로 두 번 실행됩니다. pytest가 픽스처 의존성 그래프를 완전히 분석하기 때문에 `app` 픽스처가 `smtp_connection` 매개변수화를 인식할 필요가 없습니다.
- `app` 픽스처의 범위가 `module`이고 모듈 범위의 `smtp_connection` 픽스처를 사용한다는 점에 유의하세요. `smtp_connection`이 `session` 범위에서 캐시되었더라도 예제는 여전히 작동할 것입니다: 픽스처가 "더 넓은" 범위의 픽스처를 사용하는 것은 괜찮지만 그 반대는 의미 있는 방식으로 작동하지 않습니다. 세션 범위의 픽스처는 모듈 범위의 픽스처를 의미 있게 사용할 수 없습니다.

## 픽스처 인스턴스에 의한 테스트의 자동 그룹화 (Automatic grouping of tests by fixture instances)

- pytest는 테스트 실행 중 활성 픽스처의 수를 최소화합니다. 매개변수화된 픽스처가 있는 경우, 이를 사용하는 모든 테스트는 먼저 하나의 인스턴스로 실행된 다음 정리자(finalizers)가 호출되고 다음 픽스처 인스턴스가 생성됩니다. 이는 다른 이점들 중에서도 전역 상태를 생성하고 사용하는 애플리케이션의 테스트를 용이하게 합니다.
- 다음 예제는 두 개의 매개변수화된 픽스처를 사용하며, 그 중 하나는 모듈 단위로 범위가 지정되어 있고, 모든 함수는 설정/해제 흐름을 보여주기 위해 `print` 호출을 수행합니다:

```python
# test_module.py의 내용
import pytest

@pytest.fixture(scope="module", params=["mod1", "mod2"])
def modarg(request):
    param = request.param
    print("  SETUP modarg", param)
    yield param
    print("  TEARDOWN modarg", param)

@pytest.fixture(scope="function", params=[1, 2])
def otherarg(request):
    param = request.param
    print("  SETUP otherarg", param)
    yield param
    print("  TEARDOWN otherarg", param)

def test_0(otherarg):
    print("  RUN test0 with otherarg", otherarg)

def test_1(modarg):
    print("  RUN test1 with modarg", modarg)

def test_2(otherarg, modarg):
    print(f"  RUN test2 with otherarg {otherarg} and modarg {modarg}")
```

- verbose 모드로 테스트를 실행하고 print 출력을 살펴보겠습니다:

```sh
$ pytest -v -s test_module.py
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-8.x.y, pluggy-1.x.y -- $PYTHON_PREFIX/bin/python
cachedir: .pytest_cache
rootdir: /home/sweet/project
collecting … collected 8 items

test_module.py::test_0[1]   SETUP otherarg 1
  RUN test0 with otherarg 1
PASSED  TEARDOWN otherarg 1

test_module.py::test_0[2]   SETUP otherarg 2
  RUN test0 with otherarg 2
PASSED  TEARDOWN otherarg 2

test_module.py::test_1[mod1]   SETUP modarg mod1
  RUN test1 with modarg mod1
PASSED
test_module.py::test_2[mod1-1]   SETUP otherarg 1
  RUN test2 with otherarg 1 and modarg mod1
PASSED  TEARDOWN otherarg 1

test_module.py::test_2[mod1-2]   SETUP otherarg 2
  RUN test2 with otherarg 2 and modarg mod1
PASSED  TEARDOWN otherarg 2

test_module.py::test_1[mod2]   TEARDOWN modarg mod1
  SETUP modarg mod2
  RUN test1 with modarg mod2
PASSED
test_module.py::test_2[mod2-1]   SETUP otherarg 1
  RUN test2 with otherarg 1 and modarg mod2
PASSED  TEARDOWN otherarg 1

test_module.py::test_2[mod2-2]   SETUP otherarg 2
  RUN test2 with otherarg 2 and modarg mod2
PASSED  TEARDOWN otherarg 2
  TEARDOWN modarg mod2

============================ 8 passed in 0.12s =============================
```

- 매개변수화된 모듈 범위의 `modarg` 리소스가 가능한 한 적은 수의 "활성" 리소스를 가지도록 테스트 실행 순서를 결정했음을 볼 수 있습니다. `mod1` 매개변수화 리소스에 대한 정리자는 `mod2` 리소스가 설정되기 전에 실행되었습니다.
- 특히 test_0가 완전히 독립적이며 가장 먼저 완료됩니다. 그 다음 test_1이 `mod1`과 함께 실행되고, 그 다음 test_2가 `mod1`과 함께 실행되며, 그 다음 test_1이 `mod2`와 함께 실행되고 마지막으로 test_2가 `mod2`와 함께 실행됩니다.
- 함수 범위를 가진 `otherarg` 매개변수화 리소스는 이를 사용하는 모든 테스트 전에 설정되고 후에 해제되었습니다.

## `usefixtures`를 사용하여 클래스와 모듈에서 픽스처 사용하기 (Use fixtures in classes and modules with `usefixtures`)

- 때로는 테스트 함수가 픽스처 객체에 직접 접근할 필요가 없습니다. 예를 들어, 테스트는 현재 작업 디렉토리로 빈 디렉토리를 사용해야 하지만 구체적인 디렉토리에 대해서는 신경 쓰지 않을 수 있습니다. 다음은 표준 [`tempfile`](https://docs.python.org/3/library/tempfile.html#module-tempfile "(in Python v3.12)")과 pytest 픽스처를 사용하여 이를 달성하는 방법입니다. 픽스처의 생성을 `conftest.py` 파일로 분리합니다:

```python
# conftest.py의 내용

import os
import tempfile

import pytest

@pytest.fixture
def cleandir():
    with tempfile.TemporaryDirectory() as newpath:
        old_cwd = os.getcwd()
        os.chdir(newpath)
        yield
        os.chdir(old_cwd)
```

그리고 테스트 모듈에서 `usefixtures` 마커를 통해 그 사용을 선언합니다:

```python
# test_setenv.py의 내용
import os

import pytest

@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit:
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile", "w", encoding="utf-8") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
```

- `usefixtures` 마커로 인해, `cleandir` 픽스처는 각 테스트 메소드 실행에 필요하게 됩니다. 마치 각 메소드에 "cleandir" 함수 인자를 지정한 것과 같습니다. 실행하여 픽스처가 활성화되고 테스트가 통과하는지 확인해 봅시다:

```sh
$ pytest -q
..                                                                   [100%]
2 passed in 0.12s
```

- 다음과 같이 여러 픽스처를 지정할 수 있습니다:

```python
@pytest.mark.usefixtures("cleandir", "anotherfixture")
def test(): …
```

그리고 [`pytestmark`](https://docs.pytest.org/en/stable/reference/reference.html#globalvar-pytestmark)를 사용하여 테스트 모듈 수준에서 픽스처 사용을 지정할 수 있습니다:

```python
pytestmark = pytest.mark.usefixtures("cleandir")
```

- 프로젝트의 모든 테스트에 필요한 픽스처를 ini 파일에 넣는 것도 가능합니다:

```ini
# pytest.ini의 내용
[pytest]
usefixtures = cleandir
```

> [!warning]
> - 이 마커는 **픽스처 함수**에서는 효과가 없습니다. 예를 들어, 다음은 **예상대로 작동하지 않습니다**:
> 
> ```python
> @pytest.mark.usefixtures("my_other_fixture")
> @pytest.fixture
> def my_fixture_that_sadly_wont_use_my_other_fixture(): …
> ```
> 
> 이는 deprecated 경고를 생성하며, Pytest 8에서는 오류가 됩니다.

## 다양한 수준에서 픽스처 오버라이딩하기 (Overriding fixtures on various levels)

비교적 큰 테스트 스위트에서는 `global` 또는 `root` 픽스처를 `locally` 정의된 것으로 `override`해야 할 가능성이 높습니다. 이는 테스트 코드의 가독성과 유지 보수성을 유지하기 위함입니다.

### 폴더(conftest) 수준에서 픽스처 오버라이드하기 (Override a fixture on a folder (conftest) level)

테스트 파일 구조가 다음과 같다고 가정해 봅시다:

```python
tests/
    conftest.py
        # tests/conftest.py의 내용
        import pytest

        @pytest.fixture
        def username():
            return 'username'

    test_something.py
        # tests/test_something.py의 내용
        def test_username(username):
            assert username == 'username'

    subfolder/
        conftest.py
            # tests/subfolder/conftest.py의 내용
            import pytest

            @pytest.fixture
            def username(username):
                return 'overridden-' + username

        test_something_else.py
            # tests/subfolder/test_something_else.py의 내용
            def test_username(username):
                assert username == 'overridden-username'
```

보시다시피, 같은 이름의 픽스처가 특정 테스트 폴더 수준에서 오버라이드될 수 있습니다. `base` 또는 `super` 픽스처는 `overriding` 픽스처에서 쉽게 접근할 수 있습니다 - 위 예제에서 사용된 것처럼요.

### 테스트 모듈 수준에서 픽스처 오버라이드하기 (Override a fixture on a test module level)

테스트 파일 구조가 다음과 같다고 가정해 봅시다:

```python
tests/
    conftest.py
        # tests/conftest.py의 내용
        import pytest

        @pytest.fixture
        def username():
            return 'username'

    test_something.py
        # tests/test_something.py의 내용
        import pytest

        @pytest.fixture
        def username(username):
            return 'overridden-' + username

        def test_username(username):
            assert username == 'overridden-username'

    test_something_else.py
        # tests/test_something_else.py의 내용
        import pytest

        @pytest.fixture
        def username(username):
            return 'overridden-else-' + username

        def test_username(username):
            assert username == 'overridden-else-username'
```

위 예제에서, 같은 이름의 픽스처가 특정 테스트 모듈에 대해 오버라이드될 수 있습니다.

### 직접 테스트 매개변수화로 픽스처 오버라이드하기 (Override a fixture with direct test parametrization)

테스트 파일 구조가 다음과 같다고 가정해 봅시다:

```python
tests/
    conftest.py
        # tests/conftest.py의 내용
        import pytest

        @pytest.fixture
        def username():
            return 'username'

        @pytest.fixture
        def other_username(username):
            return 'other-' + username

    test_something.py
        # tests/test_something.py의 내용
        import pytest

        @pytest.mark.parametrize('username', ['directly-overridden-username'])
        def test_username(username):
            assert username == 'directly-overridden-username'

        @pytest.mark.parametrize('username', ['directly-overridden-username-other'])
        def test_username_other(other_username):
            assert other_username == 'other-directly-overridden-username-other'
```

위 예제에서, 픽스처 값은 테스트 매개변수 값에 의해 오버라이드됩니다. 테스트가 직접 사용하지 않더라도(함수 프로토타입에서 언급하지 않더라도) 이런 방식으로 픽스처의 값을 오버라이드할 수 있습니다.

다음은 요청하신 대로 번역한 내용입니다:

## 매개변수화된 픽스처를 매개변수화되지 않은 픽스처로 오버라이드하기와 그 반대의 경우 (Override a parametrized fixture with non-parametrized one and vice versa)

테스트 파일 구조가 다음과 같다고 가정해봅시다:

```python
tests/
    conftest.py
        # tests/conftest.py의 내용
        import pytest

        @pytest.fixture(params=['one', 'two', 'three'])
        def parametrized_username(request):
            return request.param

        @pytest.fixture
        def non_parametrized_username(request):
            return 'username'

    test_something.py
        # tests/test_something.py의 내용
        import pytest

        @pytest.fixture
        def parametrized_username():
            return 'overridden-username'

        @pytest.fixture(params=['one', 'two', 'three'])
        def non_parametrized_username(request):
            return request.param

        def test_username(parametrized_username):
            assert parametrized_username == 'overridden-username'

        def test_parametrized_username(non_parametrized_username):
            assert non_parametrized_username in ['one', 'two', 'three']

    test_something_else.py
        # tests/test_something_else.py의 내용
        def test_username(parametrized_username):
            assert parametrized_username in ['one', 'two', 'three']

        def test_username(non_parametrized_username):
            assert non_parametrized_username == 'username'
```

위의 예제에서 매개변수화된 픽스처는 매개변수화되지 않은 버전으로 오버라이드되고, 매개변수화되지 않은 픽스처는 특정 테스트 모듈에 대해 매개변수화된 버전으로 오버라이드됩니다. 이는 분명히 테스트 폴더 수준에서도 동일하게 적용됩니다.

## 다른 프로젝트의 픽스처 사용하기 (Using fixtures from other projects)

- 일반적으로 pytest 지원을 제공하는 프로젝트는 [진입점](https://docs.pytest.org/en/stable/how-to/writing_plugins.html#pip-installable-plugins)을 사용하므로, 해당 프로젝트를 환경에 설치하기만 하면 이러한 픽스처를 사용할 수 있게 됩니다.
- 진입점을 사용하지 않는 프로젝트의 픽스처를 사용하려는 경우, 최상위 `conftest.py` 파일에서 [`pytest_plugins`](https://docs.pytest.org/en/stable/reference/reference.html#globalvar-pytest_plugins)를 정의하여 해당 모듈을 플러그인으로 등록할 수 있습니다.
- `mylibrary.fixtures`에 일부 픽스처가 있고 이를 `app/tests` 디렉토리에서 재사용하고 싶다고 가정해 봅시다.
- 해야 할 일은 `app/tests/conftest.py`에서 해당 모듈을 가리키는 [`pytest_plugins`](https://docs.pytest.org/en/stable/reference/reference.html#globalvar-pytest_plugins)를 정의하는 것뿐입니다.

```sh
pytest_plugins = "mylibrary.fixtures"
```

- 이렇게 하면 `mylibrary.fixtures`가 플러그인으로 효과적으로 등록되어 모든 픽스처와 훅을 `app/tests`의 테스트에서 사용할 수 있게 됩니다.

> [!NOTE]
> - 때로 사용자들은 다른 프로젝트의 픽스처를 사용하기 위해 _가져오기_ 를 하지만, 이는 권장되지 않습니다: 모듈로 픽스처를 가져오면 pytest에서 해당 모듈에 _정의된_ 것으로 등록됩니다.
> - 이는 `pytest --help`에 여러 번 나타나는 등의 사소한 결과를 초래하지만, 향후 버전에서 이 동작이 변경되거나 작동을 멈출 수 있기 때문에 **권장되지 않습니다**.


---
## 참조
[Pytest Plugin List - pytest documentation](https://docs.pytest.org/en/stable/reference/plugin_list.html#plugin-list)



### [Fixtures reference](https://docs.pytest.org/en/stable/reference/fixtures.html#reference-fixtures)

#### 내장 픽스처 (Built-in fixtures)

- [Fixture](https://docs.pytest.org/en/stable/reference/reference.html#fixtures-api)는 [@pytest.fixture](https://docs.pytest.org/en/stable/reference/reference.html#pytest-fixture-api) 데코레이터를 사용하여 정의됩니다. Pytest에는 여러 유용한 내장 픽스처가 있습니다:

> [`capfd`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-capfd)
> 
> 파일 디스크립터 `1`과 `2`로의 출력을 텍스트로 캡처합니다.
> 
> [`capfdbinary`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-capfdbinary)
> 
> 파일 디스크립터 `1`과 `2`로의 출력을 바이트로 캡처합니다.
> 
> [`caplog`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-caplog)
> 
> 로깅을 제어하고 로그 항목에 접근합니다.
> 
> [`capsys`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-capsys)
> 
> `sys.stdout`과 `sys.stderr`로의 출력을 텍스트로 캡처합니다.
> 
> [`capsysbinary`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-capsysbinary)
> 
> `sys.stdout`과 `sys.stderr`로의 출력을 바이트로 캡처합니다.
> 
> [`cache`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-cache)
> 
> pytest 실행 간에 값을 저장하고 검색합니다.
> 
> [`doctest_namespace`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-doctest_namespace)
> 
> doctest 네임스페이스에 주입되는 딕셔너리를 제공합니다.
> 
> [`monkeypatch`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-monkeypatch)
> 
> 클래스, 함수, 딕셔너리, `os.environ` 및 기타 객체를 일시적으로 수정합니다.
> 
> [`pytestconfig`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-pytestconfig)
> 
> 구성 값, 플러그인 관리자 및 플러그인 훅에 대한 액세스를 제공합니다.
> 
> [`record_property`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-record_property)
> 
> 테스트에 추가 속성을 추가합니다.
> 
> [`record_testsuite_property`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-record_testsuite_property)
> 
> 테스트 스위트에 추가 속성을 추가합니다.
> 
> [`recwarn`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-recwarn)
> 
> 테스트 함수에서 발생한 경고를 기록합니다.
> 
> [`request`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-request)
> 
> 실행 중인 테스트 함수에 대한 정보를 제공합니다.
> 
> [`testdir`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-testdir)
> 
> pytest 플러그인을 실행하고 테스트하는 데 도움이 되는 임시 테스트 디렉터리를 제공합니다.
> 
> [`tmp_path`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-tmp_path)
> 
> 각 테스트 함수에 고유한 임시 디렉터리에 대한 [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.12)") 객체를 제공합니다.
> 
> [`tmp_path_factory`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-tmp_path_factory)
> 
> 세션 범위의 임시 디렉터리를 만들고 [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.12)") 객체를 반환합니다.
> 
> [`tmpdir`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-tmpdir)
> 
> 각 테스트 함수에 고유한 임시 디렉터리에 대한 [py.path.local](https://py.readthedocs.io/en/latest/path.html) 객체를 제공합니다; [`tmp_path`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-tmp_path)로 대체되었습니다.
> 
> [`tmpdir_factory`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-tmpdir_factory)
> 
> 세션 범위의 임시 디렉터리를 만들고 `py.path.local` 객체를 반환합니다; [`tmp_path_factory`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-tmp_path_factory)로 대체되었습니다.

#### 픽스처 가용성 (Fixture availability)

- 픽스처 가용성은 테스트의 관점에서 결정됩니다. 픽스처는 테스트가 그 픽스처가 정의된 범위 내에 있을 때만 요청할 수 있습니다. 픽스처가 클래스 내부에 정의되어 있다면, 해당 클래스 내부의 테스트만 그것을 요청할 수 있습니다. 하지만 픽스처가 모듈의 전역 범위에 정의되어 있다면, 클래스 내부에 정의된 테스트를 포함하여 해당 모듈의 모든 테스트가 그것을 요청할 수 있습니다.
- 마찬가지로, 테스트는 자동 사용(autouse) 픽스처가 정의된 동일한 범위에 있는 경우에만 해당 autouse 픽스처의 영향을 받을 수 있습니다 ([[#Autouse 픽스처는 해당 스코프 내에서 가장 먼저 실행됩니다 (Autouse fixtures are executed first within their scope)|Autouse fixtures are executed first within their scope]] 참조).
- 픽스처는 또한 정의된 위치에 관계없이 다른 모든 픽스처를 요청할 수 있습니다. 단, 테스트가 관련된 모든 픽스처를 볼 수 있어야 합니다.
- 예를 들어, 다음은 정의되지 않은 범위의 픽스처(`inner`)를 요청하는 픽스처(`outer`)가 있는 테스트 파일입니다:

```python
from __future__ import annotations

import pytest

@pytest.fixture
def order():
    return []

@pytest.fixture
def outer(order, inner):
    order.append("outer")

class TestOne:
    @pytest.fixture
    def inner(self, order):
        order.append("one")

    def test_order(self, order, outer):
        assert order == ["one", "outer"]

class TestTwo:
    @pytest.fixture
    def inner(self, order):
        order.append("two")

    def test_order(self, order, outer):
        assert order == ["two", "outer"]
```

테스트의 관점에서 볼 때, 그들은 의존하는 각 픽스처를 보는 데 문제가 없습니다:

![../_images/test_fixtures_request_different_scope.svg](https://docs.pytest.org/en/stable/_images/test_fixtures_request_different_scope.svg)

##### `conftest.py`: 여러 파일 간 fixture 공유 (conftest.py: sharing fixtures across multiple files)

- `conftest.py` 파일은 전체 디렉토리에 대한 fixture를 제공하는 수단 역할을 합니다. `conftest.py`에 정의된 fixture는 해당 패키지의 모든 테스트에서 가져올 필요 없이 사용할 수 있습니다(pytest가 자동으로 발견합니다).
- 테스트가 포함된 중첩된 여러 디렉토리/패키지를 가질 수 있으며, 각 디렉토리에는 고유한 fixture가 있는 자체 `conftest.py`가 있을 수 있어 상위 디렉토리의 `conftest.py` 파일이 제공하는 fixture에 추가됩니다.
- 예를 들어, 다음과 같은 테스트 파일 구조가 주어졌다고 가정해 봅시다:

```python
tests/
    __init__.py

    conftest.py
        # content of tests/conftest.py
        import pytest

        @pytest.fixture
        def order():
            return []

        @pytest.fixture
        def top(order, innermost):
            order.append("top")

    test_top.py
        # content of tests/test_top.py
        import pytest

        @pytest.fixture
        def innermost(order):
            order.append("innermost top")

        def test_order(order, top):
            assert order == ["innermost top", "top"]

    subpackage/
        __init__.py

        conftest.py
            # content of tests/subpackage/conftest.py
            import pytest

            @pytest.fixture
            def mid(order):
                order.append("mid subpackage")

        test_subpackage.py
            # content of tests/subpackage/test_subpackage.py
            import pytest

            @pytest.fixture
            def innermost(order, mid):
                order.append("innermost subpackage")

            def test_order(order, top):
                assert order == ["mid subpackage", "innermost subpackage", "top"]
```

스코프의 경계는 다음과 같이 시각화할 수 있습니다:

![../_images/fixture_availability.svg](https://docs.pytest.org/en/stable/_images/fixture_availability.svg)

- 디렉토리는 자체적인 일종의 스코프가 되어 해당 디렉토리의 `conftest.py` 파일에 정의된 fixture가 전체 스코프에서 사용 가능해집니다.
- 테스트는 fixture를 찾기 위해 위로 검색할 수 있지만(원 밖으로 나가기), 검색을 계속하기 위해 아래로 내려갈 수는 없습니다(원 안으로 들어가기). 따라서 `tests/subpackage/test_subpackage.py::test_order`는 `tests/subpackage/test_subpackage.py`에 정의된 `innermost` fixture를 찾을 수 있지만, `tests/test_top.py`에 정의된 것은 사용할 수 없습니다. 이는 그것을 찾기 위해 한 단계 아래로 내려가야 하기 때문입니다(원 안으로 들어가기).
- 테스트가 찾는 첫 번째 fixture가 사용되므로, 특정 스코프에 대해 fixture의 동작을 변경하거나 확장해야 하는 경우 [fixture를 재정의](https://docs.pytest.org/en/stable/how-to/fixtures.html#override-fixtures)할 수 있습니다.
- `conftest.py` 파일을 사용하여 [로컬 디렉토리별 플러그인](https://docs.pytest.org/en/stable/how-to/writing_plugins.html#conftest-py-plugins)을 구현할 수도 있습니다.

##### 서드파티 플러그인의 fixture (Fixtures from third-party plugins)
- 테스트에서 사용할 수 있는 fixture가 반드시 이 구조에 정의되어 있어야 하는 것은 아닙니다. 설치된 서드파티 플러그인에서도 제공될 수 있으며, 많은 pytest 플러그인이 이렇게 작동합니다. 이러한 플러그인이 설치되어 있는 한, 제공하는 fixture는 테스트 스위트 어디에서나 요청할 수 있습니다.
- 테스트 스위트의 구조 외부에서 제공되기 때문에, 서드파티 플러그인은 `conftest.py` 파일과 테스트 스위트의 디렉토리처럼 실제 스코프를 제공하지 않습니다. 결과적으로 pytest는 이전에 설명한 대로 스코프를 벗어나면서 fixture를 검색하다가 플러그인에 정의된 fixture를 _마지막에_ 찾게 됩니다.
- 예를 들어, 다음과 같은 파일 구조가 주어졌다고 가정해 봅시다:

```python
tests/
    __init__.py

    conftest.py
        # content of tests/conftest.py
        import pytest

        @pytest.fixture
        def order():
            return []

    subpackage/
        __init__.py

        conftest.py
            # content of tests/subpackage/conftest.py
            import pytest

            @pytest.fixture(autouse=True)
            def mid(order, b_fix):
                order.append("mid subpackage")

        test_subpackage.py
            # content of tests/subpackage/test_subpackage.py
            import pytest

            @pytest.fixture
            def inner(order, mid, a_fix):
                order.append("inner subpackage")

            def test_order(order, inner):
                assert order == ["b_fix", "mid subpackage", "a_fix", "inner subpackage"]
```

- `plugin_a`가 설치되어 있고 `a_fix` fixture를 제공하며, `plugin_b`가 설치되어 있고 `b_fix` fixture를 제공한다면, 테스트의 fixture 검색은 다음과 같이 보일 것입니다:

![../_images/fixture_availability_plugins.svg](https://docs.pytest.org/en/stable/_images/fixture_availability_plugins.svg)

- pytest는 `tests/` 내부의 스코프에서 먼저 `a_fix`와 `b_fix`를 검색한 후에만 플러그인에서 이들을 검색할 것입니다.

#### Fixture 인스턴스화 순서 (Fixture instantiation order)

- pytest가 테스트를 실행하려고 할 때, 어떤 fixture가 실행될지 알게 되면 실행 순서를 파악해야 합니다. 이를 위해 3가지 요소를 고려합니다:

1. 스코프
2. 의존성
3. autouse

- fixture나 테스트의 이름, 정의된 위치, 정의된 순서, fixture가 요청된 순서는 우연의 일치 이상으로 실행 순서에 영향을 미치지 않습니다. pytest는 이러한 우연의 일치가 실행마다 일관성을 유지하도록 노력하지만, 이는 의존해서는 안 되는 것입니다. 순서를 제어하려면 이 3가지 요소에 의존하고 의존성이 명확히 설정되어 있는지 확인하는 것이 가장 안전합니다.

##### 더 높은 스코프의 fixture가 먼저 실행됩니다 (Higher-scoped fixtures are executed first)

- fixture에 대한 함수 요청 내에서 더 높은 스코프(예: `session`)의 fixture가 더 낮은 스코프(예: `function` 또는 `class`)의 fixture보다 먼저 실행됩니다. 다음은 예시입니다:

```python
from __future__ import annotations

import pytest

@pytest.fixture(scope="session")
def order():
    return []

@pytest.fixture
def func(order):
    order.append("function")

@pytest.fixture(scope="class")
def cls(order):
    order.append("class")

@pytest.fixture(scope="module")
def mod(order):
    order.append("module")

@pytest.fixture(scope="package")
def pack(order):
    order.append("package")

@pytest.fixture(scope="session")
def sess(order):
    order.append("session")

class TestClass:
    def test_order(self, func, cls, mod, pack, sess, order):
        assert order == ["session", "package", "module", "class", "function"]
```

- 더 큰 스코프의 fixture가 먼저 실행되기 때문에 이 테스트는 통과합니다. 순서는 다음과 같이 나눠집니다:

![../_images/test_fixtures_order_scope.svg](https://docs.pytest.org/en/stable/_images/test_fixtures_order_scope.svg)

##### 같은 순서의 fixture는 의존성에 따라 실행됩니다 (Fixtures of the same order execute based on dependencies)
- fixture가 다른 fixture를 요청하면 다른 fixture가 먼저 실행됩니다. 따라서 fixture `a`가 fixture `b`를 요청하면 fixture `b`가 먼저 실행됩니다. 왜냐하면 `a`는 `b`에 의존하고 `b` 없이는 작동할 수 없기 때문입니다. `a`가 `b`의 결과를 필요로 하지 않더라도 `b` 다음에 실행되도록 하기 위해 여전히 `b`를 요청할 수 있습니다. 예를 들어:

```python
from __future__ import annotations

import pytest

@pytest.fixture
def order():
    return []

@pytest.fixture
def a(order):
    order.append("a")

@pytest.fixture
def b(a, order):
    order.append("b")

@pytest.fixture
def c(b, order):
    order.append("c")

@pytest.fixture
def d(c, b, order):
    order.append("d")

@pytest.fixture
def e(d, b, order):
    order.append("e")

@pytest.fixture
def f(e, order):
    order.append("f")

@pytest.fixture
def g(f, c, order):
    order.append("g")

def test_order(g, order):
    assert order == ["a", "b", "c", "d", "e", "f", "g"]
```

무엇이 무엇에 의존하는지 매핑하면 다음과 같은 모습이 됩니다:

![../_images/test_fixtures_order_dependencies.svg](https://docs.pytest.org/en/stable/_images/test_fixtures_order_dependencies.svg)

각 fixture가 제공하는 규칙(각 fixture가 어떤 fixture 다음에 와야 하는지)이 충분히 포괄적이어서 다음과 같이 평면화할 수 있습니다:

![../_images/test_fixtures_order_dependencies_flat.svg](https://docs.pytest.org/en/stable/_images/test_fixtures_order_dependencies_flat.svg)

- 주어진 테스트에 대해 pytest가 명확하고 선형적인 의존성 체인을 파악하고 그 결과로 작업 순서를 결정할 수 있도록 이러한 요청을 통해 충분한 정보가 제공되어야 합니다. 모호성이 있고 작업 순서를 둘 이상의 방식으로 해석할 수 있다면, pytest가 언제든 그 해석 중 하나를 선택할 수 있다고 가정해야 합니다.
- 예를 들어, `d`가 `c`를 요청하지 않는다면, 즉 그래프가 다음과 같이 보인다면:

![../_images/test_fixtures_order_dependencies_unclear.svg](https://docs.pytest.org/en/stable/_images/test_fixtures_order_dependencies_unclear.svg)

- `c`를 요청한 것이 `g` 외에는 없고, `g`도 `f`를 요청하기 때문에, 이제 `c`가 `f`, `e`, 또는 `d` 이전/이후에 와야 하는지 불분명해졌습니다. `c`에 대해 설정된 유일한 규칙은 `b` 이후 그리고 `g` 이전에 실행되어야 한다는 것입니다.
- pytest는 이 경우 `c`가 어디에 위치해야 하는지 알 수 없으므로, `g`와 `b` 사이 어디든 올 수 있다고 가정해야 합니다.
- 이것이 반드시 나쁜 것은 아니지만, 유념해야 할 점입니다. 만약 실행 순서가 테스트가 목표로 하는 동작에 영향을 미치거나 테스트 결과에 영향을 줄 수 있다면, pytest가 그 순서를 선형화/"평탄화"할 수 있는 방식으로 명시적으로 순서를 정의해야 합니다.

##### Autouse 픽스처는 해당 스코프 내에서 가장 먼저 실행됩니다 (Autouse fixtures are executed first within their scope)
- Autouse 픽스처는 그것을 참조할 수 있는 모든 테스트에 적용된다고 가정되므로, 해당 스코프 내의 다른 픽스처보다 먼저 실행됩니다. Autouse 픽스처가 요청하는 픽스처는 실제 autouse 픽스처가 적용되는 테스트에 대해 효과적으로 autouse 픽스처가 됩니다.
- 따라서 픽스처 `a`가 autouse이고 픽스처 `b`가 아니지만, 픽스처 `a`가 픽스처 `b`를 요청한다면, 픽스처 `b`는 효과적으로 autouse 픽스처가 되지만, `a`가 적용되는 테스트에 대해서만 그렇습니다.
- 마지막 예에서, `d`가 `c`를 요청하지 않으면 그래프가 불분명해졌습니다. 하지만 `c`가 autouse라면, `c`가 그들에 의존하기 때문에 `b`와 `a`도 효과적으로 autouse가 될 것입니다. 결과적으로, 그들은 모두 해당 스코프 내에서 non-autouse 픽스처 위로 이동될 것입니다. 따라서 테스트 파일이 다음과 같다면:

```python
from __future__ import annotations

import pytest

@pytest.fixture
def order():
    return []

@pytest.fixture
def a(order):
    order.append("a")

@pytest.fixture
def b(a, order):
    order.append("b")

@pytest.fixture(autouse=True)
def c(b, order):
    order.append("c")

@pytest.fixture
def d(b, order):
    order.append("d")

@pytest.fixture
def e(d, order):
    order.append("e")

@pytest.fixture
def f(e, order):
    order.append("f")

@pytest.fixture
def g(f, c, order):
    order.append("g")

def test_order_and_g(g, order):
    assert order == ["a", "b", "c", "d", "e", "f", "g"]
```

그래프는 다음과 같이 보일 것입니다:

![../_images/test_fixtures_order_autouse.svg](https://docs.pytest.org/en/stable/_images/test_fixtures_order_autouse.svg)

`c`를 이제 그래프에서 `d` 위에 놓을 수 있기 때문에, pytest는 다시 한 번 그래프를 다음과 같이 선형화할 수 있습니다:

![../_images/test_fixtures_order_autouse_flat.svg](https://docs.pytest.org/en/stable/_images/test_fixtures_order_autouse_flat.svg)

이 예에서, `c`는 `b`와 `a`도 효과적으로 autouse 픽스처로 만듭니다.
- 하지만 autouse를 사용할 때는 주의해야 합니다. autouse 픽스처는 요청하지 않아도 그것에 도달할 수 있는 모든 테스트에 대해 자동으로 실행되기 때문입니다. 예를 들어, 다음 파일을 고려해보세요:

```python
from __future__ import annotations

import pytest

@pytest.fixture(scope="class")
def order():
    return []

@pytest.fixture(scope="class", autouse=True)
def c1(order):
    order.append("c1")

@pytest.fixture(scope="class")
def c2(order):
    order.append("c2")

@pytest.fixture(scope="class")
def c3(order, c1):
    order.append("c3")

class TestClassWithC1Request:
    def test_order(self, order, c1, c3):
        assert order == ["c1", "c3"]

class TestClassWithoutC1Request:
    def test_order(self, order, c2):
        assert order == ["c1", "c2"]
```

`TestClassWithoutC1Request` 내부의 어떤 것도 `c1`을 요청하지 않지만, 그 안의 테스트에 대해 여전히 실행됩니다:

![../_images/test_fixtures_order_autouse_multiple_scopes.svg](https://docs.pytest.org/en/stable/_images/test_fixtures_order_autouse_multiple_scopes.svg)

- 하지만 하나의 autouse 픽스처가 non-autouse 픽스처를 요청했다고 해서, 그 non-autouse 픽스처가 적용될 수 있는 모든 컨텍스트에 대해 autouse 픽스처가 되는 것은 아닙니다. 실제 autouse 픽스처(non-autouse 픽스처를 요청한 픽스처)가 적용될 수 있는 컨텍스트에 대해서만 효과적으로 autouse 픽스처가 됩니다. 예를 들어, 다음 테스트 파일을 살펴보세요:

```python
from __future__ import annotations

import pytest

@pytest.fixture
def order():
    return []

@pytest.fixture
def c1(order):
    order.append("c1")

@pytest.fixture
def c2(order):
    order.append("c2")

class TestClassWithAutouse:
    @pytest.fixture(autouse=True)
    def c3(self, order, c2):
        order.append("c3")

    def test_req(self, order, c1):
        assert order == ["c2", "c3", "c1"]

    def test_no_req(self, order):
        assert order == ["c2", "c3"]

class TestClassWithoutAutouse:
    def test_req(self, order, c1):
        assert order == ["c1"]

    def test_no_req(self, order):
        assert order == []
```

이는 다음과 같이 분석될 것입니다:

![../_images/test_fixtures_order_autouse_temp_effects.svg](https://docs.pytest.org/en/stable/_images/test_fixtures_order_autouse_temp_effects.svg)

- `TestClassWithAutouse` 내부의 `test_req`와 `test_no_req`에 대해, `c3`는 효과적으로 `c2`를 autouse 픽스처로 만듭니다. 이것이 `c2`와 `c3`가 요청되지 않았음에도 두 테스트 모두에 대해 실행되는 이유이며, `test_req`에 대해 `c2`와 `c3`가 `c1` 이전에 실행되는 이유입니다.
- 만약 이것이 `c2`를 _실제_ autouse 픽스처로 만든다면, `c2`는 `TestClassWithoutAutouse` 내부의 테스트에 대해서도 실행될 것입니다. 왜냐하면 그들이 원한다면 `c2`를 참조할 수 있기 때문입니다. 하지만 그렇지 않습니다. `TestClassWithoutAutouse` 테스트의 관점에서 `c2`는 autouse 픽스처가 아닙니다. 그들은 `c3`를 볼 수 없기 때문입니다.
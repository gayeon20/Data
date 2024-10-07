---
title: "[Python] 파이테스트 (Pytest)"
excerpt: pytest 프레임워크를 사용하면 작고 읽기 쉬운 테스트를 쉽게 작성할 수 있으며, 애플리케이션 및 라이브러리에 대한 복잡한 기능 테스트를 지원하도록 확장할 수 있습니다.
categories:
  - Pytest
tags:
  - Python
  - Python-Library
  - Test
  - Python-pytest
last_modified_at: 2024-04-11T15:10:56+09:00
link: https://docs.pytest.org/en/stable/getting-started.html
상위 항목: "[[python_test|파이썬 테스트 (Test)]]"
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

**하위 항목**
- [[pytest_fixtures|테스트 코드 작성 (Write code)]]

> [API Reference](https://docs.pytest.org/en/stable/reference/reference.html#configuration-options)
> [Github](https://github.com/pytest-dev/pytest)

> 요구사항: Python 3.8+ or PyPy3.

---
#TODO
- [ ] [CI Pipelines - pytest documentation](https://docs.pytest.org/en/stable/explanation/ci.html)
- [ ] [Flaky tests - pytest documentation](https://docs.pytest.org/en/stable/explanation/flaky.html)

- `pytest` 프레임워크를 사용하면 작고 읽기 쉬운 테스트를 쉽게 작성할 수 있으며, 애플리케이션 및 라이브러리에 대한 복잡한 기능 테스트를 지원하도록 확장할 수 있습니다.

```sh
pip install -U pytest
```
- `pytest` 패키지를 설치하여 사용합니다.

```sh
pytest --version   # shows where pytest was imported from
pytest --fixtures  # show available builtin function arguments
pytest -h | --help # show help on command line and config file options
```


> [!info] 특징
> - 실패하는 [assert 구문](https://docs.pytest.org/en/stable/how-to/assert.html#assert)에 대한 상세 정보 (`self.assert*` 이름을 기억할 필요 없음)
> - 테스트 모듈 및 함수의 [자동 발견](https://docs.pytest.org/en/stable/explanation/goodpractices.html#test-discovery)
> - 작은 규모 또는 매개변수화된 장기 테스트 리소스 관리를 위한 [모듈식 픽스처](https://docs.pytest.org/en/stable/reference/fixtures.html#fixture)
> - [unittest](https://docs.pytest.org/en/stable/how-to/unittest.html#unittest) (trial 포함) 테스트 스위트를 즉시 실행 가능
> - 풍부한 플러그인 아키텍처, 1300개 이상의 [외부 플러그인](https://docs.pytest.org/en/stable/reference/plugin_list.html#plugin-list)과 활발한 커뮤니티

## 실행
- Pytest는 명령줄이나 파일에서 테스트를 실행하고 선택하는 여러 방법을 지원합니다 (파일에서 인수 읽기에 대해서는 아래를 참조하세요).

### 모듈에서 테스트 실행

```sh
pytest test_mod.py
```

### 디렉토리에서 테스트 실행

```sh
pytest testing/
```

### 키워드 표현식으로 테스트 실행

```sh
pytest -k 'MyClass and not method'
```

- 이는 주어진 _문자열 표현식_ (대소문자 구분 없음)과 일치하는 이름을 포함하는 테스트를 실행합니다. 이 표현식에는 파일 이름, 클래스 이름 및 함수 이름을 변수로 사용하는 Python 연산자가 포함될 수 있습니다. 위의 예시는 `TestMyClass.test_something`은 실행하지만 `TestMyClass.test_method_simple`은 실행하지 않습니다. Windows에서 이를 실행할 때는 `''` 대신 `""`를 표현식에 사용하세요.

### 컬렉션 인수로 테스트 실행

- 작업 디렉토리에 상대적인 모듈 파일 이름을 전달하고, 그 뒤에 `::` 문자로 구분된 클래스 이름과 함수 이름과 같은 지정자, 그리고 `[]`로 둘러싸인 매개변수화의 매개변수를 따라오게 합니다.

모듈 내의 특정 테스트를 실행하려면:

```sh
pytest tests/test_mod.py::test_func
```

클래스의 모든 테스트를 실행하려면:

```sh
pytest tests/test_mod.py::TestClass
```

특정 테스트 메서드를 지정하려면:

```sh
pytest tests/test_mod.py::TestClass::test_method
```

테스트의 특정 매개변수화를 지정하려면:

```sh
pytest tests/test_mod.py::test_func[x1,y2]
```

### 마커 표현식으로 테스트 실행

`@pytest.mark.slow` 데코레이터로 장식된 모든 테스트를 실행하려면:

```sh
pytest -m slow
```

`phase` 키워드 인수가 `1`로 설정된 `@pytest.mark.slow(phase=1)` 데코레이터로 주석 처리된 모든 테스트를 실행하려면:

```sh
pytest -m "slow(phase=1)"
```

자세한 내용은 [marks](https://docs.pytest.org/en/stable/how-to/mark.html#mark)를 참조하세요.

### 패키지에서 테스트 실행

```sh
pytest --pyargs pkg.testing
```

이는 `pkg.testing`을 임포트하고 그 파일 시스템 위치를 사용하여 테스트를 찾아 실행합니다.

### 파일에서 인수 읽기

위의 모든 내용은 `@` 접두사를 사용하여 파일에서 읽을 수 있습니다:

```sh
pytest @tests_to_run.txt
```

여기서 `tests_to_run.txt`는 줄당 하나의 항목을 포함합니다. 예:

```sh
tests/test_file.py
tests/test_mod.py::test_func[x1,y2]
tests/test_mod.py::TestClass
-m slow
```

이 파일은 `pytest --collect-only -q`를 사용하여 생성하고 필요에 따라 수정할 수 있습니다.

### `python -m pytest`를 통해 pytest 호출하기

- 명령줄에서 Python 인터프리터를 통해 테스트를 실행할 수 있습니다:

```sh
python -m pytest […]
```

이는 명령줄 스크립트 `pytest […]`를 직접 호출하는 것과 거의 동일하지만, `python`을 통해 호출하면 현재 디렉토리도 `sys.path`에 추가됩니다.

### Python 코드에서 pytest 호출하기

- Python 코드에서 직접 `pytest`를 호출할 수 있습니다:

```python
retcode = pytest.main()
```

이는 명령줄에서 "pytest"를 호출하는 것과 같은 효과를 냅니다. [`SystemExit`](https://docs.python.org/3/library/exceptions.html#SystemExit "(in Python v3.12)")을 발생시키지 않고 대신 [종료 코드](https://docs.pytest.org/en/stable/reference/exit-codes.html#exit-codes)를 반환합니다. 인수를 전달하지 않으면 `main`은 프로세스의 명령줄 인수([`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "(in Python v3.12)"))에서 인수를 읽습니다. 이는 바람직하지 않을 수 있습니다. 옵션과 인수를 명시적으로 전달할 수 있습니다:

```
retcode = pytest.main(["-x", "mytestdir"])
```

- `pytest.main`에 추가 플러그인을 지정할 수 있습니다:

```python
# myinvoke.py의 내용
import sys

import pytest

class MyPlugin:
    def pytest_sessionfinish(self):
        print("*** 테스트 실행 보고 완료")

if __name__ == "__main__":
    sys.exit(pytest.main(["-qq"], plugins=[MyPlugin()]))
```
- 실행하면 MyPlugin이 추가되고 그 훅이 호출되었음을 보여줍니다:

```sh
$ python myinvoke.py
*** 테스트 실행 보고 완료
```


> [!NOTE]
> - `pytest.main()`을 호출하면 테스트와 그 테스트가 임포트하는 모든 모듈을 임포트하게 됩니다. Python의 임포트 시스템의 캐싱 메커니즘으로 인해, 같은 프로세스에서 `pytest.main()`을 연속해서 호출하면 호출 사이에 이루어진 파일 변경사항이 반영되지 않습니다. 이러한 이유로, 같은 프로세스에서 `pytest.main()`을 여러 번 호출하는 것(예를 들어, 테스트를 다시 실행하기 위해)은 권장되지 않습니다.

## 단언 (Assertion) [[pytest_assertion|(자세히 보기)]]
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


## 픽스처 (Fixture) [[pytest_fixtures|(자세히 보기)]]
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

## 마크 (Mark)
- `pytest.mark` 헬퍼를 사용하면 테스트 함수에 쉽게 메타데이터를 설정할 수 있습니다. 내장 마커의 전체 목록은 [API 참조](https://docs.pytest.org/en/stable/reference/reference.html#marks-ref)에서 찾을 수 있습니다. 또는 CLI에서 `pytest --markers` 명령을 사용하여 내장 및 사용자 정의 마커를 포함한 모든 마커를 나열할 수 있습니다.
  다음은 몇 가지 내장 마커입니다:
	- [usefixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html#usefixtures) - 테스트 함수나 클래스에 픽스처 사용
	- [filterwarnings](https://docs.pytest.org/en/stable/how-to/capture-warnings.html#filterwarnings) - 테스트 함수의 특정 경고 필터링
	- [skip](https://docs.pytest.org/en/stable/how-to/skipping.html#skip) - 항상 테스트 함수 건너뛰기
	- [skipif](https://docs.pytest.org/en/stable/how-to/skipping.html#skipif) - 특정 조건이 충족되면 테스트 함수 건너뛰기
	- [xfail](https://docs.pytest.org/en/stable/how-to/skipping.html#xfail) - 특정 조건이 충족되면 "예상된 실패" 결과 생성
	- [parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html#parametrizemark) - 같은 테스트 함수에 대해 여러 번 호출 수행

- 사용자 정의 마커를 만들거나 전체 테스트 클래스 또는 모듈에 마커를 적용하는 것은 쉽습니다. 이러한 마커는 플러그인에서 사용할 수 있으며, 일반적으로 `-m` 옵션을 사용하여 명령줄에서 [테스트를 선택](https://docs.pytest.org/en/stable/example/markers.html#mark-run)하는 데 사용됩니다.
- 문서 역할도 하는 예제는 [사용자 정의 마커 작업](https://docs.pytest.org/en/stable/example/markers.html#mark-examples)을 참조하세요.

> 마커는 테스트에만 적용할 수 있으며 [픽스처](https://docs.pytest.org/en/stable/reference/fixtures.html#fixtures)에는 영향을 미치지 않습니다.

### 마커 등록 (Registering marks)

- `pytest.ini` 파일에서 다음과 같이 사용자 정의 마커를 등록할 수 있습니다:

```ini
[pytest]
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    serial
```

또는 `pyproject.toml` 파일에서 다음과 같이 등록할 수 있습니다:

```ini
[tool.pytest.ini_options]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "serial",
]
```

- 마커 이름 뒤의 `:` 이후의 모든 내용은 선택적 설명임을 유의하세요.
  또는 [pytest_configure](https://docs.pytest.org/en/stable/reference/reference.html#initialization-hooks) 훅에서 프로그래밍 방식으로 새 마커를 등록할 수 있습니다:

```python
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "env(name): mark test to run only on named environment"
    )
```

- 등록된 마커는 pytest의 도움말 텍스트에 나타나며 경고를 발생시키지 않습니다(다음 섹션 참조). 서드파티 플러그인은 항상 [마커를 등록](https://docs.pytest.org/en/stable/how-to/writing_plugins.html#registering-markers)하는 것이 좋습니다.

### 알 수 없는 마커에 대한 오류 발생 (Raising errors on unknown marks)

- `@pytest.mark.name_of_the_mark` 데코레이터로 적용된 등록되지 않은 마커는 오타로 인해 예상치 못한 일이 발생하는 것을 방지하기 위해 항상 경고를 발생시킵니다. 이전 섹션에서 설명한 대로 `pytest.ini` 파일에 등록하거나 사용자 정의 `pytest_configure` 훅을 사용하여 사용자 정의 마커에 대한 경고를 비활성화할 수 있습니다.
- `--strict-markers` 명령줄 플래그가 전달되면 `@pytest.mark.name_of_the_mark` 데코레이터로 적용된 알 수 없는 마커는 오류를 발생시킵니다. `addopts`에 `--strict-markers`를 추가하여 프로젝트에서 이 유효성 검사를 강제할 수 있습니다:

```ini
[pytest]
addopts = --strict-markers
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    serial
```

## 파라미터화 (Parametrize)
- pytest는 여러 수준에서 테스트 파라미터화를 가능하게 합니다:
	- [`pytest.fixture()`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.fixture "pytest.fixture")는 [픽스처 함수를 파라미터화](https://docs.pytest.org/en/stable/how-to/fixtures.html#fixture-parametrize)할 수 있게 합니다.
	- [@pytest.mark.parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html#pytest-mark-parametrize)는 테스트 함수나 클래스에서 여러 인수 집합과 픽스처를 정의할 수 있게 합니다.
	- [pytest_generate_tests](https://docs.pytest.org/en/stable/how-to/parametrize.html#pytest-generate-tests)는 사용자 정의 파라미터화 스키마나 확장을 정의할 수 있게 합니다.

### `@pytest.mark.parametrize`: 테스트 함수 파라미터화하기
- 내장된 [pytest.mark.parametrize](https://docs.pytest.org/en/stable/reference/reference.html#pytest-mark-parametrize-ref) 데코레이터를 사용하면 테스트 함수의 인수를 파라미터화할 수 있습니다. 다음은 특정 입력이 예상 출력으로 이어지는지 확인하는 일반적인 테스트 함수의 예입니다:

```python
# test_expectation.py의 내용
import pytest

@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
```

- 여기서 `@parametrize` 데코레이터는 세 가지 다른 `(test_input,expected)` 튜플을 정의하여 `test_eval` 함수가 이들을 차례로 사용하여 세 번 실행되도록 합니다:

```sh
$ pytest
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-8.x.y, pluggy-1.x.y
rootdir: /home/sweet/project
collected 3 items

test_expectation.py ..F                                              [100%]

================================= FAILURES =================================
____________________________ test_eval[6*9-42] _____________________________

test_input = '6*9', expected = 42

    @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
    def test_eval(test_input, expected):
>       assert eval(test_input) == expected
E       AssertionError: assert 54 == 42
E        +  where 54 = eval('6*9')

test_expectation.py:6: AssertionError
========================= short test summary info ==========================
FAILED test_expectation.py::test_eval[6*9-42] - AssertionError: assert 54…
======================= 1 failed, 2 passed in 0.12s ========================
```

> [!warning]
> - 파라미터 값은 테스트에 그대로 전달됩니다(어떤 복사도 없음).

- 예를 들어, 리스트나 딕셔너리를 파라미터 값으로 전달하고 테스트 케이스 코드가 이를 변경하면, 그 변경 사항은 이후의 테스트 케이스 호출에 반영됩니다.

> [!warning]
> - pytest는 기본적으로 유니코드 문자열에 사용된 비 ASCII 문자를 이스케이프 처리합니다. 왜냐하면 이는 여러 단점이 있기 때문입니다. 그러나 파라미터화에 유니코드 문자열을 사용하고 이를 터미널에서 그대로(이스케이프 처리되지 않은 상태로) 보고 싶다면, `pytest.ini`에 다음 옵션을 사용하세요:
> 
> ```
> [pytest]
> disable_test_id_escaping_and_forfeit_all_rights_to_community_support = True
> ```
> 
> 단, 이는 사용 중인 OS와 현재 설치된 플러그인에 따라 원치 않는 부작용이나 버그를 일으킬 수 있으므로 자신의 책임 하에 사용하세요.

- 이 예제에서 설계된 대로, 단 하나의 입력/출력 값 쌍만이 간단한 테스트 함수를 실패시킵니다. 그리고 일반적인 테스트 함수 인수와 마찬가지로, 트레이스백에서 `input`과 `output` 값을 볼 수 있습니다.
- parametrize 마커를 클래스나 모듈에도 사용할 수 있습니다([How to mark test functions with attributes](https://docs.pytest.org/en/stable/how-to/mark.html#mark) 참조). 이는 여러 함수를 인수 집합으로 호출합니다. 예를 들면:

```python
import pytest

@pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
class TestClass:
    def test_simple_case(self, n, expected):
        assert n + 1 == expected

    def test_weird_simple_case(self, n, expected):
        assert (n * 1) + 1 == expected
```

모듈의 모든 테스트를 파라미터화하려면 [`pytestmark`](https://docs.pytest.org/en/stable/reference/reference.html#globalvar-pytestmark) 전역 변수에 할당할 수 있습니다:

```python
import pytest

pytestmark = pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])

class TestClass:
    def test_simple_case(self, n, expected):
        assert n + 1 == expected

    def test_weird_simple_case(self, n, expected):
        assert (n * 1) + 1 == expected
```

parametrize 내에서 개별 테스트 인스턴스에 마크를 지정하는 것도 가능합니다. 예를 들어 내장된 `mark.xfail`을 사용할 수 있습니다:

```python
# test_expectation.py의 내용
import pytest

@pytest.mark.parametrize(
    "test_input,expected",
    [("3+5", 8), ("2+4", 6), pytest.param("6*9", 42, marks=pytest.mark.xfail)],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected
```

이를 실행해 봅시다:

```
$ pytest
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-8.x.y, pluggy-1.x.y
rootdir: /home/sweet/project
collected 3 items

test_expectation.py ..x                                              [100%]

======================= 2 passed, 1 xfailed in 0.12s =======================
```

이전에 실패를 일으켰던 파라미터 집합이 이제 "xfailed"(실패 예상) 테스트로 나타납니다.

- `parametrize`에 제공된 값이 빈 리스트를 결과로 내는 경우(예: 어떤 함수에 의해 동적으로 생성되는 경우), pytest의 동작은 [`empty_parameter_set_mark`](https://docs.pytest.org/en/stable/reference/reference.html#confval-empty_parameter_set_mark) 옵션에 의해 정의됩니다.
- 여러 파라미터화된 인수의 모든 조합을 얻으려면 `parametrize` 데코레이터를 중첩할 수 있습니다:

```python
import pytest

@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    pass
```

- 이는 데코레이터의 순서대로 파라미터를 소진하면서 `x=0/y=2`, `x=1/y=2`, `x=0/y=3`, `x=1/y=3`의 인수 집합으로 테스트를 실행합니다.

> [!example] 기본 `pytest_generate_tests` 예제
> 
> - 때로는 자신만의 파라미터화 스키마를 구현하거나 픽스처의 파라미터나 범위를 결정하는 데 있어 일부 동적인 요소를 구현하고 싶을 수 있습니다. 이를 위해 테스트 함수를 수집할 때 호출되는 `pytest_generate_tests` 훅을 사용할 수 있습니다. 전달된 `metafunc` 객체를 통해 요청된 테스트 컨텍스트를 검사할 수 있고, 가장 중요하게는 `metafunc.parametrize()`를 호출하여 파라미터화를 수행할 수 있습니다.
> - 예를 들어, 새로운 `pytest` 명령줄 옵션을 통해 설정하고자 하는 문자열 입력을 받는 테스트를 실행하고 싶다고 가정해 봅시다. 먼저 `stringinput` 픽스처 함수 인수를 받는 간단한 테스트를 작성해 봅시다:
> 
> ```python
> # test_strings.py의 내용
> 
> def test_valid_string(stringinput):
>     assert stringinput.isalpha()
> ```
> 
> - 이제 명령줄 옵션을 추가하고 테스트 함수를 파라미터화하는 `conftest.py` 파일을 추가합니다:
> 
> ```python
> # conftest.py의 내용
> 
> def pytest_addoption(parser):
>     parser.addoption(
>         "--stringinput",
>         action="append",
>         default=[],
>         help="테스트 함수에 전달할 stringinput 목록",
>     )
> 
> def pytest_generate_tests(metafunc):
>     if "stringinput" in metafunc.fixturenames:
>         metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))
> ```
> 
> - 이제 두 개의 stringinput 값을 전달하면 테스트가 두 번 실행됩니다:
> 
> ```sh
> $ pytest -q --stringinput="hello" --stringinput="world" test_strings.py
> ..                                                                   [100%]
> 2 passed in 0.12s
> ```
> 
> - 테스트가 실패하도록 하는 stringinput으로도 실행해 봅시다:
> 
> ```sh
> $ pytest -q --stringinput="!" test_strings.py
> F                                                                    [100%]
> ================================= FAILURES =================================
> ___________________________ test_valid_string[!] ___________________________
> 
> stringinput = '!'
> 
>     def test_valid_string(stringinput):
> >       assert stringinput.isalpha()
> E       AssertionError: assert False
> E        +  where False = <built-in method isalpha of str object at 0xdeadbeef0001>()
> E        +    where <built-in method isalpha of str object at 0xdeadbeef0001> = '!'.isalpha
> 
> test_strings.py:4: AssertionError
> ========================= short test summary info ==========================
> FAILED test_strings.py::test_valid_string[!] - AssertionError: assert False
> 1 failed in 0.12s
> ```
> 
> 예상대로 테스트 함수가 실패합니다.
> stringinput을 지정하지 않으면 `metafunc.parametrize()`가 빈 파라미터 리스트로 호출되므로 테스트가 건너뛰어집니다:
> 
> ```sh
> $ pytest -q -rs test_strings.py
> s                                                                    [100%]
> ========================= short test summary info ==========================
> SKIPPED [1] test_strings.py: got empty parameter set ['stringinput'], function test_valid_string at /home/sweet/project/test_strings.py:2
> 1 skipped in 0.12s
> ```
> 
> - `metafunc.parametrize`를 다른 파라미터 집합으로 여러 번 호출할 때, 모든 집합에 걸쳐 파라미터 이름이 중복되면 안 됩니다. 그렇지 않으면 오류가 발생합니다.


## 임시 디렉토리

### `tmp_path` 픽스처 (The `tmp_path` fixture)

- `tmp_path` 픽스처를 사용하면 각 테스트 함수마다 고유한 임시 디렉토리를 제공받을 수 있습니다.
- `tmp_path`는 [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.12)") 객체입니다. 다음은 테스트에서 사용하는 예시입니다:

```python
# test_tmp_path.py의 내용
CONTENT = "content"

def test_create_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT, encoding="utf-8")
    assert p.read_text(encoding="utf-8") == CONTENT
    assert len(list(tmp_path.iterdir())) == 1
    assert 0
```

- 이를 실행하면 마지막 `assert 0` 줄을 제외하고는 테스트가 통과됩니다. 우리는 이 줄을 값을 확인하는 데 사용합니다:

```sh
$ pytest test_tmp_path.py
=========================== test session starts ============================
platform linux -- Python 3.x.y, pytest-8.x.y, pluggy-1.x.y
rootdir: /home/sweet/project
collected 1 item

test_tmp_path.py F                                                   [100%]

================================= FAILURES =================================
_____________________________ test_create_file _____________________________

tmp_path = PosixPath('PYTEST_TMPDIR/test_create_file0')

    def test_create_file(tmp_path):
        d = tmp_path / "sub"
        d.mkdir()
        p = d / "hello.txt"
        p.write_text(CONTENT, encoding="utf-8")
        assert p.read_text(encoding="utf-8") == CONTENT
        assert len(list(tmp_path.iterdir())) == 1
>       assert 0
E       assert 0

test_tmp_path.py:11: AssertionError
========================= short test summary info ==========================
FAILED test_tmp_path.py::test_create_file - assert 0
============================ 1 failed in 0.12s =============================
```

- 기본적으로 `pytest`는 마지막 3번의 `pytest` 호출에 대한 임시 디렉토리를 유지합니다. 동일한 테스트 함수의 동시 호출은 기본 임시 디렉토리를 각 동시 실행마다 고유하게 구성하여 지원됩니다. 자세한 내용은 [임시 디렉토리 위치 및 보존](https://docs.pytest.org/en/stable/how-to/tmp_path.html#temporary-directory-location-and-retention)을 참조하세요.

### `tmp_path_factory` 픽스처 (The `tmp_path_factory` fixture)

- `tmp_path_factory`는 세션 범위의 픽스처로, 다른 픽스처나 테스트에서 임의의 임시 디렉토리를 생성하는 데 사용할 수 있습니다.
- 예를 들어, 테스트 스위트에 절차적으로 생성되는 디스크의 큰 이미지가 필요하다고 가정해 보겠습니다. 각 테스트마다 자체 `tmp_path`에 동일한 이미지를 계산하는 대신, 시간을 절약하기 위해 세션당 한 번만 생성할 수 있습니다:

```python
# conftest.py의 내용
import pytest

@pytest.fixture(scope="session")
def image_file(tmp_path_factory):
    img = compute_expensive_image()
    fn = tmp_path_factory.mktemp("data") / "img.png"
    img.save(fn)
    return fn

# test_image.py의 내용
def test_histogram(image_file):
    img = load_image(image_file)
    # 히스토그램 계산 및 테스트
```

자세한 내용은 [tmp_path_factory API](https://docs.pytest.org/en/stable/reference/reference.html#tmp-path-factory-factory-api)를 참조하세요.

> [!NOTE] `tmpdir`과 `tmpdir_factory` 픽스처 (The `tmpdir` and `tmpdir_factory` fixtures)
> - `tmpdir`과 `tmpdir_factory` 픽스처는 `tmp_path`와 `tmp_path_factory`와 유사하지만, 표준 [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.12)") 객체 대신 레거시 [py.path.local](https://py.readthedocs.io/en/latest/path.html) 객체를 사용/반환합니다.
> 
> > [!NOTE]
> > - 요즘은 `tmp_path`와 `tmp_path_factory`를 사용하는 것이 선호됩니다.
> > - 오래된 코드베이스를 현대화하는 데 도움이 되도록 legacypath 플러그인을 비활성화하여 pytest를 실행할 수 있습니다:
> > 
> > ```
> > pytest -p no:legacypath
> > ```
> > 
> > - 이렇게 하면 레거시 경로를 사용하는 테스트에서 오류가 발생합니다. 이는 설정 파일의 [`addopts`](https://docs.pytest.org/en/stable/reference/reference.html#confval-addopts) 매개변수의 일부로 영구적으로 설정할 수도 있습니다.
> - 자세한 내용은 [`tmpdir`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-tmpdir) [`tmpdir_factory`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-tmpdir_factory) API를 참조하세요.



### 임시 디렉토리 위치 및 보존 (Temporary directory location and retention)
- 임시 디렉토리는 기본적으로 시스템 임시 디렉토리의 하위 디렉토리로 생성됩니다. 기본 이름은 `pytest-NUM`이며, 여기서 `NUM`은 각 테스트 실행마다 증가합니다. 기본적으로 3개의 임시 디렉토리보다 오래된 항목은 제거됩니다. 이 동작은 [`tmp_path_retention_count`](https://docs.pytest.org/en/stable/reference/reference.html#confval-tmp_path_retention_count)와 [`tmp_path_retention_policy`](https://docs.pytest.org/en/stable/reference/reference.html#confval-tmp_path_retention_policy)로 구성할 수 있습니다.
- `--basetemp` 옵션을 사용하면 매 실행 전에 디렉토리가 제거되어, 실질적으로 가장 최근 실행의 임시 디렉토리만 유지됩니다.
- 다음과 같이 기본 임시 디렉토리 설정을 재정의할 수 있습니다:

```sh
pytest --basetemp=mydir
```

> [!warning]
> - `mydir`의 내용이 완전히 제거되므로, 해당 목적으로만 사용되는 디렉토리를 사용해야 합니다.

- `pytest-xdist`를 사용하여 로컬 머신에서 테스트를 분산할 때, 모든 임시 데이터가 단일 테스트 실행당 임시 디렉토리 아래에 위치하도록 하위 프로세스에 대한 `basetemp` 디렉토리를 자동으로 구성하는 데 주의를 기울입니다.

다음은 요청하신 대로 번역한 내용입니다:

## 설정 (Configuration)

명령줄 옵션과 INI 스타일 설정 파일의 값에 대한 도움말을 보려면 일반 도움말 옵션을 사용하세요:

```
pytest -h   # 옵션 _및_ 설정 파일 설정 출력
```

이는 설치된 플러그인에 의해 등록된 명령줄 및 설정 파일 설정을 표시합니다.

### 설정 파일 형식 (Configuration file formats)
- 많은 [pytest 설정](https://docs.pytest.org/en/stable/reference/reference.html#ini-options-ref)은 _설정 파일_ 에서 설정할 수 있으며, 관례상 저장소의 루트 디렉토리에 위치합니다.

#### pytest.ini

- `pytest.ini` 파일은 비어 있더라도 다른 파일보다 우선순위가 높습니다.
- 또는 숨겨진 버전인 `.pytest.ini`를 사용할 수 있습니다.

```ini
# pytest.ini 또는 .pytest.ini
[pytest]
minversion = 6.0
addopts = -ra -q
testpaths =
    tests
    integration
```

#### pyproject.toml

- `pyproject.toml`은 `tool.pytest.ini_options` 테이블을 포함할 때 설정에 고려됩니다.

```toml
# pyproject.toml
[tool.pytest.ini_options]
minversion = "6.0"
addopts = "-ra -q"
testpaths = [
    "tests",
    "integration",
]
```

> [!NOTE]
> - 왜 다른 도구들처럼 `[tool.pytest]`가 아니라 `[tool.pytest.ini_options]`인지 궁금할 수 있습니다. 그 이유는 pytest 팀이 향후 설정을 위해 풍부한 TOML 데이터 형식을 완전히 활용할 계획이며, `[tool.pytest]` 테이블을 그를 위해 예약해두고 있기 때문입니다. `ini_options` 테이블은 현재 기존 `.ini` 설정 시스템과 향후 설정 형식 사이의 브릿지 역할을 하고 있습니다.

#### tox.ini
- `tox.ini` 파일은 [tox](https://tox.readthedocs.io/) 프로젝트의 설정 파일이며, `[pytest]` 섹션이 있는 경우 pytest 설정을 저장하는 데에도 사용할 수 있습니다.

```ini
# tox.ini
[pytest]
minversion = 6.0
addopts = -ra -q
testpaths =
    tests
    integration
```

#### setup.cfg
- `setup.cfg` 파일은 일반적인 목적의 설정 파일로, 원래 `distutils`(현재 deprecated)와 [setuptools](https://setuptools.pypa.io/en/stable/userguide/declarative_config.html)에서 사용되었으며, `[tool:pytest]` 섹션이 있는 경우 pytest 설정을 저장하는 데에도 사용할 수 있습니다.

```cfg
# setup.cfg
[tool:pytest]
minversion = 6.0
addopts = -ra -q
testpaths =
    tests
    integration
```

> [!warning]
> - 매우 간단한 사용 사례가 아니라면 `setup.cfg` 사용은 권장되지 않습니다. `.cfg` 파일은 `pytest.ini`와 `tox.ini`와 다른 파서를 사용하여 추적하기 어려운 문제를 일으킬 수 있습니다. 가능한 경우 pytest 설정을 위해 후자의 파일들 또는 `pyproject.toml`을 사용하는 것이 권장됩니다.

### 초기화: rootdir와 configfile 결정 (Initialization: determining rootdir and configfile)

- pytest는 각 테스트 실행에 대해 `rootdir`를 결정하며, 이는 명령줄 인수(지정된 테스트 파일, 경로)와 설정 파일의 존재 여부에 따라 달라집니다. 결정된 `rootdir`와 `configfile`은 시작 시 pytest 헤더의 일부로 출력됩니다. 다음은 pytest가 `rootdir`를 사용하는 방법에 대한 요약입니다:
	- 수집 중 _nodeids_ 구성; 각 테스트에는 `rootdir`에 근거하여 전체 경로, 클래스 이름, 함수 이름 및 매개변수화(있는 경우)를 고려한 고유한 _nodeid_ 가 할당됩니다.
	- 플러그인이 프로젝트/테스트 실행 관련 정보를 저장하는 안정적인 위치로 사용됩니다; 예를 들어, 내부 [cache](https://docs.pytest.org/en/stable/how-to/cache.html#cache) 플러그인은 테스트 실행 간 상태를 저장하기 위해 `rootdir`에 `.pytest_cache` 하위 디렉토리를 생성합니다.

- `rootdir`는 `sys.path`/`PYTHONPATH`를 수정하거나 모듈 가져오기 방식에 영향을 미치는 데 사용되지 **않습니다**. 자세한 내용은 [pytest 가져오기 메커니즘 및 sys.path/PYTHONPATH](https://docs.pytest.org/en/stable/explanation/pythonpath.html#pythonpath)를 참조하세요.
- `--rootdir=path` 명령줄 옵션을 사용하여 특정 디렉토리를 강제로 지정할 수 있습니다. 다른 명령줄 옵션과 달리 `--rootdir`는 `pytest.ini` 내의 [`addopts`](https://docs.pytest.org/en/stable/reference/reference.html#confval-addopts)와 함께 사용할 수 없습니다. 왜냐하면 `rootdir`는 이미 `pytest.ini`를 _찾는 데_ 사용되기 때문입니다.

#### `rootdir` 찾기 (Finding the `rootdir`)
- 다음은 `args`에서 rootdir를 찾는 알고리즘입니다:
	- 명령줄에 `-c`가 전달된 경우, 해당 파일을 설정 파일로 사용하고 그 디렉토리를 `rootdir`로 사용합니다.
	- 파일 시스템에 존재하는 경로로 인식되는 지정된 `args`의 공통 조상 디렉토리를 결정합니다. 그러한 경로가 없는 경우, 공통 조상 디렉토리는 현재 작업 디렉토리로 설정됩니다.
	- 조상 디렉토리와 상위 디렉토리에서 `pytest.ini`, `pyproject.toml`, `tox.ini`, `setup.cfg` 파일을 찾습니다. 하나가 일치하면 해당 파일이 `configfile`이 되고 그 디렉토리가 `rootdir`가 됩니다.
	- 설정 파일을 찾지 못한 경우, 공통 조상 디렉토리에서 상위로 `setup.py`를 찾아 `rootdir`를 결정합니다.
	- `setup.py`를 찾지 못한 경우, 지정된 각 `args`와 상위 디렉토리에서 `pytest.ini`, `pyproject.toml`, `tox.ini`, `setup.cfg`를 찾습니다. 하나가 일치하면 해당 파일이 `configfile`이 되고 그 디렉토리가 `rootdir`가 됩니다.
	- `configfile`을 찾지 못하고 설정 인수가 전달되지 않은 경우, 이미 결정된 공통 조상을 루트 디렉토리로 사용합니다. 이를 통해 패키지의 일부가 아니고 특정 설정 파일이 없는 구조에서 pytest를 사용할 수 있습니다.

- `args`가 주어지지 않으면, pytest는 현재 작업 디렉토리 아래에서 테스트를 수집하고 거기서부터 `rootdir` 결정을 시작합니다.
  파일은 다음 조건을 만족할 때만 설정에 일치합니다:
	- `pytest.ini`: 항상 일치하며, 비어 있더라도 우선순위를 가집니다.
	- `pyproject.toml`: `[tool.pytest.ini_options]` 테이블을 포함합니다.
	- `tox.ini`: `[pytest]` 섹션을 포함합니다.
	- `setup.cfg`: `[tool:pytest]` 섹션을 포함합니다.
 
- 마지막으로, 다른 일치 항목이 없는 경우 `pyproject.toml` 파일이 `configfile`로 간주됩니다. 이 경우 `[tool.pytest.ini_options]` 테이블을 포함하지 않아도 됩니다 (이는 `8.1`에서 추가되었습니다).
- 파일은 위의 순서대로 고려됩니다. 여러 `configfiles` 후보의 옵션은 결코 병합되지 않습니다 - 첫 번째 일치 항목이 우선합니다.
  설정 파일은 또한 `rootpath`의 값을 결정합니다.

- [`Config`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.Config) 객체(훅을 통해 또는 [`pytestconfig`](https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-pytestconfig) 픽스처를 통해 접근 가능)는 이후 다음 속성을 가집니다:
	- [`config.rootpath`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.Config.rootpath): 결정된 루트 디렉토리로, 존재가 보장됩니다. 테스트 주소("nodeids")를 구성하는 참조 디렉토리로 사용되며 플러그인에서 테스트 실행별 정보를 저장하는 데에도 사용할 수 있습니다.
	- [`config.inipath`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.Config.inipath): 결정된 `configfile`로, `None`일 수 있습니다 (역사적인 이유로 `inipath`라고 명명되었습니다).
> 버전 6.1에서 추가: `config.rootpath`와 `config.inipath` 속성. 이들은 이전의 `config.rootdir`와 `config.inifile`의 [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path) 버전으로, 기존 속성들은 `py.path.local` 타입이며 하위 호환성을 위해 여전히 존재합니다.

> [!example]
> ```
> pytest path/to/testdir path/other/
> ```
> 
> 이는 공통 조상을 `path`로 결정한 다음 다음과 같이 설정 파일을 확인합니다:
> 
> ```
> # 먼저 pytest.ini 파일을 찾습니다
> path/pytest.ini
> path/pyproject.toml  # 일치하려면 [tool.pytest.ini_options] 테이블을 포함해야 합니다
> path/tox.ini         # 일치하려면 [pytest] 섹션을 포함해야 합니다
> path/setup.cfg       # 일치하려면 [tool:pytest] 섹션을 포함해야 합니다
> pytest.ini
> … # 루트까지 계속
> 
> # 이제 setup.py를 찾습니다
> path/setup.py
> setup.py
> … # 루트까지 계속
> ```
> 
> 
> > [!warning]
> > - 사용자 정의 pytest 플러그인 명령줄 인수에 경로가 포함될 수 있습니다 (예: `pytest --log-output ../../test.log args`). 이 경우 `args`는 필수입니다. 그렇지 않으면 pytest는 rootdir 결정을 위해 test.log의 폴더를 사용합니다 ([#1435](https://github.com/pytest-dev/pytest/issues/1435) 참조). 현재 작업 디렉토리를 참조하기 위한 점 `.`도 가능합니다.
> 

### 내장 설정 파일 옵션 (Builtin configuration file options)
- 다음은 일반적으로 저장소의 루트에 위치한 `pytest.ini` (또는 `.pytest.ini`), `pyproject.toml`, `tox.ini`, 또는 `setup.cfg` 파일에 작성될 수 있는 빌트인 구성 옵션 목록입니다. 각 파일 형식에 대한 자세한 내용은 [구성 파일 형식](https://docs.pytest.org/en/stable/reference/customize.html#config-file-formats)을 참조하세요.


> [!waring]
> - 매우 간단한 사용 사례를 제외하고는 `setup.cfg`의 사용을 권장하지 않습니다. `.cfg` 파일은 `pytest.ini`와 `tox.ini`와는 다른 파서를 사용하므로 추적하기 어려운 문제를 일으킬 수 있습니다. 가능한 경우 pytest 구성을 위해 후자의 파일들이나 `pyproject.toml`을 사용하는 것이 좋습니다.

- 구성 옵션은 명령줄에서 `-o/--override-ini`를 사용하여 덮어쓸 수 있으며, 이는 여러 번 전달될 수 있습니다. 예상되는 형식은 `name=value`입니다. 예를 들어:

```sh
pytest -o console_output_style=classic -o cache_dir=/tmp/mycache
```

#### addopts

사용자가 지정한 것처럼 지정된 `OPTS`를 명령줄 인수 집합에 추가합니다. 예: 다음과 같은 ini 파일 내용이 있다면:

```
# pytest.ini 내용
[pytest]
addopts = --maxfail=2 -rf  # 2번의 실패 후 종료, 실패 정보 보고
```

`pytest test_hello.py`를 실행하는 것은 실제로 다음을 의미합니다:

```
pytest --maxfail=2 -rf test_hello.py
```

기본값은 옵션을 추가하지 않는 것입니다.

#### cache_dir

캐시 플러그인의 내용을 저장할 디렉토리를 설정합니다. 기본 디렉토리는 [rootdir](https://docs.pytest.org/en/stable/reference/customize.html#rootdir)에 생성되는 `.pytest_cache`입니다. 디렉토리는 상대 경로나 절대 경로일 수 있습니다. 상대 경로를 설정하면 [rootdir](https://docs.pytest.org/en/stable/reference/customize.html#rootdir)를 기준으로 디렉토리가 생성됩니다. 추가로 경로에는 확장될 환경 변수가 포함될 수 있습니다. 캐시 플러그인에 대한 자세한 내용은 [실패한 테스트를 다시 실행하고 테스트 실행 간 상태를 유지하는 방법](https://docs.pytest.org/en/stable/how-to/cache.html#cache-provider)을 참조하세요.

#### consider_namespace_packages

pytest가 Python 모듈을 수집할 때 [네임스페이스 패키지](https://packaging.python.org/en/latest/guides/packaging-namespace-packages)를 식별하려고 시도해야 하는지를 제어합니다. 기본값은 `False`입니다.

테스트 중인 패키지가 네임스페이스 패키지의 일부인 경우 `True`로 설정하세요.

[네이티브 네임스페이스 패키지](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/#native-namespace-packages)만 지원되며, [레거시 네임스페이스 패키지](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/#legacy-namespace-packages)를 지원할 계획은 없습니다.

버전 8.1에서 추가되었습니다.

#### console_output_style

테스트 실행 중 콘솔 출력 스타일을 설정합니다:

- `classic`: 클래식 pytest 출력.
- `progress`: 클래식 pytest 출력과 비슷하지만 진행 표시기가 있습니다.
- `progress-even-when-capture-no`: `capture=no`일 때도 진행 표시기를 사용할 수 있습니다.
- `count`: progress와 비슷하지만 진행 상황을 퍼센트 대신 완료된 테스트 수로 표시합니다.

기본값은 `progress`이지만, 선호하거나 새로운 모드가 예상치 못한 문제를 일으키는 경우 `classic`으로 돌아갈 수 있습니다:

```
# pytest.ini 내용
[pytest]
console_output_style = classic
```

#### doctest_encoding

docstring이 있는 텍스트 파일을 디코딩하는 데 사용할 기본 인코딩입니다. [pytest가 doctest를 처리하는 방법](https://docs.pytest.org/en/stable/how-to/doctest.html#doctest)을 참조하세요.

#### doctest_optionflags

표준 `doctest` 모듈의 하나 이상의 doctest 플래그 이름입니다. [pytest가 doctest를 처리하는 방법](https://docs.pytest.org/en/stable/how-to/doctest.html#doctest)을 참조하세요.

#### empty_parameter_set_mark

매개변수화에서 빈 매개변수 세트에 대한 동작을 선택할 수 있습니다.

- `skip` 빈 매개변수 세트가 있는 테스트를 건너뜁니다 (기본값)
- `xfail` 빈 매개변수 세트가 있는 테스트를 xfail(run=False)로 표시합니다
- `fail_at_collect` 매개변수화가 빈 매개변수 세트를 수집하면 예외를 발생시킵니다

```
# pytest.ini 내용
[pytest]
empty_parameter_set_mark = xfail
```

참고

이 옵션의 기본값은 향후 릴리스에서 `xfail`로 변경될 예정입니다. 이는 오류 가능성이 적다고 간주되기 때문입니다. 자세한 내용은 [#3155](https://github.com/pytest-dev/pytest/issues/3155)를 참조하세요.

#### faulthandler_timeout

테스트 실행 시간이 `X`초를 초과하면 모든 스레드의 트레이스백을 덤프합니다(fixture 설정 및 해체 시간 포함). [`faulthandler.dump_traceback_later()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.dump_traceback_later "(Python v3.12에서)") 함수를 사용하여 구현되므로 거기에 명시된 모든 주의사항이 적용됩니다.

```
# pytest.ini 내용
[pytest]
faulthandler_timeout=5
```

자세한 내용은 [Fault Handler](https://docs.pytest.org/en/stable/how-to/failures.html#faulthandler)를 참조하세요.

#### filterwarnings

일치하는 경고에 대해 취해야 할 필터 및 조치 목록을 설정합니다. 기본적으로 테스트 세션 동안 발생한 모든 경고는 테스트 세션 끝에 요약으로 표시됩니다.

```
# pytest.ini 내용
[pytest]
filterwarnings =
    error
    ignore::DeprecationWarning
```

이는 pytest에게 deprecation 경고를 무시하고 다른 모든 경고를 오류로 처리하도록 지시합니다. 자세한 내용은 [경고를 캡처하는 방법](https://docs.pytest.org/en/stable/how-to/capture-warnings.html#warnings)을 참조하세요.

#### junit_duration_report

버전 4.1에서 추가되었습니다.

JUnit XML 보고서에 지속 시간이 기록되는 방식을 구성합니다:

- `total` (기본값): 보고된 지속 시간에는 설정, 호출, 해체 시간이 포함됩니다.
- `call`: 보고된 지속 시간에는 설정 및 해체 시간을 제외한 호출 시간만 포함됩니다.

```
[pytest]
junit_duration_report = call
```

#### junit_family

버전 4.2에서 추가되었습니다.

버전 6.1에서 변경: 기본값이 `xunit2`로 변경되었습니다.

생성된 JUnit XML 파일의 형식을 구성합니다. 가능한 옵션은 다음과 같습니다:

- `xunit1` (또는 `legacy`): xunit 1.0 형식과 호환되는 이전 스타일의 출력을 생성합니다.
- `xunit2`: [xunit 2.0 스타일 출력](https://github.com/jenkinsci/xunit-plugin/blob/xunit-2.3.2/src/main/resources/org/jenkinsci/plugins/xunit/types/model/xsd/junit-10.xsd)을 생성합니다. 이는 최신 Jenkins 버전과 더 호환될 것입니다. **이것이 기본값입니다**.

```
[pytest]
junit_family = xunit2
```

#### junit_logging

버전 3.5에서 추가되었습니다.

버전 5.4에서 변경: `log`, `all`, `out-err` 옵션이 추가되었습니다.

캡처된 출력을 JUnit XML 파일에 작성해야 하는지 구성합니다. 유효한 값은 다음과 같습니다:

- `log`: 캡처된 `logging` 출력만 작성합니다.
- `system-out`: 캡처된 `stdout` 내용을 작성합니다.
- `system-err`: 캡처된 `stderr` 내용을 작성합니다.
- `out-err`: 캡처된 `stdout`와 `stderr` 내용을 모두 작성합니다.
- `all`: 캡처된 `logging`, `stdout`, `stderr` 내용을 모두 작성합니다.
- `no` (기본값): 캡처된 출력을 작성하지 않습니다.

```
[pytest]
junit_logging = system-out
```

#### junit_log_passing_tests

버전 4.6에서 추가되었습니다.

`junit_logging != "no"`인 경우, **통과된** 테스트에 대해 캡처된 출력을 JUnit XML 파일에 작성해야 하는지 구성합니다. 기본값은 `True`입니다.

```
[pytest]
junit_log_passing_tests = False
```

#### junit_suite_name

XML 항목의 루트 테스트 스위트 이름을 설정하려면 config 파일에서 `junit_suite_name` 옵션을 구성할 수 있습니다:

```
[pytest]
junit_suite_name = my_suite
```

#### log_auto_indent

여러 줄 로그 메시지의 선택적 자동 들여쓰기를 허용합니다.

모든 로깅에 대한 자동 들여쓰기 동작을 설정하기 위해 명령줄 옵션 `--log-auto-indent [value]`와 config 옵션 `log_auto_indent = [value]`를 지원합니다.

`[value]`는 다음과 같을 수 있습니다:

- True 또는 "On" - 여러 줄 로그 메시지를 동적으로 자동 들여쓰기
    
- False 또는 "Off" 또는 0 - 여러 줄 로그 메시지를 자동 들여쓰기하지 않음 (기본 동작)
    
- [양의 정수] - 여러 줄 로그 메시지를 [value] 공백만큼 자동 들여쓰기
    

```
[pytest]
log_auto_indent = False
```

특정 로그 항목에 대한 자동 들여쓰기 동작을 지정하기 위해 `logging.log()` 호출에 kwarg `extra={"auto_indent": [value]}`를 전달하는 것을 지원합니다. `extra` kwarg는 명령줄이나 config에 지정된 값을 덮어씁니다.

#### log_cli

테스트 실행 중 로그 표시를 활성화합니다(["실시간 로깅"](https://docs.pytest.org/en/stable/how-to/logging.html#live-logs)이라고도 함). 기본값은 `False`입니다.

```
[pytest]
log_cli = True
```

#### log_cli_date_format

실시간 로깅을 위해 날짜를 포맷팅할 때 사용될 [`time.strftime()`](https://docs.python.org/3/library/time.html#time.strftime "(in Python v3.12)")과 호환되는 문자열을 설정합니다.

```
[pytest]
log_cli_date_format = %Y-%m-%d %H:%M:%S
```

자세한 내용은 [실시간 로그](https://docs.pytest.org/en/stable/how-to/logging.html#live-logs)를 참조하세요.

#### log_cli_format

실시간 로깅 메시지를 포맷팅하는 데 사용되는 [`logging`](https://docs.python.org/3/library/logging.html#module-logging "(in Python v3.12)")과 호환되는 문자열을 설정합니다.

```
[pytest]
log_cli_format = %(asctime)s %(levelname)s %(message)s
```

자세한 내용은 [실시간 로그](https://docs.pytest.org/en/stable/how-to/logging.html#live-logs)를 참조하세요.

#### log_cli_level

실시간 로깅을 위해 캡처해야 하는 최소 로그 메시지 레벨을 설정합니다. 정수 값 또는 레벨의 이름을 사용할 수 있습니다.

```
[pytest]
log_cli_level = INFO
```

자세한 내용은 [실시간 로그](https://docs.pytest.org/en/stable/how-to/logging.html#live-logs)를 참조하세요.

#### log_date_format

로깅 캡처를 위해 날짜를 포맷팅할 때 사용될 [`time.strftime()`](https://docs.python.org/3/library/time.html#time.strftime "(in Python v3.12)")과 호환되는 문자열을 설정합니다.

```
[pytest]
log_date_format = %Y-%m-%d %H:%M:%S
```

자세한 내용은 [로깅 관리 방법](https://docs.pytest.org/en/stable/how-to/logging.html#logging)을 참조하세요.

#### log_file

현재 작업 디렉토리를 기준으로 로그 메시지를 작성해야 하는 파일 이름을 설정합니다. 이는 활성화된 다른 로깅 기능에 추가됩니다.

```
[pytest]
log_file = logs/pytest-logs.txt
```

자세한 내용은 [로깅 관리 방법](https://docs.pytest.org/en/stable/how-to/logging.html#logging)을 참조하세요.

#### log_file_date_format

로깅 파일의 날짜를 포맷팅할 때 사용될 [`time.strftime()`](https://docs.python.org/3/library/time.html#time.strftime "(in Python v3.12)")과 호환되는 문자열을 설정합니다.

```
[pytest]
log_file_date_format = %Y-%m-%d %H:%M:%S
```

자세한 내용은 [로깅 관리 방법](https://docs.pytest.org/en/stable/how-to/logging.html#logging)을 참조하세요.

#### log_file_format

로깅 파일로 리다이렉트되는 로깅 메시지를 포맷팅하는 데 사용되는 [`logging`](https://docs.python.org/3/library/logging.html#module-logging "(in Python v3.12)")과 호환되는 문자열을 설정합니다.

```
[pytest]
log_file_format = %(asctime)s %(levelname)s %(message)s
```

자세한 내용은 [로깅 관리 방법](https://docs.pytest.org/en/stable/how-to/logging.html#logging)을 참조하세요.

#### log_file_level

로깅 파일에 대해 캡처해야 하는 최소 로그 메시지 레벨을 설정합니다. 정수 값 또는 레벨의 이름을 사용할 수 있습니다.

```
[pytest]
log_file_level = INFO
```

자세한 내용은 [로깅 관리 방법](https://docs.pytest.org/en/stable/how-to/logging.html#logging)을 참조하세요.

#### log_format

캡처된 로깅 메시지를 포맷팅하는 데 사용되는 [`logging`](https://docs.python.org/3/library/logging.html#module-logging "(in Python v3.12)")과 호환되는 문자열을 설정합니다.

```
[pytest]
log_format = %(asctime)s %(levelname)s %(message)s
```

자세한 내용은 [로깅 관리 방법](https://docs.pytest.org/en/stable/how-to/logging.html#logging)을 참조하세요.

#### log_level

로깅 캡처를 위해 캡처해야 하는 최소 로그 메시지 레벨을 설정합니다. 정수 값 또는 레벨의 이름을 사용할 수 있습니다.

```
[pytest]
log_level = INFO
```

자세한 내용은 [로깅 관리 방법](https://docs.pytest.org/en/stable/how-to/logging.html#logging)을 참조하세요.

#### markers

`--strict-markers` 또는 `--strict` 명령줄 인수가 사용될 때, 코어 pytest나 일부 플러그인에 의해 코드에 정의된 알려진 마커만 허용됩니다.

이 설정에 추가 마커를 나열하여 화이트리스트에 추가할 수 있습니다. 이 경우 향후 회귀를 피하기 위해 `addopts`에 `--strict-markers`를 추가하는 것이 좋습니다:

```
[pytest]
addopts = --strict-markers
markers =
    slow
    serial
```

주의

`--strict-markers`의 사용이 매우 선호됩니다. `--strict`는 후방 호환성을 위해서만 유지되었으며 마커에만 적용되고 다른 옵션에는 적용되지 않기 때문에 다른 사람들에게 혼란을 줄 수 있습니다.

#### minversion

테스트 실행에 필요한 최소 pytest 버전을 지정합니다.

```
# pytest.ini의 내용
[pytest]
minversion = 3.0  # pytest-2.8로 실행하면 실패합니다
```

#### norecursedirs

테스트 검색을 위해 재귀할 때 피해야 할 디렉토리 basename 패턴을 설정합니다. 개별 (fnmatch 스타일) 패턴은 디렉토리의 basename에 적용되어 재귀 여부를 결정합니다. 패턴 매칭 문자:

```
*       모든 것과 일치
?       단일 문자와 일치
[seq]   seq의 모든 문자와 일치
[!seq]  seq에 없는 모든 문자와 일치
```

기본 패턴은 `'*.egg'`, `'.*'`, `'_darcs'`, `'build'`, `'CVS'`, `'dist'`, `'node_modules'`, `'venv'`, `'{arch}'`입니다. `norecursedirs`를 설정하면 기본값을 대체합니다. 다음은 특정 디렉토리를 피하는 방법의 예시입니다:

```
[pytest]
norecursedirs = .svn _build tmp*
```

이는 `pytest`에게 일반적인 subversion 또는 sphinx-build 디렉토리나 `tmp` 접두사가 있는 모든 디렉토리를 살펴보지 말라고 지시합니다.

또한, `pytest`는 가상 환경을 지능적으로 식별하고 무시하려고 시도합니다. 가상 환경의 루트로 간주되는 모든 디렉토리는 `--collect-in-virtualenv`가 주어지지 않는 한 테스트 수집 중에 고려되지 않습니다. 또한 `norecursedirs`가 `--collect-in-virtualenv`보다 우선순위가 높다는 점에 주의하세요; 예를 들어, `'.*'`와 일치하는 기본 디렉토리가 있는 가상 환경에서 테스트를 실행하려면 `--collect-in-virtualenv` 플래그를 사용하는 것 외에도 `norecursedirs`를 반드시 재정의해야 합니다.

#### python_classes

테스트 수집을 위해 고려되는 클래스를 결정하는 하나 이상의 이름 접두사 또는 glob 스타일 패턴. 여러 glob 패턴을 검색하려면 패턴 사이에 공백을 추가하세요. 기본적으로 pytest는 `Test`로 시작하는 모든 클래스를 테스트 수집으로 간주합니다. 다음은 `Suite`로 끝나는 클래스에서 테스트를 수집하는 예시입니다:

```
[pytest]
python_classes = *Suite
```

`unittest.TestCase`에서 파생된 클래스는 이 옵션에 관계없이 항상 수집된다는 점에 주의하세요. 이는 `unittest`의 자체 수집 프레임워크가 해당 테스트를 수집하는 데 사용되기 때문입니다.

다음은 요청하신 대로 번역한 내용입니다:

#### python_files (python_files)

하나 이상의 Glob 스타일 파일 패턴으로 테스트 모듈로 간주될 파이썬 파일을 결정합니다. 여러 glob 패턴을 검색하려면 패턴 사이에 공백을 추가하세요:

```
[pytest]
python_files = test_*.py check_*.py example_*.py
```

또는 한 줄에 하나씩:

```
[pytest]
python_files =
    test_*.py
    check_*.py
    example_*.py
```

기본적으로 `test_*.py`와 `*_test.py`에 일치하는 파일이 테스트 모듈로 간주됩니다.

#### python_functions (python_functions)

하나 이상의 이름 접두사 또는 glob 패턴으로 어떤 테스트 함수와 메서드가 테스트로 간주될지 결정합니다. 여러 glob 패턴을 검색하려면 패턴 사이에 공백을 추가하세요. 기본적으로 pytest는 `test`로 시작하는 모든 함수를 테스트로 간주합니다. 다음은 `_test`로 끝나는 테스트 함수와 메서드를 수집하는 예시입니다:

```
[pytest]
python_functions = *_test
```

이는 `unittest.TestCase`에서 파생된 클래스에 있는 메서드에는 영향을 미치지 않습니다. 이러한 테스트를 수집하는 데는 `unittest`의 자체 수집 프레임워크가 사용됩니다.

더 자세한 예시는 [명명 규칙 변경하기](https://docs.pytest.org/en/stable/example/pythoncollection.html#change-naming-conventions)를 참조하세요.

#### pythonpath (pythonpath)

파이썬 검색 경로에 추가되어야 하는 디렉토리 목록을 설정합니다. 디렉토리는 [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "(in Python v3.12)")의 앞부분에 추가됩니다. [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH "(in Python v3.12)") 환경 변수와 유사하게, 이 디렉토리들은 Python이 가져온 모듈을 찾는 곳에 포함됩니다. 경로는 [rootdir](https://docs.pytest.org/en/stable/reference/customize.html#rootdir) 디렉토리를 기준으로 상대적입니다. 디렉토리는 테스트 세션 동안 경로에 유지됩니다.

```
[pytest]
pythonpath = src1 src2
```

주의

`pythonpath`는 매우 초기에 발생하는 일부 가져오기에는 영향을 미치지 않습니다. 특히 `-p` 명령줄 옵션을 사용하여 로드되는 플러그인에는 영향을 미치지 않습니다.

#### required_plugins (required_plugins)

pytest를 실행하는 데 반드시 있어야 하는 플러그인의 공백으로 구분된 목록입니다. 플러그인은 이름 바로 뒤에 버전 지정자와 함께 또는 없이 나열할 수 있습니다. 다른 버전 지정자 사이의 공백은 허용되지 않습니다. 플러그인 중 하나라도 찾을 수 없으면 오류를 발생시킵니다.

```
[pytest]
required_plugins = pytest-django>=3.0.0,<4.0.0 pytest-html pytest-xdist>=1.0.0
```

#### testpaths (testpaths)

pytest를 [rootdir](https://docs.pytest.org/en/stable/reference/customize.html#rootdir) 디렉토리에서 실행할 때 명령줄에 특정 디렉토리, 파일 또는 테스트 ID가 주어지지 않은 경우 테스트를 검색해야 하는 디렉토리 목록을 설정합니다. 파일 시스템 경로는 재귀적인 `**` 패턴을 포함한 쉘 스타일 와일드카드를 사용할 수 있습니다.

모든 프로젝트 테스트가 알려진 위치에 있을 때 테스트 수집 속도를 높이고 의도하지 않은 테스트를 실수로 선택하지 않도록 하는 데 유용합니다.

```
[pytest]
testpaths = testing doc
```

이 구성은 다음을 실행하는 것과 같은 실질적인 효과를 가집니다:

```
pytest
```

다음을 실행하는 것과 동일한 효과:

```
pytest testing doc
```

#### tmp_path_retention_count (tmp_path_retention_count)

`tmp_path_retention_policy`에 따라 `tmp_path` 디렉토리를 몇 개의 세션 동안 유지해야 하는지 지정합니다.

```
[pytest]
tmp_path_retention_count = 3
```

기본값: `3`

#### tmp_path_retention_policy (tmp_path_retention_policy)

`tmp_path` 픽스처에 의해 생성된 디렉토리 중 어떤 것을 유지할지 테스트 결과에 따라 제어합니다.

> - `all`: 테스트 결과와 관계없이 모든 테스트에 대한 디렉토리를 유지합니다.
>     
> - `failed`: `error` 또는 `failed` 결과를 가진 테스트에 대해서만 디렉토리를 유지합니다.
>     
> - `none`: 테스트 결과와 관계없이 각 테스트가 끝날 때마다 항상 디렉토리를 제거합니다.
>     

```
[pytest]
tmp_path_retention_policy = "all"
```

기본값: `all`

#### usefixtures (usefixtures)

모든 테스트 함수에 적용될 픽스처 목록입니다. 이는 의미상 모든 테스트 함수에 `@pytest.mark.usefixtures` 마커를 적용하는 것과 같습니다.

```
[pytest]
usefixtures =
    clean_db
```

#### verbosity_assertions (verbosity_assertions)

애플리케이션 전체의 수준을 재정의하여 단언 관련 출력에 대해 특별히 상세도 수준을 설정합니다.

```
[pytest]
verbosity_assertions = 2
```

기본값은 애플리케이션 전체의 상세도 수준(명령줄 옵션 `-v`를 통해)입니다. "auto"라는 특별한 값을 사용하여 전역 상세도 수준을 명시적으로 사용할 수 있습니다.

#### verbosity_test_cases (verbosity_test_cases)

애플리케이션 전체의 수준을 재정의하여 테스트 케이스 실행 관련 출력에 대해 특별히 상세도 수준을 설정합니다.

```
[pytest]
verbosity_test_cases = 2
```

기본값은 애플리케이션 전체의 상세도 수준(명령줄 옵션 `-v`를 통해)입니다. "auto"라는 특별한 값을 사용하여 전역 상세도 수준을 명시적으로 사용할 수 있습니다.

#### xfail_strict (xfail_strict)

`True`로 설정하면 `@pytest.mark.xfail`로 표시된 테스트 중 실제로 성공한 테스트가 기본적으로 테스트 suite를 실패하게 만듭니다. 자세한 정보는 [strict 매개변수](https://docs.pytest.org/en/stable/how-to/skipping.html#xfail-strict-tutorial)를 참조하세요.

```
[pytest]
xfail_strict = True
```


### 구문 강조 테마 사용자 정의 (Syntax highlighting theme customization)
- pytest에서 사용되는 구문 강조 테마는 두 가지 환경 변수를 사용하여 사용자 정의할 수 있습니다:
	- [`PYTEST_THEME`](https://docs.pytest.org/en/stable/reference/reference.html#envvar-PYTEST_THEME)은 사용할 [pygment 스타일](https://pygments.org/docs/styles/)을 설정합니다.
	- [`PYTEST_THEME_MODE`](https://docs.pytest.org/en/stable/reference/reference.html#envvar-PYTEST_THEME_MODE)는 이 스타일을 _light_ 또는 _dark_로 설정합니다.


## 도구 통합

### pip로 패키지 설치하기 (Install package with pip)

- 개발을 위해서는 가상 환경을 위한 [`venv`](https://docs.python.org/3/library/venv.html#module-venv "(in Python v3.12)")와 애플리케이션 및 모든 종속성, 그리고 `pytest` 패키지 자체를 설치하기 위한 [pip](https://pip.pypa.io/en/stable/ "(in pip v24.1)")를 사용하는 것을 권장합니다. 이는 코드와 종속성이 시스템 Python 설치와 격리되도록 보장합니다.
- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/ "(in Python Packaging User Guide)")에 설명된 대로 저장소의 루트에 `pyproject.toml` 파일을 생성하세요. 첫 몇 줄은 다음과 같아야 합니다:

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "PACKAGENAME"
version = "PACKAGEVERSION"
```

- 여기서 `PACKAGENAME`과 `PACKAGEVERSION`은 각각 패키지의 이름과 버전입니다.
- 그런 다음 같은 디렉토리에서 다음 명령을 실행하여 "편집 가능" 모드로 패키지를 설치할 수 있습니다:

```
pip install -e .
```

- 이를 통해 소스 코드(테스트와 애플리케이션 모두)를 변경하고 원하는 대로 테스트를 다시 실행할 수 있습니다.

### Python 테스트 검색을 위한 규칙 (Conventions for Python test discovery)

- `pytest`는 다음과 같은 표준 테스트 검색을 구현합니다:
	- 인수가 지정되지 않은 경우 수집은 [`testpaths`](https://docs.pytest.org/en/stable/reference/reference.html#confval-testpaths)(구성된 경우) 또는 현재 디렉토리에서 시작됩니다. 또는 명령줄 인수를 디렉토리, 파일 이름 또는 노드 ID의 조합으로 사용할 수 있습니다.
	- [`norecursedirs`](https://docs.pytest.org/en/stable/reference/reference.html#confval-norecursedirs)와 일치하지 않는 한 디렉토리를 재귀적으로 탐색합니다.
	- 해당 디렉토리에서 `test_*.py` 또는 `*_test.py` 파일을 검색하여 [테스트 패키지 이름](https://docs.pytest.org/en/stable/explanation/goodpractices.html#test-package-name)으로 가져옵니다.
	- 해당 파일에서 테스트 항목을 수집합니다:
	    - 클래스 외부의 `test` 접두사가 붙은 테스트 함수 또는 메서드.
	    - `Test` 접두사가 붙은 테스트 클래스 내부의 `test` 접두사가 붙은 테스트 함수 또는 메서드(`__init__` 메서드 없음). `@staticmethod`와 `@classmethods`로 장식된 메서드도 고려됩니다.
- 테스트 검색을 사용자 정의하는 방법에 대한 예시는 [표준 (Python) 테스트 검색 변경하기](https://docs.pytest.org/en/stable/example/pythoncollection.html)를 참조하세요.
- Python 모듈 내에서 `pytest`는 표준 [unittest.TestCase](https://docs.pytest.org/en/stable/how-to/unittest.html#unittest-testcase) 서브클래싱 기법을 사용하여 테스트를 발견합니다.

### 테스트 레이아웃 선택하기 (Choosing a test layout)

- `pytest`는 두 가지 일반적인 테스트 레이아웃을 지원합니다:

#### 애플리케이션 코드 외부의 테스트 (Tests outside application code)

- 실제 애플리케이션 코드 외부의 추가 디렉토리에 테스트를 넣는 것은 기능 테스트가 많거나 다른 이유로 테스트를 실제 애플리케이션 코드와 분리하고 싶을 때 유용할 수 있습니다(종종 좋은 아이디어입니다):

```
pyproject.toml
src/
    mypkg/
        __init__.py
        app.py
        view.py
tests/
    test_app.py
    test_view.py
    …
```

이는 다음과 같은 이점이 있습니다:
- `pip install .`을 실행한 후 설치된 버전에 대해 테스트를 실행할 수 있습니다.
- `pip install --editable .`을 실행한 후 편집 가능한 설치로 로컬 복사본에 대해 테스트를 실행할 수 있습니다.
- 새 프로젝트의 경우 [importlib 모드](https://docs.pytest.org/en/stable/explanation/pythonpath.html#import-modes)를 사용하는 것을 권장합니다(자세한 설명은 [which-import-mode](https://docs.pytest.org/en/stable/explanation/goodpractices.html#which-import-mode) 참조). 이를 위해 `pyproject.toml`에 다음을 추가하세요:

```toml
[tool.pytest.ini_options]
addopts = [
    "--import-mode=importlib",
]
```

- 일반적으로, 특히 기본 가져오기 모드인 `prepend`를 사용하는 경우 `src` 레이아웃을 사용하는 것이 **강력히** 제안됩니다. 여기서 애플리케이션 루트 패키지는 루트의 하위 디렉토리에 있습니다. 즉, `mypkg` 대신 `src/mypkg/`에 있습니다.
- 이 레이아웃은 많은 일반적인 함정을 방지하고 많은 이점이 있습니다. 이에 대해서는 Ionel Cristian Mărieș의 이 훌륭한 [블로그 포스트](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure%3E)에서 더 자세히 설명되어 있습니다.

> [!NOTE]
> - 편집 가능한 설치를 사용하지 않고 위와 같이 `src` 레이아웃을 사용하는 경우, 로컬 복사본에 대해 직접 테스트를 실행하려면 모듈 파일에 대한 Python의 검색 경로를 확장해야 합니다. 임시 방법으로 `PYTHONPATH` 환경 변수를 설정하여 이를 수행할 수 있습니다:
> 
> ```
> PYTHONPATH=src pytest
> ```
> 
> 또는 [`pythonpath`](https://docs.pytest.org/en/stable/reference/reference.html#confval-pythonpath) 구성 변수를 사용하여 영구적으로 수행하고 `pyproject.toml`에 다음을 추가할 수 있습니다:
> 
> ```toml
> [tool.pytest.ini_options]
> pythonpath = "src"
> ```

> [!NOTE]
> - 편집 가능한 설치를 사용하지 않고 `src` 레이아웃을 사용하지 않는 경우(`mypkg`가 루트 디렉토리에 직접 있는 경우) Python이 기본적으로 현재 디렉토리를 `sys.path`에 넣어 패키지를 가져오고 `python -m pytest`를 실행하여 로컬 복사본에 대해 직접 테스트를 실행할 수 있다는 사실에 의존할 수 있습니다.
> 
> - `pytest`와 `python -m pytest`를 호출하는 것의 차이점에 대한 자세한 내용은 [Invoking pytest versus python -m pytest](https://docs.pytest.org/en/stable/explanation/pythonpath.html#pytest-vs-python-m-pytest)를 참조하세요.

### 애플리케이션 코드의 일부로서의 테스트 (Tests as part of application code)

- 테스트 디렉토리를 애플리케이션 패키지에 인라인으로 포함하는 것은 테스트와 애플리케이션 모듈 사이에 직접적인 관계가 있고 애플리케이션과 함께 배포하고 싶을 때 유용합니다:

```
pyproject.toml
[src/]mypkg/
    __init__.py
    app.py
    view.py
    tests/
        __init__.py
        test_app.py
        test_view.py
        …
```

- 이 방식에서는 `--pyargs` 옵션을 사용하여 쉽게 테스트를 실행할 수 있습니다:

```
pytest --pyargs mypkg
```

- `pytest`는 `mypkg`가 설치된 위치를 발견하고 거기에서 테스트를 수집합니다.
- 이 레이아웃은 이전 섹션에서 언급한 `src` 레이아웃과 함께 사용할 수도 있습니다.


> [!NOTE]
> - 애플리케이션에 네임스페이스 패키지(PEP420)를 사용할 수 있지만 pytest는 여전히 파일의 존재를 기반으로 [테스트 패키지 이름](https://docs.pytest.org/en/stable/explanation/goodpractices.html#test-package-name) 검색을 수행합니다. 위에서 권장하는 두 가지 파일 시스템 레이아웃 중 하나를 사용하지만 디렉토리에서 `__init__.py` 파일을 제거하면 잘 작동해야 합니다. 그러나 "인라인 테스트"의 경우 애플리케이션 코드에 접근하기 위해 절대 가져오기를 사용해야 합니다.


> [!NOTE]
> - `prepend`와 `append` 가져오기 모드에서 pytest가 파일 시스템을 재귀적으로 탐색하는 동안 테스트 파일을 발견하면 다음과 같이 가져오기 이름을 결정합니다 `"a/b/test_module.py"`:
> 	- `basedir` 결정: 이는 `__init__.py`를 포함하지 않는 첫 번째 "상향"(루트를 향한) 디렉토리입니다. 예를 들어 `a`와 `b` 모두 `__init__.py` 파일을 포함하고 있다면 `a`의 상위 디렉토리가 `basedir`가 됩니다.
> 	- 테스트 모듈을 정규화된 가져오기 이름으로 가져올 수 있도록 `sys.path.insert(0, basedir)`를 수행합니다.
> 	- 경로 구분자를 "." 문자로 변환하여 결정된 경로로 `import a.b.test_module`을 수행합니다. 이는 디렉토리와 파일 이름이 가져오기 이름에 직접 매핑되는 규칙을 따라야 함을 의미합니다.
> - 이 다소 발전된 가져오기 기술의 이유는 더 큰 프로젝트에서 여러 테스트 모듈이 서로 가져올 수 있으므로 정규화된 가져오기 이름을 도출하는 것이 테스트 모듈이 두 번 가져와지는 것과 같은 놀라움을 피하는 데 도움이 되기 때문입니다.
> - `--import-mode=importlib`를 사용하면 pytest가 `sys.path`나 `sys.modules`를 변경할 필요가 없어 훨씬 덜 복잡하고 놀라운 일이 적습니다.


#### 임포트 모드 선택 (Choosing an import mode)
- 역사적인 이유로, pytest는 새로운 프로젝트에 권장하는 `importlib` 임포트 모드 대신 `prepend` 임포트 모드를 기본값으로 사용합니다. 그 이유는 `prepend` 모드의 작동 방식에 있습니다:
- `pytest`는 전체 패키지 이름을 유추할 패키지가 없기 때문에, 테스트 파일을 최상위 모듈로 임포트합니다. 첫 번째 예시([src 레이아웃](https://docs.pytest.org/en/stable/explanation/goodpractices.html#src-layout))의 테스트 파일은 `tests/`를 `sys.path`에 추가하여 `test_app`과 `test_view`라는 최상위 모듈로 임포트됩니다.
- 이는 `importlib` 임포트 모드와 비교했을 때 단점이 있습니다: 테스트 파일의 이름이 **고유해야 합니다**.
- 같은 이름의 테스트 모듈이 필요한 경우, 해결 방법으로 `tests` 폴더와 하위 폴더에 `__init__.py` 파일을 추가하여 패키지로 변경할 수 있습니다:

```
pyproject.toml
mypkg/
    …
tests/
    __init__.py
    foo/
        __init__.py
        test_view.py
    bar/
        __init__.py
        test_view.py
```

- 이제 pytest는 모듈을 `tests.foo.test_view`와 `tests.bar.test_view`로 로드하여 같은 이름의 모듈을 가질 수 있게 됩니다. 하지만 이는 미묘한 문제를 야기합니다: `tests` 디렉토리에서 테스트 모듈을 로드하기 위해 pytest는 저장소의 루트를 `sys.path`에 추가하는데, 이로 인해 `mypkg`도 임포트 가능해지는 부작용이 생깁니다.
- 이는 [tox](https://docs.pytest.org/en/stable/explanation/goodpractices.html#tox)와 같은 도구를 사용하여 가상 환경에서 패키지를 테스트할 때 문제가 됩니다. 왜냐하면 저장소의 로컬 코드가 아닌 *설치된* 버전의 패키지를 테스트하고 싶기 때문입니다.
- `importlib` 임포트 모드는 테스트 모듈을 임포트할 때 `sys.path`를 변경하지 않기 때문에 위의 단점이 없습니다.

### tox

- 작업을 마치고 실제 패키지가 모든 테스트를 통과하는지 확인하고 싶다면 가상 환경 테스트 자동화 도구인 [tox](https://tox.wiki/en/stable/index.html)를 살펴볼 수 있습니다. `tox`는 사전 정의된 종속성으로 가상 환경을 설정하고 사전 구성된 테스트 명령을 옵션과 함께 실행하도록 도와줍니다. 소스 코드 체크아웃이 아닌 설치된 패키지에 대해 테스트를 실행하여 패키징 문제를 감지하는 데 도움이 됩니다.

### setuptools를 통해 실행하지 마세요 (Do not run via setuptools)

- setuptools와의 통합은 **권장되지 않습니다**. 즉, `python setup.py test`나 `pytest-runner`를 사용해서는 안 되며, 향후 작동이 중단될 수 있습니다.
- 이는 setuptools의 deprecated된 기능에 의존하고 pip의 보안 메커니즘을 깨는 기능에 의존하기 때문에 deprecated되었습니다. 예를 들어 'setup_requires'와 'tests_require'는 `pip --require-hashes`를 우회합니다. 자세한 정보와 마이그레이션 지침은 [pytest-runner 공지](https://github.com/pytest-dev/pytest-runner#deprecation-notice)를 참조하세요. [pypa/setuptools#1684](https://github.com/pypa/setuptools/issues/1684)도 참조하세요.
- setuptools는 [test 명령을 제거할 예정](https://github.com/pypa/setuptools/issues/931)입니다.

### flake8-pytest-style로 확인하기 (Checking with flake8-pytest-style)
- 프로젝트에서 pytest가 올바르게 사용되고 있는지 확인하기 위해 [flake8-pytest-style](https://github.com/m-burst/flake8-pytest-style) flake8 플러그인을 사용하는 것이 도움이 될 수 있습니다.
- flake8-pytest-style는 pytest 코드에서 흔한 실수와 코딩 스타일 위반을 확인합니다. 예를 들어 fixture의 잘못된 사용, 테스트 함수 이름, 마커 등을 확인합니다. 이 플러그인을 사용하면 개발 과정 초기에 이러한 오류를 잡아내고 pytest 코드가 일관되고 유지보수하기 쉽도록 할 수 있습니다.
- flake8-pytest-style가 감지하는 lint의 목록은 [PyPI 페이지](https://pypi.org/project/flake8-pytest-style/)에서 확인할 수 있습니다.

> [!NOTE]
> - flake8-pytest-style는 공식 pytest 프로젝트가 아닙니다. 일부 규칙은 `@pytest.fixture` 대신 `@pytest.fixture()`를 사용하는 것과 같은 특정 스타일 선택을 강제하지만, 선호하는 스타일에 맞게 플러그인을 구성할 수 있습니다.

다음은 요청하신 대로 번역한 내용입니다:

## pytest 임포트 메커니즘과 `sys.path`/`PYTHONPATH` (pytest import mechanisms and `sys.path`/`PYTHONPATH`)

### 임포트 모드 (Import modes)
- pytest는 테스트 모듈과 `conftest.py` 파일을 실행을 위해 임포트해야 하는 테스팅 프레임워크입니다.
- Python에서 파일을 임포트하는 것은 간단하지 않은 과정이므로, 임포트 과정의 일부 측면은 `--import-mode` 커맨드라인 플래그를 통해 제어할 수 있습니다. 이 플래그는 다음과 같은 값을 가질 수 있습니다:
- `prepend` (기본값): 
  
  각 모듈을 포함하는 디렉토리 경로가 아직 없다면 [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "(in Python v3.12)")의 시작 부분에 삽입된 다음, [`importlib.import_module`](https://docs.python.org/3/library/importlib.html#importlib.import_module "(in Python v3.12)") 함수를 사용하여 임포트됩니다.
  
  테스트를 포함하는 디렉토리에 `__init__.py` 파일을 추가하여 테스트 모듈을 패키지로 구성하는 것이 매우 권장됩니다. 이렇게 하면 테스트가 적절한 Python 패키지의 일부가 되어 pytest가 전체 이름을 해결할 수 있습니다(예: `tests.core` 패키지 내의 `test_core.py`에 대해 `tests.core.test_core`).
  
  테스트 디렉토리 트리가 패키지로 구성되어 있지 않은 경우, 각 테스트 파일은 다른 테스트 파일과 비교하여 고유한 이름을 가져야 합니다. 그렇지 않으면 pytest가 동일한 이름의 두 테스트를 발견했을 때 오류를 발생시킵니다.
  
  이는 Python 2가 여전히 지원되던 시절부터 있던 고전적인 메커니즘입니다.

- `append`: 
  
  각 모듈을 포함하는 디렉토리가 아직 없다면 [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "(in Python v3.12)")의 끝에 추가된 다음, [`importlib.import_module`](https://docs.python.org/3/library/importlib.html#importlib.import_module "(in Python v3.12)")로 임포트됩니다.
  
  이를 통해 사용자는 테스트 중인 패키지가 동일한 임포트 루트를 가지고 있더라도 설치된 버전의 패키지에 대해 테스트 모듈을 실행할 수 있습니다. 예를 들어:

```
testing/__init__.py
testing/test_pkg_under_test.py
pkg_under_test/
```

`--import-mode=append`를 사용하면 테스트가 설치된 버전의 `pkg_under_test`에 대해 실행되는 반면, `prepend`를 사용하면 로컬 버전을 선택합니다. 이러한 혼란 때문에 우리는 [src-layouts](https://docs.pytest.org/en/stable/explanation/goodpractices.html#src-layout)를 사용할 것을 권장합니다.

`prepend`와 마찬가지로, 테스트 디렉토리 트리가 패키지로 구성되어 있지 않을 때 테스트 모듈 이름이 고유해야 합니다. 왜냐하면 임포트 후 모듈이 [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "(in Python v3.12)")에 들어가기 때문입니다.

- `importlib`: 
  
  이 모드는 [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "(in Python v3.12)")에서 제공하는 더 세밀한 제어 메커니즘을 사용하여 [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "(in Python v3.12)")를 변경하지 않고 테스트 모듈을 임포트합니다.
  
  이 모드의 장점:
    - pytest는 [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "(in Python v3.12)")를 전혀 변경하지 않습니다.
    - 테스트 모듈 이름이 고유할 필요가 없습니다 - pytest는 `rootdir`를 기반으로 자동으로 고유한 이름을 생성합니다.
    단점:
    - 테스트 모듈끼리 서로 임포트할 수 없습니다.
    - 테스트 디렉토리에 있는 테스트 유틸리티 모듈(예: 테스트 관련 함수/클래스를 포함하는 `tests.helpers` 모듈)을 임포트할 수 없습니다. 이 경우 테스트 유틸리티 모듈을 애플리케이션/라이브러리 코드와 함께 배치하는 것이 권장됩니다(예: `app.testing.helpers`).
        중요: "테스트 유틸리티 모듈"이란 다른 테스트에서 직접 임포트하는 함수/클래스를 의미합니다. 이는 자동으로 발견되는 `conftest.py` 파일에 배치되어야 하는 fixture를 포함하지 않습니다.

    작동 방식:
    1. 주어진 모듈 경로(예: `tests/core/test_models.py`)에 대해 `tests.core.test_models`와 같은 정규 이름을 도출하고 임포트를 시도합니다.

        비 테스트 모듈의 경우, [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "(in Python v3.12)")를 통해 접근 가능하다면 이 방식이 작동합니다. 예를 들어, `.env/lib/site-packages/app/core.py`는 `app.core`로 임포트 가능합니다. 이는 플러그인이 비 테스트 모듈을 임포트할 때 발생합니다(예: doctesting).

        이 단계가 성공하면 모듈이 반환됩니다.

        테스트 모듈의 경우, [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "(in Python v3.12)")에서 접근할 수 없다면 이 단계는 실패합니다.

    2. 이전 단계가 실패하면, `importlib` 기능을 사용하여 모듈을 직접 임포트합니다. 이를 통해 [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "(in Python v3.12)")를 변경하지 않고 임포트할 수 있습니다.

        Python은 모듈이 [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "(in Python v3.12)")에서도 사용 가능해야 하므로, pytest는 `rootdir`로부터의 상대 위치를 기반으로 고유한 이름을 도출하고 모듈을 [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "(in Python v3.12)")에 추가합니다.

        예를 들어, `tests/core/test_models.py`는 결국 `tests.core.test_models` 모듈로 임포트됩니다.

> [!NOTE]
> - 처음에는 향후 릴리스에서 `importlib`를 기본값으로 만들 계획이었지만, 이제는 그것이 자체적인 단점 세트를 가지고 있다는 것이 분명해졌으므로 예측 가능한 미래에는 기본값이 `prepend`로 유지될 것입니다.

> [!NOTE]
> - 기본적으로 pytest는 네임스페이스 패키지를 자동으로 해결하려고 시도하지 않지만, [`consider_namespace_packages`](https://docs.pytest.org/en/stable/reference/reference.html#confval-consider_namespace_packages) 설정 변수를 통해 변경할 수 있습니다.

> [!NOTE]
> - [`pythonpath`](https://docs.pytest.org/en/stable/reference/reference.html#confval-pythonpath) 설정 변수.
> - [`consider_namespace_packages`](https://docs.pytest.org/en/stable/reference/reference.html#confval-consider_namespace_packages) 설정 변수
> - [테스트 레이아웃 선택하기](https://docs.pytest.org/en/stable/explanation/goodpractices.html#test-layout).

### `prepend`와 `append` 임포트 모드 시나리오 (prepend and append import modes scenarios)

- 다음은 `prepend` 또는 `append` 임포트 모드를 사용할 때 pytest가 테스트 모듈이나 `conftest.py` 파일을 임포트하기 위해 [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "(in Python v3.12)")를 변경해야 하는 시나리오 목록과 사용자가 이로 인해 겪을 수 있는 문제입니다.

#### 패키지 내부의 테스트 모듈 / `conftest.py` 파일 (Test modules / conftest.py files inside packages)
다음과 같은 파일 및 디렉토리 레이아웃을 고려해보세요:

```
root/
|foo/
   |__init__.py
   |conftest.py
   |bar/
      |__init__.py
      |tests/
         |__init__.py
         |test_foo.py
```

다음을 실행할 때:

```
pytest root/
```

- pytest는 `foo/bar/tests/test_foo.py`를 찾고 같은 폴더에 `__init__.py` 파일이 있기 때문에 이것이 패키지의 일부임을 인식합니다. 그런 다음 패키지 루트(이 경우 `foo/`)를 찾기 위해 `__init__.py` 파일을 여전히 포함하는 마지막 폴더를 찾을 때까지 위로 검색합니다. 모듈을 로드하기 위해 `root/`를 [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "(in Python v3.12)")의 앞부분에 삽입하여(아직 없는 경우) `test_foo.py`를 _모듈_ `foo.bar.tests.test_foo`로 로드합니다.
- 같은 로직이 `conftest.py` 파일에도 적용됩니다: `foo.conftest` 모듈로 임포트됩니다.
- 테스트가 패키지에 있을 때 전체 패키지 이름을 보존하는 것은 문제를 방지하고 테스트 모듈이 중복된 이름을 가질 수 있도록 하는 데 중요합니다. 이는 [Python 테스트 발견을 위한 규칙](https://docs.pytest.org/en/stable/explanation/goodpractices.html#test-discovery)에서도 자세히 논의됩니다.

#### 독립형 테스트 모듈 / `conftest.py` 파일 (Standalone test modules / conftest.py files)
다음과 같은 파일 및 디렉토리 레이아웃을 고려해보세요:

```
root/
|foo/
   |conftest.py
   |bar/
      |tests/
         |test_foo.py
```

다음을 실행할 때:

```
pytest root/
```

- pytest는 `foo/bar/tests/test_foo.py`를 찾고 같은 폴더에 `__init__.py` 파일이 없기 때문에 이것이 패키지의 일부가 아님을 인식합니다. 그런 다음 `test_foo.py`를 _모듈_ `test_foo`로 임포트하기 위해 `root/foo/bar/tests`를 [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "(in Python v3.12)")에 추가합니다. `conftest.py` 파일에 대해서도 `root/foo`를 [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "(in Python v3.12)")에 추가하여 `conftest`로 임포트하는 것과 동일한 작업을 수행합니다.
- 이러한 이유로 이 레이아웃은 동일한 이름의 테스트 모듈을 가질 수 없습니다. 모두 글로벌 임포트 네임스페이스에서 임포트되기 때문입니다.
- 이 내용도 [Python 테스트 발견을 위한 규칙](https://docs.pytest.org/en/stable/explanation/goodpractices.html#test-discovery)에서 자세히 논의됩니다.

### `pytest` 호출과 `python -m pytest` 호출 비교 (Invoking `pytest` versus `python -m pytest`)

- `pytest […]`로 pytest를 실행하는 것과 `python -m pytest […]`로 실행하는 것은 거의 동일한 동작을 보입니다. 단, 후자의 경우 현재 디렉토리를 [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "(in Python v3.12)")에 추가하는데, 이는 표준 `python` 동작입니다.
- 다음도 참조하세요: [python -m pytest를 통해 pytest 호출하기](https://docs.pytest.org/en/stable/how-to/usage.html#invoke-python).

## 파일 입력
[pytest-datadir · PyPI](https://pypi.org/project/pytest-datadir/)
[pytest-datafiles · PyPI](https://pypi.org/project/pytest-datafiles/)



---
## 예제
- [pytest를 사용한 Python 실패 보고서 데모](https://docs.pytest.org/en/stable/example/reportingdemo.html)
- [기본 패턴 및 예제](https://docs.pytest.org/en/stable/example/simple.html)
    - [명령줄 옵션 기본값 변경 방법](https://docs.pytest.org/en/stable/example/simple.html#how-to-change-command-line-options-defaults)
    - [명령줄 옵션에 따라 테스트 함수에 다른 값 전달하기](https://docs.pytest.org/en/stable/example/simple.html#pass-different-values-to-a-test-function-depending-on-command-line-options)
    - [동적으로 명령줄 옵션 추가하기](https://docs.pytest.org/en/stable/example/simple.html#dynamically-adding-command-line-options)
    - [명령줄 옵션에 따라 테스트 건너뛰기 제어하기](https://docs.pytest.org/en/stable/example/simple.html#control-skipping-of-tests-according-to-command-line-option)
    - [잘 통합된 어설션 헬퍼 작성하기](https://docs.pytest.org/en/stable/example/simple.html#writing-well-integrated-assertion-helpers)
    - [pytest 실행 내에서 실행 중인지 감지하기](https://docs.pytest.org/en/stable/example/simple.html#detect-if-running-from-within-a-pytest-run)
    - [테스트 보고서 헤더에 정보 추가하기](https://docs.pytest.org/en/stable/example/simple.html#adding-info-to-test-report-header)
    - [테스트 지속 시간 프로파일링](https://docs.pytest.org/en/stable/example/simple.html#profiling-test-duration)
    - [증분 테스팅 - 테스트 단계](https://docs.pytest.org/en/stable/example/simple.html#incremental-testing-test-steps)
    - [패키지/디렉토리 수준 픽스처 (설정)](https://docs.pytest.org/en/stable/example/simple.html#package-directory-level-fixtures-setups)
    - [테스트 보고서/실패 후처리](https://docs.pytest.org/en/stable/example/simple.html#post-process-test-reports-failures)
    - [픽스처에서 테스트 결과 정보 사용 가능하게 만들기](https://docs.pytest.org/en/stable/example/simple.html#making-test-result-information-available-in-fixtures)
    - [`PYTEST_CURRENT_TEST` 환경 변수](https://docs.pytest.org/en/stable/example/simple.html#pytest-current-test-environment-variable)
    - [pytest 프리징](https://docs.pytest.org/en/stable/example/simple.html#freezing-pytest)
- [테스트 매개변수화](https://docs.pytest.org/en/stable/example/parametrize.html)
    - [명령줄에 따라 매개변수 조합 생성하기](https://docs.pytest.org/en/stable/example/parametrize.html#generating-parameters-combinations-depending-on-command-line)
    - [테스트 ID에 대한 다양한 옵션](https://docs.pytest.org/en/stable/example/parametrize.html#different-options-for-test-ids)
    - ["testscenarios"의 빠른 이식](https://docs.pytest.org/en/stable/example/parametrize.html#a-quick-port-of-testscenarios)
    - [매개변수화된 리소스의 설정 지연하기](https://docs.pytest.org/en/stable/example/parametrize.html#deferring-the-setup-of-parametrized-resources)
    - [간접 매개변수화](https://docs.pytest.org/en/stable/example/parametrize.html#indirect-parametrization)
    - [특정 인수에 간접 적용하기](https://docs.pytest.org/en/stable/example/parametrize.html#apply-indirect-on-particular-arguments)
    - [클래스별 구성을 통한 테스트 메서드 매개변수화](https://docs.pytest.org/en/stable/example/parametrize.html#parametrizing-test-methods-through-per-class-configuration)
    - [여러 픽스처를 사용한 매개변수화](https://docs.pytest.org/en/stable/example/parametrize.html#parametrization-with-multiple-fixtures)
    - [선택적 구현/임포트의 매개변수화](https://docs.pytest.org/en/stable/example/parametrize.html#parametrization-of-optional-implementations-imports)
    - [개별 매개변수화된 테스트에 대한 마크 또는 테스트 ID 설정](https://docs.pytest.org/en/stable/example/parametrize.html#set-marks-or-test-id-for-individual-parametrized-test)
    - [조건부 예외 발생 매개변수화](https://docs.pytest.org/en/stable/example/parametrize.html#parametrizing-conditional-raising)
- [사용자 정의 마커 작업하기](https://docs.pytest.org/en/stable/example/markers.html)
    - [테스트 함수 마킹 및 실행을 위한 선택](https://docs.pytest.org/en/stable/example/markers.html#marking-test-functions-and-selecting-them-for-a-run)
    - [노드 ID를 기반으로 테스트 선택하기](https://docs.pytest.org/en/stable/example/markers.html#selecting-tests-based-on-their-node-id)
    - [`-k expr`를 사용하여 이름 기반으로 테스트 선택하기](https://docs.pytest.org/en/stable/example/markers.html#using-k-expr-to-select-tests-based-on-their-name)
    - [마커 등록하기](https://docs.pytest.org/en/stable/example/markers.html#registering-markers)
    - [전체 클래스 또는 모듈 마킹하기](https://docs.pytest.org/en/stable/example/markers.html#marking-whole-classes-or-modules)
    - [매개변수화 사용 시 개별 테스트 마킹하기](https://docs.pytest.org/en/stable/example/markers.html#marking-individual-tests-when-using-parametrize)
    - [테스트 실행을 제어하기 위한 사용자 정의 마커 및 명령줄 옵션](https://docs.pytest.org/en/stable/example/markers.html#custom-marker-and-command-line-option-to-control-test-runs)
    - [사용자 정의 마커에 호출 가능한 객체 전달하기](https://docs.pytest.org/en/stable/example/markers.html#passing-a-callable-to-custom-markers)
    - [여러 곳에서 설정된 마커 읽기](https://docs.pytest.org/en/stable/example/markers.html#reading-markers-which-were-set-from-multiple-places)
    - [pytest를 사용한 플랫폼 특정 테스트 마킹](https://docs.pytest.org/en/stable/example/markers.html#marking-platform-specific-tests-with-pytest)
    - [테스트 이름을 기반으로 자동으로 마커 추가하기](https://docs.pytest.org/en/stable/example/markers.html#automatically-adding-markers-based-on-test-names)
- [수집된 모든 테스트를 볼 수 있는 세션 픽스처](https://docs.pytest.org/en/stable/example/special.html)
- [표준 (Python) 테스트 검색 변경하기](https://docs.pytest.org/en/stable/example/pythoncollection.html)
    - [테스트 수집 중 경로 무시하기](https://docs.pytest.org/en/stable/example/pythoncollection.html#ignore-paths-during-test-collection)
    - [테스트 수집 중 테스트 선택 해제하기](https://docs.pytest.org/en/stable/example/pythoncollection.html#deselect-tests-during-test-collection)
    - [명령줄에서 지정된 중복 경로 유지하기](https://docs.pytest.org/en/stable/example/pythoncollection.html#keeping-duplicate-paths-specified-from-command-line)
    - [디렉토리 재귀 변경하기](https://docs.pytest.org/en/stable/example/pythoncollection.html#changing-directory-recursion)
    - [명명 규칙 변경하기](https://docs.pytest.org/en/stable/example/pythoncollection.html#changing-naming-conventions)
    - [명령줄 인수를 Python 패키지로 해석하기](https://docs.pytest.org/en/stable/example/pythoncollection.html#interpreting-cmdline-arguments-as-python-packages)
    - [수집된 내용 알아내기](https://docs.pytest.org/en/stable/example/pythoncollection.html#finding-out-what-is-collected)
    - [테스트 수집 사용자 정의하기](https://docs.pytest.org/en/stable/example/pythoncollection.html#customizing-test-collection)
- [비 Python 테스트 작업하기](https://docs.pytest.org/en/stable/example/nonpython.html)
    - [Yaml 파일에서 테스트를 지정하는 기본 예제](https://docs.pytest.org/en/stable/example/nonpython.html#a-basic-example-for-specifying-tests-in-yaml-files)
- [사용자 정의 디렉토리 수집기 사용하기](https://docs.pytest.org/en/stable/example/customdirectory.html)
    - [디렉토리 매니페스트 파일의 기본 예제](https://docs.pytest.org/en/stable/example/customdirectory.html#a-basic-example-for-a-directory-manifest-file)

## 참조
- [모듈과 환경을 몽키패치/모킹하는 방법](https://docs.pytest.org/en/stable/how-to/monkeypatch.html)
- [doctest를 실행하는 방법](https://docs.pytest.org/en/stable/how-to/doctest.html)
- [실패한 테스트를 다시 실행하고 테스트 실행 간 상태를 유지하는 방법](https://docs.pytest.org/en/stable/how-to/cache.html)
### 테스트 출력 및 결과
- [테스트 실패를 처리하는 방법](https://docs.pytest.org/en/stable/how-to/failures.html)
- [pytest의 출력 관리하기](https://docs.pytest.org/en/stable/how-to/output.html)
- [로깅을 관리하는 방법](https://docs.pytest.org/en/stable/how-to/logging.html)
- [stdout/stderr 출력을 캡처하는 방법](https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html)
- [경고를 캡처하는 방법](https://docs.pytest.org/en/stable/how-to/capture-warnings.html)
- [성공할 수 없는 테스트를 처리하기 위해 skip과 xfail을 사용하는 방법](https://docs.pytest.org/en/stable/how-to/skipping.html)
### 플러그인
- [플러그인을 설치하고 사용하는 방법](https://docs.pytest.org/en/stable/how-to/plugins.html)
- [플러그인 작성하기](https://docs.pytest.org/en/stable/how-to/writing_plugins.html)
- [훅 함수 작성하기](https://docs.pytest.org/en/stable/how-to/writing_hook_functions.html)
- [Pytest 플러그인 목록 - pytest 문서](https://docs.pytest.org/en/stable/reference/plugin_list.html#plugin-list)
### pytest와 다른 테스트 시스템
- [기존 테스트 스위트에서 pytest를 사용하는 방법](https://docs.pytest.org/en/stable/how-to/existingtestsuite.html)
- [pytest에서 `unittest` 기반 테스트를 사용하는 방법](https://docs.pytest.org/en/stable/how-to/unittest.html)
- [xunit 스타일 설정을 구현하는 방법](https://docs.pytest.org/en/stable/how-to/xunit_setup.html)
### pytest 개발 환경
- [bash 자동 완성을 설정하는 방법](https://docs.pytest.org/en/stable/how-to/bash-completion.html)

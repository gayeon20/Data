---
title: "[Python] 테스트 (Test)"
excerpt: Python의 코드 테스트에 대한 문서
categories:
  - Python
tags:
  - Python
  - Python-Library
  - Test
last_modified_at: 2024-04-11T15:10:56+09:00
link: 
상위 항목: "[[python_development|파이썬 개발 (Python Development)]]"
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

**하위 항목**
- [[python_test_unittest|Unittest]]
- [[pytest_home|파이테스트 (Pytest)]]
- [[python_tox|Tox]]

---

믿을 수 있는 코드라고 말하려면 역시 테스트 케이스가 잘 작성된 코드여야겠죠? 😊 핑퐁팀 안에서도 좋은 테스트 케이스를 작성하기 위해 노력하고 있지만, 이 글에서는 어떤 식으로 사용하는지만 간단하게 언급해보겠습니다.

Python 코드를 테스트하기 위한 도구로 pytest 와 unittest 정도를 들 수 있습니다. unittest 는 Python 의 기본 라이브러리이고, 테스트 코드를 작성하기 충분한 기능을 제공합니다. fixture 등의 기능도 pytest 보다 훨씬 Pythonic 하게 사용이 가능합니다. 하지만 pytest 는 테스트 코드 자체를 간결하게 만들고 Parameterized Test 도 훨씬 간편하도록 해줍니다. 더군다나 다른 플러그인을 붙이기에도 간편하죠.

unittest 나 pytest 중 하나만을 사용하기로 합의하진 않았지만, 핑퐁 팀 내부에서는 간결함 때문에 자연스럽게 pytest 를 주로 사용하는 중입니다. 핑퐁팀은 pytest 를 어떻게 사용하는지 더 자세하게 알려드릴게요!

## CI 에서의 pytest

CI 에서 실행하는 명령은 어떤 행동이 일어났는지 정확히 알아야 하기 때문에 기본적으로 Verbose 옵션 (`-v`) 을 주고 있습니다. 테스트 실행도 예외가 아니죠.

또한 어떤 테스트를 건너뛰었고 어떤 테스트가 실패했는지 한눈에 보기 위해 마지막에 Summary 를 출력하도록 옵션 (`-ra`) 을 주고 있습니다. 이 옵션의 의미는 pytest 문서의 [Detailed summary report](https://docs.pytest.org/en/latest/usage.html#detailed-summary-report) 를 살펴보시면 좋습니다.

하지만, 테스트가 실패했을 때 어떤 상황에 실패했는지 정확히 모른다면, 실패한 이유과 실패하기까지의 과정을 명확히 알 수 없습니다. 그래서 로컬 변수들을 출력하도록 옵션 (`-l`) 을 주어 사용하고 있습니다. 이 옵션 역시 pytest 문서의 [Modifying Python traceback printing](https://docs.pytest.org/en/latest/usage.html#modifying-python-traceback-printing) 을 살펴보시는 것을 추천드립니다.

## Code Coverage

Code Coverage 는 테스트 코드 작성할 때 참고하기 좋은 지표 중 하나입니다. 어떤 코드에 더 테스트가 필요한지, 혹은 특정 Branch 에 있는 코드에 테스트가 충분히 이루어졌는지 확인하기 위한 지표가 될 수 있습니다. 그렇기에 핑퐁팀도 Code Coverage 를 최대한 측정하려고 하고 있으며, 이를 위해 사용하는 것이 pytest-cov 입니다. pytest-cov 와 함께 pytest 를 실행하게 되면 Coverage Report 가 함께 생성됩니다. 해당 Report 가 Coveralls, CodeCov 와 같은 서비스에 업로드되면 어떤 코드를 더 테스트해야 하는지, 최근 Code Coverage 추이는 어떤지 등을 웹 상에서 손쉽게 확인할 수 있습니다.

## 병렬 실행

테스트 케이스가 많아지는 경우 병렬 실행이 필요해지는 시점이 있습니다. 이럴 때 pytest 를 쉽게 병렬화할 수 있는 방법은 pytest-xdist 플러그인을 사용하는 것입니다. CPU 코어 개수에 알맞게 Worker 수를 설정하고 나면 자동으로 병렬로 실행되게 됩니다. 하지만, 전체 실행 시간 자체가 그렇게 길지 않거나 테스트가 독립적이지 않으면 오버헤드 때문에 오히려 실행 시간이 길어지기도 하니 적절한 상황에만 사용하는 것을 추천드립니다.

## Python 버전별 실행

때로는 다양한 Python 버전에서 사용할 도구를 작성해야 하는 상황이 있습니다. 핑퐁팀은 그러한 도구를 테스트하기 위해 tox 를 사용하고 있습니다. tox 는 `tox.ini` 파일 하나를 추가하는 것만으로 손쉽게 여러 가지 버전의 Python 에서 테스트를 하도록 해주죠. 심지어 대부분의 경우에는 기존 테스트 과정을 고칠 필요도 없는 것이 장점입니다.

---

## 예제

### 1) DeepL: Unittest vs Pytest

#### (1) Unittest

```python
import unittest

from core.helpers.deepl_translate import translate


class TestDeepLTranslate(unittest.TestCase):
    def test_translate_hello_to_korean(self):
        text = "Hello"
        target_lang = "ko"
        expected_result = "안녕하세요"

        actual_result = translate(text=text, target_lang=target_lang)

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
```

**설명:**

- `TestDeepLTranslate` 클래스는 `unittest.TestCase` 클래스를 상속받는 테스트 클래스입니다.
- `test_translate_hello_to_korean` 메서드는 `translate` 함수를 테스트하는 테스트 메서드입니다.
- 테스트 메서드는 다음과 같은 작업을 수행합니다.
    - `text` 와 `target_lang` 변수에 테스트에 필요한 값을 할당합니다.
    - `translate` 함수를 호출하여 번역 결과를 얻습니다.
    - 예상 결과와 실제 결과를 비교합니다.
    - 결과가 일치하지 않으면 테스트 실패

**테스트 실행:**

```
python test_deepl_translate.py
```

**테스트 결과:**

```
test_translate_hello_to_korean (test_deepl_translate.TestDeepLTranslate) ... ok

======================================================================
1 tests in 1 module, 0 failures, 0 errors, 0 skipped
======================================================================
```

**참고:**

- 테스트 코드는 예시이며, 필요에 따라 추가 테스트 케이스를 작성해야 합니다.
- 테스트 코드를 실행하기 전에 DeepL API 키가 올바르게 설정되었는지 확인해야 합니다.

#### (2) Pytest

```python
import pytest

from core.helpers.deepl_translate import translate


@pytest.mark.parametrize("text, target_lang, expected_result", [
    ("Hello", "ko", "안녕하세요"),
    ("How are you?", "ko", "잘 지내세요?"),
    ("Thank you", "ko", "감사합니다"),
])
def test_translate(text, target_lang, expected_result):
    actual_result = translate(text=text, target_lang=target_lang)

    assert actual_result == expected_result
```

**설명:**

- `pytest.mark.parametrize` 데코레이터를 사용하여 여러 테스트 케이스를 정의합니다.
- 각 테스트 케이스는 다음 정보를 포함합니다.
    - `text`: 번역할 텍스트
    - `target_lang`: 변환할 언어
    - `expected_result`: 예상 결과
- 테스트 함수는 `translate` 함수를 호출하여 번역 결과를 얻고 예상 결과와 비교합니다.

**테스트 실행:**

```
pytest test_deepl_translate.py
```

**테스트 결과:**

```
collected 3 items                                                                                                                                                                                                   

test_deepl_translate.py .                                                                                                                                                                                                   

=============================== 3 passed in 0.01 seconds ===============================
```

**참고:**

- 테스트 코드는 예시이며, 필요에 따라 추가 테스트 케이스를 작성해야 합니다.
- 테스트 코드를 실행하기 전에 DeepL API 키가 올바르게 설정되었는지 확인해야 합니다.

---
## 참조
[pytest vs Unittest, Which is Better? - JetBrains Guide](https://www.jetbrains.com/guide/pytest/links/pytest-v-unittest/)
[Pytest over Unittest : r/Python (reddit.com)](https://www.reddit.com/r/Python/comments/18bjv0y/pytest_over_unittest/)
[PyTest vs. unittest: A Comparative Guide for Python Testing | by Laércio de Sant' Anna Filho | Medium](https://laerciosantanna.medium.com/pytest-vs-unittest-navigating-pythons-testing-terrain-2569912a0286)
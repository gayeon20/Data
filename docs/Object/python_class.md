---
title: "[Python] 클래스 (Class)"
excerpt: 클래스는 데이터와 기능을 함께 묶는 방법을 제공합니다. 새 클래스를 만드는 것은 객체의 새 _형_ 을 만들어서, 그 형의 새 인스턴스 를 만들 수 있도록 합니다. 각 클래스 인스턴스는 상태를 유지하기 위해 그 자신에게 첨부된 어트리뷰트를 가질 수 있습니다. 클래스 인스턴스는 상태를 바꾸기 위한 (클래스에 의해 정의된) 메서드도 가질 수 있습니다.
categories:
  - Python
tags:
  - Python
  - Object
  - Class
last_modified_at: 2024-04-11T15:10:55+09:00
link: 
상위 항목: "[[python_object|파이썬 객체 (Python Object)]]"
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

---
- 클래스는 데이터와 기능을 함께 묶는 방법을 제공합니다. 새 클래스를 만드는 것은 객체의 새 _형_ 을 만들어서, 그 형의 새 인스턴스 를 만들 수 있도록 합니다. 각 클래스 인스턴스는 상태를 유지하기 위해 그 자신에게 첨부된 어트리뷰트를 가질 수 있습니다. 클래스 인스턴스는 상태를 바꾸기 위한 (클래스에 의해 정의된) 메서드도 가질 수 있습니다.
- 다른 프로그래밍 언어들과 비교할 때, 파이썬의 클래스 메커니즘은 최소한의 새로운 문법과 개념을 써서 클래스를 추가합니다. C++ 과 모듈라-3 에서 발견되는 클래스 메커니즘을 혼합합니다. 파이썬 클래스는 객체 지향형 프로그래밍의 모든 표준 기능들을 제공합니다: 클래스 상속 메커니즘은 다중 베이스 클래스를 허락하고, 자식 클래스는 베이스 클래스나 클래스들의 어떤 메서드도 재정의할 수 있으며, 메서드는 같은 이름의 베이스 클래스의 메서드를 호출할 수 있습니다. 객체들은 임의의 종류의 데이터를 양적 제한 없이 가질 수 있습니다. 모듈과 마찬가지로, 클래스는 파이썬의 동적인 본성을 함께 나눕니다: 실행 시간에 만들어지고, 만들어진 후에도 더 수정될 수 있습니다.
- C++ 용어로, 보통 클래스 멤버들은 (데이터 멤버를 포함해서) _public_ (예외는 아래 [비공개 변수](https://docs.python.org/ko/3.12/tutorial/classes.html#tut-private) 를 보세요) 하고, 모든 맴버 함수들은 _virtual_ 입니다. 모듈라-3처럼, 객체의 매소드에서 그 객체의 멤버를 참조하는 줄임 표현은 없습니다: 메서드 함수는 그 객체를 표현하는 명시적인 첫 번째 인자를 선언하는데, 함수 호출 때 묵시적으로 제공됩니다. 스몰토크처럼, 클래스 자신도 객체입니다. 이것이 임포팅과 이름 변경을 위한 개념을 제공합니다. C++ 나 모듈라-3 와는 달리, 내장형도 사용자가 확장하기 위해 베이스 클래스로 사용할 수 있습니다. 또한, C++ 처럼, 특별한 문법을 갖는 대부분의 내장 연산자들은 (산술 연산자, 서브스크립팅, 등등) 클래스 인스턴스에 대해 새로 정의될 수 있습니다.

> (클래스에 대해 보편적으로 받아들여지는 용어들이 없는 상태에서, 이따금 스몰토크나 C++ 용어들을 사용할 것입니다. C++ 보다 객체 지향적 개념들이 파이썬의 것과 더 가까우므로 모듈라-3 용어를 사용할 수도 있지만, 들어본 독자들이 별로 없을 것으로 예상합니다.)

> [!NOTE] 이름과 객체에 관한 한마디
> 
> - 객체는 개체성(individuality)을 갖고, 여러 개의 이름이 (여러 개의 스코프에서) 같은 객체에 연결될 수 있습니다. 이것은 다른 언어들에서는 에일리어싱(aliasing) 이라고 알려져 있습니다. 보통 파이썬을 처음 볼 때 이 점을 높이 평가하지는 않고, 불변 기본형들 (숫자, 문자열, 튜플)을 다루는 동안은 안전하게 무시할 수 있습니다. 하지만, 에일리어싱는 리스트, 딕셔너리나 그 밖의 다른 가변 객체들을 수반하는 파이썬 코드의 의미에 극적인 효과를 줄 수 있습니다. 이것은 보통 프로그램에 혜택이 되는데, 에일리어스는 어떤 면에서 포인터처럼 동작하기 때문입니다. 예를 들어, 구현이 포인터만 전달하기 때문에, 객체를 전달하는 비용이 적게 듭니다; 그리고 함수가 인자로 전달된 객체를 수정하면, 호출자는 그 변경을 보게 됩니다 — 이것은 파스칼에서 사용되는 두 가지 서로 다른 인자 전달 메커니즘의 필요를 제거합니다.

## 파이썬 스코프와 이름 공간

- 클래스를 소개하기 전에, 파이썬의 스코프 규칙에 대해 몇 가지 말할 것이 있습니다. 클래스 정의는 이름 공간으로 깔끔한 요령을 부리고, 여러분은 무엇이 일어나는지 완전히 이해하기 위해 스코프와 이름 공간이 어떻게 동작하는지 알 필요가 있습니다. 덧붙여 말하자면, 이 주제에 대한 지식은 모든 고급 파이썬 프로그래머에게 쓸모가 있습니다. 몇 가지 정의로 시작합시다.
- _이름 공간_ 은 이름에서 객체로 가는 매핑입니다. 대부분의 이름 공간은 현재 파이썬 딕셔너리로 구현되어 있지만, 보통 다른 식으로는 알아차릴 수 없고 (성능은 예외입니다), 앞으로는 바뀔 수 있습니다. 이름 공간의 예는: 내장 이름들의 집합 ([`abs()`](https://docs.python.org/ko/3.12/library/functions.html#abs "abs") 와 같은 함수들과 내장 예외 이름들을 포함합니다); 모듈의 전역 이름들; 함수 호출에서의 지역 이름들. 어떤 의미에서 객체의 어트리뷰트 집합도 이름 공간을 형성합니다. 이름 공간에 대해 알아야 할 중요한 것은 서로 다른 이름 공간들의 이름 간에는 아무런 관계가 없다는 것입니다; 예를 들어, 두 개의 서로 다른 모듈들은 모두 혼동 없이 함수 `maximize` 를 정의할 수 있습니다 — 모듈의 사용자들은 모듈 이름을 앞에 붙여야 합니다.
- 그런데, 저는 _어트리뷰트_ 라는 단어를 점 뒤에 오는 모든 이름에 사용합니다 — 예를 들어, 표현식 `z.real` 에서, `real` 는 객체 `z` 의 어트리뷰트입니다. 엄밀하게 말해서, 모듈에 있는 이름들에 대한 참조는 어트리뷰트 참조입니다: 표현식 `modname.funcname` 에서, `modname` 은 모듈 객체고 `funcname` 는 그것의 어트리뷰트입니다. 이 경우에는 우연히도 모듈의 어트리뷰트와 모듈에서 정의된 전역 이름 간에 직접적인 매핑이 생깁니다: 같은 이름 공간을 공유합니다! 
- 속성은 읽기 전용이거나 쓰기 가능일 수 있습니다. 후자의 경우 속성에 대한 할당이 가능합니다. 모듈 어트리뷰트는 쓰기 가능하므로 `modname.the_answer = 42`를 작성할 수 있습니다. 쓰기 가능한 어트리뷰트는 [`del`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#del) 문을 사용하여 삭제할 수도 있습니다. 예를 들어 `del modname.the_answer`는 `modname`으로 명명된 객체에서 `the_answer` 속성을 제거합니다.
- 이름 공간들은 서로 다른 순간에 만들어지고 서로 다른 수명을 갖습니다. 내장 이름들을 담는 이름 공간은 파이썬 인터프리터가 시작할 때 만들어지고 영원히 지워지지 않습니다. 모듈의 전역 이름 공간은 모듈 정의를 읽는 동안 만들어집니다; 보통, 모듈 이름 공간은 인터프리터가 끝날 때까지 남습니다. 인터프리터의 최상위 호출 때문에 실행되는, 스크립트 파일이나 대화형으로 읽히는, 문장들은 [`__main__`](https://docs.python.org/ko/3.12/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.") 이라고 불리는 모듈 일부로 여겨져서 그 들 자신의 이름 공간을 갖습니다. (내장 이름들 또한 모듈에 속하는데; 이것을 [`builtins`](https://docs.python.org/ko/3.12/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.") 라 부릅니다.)
- 함수의 지역 이름 공간은 함수가 호출될 때 만들어지고, 함수가 복귀하거나 함수 내에서 처리되지 않는 예외를 일으킬 때 삭제됩니다. (사실, 잊어버린다는 것이 실제로 일어나는 일에 대한 더 좋은 설명입니다.) 물론, 재귀적 호출은 각각 자기 자신만의 지역 이름 공간을 갖습니다.
- _스코프_ 는 이름 공간을 직접 액세스할 수 있는 파이썬 프로그램의 텍스트 적인 영역입니다. 여기에서 “직접 액세스 가능한” 이란 이름에 대한 정규화되지 않은 참조가 그 이름 공간에서 이름을 찾으려고 시도한다는 의미입니다.
- 스코프가 정적으로 결정됨에도 불구하고, 동적으로 사용됩니다. 실행 중 어느 시점에서건, 이름 공간을 직접 액세스 가능한, 세 개나 네 개의 중첩된 스코프가 있습니다:
  - 가장 먼저 검색되는, 가장 내부의 스코프는 지역 이름들을 포함합니다
  - 가장 가까운 둘러싸는 범위부터 검색되는 모든 둘러싸는 함수의 범위에는 로컬이 아닌 전역 이름이 아닌 이름도 포함됩니다.
  - 마지막 직전의 스코프는 현재 모듈의 전역 이름들을 포함합니다
  - (가장 나중에 검색되는) 가장 외부의 스코프는 내장 이름들을 포함하고 있는 이름 공간입니다.

- 이름이 전역으로 선언된 경우 모든 참조와 할당은 모듈의 전역 이름이 포함된 다음 범위로 바로 이동합니다. 가장 안쪽 범위 외부에 있는 변수를 다시 바인딩하려면 [`nonlocal`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#nonlocal) 문을 사용할 수 있으며, 비로컬로 선언하지 않으면 해당 변수는 읽기 전용입니다(이러한 변수에 쓰기를 시도하면 가장 안쪽 범위에서 _new_ 로컬 변수가 생성되며 동일한 이름의 바깥쪽 변수는 변경되지 않습니다).
- 보통, 지역 스코프는 현재 함수의 지역 이름들을 (텍스트 적으로) 참조합니다. 함수 바깥에서, 지역 스코프는 전역 스코프와 같은 이름 공간을 참조합니다: 모듈의 이름 공간. 클래스 정의들은 지역 스코프에 또 하나의 이름 공간을 배치합니다.
- 스코프가 텍스트 적으로 결정된다는 것을 깨닫는 것은 중요합니다: 모듈에서 정의된 함수의 전역 스코프는, 어디에서 어떤 에일리어스를 통해 그 함수가 호출되는지에 관계없이, 그 모듈의 이름 공간입니다. 반면에, 이름을 실제로 검색하는 것은 실행시간에 동적으로 수행됩니다 — 하지만, 언어 정의는 컴파일 시점의 정적인 이름 결정을 향해 진화하고 있어서, 동적인 이름 결정에 의존하지 말아야 합니다! (사실, 지역 변수들은 이미 정적으로 결정됩니다.)
- 파이썬의 특별한 특징은 – [`global`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#global)이나 [`nonlocal`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#nonlocal) 문이 없을 때 – 이름에 대입하면 항상 가장 내부의 스코프로 간다는 것입니다. 대입은 데이터를 복사하지 않습니다 – 이름을 단지 객체에 연결할 뿐입니다. 삭제도 마찬가지입니다: 문장 `del x` 는 지역 스코프가 참조하는 이름 공간에서 `x` 의 연결을 제거합니다. 사실, 새 이름을 소개하는 모든 연산은 지역 스코프를 사용합니다: 특히, [`import`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#import) 문과 함수 정의는 모듈이나 함수 이름을 지역 스코프에 연결합니다.
- [`global`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#global) 문은 특정 변수가 전역 스코프에 있으며 그곳에 재연결되어야 함을 가리킬 때 사용될 수 있습니다; [`nonlocal`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#nonlocal) 문은 특정 변수가 둘러싸는 스코프에 있으며 그곳에 재연결되어야 함을 가리킵니다.

### 스코프와 이름 공간 예

- 이것은 어떻게 서로 다른 스코프와 이름 공간을 참조하고, [`global`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#global) 과 [`nonlocal`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#nonlocal) 이 변수 연결에 어떤 영향을 주는지를 보여주는 예입니다:

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

예제 코드의 출력은 이렇게 됩니다:

```
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```

- 어떻게 _지역_ 대입이 (이것이 기본입니다) _scope_test_ 의 _spam_ 연결을 바꾸지 않는지에 유의하세요. [`nonlocal`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#nonlocal) 대입은 _scope_test_ 의 _spam_ 연결을 바꾸고 [`global`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#global) 대입은 모듈 수준의 연결을 바꿉니다.
- [`global`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#global) 대입 전에는 _spam_ 의 연결이 없다는 것도 볼 수 있습니다.

## 클래스
- 클래스는 약간의 새 문법과 세 개의 객체형과 몇 가지 새 개념들을 도입합니다.

### 클래스 정의 문법

- 클래스 정의의 가장 간단한 형태는 이렇게 생겼습니다:

```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

- 함수 정의([`def`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#def) 문)처럼, 클래스 정의는 어떤 효과가 생기기 위해서는 먼저 실행되어야 합니다. (상상컨대 클래스 정의를 [`if`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#if) 문의 분기나 함수 내부에 놓을 수 있습니다)
- 실재적으로, 클래스 정의 내부의 문장들은 보통 함수 정의들이지만, 다른 문장들도 허락되고 때로 쓸모가 있습니다 — 나중에 이 주제로 돌아올 것입니다. 클래스 내부의 함수 정의는 보통, 메서드 호출 규약의 영향을 받은, 특별한 형태의 인자 목록을 갖습니다. — 다시, 이것은 뒤에서 설명됩니다.
- 클래스 정의에 진입할 때, 새 이름 공간이 만들어지고 지역 스코프로 사용됩니다 — 그래서, 모든 지역 변수들로의 대입은 이 새 이름 공간으로 갑니다. 특히, 함수 정의는 새 함수의 이름을 이곳에 연결합니다.
- 클래스 정의가 정상적으로 끝나면 (끝을 통해) class object가 생성됩니다. 이것은 기본적으로 클래스 정의에 의해 생성된 네임스페이스의 내용을 감싸는 래퍼이며, 다음 섹션에서 클래스 객체에 대해 자세히 알아보겠습니다. 원래 로컬 범위(클래스 정의가 입력되기 직전에 유효했던 범위)가 복원되고 클래스 객체는 여기에 클래스 정의 헤더에 지정된 클래스 이름(예제에서는 `ClassName`)에 바인딩됩니다.

### 클래스 객체
- 클래스 객체는 두 종류의 연산을 지원합니다: 어트리뷰트 참조와 인스턴스 만들기.
- _어트리뷰트 참조_ 는 파이썬의 모든 어트리뷰트 참조에 사용되는 표준 문법을 사용합니다: `obj.name`. 올바른 어트리뷰트 이름은 클래스 객체가 만들어질 때 클래스의 이름 공간에 있던 모든 이름입니다. 그래서, 클래스 정의가 이렇게 될 때:

```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```

인 경우 `MyClass.i`와 `MyClass.f`는 각각 정수와 함수 객체를 반환하는 유효한 어트리뷰트 참조입니다. 클래스 어트리뷰트도 할당할 수 있으므로 할당을 통해 `MyClass.i`의 값을 변경할 수 있습니다. '`__doc__`도 유효한 어트리뷰트로, 클래스에 속하는 문서 문자열을 반환합니다: "간단한 예제 클래스"`를 반환합니다.
- 클래스 _인스턴스 만들기_ 는 함수 표기법을 사용합니다. 클래스 객체가 클래스의 새 인스턴스를 돌려주는 매개변수 없는 함수인 체합니다. 예를 들어 (위의 클래스를 가정하면):

```python
x = MyClass()
```

는 클래스의 새 _인스턴스_ 를 만들고 이 객체를 지역 변수 `x` 에 대입합니다.

- 인스턴스화 작업('클래스 객체 호출')은 빈 객체를 생성합니다. 많은 클래스는 특정 초기 상태에 맞게 사용자 정의된 인스턴스로 객체를 생성하는 것을 좋아합니다. 따라서 클래스는 다음과 같이 [`__init__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__init__ "object.__init__")라는 특수 메서드를 정의할 수 있습니다:

```python
def __init__(self):
    self.data = []
```

- 클래스가 [`__init__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__init__ "object.__init__") 메서드를 정의하면, 클래스 인스턴스화는 새로 생성된 클래스 인스턴스에 대해 자동으로 `__init__()`를 호출합니다. 따라서 이 예제에서는 다음과 같이 초기화된 새 인스턴스를 얻을 수 있습니다:

```python
x = MyClass()
```

- 물론 [`__init__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__init__ "object.__init__") 메서드에는 유연성을 높이기 위해 인수가 있을 수 있습니다. 이 경우 클래스 인스턴스화 연산자에 주어진 인수는 `__init__()`에 전달됩니다. 예를 들어

```python
>>> class Complex:
…     def __init__(self, realpart, imagpart):
…         self.r = realpart
…         self.i = imagpart
…
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
```

### 인스턴스 객체

- 이제 인스턴스 객체로 무엇을 할 수 있을까? 인스턴스 객체가 이해하는 오직 한가지 연산은 어트리뷰트 참조입니다. 두 가지 종류의 올바른 어트리뷰트 이름이 있습니다: 데이터 어트리뷰트와 메서드.
- 데이터 어트리뷰트_는 Smalltalk에서는 "인스턴스 변수"에, C++에서는 "데이터 멤버"에 해당합니다. 데이터 어트리뷰트는 선언할 필요가 없으며, 지역 변수와 마찬가지로 처음 할당될 때 존재하게 됩니다. 예를 들어 `x`가 위에서 만든 `MyClass`의 인스턴스라면, 다음 코드는 흔적을 남기지 않고 `16`이라는 값을 출력합니다:

```python
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```

- 다른 종류의 인스턴스 어트리뷰트 참조는 method_입니다. 메서드는 객체에 '속하는' 함수입니다.
- 인스턴스 객체의 올바른 메서드 이름은 그것의 클래스에 달려있습니다. 정의상, 함수 객체인 클래스의 모든 어트리뷰트들은 상응하는 인스턴스의 메서드들을 정의합니다. 그래서 우리의 예제에서, `x.f` 는 올바른 메서드 참조인데, `MyClass.f` 가 함수이기 때문입니다. 하지만 `x.i` 는 그렇지 않은데, `MyClass.i` 가 함수가 아니기 때문입니다. 그러나, `x.f` 는 `MyClass.f` 와 같은 것이 아닙니다 — 이것은 함수 객체가 아니라 _메서드 객체_ 입니다.

### 메서드 객체
- 보통, 메서드는 연결되자마자 호출됩니다:

```python
x.f()
```

- `MyClass` 예제에서는 'hello world'라는 문자열을 반환합니다. 그러나 메서드를 바로 호출할 필요는 없습니다. `x.f`는 메서드 객체이므로 저장해 두었다가 나중에 호출할 수 있습니다. 예를 들어

```python
xf = x.f
while True:
    print(xf())
```

는 영원히 계속 `hello world` 를 인쇄합니다.

- 메서드가 호출되면 정확히 어떤 일이 일어날까요? 위에서 `f()`의 함수 정의에 인수가 지정되어 있음에도 불구하고 `x.f()`가 인자 없이 호출된 것을 보셨을 것입니다. 인수는 어떻게 된 걸까요? 인수가 필요한 함수가 인자 없이 호출될 때, 인수가 실제로 사용되지 않더라도 파이썬은 예외를 발생시킵니다….
- 실제로, 여러분은 답을 짐작할 수 있습니다: 메서드의 특별함은 인스턴스 객체가 함수의 첫 번째 인자로 전달된다는 것입니다. 우리 예에서, 호출 `x.f()`는 정확히 `MyClass.f(x)` 와 동등합니다. 일반적으로, _n_ 개의 인자들의 목록으로 메서드를 호출하는 것은, 첫 번째 인자 앞에 메서드의 인스턴스 객체를 삽입해서 만든 인자 목록으로 상응하는 함수를 호출하는 것과 동등합니다.
- 일반적으로 메서드는 다음과 같이 작동합니다. 인스턴스의 비데이터 속성이 참조되면 인스턴스의 클래스가 검색됩니다. 이름이 함수 객체인 유효한 클래스 속성을 나타내는 경우, 인스턴스 객체와 함수 객체에 대한 참조가 메서드 객체로 패킹됩니다. 메서드 객체가 인자 목록과 함께 호출되면 인스턴스 객체와 인자 목록에서 새 인자 목록이 구성되고 이 새 인자 목록으로 함수 객체가 호출됩니다.

### 클래스와 인스턴스 변수

- 일반적으로 말해서, 인스턴스 변수는 인스턴스별 데이터를 위한 것이고 클래스 변수는 ==그 클래스의 모든 인스턴스에서 공유되는 어트리뷰트와 메서드==를 위한 것입니다. 하나의 인스턴스에서 클래스 변수 값을 바꾸면 나머지 인스턴스의 클래스 변수 값도 함께 바뀝니다:

```python
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
```

- [이름과 객체에 관한 한마디](https://docs.python.org/ko/3.12/tutorial/classes.html#tut-object) 에서 논의했듯이, 리스트나 딕셔너리와 같은 [가변](https://docs.python.org/ko/3.12/glossary.html#term-mutable) 객체가 참여할 때 공유 데이터는 예상치 못한 효과를 줄 가능성이 있습니다. 예를 들어, 다음 코드에서 _tricks_ 리스트는 클래스 변수로 사용되지 않아야 하는데, 하나의 리스트가 모든 _Dog_ 인스턴스들에 공유되기 때문입니다.

```python
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
```

대신, 클래스의 올바른 설계는 인스턴스 변수를 사용해야 합니다:

```python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```

## 기타 주의사항들
- 인스턴스와 클래스 모두에서 같은 어트리뷰트 이름이 등장하면, 어트리뷰트 조회는 인스턴스를 우선합니다:

```python
>>> class Warehouse:
…    purpose = 'storage'
…    region = 'west'
…
>>> w1 = Warehouse()
>>> print(w1.purpose, w1.region)
storage west
>>> w2 = Warehouse()
>>> w2.region = 'east'
>>> print(w2.purpose, w2.region)
storage east
```

- 데이터 어트리뷰트는 메서드 뿐만 아니라 객체의 일반적인 사용자 (“클라이언트”)에 의해서 참조될 수도 있습니다. 달리 표현하면, 클래스는 순수하게 추상적인 데이터형을 구현하는데 사용될 수 없습니다. 사실, 파이썬에서는 데이터 은닉을 강제할 방법이 없습니다 — 모두 관례에 의존합니다. (반면에, C로 작성된 파이썬 구현은 필요하다면 구현 상세를 완전히 숨기고 객체에 대한 액세스를 제어할 수 있습니다; 이것은 C로 작성된 파이썬 확장에서 사용될 수 있습니다.)
- 클라이언트는 데이터 어트리뷰트를 조심스럽게 사용해야 합니다 — 클라이언트는 데이터 어트리뷰트를 건드려서 메서드들에 의해 유지되는 불변성 들을 망가뜨릴 수 있습니다. 클라이언트는 이름 충돌을 피하는 한 메서드들의 유효성을 손상하지 않고도 그들 자신의 데이터 어트리뷰트를 인스턴스 객체에 추가할 수도 있음에 유의하세요 — 다시 한번, 명명 규칙은 여러 골칫거리를 피할 수 있게 합니다.
- 메서드 안에서 데이터 어트리뷰트들(또는 다른 메서드들!)을 참조하는 줄임 표현은 없습니다. 저는 이것이 실제로 메서드의 가독성을 높인다는 것을 알게 되었습니다: 메서드를 훑어볼 때 지역 변수와 인스턴스 변수를 혼동할 우려가 없습니다.
- 종종, 메서드의 첫 번째 인자는 `self` 라고 불립니다. 이것은 관례일 뿐입니다: 이름 `self` 는 파이썬에서 아무런 특별한 의미를 갖지 않습니다. 하지만, 이 규칙을 따르지 않을 때 여러분의 코드가 다른 파이썬 프로그래머들이 읽기에 불편하고, _클래스 브라우저_ 프로그램도 이런 규칙에 의존하도록 작성되었다고 상상할 수 있음에 유의하세요.
- 클래스 어트리뷰트인 모든 함수는 그 클래스의 인스턴스들을 위한 메서드를 정의합니다. 함수 정의가 클래스 정의에 텍스트 적으로 둘러싸일 필요는 없습니다: 함수 객체를 클래스의 지역 변수로 대입하는 것 역시 가능합니다. 예를 들어:

```python
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```

- 이제 `f`, `g`, `h`는 모두 함수 객체를 참조하는 클래스 `C`의 어트리뷰트이며, 결과적으로 `g`와 정확히 동일한 `C` - `h`의 인스턴스 메서드입니다. 이러한 관행은 일반적으로 프로그램 독자에게 혼란을 줄 뿐이라는 점에 유의하세요.
- 메서드는 `self` 인자의 메서드 어트리뷰트를 사용해서 다른 메서드를 호출할 수 있습니다:

```python
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```

- 메서드는 일반 함수들과 마찬가지로 전역 이름을 참조할 수 있습니다. 메서드에 결합한 전역 스코프는 그것의 정의를 포함하는 모듈입니다. (클래스는 결코 전역 스코프로 사용되지 않습니다.) 메서드에서 전역 데이터를 사용할 좋은 이유를 거의 만나지 못하지만, 전역 스코프를 정당하게 사용하는 여러 가지 경우가 있습니다: 한가지는, 전역 스코프에 정의된 함수와 메서드 뿐만 아니라, 그곳에 임포트된 함수와 모듈도 메서드가 사용할 수 있다는 것입니다. 보통, 메서드를 포함하는 클래스 자신은 이 전역 스코프에 정의되고, 다음 섹션에서 메서드가 자신의 클래스를 참조하길 원하는 몇 가지 좋은 이유를 보게 될 것입니다.
- 각 값은 객체고, 그러므로 _클래스_ (_형_ 이라고도 불린다) 를 갖습니다. 이것은 `object.__class__` 에 저장되어 있습니다.

## 상속

- 물론, 상속을 지원하지 않는다면 언어 기능은 “클래스”라는 이름을 붙일만한 가치가 없을 것입니다. 파생 클래스 정의의 문법은 이렇게 생겼습니다:

```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

- `BaseClassName`은 파생 클래스 정의가 포함된 범위에서 액세스할 수 있는 네임스페이스에 정의되어야 합니다. 베이스 클래스 이름 대신 다른 임의의 표현식도 허용됩니다. 예를 들어 기본 클래스가 다른 모듈에 정의되어 있는 경우 유용할 수 있습니다:

```python
class DerivedClassName(modname.BaseClassName):
```

- 파생 클래스 정의의 실행은 베이스 클래스와 같은 방식으로 진행됩니다. 클래스 객체가 만들어질 때, 베이스 클래스가 기억됩니다. 이것은 어트리뷰트 참조를 결정할 때 사용됩니다: 요청된 어트리뷰트가 클래스에서 발견되지 않으면 베이스 클래스로 검색을 확장합니다. 베이스 클래스 또한 다른 클래스로부터 파생되었다면 이 규칙은 재귀적으로 적용됩니다.
- 파생 클래스의 인스턴스 만들기에 특별한 것은 없습니다: `DerivedClassName()` 는 그 클래스의 새 인스턴스를 만듭니다. 메서드 참조는 다음과 같이 결정됩니다: 대응하는 클래스 어트리뷰트가 검색되는데, 필요하면 베이스 클래스의 연쇄를 타고 내려갑니다. 이것이 함수 객체를 준다면 메서드 참조는 올바릅니다.
- 파생 클래스는 베이스 클래스의 메서드들을 재정의할 수 있습니다. 메서드가 같은 객체의 다른 메서드를 호출할 때 특별한 권한 같은 것은 없으므로, 베이스 클래스에 정의된 다른 메서드를 호출하는 베이스 클래스의 메서드는 재정의된 파생 클래스의 메서드를 호출하게 됩니다. (C++ 프로그래머를 위한 표현으로: 파이썬의 모든 메서드는 실질적으로 `virtual` 입니다.)
- 파생 클래스에서 재정의된 메서드가, 같은 이름의 베이스 클래스 메서드를 단순히 갈아치우기보다 사실은 확장하고 싶을 수 있습니다. 베이스 클래스의 메서드를 직접 호출하는 간단한 방법이 있습니다: 단지 `BaseClassName.methodname(self, arguments)` 를 호출하면 됩니다. 이것은 때로 클라이언트에게도 쓸모가 있습니다. (이것은 베이스 클래스가 전역 스코프에서 `BaseClassName` 으로 액세스 될 수 있을 때만 동작함에 주의하세요.)
- 파이썬에는 상속과 함께 사용할 수 있는 두 개의 내장 함수가 있습니다:
  
  - 인스턴스의 형을 검사하려면 [`isinstance()`](https://docs.python.org/ko/3.12/library/functions.html#isinstance "isinstance") 를 사용합니다: `isinstance(obj, int)` 는 `obj.__class__` 가 [`int`](https://docs.python.org/ko/3.12/library/functions.html#int "int") 거나 [`int`](https://docs.python.org/ko/3.12/library/functions.html#int "int") 에서 파생된 클래스인 경우만 `True` 가 됩니다.
  - 클래스 상속을 검사하려면 [`issubclass()`](https://docs.python.org/ko/3.12/library/functions.html#issubclass "issubclass") 를 사용합니다: `issubclass(bool, int)` 는 `True` 인데, [`bool`](https://docs.python.org/ko/3.12/library/functions.html#bool "bool") 이 [`int`](https://docs.python.org/ko/3.12/library/functions.html#int "int") 의 서브 클래스이기 때문입니다. 하지만, `issubclass(float, int)` 는 `False` 인데, [`float`](https://docs.python.org/ko/3.12/library/functions.html#float "float") 는 [`int`](https://docs.python.org/ko/3.12/library/functions.html#int "int") 의 서브 클래스가 아니기 때문입니다.

### 메소드 구현
- 부모 클래스의 메소드에 기능을 추가할 경우 다음과 같이 `super()`를 사용합니다.

```python
# 부모 클래스
class BaseModel:
    def __init__(self, variable1, variable2) -> None:
        self.variable1 = variable1
        self.variable2 = variable2

# 자식 클래스
class ChildModel(BaseModel):
    def __init__(
        self, variable1, variable2, variable3
    ) -> None:
	    self.variable3 = variable3
        super().__init__(variable1, variable2)
```

- `super()`의 메소드를 호출하면 부모 클래스에 정의된 기능을 수행합니다.

### 다중 상속

- 파이썬은 다중 상속의 형태도 지원합니다. 여러 개의 베이스 클래스를 갖는 클래스 정의는 이런 식입니다:

```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

- 대부분의 간단한 경우, 부모 클래스에서 상속된 속성을 검색할 때는 계층 구조가 겹치는 같은 클래스에서 두 번 검색하지 않고 왼쪽에서 오른쪽으로 깊이 우선으로 검색한다고 생각할 수 있습니다. 따라서 `DerivedClassName`에서 속성을 찾지 못하면 `Base1`에서 검색한 다음 `Base1`의 기본 클래스에서 (재귀적으로) 검색하고, 거기서도 찾지 못하면 `Base2`에서 검색하는 식으로 검색합니다.
- 사실, 이것보다는 약간 더 복잡합니다; 메서드 결정 순서는 [`super()`](https://docs.python.org/ko/3.12/library/functions.html#super "super") 로의 협력적인 호출을 지원하기 위해 동적으로 변경됩니다. 이 접근법은 몇몇 다른 다중 상속 언어들에서 call-next-method 라고 알려져 있고, 단일 상속 언어들에서 발견되는 super 호출보다 더 강력합니다.

- 다중 상속의 모든 경우 하나 이상의 다이아몬드 관계(최하위 클래스에서 여러 경로를 통해 부모 클래스 중 하나 이상에 액세스할 수 있는 경우)가 나타나기 때문에 동적 순서가 필요합니다. 예를 들어 모든 클래스는 ``객체``(https://docs.python.org/ko/3.12/library/functions.html#object "객체")로부터 상속되므로 다중 상속의 모든 경우는 ``객체``(https://docs.python.org/ko/3.12/library/functions.html#object "객체")에 도달하는 경로를 두 개 이상 제공합니다. 기본 클래스가 두 번 이상 액세스되지 않도록 동적 알고리즘은 각 클래스에 지정된 왼쪽에서 오른쪽 순서를 유지하고, 각 부모를 한 번만 호출하며, 단조로운(부모의 우선 순위에 영향을 주지 않고 클래스를 하위 클래스화할 수 있음을 의미) 방식으로 검색 순서를 선형화합니다. 이러한 속성을 종합하면 다중 상속을 통해 안정적이고 확장 가능한 클래스를 설계할 수 있습니다. 자세한 내용은 [파이썬 2.3 메서드 해결 순서](https://docs.python.org/ko/3.12/howto/mro.html#python-2-3-mro)를 참조하십시오.


## 비공개 변수
- 객체 내부에서만 액세스할 수 있는 “비공개” 인스턴스 변수는 파이썬에 존재하지 않습니다. 하지만, 대부분의 파이썬 코드에서 따르고 있는 규약이 있습니다: 밑줄로 시작하는 이름은 (예를 들어, `_spam`) API의 공개적이지 않은 부분으로 취급되어야 합니다 (그것이 함수, 메서드, 데이터 멤버중 무엇이건 간에). 구현 상세이고 통보 없이 변경되는 대상으로 취급되어야 합니다.
- 클래스-비공개 멤버들의 올바른 사례가 있으므로 (즉 서브 클래스에서 정의된 이름들과의 충돌을 피하고자), _이름 뒤섞기 (name mangling)_ 라고 불리는 메커니즘에 대한 제한된 지원이 있습니다. `__spam` 형태의 (최소 두 개의 밑줄로 시작하고, 최대 한 개의 밑줄로 끝납니다) 모든 식별자는 `_classname__spam` 로 텍스트 적으로 치환되는데, `classname` 은 현재 클래스 이름에서 앞에 오는 밑줄을 제거한 것입니다. 이 뒤섞기는 클래스 정의에 등장하는 이상, 식별자의 문법적 위치와 무관하게 수행됩니다.
  
  자세한 내용과 특수 사례는 [비공개 이름 망글링 사양](https://docs.python.org/ko/3.12/reference/expressions.html#private-name-mangling)을 참조하세요.

- 이름 뒤섞기는 클래스 내부의 메서드 호출을 방해하지 않고 서브 클래스들이 메서드를 재정의할 수 있도록 하는 데 도움을 줍니다. 예를 들어:

```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```

- 위의 예는 `MappingSubclass`가 `__update` 식별자를 도입하더라도 작동합니다. `Mapping` 클래스에서는 `_Mapping__update`로 `MappingSubclass` 클래스에서는 `_MappingSubclass__update`로 각각 대체 되기 때문입니다.
- 뒤섞기 규칙은 대체로 사고를 피하고자 설계되었다는 것에 주의하세요; 여전히 비공개로 취급되는 변수들을 액세스하거나 수정할 수 있습니다. 이것은 디버거와 같은 특별한 상황에서 쓸모 있기조차 합니다.
- `exec()` 나 `eval()` 로 전달된 코드는 호출하는 클래스의 클래스 이름을 현재 클래스로 여기지 않는다는 것에 주의하세요; 이것은 `global` 문의 효과와 유사한데, 효과가 함께 바이트-컴파일된 코드로 제한됩니다. 같은 제약이 `__dict__` 를 직접 참조할 때뿐만 아니라, `getattr()`, `setattr()`, `delattr()` 에도 적용됩니다.

## 잡동사니
- 때로는 파스칼 "레코드" 또는 C "구조체"와 유사한 데이터 유형을 사용하여 몇 개의 명명된 데이터 항목을 함께 묶는 것이 유용할 때가 있습니다. 관용적인 접근 방식은 [`데이터클래스`](https://docs.python.org/ko/3.12/library/dataclasses.html#module-dataclasses "dataclasses: 사용자 정의 클래스에서 특수 메서드를 생성합니다.")를 사용하는 것입니다:

```python
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

>>>

>>> john = Employee('john', 'computer lab', 1000)
>>> john.dept
'computer lab'
>>> john.salary
1000
```

- 특정 추상 데이터 타입을 기대하는 파이썬 코드에 해당 데이터 타입의 메서드를 에뮬레이트하는 클래스를 대신 전달할 수 있는 경우가 많습니다. 예를 들어 파일 객체에서 일부 데이터를 포맷하는 함수가 있는 경우, 문자열 버퍼에서 데이터를 대신 가져오는 [`read()`](https://docs.python.org/ko/3.12/library/io.html#io.TextIOBase.read "io.TextIOBase.read") 및 [`readline()`](https://docs.python.org/ko/3.12/library/io.html#io.TextIOBase.readline "io.TextIOBase.readline") 메서드가 있는 클래스를 정의하고 이를 인수로 전달할 수 있습니다.
- [인스턴스 메서드 객체](https://docs.python.org/ko/3.12/reference/datamodel.html#instance-methods)에도 속성이 있습니다. [`m.__self__`](https://docs.python.org/ko/3.12/reference/datamodel.html#method.__self__ "method.__self__")는 메서드 `m()`을 가진 인스턴스 객체이고, [`m.__func__`](https://docs.python.org/ko/3.12/reference/datamodel.html#method.__func__ "method.__func__")는 메서드에 대응하는 [함수 객체](https://docs.python.org/ko/3.12/reference/datamodel.html#user-defined-funcs)입니다.


## 이터레이터
- 지금쯤 아마도 여러분은 대부분의 컨테이너 객체들을 [`for`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#for) 문으로 루핑할 수 있음을 눈치챘을 것입니다:

```python
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```

- 이런 스타일의 액세스는 명료하고, 간결하고, 편리합니다. 이터레이터를 사용하면 파이썬이 보편화하고 통합됩니다. 무대 뒤에서, [`for`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#for) 문은 컨테이너 객체에 대해 [`iter()`](https://docs.python.org/ko/3.12/library/functions.html#iter "iter") 를 호출합니다. 이 함수는 메서드 [`__next__()`](https://docs.python.org/ko/3.12/library/stdtypes.html#iterator.__next__ "iterator.__next__") 를 정의하는 이터레이터 객체를 돌려주는데, 이 메서드는 컨테이너의 요소들을 한 번에 하나씩 액세스합니다. 남은 요소가 없으면, [`__next__()`](https://docs.python.org/ko/3.12/library/stdtypes.html#iterator.__next__ "iterator.__next__") 는 [`StopIteration`](https://docs.python.org/ko/3.12/library/exceptions.html#StopIteration "StopIteration") 예외를 일으켜서 `for` 루프에 종료를 알립니다. [`next()`](https://docs.python.org/ko/3.12/library/functions.html#next "next") 내장 함수를 사용해서 [`__next__()`](https://docs.python.org/ko/3.12/library/stdtypes.html#iterator.__next__ "iterator.__next__") 메서드를 호출할 수 있습니다; 이 예는 이 모든 것들이 어떻게 동작하는지 보여줍니다:

```python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_iterator object at 0x10c90e650>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
```

- 이터레이터 프로토콜의 메커니즘을 이해했다면 ==클래스에 이터레이터 동작을 쉽게 추가==할 수 있습니다. 객체를 반환하는 [`__iter__()`](https://docs.python.org/ko/3.12/library/stdtypes.html#container.__iter__ "container.__iter__") 메서드를 [`__next__()`](https://docs.python.org/ko/3.12/library/stdtypes.html#iterator.__next__ "iterator.__next__") 메서드와 함께 정의하세요. 클래스가 `__next__()`를 정의하는 경우 `__iter__()`는 그냥 `self`를 반환할 수 있습니다:

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```

```python
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
…     print(char)
…
m
a
p
s
```

## 제너레이터

- [제너레이터](https://docs.python.org/ko/3.12/glossary.html#term-generator) 는 ==이터레이터를 만드는 간단하고 강력한 도구==입니다. 일반적인 함수처럼 작성되지만 값을 돌려주고 싶을 때마다 [`yield`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#yield) 문을 사용합니다. 제너레이터에 [`next()`](https://docs.python.org/ko/3.12/library/functions.html#next "next") 가 호출될 때마다, 제너레이터는 떠난 곳에서 실행을 재개합니다 (모든 데이터 값들과 어떤 문장이 마지막으로 실행되었는지 기억합니다). 예는 제너레이터를 사소할 정도로 쉽게 만들 수 있음을 보여줍니다:

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
```

```python
>>> for char in reverse('golf'):
…     print(char)
…
f
l
o
g
```

- 제너레이터로 할 수 있는 모든 작업은 이전 섹션에서 설명한 대로 클래스 기반 이터레이터로도 수행할 수 있습니다. 제너레이터를 매우 간결하게 만드는 것은 [`__iter__()`](https://docs.python.org/ko/3.12/library/stdtypes.html#iterator.__iter__ "iterator.__iter__") 및 [`__next__()`](https://docs.python.org/ko/3.12/reference/expressions.html#generator.__next__ "generator.__next__") 메서드가 자동으로 생성된다는 점입니다.
- 또 하나의 주요 기능은 지역 변수들과 실행 상태가 호출 간에 자동으로 보관된다는 것입니다. 이것은 `self.index` 나 `self.data` 와 같은 인스턴스 변수를 사용하는 접근법에 비교해 함수를 쓰기 쉽고 명료하게 만듭니다.
- 자동 메서드 생성과 프로그램 상태의 저장에 더해, 제너레이터가 종료할 때 자동으로 [`StopIteration`](https://docs.python.org/ko/3.12/library/exceptions.html#StopIteration "StopIteration") 을 일으킵니다. 조합하면, 이 기능들이 일반 함수를 작성하는 것만큼 이터레이터를 만들기 쉽게 만듭니다.

### `yield`
- Python의 `yield` 키워드환는 제너레이터(generator)를 만드는 데 사용됩니다. 제너레이터는 이터레이터(iterator)를 생성하는 함수로, `yield`를 사용하여 값을 하나씩 반합니다. `yield`는 함수의 실행을 일시 중단하고, 값을 호출자에게 반환한 후 다시 함수의 실행을 재개할 수 있게 합니다. 예를 들어, 다음과 같은 제너레이터 함수를 작성할 수 있습니다:

```python
def number_generator():
    yield 0
    yield 1
    yield 2

for number in number_generator():
    print(number)
```

- 이 코드는 0, 1, 2를 순차적으로 출력합니다. `yield`는 함수의 상태를 유지하면서 다음 호출 시점에 이어서 실행할 수 있게 합니다.
- `yield`와 `return`의 차이점은 `return`은 함수의 실행을 종료하고 값을 반환하는 반면, `yield`는 함수의 실행을 일시 중단하고 값을 반환한 후, 다음 호출 시점에 이어서 실행을 재개한다는 점입니다.

### 제너레이터 표현식

- 간단한 제너레이터는 리스트 컴프리헨션과 비슷하지만, 대괄호 대신 괄호를 사용하는 문법을 사용한 표현식으로 간결하게 코딩할 수 있습니다. 이 표현식들은 둘러싸는 함수가 제너레이터를 즉시 사용하는 상황을 위해 설계되었습니다. 제너레이터 표현식은 완전한 제너레이터 정의보다 간결하지만, 융통성은 떨어지고, 비슷한 리스트 컴프리헨션보다 메모리를 덜 쓰는 경향이 있습니다.

```python
>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> unique_words = set(word for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
```

## 데코레이터 (Decorator)
- Python의 `@property` 데코레이터는 클래스의 메서드를 인스턴스 변수처럼 사용할 수 있게 해주는 기능입니다. 이를 통해 객체의 상태를 직접 수정하지 않고도 메서드를 통해 안전하게 데이터에 접근할 수 있습니다. 이 기능은 캡슐화라고 불리며, 객체 지향 프로그래밍에서 중요한 개념 중 하나입니다.

### 기본 사용법

- `@property` 데코레이터를 사용하면, getter 메서드를 정의할 수 있습니다. 예를 들어, 다음과 같은 `Person` 클래스를 생각해볼 수 있습니다:

```python
class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"
```

- 이제 `full_name` 속성에 접근할 때마다 `full_name` 메서드가 호출됩니다:

```python
person = Person("John", "Doe")
print(person.full_name)  # 출력: John Doe
```

### Setter와 Deleter

- `@property` 데코레이터는 getter뿐만 아니라 setter와 deleter도 지원합니다. 다음은 setter와 deleter를 추가한 예제입니다:

```python
class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @full_name.setter
    def full_name(self, name):
        first_name, last_name = name.split()
        self._first_name = first_name
        self._last_name = last_name

    @full_name.deleter
    def full_name(self):
        self._first_name = None
        self._last_name = None
```

이제 `full_name` 속성을 설정하거나 삭제할 수 있습니다:

```python
person = Person("John", "Doe")
person.full_name = "Jane Smith"
print(person.full_name)  # 출력: Jane Smith
del person.full_name
print(person.full_name)  # 출력: None None
```

- 이렇게 `@property` 데코레이터를 사용하면, 객체의 속성에 접근할 때 추가적인 로직을 실행할 수 있어 매우 유용합니다.


---
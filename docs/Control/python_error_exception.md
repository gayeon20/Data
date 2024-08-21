---
title: "[Python] 에러와 예외 (Error & Exception)"
excerpt: 
categories:
  - Python
tags:
  - Python
  - Control
  - Error
  - Exception
last_modified_at: 2024-04-11T15:10:55+09:00
link: 
상위 항목: "[[python_control|파이썬 제어문 (Python Control Statement)]]"
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

---

- 지금까지 에러 메시지가 언급되지는 않았지만, 예제들을 직접 해보았다면 아마도 몇몇 개를 보았을 것입니다. (적어도) 두 가지 구별되는 에러들이 있습니다; _문법 에러_ 와 _예외_.

## `SyntaxError`

- 문법 에러는, 파싱 에러라고도 알려져 있습니다, 아마도 여러분이 파이썬을 배우고 있는 동안에는 가장 자주 만나는 종류의 불평일 것입니다:

```
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
               ^^^^^
SyntaxError: invalid syntax
```

- 구문 분석기는 문제가 있는 줄을 반복하고 오류가 감지된 줄의 토큰을 가리키는 작은 '화살표'를 표시합니다. 이 오류는 표시된 토큰 앞에 토큰이 없기 때문에 발생할 수 있습니다. 예제에서는 [`print()`](https://docs.python.org/ko/3.12/library/functions.html#print "print") 함수 앞에 콜론(`':'`)이 없기 때문에 오류가 감지되었습니다. 파일 이름과 줄 번호가 인쇄되므로 입력이 스크립트에서 온 경우 어디에서 찾아야 하는지 알 수 있습니다.

## 예외

- 문장이나 표현식이 문법적으로 올바르다 할지라도, 실행하려고 하면 에러를 일으킬 수 있습니다. 실행 중에 감지되는 에러들을 _예외_ 라고 부르고 무조건 치명적이지는 않습니다: 파이썬 프로그램에서 이것들을 어떻게 다루는지 곧 배우게 됩니다. 하지만 대부분의 예외는 프로그램이 처리하지 않아서, 여기에서 볼 수 있듯이 에러 메시지를 만듭니다:

```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

- 에러 메시지의 마지막 줄은 어떤 일이 일어났는지 알려줍니다. 예외는 여러 형으로 나타나고, 형이 메시지 일부로 인쇄됩니다: 이 예에서의 형은 [`ZeroDivisionError`](https://docs.python.org/ko/3.12/library/exceptions.html#ZeroDivisionError "ZeroDivisionError"), [`NameError`](https://docs.python.org/ko/3.12/library/exceptions.html#NameError "NameError"), [`TypeError`](https://docs.python.org/ko/3.12/library/exceptions.html#TypeError "TypeError") 입니다. 예외 형으로 인쇄된 문자열은 발생한 내장 예외의 이름입니다. 이것은 모든 내장 예외들의 경우는 항상 참이지만, 사용자 정의 예외의 경우는 (편리한 관례임에도 불구하고) 꼭 그럴 필요는 없습니다. 표준 예외 이름은 내장 식별자입니다 (예약 키워드가 아닙니다).
- 줄의 나머지 부분은 예외의 형과 원인에 기반을 둔 상세 명세를 제공합니다.
- 에러 메시지의 앞부분은 스택 트레이스의 형태로 예외가 일어난 위치의 문맥을 보여줍니다. 일반적으로 소스의 줄들을 나열하는 스택 트레이스를 포함하고 있습니다; 하지만, 표준 입력에서 읽어 들인 줄들은 표시하지 않습니다.
- [내장 예외](https://docs.python.org/ko/3.12/library/exceptions.html#bltin-exceptions) 는 내장 예외들과 그 들의 의미를 나열하고 있습니다.

## 예외 처리하기

- 선택한 예외를 처리하는 프로그램을 만드는 것이 가능합니다. 다음 예를 보면, 올바를 정수가 입력될 때까지 사용자에게 입력을 요청하지만, 사용자가 프로그램을 인터럽트 하는 것을 허용합니다 (Control-C 나 그 외에 운영 체제가 지원하는 것을 사용해서); 사용자가 만든 인터럽트는 [`KeyboardInterrupt`](https://docs.python.org/ko/3.12/library/exceptions.html#KeyboardInterrupt "KeyboardInterrupt") 예외를 일으키는 형태로 나타남에 유의하세요.

```python
>>> while True:
…     try:
…         x = int(input("Please enter a number: "))
…         break
…     except ValueError:
…         print("Oops!  That was no valid number.  Try again…")
…
```

- [`try`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#try) 문은 다음과 같이 동작합니다.
  1. 먼저, _try 절_ ([`try`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#try) 와 [`except`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#except) 사이의 문장들) 이 실행됩니다.
  2. 예외가 발생하지 않으면, _except 절_ 을 건너뛰고 [`try`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#try) 문의 실행은 종료됩니다.
  3. [`try`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#try) 절을 실행하는 동안 예외가 발생하면 나머지 절은 건너뜁니다. 그런 다음 그 유형이 [`except`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#except) 키워드의 이름을 딴 예외와 일치하면 except 절이 실행되고 try/except 블록 이후 실행이 계속됩니다.
  4. 예외가 except 절에 명명된 예외와 일치하지 않는 예외가 발생하면 외부 [`try`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#try) 문으로 전달되고, 처리기를 찾을 수 없으면 처리되지 않은 예외가 되어 오류 메시지와 함께 실행이 중지됩니다.
- [`try`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#try) 문에는 여러 예외에 대한 핸들러를 지정하기 위해 두 개 이상의 except 절이 있을 수 있습니다. 최대 하나의 핸들러만 실행됩니다. 핸들러는 해당 try 절에서 발생하는 예외만 처리하며, 동일한 `try` 문의 다른 핸들러에서는 예외를 처리하지 않습니다. 예를 들어 except 절은 괄호로 묶인 튜플로 여러 예외의 이름을 지정할 수 있습니다:

```python
… except (RuntimeError, TypeError, NameError):
…     pass
```

- [`예외`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#except) 절의 클래스는 클래스 자체 또는 파생 클래스 중 하나의 인스턴스인 예외와 일치합니다(단, 그 반대는 아닙니다. 파생 클래스를 나열하는 except 절은 기본 클래스의 인스턴스와 일치하지 않습니다). 예를 들어 다음 코드는 B, C, D를 순서대로 출력합니다:

```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```

- 만약 except 절_이 반대로 되어 있다면(`except B`가 먼저), 첫 번째로 일치하는 except 절이 트리거되어 B, B, B가 출력되었을 것입니다.
- 예외가 발생하면 예외의 인수라고도 하는 연관 값을 가질 수 있습니다. 인수의 존재 여부와 유형은 예외 유형에 따라 다릅니다.
- 예외 이름 뒤에 except 절을 사용하여 예외 이름 뒤에 변수를 지정할 수 있습니다. 이 변수는 일반적으로 인수를 저장하는 `args` 속성을 가진 예외 인스턴스에 바인딩됩니다. 편의를 위해 기본 제공 예외 유형은 [`__str__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__str__ "object.__str__")를 정의하여 명시적으로 `.args`에 액세스하지 않고도 모든 인수를 출력합니다.

```python
>>> try:
…     raise Exception('spam', 'eggs')
… except Exception as inst:
…     print(type(inst))    # the exception type
…     print(inst.args)     # arguments stored in .args
…     print(inst)          # __str__ allows args to be printed directly,
…                          # but may be overridden in exception subclasses
…     x, y = inst.args     # unpack args
…     print('x =', x)
…     print('y =', y)
…
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```

- 예외의 [`__str__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__str__ "object.__str__") 출력은 처리되지 않은 예외의 경우 메시지의 마지막 부분('detail')으로 인쇄됩니다.

- [`BaseException`](https://docs.python.org/ko/3.12/library/exceptions.html#BaseException "BaseException")은 모든 예외의 공통 베이스 클래스입니다. 그 서브 클래스 중 하나인 [`Exception`](https://docs.python.org/ko/3.12/library/exceptions.html#Exception "Exception")은 치명적이지 않은 모든 예외의 베이스 클래스입니다. [`Exception`](https://docs.python.org/ko/3.12/library/exceptions.html#Exception "예외")의 서브 클래스가 아닌 예외는 프로그램이 종료되어야 함을 나타내는 데 사용되기 때문에 일반적으로 처리되지 않습니다. 여기에는 [`sys.exit()`](https://docs.python.org/ko/3.12/library/sys.html#sys.exit "sys.exit")에 의해 발생하는 [`SystemExit`](https://docs.python.org/ko/3.12/library/exceptions.html#SystemExit "SystemExit")와 사용자가 프로그램을 중단하고자 할 때 발생하는 [`KeyboardInterrupt`](https://docs.python.org/ko/3.12/library/exceptions.html#KeyboardInterrupt "KeyboardInterrupt")가 포함됩니다.
- [`Exception`](https://docs.python.org/ko/3.12/library/exceptions.html#Exception "예외")을 와일드카드로 사용하여 (거의) 모든 것을 잡을 수 있습니다. 그러나 처리하려는 예외 유형을 최대한 구체적으로 지정하고 예기치 않은 예외가 전파될 수 있도록 하는 것이 좋습니다.
- [`예외`](https://docs.python.org/ko/3.12/library/exceptions.html#Exception "예외")를 처리하는 가장 일반적인 패턴은 ==예외를 인쇄하거나 로깅한 다음 다시 발생==시키는 것입니다(호출자도 예외를 처리할 수 있도록 허용):

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

- [`try`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#try) ... [`except`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#except) 문에는 선택적 else 절이 있으며, 이 절이 있는 경우 모든 except 절 뒤에 따라야 합니다. 이 옵션은 try 절이 예외를 발생시키지 않는 경우 실행되어야 하는 코드에 유용합니다. 예를 들어
```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

- `else` 절의 사용이 [`try`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#try) 절에 코드를 추가하는 것보다 좋은데, `try` … `except` 문에 의해 보호되고 있는 코드가 일으키지 않은 예외를 우연히 잡게 되는 것을 방지하기 때문입니다.
- 예외 처리기는 try 절에서 즉시 발생하는 예외뿐만 아니라 try 절에서 (간접적으로라도) 호출되는 함수 내부에서 발생하는 예외도 처리합니다. 예를 들어

```python
>>> def this_fails():
…     x = 1/0
…
>>> try:
…     this_fails()
… except ZeroDivisionError as err:
…     print('Handling run-time error:', err)
…
Handling run-time error: division by zero
```

## 예외 일으키기

- [`raise`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#raise) 문은 프로그래머가 지정한 예외가 발생하도록 강제할 수 있게 합니다. 예를 들어:

```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

- [`raise`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#raise)의 유일한 인자는 발생시킬 예외를 나타냅니다. 이것은 예외 인스턴스 또는 예외 클래스(예: [`Exception`](https://docs.python.org/ko/3.12/library/exceptions.html#Exception "예외") 또는 그 서브 클래스 중 하나와 같이 [`BaseException`](https://docs.python.org/ko/3.12/library/exceptions.html#BaseException "BaseException")에서 파생되는 클래스)여야 합니다. 예외 클래스가 전달되면 인자 없이 생성자를 호출하여 암시적으로 인스턴스화됩니다:

```python
raise ValueError  # shorthand for 'raise ValueError()'
```

- 만약 예외가 발생했는지는 알아야 하지만 처리하고 싶지는 않다면, 더 간단한 형태의 [`raise`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#raise) 문이 그 예외를 다시 일으킬 수 있게 합니다:

```python
>>> try:
…     raise NameError('HiThere')
… except NameError:
…     print('An exception flew by!')
…     raise
…
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```

## 예외 연쇄

- 처리되지 않은 예외가 [`except`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#except) 섹션 내에서 발생하면 처리 중인 예외가 첨부되어 오류 메시지에 포함됩니다:

```python
>>> try:
…     open("database.sqlite")
… except OSError:
…     raise RuntimeError("unable to handle error")
…
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'
```

- 위의 예외를 처리하는 동안 또 다른 예외가 발생했습니다:

```python
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: unable to handle error
```

- 예외가 다른 예외의 직접적인 결과임을 나타내기 위해 [`raise`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#raise) 문은 선택적 [`from`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#raise) 절을 허용합니다:

```python
# exc must be exception instance or None.
raise RuntimeError from exc
```

- 이것은 예외를 변환할 때 유용할 수 있습니다. 예를 들면:

```python
>>> def func():
…     raise ConnectionError
…
>>> try:
…     func()
… except ConnectionError as exc:
…     raise RuntimeError('Failed to open database') from exc
…
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```

- 또한 `from None` 관용구를 사용하여 자동 예외 연쇄를 비활성화할 수 있습니다:

```python
>>> try:
…     open('database.sqlite')
… except OSError:
…     raise RuntimeError from None
…
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
```

- 연쇄 메커니즘에 대한 자세한 내용은, [내장 예외](https://docs.python.org/ko/3.12/library/exceptions.html#bltin-exceptions)를 참조하십시오.

## 사용자 정의 예외

- 새 예외 클래스를 만듦으로써 프로그램은 자신의 예외에 이름을 붙일 수 있습니다 (파이썬 클래스에 대한 자세한 내용은 [클래스](https://docs.python.org/ko/3.12/tutorial/classes.html#tut-classes) 를 보세요). 예외는 보통 직접적으로나 간접적으로 [`Exception`](https://docs.python.org/ko/3.12/library/exceptions.html#Exception "Exception") 클래스를 계승합니다.
- 예외 클래스는 다른 클래스가 할 수 있는 모든 작업을 수행하도록 정의할 수 있지만 일반적으로 단순하게 유지되며, 예외 처리기가 오류에 대한 정보를 추출할 수 있는 몇 가지 속성만 제공하는 경우가 많습니다.
- 대부분의 예외는 표준 예외들의 이름들과 유사하게, “Error” 로 끝나는 이름으로 정의됩니다.
- 많은 표준 모듈은 자체적으로 정의한 함수에서 발생할 수 있는 오류를 보고하기 위해 자체 예외를 정의합니다.

## 뒷정리 동작 정의하기

- [`try`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#try) 문은 또 다른 선택적 절을 가질 수 있는데 모든 상황에 실행되어야만 하는 뒷정리 동작을 정의하는 데 사용됩니다. 예를 들어:

```python
>>> try:
…     raise KeyboardInterrupt
… finally:
…     print('Goodbye, world!')
…
Goodbye, world!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
```

- [`finally`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#finally) 절이 있으면, [`try`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#try) 문이 완료되기 전에 `finally` 절이 마지막 작업으로 실행됩니다. `finally` 절은 `try` 문이 예외를 생성하는지와 관계없이 실행됩니다. 다음은 예외가 발생할 때 더 복잡한 경우를 설명합니다:
  
  - `try` 절을 실행하는 동안 예외가 발생하면, [`except`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#except) 절에서 예외를 처리할 수 있습니다. 예외가 `except` 절에서 처리되지 않으면, `finally` 절이 실행된 후 예외가 다시 발생합니다.
  - `except`나 `else` 절 실행 중에 예외가 발생할 수 있습니다. 다시, `finally` 절이 실행된 후 예외가 다시 발생합니다.
  - `finally` 절이 [`break`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#break), [`continue`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#continue) 또는 [`return`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#return) 문을 실행하는 경우 예외가 다시 발생되지 않습니다.
  - `try` 문이 [`break`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#break), [`continue`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#continue) 또는 [`return`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#return) 문에 도달하면, `finally` 절은 `break`, `continue` 또는 `return` 문 실행 직전에 실행됩니다.
  - `finally` 절에 `return` 문이 포함되면, 반환 값은 `try` 절의 `return` 문이 주는 값이 아니라, `finally` 절의 `return` 문이 주는 값이 됩니다.
      

예를 들면:

```python
>>> def bool_return():
…     try:
…         return True
…     finally:
…         return False
…
>>> bool_return()
False
```

더 복잡한 예:

```python
>>> def divide(x, y):
…     try:
…         result = x / y
…     except ZeroDivisionError:
…         print("division by zero!")
…     else:
…         print("result is", result)
…     finally:
…         print("executing finally clause")
…
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

- 보인 바와 같이, [`finally`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#finally) 절은 모든 경우에 실행됩니다. 두 문자열을 나눠서 발생한 [`TypeError`](https://docs.python.org/ko/3.12/library/exceptions.html#TypeError "TypeError") 는 [`except`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#except) 절에 의해 처리되지 않고 `finally` 절이 실행된 후에 다시 일어납니다.
- 실제 세상의 응용 프로그램에서, [`finally`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#finally) 절은 ==외부 자원을 사용할 때, 성공적인지 아닌지와 관계없이, 그 자원을 반납하는 데 유용합니다 (파일이나 네트워크 연결 같은 것들).==

## 미리 정의된 뒷정리 동작들

- 어떤 객체들은 객체가 더 필요 없을 때 개입하는 표준 뒷정리 동작을 정의합니다. 그 객체를 사용하는 연산의 성공 여부와 관계없습니다. 파일을 열고 그 내용을 화면에 인쇄하려고 하는 다음 예를 보세요.

```python
for line in open("myfile.txt"):
    print(line, end="")
```

- 이 코드의 문제점은 이 부분이 실행을 끝낸 뒤에도 예측할 수 없는 기간 동안 파일을 열린 채로 둔다는 것입니다. 간단한 스크립트에서는 문제가 되지 않지만, 큰 응용 프로그램에서는 문제가 될 수 있습니다. [`with`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#with) 문은 파일과 같은 객체들이 즉시 올바르게 뒷정리 되도록 보장하는 방법을 제공합니다.

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

- 문장이 실행된 후에, 줄을 처리하는 데 문제가 발생하더라도, 파일 _f_ 는 항상 닫힙니다. 파일과 같이, 미리 정의된 뒷정리 동작들을 제공하는 객체들은 그들의 설명서에서 이 사실을 설명합니다.

## 서로 관련이 없는 여러 예외 발생 및 처리하기

- 발생한 여러 예외를 보고해야 하는 상황이 있습니다. 동시성 프레임워크에서 여러 작업이 동시에 실패할 수 있는 경우가 많지만, 첫 번째 예외를 발생시키는 대신 실행을 계속하고 여러 오류를 수집하는 것이 바람직한 다른 사용 사례도 있습니다.
- 내장된 ==[`ExceptionGroup`](https://docs.python.org/ko/3.12/library/exceptions.html#ExceptionGroup "ExceptionGroup")은 예외 인스턴스 목록을 래핑하여 함께 발생할 수 있도록== 합니다. 그 자체가 예외이므로 다른 예외처럼 잡을 수 있습니다.

```python
>>> def f():
…     excs = [OSError('error 1'), SystemError('error 2')]
…     raise ExceptionGroup('there were problems', excs)
…
>>> f()
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  |   File "<stdin>", line 3, in f
  | ExceptionGroup: there were problems
  +-+---------------- 1 ----------------
    | OSError: error 1
    +---------------- 2 ----------------
    | SystemError: error 2
    +------------------------------------
>>> try:
…     f()
… except Exception as e:
…     print(f'caught {type(e)}: e')
…
caught <class 'ExceptionGroup'>: e
>>>
```

- `Exception` 대신 `except*`를 사용하면 그룹에서 특정 유형과 일치하는 예외만 선택적으로 처리할 수 있습니다. 중첩된 예외 그룹을 보여주는 다음 예제에서는 각 `except*` 절이 특정 유형의 예외 그룹에서 추출하는 동시에 다른 모든 예외가 다른 절로 전파되어 결국 다시 발생하도록 합니다.
- Python 3.11부터 도입된 `except*` 문법은 여러 예외를 동시에 처리할 수 있는 기능을 제공합니다. 이는 특히 비동기 프로그래밍에서 유용합니다. 기본적인 사용법은 다음과 같습니다:

```python
try:
    # 예외가 발생할 가능성이 있는 코드
except* (TypeError, ValueError) as e:
    # 여러 예외를 동시에 처리
    print(f"예외 발생: {e}")
```

```python
>>> def f():
…     raise ExceptionGroup(
…         "group1",
…         [
…             OSError(1),
…             SystemError(2),
…             ExceptionGroup(
…                 "group2",
…                 [
…                     OSError(3),
…                     RecursionError(4)
…                 ]
…             )
…         ]
…     )
…
>>> try:
…     f()
… except* OSError as e:
…     print("There were OSErrors")
… except* SystemError as e:
…     print("There were SystemErrors")
…
There were OSErrors
There were SystemErrors
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 2, in <module>
  |   File "<stdin>", line 2, in f
  | ExceptionGroup: group1
  +-+---------------- 1 ----------------
    | ExceptionGroup: group2
    +-+---------------- 1 ----------------
      | RecursionError: 4
      +------------------------------------
```

- 예외 그룹에 중첩된 예외는 유형이 아닌 인스턴스여야 한다는 점에 유의하세요. 이는 실제로 예외는 일반적으로 다음과 같은 패턴에 따라 프로그램에서 이미 발생하여 포착된 예외이기 때문입니다:

```python
>>> excs = []
… for test in tests:
…     try:
…         test.run()
…     except Exception as e:
…         excs.append(e)
…
>>> if excs:
…    raise ExceptionGroup("Test Failures", excs)
…
```

## 메모로 예외 강화하기

- 예외가 발생하기 위해 생성되면 일반적으로 발생한 오류를 설명하는 정보로 초기화됩니다. 예외가 발생한 후에 정보를 추가하는 것이 유용한 경우가 있습니다. 이를 위해 예외에는 문자열을 받아 예외의 메모 목록에 추가하는 `add_note(note)` 메서드가 있습니다. 표준 트레이스백 렌더링에는 예외가 추가된 순서대로 모든 메모가 예외 이후에 포함됩니다.

```python
>>> try:
…     raise TypeError('bad type')
… except Exception as e:
…     e.add_note('Add some information')
…     e.add_note('Add some more information')
…     raise
…
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: bad type
Add some information
Add some more information
```

- 예를 들어 예외를 예외 그룹으로 수집할 때 개별 오류에 대한 컨텍스트 정보를 추가할 수 있습니다. 다음에서는 그룹의 각 예외에 해당 오류가 언제 발생했는지를 나타내는 메모가 있습니다.

```python
>>> def f():
…     raise OSError('operation failed')
…
>>> excs = []
>>> for i in range(3):
…     try:
…         f()
…     except Exception as e:
…         e.add_note(f'Happened in Iteration {i+1}')
…         excs.append(e)
…
>>> raise ExceptionGroup('We have some problems', excs)
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  | ExceptionGroup: We have some problems (3 sub-exceptions)
  +-+---------------- 1 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |   File "<stdin>", line 2, in f
    | OSError: operation failed
    | Happened in Iteration 1
    +---------------- 2 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |   File "<stdin>", line 2, in f
    | OSError: operation failed
    | Happened in Iteration 2
    +---------------- 3 ----------------
    | Traceback (most recent call last):
    |   File "<stdin>", line 3, in <module>
    |   File "<stdin>", line 2, in f
    | OSError: operation failed
    | Happened in Iteration 3
    +------------------------------------
```

---
## 참조
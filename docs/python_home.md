---
title: "[Python] 파이썬"
excerpt: 
categories:
  - Python
tags:
  - Software-Language
  - Interpreter-Language
  - Object-Oriented-Programming
  - Python
  - Comment
  - Operator
last_modified_at: 2024-04-11T15:10:55+09:00
link: https://docs.python.org/ko/3/
상위 항목: "[[software_language|소프트웨어 언어 (Software Language)]]"
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

**하위 항목**
- [[python_control|파이썬 제어문 (Python Control)]]
- [[python_environment|파이썬 환경 (Python Environment)]]
- [[python_exception_handling|파이썬 예외 처리 (Python Exception Handling)]]
- [[python_expression|파이썬 표현식 (Python Expression)]]
- [[python_extension|파이썬 확장 (Python Extension)]]
- [[python_input_output|파이썬 입출력 (Python Input & Output)]]
- [[python_language_structure|파이썬 언어 구조 (Python Language Structure)]]
- [[python_module|파이썬 모듈 (Python Module)]]
- [[python_object||파이썬 객체 (Python Object)]]

---
> [[#코딩 스타일]]

- [ ] [[python_library|라이브러리]]
- [ ] 표현식
- [ ] 언어 구조
- [ ] 


# Python 언어

> [!summary]
> > 다음 내용은 Python 언어의 특징을 다룹니다.
> - [[#인터프리터 (Interpreter)]]


- 전문 소프트웨어 개발자라면, 여러 C/C++/Java 라이브러리들을 갖고 작업해야만 할 수 있는데, 일반적인 코드작성/컴파일/테스트/재컴파일 순환이 너무 느리다는 것을 깨닫게 됩니다. 어쩌면 그 라이브러리들을 위한 테스트 스위트를 작성하다가, 테스트 코드 작성에 따분해하는 자신을 발견하게 됩니다. 또는 확장 언어를 사용하는 프로그램을 작성했는데, 완전히 새로운 언어 전체를 설계하고 구현하고 싶지 않을 수 있습니다. 파이썬은 바로 여러분을 위한 언어입니다.
- 이러한 작업 중 일부는 Unix 셸 스크립트나 Windows 배치 파일을 작성할 수 있지만 셸 스크립트는 파일을 이동하고 텍스트 데이터를 변경하는 데 가장 적합하며 GUI 애플리케이션이나 게임에는 적합하지 않습니다. C/C++/Java 프로그램을 작성할 수도 있지만 초안을 작성하는 데도 많은 개발 시간이 소요될 수 있습니다. Python은 사용이 간편하고 Windows, macOS, Unix 운영 체제에서 사용할 수 있으며 작업을 더 빠르게 완료하는 데 도움이 됩니다.
- 파이썬은 사용이 간단하지만, 제대로 갖춰진 프로그래밍 언어인데, 셸 스크립트나 배치 파일보다 더 많은 구조를 제공하고 커다란 프로그램을 위한 지원을 제공합니다. 반면에, 파이썬은 C보다 훨씬 많은 에러 검사를 제공하고, 유연한 배열과 딕셔너리같은 고수준의 자료형들을 내장하고 있습니다. 더 일반적인 자료형들 때문에 Awk 나 Perl보다도 더 많은 문제영역에 쓸모가 있는데, 그러면서도 여전히 많은 것들이 적어도 이들 언어를 사용하는 것만큼 파이썬에서도 쉽게 해결할 수 있습니다.
- 파이썬은 여러분의 프로그램을 여러 모듈로 나눌 수 있도록 하는데, 각 모듈은 다른 파이썬 프로그램에서 재사용할 수 있습니다. 대규모의 표준 모듈들이 따라오는데 여러분의 프로그램 기초로 사용하거나 파이썬 프로그래밍을 배우기 위한 예제로 활용할 수 있습니다. 이 모듈에는 파일 입출력, 시스템 호출, 소켓들이 포함되는데, 심지어 Tk 와 같은 GUI 도구상자에 대한 인터페이스도 들어있습니다.
- 파이썬은 인터프리터 언어입니다. 컴파일과 링크 단계가 필요 없으므로 개발 시간을 상당히 단축해줍니다. 인터프리터는 대화형으로 사용할 수 있어서, 언어의 기능을 실험하거나, 쓰고 버릴 프로그램을 만들거나, 바닥부터 프로그램을 만들어가는 동안 함수들을 테스트하기 쉽습니다. 간편한 탁상용 계산기이기도 합니다.
- 파이썬은 간결하고 읽기 쉽게 프로그램을 작성할 수 있도록 합니다. 파이썬 프로그램은 여러 가지 이유로 같은 기능의 C, C++, Java 프로그램들에 비교해 간결합니다:
  
  1. 고수준의 자료형 때문에 복잡한 연산을 한 문장으로 표현할 수 있습니다;
  2. 문장의 묶음은 괄호 대신에 들여쓰기를 통해 이루어집니다;
  3. 변수나 인자의 선언이 필요 없다.
  
- 파이썬은 _확장 가능_ 하다: C로 프로그램하는 법을 안다면, 인터프리터에 새로운 내장 함수나 자료형을 추가해서, 핵심 연산을 최대 속도로 수행하거나 바이너리 형태로만 제공되는 라이브러리(가령 업체가 제공하는 그래픽스 라이브러리)에 파이썬 프로그램을 연결할 수 있습니다. 진짜 파이썬에 매료되었다면, C로 만든 응용 프로그램에 파이썬 인터프리터를 연결하여 그 응용 프로그램의 확장이나 명령 언어로 사용할 수 있습니다.
- 파이썬 이라는 이름은 “Monty Python’s Flying Circus”라는 BBC 쇼에서 따온 것이고, 파충류와는 아무런 관련이 없습니다. 문서에서 Monty Python의 농담을 인용하는 것은 허락된 것일 뿐만 아니라, 권장되고 있습니다.


## 인터프리터 (Interpreter)

- 파이썬 인터프리터는 일반적으로 사용할 수 있는 Linux 시스템에서 `/usr/local/bin/python3.12`로 설치되며, 유닉스 셸의 검색 경로에 `/usr/local/bin`을 넣으면 명령을 입력하여 시작할 수 있습니다:
  
  `python3.12`
  
  을 셸에 입력해서 실행할 수 있습니다. 인터프리터가 위치하는 디렉터리의 선택은 설치 옵션이기 때문에, 다른 장소도 가능합니다; 주변의 파이썬 전문가나 시스템 관리자에게 확인할 필요가 있습니다. (예를 들어, `/usr/local/python` 도 널리 사용되는 위치입니다.)

- [Microsoft Store](https://docs.python.org/ko/3.12/using/windows.html#windows-store)에서 파이썬을 설치한 Windows 컴퓨터에서는 `python3.12` 명령어를 사용할 수 있습니다. [py.exe 런처](https://docs.python.org/ko/3.12/using/windows.html#launcher)가 설치되어 있는 경우 `py` 명령을 사용할 수 있습니다. Python을 실행하는 다른 방법은 [보충 설명: 환경 변수 설정하기](https://docs.python.org/ko/3.12/using/windows.html#setting-envvars)를 참조하세요.
- 기본 프롬프트에서 EOF(end-of-file) 문자(유닉스에서는 Control-D, 윈도우에서는 Control-Z)를 입력하면 인터프리터가 종료하고, 종료 상태 코드는 0 이 됩니다. 이 방법이 통하지 않는다면 `quit()` 명령을 입력해서 인터프리터를 종료시킬 수 있습니다.
- 인터프리터는 [GNU Readline](https://tiswww.case.edu/php/chet/readline/rltop.html) 라이브러리를 지원하는 시스템에서 줄 편집 기능으로 대화형 편집, 히스토리 치환, 코드 완성 등을 제공합니다. 아마도 명령행 편집이 제공되는지 확인하는 가장 빠른 방법은 첫 프롬프트에서 Control-P 를 입력하는 것입니다. 삑 하는 소리가 난다면 명령행 편집이 지원되고 있습니다; 입력 키에 대한 소개는 부록 [대화형 입력 편집 및 히스토리 치환](https://docs.python.org/ko/3.12/tutorial/interactive.html#tut-interacting) 을 보세요. 아무런 반응도 없거나 `^P` 가 출력된다면 명령행 편집이 제공되지 않는 것입니다; 현재 줄에서 문자를 지우기 위해 백스페이스를 사용할 수 있는 것이 전부입니다.
- 인터프리터는 어느 정도 유닉스 셸처럼 동작합니다: tty 장치에 표준 입력이 연결된 상태로 실행되면, 대화형으로 명령을 읽고 실행합니다; 파일명을 인자로 주거나 파일을 표준입력으로 연결한 상태로 실행되면 스크립트를 읽고 실행합니다.
- 인터프리터를 시작하는 두 번째 방법은 셸의 [`-c`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-c) 옵션과 유사하게 _command_ 에 있는 문을 실행하는 `python -c command [arg] …`입니다. 파이썬 문에는 공백이나 셸에 고유한 다른 문자가 포함되는 경우가 많으므로 일반적으로 _command_ 전체를 인용하는 것이 좋습니다.
- 몇몇 파이썬 모듈들은 스크립트로도 쓸모가 있습니다. `python -m module [arg] …` 로 실행할 수 있는데, 마치 _module_ 모듈 소스 파일의 경로명을 명령행에 입력한 것처럼 실행되게 됩니다.
- 스크립트 파일이 사용될 때, 때로 스크립트를 실행한 후에 대화형 모드로 들어가는 것이 편리할 때가 있습니다. 스크립트 앞에 [`-i`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-i) 를 전달하면 됩니다.
- 모든 명령행 옵션은 [명령 줄과 환경](https://docs.python.org/ko/3.12/using/cmdline.html#using-on-general) 에서 찾을 수 있습니다.

### 인자 전달
- 스크립트 이름과 추가의 인자들이 인터프리터로 전달될 때, 문자열의 목록으로 변환된 후 `sys` 모듈의 `argv` 변수에 저장됩니다. `import sys` 를 사용해서 이 목록에 접근할 수 있습니다. 
- 목록의 길이는 최소한 1이고, 스크립트도 추가의 인자도 없는 경우로, `sys.argv[0]` 은 빈 문자열입니다. 
- 스크립트 이름을 `'-'` (표준 입력을 뜻한다) 로 주면 `sys.argv[0]` 는 `'-'` 가 됩니다. [`-c`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-c) _command_ 가 사용되면 `sys.argv[0]` 는 `'-c'` 로 설정됩니다. [`-m`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-m) _module_ 이 사용되면 `sys.argv[0]` 는 모듈의 절대 경로명이 됩니다. [`-c`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-c) _command_ 나 [`-m`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-m) _module_ 뒤에 오는 옵션들은 파이썬 인터프리터가 소모하지 않고 명령이나 모듈이 처리하도록 `sys.argv` 로 전달됩니다.

### 대화형 모드
- 명령을 tty 에서 읽을 때, 인터프리터가 _대화형 모드_ 로 동작한다고 말합니다. 이 모드에서는 _기본 프롬프트_ 를 표시해서 다음 명령을 요청하는데, 보통 세 개의 …보다 크다 기호입니다 (`>>>`); 한 줄로 끝나지 않고 이어지는 줄의 입력을 요청할 때는 보조 프롬프트가 사용되는데, 기본적으로 세 개의 점입니다 (`…`). 인터프리터는 첫 번째 프롬프트를 인쇄하기 전에 버전 번호와 저작권 공지를 포함하는 환영 메시지를 출력합니다.

```python
$ python3.12
Python 3.12 (default, April 4 2022, 09:25:04)
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

- 이어지는 줄은 여러 줄로 구성된 구조물을 입력할 때 필요합니다. 예를 들자면, 이런 식의 [`if`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#if) 문이 가능합니다:

```python
>>> the_world_is_flat = True
>>> if the_world_is_flat:
…     print("Be careful not to fall off!")
…
Be careful not to fall off!
```

- 대화형 모드에 대해 더 알고 싶다면, [대화형 모드](https://docs.python.org/ko/3.12/tutorial/appendix.html#tut-interac) 를 보세요.

### 인터프리터와 환경
#### 소스 코드 인코딩
- 기본적으로, 파이썬 소스 파일들은 UTF-8으로 인코드 된 것으로 취급됩니다. 이 인코딩에서는 대부분 언어에서 사용되는 문자들을 문자열 상수, 식별자, 주석 등에서 함께 사용할 수 있습니다. (하지만 표준 라이브러리는 오직 ASCII 문자만 식별자로 사용하고 있는데, 범용 코드에서는 이 관례를 따르는 것이 좋습니다.) 이 문자들을 모두 올바로 표시하기 위해서는 편집기가 파일이 UTF-8임을 인식해야 하고, 이 파일에 포함된 모든 문자를 지원할 수 있는 글꼴을 사용해야 합니다.
- 인코딩을 기본값 외의 것으로 선언하려면, 파일의 첫 줄에 특별한 형태의 주석 문을 추가해야 합니다. 문법은 이렇습니다:

```python
# -*coding: encoding -*_encoding_ 은 파이썬이 지원하는 코덱 ([`codecs`](https://docs.python.org/ko/3.12/library/codecs.html#module-codecs "codecs: Encode and decode data and streams.")) 중 하나여야 합니다.
```

- 예를 들어, Windows-1252 인코딩을 사용하도록 선언하려면, 소스 코드 파일의 첫 줄은 이렇게 되어야 합니다:

```python
# -*coding: cp1252 -*-
```

- 첫 줄 규칙의 한가지 예외는 소스 코드가 [유닉스 “셔뱅 (shebang)” 줄](https://docs.python.org/ko/3.12/tutorial/appendix.html#tut-scripts) 로 시작하는 경우입니다. 이 경우에, 인코딩 선언은 두 번째 줄에 들어갑니다. 예를 들어:

```python
#!/usr/bin/env python3
# -*coding: cp1252 -*-
```

---
# Python 초급
> [!summary]
> > 다음 내용은 Python 프로그램을 구성하는 기본적인 문법을 다룹니다.
> > Python을 사용한다면 반드시 알아야 할 내용입니다.
> - [[#주석 (Comment)]]
> - [[#변수 (Variable) python_variable (자세히 보기)|변수 (Variable)]]
> - [[#제어문 (Control) python_control (자세히 보기)|제어문 (Control)]]


> [!NOTE] 문자 입출력
> ```python
> print("Hello world")
> ```
> - `print` 함수로 메시지를 출력할 수 있습니다.
> 
> ```python
> variable = input("설명 메시지")
> ```
> - `input`은 입력한 값을 문자열 (`str`) 타입으로 저장합니다.
> - `"설명 메시지"`는 설명을 위해 출력할 메시지를 결정합니다.
> - 프로그램의 출력을 표현하는 여러 가지 방법이 있습니다; 사람이 일기에 적합한 형태로 데이터를 인쇄할 수도 있고, 나중에 사용하기 위해 파일에 쓸 수도 있습니다.

## 주석 (Comment)

```python
# 이 문장은 주석입니다.
```

- `#` 기호를 사용하여 주석을 작성할 수 있습니다.

## 변수 (Variable) [[python_variable|(자세히 보기)]]
```python
variable = value
```

- 메모리에 존재하는 대상들을 객체라고 합니다.
- 데이터 값을 가리키는 객체, 가리키는 대상이 변할 수 있습니다.
- Python 에서는 Function, Class 등 모든 것을 객체로 나타냅니다.
- 변수에 저장된 값으로 스스로 판단하여 자료형을 지정합니다.

### 숫자 (Numeric)

```python
i = 12
print(i) # int, 결과: 12

f = 1.23
print(f) # float, 결과: 1.23
```

- Python 은 정수를 `int` 로 나타낸다. (나타낼 수 있는 최대 길이에 제한이 없다.)
- 실수 타입은 `float`, 복소수 타입은 `complex` 로 나타낸다.
- `-x` 와 같이 `-` 를 붙이면 음수로 나타낼 수 있다.

| 산술 연산자       | 의미                                |
| ------------ | --------------------------------- |
| `+`          | 덧셈                                |
| `-`          | 뺄셈                                |
| `*`          | 곱셈                                |
| `**`         | 제곱                                |
| `/`          | 나눗셈                               |
| `//`         | 몫                                 |
| `%`          | 나머지                               |
#### 대입 연산자 (Assignment Operator)
- 변수를 선언하고 값을 할당할 때 사용합니다.

| 연산자   | 내용                      |
| ----- | ----------------------- |
| `=`   | 좌변에 우변 값 할당             |
| `+=`  | 좌변 값에 우변 값을 더하여 할당      |
| `-=`  | 좌변 값에 우변 값을 빼서 할당       |
| `*=`  | 좌변 값에 우변 값을 곱해서 할당      |
| `/=`  | 좌변 값에 우변 값을 나눠서 할당      |
| `%=`  | 좌변 값을 우변 값으로 나눈 나머지 할당  |
| `//=` | 좌변 값을 우변 값으로 나눈 몫 할당    |
| `**=` | 좌변 값을 우변 값으로 지수 연산하여 할당 |

### 논리 (Boolean)

```python
b = True
print(b) # 결과: True
```

- 참과 거짓을 표현하는 데이터 타입, `bool` 로 나타낸다.
- 위 연산자의 결과에 따라 `True` 와 `False` 로 반환한다.
- `is`, `is not` 의 경우 단순히 값이 같은 것 뿐만 아니라 같은 메모리 주소에 할당된 같은 객체인지 확인한다.

| 비교 연산자 | 의미 |
| ---- | ---- |
| `x > y` | x 가 y 보다 큰지 여부 |
| `x >= y` | x 가 y 보다 크거나 같은지 여부 |
| `x < y` | x 가 y 보다 작은지 여부 |
| `x <= y` | x 가 y 보다 작거나 같은지 여부 |
| `x == y` | x 와 y 가 같은지 여부 |
| `x!= y` | x 와 y 가 다른지 여부 |
| `x is y` | x 와 y 가 같은 객체인지 여부 |
| `x is not y` | x 와 y 가 다른 객체인지 여부 |

| 논리 연산자    | 의미                                               |
| --------- | ------------------------------------------------ |
| `x or y`  | x 또는 y 가 `True` 인가?                              |
| `x and y` | x 와 y 모두 `True` 인가?                              |
| `not x`   | x 가 `True` 라면 `False`, `False` 라면 `True` 를 반환한다. |

### 문자열 (String) [[Software/Code/Language/Python/Object/Variable/python_string|(자세히 보기)]]
- 파이썬의 텍스트 데이터는 [`str`](https://docs.python.org/ko/3.12/library/stdtypes.html#str "str"), 또는 _문자열 (strings)_, 객체를 사용하여 처리됩니다. 문자열은 유니코드 코드 포인트의 불변 [시퀀스](https://docs.python.org/ko/3.12/library/stdtypes.html#typesseq) 입니다. 

```python
s = "Hello"
print(s) # 결과: "Hello"

string = """
H
E
L
L
O
"""
print(string)
```

- 문자열 리터럴은 다양한 방법으로 작성됩니다:
  
  작은따옴표: `'"큰" 따옴표를 담을 수 있습니다'`
  Double quotes: `"allows embedded 'single' quotes"`
  삼중 따옴표: `'''세 개의 작은따옴표'''`, `"""세 개의 큰따옴표"""`

- 삼중 따옴표로 묶인 문자열은 여러 줄에 걸쳐있을 수 있습니다 - 연관된 모든 공백이 문자열 리터럴에 포함됩니다.
- 단일 표현식의 일부이고 그 들 사이에 공백만 있는 문자열 리터럴은 묵시적으로 단일 문자열 리터럴로 변환됩니다. 즉, `("spam " "eggs") == "spam eggs"`.
- 문자열은 [`str`](https://docs.python.org/ko/3.12/library/stdtypes.html#str "str") 생성자를 사용하여 다른 객체로부터 만들어질 수도 있습니다.
- 별도의 `char` 형이 없으므로 문자열을 인덱싱하면 길이가 1인 문자열이 생성됩니다. 

### 리스트 (List) [[Software/Code/Language/Python/Object/Variable/python_list|(자세히 보기)]]
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

##### 인덱스 (Index)
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

##### 중첩 리스트

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
### 튜플 (Tuple)
- 리스트와 문자열이 인덱싱과 슬라이싱 연산과 같은 많은 성질을 공유함을 보았습니다. 이것들은 _시퀀스_ 자료 형의 두 가지 예입니다 ([시퀀스 형 — list, tuple, range](https://docs.python.org/ko/3.12/library/stdtypes.html#typesseq) 를 보세요). 파이썬은 진화하는 언어이기 때문에, 다른 시퀀스 자료형이 추가될 수도 있습니다. 다른 표준 시퀀스 자료 형이 있습니다: _튜플_ 입니다.
- 튜플은 쉼표로 구분되는 여러 값으로 구성됩니다. 예를 들어:

```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
>>> u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
>>> t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
>>> v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```

- 여러분이 보듯이, 출력되는 튜플은 항상 괄호로 둘러싸입니다, 그래서 중첩된 튜플이 올바르게 해석됩니다; 종종 괄호가 필요하기는 하지만 (튜플이 더 큰 표현식의 일부일 때), 둘러싼 괄호와 함께 또는 없이 입력될 수 있습니다. 튜플의 개별 항목에 대입하는 것은 가능하지 않지만, 리스트 같은 가변 객체를 포함하는 튜플을 만들 수는 있습니다.

```python
TUPLE_A = '배트맨', 1989, '슈퍼맨II' , 1980
TUPLE_B = ('배트맨', 1989, '슈퍼맨II' , 1980)
TUPLE_C = tuple(['배트맨', 1989, '슈퍼맨II' , 1980])

print(TUPLE_A)
print(TUPLE_B)
print(TUPLE_C)

TUPLE_A[3] = 1981 # 에러 발생
```

- 처음 객체를 생성하면 이후에는 내부의 값 변경이 불가능한 자료 구조입니다. 값 변경이 불가능한 것 외에는 List 와 유사합니다. 튜플이 리스트처럼 보인다 하더라도, 이것들은 다른 상황에서 다른 목적으로 사용됩니다.
- 일반적으로 서로 다른 (heterogeneous) 종류의 데이터 타입으로 이루어진 항목들을 변수에 바로 할당하는 요소들은 언패킹이나 인덱싱 (또는 [`네임드 튜플`](https://docs.python.org/ko/3.12/library/collections.html#collections.namedtuple "collections.namedtuple") 의 경우는 어트리뷰트로도) 용도로 사용합니다.
  리스트는 [가변](https://docs.python.org/ko/3.12/glossary.html#term-mutable) 이고, 요소들은 보통 등질 적이고 리스트에 대한 이터레이션으로 액세스 됩니다.
- 열거형 데이터가 필요할 때 값의 변경이 필요하지 않을 경우 List 보다 Tuple 타입을 사용하는 것이 속도가 빨라 성능에 더 유리합니다.
- `()` 로 감싸거나 괄호를 사용하지 않고 `,` 를 사용하여 Tuple 을 생성할 수 있으며 `tuple()`로도 생성할 수 있습니다.
- 특별한 문제는 비었거나 하나의 항목을 갖는 튜플을 만드는 것입니다: 이 경우를 수용하기 위해 문법은 추가적인 예외 사항을 갖고 있습니다. 빈 튜플은 빈 괄호 쌍으로 만들어집니다; 하나의 항목으로 구성된 튜플은 값 뒤에 쉼표를 붙여서 만듭니다 (값 하나를 괄호로 둘러싸기만 하는 것으로는 충분하지 않습니다). 추합니다, 하지만 효과적입니다. 예를 들어:

```python
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
```

```python
TUPLE_EMPTY_A = () # Tuple 타입
TUPLE_EMPTY_B = tuple() # Tuple 타입
TUPLE_A = 'Hello', # Tuple 타입
NOT_TUPLE = ('Hello') # String 타입
```

- 빈 Tuple 을 생성할 경우 `()` 만 할당하거나 `tuple()` 을 사용하면 된다.
- 하나의 값만 할당할 경우 끝에 `,` 를 사용해야 한다. `,` 를 붙이지 않거나 하나의 값에 `()` 를 사용할 경우 입력한 값의 타입으로 생성된다.

```python
TUPLE_A = [1, 2, 3], [4, 5, 6]
TUPLE_A[1][2] = 7
print(TUPLE_A) # 결과: [1, 2, 3], [4, 5, 7]
```

- Tuple 에 포함된 값은 변경이 불가능하지만 리스트를 값으로 가질 경우 리스트 내부의 값은 변경할 수 있다.
- Tuple 이 값으로 갖는 것은 List 의 주소이다. List 는 값이 변경한 자료 구조이므로 내부 값을 변경해도 Tuple 의 규칙에 위배되지 않는다.

##### Unpacking

```python
TUPLE_A = '배트맨', 1989, '슈퍼맨II' , 1980
a, b, c, d = TUPLE_A
print(a) # 결과: '배트맨'
print(b) # 결과: 1989
print(c) # 결과: '슈퍼맨II'
print(d) # 결과: 1980
```

- 위의 `TUPLE_A` 처럼 여러 값들을 하나의 변수에 할당하는 것을 **Packing**이라고 합니다. 문장 `t = 12345, 54321, 'hello!'` 는 _튜플 패킹_ 의 예입니다: 값 `12345`, `54321`, `'hello!'` 는 함께 튜플로 패킹 됩니다. 반대 연산 또한 가능합니다:

```python
x, y, z = t
```

- `a, b, c, d = TUPLE_A` 처럼 Packing 한 변수를 활용하여 여러 변수에 동시에 값을 할당하는 것을 **Unpacking**이라 합니다. 시퀀스 언 패킹 이라고 불리고 오른쪽에 어떤 시퀀스가 와도 됩니다. 시퀀스 언 패킹은 등호의 좌변에 시퀀스에 있는 요소들과 같은 개수의 변수들이 올 것을 요구합니다. 다중 대입은 사실 튜플 패킹과 시퀀스 언 패킹의 조합일뿐이라는 것에 유의하세요.

### 집합 (Set)

- 파이썬은 _집합_ 을 위한 자료 형도 포함합니다. 집합은 중복되는 요소가 없는 순서 없는 컬렉션입니다. 기본적인 용도는 멤버십 검사와 중복 항목 제거입니다. 집합 객체는 합집합, 교집합, 차집합, 대칭 차집합과 같은 수학적인 연산들도 지원합니다. 수학의 합집합 (`|`), 교집합 (`&`), 차집합 (`-`), 여집합 (`^`) 을 구현할 수 있습니다.
- 집합을 만들 때는 `{VALUE1, VALUE2}` 와 같이 중괄호 `{}`를 사용하거나 [`set()`](https://docs.python.org/ko/3.12/library/stdtypes.html#set "set") 함수를 사용할 수 있습니다. 

> [!warning] 
> - 빈 집합을 만들려면 `set()` 을 사용해야 합니다. `{}` 가 아닙니다; 후자는 빈 딕셔너리를 만듭니다.

- Index 가 없으며 중복이 허용되지 않는 데이터 집합입니다. Index 가 없으므로 순서가 존재하지 않습니다.
- Dictionary 의 생성 문법과 겹쳐서 `{}` 만으로는 빈 Set 를 생성할 수 없다. `set()` 로만 빈 Set 를 생성할 수 있다.

```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
>>>
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

- [[Software/Code/Language/Python/Object/Variable/python_list|리스트 컴프리헨션]] 과 유사하게, 집합 컴프리헨션도 지원됩니다:

```python
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```

| 메서드                   | 설명           |
| --------------------- | ------------ |
| `add(값)`              | 값 추가         |
| `update([값1, 값2, …])` | 여러 값 한 번에 추가 |
| `remove(값)`           | 특정 값 제거      |


### 딕셔너리 (Dictionary)
- 파이썬에 내장된 또 다른 유용한 데이터 유형은 dictionary입니다([매핑 형 - 딕셔너리](https://docs.python.org/ko/3.12/library/stdtypes.html#typesmapping) 참조). 딕셔너리는 다른 언어에서 Map 타입, “연관 메모리” 또는 “연관 배열”로 불리기도 합니다. 

```python
DICTIONARY_A = {'blue': 3, 'red': 4, 'green': 5}
DICTIONARY_B = dict([('brown', 3), ('gray', 7)])
DICTIONARY_C = dict(brown=3, gray=7)
DICTIONARY_EMPTY_A = {} # Dictionary 타입
DICTIONARY_EMPTY_B = dict() # Dictionary 타입
```

- 숫자 범위로 색인되는 시퀀스와 달리 딕셔너리는 key로 색인되며, 이는 어떤 불변의 유형이든 될 수 있습니다(문자열과 숫자는 항상 키가 될 수 있습니다). 문자열, 숫자 또는 튜플만 포함된 경우 튜플을 키로 사용할 수 있으며, 튜플에 직접 또는 간접적으로 변경 가능한 객체가 포함된 경우 키로 사용할 수 없습니다. 
  리스트는 인덱스 할당, 슬라이스 할당 또는 `append()` 및 `extend()`와 같은 메서드를 사용하여 제자리에서 수정할 수 있으므로 리스트를 키로 사용할 수 없습니다.
- 다른 타입처럼 숫자 Index 가 자동으로 적용되지 않으므로 순서가 존재하지 않습니다.
- `key:value` 와 같이 `:` 를 사용하여 표기합니다. 딕셔너리를 (한 딕셔너리 안에서) 키가 중복되지 않는다는 제약 조건을 가진 _키: 값_ 쌍의 집합으로 생각하는 것이 최선입니다. 
- 중괄호 쌍은 빈 딕셔너리를 만듭니다: `{}`. 각 쌍은 `,` 로 구분하며 `{}` 로 감싸서 선언합니다. 중괄호 안에 쉼표로 분리된 키:값 쌍들의 목록을 넣으면, 딕셔너리에 초기 키:값 쌍들을 제공합니다; 이것이 딕셔너리가 출력되는 방식이기도 합니다. 혹은 `dict` 함수를 사용하여 생성할 수 있습니다. 이 경우 Key 와 Value 가 구분되도록 입력해야 합니다.
- 숫자로는 값들을 구분하기 힘들 때 주로 사용합니다. 단순한 숫자 Index 로도 충분할 경우 Dictionary 타입은 오히려 성능에 악영향을 줍니다.
- 딕셔너리의 주 연산은 값을 키와 함께 저장하고 주어진 키로 값을 추출하는 것입니다. `del` 로 키:값 쌍을 삭제하는 것도 가능합니다. 이미 사용하고 있는 키로 저장하면, 그 키로 저장된 예전 값은 잊힙니다. 존재하지 않는 키로 값을 추출하는 것은 에러입니다.
- 딕셔러리에 `list(d)` 를 수행하면 딕셔너리에서 사용되고 있는 모든 키의 리스트를 삽입 순서대로 돌려줍니다 (정렬을 원하면 대신 `sorted(d)` 를 사용하면 됩니다). 하나의 키가 딕셔너리에 있는지 검사하려면, [`in`](https://docs.python.org/ko/3.12/reference/expressions.html#in) 키워드들 사용하세요.

```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```

- [`dict()`](https://docs.python.org/ko/3.12/library/stdtypes.html#dict "dict") 생성자는 키-값 쌍들의 시퀀스로 부터 직접 딕셔너리를 구성합니다.

```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

- 이에 더해, 딕셔너리 컴프리헨션은 임의의 키와 값 표현식들로 부터 딕셔너리를 만드는데 사용될 수 있습니다:

```python
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

- 키가 간단한 문자열일 때, 때로 키워드 인자들을 사용해서 쌍을 지정하기가 쉽습니다:

```python
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

```python
DICTIONARY_A = {'blue': 3, 'red': 4, 'green': 5}
print(DICTIONARY_A['blue']) # 결과: 3

DICTIONARY_A['black'] = 1
print(DICTIONARY_A) # 결과: {'blue': 3, 'red': 4, 'green': 5, 'black' = 1}

del DICTIONARY_A['green']
print(DICTIONARY_A) # 결과: {'blue': 3, 'red': 4, 'black' = 1}

DICTIONARY_A['black'] = 5
print(DICTIONARY_A) # 결과: {'blue': 3, 'red': 4, 'black' = 5}
```

- `DICTIONARY[KEY] = VALUE` 로 새로운 값을 추가할 수 있습니다.
- `del DICTIONARY[KEY]` 로 `KEY` 를 갖는 쌍을 제거할 수 있습니다.
- 기존에 있던 `KEY` 에 새로운 값을 할당하면 기존 값을 변경할 수 있습니다.

```python
DICTIONARY_A = {'blue': 3, 'red': 4, 'green': 5}
print(3 in DICTIONARY_A) # 결과: False
```

- `in` 을 사용할 경우 key 값을 기준으로 참/거짓을 판단합니다.


## 제어문 (Control) [[python_control|(자세히 보기)]]
- Python 의 제어문은 다른 언어의 `{ }` 대신 `:` 과 **들여쓰기**로 처리합니다.

| 연산자 / 예약어  | 설명                |
| ---------- | ----------------- |
| x < y      | x 가 y 보다 작다.      |
| x > y      | x 가 y 보다 크다.      |
| x == y     | x 와 y 가 같다.       |
| x != y     | x 와 y 가 같지 않다.    |
| x >= y     | x 가 y 보다 크거나 같다.  |
| x <= y     | x 가 y 보다 작거나 같다.  |
| x or y     | x 또는 y 가 참이면 참    |
| x and y    | x 와 y 가 모두 참이면 참  |
| not x      | x 가 거짓이면 참        |
| x in A     | x 가 A 의 요소로 있으면 참 |
| x not in A | x 가 A 의 요소가 아니면 참 |

> [!NOTE] `in`
> 
> ```python
> LIST = [1, 2, 3, 4]
> print(2 in LIST) # 결과: True
> ```
> 
> - 열거형 데이터에는 `in` 을 사용할 수 있다. 해당 데이터에 입력한 값이 존재하면 `True`, 이외에는 `False` 를 반환한다.


### 조건문 (Condition)

#### `if`

```python
if 조건문:
	<실행할 문장>
elif 조건문:
	<실행할 문장>
elif 조건문:
	<실행할 문장>
else:
	<실행할 문장>
```

- if 문에 속하는 문장에는 모두 들여쓰기 (indentation) 를 해야 합니다. 들여쓰기 정도를 통일시켜야 합니다. (커뮤니티에서는 Spacebar 4 번을 권장합니다.)
- 위에서부터 조건을 확인하여 처음으로 만족한 블록만 실행합니다.
- 모든 조건을 만족하지 못했을 경우 `else` 블록이 실행됩니다.

```python
if 조건문1:
    if 조건문 2:
        <실행할 문장 1>
    <실행할 문장 2>
else:
    <실행할 문장 3>
```

- `if` 조건문 내에 또 다른 `if` 조건문을 사용할 수 있다.

```python
if 조건문: <실행할 문장>
<조건문이 참일 때 실행할 문장> if 조건문 else <조건문이 거짓일 때 실행할 문장>
```

- `if` 조건문을 한 줄로 나타내고 싶을 경우 위처럼 사용할 수 있다.

```python
message = "success" if score >= 60 else "failure" # 60 이상이면 success, 미만이면 failure가 할당
```

- 변수에 값을 할당할 때 `if` 조건문의 결과를 적용할 수 있다.

```python
if not line: break
```

- `if` 의 조건에 `not` 을 적용할 수 있다.

#### `match`
- [`match`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#match) 문은 표현식을 받아 그 값을 하나 이상의 대소문자 블록으로 주어진 연속 패턴과 비교합니다. 이는 표면적으로는 C, Java 또는 JavaScript(및 기타 여러 언어)의 switch 문과 비슷하지만, Rust나 Haskell 같은 언어의 패턴 매칭과 더 유사합니다. 일치하는 첫 번째 패턴만 실행되며 값에서 구성 요소(시퀀스 요소 또는 객체 속성)를 변수로 추출할 수도 있습니다.
- 가장 간단한 형태는 주제 값을 하나 이상의 리터럴과 비교하는 것입니다:

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```

- 마지막 블록에 주목하세요. “변수 이름” `_`은 _와일드카드_ 역할을 하며 절대 일치하지 않습니다. 대소문자가 일치하지 않으면 브랜치 중 어느 것도 실행되지 않습니다.
- '`|`(“또는”)를 사용하여 여러 리터럴을 하나의 패턴으로 결합할 수 있습니다:

```python
case 401 | 403 | 404:
    return "Not allowed"
```

- 패턴은 할당 풀기처럼 보일 수 있으며 변수를 바인딩하는 데 사용할 수 있습니다:

```python
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
```

- 이 패턴을 주의 깊게 살펴보세요! 첫 번째 패턴은 두 개의 리터럴이 있으며, 위에 표시된 리터럴 패턴의 확장으로 생각할 수 있습니다. 하지만 다음 두 패턴은 리터럴과 변수를 결합하고, 변수는 주어(`point`)의 값을 바인딩합니다. 네 번째 패턴은 두 개의 값을 캡처하므로 개념적으로 언패킹 할당 `(x, y) = point`와 유사합니다.

### 반복문 (Loop)

#### `while`

```python
while 조건문:
    실행할 문장1
    실행할 문장2
    실행할 문장3
```

- 조건문을 만족하는 동안 계속 실행한다. (조건문을 만족하지 않으면 한 번도 실행하지 않는다.)
- 조건문을 True 로 두면 무한 루프를 만들 수 있다. (Python IDLE 에서는 Ctrl + C 로 빠져나갈 수 있다.)

#### `for`

```python
for <value> in <iterable>:
	수행할 문장1
	수행할 문장2
```

- `<value>` 에 `list`, `tuple`, `string` 과 같은 `iterable` 에서 값들을 순서대로 `value` 에 대입하여 반복한다.
- 특히 `range` 함수와 함께 자주 쓰인다.

> [!NOTE] `range`
> `for` 반복문에 많이 사용된다. `for({start}, end, {step})` 의 문법을 갖는다.
>
> ```python
> range(5) # 0부터 4까지의 정수
> range(1, 10) # 1부터 9까지의 정수
> range(10, 1, -2) # 10부터 2까지 -2씩 감소
> ```

```python
for <value1> in <iterable1>:
    for <value2> in <iterable2>:
        실행할 문장
```

- `for` 반복문 역시 중첩으로 사용할 수 있다.

```python
# 리스트 내포
[표현식 for <value> in <iterable> if 조건문]

# 리스트 내포 (for 문 여러 개)
[표현식 for <value>1 in <iterable1> if 조건문1
표현식 for <value>2 in <iterable2> if 조건문2
표현식 for <value>n in <iterable3> if 조건문n]
```

- `for` 문을 이용하여 리스트에 값을 바로 입력할 수 있다. (리스트 내포)
- 하나의 리스트에 `for` 문을 여러 개 사용할 수도 있다.

```python
squares = []
for x in range(10):
	squares.append(x**2)

new_squares = [y**2 for y in range(10)]
```

- 리스트에 값을 입력할 경우 리스트 내포를 활용하는 것이 더 유리하다.

```python
SET = {x for x in 'abracadabra' if x not in 'abc'}
pairs = [(a, b) for a in A for b in B if a! = b]
```

- `SET` 처럼 `for` 문장도 한 줄로 표현할 수 있다.
- 또한 `pairs` 처럼 중첩 `for` 반복문도 한 줄로 나타낼 수 있다.

```python
DICT = {x: x**2 for x in (2, 4, 6)}
```

- Dictionary 타입도 `for` 반복문을 사용하여 생성할 수 있다. 단, `key:value` 를 어떻게 생성할 것인지 나타내야 한다.

#### `break`

```python
for value in range(5):
    if LIST[x] == "Yellow":
        break
		print("이 문장은 실행되지 않습니다.")
```

- `break` 를 실행하면 `iterable` 에 남아있는 값과 상관 없이 해당 반복문이 종료된다.

#### `continue`

```python
for value in range(5):
    if LIST[x] == "Yellow":
        continue
	print("continue가 실행되면 이 문장은 실행되지 않습니다.")
```

- `continue` 가 실행되면 해당 `value` 에 대한 반복문은 종료하고 `iterable` 의 다음 값을 `value` 에 대입하여 반복문을 이어간다.

#### `pass`

```python
for value in range(5):
    if LIST[x] == "Yellow":
        pass
	else:
		print("pass가 실행되지 않으면 이 문장이 실행됩니다.")
```

- `pass` 는 아무 문장도 실행하지 않는다. 특정 조건을 충족했을 때 아무 문장도 실행하지 말아야 할 경우에 주로 활용된다.

---
# Python 중급
> [!summary]
> > 다음 내용은 Python 프로그램을 구성하는 객체 단위를 다룹니다.
> > Python 프로그램의 구성을 이해하여 다른 사람이 작성한 코드를 읽고, 
> > 올바르게 작성하기 위해 알아야 할 내용입니다. 
> - [[#코딩 스타일]]
> - [[#함수 python_function (자세히 보기)|함수 (Functions)]]
> - [[Software/Code/Language/Python/Object/python_class|클래스 (Class)]]
> - [[#모듈 (Module) python_module (자세히 보기)|모듈 (Module)]]


## 코딩 스타일
- 이제 여러분은 파이썬의 더 길고, 더 복잡한 조각들을 작성하려고 합니다, 코딩 스타일에 대해 말할 적절한 시간입니다. 
- 대부분 언어는 서로 다른 스타일로 작성될 (또는 더 간략하게, 포맷될) 수 있습니다; 어떤 것들은 다른 것들보다 더 읽기 쉽습니다. 다른 사람들이 여러분의 코드를 읽기 쉽게 만드는 것은 항상 좋은 생각이고, 훌륭한 코딩 스타일을 도입하는 것은 그렇게 하는 데 큰 도움을 줍니다.
- 파이썬을 위해, 대부분 프로젝트가 고수하는 스타일 가이드로 [**PEP 8**](https://peps.python.org/pep-0008/)이 나왔습니다; 이것은 매우 읽기 쉽고 눈이 편안한 코딩 스타일을 장려합니다. 모든 파이썬 개발자는 언젠가는 이 문서를 읽어야 합니다; 여러분을 위해 가장 중요한 부분들을 추려봤습니다:
  
  - ==들여쓰기에 4-스페이스를 사용하고, 탭을 사용하지 마세요.== 4개의 스페이스는 작은 들여쓰기 (더 많은 중첩 도를 허락합니다) 와 큰 들여쓰기 (읽기 쉽습니다) 사이의 좋은 절충입니다. 탭은 혼란을 일으키고, 없애는 것이 최선입니다.
  - ==79자를 넘지 않도록 줄 넘김== 하세요. 이것은 작은 화면을 가진 사용자를 돕고 큰 화면에서는 여러 코드 파일들을 나란히 볼 수 있게 합니다.
  - ==함수, 클래스, 함수 내의 큰 코드 블록 사이에 빈 줄==을 넣어 분리하세요.
  - 가능하다면, ==주석은 별도의 줄==로 넣으세요.
  - ==[[Software/Code/Language/Python/Object/python_function|docstring]]==을 사용하세요.
  - 연산자들 주변과 콤마 뒤에 스페이스를 넣고, 괄호 바로 안쪽에는 스페이스를 넣지 마세요: `a = f(1, 2) + g(3, 4)`.
  - 클래스와 함수들에 일관성 있는 이름을 붙이세요; 관례는 클래스의 경우 `UpperCamelCase`, 함수와 메서드의 경우 `lowercase_with_underscores`입니다. 첫 번째 메서드 인자의 이름으로는 항상 `self`를 사용하세요 (클래스와 메서드에 대한 자세한 내용은 [클래스와의 첫 만남](https://docs.python.org/ko/3.12/tutorial/classes.html#tut-firstclasses) 을 보세요).
  - 여러분의 코드를 국제적인 환경에서 사용하려고 한다면 특별한 인코딩을 사용하지 마세요. 어떤 경우에도 파이썬의 기본, UTF-8, 또는 단순 ASCII조차, 이 최선입니다.
  - 마찬가지로, 다른 언어를 사용하는 사람이 코드를 읽거나 유지할 약간의 가능성만 있더라도, 식별자에 ASCII 이외의 문자를 사용하지 마세요.



## 함수 (Functions) [[Software/Code/Language/Python/Object/python_function|(자세히 보기)]]

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

### 내장 함수
#### `len`

```python
print(len("Hello")) # 결과: 5
```

- `len(variable)` 은 입력한 iterable 의 길이를 반환한다.


## 클래스 (Class) [[python_class|(자세히 보기)]]
- 클래스는 데이터와 기능을 함께 묶는 방법을 제공합니다. 새 클래스를 만드는 것은 객체의 새 _형_ 을 만들어서, 그 형의 새 인스턴스 를 만들 수 있도록 합니다. 각 클래스 인스턴스는 상태를 유지하기 위해 그 자신에게 첨부된 어트리뷰트를 가질 수 있습니다. 클래스 인스턴스는 상태를 바꾸기 위한 (클래스에 의해 정의된) 메서드도 가질 수 있습니다.

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



## 모듈 (Module) [[python_module|(자세히 보기)]]

- 파이썬 인터프리터를 종료한 후에 다시 들어가면, 여러분이 만들었던 정의들이 사라집니다 (함수나 변수들). 그래서, 좀 긴 프로그램을 쓰고자 한다면, 대신 인터프리터 입력을 편집기를 사용해서 준비한 후에 그 파일을 입력으로 사용해서 실행하는 것이 좋습니다. 이렇게 하는 것을 _스크립트_ 를 만든다고 합니다. 프로그램이 길어짐에 따라, 유지를 쉽게 하려고 여러 개의 파일로 나누고 싶을 수 있습니다. 여러 프로그램에서 썼던 편리한 함수를 각 프로그램에 정의를 복사하지 않고도 사용하고 싶을 수도 있습니다.
- 이런 것을 지원하기 위해, 파이썬은 정의들을 파일에 넣고 스크립트나 인터프리터의 대화형 모드에서 사용할 수 있는 방법을 제공합니다. 그런 파일을 _모듈_ 이라고 부릅니다; 모듈로부터 정의들이 다른 모듈이나 _메인_ 모듈로 _임포트_ 될 수 있습니다 (메인 모듈은 최상위 수준에서 실행되는 스크립트나 계산기 모드에서 액세스하는 변수들의 컬렉션입니다).
- 모듈은 파이썬 정의와 문장들을 담고 있는 파일입니다. 파일의 이름은 모듈 이름에 확장자 `.py` 를 붙입니다. 모듈 내에서, 모듈의 이름은 전역 변수 `__name__` 으로 제공됩니다. 예를 들어, 여러분이 좋아하는 편집기로 `fibo.py` 라는 이름의 파일을 현재 디렉터리에 만들고 다음과 같은 내용으로 채웁니다:

```python
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

- 이제 파이썬 인터프리터에 들어가서 이 모듈을 다음과 같은 명령으로 임포트 합니다:

```python
>>> import fibo
```

- 이것은 현재 [namespace](https://docs.python.org/ko/3.12/glossary.html#term-namespace)(자세한 내용은 [파이썬 스크립트와 namespace](https://docs.python.org/ko/3.12/tutorial/classes.html#tut-scopes) 참조)에 `fibo`에 정의된 함수 이름을 직접 추가하는 것이 아니라, 모듈 이름 `fibo`만 추가합니다. 모듈 이름을 사용하여 함수에 액세스할 수 있습니다:

```python
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
```

- 함수를 자주 사용할 거라면 지역 이름으로 대입할 수 있습니다:

```python
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

- 모듈은 함수 정의뿐만 아니라 실행 가능한 문장들도 포함할 수 있습니다. 이 문장들은 모듈을 초기화하는 데 사용됩니다. 이것들은 임포트 문에서 모듈 이름이 _처음_ 등장할 때만 실행됩니다. [[1]](https://docs.python.org/ko/3.12/tutorial/modules.html#id3) (이것들은 파일이 스크립트로 실행될 때도 실행됩니다.)
- 각 모듈에는 모듈에 정의된 모든 함수가 전역 네임스페이스로 사용하는 고유한 개인 네임스페이스가 있습니다. 따라서 모듈 작성자는 사용자의 전역 변수와 실수로 충돌할 염려 없이 모듈에서 전역 변수를 사용할 수 있습니다. 반면에 자신이 무엇을 하고 있는지 알고 있다면 모듈의 전역 변수를 함수를 참조하는 데 사용되는 것과 동일한 표기법인 `modname.itemname`을 사용하여 모듈의 전역 변수를 건드릴 수 있습니다.
- 모듈은 다른 모듈을 가져올 수 있습니다. 모듈(또는 스크립트)의 시작 부분에 모든 [`import`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#import) 문을 배치하는 것이 일반적이지만 필수는 아닙니다. 가져온 모듈 이름을 모듈의 최상위 수준(함수나 클래스 외부)에 배치하면 모듈의 전역 네임스페이스에 추가됩니다.
- 모듈에서 가져오는 모듈의 네임스페이스로 직접 이름을 가져오는 [`import`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#import) 구문의 변형이 있습니다. 예를 들어

```python
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

이렇게 하면 로컬 네임스페이스에서 가져오는 모듈 이름을 가져오지 않습니다(예제에서는 `fibo`가 정의되지 않음).
- 모듈이 정의하는 모든 이름을 임포트하는 변종도 있습니다:

```python
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

- 이것은 밑줄 (`_`) 로 시작하는 것들을 제외한 모든 이름을 임포트 합니다. 대부분 파이썬 프로그래머들은 이 기능을 사용하지 않는데, 인터프리터로 알려지지 않은 이름들의 집합을 도입하게 되어, 여러분이 이미 정의한 것들을 가리게 될 수 있기 때문입니다.
- 일반적으로 모듈이나 패키지에서 `*` 를 임포트하는 것은 눈살을 찌푸리게 한다는 것에 유의하세요, 종종 읽기에 편하지 않은 코드를 만들기 때문입니다. 하지만, 대화형 세션에서 입력을 줄이고자 사용하는 것은 상관없습니다.
- 모듈 이름 다음에 `as` 가 올 경우, `as` 다음의 이름을 임포트한 모듈에 직접 연결합니다.

```python
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

- 이것은 `import fibo` 가하는 것과 같은 방식으로 모듈을 임포트 하는데, 유일한 차이점은 그 모듈을 `fib` 라는 이름으로 사용할 수 있다는 것입니다.
- [`from`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#from)을 써서 비슷한 효과를 낼 때도 사용할 수 있습니다:

```python
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

> [!note] 
> - 효율성의 이유로, 각 모듈은 인터프리터 세션마다 한 번만 임포트됩니다. 그래서, 여러분이 모듈을 수정하면, 인터프리터를 다시 시작시켜야 합니다 — 또는, 대화형으로 시험하는 모듈이 하나뿐이라면, [`importlib.reload()`](https://docs.python.org/ko/3.12/library/importlib.html#importlib.reload "importlib.reload") 를 사용하세요. 예를 들어, 
>   
>   `import importlib; importlib.reload(modulename)`.


---
# Python 고급
> [!summary]
> > 다음 내용은 Python 프로그램을 확장하고, 오류를 제어하기 위한 방법을 다룹니다.
> > 실무에서 Python 프로그램을 작성하고, 안정성 있게 작성하려면 알아야 할 내용입니다.
> - [[#에러와 예외 (Error & Exception) python_error_exception (자세히 보기)|에러와 예외 (Error & Exception)]]
> - [[#라이브러리 (Library) python_library (자세히 보기)|라이브러리 (Library)]]
> - [[#파일 입출력 (File Input & Output) python_input_output (자세히 보기)|파일 입출력 (File Input & Output)]]
> - [[#가상 환경 (Virtual Environment)]]


## 에러와 예외 (Error & Exception) [[python_error_exception|(자세히 보기)]]
#### 예외

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


#### 예외 처리하기

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


- [`BaseException`](https://docs.python.org/ko/3.12/library/exceptions.html#BaseException "BaseException")은 모든 예외의 공통 베이스 클래스입니다. 그 서브 클래스 중 하나인 [`Exception`](https://docs.python.org/ko/3.12/library/exceptions.html#Exception "Exception")은 치명적이지 않은 모든 예외의 베이스 클래스입니다. [`Exception`](https://docs.python.org/ko/3.12/library/exceptions.html#Exception "예외")의 서브 클래스가 아닌 예외는 프로그램이 종료되어야 함을 나타내는 데 사용되기 때문에 일반적으로 처리되지 않습니다. 여기에는 [`sys.exit()`](https://docs.python.org/ko/3.12/library/sys.html#sys.exit "sys.exit")에 의해 발생하는 [`SystemExit`](https://docs.python.org/ko/3.12/library/exceptions.html#SystemExit "SystemExit")와 사용자가 프로그램을 중단하고자 할 때 발생하는 [`KeyboardInterrupt`](https://docs.python.org/ko/3.12/library/exceptions.html#KeyboardInterrupt "KeyboardInterrupt")가 포함됩니다.
- [`Exception`](https://docs.python.org/ko/3.12/library/exceptions.html#Exception "예외")을 와일드카드로 사용하여 (거의) 모든 것을 잡을 수 있습니다. 그러나 처리하려는 예외 유형을 최대한 구체적으로 지정하고 예기치 않은 예외가 전파될 수 있도록 하는 것이 좋습니다.
- [`예외`](https://docs.python.org/ko/3.12/library/exceptions.html#Exception "예외")를 처리하는 가장 일반적인 패턴은 ==예외를 인쇄하거나 로깅한 다음 다시 발생==시키는 것입니다(호출자도 예외를 처리할 수 있도록 허용)
- [`try`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#try) … [`except`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#except) 문에는 선택적 else 절이 있으며, 이 절이 있는 경우 모든 except 절 뒤에 따라야 합니다. 이 옵션은 try 절이 예외를 발생시키지 않는 경우 실행되어야 하는 코드에 유용합니다. 예를 들어
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

#### 예외 일으키기

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

#### 예외 연쇄

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

#### 사용자 정의 예외

- 새 예외 클래스를 만듦으로써 프로그램은 자신의 예외에 이름을 붙일 수 있습니다 (파이썬 클래스에 대한 자세한 내용은 [클래스](https://docs.python.org/ko/3.12/tutorial/classes.html#tut-classes) 를 보세요). 예외는 보통 직접적으로나 간접적으로 [`Exception`](https://docs.python.org/ko/3.12/library/exceptions.html#Exception "Exception") 클래스를 계승합니다.
- 예외 클래스는 다른 클래스가 할 수 있는 모든 작업을 수행하도록 정의할 수 있지만 일반적으로 단순하게 유지되며, 예외 처리기가 오류에 대한 정보를 추출할 수 있는 몇 가지 속성만 제공하는 경우가 많습니다.
- 대부분의 예외는 표준 예외들의 이름들과 유사하게, “Error” 로 끝나는 이름으로 정의됩니다.
- 많은 표준 모듈은 자체적으로 정의한 함수에서 발생할 수 있는 오류를 보고하기 위해 자체 예외를 정의합니다.


#### 뒷정리 동작 정의하기

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
- 실제 세상의 응용 프로그램에서, [`finally`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#finally) 절은 외부 자원을 사용할 때, 성공적인지 아닌지와 관계없이, 그 자원을 반납하는 데 유용합니다 (파일이나 네트워크 연결 같은 것들).

#### 서로 관련이 없는 여러 예외 발생 및 처리하기

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

#### 메모로 예외 강화하기

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

## 라이브러리 (Library) [[python_library|(자세히 보기)]]
- 파이썬에는 `math` 등 기본으로 `import`하여 사용할 수 있도록 구현한 표준 라이브러리가 있습니다. 필요한 기능이 있을 경우 이를 사용하여 코드를 작성할 수 있습니다.
- 표준 라이브러리 외에도 추가적인 기능이 필요할 경우 다른 사람들이 구현한 라이브러리를 설치 [[python_module|("모듈"의 "패키지" 참조)]]하여 사용할 수 있습니다.

## 파일 입출력 (File Input & Output) [[python_input_output|(자세히 보기)]]

- [`open()`](https://docs.python.org/ko/3.12/library/functions.html#open "open")은 [파일 객체](https://docs.python.org/ko/3.12/glossary.html#term-file-object)를 반환하며, 두 개의 위치 인수와 하나의 키워드 인수인 `open(filename, mode, encoding=None)`과 함께 가장 일반적으로 사용됩니다.

```python
>>> f = open('workfile', 'w', encoding="utf-8")
```

- 첫 번째 인자는 파일 이름을 담은 문자열입니다. 두 번째 인자는 파일이 사용될 방식을 설명하는 몇 개의 문자들을 담은 또 하나의 문자열입니다. _mode_ 는 파일을 읽기만 하면 `'r'`, 쓰기만 하면 `'w'` (같은 이름의 이미 존재하는 파일은 삭제됩니다) 가 되고, `'a'` 는 파일을 덧붙이기 위해 엽니다; 파일에 기록되는 모든 데이터는 자동으로 끝에 붙습니다. `'r+'` 는 파일을 읽고 쓰기 위해 엽니다. _mode_ 인자는 선택적인데, 생략하면 `'r'` 이 가정됩니다.
- 일반적으로 파일은 _텍스트 모드_, 즉 특정 인코딩으로 인코딩된 파일에서 문자열을 읽고 쓰는 방식으로 열립니다. encoding_을 지정하지 않으면 기본값은 플랫폼에 따라 달라집니다([`open()`](https://docs.python.org/ko/3.12/library/functions.html#open "open") 참조). UTF-8이 사실상의 최신 표준이므로 다른 인코딩을 사용해야 하는 경우가 아니라면 `encoding="utf-8"`을 사용하는 것이 좋습니다. 모드에 `'b'`를 추가하면 파일이 바이너리 모드로 열립니다. 바이너리 모드 데이터는 [`바이트`](https://docs.python.org/ko/3.12/library/stdtypes.html#bytes "바이트") 객체로 읽고 씁니다. 바이너리 모드로 파일을 열 때는 encoding을 지정할 수 없습니다.
- 텍스트 모드에서, 읽을 때의 기본 동작은 플랫폼 의존적인 줄 종료 (유닉스에서 `\n`, 윈도우에서 `\r\n`) 를 단지 `\n` 로 변경하는 것입니다. 텍스트 모드로 쓸 때, 기본 동작은 `\n` 를 다시 플랫폼 의존적인 줄 종료로 변환하는 것입니다. 이 파일 데이터에 대한 무대 뒤의 수정은 텍스트 파일의 경우는 문제가 안 되지만, `JPEG` 이나 `EXE` 파일과 같은 바이너리 데이터를 망치게 됩니다. 그런 파일을 읽고 쓸 때 바이너리 모드를 사용하도록 주의하세요.
- 파일 객체를 다룰 때 [`with`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#with) 키워드를 사용하는 것은 좋은 습관입니다. 혜택은 도중 예외가 발생하더라도 스위트가 종료될 때 파일이 올바르게 닫힌다는 것입니다. `with` 를 사용하는 것은 동등한 [`try`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#try)-[`finally`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#finally) 블록을 쓰는 것에 비교해 훨씬 짧기도 합니다:

```python
>>> with open('workfile', encoding="utf-8") as f:
…     read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True
```

- [`with`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#with) 키워드를 사용하지 않으면, `f.close()` 를 호출해서 파일을 닫고 사용된 시스템 자원을 즉시 반납해야 합니다.

> [!warning]
> - `with` 키워드를 사용하거나 `f.close()`를 호출하지 않고 `f.write()`를 호출하면 프로그램이 성공적으로 종료되더라도 `f.write()`의 인자가 디스크에 완전히 기록되지 않을 **수** 있습니다.

- 파일 객체가 닫힌 후에는, [`with`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#with) 문이나 `f.close()` 를 호출하는 경우 모두, 파일 객체를 사용하려는 시도는 자동으로 실패합니다.

```python
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

### 파일 객체의 매소드

- 이 섹션의 나머지 예들은 `f` 라는 파일 객체가 이미 만들어졌다고 가정합니다.
- 파일의 내용을 읽으려면, `f.read(size)` 를 호출하는데, 일정량의 데이터를 읽고 문자열 (텍스트 모드 에서) 이나 바이트열 (바이너리 모드에서) 로 돌려줍니다. _size_ 는 선택적인 숫자 인자입니다. _size_ 가 생략되거나 음수면 파일의 내용 전체를 읽어서 돌려줍니다; 파일의 크기가 기계의 메모리보다 두 배 크다면 여러분이 감당할 문제입니다. 그렇지 않으면 최대 _size_ 문자(텍스트 모드에서)나 _size_ 바이트(바이너리 모드에서)를 읽고 돌려줍니다. 파일의 끝에 도달하면, `f.read()` 는 빈 문자열 (`''`) 을 돌려줍니다.

```python
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
```

- `f.readline()` 은 파일에서 한 줄을 읽습니다; 개행 문자 (`\n`) 는 문자열의 끝에 보존되고, 파일이 개행문자로 끝나지 않는 때에만 파일의 마지막 줄에서만 생략됩니다. 이렇게 반환 값을 모호하지 않게 만듭니다; `f.readline()` 가 빈 문자열을 돌려주면, 파일의 끝에 도달한 것이지만, 빈 줄은 `'\n'`, 즉 하나의 개행문자만을 포함하는 문자열로 표현됩니다.

```python
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
```

- 파일에서 줄들을 읽으려면, 파일 객체에 대해 루핑할 수 있습니다. 이것은 메모리 효율적이고, 빠르며 간단한 코드로 이어집니다:

```python
>>> for line in f:
…     print(line, end='')
…
This is the first line of the file.
Second line of the file
```

- 파일의 모든 줄을 리스트로 읽어 들이려면 `list(f)` 나 `f.readlines()` 를 쓸 수 있습니다.
- `f.write(string)` 은 _string_ 의 내용을 파일에 쓰고, 출력된 문자들의 개수를 돌려줍니다.

```python
>>> f.write('This is a test\n')
15
```

- 다른 형의 객체들은 쓰기 전에 변환될 필요가 있습니다 – 문자열 (텍스트 모드에서) 이나 바이트열 객체 (바이너리 모드에서) 로 –:

```python
>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18
```

- `f.tell()` 은 파일의 현재 위치를 가리키는 정수를 돌려주는데, 바이너리 모드의 경우 파일의 처음부터의 바이트 수로 표현되고 텍스트 모드의 경우는 불투명한 숫자입니다.
- 파일 객체의 위치를 바꾸려면, `f.seek(offset, whence)` 를 사용합니다. 위치는 기준점에 _offset_ 을 더해서 계산됩니다; 기준점은 _whence_ 인자로 선택합니다. _whence_ 값이 0이면 파일의 처음부터 측정하고, 1이면 현재 파일 위치를 사용하고, 2 는 파일의 끝을 기준점으로 사용합니다. _whence_ 는 생략될 수 있고, 기본값은 0이라서 파일의 처음을 기준점으로 사용합니다.

```python
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
```

- 텍스트 파일에서는 (모드 문자열에 `b` 가 없이 열린 것들), 파일의 시작에 상대적인 위치 변경만 허락되고 (예외는 `seek(0, 2)` 를 사용해서 파일의 끝으로 위치를 변경하는 경우입니다), 올바른 _offset_ 값은 `f.tell()` 이 돌려준 값과 0뿐입니다. 그 밖의 다른 _offset_ 값은 정의되지 않은 결과를 낳습니다.
- 파일 객체에는 [`isatty()`](https://docs.python.org/ko/3.12/library/io.html#io.IOBase.isatty "io.IOBase.isatty") 및 [`truncate()`](https://docs.python.org/ko/3.12/library/io.html#io.IOBase.truncate "io.IOBase.truncate") 등 자주 사용되지 않는 몇 가지 추가 메서드가 있으며, 파일 객체에 대한 전체 가이드는 라이브러리 참조를 참조하시기 바랍니다.

### [`json`](https://docs.python.org/ko/3.12/library/json.html#module-json "json: Encode and decode the JSON format.") 으로 구조적인 데이터를 저장하기

- 문자열은 파일에 쉽게 쓰고 파일에서 읽을 수 있습니다. 숫자는 [`read()`](https://docs.python.org/ko/3.12/library/io.html#io.TextIOBase.read "io.TextIOBase.read") 메서드가 문자열만 반환하므로 `'123'`과 같은 문자열을 받아 숫자 값 123을 반환하는 [`int()`](https://docs.python.org/ko/3.12/library/functions.html#int "int") 같은 함수에 전달해야 하므로 조금 더 많은 노력이 필요합니다. 중첩된 목록이나 사전과 같이 더 복잡한 데이터 유형을 저장하려는 경우 수작업으로 구문 분석하고 직렬화하는 것은 복잡해집니다.
- 복잡한 데이터 유형을 파일에 저장하기 위해 사용자가 지속적으로 코드를 작성하고 디버깅하는 대신 Python을 사용하면 [JSON(JavaScript Object Notation)](https://json.org/)이라는 널리 사용되는 데이터 교환 형식을 사용할 수 있습니다. 표준 모듈은 [`json`](https://docs.python.org/ko/3.12/library/json.html#module-json "json: JSON 형식을 인코딩하고 디코딩합니다.")는 Python 데이터 계층구조를 가져와 문자열 표현으로 변환할 수 있으며, 이 프로세스를 serializing이라고 합니다. 문자열 표현에서 데이터를 재구성하는 것을 역직렬화라고 합니다. 직렬화와 역직렬화 사이에 객체를 나타내는 문자열은 파일이나 데이터에 저장되어 있거나 네트워크 연결을 통해 멀리 떨어진 컴퓨터로 전송되었을 수 있습니다.

> [!NOTE]
> - JSON 형식은 데이터 교환을 위해 현대 응용 프로그램들이 자주 사용합니다. 많은 프로그래머가 이미 이것에 익숙하므로, 연동성을 위한 좋은 선택이 됩니다.

- 객체 `x` 가 있을 때, 간단한 한 줄의 코드로 그것의 JSON 문자열 표현을 볼 수 있습니다:

```python
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'
```

- [`dump()`](https://docs.python.org/ko/3.12/library/json.html#json.dump "json.dump")라는 [`dumps()`](https://docs.python.org/ko/3.12/library/json.html#json.dumps "json.dumps") 함수의 변종은 객체를 [텍스트 파일](https://docs.python.org/ko/3.12/glossary.html#term-text-file) 로 직렬화합니다. 그래서 `f` 가 쓰기를 위해 열린 [텍스트 파일](https://docs.python.org/ko/3.12/glossary.html#term-text-file) 이면, 이렇게 할 수 있습니다:

```python
json.dump(x, f)
```

- `f`가 읽기 위해 열린 [바이너리 파일](https://docs.python.org/ko/3.12/glossary.html#term-binary-file) 또는 [텍스트 파일](https://docs.python.org/ko/3.12/glossary.html#term-text-file) 객체인 경우, 객체를 다시 디코딩하려면 다음과 같이 합니다:

```python
x = json.load(f)
```


> [!NOTE]
> - JSON 파일은 UTF-8로 인코딩해야 합니다. JSON 파일을 [텍스트 파일](https://docs.python.org/ko/3.12/glossary.html#term-text-file)로 열 때는 읽기와 쓰기 모두 `encoding="utf-8"`을 사용하세요.

- 이 간단한 직렬화 테크닉이 리스트와 딕셔너리를 다룰 수 있지만, 임의의 클래스 인스턴스를 JSON 으로 직렬화하기 위해서는 약간의 수고가 더 필요합니다. [`json`](https://docs.python.org/ko/3.12/library/json.html#module-json "json: Encode and decode the JSON format.") 모듈의 레퍼런스는 이 방법에 대한 설명을 담고 있습니다.


### [`pickle`](https://docs.python.org/ko/3.12/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") - 피클 모듈
- [JSON](https://docs.python.org/ko/3.12/tutorial/inputoutput.html#tut-json) 에 반해, _pickle_ 은 임의의 복잡한 파이썬 객체들을 직렬화할 수 있는 프로토콜입니다. 파이썬에 국한되고 다른 언어로 작성된 응용 프로그램들과 통신하는데 사용될 수 없습니다. 기본적으로 안전하지 않기도 합니다: 믿을 수 없는 소스에서 온 데이터를 역 직렬화할 때, 숙련된 공격자에 의해 데이터가 조작되었다면 임의의 코드가 실행될 수 있습니다.


## 가상 환경 (Virtual Environment)

- 파이썬 응용 프로그램은 종종 표준 라이브러리의 일부로 제공되지 않는 패키지와 모듈을 사용합니다. 응용 프로그램에 특정 버전의 라이브러리가 필요할 수 있는데, 응용 프로그램에 특정 버그가 수정된 버전이 필요하거나, 라이브러리 인터페이스의 구식 버전을 사용하여 응용 프로그램을 작성할 수도 있기 때문입니다.
- 즉, 하나의 파이썬 설치가 모든 응용 프로그램의 요구 사항을 충족시키는 것이 불가능할 수도 있습니다. 응용 프로그램 A에 특정 모듈의 버전 1.0이 필요하지만, 응용 프로그램 B에 버전 2.0이 필요한 경우, 요구 사항이 충돌하고, 버전 1.0 또는 2.0을 설치하면 어느 한 응용 프로그램은 실행할 수 없게 됩니다.
- 이 문제에 대한 해결책은 [가상 환경](https://docs.python.org/ko/3.12/glossary.html#term-virtual-environment) 을 만드는 것입니다. 이 가상 환경은 특정 버전 파이썬 설치와 여러 추가 패키지를 포함하는 완비된 디렉터리 트리입니다.
- 서로 다른 응용 프로그램은 서로 다른 가상 환경을 사용할 수 있습니다. 앞서 본 상충하는 요구 사항의 예를 해결하기 위해, 응용 프로그램 A에는 버전 1.0이 설치된 자체 가상 환경이 있고, 응용 프로그램 B에는 버전 2.0이 있는 다른 가상 환경이 있을 수 있습니다. 응용 프로그램 B에서 라이브러리를 버전 3.0으로 업그레이드해야 하는 경우, 응용 프로그램 A의 환경에 영향을 미치지 않습니다.

### 가상 환경 만들기

- 가상 환경을 생성하고 관리하는 데 사용되는 모듈은 [`venv`](https://docs.python.org/ko/3.12/library/venv.html#module-venv "venv: 가상 환경 생성."). [`venv`](https://docs.python.org/ko/3.12/library/venv.html#module-venv "venv: 가상 환경 생성.")는 명령이 실행된 파이썬 버전을 설치합니다 ([`--version`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-version) 옵션에서 보고한 대로). 예를 들어 `python3.12`로 명령을 실행하면 버전 3.12가 설치됩니다.
- 가상 환경을 만들려면, 원하는 디렉터리를 결정하고, [`venv`](https://docs.python.org/ko/3.12/library/venv.html#module-venv "venv: Creation of virtual environments.") 모듈을 스크립트로 실행하는데 디렉터리 경로를 명령행 인자로 전달합니다:

```shell
python -m venv tutorial-env
```

- 이렇게 하면 `tutorial-env` 디렉터리가 없는 경우 그 안에 파이썬 인터프리터 사본과 다양한 지원 파일이 포함된 디렉터리가 만들어집니다.
- 가상 환경의 일반적인 디렉터리 위치는 `.venv`입니다. 이 이름은 디렉터리가 보통 셸에서 숨겨져 있도록 하므로, 디렉터리가 존재하는 이유를 설명하는 이름을 제공하면서도 방해받지 않습니다. 또한 일부 툴링(tooling)이 지원하는 `.env` 환경 변수 정의 파일과의 충돌을 방지합니다.
- 가상 환경을 만들었으면, 가상 환경을 활성화할 수 있습니다.
  윈도우에서 이렇게 실행합니다:

```shell
tutorial-env\Scripts\activate
```

Unix 또는 MacOS에서 이렇게 실행합니다:

```shell
source tutorial-env/bin/activate
```

> (이 스크립트는 bash 셸을 위해 작성된 것으로, **csh** 또는 **fish** 셸을 사용하는 경우에는, 대신 `activate.csh` 와 `activate.fish` 스크립트를 사용해야 합니다.)

- 가상 환경을 활성화하면, 셸의 프롬프트가 변경되어 사용 중인 가상 환경을 보여주고, 환경을 수정하여 `python` 을 실행하면 특정 버전의 파이썬이 실행되도록 합니다. 예를 들어:

```shell
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>
```

- 가상 환경을 비활성화하려면 터미널에 다음과 같이 입력합니다:

```shell
deactivate
```


# Python 심화
> [!summary]
> > 다음 내용은 Python을 깊게 이해하기 위한 내용들입니다.
> - [[#환경 설정 python_environment (자세히 보기)|환경 설정 (Environment Settings)]]
> - [[#언어 구조 (Language Structure) python_language_structure (자세히 보기)|언어 구조 (Language Structure)]]
> - [[#대화형 시작 파일]]
> - [[#커스터마이제이션 모듈]]
> - [[#확장 (Extensions)]]

## 환경 설정 (Environment Settings) [[python_environment|(자세히 보기)]]

### 개발 모드

- 파이썬 개발 모드에는 기본적으로 활성화하기에 너무 비싼 추가 실행 시간 검사를 도입합니다. 코드가 올바르면 기본값보다 더 상세하지(verbose) 않아야 합니다; 새로운 경고는 문제가 감지될 때만 발생합니다.
- [`-X dev`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-X) 명령 줄 옵션을 사용하거나 [`PYTHONDEVMODE`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONDEVMODE) 환경 변수를 `1`로 설정하여 활성화할 수 있습니다.

#### 개발 모드의 효과

- 파이썬 개발 모드를 활성화하는 것은 다음 명령과 유사하지만, 아래에 설명된 추가 효과가 있습니다:

```sh
PYTHONMALLOC=debug PYTHONASYNCIODEBUG=1 python -W default -X faulthandler
```

- `default` [경고 필터](https://docs.python.org/ko/3.12/library/warnings.html#describing-warning-filters)를 추가합니다. 다음과 같은 경고가 표시됩니다:
	- [`DeprecationWarning`](https://docs.python.org/ko/3.12/library/exceptions.html#DeprecationWarning "DeprecationWarning")
	- [`ImportWarning`](https://docs.python.org/ko/3.12/library/exceptions.html#ImportWarning "ImportWarning")
	- [`PendingDeprecationWarning`](https://docs.python.org/ko/3.12/library/exceptions.html#PendingDeprecationWarning "PendingDeprecationWarning")
	- [`ResourceWarning`](https://docs.python.org/ko/3.12/library/exceptions.html#ResourceWarning "ResourceWarning")
  일반적으로, 위의 경고는 기본 [경고 필터](https://docs.python.org/ko/3.12/library/warnings.html#describing-warning-filters)가 필터링합니다.
  [`-W default`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-W) 명령 줄 옵션이 사용된 것처럼 작동합니다.
  경고를 에러로 처리하려면 [`-W error`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-W) 명령 줄 옵션을 사용하거나 [`PYTHONWARNINGS`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONWARNINGS) 환경 변수를 `error`로 설정하십시오.
- 메모리 할당자에 디버그 훅을 설치하여 다음을 확인합니다:
	- 버퍼 언더플로
	- 버퍼 오버플로
	- 메모리 할당자 API 위반
	- GIL의 안전하지 않은 사용
  [`PyMem_SetupDebugHooks()`](https://docs.python.org/ko/3.12/c-api/memory.html#c.PyMem_SetupDebugHooks "PyMem_SetupDebugHooks") C 함수를 참조하십시오.
  [`PYTHONMALLOC`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONMALLOC) 환경 변수가 `debug`로 설정된 것처럼 동작합니다.
  메모리 할당자에 디버그 훅을 설치하지 않고 파이썬 개발 모드를 사용하려면, [`PYTHONMALLOC`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONMALLOC) 환경 변수를 `default`로 설정하십시오.

- 파이썬 시작 시 [`faulthandler.enable()`](https://docs.python.org/ko/3.12/library/faulthandler.html#faulthandler.enable "faulthandler.enable")를 호출하여 [`SIGSEGV`](https://docs.python.org/ko/3.12/library/signal.html#signal.SIGSEGV "signal.SIGSEGV"), [`SIGFPE`](https://docs.python.org/ko/3.12/library/signal.html#signal.SIGFPE "signal.SIGFPE"), [`SIGABRT`](https://docs.python.org/ko/3.12/library/signal.html#signal.SIGABRT "signal.SIGABRT"), [`SIGBUS`](https://docs.python.org/ko/3.12/library/signal.html#signal.SIGBUS "signal.SIGBUS") 및 [`SIGILL`](https://docs.python.org/ko/3.12/library/signal.html#signal.SIGILL "signal.SIGILL") 시그널에 대한 처리기를 설치하여 크래시 시 파이썬 트레이스백을 덤프할 수 있습니다.
  
  [`-X faulthandler`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-X) 명령 줄 옵션이 사용되거나 [`PYTHONFAULTHANDLER`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONFAULTHANDLER) 환경 변수가 `1`로 설정된 것처럼 작동합니다.

- [asyncio 디버그 모드](https://docs.python.org/ko/3.12/library/asyncio-dev.html#asyncio-debug-mode)를 활성화합니다. 예를 들어, [`asyncio`](https://docs.python.org/ko/3.12/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.")는 어웨이트 하지 않은 코루틴을 확인하고 이를 로그 합니다.
  [`PYTHONASYNCIODEBUG`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONASYNCIODEBUG) 환경 변수가 `1`로 설정된 것처럼 동작합니다.
- 문자열 인코딩과 디코딩 연산에 대해 _encoding_ 과 _errors_ 인자를 확인합니다. 예: [`open()`](https://docs.python.org/ko/3.12/library/functions.html#open "open"), [`str.encode()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.encode "str.encode") 및 [`bytes.decode()`](https://docs.python.org/ko/3.12/library/stdtypes.html#bytes.decode "bytes.decode").
  
  기본적으로, 최상의 성능을 위해, _errors_ 인자는 첫 번째 인코딩/디코딩 에러에서만 검사되며 빈 문자열에 대해서는 _encoding_ 인자가 무시되는 경우가 있습니다.

- [`io.IOBase`](https://docs.python.org/ko/3.12/library/io.html#io.IOBase "io.IOBase") 파괴자는 `close()` 예외를 로그 합니다.
- [`sys.flags`](https://docs.python.org/ko/3.12/library/sys.html#sys.flags "sys.flags")의 [`dev_mode`](https://docs.python.org/ko/3.12/library/sys.html#sys.flags.dev_mode "sys.flags.dev_mode") 속성을 `True`로 설정합니다.

- 파이썬 개발 모드는 (성능과 메모리에 대한) 오버헤드 비용이 너무 비싸서, 기본적으로 [`tracemalloc`](https://docs.python.org/ko/3.12/library/tracemalloc.html#module-tracemalloc "tracemalloc: Trace memory allocations.") 모듈을 활성화하지 않습니다. [`tracemalloc`](https://docs.python.org/ko/3.12/library/tracemalloc.html#module-tracemalloc "tracemalloc: Trace memory allocations.") 모듈을 활성화하면 일부 에러의 원인에 대한 추가 정보가 제공됩니다. 예를 들어, [`ResourceWarning`](https://docs.python.org/ko/3.12/library/exceptions.html#ResourceWarning "ResourceWarning")은 자원이 할당된 곳의 트레이스백을 로그하고, 버퍼 오버플로 에러는 메모리 블록이 할당된 곳의 트레이스백을 로그 합니다.
- 파이썬 개발 모드는 [`-O`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-O) 명령 줄 옵션이 [`assert`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#assert) 문을 제거하거나 [`__debug__`](https://docs.python.org/ko/3.12/library/constants.html#debug__ "__debug__")를 `False`로 설정하는 것을 막지 않습니다.
- 파이썬 개발 모드는 파이썬을 시작할 때만 활성화할 수 있습니다. 해당 값은 [`sys.flags.dev_mode`](https://docs.python.org/ko/3.12/library/sys.html#sys.flags "sys.flags")에서 읽을 수 있습니다.

> 버전 3.8에서 변경: [`io.IOBase`](https://docs.python.org/ko/3.12/library/io.html#io.IOBase "io.IOBase") 파괴자는 이제 `close()` 예외를 로그 합니다.
> 버전 3.9에서 변경: _encoding_ 과 _errors_ 인자는 이제 문자열 인코딩과 디코딩 연산을 검사합니다.

> [!example] `ResourceWarning` 예
> 
> - 명령 줄에 지정된 텍스트 파일의 줄 수를 세는 스크립트의 예:
> 
> ```python
> import sys
> 
> def main():
>     fp = open(sys.argv[1])
>     nlines = len(fp.readlines())
>     print(nlines)
>     # The file is closed implicitly
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> - 스크립트는 파일을 명시적으로 닫지 않습니다. 기본적으로, 파이썬은 아무런 경고도 하지 않습니다. 269 줄이 있는 README.txt를 사용하는 예:
> 
> ```sh
> $ python script.py README.txt
> 269
> ```
> 
> 파이썬 개발 모드를 사용하면 [`ResourceWarning`](https://docs.python.org/ko/3.12/library/exceptions.html#ResourceWarning "ResourceWarning") 경고가 표시됩니다:
> 
> ```sh
> $ python -X dev script.py README.txt
> 269
> script.py:10: ResourceWarning: unclosed file <_io.TextIOWrapper name='README.rst' mode='r' encoding='UTF-8'>
>   main()
> ResourceWarning: Enable tracemalloc to get the object allocation traceback
> ```
> 
> 또한, [`tracemalloc`](https://docs.python.org/ko/3.12/library/tracemalloc.html#module-tracemalloc "tracemalloc: Trace memory allocations.")을 활성화하면 파일이 열린 줄이 표시됩니다:
> 
> ```sh
> $ python -X dev -X tracemalloc=5 script.py README.rst
> 269
> script.py:10: ResourceWarning: unclosed file <_io.TextIOWrapper name='README.rst' mode='r' encoding='UTF-8'>
>   main()
> Object allocated at (most recent call last):
>   File "script.py", lineno 10
>     main()
>   File "script.py", lineno 4
>     fp = open(sys.argv[1])
> ```
> - 수선은 파일을 명시적으로 닫는 것입니다. 컨텍스트 관리자를 사용하는 예:
> 
> ```python
> def main():
>     # Close the file explicitly when exiting the with block
>     with open(sys.argv[1]) as fp:
>         nlines = len(fp.readlines())
>     print(nlines)
> ```
> 
> - 자원을 명시적으로 닫지 않으면 예상보다 오래 자원을 열어둘 수 있습니다; 파이썬을 종료할 때 심각한 문제가 발생할 수 있습니다. CPython에서도 나쁘지만, PyPy에서는 더 나쁩니다. 리소스를 명시적으로 닫으면 응용 프로그램을 더 결정적이고 안정적으로 만들 수 있습니다.

> [!example] 잘못된 파일 기술자 에러 예
> 
> - 자신의 첫 줄을 표시하는 스크립트:
> 
> ```python
> import os
> 
> def main():
>     fp = open(__file__)
>     firstline = fp.readline()
>     print(firstline.rstrip())
>     os.close(fp.fileno())
>     # The file is closed implicitly
> 
> main()
> ```
> 
> - 기본적으로, 파이썬은 아무런 경고도 하지 않습니다:
> 
> ```sh
> $ python script.py
> import os
> ```
> 
> - 파이썬 개발 모드는 [`ResourceWarning`](https://docs.python.org/ko/3.12/library/exceptions.html#ResourceWarning "ResourceWarning")을 표시하고 파일 객체를 파이널라이즈 할 때 “잘못된 파일 기술자(Bad file descriptor)” 에러를 로그 합니다:
> 
> ```sh
> $ python -X dev script.py
> import os
> script.py:10: ResourceWarning: unclosed file <_io.TextIOWrapper name='script.py' mode='r' encoding='UTF-8'>
>   main()
> ResourceWarning: Enable tracemalloc to get the object allocation traceback
> Exception ignored in: <_io.TextIOWrapper name='script.py' mode='r' encoding='UTF-8'>
> Traceback (most recent call last):
>   File "script.py", line 10, in `<module>`
>     main()
> OSError: [Errno 9] Bad file descriptor
> ```
> 
> - `os.close(fp.fileno())`는 파일 기술자를 닫습니다. 파일 객체 파이널라이저가 파일 기술자를 다시 닫으려고 하면, `Bad file descriptor` 에러로 실패합니다. 파일 기술자는 한 번만 닫아야 합니다. 최악의 시나리오에서는, 두 번 닫을 때 충돌이 발생할 수 있습니다 (예는 [bpo-18748](https://bugs.python.org/issue?@action=redirect&bpo=18748)을 참조하십시오).
> - 수선은 `os.close(fp.fileno())` 줄을 제거하거나, `closefd=False`로 파일을 여는 것입니다.

## 언어 구조 (Language Structure) [[python_language_structure|(자세히 보기)]]
### 줄 구조(Line structure)

파이썬 프로그램은 여러 개의 _논리적인 줄(logical lines)_ 들로 나뉩니다.

#### 논리적인 줄

- 논리적인 줄의 끝은 NEWLINE 토큰으로 표현됩니다. 문법이 허락하지 않는 이상 (예를 들어 복합문에서 문장들 사이) 문장은 논리적인 줄 간의 경계를 가로지를 수 없습니다. 논리적인 줄은 명시적이거나 묵시적인 _줄 결합(line joining)_ 규칙에 따라 하나 이상의 _물리적인 줄(physical lines)_ 들로 구성됩니다.

#### 물리적인 줄

- 물리적인 줄은 줄의 끝을 나타내는 시퀀스로 끝나는 문자들의 시퀀스입니다. 소스 파일과 문자열에는 플랫폼들의 표준 줄 종료 시퀀스들이 모두 사용될 수 있습니다 - ASCII LF (개행문자)를 사용하는 유닉스 형, ASCII 시퀀스 CR LF(캐리지 리턴 다음에 오는 개행 문자)를 사용하는 윈도우 형, ASCII CR(캐리지 리턴)을 사용하는 예전의 매킨토시 형. 이 형태들은 플랫폼의 종류와 관계없이 동등하게 사용할 수 있습니다. 입력의 끝은 마지막 물리적인 줄의 묵시적 종결자 역할을 합니다.
- 파이썬을 내장할 때는, 소스 코드 문자열은 반드시 줄 종료 문자에 표준 C 관행(ASCII LF를 표현하는 `\n` 문자로 줄이 종료됩니다)을 적용해서 파이썬 API로 전달되어야 합니다.

#### 주석
- 주석은 문자열 리터럴에 포함되지 않는 해시 문자(`#`)로 시작하고 물리적인 줄의 끝에서 끝납니다. 묵시적인 줄 결합 규칙이 유효하지 않은 이상, 주석은 논리적인 줄을 종료시킵니다. 주석은 문법이 무시합니다.

#### 인코딩 선언

- 파이썬 스크립트의 첫 번 째나 두 번째 줄에 있는 주석이 정규식 `coding[=:]\s*([-\w.]+)` 과 매치되면, 이 주석은 인코딩 선언으로 처리됩니다. 이 정규식의 첫 번째 그룹은 소스 코드 파일의 인코딩 이름을 지정합니다. 인코딩 선언은 줄 전체에 홀로 나와야 합니다. 만약 두 번째 줄이라면, 첫 번째 줄 역시 주석만 있어야 합니다. 인코딩 선언의 권장 형태는 두 개입니다. 하나는

```python
# -*- coding: <encoding-name> -*-
```

인데 GNU Emacs에서도 인식됩니다. 다른 하나는

```python
# vim:fileencoding=<encoding-name>
```

인데 Bram Moolenaar 의 VIM에서 인식됩니다.

- 인코딩 선언을 찾을 수 없는 경우 기본 인코딩은 UTF-8입니다. 파일의 암시적 또는 명시적 인코딩이 UTF-8인 경우 구문 오류가 아닌 초기 UTF-8 바이트 순서 표시(b'xefxbbxbf')가 무시됩니다.
- 인코딩이 선언된 경우 인코딩 이름은 파이썬에서 인식되어야 합니다([표준 인코딩](https://docs.python.org/ko/3.12/library/codecs.html#standard-encodings) 참조). 인코딩은 문자열 리터럴, 주석 및 식별자를 포함한 모든 어휘 분석에 사용됩니다.

#### 명시적인 줄 결합
- 둘 이상의 물리적인 줄은 역 슬래시 문자(`\`)를 사용해서 논리적인 줄로 결합할 수 있습니다: 물리적인 줄이 문자열 리터럴이나 주석의 일부가 아닌 역 슬래시 문자로 끝나면, 역 슬래시와 뒤따르는 개행 문자가 제거된 채로, 현재 만들어지고 있는 논리적인 줄에 합쳐집니다. 예를 들어:

```python
if 1900 < year < 2100 and 1 <= month <= 12 \
   and 1 <= day <= 31 and 0 <= hour < 24 \
   and 0 <= minute < 60 and 0 <= second < 60:   # Looks like a valid date
        return 1
```

- 역 슬래시로 끝나는 줄은 주석이 포함될 수 없습니다. 역 슬래시는 주석을 결합하지 못합니다. 역 슬래시는 문자열 리터럴을 제외한 어떤 토큰도 결합하지 못합니다 (즉, 문자열 리터럴 이외의 어떤 토큰도 역 슬래시를 사용해서 두 줄에 나누어 기록할 수 없습니다.). 문자열 리터럴 밖에 있는 역 슬래시가 앞에서 언급한 장소 이외의 곳에 등장하는 것은 문법에 어긋납니다.

#### 묵시적인 줄 결합

- 괄호(`()`), 대괄호(`[]`), 중괄호(`{}`)가 사용되는 표현은 역 슬래시 없이도 여러 개의 물리적인 줄로 나눌 수 있습니다. 예를 들어:

```python
month_names = ['Januari', 'Februari', 'Maart',      # These are the
               'April',   'Mei',      'Juni',       # Dutch names
               'Juli',    'Augustus', 'September',  # for the months
               'Oktober', 'November', 'December']   # of the year
```

- 묵시적으로 이어지는 줄들은 주석을 포함할 수 있습니다. 이어지는 줄들의 들여쓰기는 중요하지 않습니다. 중간에 빈 줄이 들어가도 됩니다. 묵시적으로 줄 결합하는 줄 들 간에는 NEWLINE 토큰이 만들어지지 않습니다. 묵시적으로 이어지는 줄들은 삼중 따옴표 된 문자열들에서도 등장할 수 있는데 (아래를 보라), 이 경우는 주석이 포함될 수 없습니다.

#### 빈 줄

- 스페이스, 탭, 폼 피드(formfeed) 와 주석만으로 구성된 논리적인 줄은 무시됩니다. (즉 NEWLINE 토큰이 만들어지지 않습니다.) 대화형으로 문장이 입력되는 도중에는 빈 줄의 처리가 REPL 구현에 따라 달라질 수 있습니다. 표준 대화형 인터프리터에서는, 완전히 빈 줄(즉 공백이나 주석조차 없는 것)은 다중 행 문장을 종료시킵니다.

#### 들여쓰기

- 논리적인 줄의 제일 앞에 오는 공백(스페이스와 탭)은 줄의 들여쓰기 수준을 계산하는 데 사용되고, 이는 다시 문장들의 묶음을 결정하는 데 사용되게 됩니다.
- 탭은 (왼쪽에서 오른쪽으로) 1~8개의 스페이스로 변환되는데, 치환된 후의 총 스페이스 문자 수가 8의 배수가 되도록 맞춥니다. (유닉스에서 사용되는 규칙에 맞추려는 것입니다.) 첫 번째 비 공백 문자 앞에 나오는 공백의 총수가 줄의 들여쓰기를 결정합니다. 들여쓰기는 역 슬래시를 사용해서 여러 개의 물리적인 줄로 나눠질 수 없습니다; 첫 번째 역 슬래시 이전의 공백이 들여쓰기를 결정합니다.
- 소스 파일이 탭과 스페이스를 섞어 쓰는 경우, 탭이 몇 개의 스페이스에 해당하는지에 따라 다르게 해석될 수 있으면 [`TabError`](https://docs.python.org/ko/3.12/library/exceptions.html#TabError "TabError") 를 일으킵니다.

> **크로스-플랫폼 호환성 유의 사항:** UNIX 이외의 플랫폼에서 편집기들이 동작하는 방식 때문에, 하나의 파일 내에서 들여쓰기를 위해 탭과 스페이스를 섞어 쓰는 것은 현명한 선택이 아닙니다. 다른 플랫폼들에서는 최대 들여쓰기 수준에 제한이 있을 수도 있다는 점도 주의해야 합니다.

- 폼 피드 문자는 줄의 처음에 나올 수 있습니다; 앞서 설명한 들여쓰기 수준 계산에서는 무시됩니다. 페이지 넘김 문자 앞에 공백이나 탭이 있는 경우는 정의되지 않은 효과를 줄 수 있습니다 (가령, 스페이스 수가 0으로 초기화될 수 있습니다).
- 연속된 줄의 들여쓰기 수준은, 스택을 사용해서, 다음과 같은 방법으로 INDENT와 DEDENT 토큰을 만드는 데 사용됩니다.
- 파일의 첫 줄을 읽기 전에 `0` 하나를 스택에 넣습니다(push); 이 값은 다시 꺼내는(pop) 일이 없습니다. 스택에 넣는 값은 항상 스택의 아래에서 위로 올라갈 때 단조 증가합니다. 각 논리적인 줄의 처음에서 줄의 들여쓰기 수준이 스택의 가장 위에 있는 값과 비교됩니다. 같다면 아무런 일도 일어나지 않습니다. 더 크다면 그 값을 스택에 넣고 하나의 INDENT 토큰을 만듭니다. 더 작다면 이 값은 스택에 있는 값 중 하나여야만 합니다. 이 값보다 큰 모든 스택의 값들을 꺼내고(pop), 꺼낸 횟수만큼의 DEDENT 토큰을 만듭니다. 파일의 끝에서, 스택에 남아있는 0보다 큰 값의 개수만큼 DEDENT 토큰을 만듭니다. 여기에 (혼란스럽다 할지라도) 올바르게 들여쓰기 된 파이썬 코드 조각이 있습니다:

```python
def perm(l):
        # Compute the list of all permutations of l
    if len(l) <= 1:
                  return [l]
    r = []
    for i in range(len(l)):
             s = l[:i] + l[i+1:]
             p = perm(s)
             for x in p:
              r.append(l[i:i+1] + x)
    return r
```

다음 예는 여러 가지 들여쓰기 에러를 보여줍니다:

```python
 def perm(l):                       # error: first line indented
for i in range(len(l)):             # error: not indented
    s = l[:i] + l[i+1:]
        p = perm(l[:i] + l[i+1:])   # error: unexpected indent
        for x in p:
                r.append(l[i:i+1] + x)
            return r                # error: inconsistent dedent
```

> 사실, 처음 세 개의 에러는 파서가 감지합니다. 단지 마지막 에러만 어휘 분석기가 감지합니다. — `return r` 의 들여쓰기가 스택에 있는 값과 일치하지 않습니다.

#### 토큰 사이의 공백

- 논리적인 줄의 처음과 문자열 리터럴을 제외하고, 공백 문자인 스페이스, 탭, 폼 피드는 토큰을 분리하기 위해 섞어 쓸 수 있습니다. 두 토큰을 붙여 쓸 때 다른 토큰으로 해석될 수 있는 경우만 토큰 사이에 공백이 필요합니다. (예를 들어, ab 는 하나의 토큰이지만, a b 는 두 개의 토큰입니다.)


### 식별자의 예약 영역
- (키워드와는 별개로) 어떤 부류의 식별자들은 특별한 의미가 있습니다. 이 부류의 식별자들은 시작과 끝의 밑줄 문자 패턴으로 구분됩니다:

`_*`
- `from module import *`에서 가져올 수 없습니다.

`_`
- [`match`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#match) 문 내의 `case` 패턴에서 `_`는 [와일드카드](https://docs.python.org/ko/3.12/reference/compound_stmts.html#wildcard-patterns)를 나타내는 [소프트 키워드](https://docs.python.org/ko/3.12/reference/lexical_analysis.html#soft-keywords)입니다.
- 이와 별도로 대화형 인터프리터는 마지막 평가의 결과를 `_` 변수에 저장합니다. (이 변수는 [`builtins`](https://docs.python.org/ko/3.12/library/builtins.html#module-builtins "builtins")에 저장됩니다: 내장 네임스페이스를 제공하는 모듈.") 모듈에 `print`와 같은 내장 함수와 함께 저장됩니다.)
- 다른 곳에서는 `_`가 일반 식별자입니다. "특별한" 항목의 이름을 지정하는 데 자주 사용되지만 파이썬 자체에는 특별하지 않습니다.

> 이름 `_` 은 종종 국제화(internationalization)와 관련되어 사용됩니다. 이 관례에 관해서는 [`gettext`](https://docs.python.org/ko/3.12/library/gettext.html#module-gettext "gettext: Multilingual internationalization services.") 모듈의 문서를 참조하십시오.

- 사용하지 않는 변수에도 일반적으로 사용됩니다.

`__*__`
- 시스템 정의 이름, 비공식적으로 “던더(dunder)” 이름이라고 알려졌습니다. 이 이름들은 인터프리터와 그 구현(표준 라이브러리를 포함합니다)이 정의합니다. 현재 정의된 시스템 이름은 [특수 메서드 이름들](https://docs.python.org/ko/3.12/reference/datamodel.html#specialnames) 섹션과 그 외의 곳에서 논의됩니다. 파이썬의 미래 버전에서는 더 많은 것들이 정의될 가능성이 큽니다. 어떤 문맥에서건, 명시적으로 문서로 만들어진 사용법을 벗어나는 `__*__` 이름의 _모든_ 사용은, 경고 없이 손상될 수 있습니다.

`__*`
- 클래스-비공개 이름. 이 부류의 이름들을 클래스 정의 문맥에서 사용하면 뒤섞인 형태로 변형됩니다. 부모 클래스와 자식 클래스의 “비공개(private)” 어트리뷰트 간의 이름 충돌을 피하기 위함입니다. [식별자 (이름)](https://docs.python.org/ko/3.12/reference/expressions.html#atom-identifiers) 섹션을 보세요.


## 대화형 시작 파일

- 파이썬을 대화형으로 사용할 때, 종종 인터프리터가 시작될 때마다 실행되는 표준 명령들이 있으면 편리합니다. [`PYTHONSTARTUP`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONSTARTUP) 환경 변수를 시작 명령이 들어있는 파일 이름으로 설정하면 됩니다. 이것은 유닉스 셸의 `.profile` 기능과 유사합니다.
- 이 파일은 대화형 세션에서만 읽히며, 파이썬이 스크립트에서 명령을 읽을 때나, `/dev/tty` 가 명령의 명시적 소스인 경우(대화형 세션처럼 동작한다)에는 읽지 않습니다. 대화형 명령이 실행되는 같은 이름 공간에서 실행되므로, 이 파일에서 정의하거나 임포트하는 객체들을 대화형 세션에서 정규화하지 않은 이름으로 사용할 수 있습니다. 이 파일에서 `sys.ps1` 및 `sys.ps2` 프롬프트를 변경할 수도 있습니다.
- 현재 디렉터리에서 추가 시작 파일을 읽으려면, 전역 시작 파일에서 `if os.path.isfile('.pythonrc.py'): exec(open('.pythonrc.py').read())` 와 같은 코드를 사용해서 프로그램할 수 있습니다. 스크립트에서 시작 파일을 사용하려면 스크립트에서 명시적으로 수행해야 합니다:

```python
import os
filename = os.environ.get('PYTHONSTARTUP')
if filename and os.path.isfile(filename):
    with open(filename) as fobj:
        startup_file = fobj.read()
    exec(startup_file)
```

## 커스터마이제이션 모듈

- 파이썬은 사용자 정의할 수 있는 두 가지 훅, 즉 사이트 사용자 정의와 사용자 사용자 정의를 제공합니다. 작동 방식을 확인하려면 먼저 사용자 사이트 패키지 디렉터리의 위치를 찾아야 합니다. Python을 시작하고 이 코드를 실행합니다:

```python
>>> import site
>>> site.getusersitepackages()
'/home/user/.local/lib/python3.x/site-packages'
```

- 이제 그 디렉터리에 `usercustomize.py` 라는 이름의 파일을 만들고 원하는 것들을 넣을 수 있습니다. 자동 임포트를 비활성화하는 [`-s`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-s) 옵션으로 시작하지 않는 한, 이 파일은 모든 파이썬 실행에 영향을 줍니다.
- 사이트 사용자 정의는 같은 방식으로 작동하지만 일반적으로 컴퓨터 관리자가 글로벌 사이트 패키지 디렉터리에서 생성하며 사용자 정의 전에 가져옵니다. 사이트별 구성을 담당하는 모듈인 [`site`](https://docs.python.org/ko/3.12/library/site.html#module-site "사이트: 사이트별 구성을 담당하는 모듈.") 모듈의 문서를 참조하세요.

## 확장 (Extensions)
**CPython**
- 원조이기도 하고 가장 잘 관리되고 있는 C로 작성된 파이썬 구현입니다. 언어의 새로운 기능은 보통 여기에서 처음 등장합니다.

**Jython**
- Java로 구현된 Python. 이 구현은 Java 애플리케이션의 스크립팅 언어로 사용하거나 Java 클래스 라이브러리를 사용하여 애플리케이션을 만드는 데 사용할 수 있습니다. 또한 Java 라이브러리에 대한 테스트를 생성하는 데 자주 사용됩니다. 자세한 내용은 [Jython 웹사이트](https://www.jython.org/)에서 확인할 수 있습니다.

**Python for .NET**
- 이 구현은 실제로는 CPython 구현을 사용하지만, 매니지드(managed) .NET 응용 프로그램이고 .NET 라이브러리를 제공합니다. Bryan Lloyd가 만들었습니다다. 더 자세한 정보는 [Python for .NET 홈페이지](https://pythonnet.github.io/) 에서 제공됩니다.

**IronPython**
- .NET용 대체 Python입니다. Python.NET과 달리 IL을 생성하고 Python 코드를 .NET 어셈블리로 직접 컴파일하는 완전한 Python 구현입니다. Jython의 원조인 Jim Hugunin이 만들었습니다. 자세한 내용은 [IronPython 웹사이트](https://ironpython.net/)를 참조하세요.

**PyPy**
- 완전히 파이썬으로 작성된 파이썬 구현입니다. 스택리스 지원 및 적시 컴파일러와 같이 다른 구현에서는 찾아볼 수 없는 여러 고급 기능을 지원합니다. 이 프로젝트의 목표 중 하나는 (파이썬으로 작성되었기 때문에) 인터프리터를 더 쉽게 수정할 수 있도록 하여 언어 자체에 대한 실험을 장려하는 것입니다. 자세한 정보는 [PyPy 프로젝트 홈페이지](https://www.pypy.org/)에서 확인할 수 있습니다.

> 각 구현은 이 설명서에서 설명되는 언어와 조금씩 각기 다른 방법으로 벗어나거나, 표준 파이썬 문서에서 다루는 범위 밖의 특별한 정보들을 소개합니다. 여러분이 사용 중인 구현에 대해 어떤 것을 더 알아야 하는지 판단하기 위해서는 구현 별로 제공되는 문서를 참조할 필요가 있습니다.

---
# 참조
[3.12.5 Documentation (python.org)](https://docs.python.org/ko/3/)
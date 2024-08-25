---
title: "[Python] 입출력 (Input & Output)"
excerpt: 
categories:
  - Python
tags:
  - Python
  - Input-Output
last_modified_at: 2024-04-11T15:10:55+09:00
link: 
상위 항목: "[[python_home|파이썬 (Python)]]"
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

---

- 프로그램의 출력을 표현하는 여러 가지 방법이 있습니다; 사람이 일기에 적합한 형태로 데이터를 인쇄할 수도 있고, 나중에 사용하기 위해 파일에 쓸 수도 있습니다.


## 문자 입출력

```python
print("Hello world")
```
- `print` 함수로 메시지를 출력할 수 있습니다.

```python
variable = input("설명 메시지")
```

- `input`은 입력한 값을 문자열 (`str`) 타입으로 저장합니다.
- `"설명 메시지"`는 설명을 위해 출력할 메시지를 결정합니다.
- 프로그램의 출력을 표현하는 여러 가지 방법이 있습니다; 사람이 일기에 적합한 형태로 데이터를 인쇄할 수도 있고, 나중에 사용하기 위해 파일에 쓸 수도 있습니다.

- 값을 작성하는 두 가지 방법: 표현식 문과 [`print()`](https://docs.python.org/ko/3.12/library/functions.html#print “print”) 함수 외에 세 번째 방법은 파일 객체의 [`write()`](https://docs.python.org/ko/3.12/library/io.html#io.TextIOBase.write “io.TextIOBase.write”) 메서드를 사용하는 것인데, 표준 출력 파일은 `sys.stdout`으로 참조할 수 있습니다.

## 파일 입출력

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


---
## 참조
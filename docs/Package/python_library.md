---
title: "[Python] 라이브러리 (Standard Library)"
excerpt: 
categories:
  - Python
tags:
  - Python
  - Module
  - Package
  - Python-Library
last_modified_at: 2024-04-11T15:10:55+09:00
link: https://docs.python.org/ko/3.12/library/index.html#library-index
상위 항목: "[[python_module|파이썬 모듈 (Python Module)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

**하위 항목**
- [[python_ai|파이썬 인공지능 (Python AI)]]
- [[python_logging|파이썬 로깅 (Python Logging)]]]]


---
> 본 문서는 표준 라이브러리의 간단한 설명만 다룹니다. 자세한 사용법 및 추가 설치가 필요한 라이브러리는 하위 문서를 참고하세요.

“파이썬 라이브러리”에는 여러 가지 구성 요소가 포함되어 있습니다.

여기에는 일반적으로 숫자 및 리스트와 같이 언어의 “핵심” 부분으로 간주하는 데이터형이 포함됩니다. 이러한 형의 경우, 파이썬 언어 핵심은 리터럴의 형식을 정의하고 그 의미에 몇 가지 제약을 가하지만, 의미를 완전히 정의하지는 않습니다. (반면에, 언어 핵심은 연산자의 철자법과 우선순위와 같은 문법적 속성을 정의합니다.)

라이브러리는 또한 내장 함수와 예외를 포함합니다 — [`import`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#import) 문을 쓰지 않고도 모든 파이썬 코드에서 사용할 수 있는 객체들입니다. 이들 중 일부는 언어 핵심에 의해 정의되지만, 핵심 의미에 필수적인 것은 아니며 여기에서 설명합니다.

그러나 라이브러리 대부분은 모듈 컬렉션으로 구성됩니다. 이 컬렉션을 나누는 데는 여러 가지 방법이 있습니다. 일부 모듈은 C로 작성되고 파이썬 인터프리터에 내장되어 있습니다; 다른 것은 파이썬으로 작성되고 소스 형식으로 임포트 됩니다. 일부 모듈은 스택 추적 인쇄와 같이 파이썬에 매우 특정한 인터페이스를 제공합니다; 일부는 특정 하드웨어에 대한 액세스와 같이 운영 체제에 특정한 인터페이스를 제공합니다; 다른 것은 월드 와이드 웹과 같은 응용 프로그램 영역에 특정한 인터페이스를 제공합니다. 일부 모듈은 파이썬의 모든 버전과 이식에서 사용할 수 있습니다; 다른 것은 하위 시스템이 지원하거나 요구할 때만 사용할 수 있습니다; 그러나 다른 것들은 파이썬이 컴파일되고 설치될 때 특정 설정 옵션이 선택되었을 때만 사용할 수 있습니다.

이 설명서는 “안쪽에서부터 밖으로” 구성되어 있습니다. 먼저 내장 함수, 데이터형 및 예외, 마지막으로 관련 모듈의 장으로 그룹화된 모듈들을 설명합니다.

즉, 처음부터 이 설명서를 읽고, 지루할 때 다음 장으로 건너뛰면, 파이썬 라이브러리가 지원하는 사용 가능한 모듈과 응용 프로그램 영역에 대한 적당한 개요를 얻게 됩니다. 물론 소설처럼 읽을 필요는 없습니다. (설명서 앞에 있는) 목차를 검색하거나, (뒤에 있는) 색인에서 특정 함수, 모듈 또는 용어를 찾을 수도 있습니다. 그리고 마지막으로, 무작위 주제에 대해 배우는 것을 즐긴다면, 임의의 페이지 번호 (모듈 [`random`](https://docs.python.org/ko/3.12/library/random.html#module-random "random: Generate pseudo-random numbers with various common distributions.") 참조)를 선택하고 한두 섹션을 읽으면 됩니다. 이 설명서의 섹션을 읽는 순서와 관계없이, [내장 함수](https://docs.python.org/ko/3.12/library/functions.html#built-in-funcs) 장에서 시작하는 것이 도움이 되는데, 설명서의 나머지 부분은 이 내용에 익숙하다고 가정하기 때문입니다.

## 가용성에 대한 참고 사항
- “가용성: 유닉스” 참고 사항은 이 기능이 유닉스 시스템에서 일반적으로 발견된다는 것을 뜻합니다. 특정 운영 체제에 이 기능이 존재하는지에 관한 어떠한 주장도 하지 않습니다.
    
- If not separately noted, all functions that claim “Availability: Unix” are supported on macOS, which builds on a Unix core.
    
- If an availability note contains both a minimum Kernel version and a minimum libc version, then both conditions must hold. For example a feature with note _Availability: Linux >= 3.17 with glibc >= 2.27_ requires both Linux 3.17 or newer and glibc 2.27 or newer.
    

### WebAssembly platforms

The [WebAssembly](https://webassembly.org/) platforms `wasm32-emscripten` ([Emscripten](https://emscripten.org/)) and `wasm32-wasi` ([WASI](https://wasi.dev/)) provide a subset of POSIX APIs. WebAssembly runtimes and browsers are sandboxed and have limited access to the host and external resources. Any Python standard library module that uses processes, threading, networking, signals, or other forms of inter-process communication (IPC), is either not available or may not work as on other Unix-like systems. File I/O, file system, and Unix permission-related functions are restricted, too. Emscripten does not permit blocking I/O. Other blocking operations like [`sleep()`](https://docs.python.org/ko/3.12/library/time.html#time.sleep "time.sleep") block the browser event loop.

The properties and behavior of Python on WebAssembly platforms depend on the [Emscripten](https://emscripten.org/)-SDK or [WASI](https://wasi.dev/)-SDK version, WASM runtimes (browser, NodeJS, [wasmtime](https://wasmtime.dev/)), and Python build time flags. WebAssembly, Emscripten, and WASI are evolving standards; some features like networking may be supported in the future.

For Python in the browser, users should consider [Pyodide](https://pyodide.org/) or [PyScript](https://pyscript.net/). PyScript is built on top of Pyodide, which itself is built on top of CPython and Emscripten. Pyodide provides access to browsers’ JavaScript and DOM APIs as well as limited networking capabilities with JavaScript’s `XMLHttpRequest` and `Fetch` APIs.

- Process-related APIs are not available or always fail with an error. That includes APIs that spawn new processes ([`fork()`](https://docs.python.org/ko/3.12/library/os.html#os.fork "os.fork"), [`execve()`](https://docs.python.org/ko/3.12/library/os.html#os.execve "os.execve")), wait for processes ([`waitpid()`](https://docs.python.org/ko/3.12/library/os.html#os.waitpid "os.waitpid")), send signals ([`kill()`](https://docs.python.org/ko/3.12/library/os.html#os.kill "os.kill")), or otherwise interact with processes. The [`subprocess`](https://docs.python.org/ko/3.12/library/subprocess.html#module-subprocess "subprocess: Subprocess management.") is importable but does not work.
    
- The [`socket`](https://docs.python.org/ko/3.12/library/socket.html#module-socket "socket: Low-level networking interface.") module is available, but is limited and behaves differently from other platforms. On Emscripten, sockets are always non-blocking and require additional JavaScript code and helpers on the server to proxy TCP through WebSockets; see [Emscripten Networking](https://emscripten.org/docs/porting/networking.html) for more information. WASI snapshot preview 1 only permits sockets from an existing file descriptor.
    
- Some functions are stubs that either don’t do anything and always return hardcoded values.
    
- Functions related to file descriptors, file permissions, file ownership, and links are limited and don’t support some operations. For example, WASI does not permit symlinks with absolute file names.

## 운영 체제 인터페이스
- [`os`](https://docs.python.org/ko/3.12/library/os.html#module-os "os: Miscellaneous operating system interfaces.") 모듈은 운영 체제와 상호 작용하기 위한 수십 가지 함수들을 제공합니다:

```python
>>> import os
>>> os.getcwd()      # Return the current working directory
'C:\\Python312'
>>> os.chdir('/server/accesslogs')   # Change current working directory
>>> os.system('mkdir today')   # Run the command mkdir in the system shell
0
```

- `from os import *` 대신에 `import os` 스타일을 사용해야 합니다. 그래야 [`os.open()`](https://docs.python.org/ko/3.12/library/os.html#os.open "os.open") 이 내장 [`open()`](https://docs.python.org/ko/3.12/library/functions.html#open "open") 을 가리는 것을 피할 수 있는데, 두 함수는 아주 다르게 동작합니다.
- [`os`](https://docs.python.org/ko/3.12/library/os.html#module-os "os: Miscellaneous operating system interfaces.") 와 같은 큰 모듈과 작업할 때, 내장 [`dir()`](https://docs.python.org/ko/3.12/library/functions.html#dir "dir") 과 [`help()`](https://docs.python.org/ko/3.12/library/functions.html#help "help") 함수는 대화형 도우미로 쓸모가 있습니다.

```python
>>> import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>
```

- 일상적인 파일과 디렉터리 관리 작업을 위해, [`shutil`](https://docs.python.org/ko/3.12/library/shutil.html#module-shutil "shutil: High-level file operations, including copying.") 모듈은 사용하기 쉬운 더 고수준의 인터페이스를 제공합니다:

```python
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'
```

## 파일 와일드카드

- [`glob`](https://docs.python.org/ko/3.12/library/glob.html#module-glob "glob: Unix shell style pathname pattern expansion.") 모듈은 디렉터리 와일드카드 검색으로 파일 목록을 만드는 함수를 제공합니다:

```python
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
```

## 명령행 인자

- 일반적인 유틸리티 스크립트는 명령줄 인수를 처리해야 하는 경우가 많습니다. 이러한 인수는 [`sys`](https://docs.python.org/ko/3.12/library/sys.html#module-sys "sys: 시스템별 매개변수 및 함수에 액세스합니다.") 모듈의 _argv_ 속성에 목록으로 저장됩니다. 예를 들어 다음 `demo.py` 파일을 살펴봅시다:

```python
# File demo.py
import sys
print(sys.argv)
```

다음은 명령줄에서 `python demo.py one two three`을 실행한 결과입니다:

```python
['demo.py', 'one', 'two', 'three']
```

```python
from math import exp

if __name__ == "__main__":
    import sys
    print(exp(sys.argv[1]))
```

- `sys.argv[1]` 은 파일명 다음에 입력한 인자값을 의미한다. `python <file>.py 50` 과 같이 실행할 수 있습니다.
- [`argparse`](https://docs.python.org/ko/3.12/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.") 모듈은 명령 줄 인자를 처리하는 더 정교한 메커니즘을 제공합니다. 다음 스크립트는 하나 이상의 파일명과 선택적으로 표시할 줄 수를 추출합니다:

```python
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
```

- `python top.py --lines=5 alpha.txt beta.txt`를 사용하여 명령 줄에서 실행할 때, 스크립트는 `args.lines`를 `5`로, `args.filenames`를 `['alpha.txt', 'beta.txt']`로 설정합니다.



## 에러 출력 리디렉션과 프로그램 종료

- [`sys`](https://docs.python.org/ko/3.12/library/sys.html#module-sys "sys: Access system-specific parameters and functions.") 모듈은 _stdin_, _stdout_, _stderr_ 어트리뷰트도 갖고 있습니다. 가장 마지막 것은 _stdout_ 이 리디렉트 되었을 때도 볼 수 있는 경고와 에러 메시지들을 출력하는데 쓸모가 있습니다:

```python
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
```

- 스크립트를 종료하는 가장 직접적인 방법은 `sys.exit()` 를 쓰는 것입니다.

## 문자열 패턴 매칭

- [`re`](https://docs.python.org/ko/3.12/library/re.html#module-re "re: Regular expression operations.") 모듈은 고급 문자열 처리를 위한 정규식 도구들을 제공합니다. 복잡한 매칭과 조작을 위해, 정규식은 간결하고 최적화된 솔루션을 제공합니다:

```python
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
```

- 단지 간단한 기능만 필요한 경우에는, 문자열 메서드들이 선호되는데 읽기 쉽고 디버깅이 쉽기 때문입니다:

```python
>>> 'tea for too'.replace('too', 'two')
'tea for two'
```


## 수학
- [`math`](https://docs.python.org/ko/3.12/library/math.html#module-math) 모듈은 부동소수점 수학을 위한 기본 C 라이브러리 함수에 대한 액세스를 제공합니다:

```python
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0
```

- [`random`](https://docs.python.org/ko/3.12/library/random.html#module-random "random: Generate pseudo-random numbers with various common distributions.") 모듈은 무작위 선택을 할 수 있는 도구들을 제공합니다:

```python
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float
0.17970987693706186
>>> random.randrange(6)    # random integer chosen from range(6)
4
```

- [`statistics`](https://docs.python.org/ko/3.12/library/statistics.html#module-statistics "statistics: Mathematical statistics functions") 모듈은 수치 데이터의 기본적인 통계적 특성들을 (평균, 중간값, 분산, 등등) 계산합니다.

```python
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
```

- SciPy 프로젝트 <[https://scipy.org](https://scipy.org/)> 는 다른 수치 계산용 모듈들을 많이 갖고 있습니다.

## 인터넷 액세스

- 인터넷을 액세스하고 인터넷 프로토콜들을 처리하는 많은 모듈이 있습니다. 가장 간단한 두 개는 URL에서 데이터를 읽어오는 [`urllib.request`](https://docs.python.org/ko/3.12/library/urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs.") 와 메일을 보내는 [`smtplib`](https://docs.python.org/ko/3.12/library/smtplib.html#module-smtplib "smtplib: SMTP protocol client (requires sockets).") 입니다:

```python
>>> from urllib.request import urlopen
>>> with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
...     for line in response:
...         line = line.decode()             # Convert bytes to a str
...         if line.startswith('datetime'):
...             print(line.rstrip())         # Remove trailing newline
...
datetime: 2022-01-01T01:36:47.689215+00:00
```

```python
>>> import smtplib
>>> server = smtplib.SMTP('localhost')
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
... """To: jcaesar@example.org
... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)
>>> server.quit()
```

- (두 번째 예는 localhost 에서 메일 서버가 실행되고 있어야 한다는 것에 주의하세요.)

## 날짜와 시간

- [`datetime`](https://docs.python.org/ko/3.12/library/datetime.html#module-datetime "datetime: Basic date and time types.") 모듈은 날짜와 시간을 조작하는 클래스들을 제공하는데, 간단한 방법과 복잡한 방법 모두 제공합니다. 날짜와 시간 산술이 지원되지만, 구현의 초점은 출력 포매팅과 조작을 위해 효율적으로 멤버를 추출하는 데에 맞춰져 있습니다. 모듈은 시간대를 고려하는 객체들도 지원합니다.

```python
>>> # dates are easily constructed and formatted
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

>>> # dates support calendar arithmetic
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368
```

## 데이터 압축

- 일반적인 데이터 보관 및 압축 형식들을 다음과 같은 모듈들이 직접 지원합니다: [`zlib`](https://docs.python.org/ko/3.12/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip."), [`gzip`](https://docs.python.org/ko/3.12/library/gzip.html#module-gzip "gzip: Interfaces for gzip compression and decompression using file objects."), [`bz2`](https://docs.python.org/ko/3.12/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression."), [`lzma`](https://docs.python.org/ko/3.12/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library."), [`zipfile`](https://docs.python.org/ko/3.12/library/zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files."), [`tarfile`](https://docs.python.org/ko/3.12/library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files.").

```python
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
```

## 성능 측정

- 일부 파이썬 사용자들은 같은 문제에 대한 다른 접근법들의 상대적인 성능을 파악하는데 깊은 관심을 두고 있습니다. 파이썬은 이런 질문들에 즉시 답을 주는 측정 도구를 제공합니다.
- 예를 들어, 인자들을 맞교환하는 전통적인 방식 대신에, 튜플 패킹과 언 패킹을 사용하고자 하는 유혹을 느낄 수 있습니다. [`timeit`](https://docs.python.org/ko/3.12/library/timeit.html#module-timeit "timeit: Measure the execution time of small code snippets.") 모듈은 적당한 성능 이점을 신속하게 보여줍니다:

```python
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791
```

- [`timeit`](https://docs.python.org/ko/3.12/library/timeit.html#module-timeit "timeit: Measure the execution time of small code snippets.") 의 정밀도와는 대조적으로, [`profile`](https://docs.python.org/ko/3.12/library/profile.html#module-profile "profile: Python source profiler.") 과 [`pstats`](https://docs.python.org/ko/3.12/library/profile.html#module-pstats "pstats: Statistics object for use with the profiler.") 모듈은 큰 블록의 코드에서 시간 임계 섹션을 식별하기 위한 도구들을 제공합니다.

## 품질 관리

- 고품질의 소프트웨어를 개발하는 한 가지 접근법은 개발되는 각 함수에 대한 테스트를 작성하고, 그것들을 개발 프로세스 중에 자주 실행하는 것입니다.
- [`doctest`](https://docs.python.org/ko/3.12/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.") 모듈은 모듈을 훑어보고 프로그램의 독스트링들에 내장된 테스트들을 검사하는 도구를 제공합니다. 테스트 만들기는 평범한 호출을 그 결과와 함께 독스트링으로 복사해서 붙여넣기를 하는 수준으로 간단해집니다. 사용자에게 예제를 함께 제공해서 설명서를 개선하고, doctest 모듈이 설명서에서 코드가 여전히 사실인지 확인하도록 합니다.

```python
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)
```

```python
import doctest
doctest.testmod()   # automatically validate the embedded tests
```

- [`unittest`](https://docs.python.org/ko/3.12/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") 모듈은 [`doctest`](https://docs.python.org/ko/3.12/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.") 모듈만큼 쉬운 것은 아니지만, 더욱 포괄적인 테스트 집합을 별도의 파일로 관리할 수 있게 합니다:

```python
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests
```

## 배터리가 포함됩니다
- 파이썬은 “배터리가 포함됩니다” 철학을 갖고 있습니다. 이는 더 큰 패키지의 정교하고 강력한 기능을 통해 가장 잘 나타납니다. 예를 들어:

- [`xmlrpc.client`](https://docs.python.org/ko/3.12/library/xmlrpc.client.html#module-xmlrpc.client "xmlrpc.client: XML-RPC 클라이언트 액세스.") 및 [`xmlrpc.server`](https://docs.python.org/ko/3.12/library/xmlrpc.server.html#module-xmlrpc.server "xmlrpc.server: 기본 XML-RPC 서버 구현.") 모듈은 원격 프로시저 호출을 거의 간단한 작업으로 구현할 수 있게 해줍니다. 모듈의 이름과는 달리 XML에 대한 직접적인 지식이나 처리가 필요하지 않습니다.
- [`email`](https://docs.python.org/ko/3.12/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.") 패키지는 MIME 및 기타 [**RFC 2822**](https://datatracker.ietf.org/doc/html/rfc2822.html) 기반 메시지 문서를 포함하는 전자 메일 메시지를 관리하기 위한 라이브러리입니다. 실제로 메시지를 보내고 받는 [`smtplib`](https://docs.python.org/ko/3.12/library/smtplib.html#module-smtplib "smtplib: SMTP protocol client (requires sockets).") 와 [`poplib`](https://docs.python.org/ko/3.12/library/poplib.html#module-poplib "poplib: POP3 protocol client (requires sockets).") 와는 달리, email 패키지는 복잡한 메시지 구조 (첨부 파일 포함) 를 작성하거나 해독하고 인터넷 인코딩과 헤더 프로토콜을 구현하기 위한 완벽한 도구 상자를 가지고 있습니다.
- [`json`](https://docs.python.org/ko/3.12/library/json.html#module-json "json: Encode and decode the JSON format.") 패키지는 널리 사용되는 데이터 교환 형식을 파싱하기위한 강력한 지원을 제공합니다. [`csv`](https://docs.python.org/ko/3.12/library/csv.html#module-csv "csv: Write and read tabular data to and from delimited files.") 모듈은 데이터베이스와 스프레드시트에서 일반적으로 지원되는 쉼표로 구분된 값 형식으로 파일을 직접 읽고 쓸 수 있도록 지원합니다. XML 처리는 [`xml.etree.ElementTree`](https://docs.python.org/ko/3.12/library/xml.etree.elementtree.html#module-xml.etree.ElementTree "xml.etree.ElementTree: Implementation of the ElementTree API."), [`xml.dom`](https://docs.python.org/ko/3.12/library/xml.dom.html#module-xml.dom "xml.dom: Document Object Model API for Python.") 및 [`xml.sax`](https://docs.python.org/ko/3.12/library/xml.sax.html#module-xml.sax "xml.sax: Package containing SAX2 base classes and convenience functions.") 패키지에 의해 지원됩니다. 이러한 모듈과 패키지를 함께 사용하면 파이썬 응용 프로그램과 다른 도구 간의 데이터 교환이 크게 단순해집니다.
- [`sqlite3`](https://docs.python.org/ko/3.12/library/sqlite3.html#module-sqlite3 "sqlite3: A DB-API 2.0 implementation using SQLite 3.x.") 모듈은 SQLite 데이터베이스 라이브러리의 래퍼인데, 약간 비표준 SQL 구문을 사용하여 업데이트되고 액세스 될 수 있는 퍼시스턴트 데이터베이스를 제공합니다.
- 국제화는 [`gettext`](https://docs.python.org/ko/3.12/library/gettext.html#module-gettext "gettext: Multilingual internationalization services."), [`locale`](https://docs.python.org/ko/3.12/library/locale.html#module-locale "locale: Internationalization services."), 그리고 [`codecs`](https://docs.python.org/ko/3.12/library/codecs.html#module-codecs "codecs: Encode and decode data and streams.") 패키지를 포함한 많은 모듈에 의해 지원됩니다.

전문 프로그래밍 요구 사항을 지원하는 고급 모듈을 다루고 있습니다. 이러한 모듈은 작은 스크립트에서는 거의 사용되지 않습니다.

---
> 아래 라이브러리는 전문 프로그래밍 요구 사항을 지원하는 고급 모듈입니다.

## 출력 포매팅

- [`reprlib`](https://docs.python.org/ko/3.12/library/reprlib.html#module-reprlib "reprlib: Alternate repr() implementation with size limits.") 모듈은 크거나 깊게 중첩된 컨테이너의 축약 된 디스플레이를 위해 커스터마이즈된 [`repr()`](https://docs.python.org/ko/3.12/library/functions.html#repr "repr") 의 버전을 제공합니다:

```python
>>> import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', …}"
```

- [`pprint`](https://docs.python.org/ko/3.12/library/pprint.html#module-pprint "pprint: Data pretty printer.") 모듈은 인터프리터가 읽을 수 있는 방식으로 내장 객체나 사용자 정의 객체를 인쇄하는 것을 보다 정교하게 제어할 수 있게 합니다. 결과가 한 줄보다 길면 “예쁜 프린터”가 줄 바꿈과 들여쓰기를 추가하여 데이터 구조를 보다 명확하게 나타냅니다:

```python
>>> import pprint
>>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
…     'yellow'], 'blue']]]
…
>>> pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
```

- [`textwrap`](https://docs.python.org/ko/3.12/library/textwrap.html#module-textwrap "textwrap: Text wrapping and filling") 모듈은 텍스트의 문단을 주어진 화면 너비에 맞게 포맷합니다:

```python
>>> import textwrap
>>> doc = """The wrap() method is just like fill() except that it returns
… a list of strings instead of one big string with newlines to separate
… the wrapped lines."""
…
>>> print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
```

- [`locale`](https://docs.python.org/ko/3.12/library/locale.html#module-locale "locale: Internationalization services.") 모듈은 문화권 특정 데이터 포맷의 데이터베이스에 액세스합니다. locale의 format 함수의 grouping 어트리뷰트는 그룹 구분 기호로 숫자를 포매팅하는 직접적인 방법을 제공합니다:

```python
>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'English_United States')
'English_United States'
>>> conv = locale.localeconv()          # get a mapping of conventions
>>> x = 1234567.8
>>> locale.format_string("%d", x, grouping=True)
'1,234,567'
>>> locale.format_string("%s%.*f", (conv['currency_symbol'],
…                      conv['frac_digits'], x), grouping=True)
'$1,234,567.80'
```

## 템플릿

- [`string`](https://docs.python.org/ko/3.12/library/string.html#module-string "string: Common string operations.") 모듈은 다재다능한 [`Template`](https://docs.python.org/ko/3.12/library/string.html#string.Template "string.Template") 클래스를 포함하고 있는데, 최종 사용자가 편집하기에 적절한 단순한 문법을 갖고 있습니다. 따라서 사용자는 응용 프로그램을 변경하지 않고도 응용 프로그램을 커스터마이즈할 수 있습니다.
- 형식은 `$` 와 유효한 파이썬 식별자 (영숫자와 밑줄)로 만들어진 자리표시자 이름을 사용합니다. 중괄호를 사용하여 자리표시자를 둘러싸면 공백없이 영숫자가 뒤따르도록 할 수 있습니다. `$$` 을 쓰면 하나의 이스케이프 된 `$` 를 만듭니다:

```python
>>> from string import Template
>>> t = Template('${village}folk send $$10 to $cause.')
>>> t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'
```

- [`substitute()`](https://docs.python.org/ko/3.12/library/string.html#string.Template.substitute "string.Template.substitute") 메서드는 자리표시자가 딕셔너리나 키워드 인자로 제공되지 않을 때 [`KeyError`](https://docs.python.org/ko/3.12/library/exceptions.html#KeyError "KeyError") 를 일으킵니다. 메일 병합 스타일 응용 프로그램의 경우 사용자가 제공한 데이터가 불완전할 수 있으며 [`safe_substitute()`](https://docs.python.org/ko/3.12/library/string.html#string.Template.safe_substitute "string.Template.safe_substitute") 메서드가 더 적절할 수 있습니다. 데이터가 누락 된 경우 자리표시자를 변경하지 않습니다:

```python
>>> t = Template('Return the $item to $owner.')
>>> d = dict(item='unladen swallow')
>>> t.substitute(d)
Traceback (most recent call last):
  …
KeyError: 'owner'
>>> t.safe_substitute(d)
'Return the unladen swallow to $owner.'
```

- Template 서브 클래스는 사용자 정의 구분자를 지정할 수 있습니다. 예를 들어 사진 브라우저를 위한 일괄 이름 바꾸기 유틸리티는 현재 날짜, 이미지 시퀀스 번호 또는 파일 형식과 같은 자리표시자에 백분율 기호를 사용하도록 선택할 수 있습니다:

```python
>>> import time, os.path
>>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
>>> class BatchRename(Template):
…     delimiter = '%'
…
>>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

>>> t = BatchRename(fmt)
>>> date = time.strftime('%d%b%y')
>>> for i, filename in enumerate(photofiles):
…     base, ext = os.path.splitext(filename)
…     newname = t.substitute(d=date, n=i, f=ext)
…     print('{0} --> {1}'.format(filename, newname))
```

```
img_1074.jpg --> Ashley_0.jpg
img_1076.jpg --> Ashley_1.jpg
img_1077.jpg --> Ashley_2.jpg
```

- 템플릿의 또 다른 응용은 다중 출력 형식의 세부 사항에서 프로그램 논리를 분리하는 것입니다. 이렇게 하면 XML 파일, 일반 텍스트 보고서 및 HTML 웹 보고서에 대한 커스텀 템플릿을 치환할 수 있습니다.

## 바이너리 데이터 레코드 배치 작업

- [`struct`](https://docs.python.org/ko/3.12/library/struct.html#module-struct "struct: Interpret bytes as packed binary data.") 모듈은 가변 길이 바이너리 레코드 형식으로 작업하기 위한 [`pack()`](https://docs.python.org/ko/3.12/library/struct.html#struct.pack "struct.pack") 과 [`unpack()`](https://docs.python.org/ko/3.12/library/struct.html#struct.unpack "struct.unpack") 함수를 제공합니다. 다음 예제는 [`zipfile`](https://docs.python.org/ko/3.12/library/zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files.") 모듈을 사용하지 않고 ZIP 파일의 헤더 정보를 루핑하는 법을 보여줍니다. 팩 코드 `"H"` 와 `"I"` 는 각각 2바이트와 4바이트의 부호 없는 숫자를 나타냅니다. `"<"` 는 표준 크기이면서 리틀 엔디안 바이트 순서를 가짐을 나타냅니다:

```python
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header
```

## 다중 스레딩

- 스레딩은 차례로 종속되지 않는 작업을 분리하는 기술입니다. 스레드는 다른 작업이 백그라운드에서 실행되는 동안 사용자 입력을 받는 응용 프로그램의 응답을 향상하는 데 사용할 수 있습니다. 관련된 사용 사례는 다른 스레드의 계산과 병렬로 I/O를 실행하는 경우입니다.
- 다음 코드는 메인 프로그램이 계속 실행되는 동안 고수준 [`threading`](https://docs.python.org/ko/3.12/library/threading.html#module-threading "threading: Thread-based parallelism.") 모듈이 백그라운드에서 작업을 어떻게 수행할 수 있는지 보여줍니다:

```python
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')
```

- 다중 스레드 응용 프로그램의 가장 큰 문제점은 데이터 또는 다른 자원을 공유하는 스레드를 조정하는 것입니다. 이를 위해 threading 모듈은 록, 이벤트, 조건 변수 및 세마포어를 비롯한 많은 수의 동기화 기본 요소를 제공합니다.
- 이러한 도구는 강력하지만, 사소한 설계 오류로 인해 재현하기 어려운 문제가 발생할 수 있습니다. 따라서, 작업 조정에 대한 선호되는 접근 방식은 자원에 대한 모든 액세스를 단일 스레드에 집중시킨 다음 [`queue`](https://docs.python.org/ko/3.12/library/queue.html#module-queue "queue: A synchronized queue class.") 모듈을 사용하여 해당 스레드에 다른 스레드의 요청을 제공하는 것입니다. 스레드 간 통신 및 조정을 위한 [`Queue`](https://docs.python.org/ko/3.12/library/queue.html#queue.Queue "queue.Queue") 객체를 사용하는 응용 프로그램은 설계하기 쉽고, 읽기 쉽고, 신뢰성이 높습니다.

## 로깅

- [`logging`](https://docs.python.org/ko/3.12/library/logging.html#module-logging "logging: Flexible event logging system for applications.") 모듈은 완전한 기능을 갖춘 유연한 로깅 시스템을 제공합니다. 가장 단순한 경우, 로그 메시지는 파일이나 `sys.stderr` 로 보내집니다:

```python
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
```

그러면 다음과 같은 결과가 출력됩니다:

```
WARNING:root:Warning:config file server.conf not found
ERROR:root:Error occurred
CRITICAL:root:Critical error -- shutting down
```

- 기본적으로 정보 및 디버깅 메시지는 표시되지 않고 출력은 표준 에러로 보내집니다. 다른 출력 옵션에는 전자 메일, 데이터 그램, 소켓 또는 HTTP 서버를 통한 메시지 라우팅이 포함됩니다. 새로운 필터는 메시지 우선순위에 따라 다른 라우팅을 선택할 수 있습니다: [`DEBUG`](https://docs.python.org/ko/3.12/library/logging.html#logging.DEBUG "logging.DEBUG"), [`INFO`](https://docs.python.org/ko/3.12/library/logging.html#logging.INFO "logging.INFO"), [`WARNING`](https://docs.python.org/ko/3.12/library/logging.html#logging.WARNING "logging.WARNING"), [`ERROR`](https://docs.python.org/ko/3.12/library/logging.html#logging.ERROR "logging.ERROR") , 그리고 [`CRITICAL`](https://docs.python.org/ko/3.12/library/logging.html#logging.CRITICAL "logging.CRITICAL").
- 로깅 시스템은 파이썬에서 직접 구성하거나, 응용 프로그램을 변경하지 않고 사용자 정의 로깅을 위해 사용자가 편집할 수 있는 설정 파일에서 로드 할 수 있습니다.

## 약한 참조

- 파이썬은 자동 메모리 관리 (대부분 객체에 대한 참조 횟수 추적 및 순환을 제거하기 위한 [가비지 수거](https://docs.python.org/ko/3.12/glossary.html#term-garbage-collection))를 수행합니다. 메모리는 마지막 참조가 제거된 직후에 해제됩니다.
- 이 접근법은 대부분의 응용 프로그램에서 잘 작동하지만, 때로는 다른 것들에 의해 사용되는 동안에만 객체를 추적해야 할 필요가 있습니다. 불행하게도, 단지 그것들을 추적하는 것만으로도 그들을 영구적으로 만드는 참조를 만듭니다. [`weakref`](https://docs.python.org/ko/3.12/library/weakref.html#module-weakref "weakref: Support for weak references and weak dictionaries.") 모듈은 참조를 만들지 않고 객체를 추적할 수 있는 도구를 제공합니다. 객체가 더 필요하지 않으면 weakref 테이블에서 객체가 자동으로 제거되고 weakref 객체에 대한 콜백이 트리거됩니다. 일반적인 응용에는 만드는 데 비용이 많이 드는 개체 캐싱이 포함됩니다:

```python
>>> import weakref, gc
>>> class A:
…     def __init__(self, value):
…         self.value = value
…     def __repr__(self):
…         return str(self.value)
…
>>> a = A(10)                   # create a reference
>>> d = weakref.WeakValueDictionary()
>>> d['primary'] = a            # does not create a reference
>>> d['primary']                # fetch the object if it is still alive
10
>>> del a                       # remove the one reference
>>> gc.collect()                # run garbage collection right away
0
>>> d['primary']                # entry was automatically removed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary']                # entry was automatically removed
  File "C:/python312/lib/weakref.py", line 46, in __getitem__
    o = self.data[key]()
KeyError: 'primary'
```

## 리스트 작업 도구

- 내장 리스트 형으로 많은 데이터 구조 요구를 충족시킬 수 있습니다. 그러나 때로는 다른 성능 상충 관계가 있는 대안적 구현이 필요할 수도 있습니다.
- [`array`](https://docs.python.org/ko/3.12/library/array.html#module-array "array: 균일하게 입력된 숫자 값의 공간 효율적인 배열.") 모듈은 동종 데이터만 저장하는 목록과 같은 [`array`](https://docs.python.org/ko/3.12/library/array.html#array.array "array.array") 객체를 제공하여 보다 컴팩트하게 저장합니다. 다음 예제는 일반적인 파이썬 int 객체 목록의 항목당 16바이트가 아닌 2바이트 부호 없는 이진수(타입코드 `"H"`)로 저장된 숫자 배열을 보여줍니다:

```python
>>> from array import array
>>> a = array('H', [4000, 10, 700, 22222])
>>> sum(a)
26932
>>> a[1:3]
array('H', [10, 700])
```

- [`collections`](https://docs.python.org/ko/3.12/library/collections.html#module-collections "collections: 컨테이너 데이터 타입") 모듈은 왼쪽에서 추가 및 팝이 빠르지만 가운데에서 조회 속도가 느린 목록과 같은 [`deque`](https://docs.python.org/ko/3.12/library/collections.html#collections.deque "collections.deque") 객체를 제공합니다. 이러한 객체는 대기열과 폭 우선 트리 검색을 구현하는 데 적합합니다:

```python
>>> from collections import deque
>>> d = deque(["task1", "task2", "task3"])
>>> d.append("task4")
>>> print("Handling", d.popleft())
Handling task1

unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)
```

- 대안적 리스트 구현 외에도 라이브러리는 정렬된 리스트를 조작하는 함수들이 있는 [`bisect`](https://docs.python.org/ko/3.12/library/bisect.html#module-bisect "bisect: Array bisection algorithms for binary searching.") 모듈과 같은 다른 도구를 제공합니다:

```python
>>> import bisect
>>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
>>> bisect.insort(scores, (300, 'ruby'))
>>> scores
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
```

- [`heapq`](https://docs.python.org/ko/3.12/library/heapq.html#module-heapq "heapq: Heap queue algorithm (a.k.a. priority queue).") 모듈은 일반 리스트를 기반으로 힙을 구현하는 함수를 제공합니다. 가장 값이 작은 항목은 항상 위치 0에 유지됩니다. 이것은 가장 작은 요소에 반복적으로 액세스하지만, 전체 목록 정렬을 실행하지 않으려는 응용에 유용합니다:

```python
>>> from heapq import heapify, heappop, heappush
>>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
>>> heapify(data)                      # rearrange the list into heap order
>>> heappush(data, -5)                 # add a new entry
>>> [heappop(data) for i in range(3)]  # fetch the three smallest entries
[-5, 0, 1]
```

## 십진수 부동 소수점 산술 (Decimal Floating-Point Arithmetic)

- [`decimal`](https://docs.python.org/ko/3.12/library/decimal.html#module-decimal "decimal: 일반 십진수 산술 사양의 구현.") 모듈은 십진수 부동 소수점 산술을 위한 [`Decimal`](https://docs.python.org/ko/3.12/library/decimal.html#decimal.Decimal "decimal.Decimal") 데이터형을 제공합니다. 이 클래스는 이진 부동소수점의 내장 [`float`](https://docs.python.org/ko/3.12/library/functions.html#float "float") 구현과 비교했을 때 특히 다음과 같은 경우에 유용합니다.
  - 정확한 10진수 표현이 필요한 금융 응용 및 기타 용도,
  - 정밀도 제어,
  - 법적 또는 규제 요구 사항을 충족하는 반올림 제어,
  - 유효숫자 추적, 또는 사용자가 결과가 손으로 계산한 것과 일치 할 것으로 기대하는 응용.
- 예를 들어, 70센트 전화 요금에 대해 5% 세금을 계산하면, 십진 부동 소수점 및 이진 부동 소수점에 다른 결과가 나타납니다. 결과를 가장 가까운 센트로 반올림하면 차이가 드러납니다:

```python
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round( * 1.05, 2)
0.73
```

- [`Decimal`](https://docs.python.org/ko/3.12/library/decimal.html#decimal.Decimal "decimal.Decimal") 결과는 끝에 붙는 0을 유지하며, 두 개의 유효숫자를 가진 피승수로부터 네 자리의 유효숫자를 자동으로 추론합니다. Decimal은 손으로 한 수학을 재현하고 이진 부동 소수점이 십진수를 정확하게 표현할 수 없을 때 발생할 수 있는 문제를 피합니다.
- 정확한 표현은 [`Decimal`](https://docs.python.org/ko/3.12/library/decimal.html#decimal.Decimal "decimal.Decimal") 클래스가 이진 부동 소수점에 적합하지 않은 모듈로 계산과 동등성 검사를 수행할 수 있도록 합니다:

```python
>>> Decimal('1.00') % Decimal('')
Decimal('0.00')
>>> 1.00 % 0.10
0.09999999999999995

>>> sum([Decimal('0.1')]*10) == Decimal('1.0')
True
>>> 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0
False
```

- [`decimal`](https://docs.python.org/ko/3.12/library/decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic  Specification.") 모듈은 필요한 만큼의 정밀도로 산술을 제공합니다:

```python
>>> getcontext().prec = 36
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857')
```


---

## 예제

## 참조
### 텍스트 처리
- [re — Regular expression operations — Python 3.12.5 문서](https://docs.python.org/ko/3.12/library/re.html)
- [difflib — Helpers for computing deltas — Python 3.12.5 문서](https://docs.python.org/ko/3.12/library/difflib.html)
- [textwrap — Text wrapping and filling — Python 3.12.5 문서](https://docs.python.org/ko/3.12/library/textwrap.html)
- [unicodedata — Unicode Database — Python 3.12.5 문서](https://docs.python.org/ko/3.12/library/unicodedata.html)
- [stringprep — Internet String Preparation — Python 3.12.5 문서](https://docs.python.org/ko/3.12/library/stringprep.html)
- [readline — GNU readline interface — Python 3.12.5 문서](https://docs.python.org/ko/3.12/library/readline.html)
- [rlcompleter — Completion function for GNU readline — Python 3.12.5 문서](https://docs.python.org/ko/3.12/library/rlcompleter.html)
### 바이너리 데이터 서비스
- [`struct` — Interpret bytes as packed binary data](https://docs.python.org/ko/3.12/library/struct.html)
- [`codecs` — Codec registry and base classes](https://docs.python.org/ko/3.12/library/codecs.html)
- [데이터형](https://docs.python.org/ko/3.12/library/datatypes.html)
- [`datetime` — Basic date and time types](https://docs.python.org/ko/3.12/library/datetime.html)
- [`zoneinfo` — IANA time zone support](https://docs.python.org/ko/3.12/library/zoneinfo.html)
- [`calendar` — General calendar-related functions](https://docs.python.org/ko/3.12/library/calendar.html)
- [`collections` — Container datatypes](https://docs.python.org/ko/3.12/library/collections.html)
- [`collections.abc` — Abstract Base Classes for Containers](https://docs.python.org/ko/3.12/library/collections.abc.html)
- [`heapq` — Heap queue algorithm](https://docs.python.org/ko/3.12/library/heapq.html)
- [`bisect` — Array bisection algorithm](https://docs.python.org/ko/3.12/library/bisect.html)
- [`array` — Efficient arrays of numeric values](https://docs.python.org/ko/3.12/library/array.html)
- [`weakref` — 약한 참조](https://docs.python.org/ko/3.12/library/weakref.html)
- [`types` — Dynamic type creation and names for built-in types](https://docs.python.org/ko/3.12/library/types.html)
- [`copy` — Shallow and deep copy operations](https://docs.python.org/ko/3.12/library/copy.html)
- [`pprint` — Data pretty printer](https://docs.python.org/ko/3.12/library/pprint.html)
- [`reprlib` — Alternate `repr()` implementation](https://docs.python.org/ko/3.12/library/reprlib.html)
- [`enum` — Support for enumerations](https://docs.python.org/ko/3.12/library/enum.html)
- [`graphlib` — Functionality to operate with graph-like structures](https://docs.python.org/ko/3.12/library/graphlib.html)
###  [숫자와 수학 모듈](https://docs.python.org/ko/3.12/library/numeric.html)
- [`numbers` — Numeric abstract base classes](https://docs.python.org/ko/3.12/library/numbers.html)
- [`math` — Mathematical functions](https://docs.python.org/ko/3.12/library/math.html)
- [`cmath` — Mathematical functions for complex numbers](https://docs.python.org/ko/3.12/library/cmath.html)
- [`decimal` — Decimal fixed-point and floating-point arithmetic](https://docs.python.org/ko/3.12/library/decimal.html)
- [`fractions` — Rational numbers](https://docs.python.org/ko/3.12/library/fractions.html)
- [`random` — Generate pseudo-random numbers](https://docs.python.org/ko/3.12/library/random.html)
- [`statistics` — Mathematical statistics functions](https://docs.python.org/ko/3.12/library/statistics.html)
###  [함수형 프로그래밍 모듈](https://docs.python.org/ko/3.12/library/functional.html)
- [`itertools` — Functions creating iterators for efficient looping](https://docs.python.org/ko/3.12/library/itertools.html)
- [`functools` — Higher-order functions and operations on callable objects](https://docs.python.org/ko/3.12/library/functools.html)
- [`operator` — Standard operators as functions](https://docs.python.org/ko/3.12/library/operator.html)
###  [파일과 디렉터리 액세스](https://docs.python.org/ko/3.12/library/filesys.html)
- [`pathlib` — Object-oriented filesystem paths](https://docs.python.org/ko/3.12/library/pathlib.html)
- [`os.path` — Common pathname manipulations](https://docs.python.org/ko/3.12/library/os.path.html)
- [`fileinput` — Iterate over lines from multiple input streams](https://docs.python.org/ko/3.12/library/fileinput.html)
- [`stat` — Interpreting `stat()` results](https://docs.python.org/ko/3.12/library/stat.html)
- [`filecmp` — File and Directory Comparisons](https://docs.python.org/ko/3.12/library/filecmp.html)
- [`tempfile` — Generate temporary files and directories](https://docs.python.org/ko/3.12/library/tempfile.html)
- [`glob` — Unix style pathname pattern expansion](https://docs.python.org/ko/3.12/library/glob.html)
- [`fnmatch` — Unix filename pattern matching](https://docs.python.org/ko/3.12/library/fnmatch.html)
- [`linecache` — Random access to text lines](https://docs.python.org/ko/3.12/library/linecache.html)
- [`shutil` — High-level file operations](https://docs.python.org/ko/3.12/library/shutil.html)
###  [데이터 지속성](https://docs.python.org/ko/3.12/library/persistence.html)
- [`pickle` — Python object serialization](https://docs.python.org/ko/3.12/library/pickle.html)
- [`copyreg` — Register `pickle` support functions](https://docs.python.org/ko/3.12/library/copyreg.html)
- [`shelve` — Python object persistence](https://docs.python.org/ko/3.12/library/shelve.html)
- [`marshal` — Internal Python object serialization](https://docs.python.org/ko/3.12/library/marshal.html)
- [`dbm` — Interfaces to Unix “databases”](https://docs.python.org/ko/3.12/library/dbm.html)
- [`sqlite3` — DB-API 2.0 interface for SQLite databases](https://docs.python.org/ko/3.12/library/sqlite3.html)
###  [데이터 압축 및 보관](https://docs.python.org/ko/3.12/library/archiving.html)
- [`zlib` — Compression compatible with **gzip**](https://docs.python.org/ko/3.12/library/zlib.html)
- [`gzip` — Support for **gzip** files](https://docs.python.org/ko/3.12/library/gzip.html)
- [`bz2` — Support for **bzip2** compression](https://docs.python.org/ko/3.12/library/bz2.html)
- [`lzma` — Compression using the LZMA algorithm](https://docs.python.org/ko/3.12/library/lzma.html)
- [`zipfile` — Work with ZIP archives](https://docs.python.org/ko/3.12/library/zipfile.html)
- [`tarfile` — Read and write tar archive files](https://docs.python.org/ko/3.12/library/tarfile.html)
###  [파일 형식](https://docs.python.org/ko/3.12/library/fileformats.html)
- [`csv` — CSV File Reading and Writing](https://docs.python.org/ko/3.12/library/csv.html)
- [`configparser` — Configuration file parser](https://docs.python.org/ko/3.12/library/configparser.html)
- [`tomllib` — Parse TOML files](https://docs.python.org/ko/3.12/library/tomllib.html)
- [`netrc` — netrc file processing](https://docs.python.org/ko/3.12/library/netrc.html)
- [`plistlib` — Generate and parse Apple `.plist` files](https://docs.python.org/ko/3.12/library/plistlib.html)
###  [암호화 서비스](https://docs.python.org/ko/3.12/library/crypto.html)
- [`hashlib` — Secure hashes and message digests](https://docs.python.org/ko/3.12/library/hashlib.html)
- [`hmac` — Keyed-Hashing for Message Authentication](https://docs.python.org/ko/3.12/library/hmac.html)
- [`secrets` — Generate secure random numbers for managing secrets](https://docs.python.org/ko/3.12/library/secrets.html)
###  [일반 운영 체제 서비스](https://docs.python.org/ko/3.12/library/allos.html)
- [`os` — Miscellaneous operating system interfaces](https://docs.python.org/ko/3.12/library/os.html)
- [`io` — Core tools for working with streams](https://docs.python.org/ko/3.12/library/io.html)
- [`time` — Time access and conversions](https://docs.python.org/ko/3.12/library/time.html)
- [`argparse` — Parser for command-line options, arguments and sub-commands](https://docs.python.org/ko/3.12/library/argparse.html)
- [`getopt` — C-style parser for command line options](https://docs.python.org/ko/3.12/library/getopt.html)
- [`logging` — Logging facility for Python](https://docs.python.org/ko/3.12/library/logging.html)
- [`logging.config` — Logging configuration](https://docs.python.org/ko/3.12/library/logging.config.html)
- [`logging.handlers` — Logging handlers](https://docs.python.org/ko/3.12/library/logging.handlers.html)
- [`getpass` — Portable password input](https://docs.python.org/ko/3.12/library/getpass.html)
- [`curses` — Terminal handling for character-cell displays](https://docs.python.org/ko/3.12/library/curses.html)
- [`curses.textpad` — curses 프로그램을 위한 텍스트 입력 위젯](https://docs.python.org/ko/3.12/library/curses.html#module-curses.textpad)
- [`curses.ascii` — Utilities for ASCII characters](https://docs.python.org/ko/3.12/library/curses.ascii.html)
- [`curses.panel` — A panel stack extension for curses](https://docs.python.org/ko/3.12/library/curses.panel.html)
- [`platform` — Access to underlying platform’s identifying data](https://docs.python.org/ko/3.12/library/platform.html)
- [`errno` — Standard errno system symbols](https://docs.python.org/ko/3.12/library/errno.html)
- [`ctypes` — A foreign function library for Python](https://docs.python.org/ko/3.12/library/ctypes.html)
###  [동시 실행](https://docs.python.org/ko/3.12/library/concurrency.html)
- [`threading` — Thread-based parallelism](https://docs.python.org/ko/3.12/library/threading.html)
- [`multiprocessing` — Process-based parallelism](https://docs.python.org/ko/3.12/library/multiprocessing.html)
- [`multiprocessing.shared_memory` — Shared memory for direct access across processes](https://docs.python.org/ko/3.12/library/multiprocessing.shared_memory.html)
- [The `concurrent` package](https://docs.python.org/ko/3.12/library/concurrent.html)
- [`concurrent.futures` — Launching parallel tasks](https://docs.python.org/ko/3.12/library/concurrent.futures.html)
- [`subprocess` — Subprocess management](https://docs.python.org/ko/3.12/library/subprocess.html)
- [`sched` — Event scheduler](https://docs.python.org/ko/3.12/library/sched.html)
- [`queue` — A synchronized queue class](https://docs.python.org/ko/3.12/library/queue.html)
- [`contextvars` — Context Variables](https://docs.python.org/ko/3.12/library/contextvars.html)
- [`_thread` — Low-level threading API](https://docs.python.org/ko/3.12/library/_thread.html)
###  [네트워킹과 프로세스 간 통신](https://docs.python.org/ko/3.12/library/ipc.html)
- [`asyncio` — Asynchronous I/O](https://docs.python.org/ko/3.12/library/asyncio.html)
- [`socket` — Low-level networking interface](https://docs.python.org/ko/3.12/library/socket.html)
- [`ssl` — TLS/SSL wrapper for socket objects](https://docs.python.org/ko/3.12/library/ssl.html)
- [`select` — Waiting for I/O completion](https://docs.python.org/ko/3.12/library/select.html)
- [`selectors` — High-level I/O multiplexing](https://docs.python.org/ko/3.12/library/selectors.html)
- [`signal` — Set handlers for asynchronous events](https://docs.python.org/ko/3.12/library/signal.html)
- [`mmap` — Memory-mapped file support](https://docs.python.org/ko/3.12/library/mmap.html)
###  [인터넷 데이터 처리](https://docs.python.org/ko/3.12/library/netdata.html)
- [`email` — An email and MIME handling package](https://docs.python.org/ko/3.12/library/email.html)
- [`json` — JSON encoder and decoder](https://docs.python.org/ko/3.12/library/json.html)
- [`mailbox` — Manipulate mailboxes in various formats](https://docs.python.org/ko/3.12/library/mailbox.html)
- [`mimetypes` — Map filenames to MIME types](https://docs.python.org/ko/3.12/library/mimetypes.html)
- [`base64` — Base16, Base32, Base64, Base85 Data Encodings](https://docs.python.org/ko/3.12/library/base64.html)
- [`binascii` — Convert between binary and ASCII](https://docs.python.org/ko/3.12/library/binascii.html)
- [`quopri` — Encode and decode MIME quoted-printable data](https://docs.python.org/ko/3.12/library/quopri.html)
###  [구조화된 마크업 처리 도구](https://docs.python.org/ko/3.12/library/markup.html)
- [`html` — HyperText Markup Language support](https://docs.python.org/ko/3.12/library/html.html)
- [`html.parser` — Simple HTML and XHTML parser](https://docs.python.org/ko/3.12/library/html.parser.html)
- [`html.entities` — Definitions of HTML general entities](https://docs.python.org/ko/3.12/library/html.entities.html)
- [XML 처리 모듈](https://docs.python.org/ko/3.12/library/xml.html)
- [`xml.etree.ElementTree` — The ElementTree XML API](https://docs.python.org/ko/3.12/library/xml.etree.elementtree.html)
- [`xml.dom` — The Document Object Model API](https://docs.python.org/ko/3.12/library/xml.dom.html)
- [`xml.dom.minidom` — Minimal DOM implementation](https://docs.python.org/ko/3.12/library/xml.dom.minidom.html)
- [`xml.dom.pulldom` — Support for building partial DOM trees](https://docs.python.org/ko/3.12/library/xml.dom.pulldom.html)
- [`xml.sax` — Support for SAX2 parsers](https://docs.python.org/ko/3.12/library/xml.sax.html)
- [`xml.sax.handler` — Base classes for SAX handlers](https://docs.python.org/ko/3.12/library/xml.sax.handler.html)
- [`xml.sax.saxutils` — SAX Utilities](https://docs.python.org/ko/3.12/library/xml.sax.utils.html)
- [`xml.sax.xmlreader` — Interface for XML parsers](https://docs.python.org/ko/3.12/library/xml.sax.reader.html)
- [`xml.parsers.expat` — Fast XML parsing using Expat](https://docs.python.org/ko/3.12/library/pyexpat.html)
###  [인터넷 프로토콜과 지원](https://docs.python.org/ko/3.12/library/internet.html)
- [`webbrowser` — Convenient web-browser controller](https://docs.python.org/ko/3.12/library/webbrowser.html)
- [`wsgiref` — WSGI Utilities and Reference Implementation](https://docs.python.org/ko/3.12/library/wsgiref.html)
- [`urllib` — URL handling modules](https://docs.python.org/ko/3.12/library/urllib.html)
- [`urllib.request` — Extensible library for opening URLs](https://docs.python.org/ko/3.12/library/urllib.request.html)
- [`urllib.response` — urllib가 사용하는 응답 클래스](https://docs.python.org/ko/3.12/library/urllib.request.html#module-urllib.response)
- [`urllib.parse` — Parse URLs into components](https://docs.python.org/ko/3.12/library/urllib.parse.html)
- [`urllib.error` — Exception classes raised by urllib.request](https://docs.python.org/ko/3.12/library/urllib.error.html)
- [`urllib.robotparser` — Parser for robots.txt](https://docs.python.org/ko/3.12/library/urllib.robotparser.html)
- [`http` — HTTP modules](https://docs.python.org/ko/3.12/library/http.html)
- [`http.client` — HTTP protocol client](https://docs.python.org/ko/3.12/library/http.client.html)
- [`ftplib` — FTP protocol client](https://docs.python.org/ko/3.12/library/ftplib.html)
- [`poplib` — POP3 protocol client](https://docs.python.org/ko/3.12/library/poplib.html)
- [`imaplib` — IMAP4 protocol client](https://docs.python.org/ko/3.12/library/imaplib.html)
- [`smtplib` — SMTP protocol client](https://docs.python.org/ko/3.12/library/smtplib.html)
- [`uuid` — UUID objects according to **RFC 4122**](https://docs.python.org/ko/3.12/library/uuid.html)
- [`socketserver` — A framework for network servers](https://docs.python.org/ko/3.12/library/socketserver.html)
- [`http.server` — HTTP servers](https://docs.python.org/ko/3.12/library/http.server.html)
- [`http.cookies` — HTTP state management](https://docs.python.org/ko/3.12/library/http.cookies.html)
- [`http.cookiejar` — Cookie handling for HTTP clients](https://docs.python.org/ko/3.12/library/http.cookiejar.html)
- [`xmlrpc` — XMLRPC server and client modules](https://docs.python.org/ko/3.12/library/xmlrpc.html)
- [`xmlrpc.client` — XML-RPC client access](https://docs.python.org/ko/3.12/library/xmlrpc.client.html)
- [`xmlrpc.server` — Basic XML-RPC servers](https://docs.python.org/ko/3.12/library/xmlrpc.server.html)
- [`ipaddress` — IPv4/IPv6 manipulation library](https://docs.python.org/ko/3.12/library/ipaddress.html)
###  [멀티미디어 서비스](https://docs.python.org/ko/3.12/library/mm.html)
- [`wave` — Read and write WAV files](https://docs.python.org/ko/3.12/library/wave.html)
- [`colorsys` — Conversions between color systems](https://docs.python.org/ko/3.12/library/colorsys.html)
###  [국제화](https://docs.python.org/ko/3.12/library/i18n.html)
- [`gettext` — Multilingual internationalization services](https://docs.python.org/ko/3.12/library/gettext.html)
- [`locale` — Internationalization services](https://docs.python.org/ko/3.12/library/locale.html)
###  [프로그램 프레임워크](https://docs.python.org/ko/3.12/library/frameworks.html)
- [`turtle` — 터틀 그래픽](https://docs.python.org/ko/3.12/library/turtle.html)
- [`cmd` — Support for line-oriented command interpreters](https://docs.python.org/ko/3.12/library/cmd.html)
- [`shlex` — Simple lexical analysis](https://docs.python.org/ko/3.12/library/shlex.html)
###  [Tk를 사용한 그래픽 사용자 인터페이스](https://docs.python.org/ko/3.12/library/tk.html)
- [`tkinter` — Python interface to Tcl/Tk](https://docs.python.org/ko/3.12/library/tkinter.html)
- [`tkinter.colorchooser` — Color choosing dialog](https://docs.python.org/ko/3.12/library/tkinter.colorchooser.html)
- [`tkinter.font` — Tkinter font wrapper](https://docs.python.org/ko/3.12/library/tkinter.font.html)
- [Tkinter 대화 상자](https://docs.python.org/ko/3.12/library/dialog.html)
- [`tkinter.messagebox` — Tkinter message prompts](https://docs.python.org/ko/3.12/library/tkinter.messagebox.html)
- [`tkinter.scrolledtext` — Scrolled Text Widget](https://docs.python.org/ko/3.12/library/tkinter.scrolledtext.html)
- [`tkinter.dnd` — Drag and drop support](https://docs.python.org/ko/3.12/library/tkinter.dnd.html)
- [`tkinter.ttk` — Tk themed widgets](https://docs.python.org/ko/3.12/library/tkinter.ttk.html)
- [`tkinter.tix` — Extension widgets for Tk](https://docs.python.org/ko/3.12/library/tkinter.tix.html)
- [IDLE](https://docs.python.org/ko/3.12/library/idle.html)
###  [개발 도구](https://docs.python.org/ko/3.12/library/development.html)
- [`typing` — 형 힌트 지원](https://docs.python.org/ko/3.12/library/typing.html)
- [`pydoc` — Documentation generator and online help system](https://docs.python.org/ko/3.12/library/pydoc.html)
- [파이썬 개발 모드](https://docs.python.org/ko/3.12/library/devmode.html)
- [`doctest` — Test interactive Python examples](https://docs.python.org/ko/3.12/library/doctest.html)
- [`unittest` — Unit testing framework](https://docs.python.org/ko/3.12/library/unittest.html)
- [`unittest.mock` — mock object library](https://docs.python.org/ko/3.12/library/unittest.mock.html)
- [`unittest.mock` — getting started](https://docs.python.org/ko/3.12/library/unittest.mock-examples.html)
- [2to3 — Automated Python 2 to 3 code translation](https://docs.python.org/ko/3.12/library/2to3.html)
- [`test` — Regression tests package for Python](https://docs.python.org/ko/3.12/library/test.html)
- [`test.support` — 파이썬 테스트 스위트용 유틸리티](https://docs.python.org/ko/3.12/library/test.html#module-test.support)
- [`test.support.socket_helper` — 소켓 테스트용 유틸리티](https://docs.python.org/ko/3.12/library/test.html#module-test.support.socket_helper)
- [`test.support.script_helper` — 파이썬 실행 테스트용 유틸리티](https://docs.python.org/ko/3.12/library/test.html#module-test.support.script_helper)
- [`test.support.bytecode_helper` — 올바른 바이트 코드 생성 테스트를 위한 지원 도구](https://docs.python.org/ko/3.12/library/test.html#module-test.support.bytecode_helper)
- [`test.support.threading_helper` — Utilities for threading tests](https://docs.python.org/ko/3.12/library/test.html#module-test.support.threading_helper)
- [`test.support.os_helper` — Utilities for os tests](https://docs.python.org/ko/3.12/library/test.html#module-test.support.os_helper)
- [`test.support.import_helper` — Utilities for import tests](https://docs.python.org/ko/3.12/library/test.html#module-test.support.import_helper)
- [`test.support.warnings_helper` — Utilities for warnings tests](https://docs.python.org/ko/3.12/library/test.html#module-test.support.warnings_helper)
###  [디버깅과 프로파일링](https://docs.python.org/ko/3.12/library/debug.html)
- [감사 이벤트 표](https://docs.python.org/ko/3.12/library/audit_events.html)
- [`bdb` — Debugger framework](https://docs.python.org/ko/3.12/library/bdb.html)
- [`faulthandler` — Dump the Python traceback](https://docs.python.org/ko/3.12/library/faulthandler.html)
- [`pdb` — 파이썬 디버거](https://docs.python.org/ko/3.12/library/pdb.html)
- [파이썬 프로파일러](https://docs.python.org/ko/3.12/library/profile.html)
- [`timeit` — Measure execution time of small code snippets](https://docs.python.org/ko/3.12/library/timeit.html)
- [`trace` — Trace or track Python statement execution](https://docs.python.org/ko/3.12/library/trace.html)
- [`tracemalloc` — Trace memory allocations](https://docs.python.org/ko/3.12/library/tracemalloc.html)
###  [소프트웨어 패키징 및 배포](https://docs.python.org/ko/3.12/library/distribution.html)
- [`ensurepip` — Bootstrapping the `pip` installer](https://docs.python.org/ko/3.12/library/ensurepip.html)
- [`venv` — Creation of virtual environments](https://docs.python.org/ko/3.12/library/venv.html)
- [`zipapp` — Manage executable Python zip archives](https://docs.python.org/ko/3.12/library/zipapp.html)
### [파이썬 실행시간 서비스](https://docs.python.org/ko/3.12/library/python.html)
- [`sys` — System-specific parameters and functions](https://docs.python.org/ko/3.12/library/sys.html)
- [`sys.monitoring` — Execution event monitoring](https://docs.python.org/ko/3.12/library/sys.monitoring.html)
- [`sysconfig` — Provide access to Python’s configuration information](https://docs.python.org/ko/3.12/library/sysconfig.html)
- [`builtins` — Built-in objects](https://docs.python.org/ko/3.12/library/builtins.html)
- [`__main__` — Top-level code environment](https://docs.python.org/ko/3.12/library/__main__.html)
- [`warnings` — Warning control](https://docs.python.org/ko/3.12/library/warnings.html)
- [`dataclasses` — Data Classes](https://docs.python.org/ko/3.12/library/dataclasses.html)
- [`contextlib` — `with` 문 컨텍스트를 위한 유틸리티](https://docs.python.org/ko/3.12/library/contextlib.html)
- [`abc` — Abstract Base Classes](https://docs.python.org/ko/3.12/library/abc.html)
- [`atexit` — Exit handlers](https://docs.python.org/ko/3.12/library/atexit.html)
- [`traceback` — Print or retrieve a stack traceback](https://docs.python.org/ko/3.12/library/traceback.html)
- [`__future__` — Future statement definitions](https://docs.python.org/ko/3.12/library/__future__.html)
- [`gc` — Garbage Collector interface](https://docs.python.org/ko/3.12/library/gc.html)
- [`inspect` — Inspect live objects](https://docs.python.org/ko/3.12/library/inspect.html)
- [`site` — Site-specific configuration hook](https://docs.python.org/ko/3.12/library/site.html)
### [사용자 정의 파이썬 인터프리터](https://docs.python.org/ko/3.12/library/custominterp.html)
- [`code` — Interpreter base classes](https://docs.python.org/ko/3.12/library/code.html)
- [`codeop` — Compile Python code](https://docs.python.org/ko/3.12/library/codeop.html)
### [모듈 임포트 하기](https://docs.python.org/ko/3.12/library/modules.html)
- [`zipimport` — Import modules from Zip archives](https://docs.python.org/ko/3.12/library/zipimport.html)
- [`pkgutil` — Package extension utility](https://docs.python.org/ko/3.12/library/pkgutil.html)
- [`modulefinder` — Find modules used by a script](https://docs.python.org/ko/3.12/library/modulefinder.html)
- [`runpy` — Locating and executing Python modules](https://docs.python.org/ko/3.12/library/runpy.html)
- [`importlib` — `import`의 구현](https://docs.python.org/ko/3.12/library/importlib.html)
- [`importlib.resources` – Package resource reading, opening and access](https://docs.python.org/ko/3.12/library/importlib.resources.html)
- [`importlib.resources.abc` – Abstract base classes for resources](https://docs.python.org/ko/3.12/library/importlib.resources.abc.html)
- [`importlib.metadata` – Accessing package metadata](https://docs.python.org/ko/3.12/library/importlib.metadata.html)
- [The initialization of the `sys.path` module search path](https://docs.python.org/ko/3.12/library/sys_path_init.html)
### [파이썬 언어 서비스](https://docs.python.org/ko/3.12/library/language.html)
- [`ast` — Abstract Syntax Trees](https://docs.python.org/ko/3.12/library/ast.html)
- [`symtable` — Access to the compiler’s symbol tables](https://docs.python.org/ko/3.12/library/symtable.html)
- [`token` — Constants used with Python parse trees](https://docs.python.org/ko/3.12/library/token.html)
- [`keyword` — Testing for Python keywords](https://docs.python.org/ko/3.12/library/keyword.html)
- [`tokenize` — Tokenizer for Python source](https://docs.python.org/ko/3.12/library/tokenize.html)
- [`tabnanny` — Detection of ambiguous indentation](https://docs.python.org/ko/3.12/library/tabnanny.html)
- [`pyclbr` — Python module browser support](https://docs.python.org/ko/3.12/library/pyclbr.html)
- [`py_compile` — Compile Python source files](https://docs.python.org/ko/3.12/library/py_compile.html)
- [`compileall` — Byte-compile Python libraries](https://docs.python.org/ko/3.12/library/compileall.html)
- [`dis` — Disassembler for Python bytecode](https://docs.python.org/ko/3.12/library/dis.html)
- [`pickletools` — Tools for pickle developers](https://docs.python.org/ko/3.12/library/pickletools.html)
### [MS 윈도우 특정 서비스](https://docs.python.org/ko/3.12/library/windows.html)
- [`msvcrt` — Useful routines from the MS VC++ runtime](https://docs.python.org/ko/3.12/library/msvcrt.html)
- [`winreg` — Windows registry access](https://docs.python.org/ko/3.12/library/winreg.html)
- [`winsound` — Sound-playing interface for Windows](https://docs.python.org/ko/3.12/library/winsound.html)
### [유닉스 특정 서비스](https://docs.python.org/ko/3.12/library/unix.html)
- [`posix` — The most common POSIX system calls](https://docs.python.org/ko/3.12/library/posix.html)
- [`pwd` — The password database](https://docs.python.org/ko/3.12/library/pwd.html)
- [`grp` — The group database](https://docs.python.org/ko/3.12/library/grp.html)
- [`termios` — POSIX style tty control](https://docs.python.org/ko/3.12/library/termios.html)
- [`tty` — Terminal control functions](https://docs.python.org/ko/3.12/library/tty.html)
- [`pty` — Pseudo-terminal utilities](https://docs.python.org/ko/3.12/library/pty.html)
- [`fcntl` — The `fcntl` and `ioctl` system calls](https://docs.python.org/ko/3.12/library/fcntl.html)
- [`resource` — Resource usage information](https://docs.python.org/ko/3.12/library/resource.html)
- [`syslog` — Unix syslog library routines](https://docs.python.org/ko/3.12/library/syslog.html)
###  [Modules command-line interface (CLI)](https://docs.python.org/ko/3.12/library/cmdline.html)
### [대체된 모듈](https://docs.python.org/ko/3.12/library/superseded.html)
- [`aifc` — AIFF와 AIFC 파일 읽고 쓰기](https://docs.python.org/ko/3.12/library/aifc.html)
- [`audioop` — Manipulate raw audio data](https://docs.python.org/ko/3.12/library/audioop.html)
- [`cgi` — Common Gateway Interface support](https://docs.python.org/ko/3.12/library/cgi.html)
- [`cgitb` — CGI 스크립트를 위한 트레이스백 관리자](https://docs.python.org/ko/3.12/library/cgitb.html)
- [`chunk` — IFF 청크된 데이터 읽기](https://docs.python.org/ko/3.12/library/chunk.html)
- [`crypt` — 유닉스 비밀번호 확인 함수](https://docs.python.org/ko/3.12/library/crypt.html)
- [`imghdr` — 이미지 유형 판단](https://docs.python.org/ko/3.12/library/imghdr.html)
- [`mailcap` — Mailcap 파일 처리](https://docs.python.org/ko/3.12/library/mailcap.html)
- [`msilib` — Read and write Microsoft Installer files](https://docs.python.org/ko/3.12/library/msilib.html)
- [`nis` — Sun의 NIS(옐로 페이지)에 대한 인터페이스](https://docs.python.org/ko/3.12/library/nis.html)
- [`nntplib` — NNTP 프로토콜 클라이언트](https://docs.python.org/ko/3.12/library/nntplib.html)
- [`optparse` — Parser for command line options](https://docs.python.org/ko/3.12/library/optparse.html)
- [`ossaudiodev` — Access to OSS-compatible audio devices](https://docs.python.org/ko/3.12/library/ossaudiodev.html)
- [`pipes` — 셸 파이프라인에 대한 인터페이스](https://docs.python.org/ko/3.12/library/pipes.html)
- [`sndhdr` — 음향 파일 유형 판단](https://docs.python.org/ko/3.12/library/sndhdr.html)
- [`spwd` — 섀도 암호 데이터베이스](https://docs.python.org/ko/3.12/library/spwd.html)
- [`sunau` — Sun AU 파일 읽고 쓰기](https://docs.python.org/ko/3.12/library/sunau.html)
- [`telnetlib` — 텔넷 클라이언트](https://docs.python.org/ko/3.12/library/telnetlib.html)
- [`uu` — uuencode 파일 인코딩과 디코딩](https://docs.python.org/ko/3.12/library/uu.html)
- [`xdrlib` — XDR 데이터 인코딩과 디코딩](https://docs.python.org/ko/3.12/library/xdrlib.html)
### 보안
The following modules have specific security considerations:
- [`base64`](https://docs.python.org/ko/3.12/library/base64.html#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85"): [base64 security considerations](https://docs.python.org/ko/3.12/library/base64.html#base64-security) in [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)
- [`cgi`](https://docs.python.org/ko/3.12/library/cgi.html#module-cgi "cgi: Helpers for running Python scripts via the Common Gateway Interface. (폐지됨)"): [CGI security considerations](https://docs.python.org/ko/3.12/library/cgi.html#cgi-security)
- [`hashlib`](https://docs.python.org/ko/3.12/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms."): [all constructors take a “usedforsecurity” keyword-only argument disabling known insecure and blocked algorithms](https://docs.python.org/ko/3.12/library/hashlib.html#hashlib-usedforsecurity)
- [`http.server`](https://docs.python.org/ko/3.12/library/http.server.html#module-http.server "http.server: HTTP server and request handlers.") is not suitable for production use, only implementing basic security checks. See the [security considerations](https://docs.python.org/ko/3.12/library/http.server.html#http-server-security).
- [`logging`](https://docs.python.org/ko/3.12/library/logging.html#module-logging "logging: Flexible event logging system for applications."): [Logging configuration uses eval()](https://docs.python.org/ko/3.12/library/logging.config.html#logging-eval-security)
- [`multiprocessing`](https://docs.python.org/ko/3.12/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism."): [Connection.recv() uses pickle](https://docs.python.org/ko/3.12/library/multiprocessing.html#multiprocessing-recv-pickle-security)
- [`pickle`](https://docs.python.org/ko/3.12/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back."): [Restricting globals in pickle](https://docs.python.org/ko/3.12/library/pickle.html#pickle-restrict)
- [`random`](https://docs.python.org/ko/3.12/library/random.html#module-random "random: Generate pseudo-random numbers with various common distributions.") shouldn’t be used for security purposes, use [`secrets`](https://docs.python.org/ko/3.12/library/secrets.html#module-secrets "secrets: Generate secure random numbers for managing secrets.") instead
- [`shelve`](https://docs.python.org/ko/3.12/library/shelve.html#module-shelve "shelve: Python object persistence."): [shelve is based on pickle and thus unsuitable for dealing with untrusted sources](https://docs.python.org/ko/3.12/library/shelve.html#shelve-security)
- [`ssl`](https://docs.python.org/ko/3.12/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects"): [SSL/TLS security considerations](https://docs.python.org/ko/3.12/library/ssl.html#ssl-security)
- [`subprocess`](https://docs.python.org/ko/3.12/library/subprocess.html#module-subprocess "subprocess: Subprocess management."): [Subprocess security considerations](https://docs.python.org/ko/3.12/library/subprocess.html#subprocess-security)
- [`tempfile`](https://docs.python.org/ko/3.12/library/tempfile.html#module-tempfile "tempfile: Generate temporary files and directories."): [mktemp is deprecated due to vulnerability to race conditions](https://docs.python.org/ko/3.12/library/tempfile.html#tempfile-mktemp-deprecated)
- [`xml`](https://docs.python.org/ko/3.12/library/xml.html#module-xml "xml: Package containing XML processing modules"): [XML vulnerabilities](https://docs.python.org/ko/3.12/library/xml.html#xml-vulnerabilities)
- [`zipfile`](https://docs.python.org/ko/3.12/library/zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files."): [maliciously prepared .zip files can cause disk volume exhaustion](https://docs.python.org/ko/3.12/library/zipfile.html#zipfile-resources-limitations)

The [`-I`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-I) command line option can be used to run Python in isolated mode. When it cannot be used, the [`-P`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-P) option or the [`PYTHONSAFEPATH`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONSAFEPATH) environment variable can be used to not prepend a potentially unsafe path to [`sys.path`](https://docs.python.org/ko/3.12/library/sys.html#sys.path "sys.path") such as the current directory, the script’s directory or an empty string.
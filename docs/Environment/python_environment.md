---
title: "[Python] 환경 (Environment)"
excerpt: 가상 환경은 특정 버전 파이썬 설치와 여러 추가 패키지를 포함하는 완비된 디렉터리 트리입니다. 서로 다른 응용 프로그램은 서로 다른 가상 환경을 사용할 수 있습니다. 상충하는 요구 사항의 예를 해결하기 위해, 응용 프로그램 A에는 버전 1.0이 설치된 자체 가상 환경이 있고, 응용 프로그램 B에는 버전 2.0이 있는 다른 가상 환경이 있을 수 있습니다.
categories:
  - Python
tags:
  - Python
  - Virtual-Environment
  - Environment-Variable
last_modified_at: 2024-04-11T15:10:55+09:00
link: 
상위 항목: "[[python_home|파이썬 (Python)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

---

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

## 환경 변수
### 명령 줄 (Command line)
- CPython 인터프리터는 명령 줄과 환경에서 다양한 설정을 찾습니다.
> **CPython 구현 상세:** 다른 구현의 명령 줄 체계는 다를 수 있습니다. 자세한 내용은 [대안 구현들](https://docs.python.org/ko/3.12/reference/introduction.html#implementations) 참조하십시오.

- 파이썬을 호출할 때 다음 옵션들을 지정할 수 있습니다:

```shell
python [-bBdEhiIOPqRsSuvVWx?] [-c command | -m module-name | script | - ] [args]
```

- 물론, 가장 일반적인 사용 사례는 간단한 스크립트 호출입니다:

```shell
python myscript.py
```

#### 인터페이스 옵션
- 인터프리터 인터페이스는 유닉스 셸의 인터페이스와 비슷하지만, 몇 가지 추가 호출 방법을 제공합니다:
  
  - tty 장치에 연결된 표준 입력으로 호출하면, 명령을 입력하라는 프롬프트를 준 후 EOF(파일 끝 문자, 유닉스에서는 Ctrl-D, 윈도우에서는 Ctrl-Z, Enter로 만들 수 있습니다)가 읽힐 때까지 실행합니다.
  - 파일 이름 인자나 파일을 표준 입력으로 사용해서 호출하면, 해당 파일에서 스크립트를 읽고 실행합니다.
  - 디렉터리 이름 인자로 호출되면, 해당 디렉터리에서 적절히 이름 붙은 스크립트를 읽고 실행합니다.
  - `-c command` 로 호출되면, _command_ 로 주어지는 파이썬 문장을 실행합니다. 여기서 _command_ 는 개행 문자로 구분된 여러 개의 문장을 포함할 수 있습니다. 선행 공백은 파이썬 문장에서 중요합니다!
  - `-m module-name` 으로 호출되면, 주어진 모듈을 파이썬 모듈 경로에서 찾은 후에 스크립트로 실행합니다.

- 비대화형 모드에서는, 실행하기 전에 전체 입력을 구문 분석합니다.
- 인터페이스 옵션은 인터프리터에 의해 소비되는 옵션의 목록을 종료합니다, 뒤따르는 모든 인자는 [`sys.argv`](https://docs.python.org/ko/3.12/library/sys.html#sys.argv "sys.argv") 로 들어갑니다 – 첫 번째 요소, 서브 스크립트 0(`sys.argv[0]`)은 프로그램 소스를 반영하는 문자열임에 유의하세요.

`-c <command>`

- _command_ 의 파이썬 코드를 실행합니다. _command_ 는 개행 문자로 구분된 하나 이상의 문장일 수 있는데, 일반 모듈 코드에서와 같이 선행 공백은 의미가 있습니다.
- 이 옵션을 주면, [`sys.argv`](https://docs.python.org/ko/3.12/library/sys.html#sys.argv "sys.argv") 의 첫 번째 요소는 `"-c"` 가 되고, 현재 디렉터리를 [`sys.path`](https://docs.python.org/ko/3.12/library/sys.html#sys.path "sys.path") 의 시작 부분에 추가합니다 (그 디렉터리에 있는 모듈을 최상위 모듈로 임포트 할 수 있게 합니다).
- `command`를 인자로 [감사 이벤트(auditing event)](https://docs.python.org/ko/3.12/library/sys.html#auditing) `cpython.run_command`를 발생시킵니다.

`-m <module-name>`

- 제공된 이름의 모듈을 [`sys.path`](https://docs.python.org/ko/3.12/library/sys.html#sys.path "sys.path") 에서 검색하고 그 내용을 [`__main__`](https://docs.python.org/ko/3.12/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.") 모듈로서 실행합니다.
- 인자가 _모듈_ 이름이기 때문에, 파일 확장자(`.py`)를 주지 않아야 합니다. 모듈 이름은 유효한 절대 파이썬 모듈 이름이어야 하지만, 구현이 항상 이를 강제하는 것은 아닙니다 (예를 들어, 하이픈을 포함하는 이름을 허락할 수도 있습니다).
- 패키지 이름(이름 공간 패키지 포함)도 허용됩니다. 일반 모듈 대신 패키지 이름이 제공되면, 인터프리터는 `<pkg>.__main__` 을 메인 모듈로 실행합니다. 이 동작은 인터프리터에 스크립트 인자로 전달되는 디렉터리 및 zip 파일의 처리와 의도적으로 유사합니다.

> 이 옵션은 내장 모듈이나 확장 모듈에는 사용될 수 없는데, 이것들은 파이썬 모듈 파일을 갖고 있지 않기 때문입니다. 그러나, 원래 소스 파일이 없는 사전 컴파일된 모듈에는 여전히 사용할 수 있습니다.

- 이 옵션을 주면, [`sys.argv`](https://docs.python.org/ko/3.12/library/sys.html#sys.argv "sys.argv") 의 첫 번째 요소는 모듈 파일의 전체 경로가 됩니다 (모듈 파일을 찾는 동안에는 첫 번째 요소를 `"-m"` 으로 설정합니다). [`-c`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-c) 옵션과 마찬가지로, 현재 디렉터리가 [`sys.path`](https://docs.python.org/ko/3.12/library/sys.html#sys.path "sys.path") 의 시작 부분에 추가됩니다.
- [`-I`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-I) 옵션을 사용하면 [`sys.path`](https://docs.python.org/ko/3.12/library/sys.html#sys.path "sys.path")에 현재 디렉토리나 사용자의 사이트-패키지 디렉터리가 없는 격리 모드에서 스크립트를 실행할 수 있습니다. 모든 `PYTHON*` 환경 변수도 무시됩니다.
- 많은 표준 라이브러리 모듈에는 스크립트로 실행할 때 호출되는 코드가 들어 있습니다. 한 예는 [`timeit`](https://docs.python.org/ko/3.12/library/timeit.html#module-timeit "timeit: Measure the execution time of small code snippets.") 모듈입니다:

```python
python -m timeit -s "setup here" "benchmarked code here"
python -m timeit -h # for details
```

- `module-name`을 인자로 [감사 이벤트(auditing event)](https://docs.python.org/ko/3.12/library/sys.html#auditing) `cpython.run_module`을 발생시킵니다.

> [`runpy.run_module()`](https://docs.python.org/ko/3.12/library/runpy.html#runpy.run_module "runpy.run_module")
> - 파이썬 코드에서 직접 사용할 수 있는 동등한 기능
> 
> [**PEP 338**](https://peps.python.org/pep-0338/) – 모듈을 스크립트로 실행하기

> 버전 3.1에서 변경: `__main__` 서브 모듈을 실행할 패키지 이름을 제공할 수 있습니다.
> 버전 3.4에서 변경: 이름 공간 패키지도 지원됩니다.

`-`
- 표준 입력([`sys.stdin`](https://docs.python.org/ko/3.12/library/sys.html#sys.stdin "sys.stdin"))에서 명령을 읽습니다. 표준 입력이 터미널이면, [`-i`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-i) 가 묵시적으로 적용됩니다.
- 이 옵션을 주면, [`sys.argv`](https://docs.python.org/ko/3.12/library/sys.html#sys.argv "sys.argv") 의 첫 번째 요소는 `"-"` 이 되고, 현재 디렉터리가 [`sys.path`](https://docs.python.org/ko/3.12/library/sys.html#sys.path "sys.path") 의 처음에 추가됩니다.
- 인자 없이 [감사 이벤트(auditing event)](https://docs.python.org/ko/3.12/library/sys.html#auditing) `cpython.run_stdin`을 발생시킵니다.

`<script>`
- _script_ 에 담긴 파이썬 코드를 실행합니다. _script_ 는 파이썬 파일이나 `__main__.py` 파일이 들어있는 디렉터리나 `__main__.py` 파일을 포함하는 zip 파일을 가리키는 파일 시스템 경로(절대나 상대)여야 합니다.
- 이 옵션을 주면, [`sys.argv`](https://docs.python.org/ko/3.12/library/sys.html#sys.argv "sys.argv") 의 첫 번째 요소는 명령 줄에서 주어진 스크립트 이름이 됩니다.
- 스크립트 이름이 파이썬 파일을 직접 가리키면, 해당 파일을 포함하는 디렉터리가 [`sys.path`](https://docs.python.org/ko/3.12/library/sys.html#sys.path "sys.path") 의 시작 부분에 추가되고, 파일은 [`__main__`](https://docs.python.org/ko/3.12/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.") 모듈로 실행됩니다.
- 스크립트 이름이 디렉터리 나 zip 파일을 가리키면, 스크립트 이름이 [`sys.path`](https://docs.python.org/ko/3.12/library/sys.html#sys.path "sys.path") 의 시작 부분에 추가되고, 해당 위치의 `__main__.py` 파일을 [`__main__`](https://docs.python.org/ko/3.12/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.") 모듈로 실행합니다.
- [`-I`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-I) 옵션을 사용하면 스크립트의 디렉토리나 사용자의 사이트-패키지 디렉토리를 포함하지 않는 [`sys.path`](https://docs.python.org/ko/3.12/library/sys.html#sys.path "sys.path")에서 스크립트를 격리 모드로 실행할 수 있습니다. 모든 `PYTHON*` 환경 변수도 무시됩니다.
- `filename`을 인자로 [감사 이벤트(auditing event)](https://docs.python.org/ko/3.12/library/sys.html#auditing) `cpython.run_file`을 발생시킵니다.

> [`runpy.run_path()`](https://docs.python.org/ko/3.12/library/runpy.html#runpy.run_path "runpy.run_path")
> - 파이썬 코드에서 직접 사용할 수 있는 동등한 기능

- 인터페이스 옵션을 주지 않으면, [`-i`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-i) 가 묵시적으로 적용되고, `sys.argv[0]` 는 빈 문자열(`""`)이 되고, 현재 디렉터리가 [`sys.path`](https://docs.python.org/ko/3.12/library/sys.html#sys.path "sys.path") 의 처음에 추가됩니다. 또한, 플랫폼에서 사용 가능한 경우 ([Readline 구성](https://docs.python.org/ko/3.12/library/site.html#rlcompleter-config) 를 참조하세요), 탭 완성 및 히스토리 편집이 자동으로 활성화됩니다.


> [인터프리터 실행하기](https://docs.python.org/ko/3.12/tutorial/interpreter.html#tut-invoking)

> 버전 3.4에서 변경: 탭 완성과 히스토리 편집의 자동 활성화.

### 일반 옵션

`-?` `-h` `--help`

- 모든 명령줄 옵션과 해당 환경 변수에 대한 간단한 설명을 인쇄하고 종료합니다.

`--help-env` (3.11 추가)

- 파이썬 관련 환경 변수에 대한 간단한 설명을 출력하고 종료합니다.

`--help-xoptions` (3.11 추가)

- 구현별 [`-X`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-X) 옵션에 대한 설명을 인쇄하고 종료합니다.

`--help-all` (3.11 추가)

- 전체 사용 정보를 인쇄하고 종료합니다.

`-V` `--version`

- 파이썬 버전 번호를 출력하고 종료합니다. 출력 예는 다음과 같습니다:

```
Python 3.8.0b2+
```

- 두 번 지정하면, 다음과 같이 빌드에 관한 추가 정보를 인쇄합니다:

```
Python 3.8.0b2+ (3.8:0c076caaa8, Apr 20 2019, 21:55:00)
[GCC 6.2.0 20161005]
```

> Added in version 3.6: `-VV` 옵션.

### 기타 옵션

`-b`

- 인코딩을 지정하지 않고 [`바이트`](https://docs.python.org/ko/3.12/library/stdtypes.html#bytes "바이트") 또는 [`바이트어레이`](https://docs.python.org/ko/3.12/library/stdtypes.html#bytearray "바이트어레이")를 [`str`](https://docs.python.org/ko/3.12/library/stdtypes.html#str "스트링")으로 변환하거나 `바이트` 또는 `바이트어레이`를 [`str`]과 비교하거나 [`int`](https://docs.python.org/ko/3.12/library/functions.html#int "int")와 비교하면 경고를 발행합니다. 옵션이 두 번(`-bb`) 지정되면 오류를 발생시킵니다.

> 버전 3.5에서 변경: [`byte`](https://docs.python.org/ko/3.12/library/stdtypes.html#bytes "바이트")와 [`int`](https://docs.python.org/ko/3.12/library/functions.html#int "인트")의 비교에도 영향을 줍니다.

`-B`

- 주어지면, 파이썬은 소스 모듈을 임포트 할 때 `.pyc` 파일을 쓰려고 하지 않습니다. [`PYTHONDONTWRITEBYTECODE`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE) 도 참조하십시오.

`--check-hash-based-pycs default|always|never`
- 해시 기반 `.pyc` 파일의 검증 동작을 제어합니다. [캐시된 바이트 코드 무효화](https://docs.python.org/ko/3.12/reference/import.html#pyc-invalidation)를 참조하세요. `default` 로 설정하면, 검사형과 비검사형 해시 기반 바이트 코드 캐시 파일은 기본 의미에 따라 유효성이 검사됩니다. `always` 로 설정하면, 모든 해시 기반 `.pyc` 파일들은, 검사형과 비검사형을 가리지 않고, 해당 소스 파일에 대해 유효성이 검사됩니다. `never` 로 설정되면, 해시 기반 `.pyc` 파일은 해당 소스 파일에 대해 유효성이 검사되지 않습니다.
- 타임스탬프 기반 `.pyc` 파일의 의미는 이 옵션의 영향을 받지 않습니다.

`-d`

- 구문 분석기 디버깅 출력을 켭니다(전문가 전용). '`PYTHONDEBUG`'(https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONDEBUG) 환경 변수를 참조하세요.
- 이 옵션을 사용하려면 [파이썬 디버그 빌드](https://docs.python.org/ko/3.12/using/configure.html#debug-build)가 필요하며, 그렇지 않으면 무시됩니다.

`-E`

- 설정되어 있을 수 있는 모든 `PYTHON*` 환경 변수(예: [`PYTHONPATH`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONPATH) 및 [`PYTHONHOME`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONHOME)를 무시합니다.
- 또한 [`-P`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-P) 및 [`-I`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-I) (격리) 옵션을 참조하십시오.

`-i`

- 스크립트가 첫 번째 인자로 전달되거나 [`-c`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-c) 옵션이 사용되면, [`sys.stdin`](https://docs.python.org/ko/3.12/library/sys.html#sys.stdin "sys.stdin") 가 터미널로 보이지 않을 때도, 스크립트나 명령을 실행한 후에 대화형 모드에 진입합니다. [`PYTHONSTARTUP`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONSTARTUP) 파일은 읽지 않습니다.
- 이것은 스크립트가 예외를 발생시킬 때 전역 변수나 스택 트레이스를 검사하는 데 유용할 수 있습니다. [`PYTHONINSPECT`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONINSPECT) 도 참조하십시오.

`-I` (3.4 추가)

- 격리 모드에서 파이썬을 실행합니다. 여기에는 [`-E`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-E), [`-P`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-P) 및 [`-s`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-s) 옵션도 포함됩니다.
- 격리 모드에서 [`sys.path`](https://docs.python.org/ko/3.12/library/sys.html#sys.path "sys.path")에는 스크립트의 디렉토리나 사용자의 사이트-패키지 디렉토리가 포함되지 않습니다. 모든 `PYTHON*` 환경 변수도 무시됩니다. 사용자가 악성 코드를 삽입하지 못하도록 추가 제한이 적용될 수 있습니다.

`-O`
- `assert` 문과 [`__debug__`](https://docs.python.org/ko/3.12/library/constants.html#debug__ "__debug__") 의 값에 대한 조건부 코드를 제거합니다. `.pyc` 확장자 앞에 `.opt-1` 을 추가하여 컴파일된 ([바이트 코드](https://docs.python.org/ko/3.12/glossary.html#term-bytecode)) 파일의 이름을 구분합니다 ([**PEP 488**](https://peps.python.org/pep-0488/)을 참조하세요). [`PYTHONOPTIMIZE`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONOPTIMIZE) 도 참조하십시오.

> 버전 3.5에서 변경: [**PEP 488**](https://peps.python.org/pep-0488/) 에 따라 `.pyc` 파일명을 수정합니다.

`-OO`
- [`-O`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-O)를 적용하고 독스트링도 버립니다. `.pyc` 확장자 앞에 `.opt-2` 를 추가하여 컴파일 된([바이트 코드](https://docs.python.org/ko/3.12/glossary.html#term-bytecode)) 파일의 이름을 구분합니다 (참조 [**PEP 488**](https://peps.python.org/pep-0488/)을 참조하세요).

> 버전 3.5에서 변경: [**PEP 488**](https://peps.python.org/pep-0488/) 에 따라 `.pyc` 파일명을 수정합니다.

`-P` (3.11 추가)

- 안전하지 않을 수 있는 경로를 [`sys.path`](https://docs.python.org/ko/3.12/library/sys.html#sys.path "sys.path")에 앞에 붙이지 마세요:
  
  - `python -m module` 명령줄: 현재 작업 디렉터리를 앞에 붙이지 마세요.
  - `python script.py` 명령줄: 스크립트의 디렉터리를 앞에 붙이지 마세요. 심볼릭 링크인 경우 심볼릭 링크를 확인합니다.
  - `python -c code` 및 `python`(REPL) 명령줄: 현재 작업 디렉터리를 의미하는 빈 문자열을 앞에 붙이지 마세요.
    
- 또한 [`PYTHONSAFEPATH`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONSAFEPATH) 환경 변수와 [`-E`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-E) 및 [`-I`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-I)(격리) 옵션을 참조하세요.


`-q` (3.2 추가)
- 대화형 모드에서도 저작권과 버전 메시지를 표시하지 않습니다.

`-R` (3.2.3 추가)

- 해시 무작위화를 켭니다. 이 옵션은 [`PYTHONHASHSEED`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONHASHSEED) 환경 변수가 `0` 으로 설정된 경우에만 효과가 있습니다, 해시 무작위화는 기본적으로 활성화되기 때문입니다.
- 이전 버전의 파이썬에서 이 옵션은 해시 무작위화를 켜서 문자열 및 바이트열 객체의 [`__hash__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__hash__ "object.__hash__") 값을 예측할 수 없는 임의의 값으로 "소금에 절이도록" 합니다. 개별 파이썬 프로세스 내에서는 일정하게 유지되지만, 반복되는 파이썬 호출 간에는 예측할 수 없습니다. 해시 무작위화는 딕셔너리 구조의 최악의 성능인 $O(n^2)$ 복잡성을 악용하는 신중하게 선택한 입력으로 인한 서비스 거부에 대한 보호 기능을 제공하기 위해 고안되었습니다. 자세한 내용은 [http://ocert.org/advisories/ocert-2011-003.html](http://ocert.org/advisories/ocert-2011-003.html)를 참조하세요.
- [`PYTHONHASHSEED`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONHASHSEED) 는 해시 시드 시크릿에 고정값을 설정할 수 있게 합니다.

> 버전 3.7에서 변경: 이 옵션은 더는 무시되지 않습니다.

`-s`
- [`사용자 site-packages 디렉터리`](https://docs.python.org/ko/3.12/library/site.html#site.USER_SITE "site.USER_SITE") 를 [`sys.path`](https://docs.python.org/ko/3.12/library/sys.html#sys.path "sys.path") 에 추가하지 않습니다.
- See also [`PYTHONNOUSERSITE`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONNOUSERSITE).

> [**PEP 370**](https://peps.python.org/pep-0370/) – 사용자별 site-packages 디렉터리

`-S`
- [`site`](https://docs.python.org/ko/3.12/library/site.html#module-site "site: Module responsible for site-specific configuration.") 모듈의 임포트와 이 모듈이 수반하는 [`sys.path`](https://docs.python.org/ko/3.12/library/sys.html#sys.path "sys.path") 의 사이트 의존적 조작을 비활성화합니다. 또한 [`site`](https://docs.python.org/ko/3.12/library/site.html#module-site "site: Module responsible for site-specific configuration.") 가 나중에 명시적으로 임포트될 때도 이 조작을 비활성화합니다 (조작하기를 원하면 [`site.main()`](https://docs.python.org/ko/3.12/library/site.html#site.main "site.main") 을 호출하십시오).

`-u`
- `stdout` 과 `stderr` 스트림을 버퍼링하지 않도록 만듭니다. 이 옵션은 stdin 스트림에는 영향을 미치지 않습니다.
- [`PYTHONUNBUFFERED`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONUNBUFFERED) 도 참조하세요.

> 버전 3.7에서 변경: stdout 과 stderr 스트림의 텍스트 계층은 이제 버퍼링 되지 않습니다.

`-v`

- 모듈이 초기화될 때마다 모듈이 로드된 위치(파일 이름 또는 내장 모듈)를 보여주는 메시지를 인쇄합니다. 두 번(`-vv`) 지정하면 모듈을 검색할 때 확인된 각 파일에 대한 메시지를 인쇄합니다. 종료 시 모듈 정리에 대한 정보도 제공합니다.

> 버전 3.10에서 변경: [`site`](https://docs.python.org/ko/3.12/library/site.html#module-site "사이트: 사이트별 구성을 담당하는 모듈.") 모듈은 처리 중인 사이트별 경로와 `.pth` 파일을 보고합니다.

- 또한 [`pythonverbose`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONVERBOSE)를 참조하십시오.

`-W arg`
- 경고 제어. 파이썬의 경고 기계는 기본적으로 경고 메시지를 [`sys.stderr`](https://docs.python.org/ko/3.12/library/sys.html#sys.stderr "sys.stderr")에 출력합니다.
- 가장 단순한 설정은 프로세스가 만드는 모든 경고에 무조건 특정 액션을 적용합니다 (그렇지 않으면 기본적으로 무시되는 경고조차도):

```
-Wdefault  # Warn once per call location
-Werror    # Convert to exceptions
-Walways   # Warn every time
-Wall      # Same as -Walways
-Wmodule   # Warn once per calling module
-Wonce     # Warn once per Python process
-Wignore   # Never warn
```

- 작업 이름은 원하는 대로 축약할 수 있으며 인터프리터는 이를 적절한 작업 이름으로 해석합니다. 예를 들어 `-Wi`는 `-Wignore`와 동일합니다.
- 인수의 전체 형식은 다음과 같습니다:

```
action:message:category:module:lineno
```

- 빈 필드는 모든 값과 일치하며, 후행 빈 필드는 생략할 수 있습니다. 예를 들어 `-W ignore::DeprecationWarning`은 모든 DeprecationWarning 경고를 무시합니다.
  
  `action` 필드는 위에서 설명한 것과 같지만 나머지 필드와 일치하는 경고에만 적용됩니다.
  `message` 필드는 전체 경고 메시지와 일치해야 하며 대소문자를 구분하지 않습니다.
  `category` 필드는 경고 카테고리와 일치해야 합니다(예: `DeprecationWarning`). 이 필드는 클래스 이름이어야 하며, 메시지의 실제 경고 카테고리가 지정된 경고 카테고리의 하위 클래스인지 여부를 테스트합니다.
  `module` 필드는 (정규화된) 모듈 이름과 일치하며, 대소문자를 구분하여 일치합니다.
  `lineno` 필드는 줄 번호와 일치하며, 여기서 0은 모든 줄 번호와 일치하므로 생략된 줄 번호와 동일합니다.

- 여러 개의 [`-W`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-W) 옵션을 지정할 수 있으며, 경고가 두 개 이상의 옵션과 일치하면 마지막으로 일치하는 옵션에 대한 작업이 수행됩니다. 잘못된 [`-W`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-W) 옵션은 무시됩니다(단, 첫 번째 경고가 발생하면 잘못된 옵션에 대한 경고 메시지가 출력됩니다).
- 경고는 [`PYTHONWARNINGS`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONWARNINGS) 환경 변수를 사용하여 제어할 수도 있고, 파이썬 프로그램 내에서 [`warnings`](https://docs.python.org/ko/3.12/library/warnings.html#module-warnings "warnings)를 사용하여 제어할 수도 있습니다: 경고 메시지를 발행하고 처리를 제어합니다.") 모듈을 사용합니다. 예를 들어, [`warnings.filterwarnings()`](https://docs.python.org/ko/3.12/library/warnings.html#warnings.filterwarnings "warnings.filterwarnings") 함수를 사용하여 경고 메시지에 정규식을 사용할 수 있습니다.
- 자세한 내용은 [경고 필터](https://docs.python.org/ko/3.12/library/warnings.html#warning-filter)와 [경고 필터 설명](https://docs.python.org/ko/3.12/library/warnings.html#describing-warning-filters)를 참조하십시오.

`-x`

- 소스의 첫 번째 줄을 건너 뛰어서, 유닉스 이외의 형식의 `#!cmd` 을 사용할 수 있게 합니다. 이것은 DOS 전용 핵(hack)을 위한 것입니다.

`-X` (3.2 추가)

- 다양한 구현 특정 옵션을 위해 예약되어 있습니다. CPython은 현재 다음과 같은 가능한 값을 정의합니다:
  
  - `-X faulthandler` (3.3 추가)를 사용하여 [`faulthanlder`](https://docs.python.org/ko/3.12/library/faulthandler.html#module-faulthandler "폴핸들러: 파이썬 트레이스백을 덤프합니다."). [`PYTHONFAULTHANDLER`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONFAULTHANDLER)도 참조하십시오.
  - `-X showrefcount` (3.4 추가) 를 사용하여 프로그램이 완료될 때 또는 대화형 인터프리터에서 각 문 뒤에 총 참조 수와 사용된 메모리 블록 수를 출력할 수 있습니다. 이 기능은 [디버그 빌드](https://docs.python.org/ko/3.12/using/configure.html#debug-build)에서만 작동합니다.
  - `-X tracemalloc` (3.4 추가) 를 사용하여 파이썬 메모리 할당 추적을 시작하려면 [`tracemalloc`](https://docs.python.org/ko/3.12/library/tracemalloc.html#module-tracemalloc "tracemalloc: 메모리 할당을 추적합니다.") 모듈을 사용합니다. 기본적으로 가장 최근 프레임만 트레이스의 트레이스백에 저장됩니다. 트레이스백 제한을 _NFRAME_ 프레임으로 설정하여 추적을 시작하려면 `-X tracemalloc=NFRAME`을 사용합니다. 자세한 내용은 [`tracemalloc.start()`](https://docs.python.org/ko/3.12/library/tracemalloc.html#tracemalloc.start "tracemalloc.start") 및 [`PYTHONTRACEMALLOC`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONTRACEMALLOC)를 참조하세요.
  - `-X int_max_str_digits` (3.11 추가) 는 [정수 문자열 변환 길이 제한](https://docs.python.org/ko/3.12/library/stdtypes.html#int-max-str-digits)을 구성합니다. 또한 [`PYTHONINTMAXSTRDIGITS`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONINTMAXSTRDIGITS)를 참조하십시오.
  - `-X importtime` (3.7 추가) 은 각 임포트가 얼마나 오래 걸렸는지 보여줍니다. 모듈 이름, 누적 시간(중첩된 임포트 포함), 자체 시간(중첩 임포트 제외)을 표시합니다. 다중 스레드 응용 프로그램에서 출력이 깨질 수 있음에 유의하십시오. 일반적인 사용법은 `python3 -X importtime -c 'import asyncio'` 입니다. [`PYTHONPROFILEIMPORTTIME`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONPROFILEIMPORTTIME) 도 참조하십시오.
  - `-X dev` (3.7 추가): [파이썬 개발 모드](https://docs.python.org/ko/3.12/library/devmode.html#devmode)를 활성화하면 기본적으로 활성화하기에는 비용이 너무 많이 드는 추가 런타임 검사를 도입합니다. [파이썬 개발 모드](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONDEVMODE)도 참조하세요.
  - `-X utf8` (3.7 추가) 는 [파이썬 UTF-8 모드](https://docs.python.org/ko/3.12/library/os.html#utf8-mode)를 활성화합니다. `-X utf8=0`은 [파이썬 UTF-8 모드](https://docs.python.org/ko/3.12/library/os.html#utf8-mode)를 명시적으로 비활성화합니다(자동으로 활성화되는 경우에도). 또한 [`PYTHONUTF8`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONUTF8)을 참조하십시오.
  - `-X pycache_prefix=PATH` (3.8 추가)는 `.pyc` 파일을 코드 트리 대신에 지정된 디렉터리를 루트로 하는 병렬 트리에 쓰도록 합니다. [`PYTHONPYCACHEPREFIX`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONPYCACHEPREFIX)도 참조하십시오.
  - `-X warn_default_encoding` (3.10 추가)은 파일을 열 때 로케일별 기본 인코딩을 사용하면 [`EncodingWarning`](https://docs.python.org/ko/3.12/library/exceptions.html#EncodingWarning "EncodingWarning")을 발행합니다. 또한 [`PYTHONWARNDEFAULTENCODING`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONWARNDEFAULTENCODING)을 참조하십시오.
  - `-X no_debug_ranges` (3.11 추가) 는 코드 객체의 모든 명령어에 추가 위치 정보(끝줄, 시작 열 오프셋 및 끝 열 오프셋)를 매핑하는 테이블을 포함하지 않도록 설정합니다. 이는 인터프리터가 트레이스백을 표시할 때 추가 시각적 위치 표시기를 억제하고 더 작은 코드 객체와 pyc 파일을 원할 때 유용합니다. 또한 [`python_debounds`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONNODEBUGRANGES)를 참조하십시오.
  - `-X frozen_modules` (3.11 추가)는 고정된 모듈을 가져오기 기계에서 무시할지 여부를 결정합니다. 값이 "켜짐"이면 가져오기되고 "꺼짐"이면 무시됩니다. 기본값은 설치된 Python(일반적인 경우)인 경우 "켜기"입니다. 개발 중(소스 트리에서 실행 중)인 경우 기본값은 "꺼짐"입니다. 이 플래그가 "off"로 설정되어 있어도 "importlib_bootstrap" 및 "importlib_bootstrap_external" 고정 모듈은 항상 사용된다는 점에 유의하세요.
  - `-X perf` 를 사용하면 Linux `perf` 프로파일러를 지원할 수 있습니다. 이 옵션을 제공하면 `perf` 프로파일러가 Python 호출을 보고할 수 있습니다. 이 옵션은 일부 플랫폼에서만 사용할 수 있으며 현재 시스템에서 지원되지 않는 경우 아무 작업도 수행하지 않습니다. 기본값은 "off"입니다. 또한 [`PYTHONPERFSUPPORT`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONPERFSUPPORT) 및 [Linux perf 프로파일러에 대한 파이썬 지원](https://docs.python.org/ko/3.12/howto/perf_profiling.html#perf-profiling)을 참조하십시오.

- 또한 [`sys._xoptions`](https://docs.python.org/ko/3.12/library/sys.html#sys._xoptions "sys._xoptions") 딕셔너리를 통해 임의의 값을 전달하고 조회할 수 있도록 합니다.

> 버전 3.9에서 변경: Removed the `-X showalloccount` option.
> 버전 3.10에서 변경: Removed the `-X oldparser` option.

### 사용해서는 안 되는 옵션

`-J`

- [Jython](https://www.jython.org/) 이 사용하기 위해 예약되었습니다


### 내장 환경 변수
- 이 환경 변수들은 파이썬의 동작에 영향을 주며, -E와 -I 이외의 명령 줄 스위치보다 먼저 처리됩니다. 충돌하면 명령 줄 스위치가 환경 변수에 우선하는 것이 관례입니다.

`PYTHONHOME`
- 표준 파이썬 라이브러리의 위치를 변경합니다. 기본적으로, 라이브러리는 `_prefix_/lib/python_version_`과 `_exec_prefix_/lib/python_version_`에서 검색되는데, `_prefix_` 와 `_exec_prefix_` 는 설치 의존적인 디렉터리이고, 둘 다 기본값은 `/usr/local` 입니다.
- [`PYTHONHOME`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONHOME) 이 하나의 디렉터리로 설정되면, 그 값은 `_prefix_` 와 `_exec_prefix_` 를 모두 대체합니다. 이들에 대해 다른 값을 지정하려면, [`PYTHONHOME`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONHOME) 을 `_prefix_:_exec_prefix_` 로 설정하십시오.

`PYTHONPATH`

- 모듈 파일의 기본 검색 경로를 보강합니다. 형식은 셸의 `PATH` 와 같습니다: 하나 이상의 디렉터리 경로명이 [`os.pathsep`](https://docs.python.org/ko/3.12/library/os.html#os.pathsep "os.pathsep") (예를 들어, 유닉스에서는 콜론, 윈도우에서는 세미콜론) 로 구분됩니다. 존재하지 않는 디렉터리는 조용히 무시됩니다.
- 일반 디렉터리 외에도, 개별 [`PYTHONPATH`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONPATH) 엔트리는 순수 파이썬 모듈(소스 또는 컴파일된 형식)을 포함하는 zip 파일을 가리킬 수 있습니다. 확장 모듈은 zip 파일에서 임포트될 수 없습니다.
- 기본 검색 경로는 설치 의존적이지만, 일반적으로 `_prefix_/lib/python_version_`으로 시작합니다 (위의 [`PYTHONHOME`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONHOME) 을 참조하세요). _항상_ [`PYTHONPATH`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONPATH) 에 추가됩니다.
- 위에서 설명한 대로 [인터페이스 옵션](https://docs.python.org/ko/3.12/using/cmdline.html#using-on-interface-options) 하에서는 [`PYTHONPATH`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONPATH) 앞에 검색 경로에 추가 디렉터리가 삽입됩니다. 검색 경로는 파이썬 프로그램 내에서 [`sys.path`](https://docs.python.org/ko/3.12/library/sys.html#sys.path "sys.path") 변수로 조작할 수 있습니다.

`PYTHONSAFEPATH` (3.11 추가)

- 비어 있지 않은 문자열로 설정된 경우 [`sys.path`](https://docs.python.org/ko/3.12/library/sys.html#sys.path "sys.path")에 안전하지 않을 수 있는 경로를 앞에 붙이지 마세요. 자세한 내용은 [`-P`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-P) 옵션을 참조하세요.

`PYTHONPLATLIBDIR` (3.9 추가)

- 이것을 비어 있지 않은 문자열로 설정하면, [`sys.platlibdir`](https://docs.python.org/ko/3.12/library/sys.html#sys.platlibdir "sys.platlibdir") 값을 재정의합니다.

`PYTHONSTARTUP`
- 이것이 읽을 수 있는 파일의 이름이면, 첫 번째 프롬프트가 대화형 모드에 표시되기 전에, 해당 파일의 파이썬 명령이 실행됩니다. 이 파일은 대화형 명령이 실행되는 것과 같은 이름 공간에서 실행되므로, 여기에서 정의되거나 임포트 한 객체를 대화형 세션에서 그대로 사용할 수 있습니다. 이 파일에서 프롬프트 [`sys.ps1`](https://docs.python.org/ko/3.12/library/sys.html#sys.ps1 "sys.ps1") 과 [`sys.ps2`](https://docs.python.org/ko/3.12/library/sys.html#sys.ps2 "sys.ps2") 와 훅 [`sys.__interactivehook__`](https://docs.python.org/ko/3.12/library/sys.html#sys.__interactivehook__ "sys.__interactivehook__") 도 바꿀 수 있습니다.
- 시작 시 호출될 때 filename을 인자로 [감사 이벤트(auditing event)](https://docs.python.org/ko/3.12/library/sys.html#auditing) `cpython.run_startup`을 발생시킵니다.

`PYTHONOPTIMIZE`
- 비어 있지 않은 문자열로 설정하면 [`-O`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-O) 옵션을 지정하는 것과 같습니다. 정수로 설정하면, [`-O`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-O)를 여러 번 지정하는 것과 같습니다.

`PYTHONBREAKPOINT` (3.7 추가)
- 설정되면, 점으로 구분된 경로 표기법을 사용하여 콜러블의 이름을 지정합니다. 콜러블을 포함하는 모듈이 임포트 된 후에 콜러블은, 내장 [`breakpoint()`](https://docs.python.org/ko/3.12/library/functions.html#breakpoint "breakpoint") 에 의해 호출되는 [`sys.breakpointhook()`](https://docs.python.org/ko/3.12/library/sys.html#sys.breakpointhook "sys.breakpointhook") 의 기본 구현이 실행합니다. 설정되지 않았거나 빈 문자열로 설정하면, 값 “pdb.set_trace”와 동등합니다. 문자열 “0”으로 설정하면, [`sys.breakpointhook()`](https://docs.python.org/ko/3.12/library/sys.html#sys.breakpointhook "sys.breakpointhook") 의 기본 구현은 아무것도 하지 않고 즉시 반환합니다.

`PYTHONDEBUG`
- 비어 있지 않은 문자열로 설정하면, [`-d`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-d) 옵션을 지정하는 것과 같습니다. 정수로 설정하면, [`-d`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-d)를 여러 번 지정하는 것과 같습니다.
- 이 환경 변수는 [파이썬 디버그 빌드](https://docs.python.org/ko/3.12/using/configure.html#debug-build)가 필요하며, 그렇지 않으면 무시됩니다.

`PYTHONINSPECT`

- 비어 있지 않은 문자열로 설정하면, [`-i`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-i) 옵션을 지정하는 것과 같습니다.
- 이 변수는 프로그램 종료 시 검사 모드를 강제하기 위해, [`os.environ`](https://docs.python.org/ko/3.12/library/os.html#os.environ "os.environ") 을 사용해서 파이썬 코드에 의해 수정될 수도 있습니다.
- 인자 없이 [감사 이벤트(auditing event)](https://docs.python.org/ko/3.12/library/sys.html#auditing) `cpython.run_stdin`을 발생시킵니다.

> 버전 3.12.5에서 변경: (also 3.11.10, 3.10.15, 3.9.20, and 3.8.20) Emits audit events.

`PYTHONUNBUFFERED`
- 비어 있지 않은 문자열로 설정하면, [`-u`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-u) 옵션을 지정하는 것과 같습니다.

`PYTHONVERBOSE`
- 비어 있지 않은 문자열로 설정하면, [`-v`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-v) 옵션을 지정하는 것과 같습니다. 정수로 설정하면 [`-v`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-v)를 여러 번 지정하는 것과 같습니다.

`PYTHONCASEOK`
- 이 옵션을 설정하면 파이썬은 [`import`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#import) 문에서 대소문자를 무시합니다. 이 옵션은 Windows와 macOS에서만 작동합니다.

`PYTHONDONTWRITEBYTECODE`
- 비어 있지 않은 문자열로 설정되면, 파이썬은 소스 모듈을 임포트 할 때 `.pyc` 파일을 쓰지 않습니다. 이는 [`-B`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-B) 옵션을 지정하는 것과 같습니다.

`PYTHONPYCACHEPREFIX` (3.8 추가)
- 설정되면, 파이썬은 소스 트리 내의 `__pycache__` 디렉터리 대신에 이 경로에 있는 미러 디렉터리 트리에 `.pyc` 파일을 씁니다. 이것은 [`-X`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-X) `pycache_prefix=PATH` 옵션을 지정하는 것과 동등합니다.

`PYTHONHASHSEED` (3.2.3 추가)
- 이 변수가 설정되어 있지 않거나 `random` 으로 설정되면, str과 bytes 객체의 해시 시드에 난수가 사용됩니다.
- [`PYTHONHASHSEED`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONHASHSEED) 가 정숫값으로 설정되면, 해시 무작위화가 적용되는 형의 hash()를 생성하기 위한 고정 시드로 사용됩니다.
- 목적은 인터프리터 자체에 대한 셀프 테스트와 같은 이유로 반복 가능한 해싱을 허용하거나, 파이썬 프로세스 클러스터가 해시값을 공유하도록 허용하는 것입니다.
- 정수는 [0,4294967295] 범위의 십진수여야 합니다. 값 0을 지정하면 해시 무작위화가 비활성화됩니다.

`PYTHONINTMAXSTRDIGITS` (3.11 추가)

- 이 변수를 정수로 설정하면 인터프리터의 전역 [정수 문자열 변환 길이 제한](https://docs.python.org/ko/3.12/library/stdtypes.html#int-max-str-digits)을 구성하는 데 사용됩니다.

`PYTHONIOENCODING` 

- 인터프리터를 실행하기 전에 이것이 설정되면, `stdin/stdout/stderr`에 사용되는 인코딩을 대체합니다. 문법은 `encodingname:errorhandler` 형식입니다. `encodingname` 과 `:errorhandler` 부분은 모두 선택 사항이며 [`str.encode()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.encode "str.encode") 에서와 같은 의미입니다.
- stderr의 경우, `:errorhandler` 부분은 무시됩니다; 처리기는 항상 `'backslashreplace'` 입니다.

> 버전 3.4에서 변경: `encodingname` 부분은 이제 선택적입니다.
> 버전 3.6에서 변경: Windows에서, [`PYTHONLEGACYWINDOWSSTDIO`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSSTDIO) 도 지정하지 않는 한, 대화형 콘솔 버퍼에서 이 변수로 지정된 인코딩이 무시됩니다. 표준 스트림을 통해 리디렉션 된 파일과 파이프는 영향을 받지 않습니다.

`PYTHONNOUSERSITE`
- 설정되면, 파이썬은 [`사용자 site-packages 디렉터리`](https://docs.python.org/ko/3.12/library/site.html#site.USER_SITE "site.USER_SITE") 를 [`sys.path`](https://docs.python.org/ko/3.12/library/sys.html#sys.path "sys.path") 에 추가하지 않습니다.

> [**PEP 370**](https://peps.python.org/pep-0370/) – 사용자별 site-packages 디렉터리

`PYTHONUSERBASE`
- [`사용자 사이트-패키지 디렉터리`](https://docs.python.org/ko/3.12/library/site.html#site.USER_BASE "site.USER_BASE") 및 `python -m pip install --user`의 [`사용자 사이트-패키지 디렉터리`](https://docs.python.org/ko/3.12/library/site.html#site.USER_SITE "site.USER_SITE) 및 [설치 경로](https://docs.python.org/ko/3.12/library/sysconfig.html#sysconfig-user-scheme) 경로를 계산하는 데 사용되는 [`사용자 기본 디렉터리`]를 정의합니다.

> [**PEP 370**](https://peps.python.org/pep-0370/) – 사용자별 site-packages 디렉터리

`PYTHONEXECUTABLE`

- 이 환경 변수가 설정되어 있으면 `sys.argv[0]`가 C 런타임을 통해 가져온 값 대신 해당 값으로 설정됩니다. macOS에서만 작동합니다.

`PYTHONWARNINGS`

- [`-W`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-W) 옵션과 동등합니다. 쉼표로 구분된 문자열로 설정하면, [`-W`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-W)를 여러 번 지정하는 것과 같습니다. 목록의 뒷부분에 있는 필터는 목록의 이전 필터보다 우선합니다.
- 가장 단순한 설정은 프로세스가 만드는 모든 경고에 무조건 특정 액션을 적용합니다 (그렇지 않으면 기본적으로 무시되는 경고조차도):

```
PYTHONWARNINGS=default  # Warn once per call location
PYTHONWARNINGS=error    # Convert to exceptions
PYTHONWARNINGS=always   # Warn every time
PYTHONWARNINGS=all      # Same as PYTHONWARNINGS=always
PYTHONWARNINGS=module   # Warn once per calling module
PYTHONWARNINGS=once     # Warn once per Python process
PYTHONWARNINGS=ignore   # Never warn
```

> 자세한 내용은 [경고 필터](https://docs.python.org/ko/3.12/library/warnings.html#warning-filter)와 [경고 필터 설명](https://docs.python.org/ko/3.12/library/warnings.html#describing-warning-filters)를 참조하십시오.

`PYTHONFAULTHANDLER` (3.3 추가)
- 이 환경 변수가 비어 있지 않은 문자열로 설정된 경우, 시작 시 [`faulthandler.enable()`](https://docs.python.org/ko/3.12/library/faulthandler.html#faulthandler.enable "faulthandler.enable")가 호출됩니다: [`SIGSEGV`](https://docs.python.org/ko/3.12/library/signal.html#signal.SIGSEGV "signal.SIGSEGV"), [`SIGFPE`](https://docs.python.org/ko/3.12/library/signal.html#signal.SIGFPE "signal.SIGFPE"), [`SIGABRT`](https://docs.python.org/ko/3.12/library/signal.html#signal.SIGABRT "signal.SIGABRT"), [`SIGBUS`](https://docs.python.org/ko/3.12/library/signal.html#signal.SIGBUS "signal.SIGBUS") 및 [`SIGILL`](https://docs.python.org/ko/3.12/library/signal.html#signal.SIGILL "signal.SIGILL") 시그널을 위한 처리기를 설치하여 Python 트레이스백을 덤프합니다. 이는 [`-X`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-X) `폴핸들러` 옵션과 동일합니다.

`PYTHONTRACEMALLOC` (3.4 추가)

- 이 환경 변수가 비어 있지 않은 문자열로 설정되어 있으면 [`tracemalloc`](https://docs.python.org/ko/3.12/library/tracemalloc.html#module-tracemalloc "tracemalloc.") 모듈을 사용하여 파이썬 메모리 할당을 추적하기 시작합니다: 메모리 할당을 추적합니다.") 모듈을 사용합니다. 이 변수의 값은 트레이스의 트레이스백에 저장되는 최대 프레임 수입니다. 예를 들어, `PYTHONTRACEMALLOC=1`은 가장 최근 프레임만 저장합니다. 자세한 내용은 [`tracemalloc.start()`](https://docs.python.org/ko/3.12/library/tracemalloc.html#tracemalloc.start "tracemalloc.start") 함수를 참조하세요. 이는 [`-X`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-X) `tracemalloc` 옵션을 설정하는 것과 동일합니다.


`PYTHONPROFILEIMPORTTIME` (3.7 추가)

- 이 환경 변수가 비어 있지 않은 문자열로 설정되어 있으면 파이썬은 각 가져오기에 걸리는 시간을 표시합니다. 이는 [`-X`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-X) `importtime` 옵션을 설정하는 것과 동일합니다.

`PYTHONASYNCIODEBUG` (3.4 추가)
- 이 환경 변수가 비어 있지 않은 문자열로 설정되면, [`asyncio`](https://docs.python.org/ko/3.12/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.") 모듈의 [디버그 모드](https://docs.python.org/ko/3.12/library/asyncio-dev.html#asyncio-debug-mode) 를 활성화합니다.

`PYTHONMALLOC` (3.6 추가)

- 파이썬 메모리 할당자를 설정하거나 디버그 훅을 설치합니다.
- 파이썬이 사용하는 메모리 할당자를 설정합니다:
  
  - `default`: [기본 메모리 할당자](https://docs.python.org/ko/3.12/c-api/memory.html#default-memory-allocators) 를 사용합니다.
  - `malloc`: 모든 도메인에 대해 C 라이브러리의 `malloc()` 함수를 사용합니다([`PYMEM_DOMIN_RAW`](https://docs.python.org/ko/3.12/c-api/memory.html#c.PYMEM_DOMAIN_RAW "PYMEM_DOMIN_RAW"), [`PYMEM_DOMIN_MEM`](https://docs.python.org/ko/3.12/c-api/memory.html#c.PYMEM_DOMAIN_MEM "PYMEM_DOMIN_MEM"), [`PYMEM_DOMIN_OBJ`](https://docs.python.org/ko/3.12/c-api/memory.html#c.PYMEM_DOMAIN_OBJ "PYMEM_DOMIN_OBJ")).
  - `pymalloc`: [`pymalloc` 할당자](https://docs.python.org/ko/3.12/c-api/memory.html#pymalloc)를 사용하여 [`PYMEM_DOMIN_MEM`](https://docs.python.org/ko/3.12/c-api/memory.html#c.PYMEM_DOMAIN_MEM "PYMEM_DOMIN_MEM") 및 [`PYMEM_DOMIN_OBJ`](https://docs.python.org/ko/3.12/c-api/memory.html#c.PYMEM_DOMAIN_OBJ "PYMEM_DOMIN_OBJ") 도메인을 할당하고 `malloc()` 함수를 사용하여 [`PYMEM_DOMIN_RAW`](https://docs.python.org/ko/3.12/c-api/memory.html#c.PYMEM_DOMAIN_RAW "PYMEM_DOMIN_RAW") 도메인에 할당할 수 있습니다.

- [디버그 후크](https://docs.python.org/ko/3.12/c-api/memory.html#pymem-debug-hooks)를 설치합니다:
  
  - `debug`: [기본 메모리 할당자](https://docs.python.org/ko/3.12/c-api/memory.html#default-memory-allocators) 위에 디버그 훅을 설치합니다.
  - `malloc_debug`: `malloc` 과 같지만, 디버그 훅도 설치합니다.
  - `pymalloc_debug`: `pymalloc` 과 같지만, 디버그 훅도 설치합니다.

> 버전 3.7에서 변경: `"default"` 할당자를 추가했습니다.

`PYTHONMALLOCSTATS`

- 비어 있지 않은 문자열로 설정되면, 파이썬은 새로운 `pymalloc` 객체 영역이 생성될 때마다, 그리고 종료할 때 [pymalloc 메모리 할당자](https://docs.python.org/ko/3.12/c-api/memory.html#pymalloc) 의 통계를 인쇄합니다.
- [`PYTHONMALLOC`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONMALLOC) 환경 변수를 사용하여 C 라이브러리의 `malloc()` 할당자를 강제로 사용하거나, `pymalloc` 지원 없이 파이썬을 구성하면, 이 변수는 무시됩니다.

> 버전 3.6에서 변경: 이 변수는 이제 배포 모드로 컴파일된 파이썬에서도 사용할 수 있습니다. 이제 빈 문자열로 설정하면 효과가 없습니다.

`PYTHONLEGACYWINDOWSFSENCODING` (3.6 추가)

- 비어 있지 않은 문자열로 설정하면 기본 [파일 시스템 인코딩 및 오류 처리기](https://docs.python.org/ko/3.12/glossary.html#term-filesystem-encoding-and-error-handler) 모드가 각각 3.6 이전 값인 'mbcs' 및 'replace'로 되돌아갑니다. 그렇지 않으면 새로운 기본값인 'utf-8' 및 'surrogatepass'가 사용됩니다.
- 이것은 또한 실행 시간에 [`sys._enablelegacywindowsfsencoding()`](https://docs.python.org/ko/3.12/library/sys.html#sys._enablelegacywindowsfsencoding "sys._enablelegacywindowsfsencoding") 으로 활성화 될 수 있습니다.
> [가용성](https://docs.python.org/ko/3.12/library/intro.html#availability): 윈도우.
> 자세한 내용은 [**PEP 529**](https://peps.python.org/pep-0529/)를 참조하십시오.

`PYTHONLEGACYWINDOWSSTDIO` (3.6 추가)

- 비어 있지 않은 문자열로 설정하면, 새 콘솔 입력기와 출력기를 사용하지 않습니다. 이것은 유니코드 문자가 utf-8을 사용하는 대신 활성 콘솔 코드 페이지에 따라 인코딩됨을 의미합니다.
- 이 변수는 표준 스트림이 콘솔 버퍼를 참조하는 대신 리디렉트 된 (파일 또는 파이프로) 경우 무시됩니다.

> [가용성](https://docs.python.org/ko/3.12/library/intro.html#availability): 윈도우.

`PYTHONCOERCECLOCALE` (3.7 추가)

- 값 `0` 으로 설정하면, 주 파이썬 명령 줄 응용 프로그램이 레거시 ASCII 기반 C와 POSIX 로케일을 보다 유능한 UTF-8 기반 대안으로 강제 변환하지 않습니다.
- 이 변수가 설정되지 _않고_ (또는 `0` 이외의 값으로 설정되고), 환경 변수에 우선하는 `LC_ALL` 로케일도 설정되지 않고, `LC_CTYPE` 범주에 대해 보고되는 현재 로케일이 기본 `C` 로케일이거나 명시적인 ASCII 기반의 `POSIX` 로케일이면, 파이썬 CLI는 인터프리터 런타임을 로드하기 전에 `LC_CTYPE` 범주에 대해 다음 로케일을 나열된 순서대로 구성하려고 시도합니다:
  
  - `C.UTF-8`
  - `C.utf8`
  - `UTF-8`

- 이러한 로케일 범주 중 하나를 설정하는 데 성공하면, 파이썬 런타임이 초기화되기 전에 `LC_CTYPE` 환경 변수도 현재 프로세스 환경에서 적절히 설정됩니다. 이렇게 하면 인터프리터 자신과 같은 프로세스에서 실행되는 다른 로케일 인식 구성 요소(가령 GNU `readline` 라이브러리)가 볼 수 있는 것에 더해, 갱신된 설정을 현재 C 로케일이 아닌 환경을 조회하는 연산(가령 파이썬 자체의 [`locale.getdefaultlocale()`](https://docs.python.org/ko/3.12/library/locale.html#locale.getdefaultlocale "locale.getdefaultlocale"))뿐만 아니라, 자식 프로세스에서도 (이 프로세스가 파이썬 인터프리터를 실행하는지에 관계없이) 볼 수 있습니다.
- 이러한 로케일 중 하나를 구성하면 (명시적으로나 위의 묵시적 로케일 강제 변경을 통해) [`sys.stdin`](https://docs.python.org/ko/3.12/library/sys.html#sys.stdin "sys.stdin") 과 [`sys.stdout`](https://docs.python.org/ko/3.12/library/sys.html#sys.stdout "sys.stdout") 에 대해 `surrogateescape` [에러 처리기](https://docs.python.org/ko/3.12/library/codecs.html#error-handlers) 를 자동으로 활성화합니다 ([`sys.stderr`](https://docs.python.org/ko/3.12/library/sys.html#sys.stderr "sys.stderr") 는 다른 로케일에서처럼 `backslashreplace` 를 계속 사용합니다). 이 스트림 처리 동작은 평소처럼 [`PYTHONIOENCODING`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONIOENCODING)을 사용하여 대체할 수 있습니다.
- 디버깅을 위해, `PYTHONCOERCECLOCALE=warn` 을 설정하면, 로케일 강제 변경이 일어나거나, 그렇지 않고 강제 변경을 _유발할_ 로케일이 파이썬 런타임이 초기화될 때 여전히 활성 상태면 파이썬은 `stderr` 로 경고 메시지를 보냅니다.
- 또한, 로케일 강제 변환이 비활성화되거나 적절한 대상 로케일을 찾지 못할 때도, 레거시 ASCII 기반 로케일에서 [`PYTHONUTF8`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONUTF8) 은 기본적으로 활성화됨에 유의하십시오. 인터프리터가 시스템 인터페이스에 대해 `UTF-8` 대신에 `ASCII` 를 사용하게 하려면, 두 가지 기능을 모두 비활성화시켜야 합니다.

> [Availability](https://docs.python.org/ko/3.12/library/intro.html#availability): Unix.
> 자세한 내용은 [**PEP 538**](https://peps.python.org/pep-0538/)을 참조하십시오.

`PYTHONDEVMODE` (3.7 추가)

- 이 환경 변수가 비어 있지 않은 문자열로 설정되어 있으면 [Python 개발 모드](https://docs.python.org/ko/3.12/library/devmode.html#devmode)를 활성화하여 기본적으로 활성화하기에는 너무 많은 비용이 드는 추가 런타임 검사를 도입합니다. 이는 [`-X`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-X) `dev` 옵션을 설정하는 것과 동일합니다.

`PYTHONUTF8` (3.7 추가)

- '1'로 설정하면 [파이썬 UTF-8 모드](https://docs.python.org/ko/3.12/library/os.html#utf8-mode)를 활성화합니다. 
- '0'으로 설정하면 [파이썬 UTF-8 모드](https://docs.python.org/ko/3.12/library/os.html#utf8-mode)를 비활성화합니다.
- 다른 모든 비어 있지 않은 문자열로 설정하면, 인터프리터를 초기화하는 동안 에러가 발생합니다.

`PYTHONWARNDEFAULTENCODING` (3.10 추가)

- 이 환경 변수가 비어 있지 않은 문자열로 설정되어 있으면 로캘별 기본 인코딩이 사용될 때 [`EncodingWarning`](https://docs.python.org/ko/3.12/library/exceptions.html#EncodingWarning "EncodingWarning")을 발행합니다.
- 자세한 내용은 [옵트인 인코딩 경고](https://docs.python.org/ko/3.12/library/io.html#io-encoding-warning)를 참조하세요.


`PYTHONNODEBUGRANGES` (3.11 추가)

- 이 변수를 설정하면 코드 객체의 모든 명령어에 추가 위치 정보(끝줄, 시작 열 오프셋 및 끝 열 오프셋)를 매핑하는 테이블을 포함하지 않도록 설정합니다. 이 변수는 인터프리터가 트레이스백을 표시할 때 추가 시각적 위치 표시기를 억제하고 더 작은 코드 객체 및 pyc 파일을 원하는 경우에 유용합니다.

`PYTHONPERFSUPPORT` (3.12 추가)

- 이 변수를 0이 아닌 값으로 설정하면 Linux `perf` 프로파일러를 지원하여 파이썬 호출을 감지할 수 있도록 합니다.
- `0`으로 설정하면 Linux `perf` 프로파일러 지원을 비활성화합니다.
- 또한 [`-X perf`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-X) 명령줄 옵션 및 [Linux perf 프로파일러에 대한 Python 지원](https://docs.python.org/ko/3.12/howto/perf_profiling.html#perf-profiling)을 참조하세요.

#### 디버그 모드 변수

`PYTHONDUMPREFS`
- 설정되면, 파이썬은 인터프리터를 종료한 후에도 살아있는 객체와 참조 횟수를 덤프합니다.
- [`with-trace-refs`](https://docs.python.org/ko/3.12/using/configure.html#cmdoption-with-trace-refs) 빌드 옵션으로 구성된 Python이 필요합니다.

`PYTHONDUMPREFSFILE=FILENAME` (3.11 추가)
- 이 옵션을 설정하면 파이썬은 인터프리터를 종료한 후에도 여전히 살아있는 객체와 참조 수를 _FILENAME_ 이라는 파일에 덤프합니다.
- [`with-trace-refs`](https://docs.python.org/ko/3.12/using/configure.html#cmdoption-with-trace-refs) 빌드 옵션으로 구성된 Python이 필요합니다.

## 개발자 모드 (Dev Mode)
- 파이썬 개발 모드에는 기본적으로 활성화하기에 너무 비싼 추가 실행 시간 검사를 도입합니다. 코드가 올바르면 기본값보다 더 상세하지(verbose) 않아야 합니다; 새로운 경고는 문제가 감지될 때만 발생합니다.
- [`-X dev`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-X) 명령 줄 옵션을 사용하거나 [`PYTHONDEVMODE`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONDEVMODE) 환경 변수를 `1`로 설정하여 활성화할 수 있습니다.

### 파이썬 개발 모드의 효과

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

### 디버그 빌드 (Debug Build)
- 디버그 빌드는 [`--wydebug`](https://docs.python.org/ko/3.12/using/configure.html#cmdoption-with-pydebug) 구성 옵션으로 빌드한 Python입니다.
- 기본적으로 모든 경고 표시: 기본 경고 필터 목록은 [`warnings`](https://docs.python.org/ko/3.12/library/warnings.html#module-warnings "warnings: 경고 메시지를 발행하고 처리를 제어합니다.") 모듈에서 기본 경고 필터 목록이 비어 있습니다.
- [`sys.abiflags`](https://docs.python.org/ko/3.12/library/sys.html#sys.abiflags "sys.abiflags")에 `d`를 추가합니다.
- [`sys.gettotalrefcount()` 함수를 추가합니다.
- [`-X showrefcount`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-X) 명령줄 옵션을 추가합니다.
- [`-d`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-d) 명령줄 옵션과 [`PYTHONDEBUG`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONDEBUG) 환경 변수를 추가하여 구문 분석기를 디버그할 수 있습니다.
- 변수가 정의된 경우 바이트코드 평가 루프에서 저수준 추적을 활성화하는 `__lltrace__` 변수에 대한 지원 추가.
- 메모리 할당자에 대한 디버그 훅](https://docs.python.org/ko/3.12/c-api/memory.html#default-memory-allocators)을 설치하여 버퍼 오버플로 및 기타 메모리 오류를 감지합니다.
- `Py_DEBUG` 및 `Py_REF_DEBUG` 매크로를 정의합니다.
- 런타임 검사 추가: `#ifdef Py_DEBUG` 및 `#endif`로 둘러싸인 코드. `assert(...)` 및 `_PyObject_ASSERT(...)` 어설션 활성화: `NDEBUG` 매크로를 설정하지 않습니다([`--with-assertions`](https://docs.python.org/ko/3.12/using/configure.html#cmdoption-with-assertions) 구성 옵션도 참조). 주요 런타임 검사:
    - 함수 인자에 대한 건전성 검사 추가 
    - 유니코드 및 int 객체는 초기화되지 않은 객체의 사용을 감지하는 패턴으로 메모리가 채워진 상태로 생성됩니다. 
    - 현재 예외를 지우거나 대체할 수 있는 함수가 예외가 발생한 상태에서 호출되지 않는지 확인
    - 할당 해제기 함수가 현재 예외를 변경하지 않는지 확인합니다.
    - 가비지 컬렉터([`gc.collect()`](https://docs.python.org/ko/3.12/library/gc.html#gc.collect "gc.collect") 함수)는 객체 일관성에 대한 몇 가지 기본 검사를 실행합니다. 
    - `Py_SAFE_DOWNCAST()` 매크로는 넓은 타입에서 좁은 타입으로 다운 캐스팅할 때 정수 언더플로우 및 오버플로우를 검사합니다.

> 버전 3.8에서 변경: 이제 릴리스 빌드와 디버그 빌드가 ABI와 호환됩니다: `Py_DEBUG` 매크로를 정의하면 더 이상 `Py_TRACE_REFS` 매크로([`--with-trace-refs`](https://docs.python.org/ko/3.12/using/configure.html#cmdoption-with-trace-refs) 옵션 참조)를 의미하지 않아 유일한 ABI 비호환성을 유발합니다.

### 디버그 옵션 (Debug options)

`--with-pydebug`
- [[#디버그 빌드 (Debug Build)]]: `Py_DEBUG` 매크로를 정의합니다(기본적으로 비활성화됨).

`--with-trace-refs` (3.8 추가)
- 디버깅 목적으로 추적 참조를 사용하도록 설정합니다(기본적으로 비활성화됨).
  
  효과:
	- `Py_TRACE_REFS` 매크로를 정의합니다. 
	- `sys.getobjects()` 함수를 추가합니다. 
	- [`PYTHONDUMPREFS`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONDUMPREFS) 환경 변수를 추가합니다.
   
- 이 빌드는 릴리스 빌드(기본 빌드) 또는 디버그 빌드(`Py_DEBUG` 및 `Py_REF_DEBUG` 매크로)와 ABI가 호환되지 않습니다.

`--with-assertions` (3.6 추가)
- C 어설션을 활성화하여 빌드합니다(기본값은 아니요): `assert(...);` 및 `_PyObject_ASSERT(...);`.
- 설정된 경우, `NDEBUG` 매크로는 [`OPT`](https://docs.python.org/ko/3.12/using/configure.html#envvar-OPT) 컴파일러 변수에 정의되지 않습니다.
- 어설션을 활성화하는 [`--with-pydebug`](https://docs.python.org/ko/3.12/using/configure.html#cmdoption-with-pydebug) 옵션([debug build](https://docs.python.org/ko/3.12/using/configure.html#debug-build)도 참조하십시오.

`--with-valgrind`
- Valgrind 지원을 활성화합니다(기본값은 아니요).

`--with-dtrace` (3.6 추가)
- DTrace 지원을 활성화합니다(기본값은 아니요).
- [DTrace 및 SystemTap으로 CPython 계측하기](https://docs.python.org/ko/3.12/howto/instrumentation.html#instrumentation)를 참조하세요.

`--with-address-sanitizer` (3.6 추가)
- AddressSanitizer 메모리 오류 탐지기 'asan'을 활성화합니다(기본값은 아니요).

`--with-memory-sanitizer` (3.6 추가)
- 메모리 새니타이저 할당 오류 감지기인 `msan`을 활성화합니다(기본값은 아니요).

`--with-undefined-behavior-sanitizer` (3.6 추가)
- 정의되지 않은 동작 탐지기를 활성화합니다(기본값은 아니요).


## 빌드 설정
[3. Python 구성 — Python 3.12.5 문서](https://docs.python.org/ko/3.12/using/configure.html)


### 성능 옵션 (Performance options)
- 최상의 성능을 위해 `--enable-optimizations --with-lto`(PGO + LTO)를 사용하여 Python을 구성하는 것이 좋습니다. 실험적인 `--enable-bolt` 플래그를 사용하여 성능을 개선할 수도 있습니다.

`--enable-optimizations` (3.6 추가)
- 프로파일 가이드 최적화(PGO)를 [`PROFILE_TASK`](https://docs.python.org/ko/3.12/using/configure.html#envvar-PROFILE_TASK)를 사용하여 활성화합니다(기본적으로 비활성화됨).
- C 컴파일러 Clang은 PGO를 위해 `llvm-profdata` 프로그램이 필요합니다. macOS에서는 GCC에도 필요합니다: GCC는 macOS에서 Clang의 별칭일 뿐입니다.
- libpython에서 `--enable-shared`를 사용하고 GCC를 사용하는 경우 컴파일러 및 링커 플래그에 `-fno-semantic-interposition`을 추가하여 의미론적 삽입도 비활성화합니다.


> 빌드 중에 일부 소스 파일에 프로필 데이터를 사용할 수 없다는 컴파일러 경고가 표시될 수 있습니다. 이러한 경고는 프로필 데이터를 수집하는 동안 코드의 일부만 실행되므로 무해합니다. Clang에서 이러한 경고를 비활성화하려면 [`CFLAGS`](https://docs.python.org/ko/3.12/using/configure.html#envvar-CFLAGS)에 `-Wno-profile-instr-unprofiled`를 추가하여 수동으로 비활성화하세요.

> 버전 3.10에서 변경: GCC에서 `-fno-semantic-interposition`을 사용합니다.

`PROFILE_TASK` (3.8 추가)
- Makefile에 사용되는 환경 변수입니다: PGO 생성 작업을 위한 Python 명령줄 인수입니다.

Default: `-m test --pgo --timeout=$(TESTTIMEOUT)`.

`--with-lto=[full|thin|no|yes]` (3.6 추가)
- 모든 빌드에서 링크 시간 최적화(LTO)를 활성화합니다(기본적으로 비활성화됨). C 컴파일러 Clang은 LTO를 위해 `llvm-ar`(macOS에서는 `ar`)와 LTO 인식 링커(`ld.gold` 또는 `lld`)를 필요로 합니다.

> 3.11 추가: ThinLTO 기능을 사용하려면 Clang에서 `--with-lto=thin`을 사용하세요.

> 버전 3.12에서 변경: 컴파일러가 이 플래그를 수락하면 Clang의 기본 최적화 정책으로 ThinLTO를 사용합니다.

`--enable-bolt` (3.12 추가)
- BOLT 포스트 링크 바이너리 옵티마이저](https://github.com/llvm/llvm-project/tree/main/bolt) 사용을 활성화합니다(기본적으로 비활성화됨).
- BOLT는 LLVM 프로젝트의 일부이지만 바이너리 배포에 항상 포함되지는 않습니다. 이 플래그를 사용하려면 `llvm-bolt` 및 `merge-fdata`를 사용할 수 있어야 합니다.
- BOLT는 아직 상당히 새로운 프로젝트이므로 이 플래그는 현재로서는 실험적인 것으로 간주해야 합니다. 이 도구는 머신 코드에서 작동하므로 빌드 환경 + 기타 최적화 구성 인수 + CPU 아키텍처의 조합에 따라 성공 여부가 결정되며 모든 조합이 지원되는 것은 아닙니다. LLVM 16 이전의 BOLT 버전은 일부 시나리오에서 BOLT가 충돌하는 것으로 알려져 있습니다. BOLT 최적화를 위해서는 LLVM 16 이상을 사용할 것을 강력히 권장합니다.
- `BOLT_INSTRUMENT_FLAGS` 및 `BOLT_APPLY_FLAGS` **configure** 변수를 정의하여 각각 **llvm-bolt**의 기본 인수 집합을 재정의하여 바이너리에 볼트 데이터를 계측 및 적용하도록 할 수 있습니다.

`--with-computed-gotos`
- 평가 루프에서 계산된 고토를 활성화합니다(지원되는 컴파일러에서 기본적으로 활성화됨).

`--without-pymalloc`
- 특수 파이썬 메모리 할당자 [pymalloc](https://docs.python.org/ko/3.12/c-api/memory.html#pymalloc)(기본적으로 활성화됨)를 비활성화합니다. 
- [`PYTHONMALLOC`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONMALLOC) 환경 변수를 참조하십시오.

`--without-doc-strings
- 정적 문서 문자열을 비활성화하여 메모리 사용량을 줄입니다(기본적으로 활성화됨). 
- 파이썬에 정의된 문서 문자열은 영향을 받지 않습니다. 
- `WITH_DOC_STRINGS` 매크로를 정의하지 마세요. 
- `PyDoc_STRVAR()` 매크로를 참조하세요.

`--enable-profiling`
- `gprof`로 C레벨 코드 프로파일링을 활성화합니다(기본적으로 비활성화됨).

`--with-strict-overflow`
C 컴파일러 플래그에 `-fstrict-overflow`를 추가합니다(기본값은 `-fno-strict-overflow` 대신 추가합니다).


## 운영체제 별 Python

### Unix
#### 최신 버전의 파이썬 내려받기와 설치

##### 리눅스

- 파이썬은 대부분 리눅스 배포판에 사전 설치되어 있으며, 다른 모든 곳에서 패키지로 사용할 수 있습니다. 그러나 배포판 패키지에 없는 어떤 기능을 사용하고 싶을 수 있습니다. 소스에서 최신 버전의 파이썬을 쉽게 컴파일할 수 있습니다.
- 파이썬이 미리 설치되어 있지 않고 저장소에도 없으면, 여러분 자신의 배포를 위한 패키지를 쉽게 만들 수 있습니다. 다음 링크를 살펴보십시오:

> [!NOTE] 패키지
> **데비안 사용자용**
> [https://www.debian.org/doc/manuals/maint-guide/first.en.html](https://www.debian.org/doc/manuals/maint-guide/first.en.html)
> 
> **OpenSuse 사용자용**
> [https://en.opensuse.org/Portal:Packaging](https://en.opensuse.org/Portal:Packaging)
> 
> **Fedora 사용자용**
> [https://docs.fedoraproject.org/en-US/package-maintainers/Packaging_Tutorial_GNU_Hello/](https://docs.fedoraproject.org/en-US/package-maintainers/Packaging_Tutorial_GNU_Hello/)
> 
> **Slackware 사용자용**
> [https://slackbook.org/html/package-management-making-packages.html](https://slackbook.org/html/package-management-making-packages.html)
> 


##### FreeBSD와 OpenBSD
- FreeBSD 사용자, 패키지를 추가하려면 이렇게 하십시오:

```sh
pkg install python3
```

- OpenBSD 사용자, 패키지를 추가하려면 이렇게 하십시오:

```sh
pkg_add -r python

pkg_add ftp://ftp.openbsd.org/pub/OpenBSD/4.2/packages/<insert your architecture here>/python-<version>.tgz
```

- 예를 들어 i386 사용자는 이렇게 파이썬 2.5.1 버전을 얻습니다:

```sh
pkg_add ftp://ftp.openbsd.org/pub/OpenBSD/4.2/packages/i386/python-2.5.1p2.tgz
```

#### 파이썬 빌드하기

- CPython을 직접 컴파일하려면 먼저 [소스](https://www.python.org/downloads/source/)를 구해야 합니다. 최신 릴리스의 소스를 다운로드하거나 새 [클론](https://devguide.python.org/setup/#get-the-source-code)을 가져올 수 있습니다. (패치를 기여하려면 클론이 필요합니다.)
- 빌드 프로세스는 일반적으로 다음과 같은 명령으로 구성됩니다

```
./configure
make
make install
```

- 특정 Unix 플랫폼에 대한 [구성 옵션](https://docs.python.org/ko/3.12/using/configure.html#configure-options) 및 주의 사항은 Python 소스 트리의 루트에 있는 [README.rst](https://github.com/python/cpython/tree/3.12/README.rst) 파일에 광범위하게 문서화되어 있습니다.


> [!warning]
> - `make install`은 `python3` 바이너리를 덮어쓰거나 가장 할 수 있습니다. 따라서 `make altinstall`을 `make install` 대신 권장하는데, `_exec_prefix_/bin/python_version_` 만 설치하기 때문입니다.

#### 파이썬 관련 경로와 파일

- 이는 현지 설치 규칙에 따라 다를 수 있으며, [`prefix`](https://docs.python.org/ko/3.12/using/configure.html#cmdoption-prefix) 및 [`exec_prefix`](https://docs.python.org/ko/3.12/using/configure.html#cmdoption-exec-prefix)는 설치에 따라 다르며 GNU 소프트웨어의 경우와 동일하게 해석해야 합니다.
- 예를 들어, 대부분 리눅스 시스템에서, 기본값은 모두 `/usr`입니다.

| 파일/디렉터리                                                                     | 의미                                                        |
| --------------------------------------------------------------------------- | --------------------------------------------------------- |
| `_exec_prefix_/bin/python3`                                                 | 인터프리터의 권장 위치.                                             |
| `_prefix_/lib/python_version_`, `_exec_prefix_/lib/python_version_`         | 표준 모듈을 포함하는 디렉터리의 권장 위치.                                  |
| `_prefix_/include/python_version_`, `_exec_prefix_/include/python_version_` | 파이썬 확장을 개발하고 인터프리터를 내장하는 데 필요한 인클루드 파일을 포함하는 디렉터리의 권장 위치. |

#### 파이썬 스크립트 만들기
- 유닉스에서 파이썬 스크립트를 쉽게 사용하려면, 실행 파일로 만들어야 합니다.
- 스크립트는 **chmod** 명령을 사용하여 실행 가능한 모드, 또는 권한, 을 부여받을 수 있습니다.

```sh
$ chmod +x myscript.py
```

- 윈도우 시스템에서는 “실행 가능 모드”라는 개념이 없습니다. 파이썬 설치 프로그램은 `.py` 파일을 `python.exe`와 자동으로 연결하여, 파이썬 파일을 이중 클릭하면 스크립트로 실행합니다. 확장자는 `.pyw` 일 수도 있습니다. 이 경우, 일반적으로 나타나는 콘솔 창은 표시되지 않습니다.
- 그리고, 스크립트의 상단에 적절한 셔뱅(Shebang) 줄을 넣습니다. 좋은 선택은 대개 이렇습니다. BSD 스타일의 유닉스 시스템에서 파이썬 스크립트는 셸 스크립트처럼 직접 실행할 수 있게 만들 수 있습니다. 다음과 같은 줄

```python
#!/usr/bin/env python3
```

- (인터프리터가 사용자의 `PATH` 에 있다고 가정할 때)을 스크립트의 시작 부분에 넣고 파일에 실행 가능 모드를 줍니다. `#!` 는 반드시 파일의 처음 두 문자여야 합니다. 일부 플랫폼에서는 이 첫 번째 줄이 유닉스 스타일의 줄 종료 (`'\n'`)로 끝나야 하며, 윈도우 줄 종료(`'\r\n'`)는 허락되지 않습니다. 파이썬에서 해시, 또는 파운드, 문자 `'#'` 는 주석을 시작하는 데 사용됩니다.
- 이것은 `PATH` 전체에서 파이썬 인터프리터를 검색합니다. 그러나, 일부 유닉스에는 **env** 명령이 없을 수 있으므로, 인터프리터 경로로 `/usr/bin/python3`를 하드 코딩해야 할 수 있습니다.
- 파이썬 스크립트에서 셸 명령을 사용하려면, [`subprocess`](https://docs.python.org/ko/3.12/library/subprocess.html#module-subprocess "subprocess: Subprocess management.") 모듈을 보십시오.

#### 사용자 지정 OpenSSL

1. 공급업체의 OpenSSL 구성 및 시스템 신뢰 저장소를 사용하려면 `/etc`에서 `openssl.cnf` 파일 또는 심볼릭 링크가 있는 디렉터리를 찾습니다. 대부분의 배포판에서 이 파일은 `/etc/ssl` 또는 `/etc/pki/tls`에 있습니다. 디렉터리에는 `cert.pem` 파일 및/또는 `certs` 디렉터리도 포함되어야 합니다..

```sh
$ find /etc/ -name openssl.cnf -printf "%h\n"
/etc/ssl
```

2. OpenSSL을 다운로드, 빌드 및 설치합니다. 설치`가 아닌 `install_sw`를 사용해야 합니다. install_sw` 타겟은 `openssl.cnf`를 재정의하지 않습니다.

```sh
$ curl -O https://www.openssl.org/source/openssl-VERSION.tar.gz
$ tar xzf openssl-VERSION
$ pushd openssl-VERSION
$ ./config \
	--prefix=/usr/local/custom-openssl \
	--libdir=lib \
	--openssldir=/etc/ssl
$ make -j1 depend
$ make -j8
$ make install_sw
$ popd
```

3. 사용자 지정 OpenSSL로 Python 빌드(`--with-openssl` 및 `--with-openssl-rpath` 옵션 구성 참조).

```python
$ pushd python-3.x.x
$ ./configure -C \
	--with-openssl=/usr/local/custom-openssl \
	--with-openssl-rpath=auto \
	--prefix=/usr/local/python-3.x.x
$ make -j8
$ make altinstall
```

> OpenSSL의 패치 릴리스에는 이전 버전과 호환되는 ABI가 있습니다. OpenSSL을 업데이트하기 위해 Python을 다시 컴파일할 필요는 없습니다. 사용자 지정 OpenSSL 설치를 최신 버전으로 교체하는 것으로 충분합니다.

### Windows
[4. 윈도우에서 파이썬 사용하기 — Python 3.12.5 문서](https://docs.python.org/ko/3.12/using/windows.html)

### Mac
[5. Using Python on a Mac — Python 3.12.5 문서](https://docs.python.org/ko/3.12/using/mac.html)

---


## 참조



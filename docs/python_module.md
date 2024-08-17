---
title: "[Python] 함수 (Function)"
excerpt: 
categories:
  - Python
tags:
  - Python
  - Module
last_modified_at: 2024-04-11T15:10:55+09:00
link: 
상위 항목: "[[python_home|파이썬 (Python)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

---

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

Modules can import other modules. It is customary but not required to place all [`import`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#import) statements at the beginning of a module (or script, for that matter). The imported module names, if placed at the top level of a module (outside any functions or classes), are added to the module’s global namespace.

There is a variant of the [`import`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#import) statement that imports names from a module directly into the importing module’s namespace. For example:

>>>

>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

This does not introduce the module name from which the imports are taken in the local namespace (so in the example, `fibo` is not defined).

모듈이 정의하는 모든 이름을 임포트하는 변종도 있습니다:

>>>

>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

이것은 밑줄 (`_`) 로 시작하는 것들을 제외한 모든 이름을 임포트 합니다. 대부분 파이썬 프로그래머들은 이 기능을 사용하지 않는데, 인터프리터로 알려지지 않은 이름들의 집합을 도입하게 되어, 여러분이 이미 정의한 것들을 가리게 될 수 있기 때문입니다.

일반적으로 모듈이나 패키지에서 `*` 를 임포트하는 것은 눈살을 찌푸리게 한다는 것에 유의하세요, 종종 읽기에 편하지 않은 코드를 만들기 때문입니다. 하지만, 대화형 세션에서 입력을 줄이고자 사용하는 것은 상관없습니다.

모듈 이름 다음에 `as` 가 올 경우, `as` 다음의 이름을 임포트한 모듈에 직접 연결합니다.

>>>

>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

이것은 `import fibo` 가하는 것과 같은 방식으로 모듈을 임포트 하는데, 유일한 차이점은 그 모듈을 `fib` 라는 이름으로 사용할 수 있다는 것입니다.

[`from`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#from)을 써서 비슷한 효과를 낼 때도 사용할 수 있습니다:

>>>

>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

참고

 

효율성의 이유로, 각 모듈은 인터프리터 세션마다 한 번만 임포트됩니다. 그래서, 여러분이 모듈을 수정하면, 인터프리터를 다시 시작시켜야 합니다 — 또는, 대화형으로 시험하는 모듈이 하나뿐이라면, [`importlib.reload()`](https://docs.python.org/ko/3.12/library/importlib.html#importlib.reload "importlib.reload") 를 사용하세요. 예를 들어, `import importlib; importlib.reload(modulename)`.

### 6.1.1. 모듈을 스크립트로 실행하기[](https://docs.python.org/ko/3.12/tutorial/modules.html#executing-modules-as-scripts "Link to this heading")

여러분이 파이썬 모듈을 이렇게 실행하면

python fibo.py <arguments>

모듈에 있는 코드는, 그것을 임포트할 때처럼 실행됩니다. 하지만 `__name__` 은 `"__main__"` 로 설정됩니다. 이것은, 이 코드를 모듈의 끝에 붙여서:

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

파일을 임포트할 수 있는 모듈뿐만 아니라 스크립트로도 사용할 수 있도록 만들 수 있음을 의미하는데, 오직 모듈이 “메인” 파일로 실행될 때만 명령행을 파싱하는 코드가 실행되기 때문입니다:

$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34

모듈이 임포트될 때, 코드는 실행되지 않습니다:

>>>

>>> import fibo
>>>

이것은 종종 모듈에 대한 편리한 사용자 인터페이스를 제공하거나 테스트 목적으로 사용됩니다 (모듈을 스크립트로 실행하면 테스트 스위트를 실행하기).

### 6.1.2. 모듈 검색 경로[](https://docs.python.org/ko/3.12/tutorial/modules.html#the-module-search-path "Link to this heading")

When a module named `spam` is imported, the interpreter first searches for a built-in module with that name. These module names are listed in [`sys.builtin_module_names`](https://docs.python.org/ko/3.12/library/sys.html#sys.builtin_module_names "sys.builtin_module_names"). If not found, it then searches for a file named `spam.py` in a list of directories given by the variable [`sys.path`](https://docs.python.org/ko/3.12/library/sys.html#sys.path "sys.path"). [`sys.path`](https://docs.python.org/ko/3.12/library/sys.html#sys.path "sys.path") is initialized from these locations:

- 입력 스크립트를 포함하는 디렉터리 (또는 파일이 지정되지 않았을 때는 현재 디렉터리).
    
- [`PYTHONPATH`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONPATH) (디렉터리 이름들의 목록, 셸 변수 `PATH` 와 같은 문법).
    
- The installation-dependent default (by convention including a `site-packages` directory, handled by the [`site`](https://docs.python.org/ko/3.12/library/site.html#module-site "site: Module responsible for site-specific configuration.") module).
    

More details are at [The initialization of the sys.path module search path](https://docs.python.org/ko/3.12/library/sys_path_init.html#sys-path-init).

참고

 

심볼릭 링크를 지원하는 파일 시스템에서, 입력 스크립트를 포함하는 디렉터리는 심볼릭 링크를 변환한 후에 계산됩니다. 다른 말로, 심볼릭 링크를 포함하는 디렉터리는 모듈 검색 경로에 포함되지 **않습니다**.

초기화 후에, 파이썬 프로그램은 [`sys.path`](https://docs.python.org/ko/3.12/library/sys.html#sys.path "sys.path") 를 수정할 수 있습니다. 스크립트를 포함하는 디렉터리는 검색 경로의 처음에, 표준 라이브러리 경로의 앞에 놓입니다. 이것은 같은 이름일 경우 라이브러리 디렉터리에 있는 것 대신 스크립트를 포함하는 디렉터리의 것이 로드된다는 뜻입니다. 이 치환이 의도된 것이 아니라면 에러입니다. 더 자세한 정보는 [표준 모듈들](https://docs.python.org/ko/3.12/tutorial/modules.html#tut-standardmodules) 을 보세요.

### 6.1.3. “컴파일된” 파이썬 파일[](https://docs.python.org/ko/3.12/tutorial/modules.html#compiled-python-files "Link to this heading")

모듈 로딩을 빠르게 하려고, 파이썬은 `__pycache__` 디렉터리에 각 모듈의 컴파일된 버전을 `module._version_.pyc` 라는 이름으로 캐싱합니다. version 은 컴파일된 파일의 형식을 지정합니다; 일반적으로 파이썬의 버전 번호를 포함합니다. 예를 들어, CPython 배포 3.3 에서 spam.py 의 컴파일된 버전은 `__pycache__/spam.cpython-33.pyc` 로 캐싱 됩니다. 이 명명법은 서로 다른 파이썬 배포와 버전의 컴파일된 모듈들이 공존할 수 있도록 합니다.

파이썬은 소스의 수정 시간을 컴파일된 버전과 비교해서 시효가 지나 다시 컴파일해야 하는지 검사합니다. 이것은 완전히 자동화된 과정입니다. 또한, 컴파일된 모듈은 플랫폼 독립적이기 때문에, 같은 라이브러리를 서로 다른 아키텍처를 갖는 시스템들에서 공유할 수 있습니다.

파이썬은 두 가지 상황에서 캐시를 검사하지 않습니다. 첫째로, 명령행에서 직접 로드되는 모듈들은 항상 재컴파일하고 그 결과를 저장하지 않습니다. 둘째로, 소스 모듈이 없으면 캐시를 검사하지 않습니다. 소스 없는 (컴파일된 파일만 있는) 배포를 지원하려면, 컴파일된 모듈이 소스 디렉터리에 있어야 하고, 소스 모듈이 없어야 합니다.

전문가를 위한 몇 가지 팁

- 컴파일된 모듈의 크기를 줄이려면 파이썬 명령에 [`-O`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-O) 나 [`-OO`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-OO) 스위치를 사용할 수 있습니다. `-O` 스위치는 assert 문을 제거하고, `-OO` 스위치는 assert 문과 __doc__ 문자열을 모두 제거합니다. 어떤 프로그램들은 이것들에 의존하기 때문에, 무엇을 하고 있는지 아는 경우만 이 옵션을 사용해야 합니다. “최적화된” 모듈은 `opt-` 태그를 갖고, 보통 더 작습니다. 미래의 배포에서는 최적화의 효과가 변경될 수 있습니다.
    
- `.py` 파일에서 읽을 때보다 `.pyc` 파일에서 읽을 때 프로그램이 더 빨리 실행되지는 않습니다; `.pyc` 파일에서 더 빨라지는 것은 로드되는 속도뿐입니다.
    
- 모듈 [`compileall`](https://docs.python.org/ko/3.12/library/compileall.html#module-compileall "compileall: Tools for byte-compiling all Python source files in a directory tree.") 은 디렉터리에 있는 모든 모듈의 .pyc 파일들을 만들 수 있습니다.
    
- 이 절차에 대한 더 자세한 정보, 결정들의 순서도를 포함합니다, 는 [**PEP 3147**](https://peps.python.org/pep-3147/) 에 나옵니다.
    

## 6.2. 표준 모듈들[](https://docs.python.org/ko/3.12/tutorial/modules.html#standard-modules "Link to this heading")

파이썬은 표준 모듈들의 라이브러리가 함께 오는데, 별도의 문서 파이썬 라이브러리 레퍼런스 (이후로는 “라이브러리 레퍼런스”) 에서 설명합니다. 어떤 모듈들은 인터프리터에 내장됩니다; 이것들은 언어의 핵심적인 부분은 아니지만 그런데도 내장된 연산들에 대한 액세스를 제공하는데, 효율이나 시스템 호출과 같은 운영 체제 기본 요소들에 대한 액세스를 제공하기 위함입니다. 그런 모듈들의 집합은 설정 옵션인데 기반 플랫폼 의존적입니다. 예를 들어, [`winreg`](https://docs.python.org/ko/3.12/library/winreg.html#module-winreg "winreg: Routines and objects for manipulating the Windows registry. (Windows)") 모듈은 윈도우 시스템에서만 제공됩니다. 특별한 모듈 하나는 주목을 받을 필요가 있습니다: [`sys`](https://docs.python.org/ko/3.12/library/sys.html#module-sys "sys: Access system-specific parameters and functions."). 모든 파이썬 인터프리터에 내장됩니다. 변수 `sys.ps1` 와 `sys.ps2` 는 기본과 보조 프롬프트로 사용되는 문자열을 정의합니다:

>>>

>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'… '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>

이 두 개의 변수들은 인터프리터가 대화형 모드일 때만 정의됩니다.

변수 `sys.path` 는 인터프리터의 모듈 검색 경로를 결정하는 문자열들의 리스트입니다. 환경 변수 [`PYTHONPATH`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONPATH) 에서 취한 기본 경로나, [`PYTHONPATH`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONPATH) 가 설정되지 않는 경우 내장 기본값으로 초기화됩니다. 표준 리스트 연산을 사용해서 수정할 수 있습니다:

>>>

>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')

## 6.3. [`dir()`](https://docs.python.org/ko/3.12/library/functions.html#dir "dir") 함수[](https://docs.python.org/ko/3.12/tutorial/modules.html#the-dir-function "Link to this heading")

내장 함수 [`dir()`](https://docs.python.org/ko/3.12/library/functions.html#dir "dir") 은 모듈이 정의하는 이름들을 찾는 데 사용됩니다. 문자열들의 정렬된 리스트를 돌려줍니다:

>>>

>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)  
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
 '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
 '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
 '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']

인자가 없으면, [`dir()`](https://docs.python.org/ko/3.12/library/functions.html#dir "dir") 는 현재 정의한 이름들을 나열합니다:

>>>

>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']

모든 형의 이름을 나열한다는 것에 유의해야 합니다: 변수, 모듈, 함수, 등등.

[`dir()`](https://docs.python.org/ko/3.12/library/functions.html#dir "dir") 은 내장 함수와 변수들의 이름을 나열하지 않습니다. 그것들의 목록을 원한다면, 표준 모듈 [`builtins`](https://docs.python.org/ko/3.12/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.") 에 정의되어 있습니다:

>>>

>>> import builtins
>>> dir(builtins)  
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']

## 6.4. 패키지[](https://docs.python.org/ko/3.12/tutorial/modules.html#packages "Link to this heading")

Packages are a way of structuring Python’s module namespace by using “dotted module names”. For example, the module name `A.B` designates a submodule named `B` in a package named `A`. Just like the use of modules saves the authors of different modules from having to worry about each other’s global variable names, the use of dotted module names saves the authors of multi-module packages like NumPy or Pillow from having to worry about each other’s module names.

음향 파일과 과 음향 데이터의 일관된 처리를 위한 모듈들의 컬렉션 (“패키지”) 을 설계하길 원한다고 합시다. 여러 종류의 음향 파일 형식이 있으므로 (보통 확장자로 구분됩니다, 예를 들어: `.wav`, `.aiff`, `.au`), 다양한 파일 형식 간의 변환을 위해 계속 늘어나는 모듈들의 컬렉션을 만들고 유지할 필요가 있습니다. 또한, 음향 데이터에 적용하고자 하는 많은 종류의 연산들도 있으므로 (믹싱, 에코 넣기, 이퀄라이저 기능 적용, 인공적인 스테레오 효과 만들기와 같은), 이 연산들을 수행하기 위한 모듈들을 끊임없이 작성하게 될 것입니다. 패키지를 이렇게 구성해 볼 수 있습니다 (계층적 파일 시스템으로 표현했습니다):

sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              …
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              …
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              …

패키지를 임포트할 때, 파이썬은 `sys.path` 에 있는 디렉터리들을 검색하면서 패키지 서브 디렉터리를 찾습니다.

The `__init__.py` files are required to make Python treat directories containing the file as packages (unless using a [namespace package](https://docs.python.org/ko/3.12/glossary.html#term-namespace-package), a relatively advanced feature). This prevents directories with a common name, such as `string`, from unintentionally hiding valid modules that occur later on the module search path. In the simplest case, `__init__.py` can just be an empty file, but it can also execute initialization code for the package or set the `__all__` variable, described later.

패키지 사용자는 패키지로부터 개별 모듈을 임포트할 수 있습니다, 예를 들어:

import sound.effects.echo

This loads the submodule `sound.effects.echo`. It must be referenced with its full name.

sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

서브 모듈을 임포트하는 다른 방법은 이렇습니다:

from sound.effects import echo

This also loads the submodule `echo`, and makes it available without its package prefix, so it can be used as follows:

echo.echofilter(input, output, delay=0.7, atten=4)

또 다른 방법은 원하는 함수나 변수를 직접 임포트하는 것입니다:

from sound.effects.echo import echofilter

Again, this loads the submodule `echo`, but this makes its function `echofilter()` directly available:

echofilter(input, output, delay=0.7, atten=4)

`from package import item` 를 사용할 때, item은 패키지의 서브 모듈 (또는 서브 패키지)일 수도 있고 함수, 클래스, 변수 등 패키지에 정의된 다른 이름들일 수도 있음에 유의하세요. `import` 문은 먼저 item이 패키지에 정의되어 있는지 검사하고, 그렇지 않으면 모듈이라고 가정하고 로드를 시도합니다. 찾지 못한다면, [`ImportError`](https://docs.python.org/ko/3.12/library/exceptions.html#ImportError "ImportError") 예외를 일으킵니다.

이에 반하여, `import item.subitem.subsubitem` 와 같은 문법을 사용할 때, 마지막 것을 제외한 각 항목은 반드시 패키지여야 합니다; 마지막 항목은 모듈이나 패키지가 될 수 있지만, 앞의 항목에서 정의된 클래스, 함수, 변수 등이 될 수는 없습니다.

### 6.4.1. 패키지에서 * 임포트 하기[](https://docs.python.org/ko/3.12/tutorial/modules.html#importing-from-a-package "Link to this heading")

이제 `from sound.effects import *` 라고 쓰면 어떻게 될까? 이상적으로는, 어떻게든 파일 시스템에서 패키지에 어떤 모듈들이 들어있는지 찾은 다음, 그것들 모두를 임포트 하기를 원할 것입니다. 이렇게 하는 데는 시간이 오래 걸리고 서브 모듈을 임포트 함에 따라 어떤 서브 모듈을 명시적으로 임포트할 경우만 일어나야만 하는 원하지 않는 부수적 효과가 발생할 수 있습니다.

유일한 해결책은 패키지 저자가 패키지의 색인을 명시적으로 제공하는 것입니다. [`import`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#import) 문은 다음과 같은 관례가 있습니다: 패키지의 `__init__.py` 코드가 `__all__` 이라는 이름의 목록을 제공하면, 이것을 `from package import *` 를 만날 때 임포트 해야만 하는 모듈 이름들의 목록으로 받아들입니다. 새 버전의 패키지를 출시할 때 이 목록을 최신 상태로 유지하는 것은 패키지 저자의 책임입니다. 패키지 저자가 패키지에서 * 를 임포트하는 용도가 없다고 판단한다면, 이것을 지원하지 않기로 할 수도 있습니다. 예를 들어, 파일 `sound/effects/__init__.py` 는 다음과 같은 코드를 포함할 수 있습니다:

__all__ = ["echo", "surround", "reverse"]

This would mean that `from sound.effects import *` would import the three named submodules of the `sound.effects` package.

Be aware that submodules might become shadowed by locally defined names. For example, if you added a `reverse` function to the `sound/effects/__init__.py` file, the `from sound.effects import *` would only import the two submodules `echo` and `surround`, but _not_ the `reverse` submodule, because it is shadowed by the locally defined `reverse` function:

__all__ = [
    "echo",      # refers to the 'echo.py' file
    "surround",  # refers to the 'surround.py' file
    "reverse",   # !!! refers to the 'reverse' function now !!!
]

def reverse(msg: str):  # <-- this name shadows the 'reverse.py' submodule
    return msg[::-1]    #     in the case of a 'from sound.effects import *'

If `__all__` is not defined, the statement `from sound.effects import *` does _not_ import all submodules from the package `sound.effects` into the current namespace; it only ensures that the package `sound.effects` has been imported (possibly running any initialization code in `__init__.py`) and then imports whatever names are defined in the package. This includes any names defined (and submodules explicitly loaded) by `__init__.py`. It also includes any submodules of the package that were explicitly loaded by previous [`import`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#import) statements. Consider this code:

import sound.effects.echo
import sound.effects.surround
from sound.effects import *

In this example, the `echo` and `surround` modules are imported in the current namespace because they are defined in the `sound.effects` package when the `from…import` statement is executed. (This also works when `__all__` is defined.)

설사 어떤 모듈이 `import *` 를 사용할 때 특정 패턴을 따르는 이름들만 익스포트 하도록 설계되었다 하더라도, 프로덕션 코드에서는 여전히 좋지 않은 사례로 여겨집니다.

`from package import specific_submodule` 을 사용하는데 잘못된 것은 없다는 것을 기억하세요! 사실, 임포트하는 모듈이 다른 패키지에서 같은 이름의 서브 모듈을 사용할 필요가 없는 한 권장되는 표기법입니다.

### 6.4.2. 패키지 내부 간의 참조[](https://docs.python.org/ko/3.12/tutorial/modules.html#intra-package-references "Link to this heading")

When packages are structured into subpackages (as with the `sound` package in the example), you can use absolute imports to refer to submodules of siblings packages. For example, if the module `sound.filters.vocoder` needs to use the `echo` module in the `sound.effects` package, it can use `from sound.effects import echo`.

You can also write relative imports, with the `from module import name` form of import statement. These imports use leading dots to indicate the current and parent packages involved in the relative import. From the `surround` module for example, you might use:

from . import echo
from .. import formats
from ..filters import equalizer

상대 임포트가 현재 모듈의 이름에 기반을 둔다는 것에 주의하세요. 메인 모듈의 이름은 항상 `"__main__"` 이기 때문에, 파이썬 응용 프로그램의 메인 모듈로 사용될 목적의 모듈들은 반드시 절대 임포트를 사용해야 합니다.

### 6.4.3. 여러 디렉터리에 있는 패키지[](https://docs.python.org/ko/3.12/tutorial/modules.html#packages-in-multiple-directories "Link to this heading")

패키지는 특별한 어트리뷰트 하나를 더 지원합니다, [`__path__`](https://docs.python.org/ko/3.12/reference/import.html#path__ "__path__"). 이것은 패키지의 `__init__.py` 파일을 실행하기 전에, 이 파일이 들어있는 디렉터리의 이름을 포함하는 리스트로 초기화됩니다. 이 변수는 수정할 수 있습니다; 그렇게 하면 그 이후로 패키지에 포함된 모듈과 서브 패키지를 검색하는 데 영향을 주게 됩니다.

이 기능이 자주 필요하지는 않지만, 패키지에서 발견되는 모듈의 집합을 확장하는 데 사용됩니다.

---

## 예제

## 참조

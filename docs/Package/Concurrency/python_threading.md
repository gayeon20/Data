---
title: "[Python] 쓰레딩 (Threading)"
excerpt: 
categories:
  - Python
tags:
  - Python
  - Python-Library
  - Concurrency
  - Python-threading
last_modified_at: 2024-04-11T15:11:34+09:00
link: https://docs.python.org/ko/3/library/threading.html
상위 항목: "[[python_concurrency|파이썬 동시 실행 (Python Concurrency)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`


---
- 이 모듈은 하위 수준 [`_thread`] 모듈 위에 상위 수준 스레딩 인터페이스를 구성합니다.
> 버전 3.7에서 변경: 이 모듈은 선택 사양이었지만, 이제는 항상 사용 가능합니다.

> [!NOTE]
> [`concurrent.futures.ThreadPoolExecutor`](https://docs.python.org/ko/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor)는 호출 스레드의 실행을 차단하지 않고 백그라운드 스레드에 작업을 푸시하면서도 필요할 때 결과를 검색할 수 있는 더 높은 수준의 인터페이스를 제공합니다.
> [`queue`](https://docs.python.org/ko/3/library/queue.html#module-queue)는 실행 중인 스레드 간에 데이터를 교환하기 위한 스레드 안전 인터페이스를 제공합니다.
> [`asyncio`](https://docs.python.org/ko/3/library/asyncio.html#module-asyncio)는 여러 운영 체제 스레드를 사용하지 않고도 작업 수준의 동시성을 달성하는 대안적 접근 방식을 제공합니다.

> Python 2.x 시리즈에서 이 모듈은 일부 메서드와 함수에 camelCase 이름을 포함하고 있었습니다. 이들은 Python 3.10부터 사용 중단되었지만, Python 2.5 이하 버전과의 호환성을 위해 여전히 지원됩니다.

> **CPython 구현 상세:** CPython에서는, 전역 인터프리터 록으로 인해 한 번에 하나의 스레드만 파이썬 코드를 실행할 수 있습니다 (설사 일부 성능 지향 라이브러리가 이 제한을 극복할 수 있을지라도). 응용 프로그램에서 멀티 코어 기계의 계산 자원을 더 잘 활용하려면 [`multiprocessing`](https://docs.python.org/ko/3/library/multiprocessing.html#module-multiprocessing)이나 [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/ko/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor)를 사용하는 것이 좋습니다. 그러나, 여러 I/O 병목 작업을 동시에 실행하고 싶을 때 threading은 여전히 적절한 모델입니다.

> 가용성 (Availability): Emscripten, WASI에서는 사용할 수 없습니다.

- 이 모듈은 WebAssembly 플랫폼 wasm32-emscripten 및 wasm32-wasi에서 작동하지 않거나 사용할 수 없습니다. 자세한 정보는 WebAssembly 플랫폼을 참조하세요.

`threading.active_count()`
- 현재 살아있는 Thread 객체 수를 반환합니다. 반환된 수는 enumerate()가 반환한 리스트의 길이와 같습니다.
- 함수 `activeCount`는 이 함수의 사용 중단된 별칭입니다.

`threading.current_thread()`
- 호출자의 제어 스레드에 해당하는 현재 Thread 객체를 반환합니다. 호출자의 제어 스레드가 threading 모듈을 통해 만들어지지 않았으면, 기능이 제한된 더미 스레드 객체가 반환됩니다.
- 함수 `currentThread`는 이 함수의 사용 중단된 별칭입니다.

`threading.excepthook(args, /)`
- Thread.run()에 의해 발생한 포착되지 않은 예외를 처리합니다.
- args 인자에는 다음과 같은 어트리뷰트가 있습니다:
	- exc_type: 예외 형.
	- exc_value: 예외 값, None일 수 있습니다.
	- exc_traceback: 예외 트레이스백, None일 수 있습니다.
	- thread: 예외를 발생시킨 스레드, None일 수 있습니다.
- exc_type이 SystemExit이면, 예외는 조용히 무시됩니다. 그렇지 않으면, sys.stderr에 예외가 인쇄됩니다.
- 이 함수에서 예외가 발생하면, 이를 처리하기 위해 sys.excepthook()이 호출됩니다.
- Thread.run()에 의해 발생한 포착되지 않은 예외를 처리하는 방법을 제어하기 위해 threading.excepthook()을 재정의할 수 있습니다.
- 사용자 정의 훅을 사용하여 exc_value를 저장하면 참조 순환을 만들 수 있습니다. 예외가 더는 필요하지 않을 때 참조 순환을 끊기 위해 명시적으로 지워야 합니다.
- 사용자 정의 훅을 사용하여 thread를 저장하면 파이널라이즈 중인 객체로 설정되면 이를 되살릴 수 있습니다. 객체를 되살리는 것을 방지하려면 사용자 정의 훅이 완료된 후 thread를 보관하지 마십시오.

> sys.excepthook()은 포착되지 않은 예외를 처리합니다.

> 버전 3.8에서 추가.

`threading.__excepthook__`

- threading.excepthook()의 원래 값을 보유합니다. 깨진 객체나 대체 객체로 교체되는 경우 원래 값을 복원할 수 있도록 저장됩니다.

> 버전 3.10에서 추가.

`threading.get_ident()`

- 현재 스레드의 '스레드 식별자'를 반환합니다. 이것은 0이 아닌 정수입니다. 이 값은 직접적인 의미가 없습니다; 이것은 매직 쿠키로 사용하려는 것입니다, 예를 들어 스레드 특정 데이터의 딕셔너리를 인덱싱하는 데 사용됩니다. 스레드 식별자는 스레드가 종료되고 다른 스레드가 만들어질 때 재활용될 수 있습니다.

> 버전 3.3에서 추가.

`threading.get_native_id()`
- 커널이 할당한 현재 스레드의 네이티브 정수 스레드 ID를 반환합니다. 음수가 아닌 정수입니다. 이 값은 시스템 전체에서 이 특정 스레드를 고유하게 식별하는 데 사용될 수 있습니다 (스레드가 종료될 때까지, 그 후에는 OS에서 값을 재활용할 수 있습니다).

> 가용성: Windows, FreeBSD, Linux, macOS, OpenBSD, NetBSD, AIX, DragonFlyBSD.

> 버전 3.8에서 추가.

`threading.enumerate()`

- 현재 활성 상태인 모든 Thread 객체의 리스트를 반환합니다. 이 리스트에는 데몬 스레드와 current_thread()에 의해 생성된 더미 스레드 객체가 포함됩니다. 종료된 스레드와 아직 시작되지 않은 스레드는 제외됩니다. 그러나 메인 스레드는 종료된 경우에도 항상 결과에 포함됩니다.

`threading.main_thread()`

- 메인 Thread 객체를 반환합니다. 정상적인 조건에서, 메인 스레드는 파이썬 인터프리터가 시작된 스레드입니다.

> 버전 3.4에서 추가.

`threading.settrace(func)`

- threading 모듈에서 시작된 모든 스레드에 대한 추적 함수를 설정합니다. func는 run() 메서드가 호출되기 전에 각 스레드에 대해 sys.settrace()로 전달됩니다.

`threading.settrace_all_threads(func)`

- threading 모듈에서 시작된 모든 스레드와 현재 실행 중인 모든 Python 스레드에 대한 추적 함수를 설정합니다.
- func는 각 스레드의 run() 메서드가 호출되기 전에 sys.settrace()로 전달됩니다.

> 버전 3.12에서 추가.

`threading.gettrace()`
- settrace()에 의해 설정된 추적 함수를 가져옵니다.

> 버전 3.10에서 추가.

`threading.setprofile(func)`

- threading 모듈에서 시작된 모든 스레드에 대한 프로파일 함수를 설정합니다. func는 run() 메서드가 호출되기 전에 각 스레드에 대해 sys.setprofile()로 전달됩니다.

`threading.setprofile_all_threads(func)`
- threading 모듈에서 시작된 모든 스레드와 현재 실행 중인 모든 Python 스레드에 대한 프로파일 함수를 설정합니다.
- func는 각 스레드의 run() 메서드가 호출되기 전에 sys.setprofile()로 전달됩니다.

> 버전 3.12에서 추가.

`threading.getprofile()`
- setprofile()에 의해 설정된 프로파일러 함수를 가져옵니다.

> 버전 3.10에서 추가.

`threading.stack_size([size])`

- 새 스레드를 만들 때 사용된 스레드 스택 크기를 반환합니다. 선택적 size 인자는 이후에 만들어지는 스레드에 사용할 스택 크기를 지정하며, 0(플랫폼이나 구성된 기본값을 사용합니다)이거나 32,768 (32 KiB) 이상의 양의 정숫값이어야 합니다. size를 지정하지 않으면, 0이 사용됩니다. 스레드 스택 크기 변경이 지원되지 않으면, RuntimeError가 발생합니다. 지정된 스택 크기가 유효하지 않으면, ValueError가 발생하고 스택 크기는 수정되지 않습니다. 32 KiB는 현재 인터프리터 자체에 충분한 스택 공간을 보장하기 위해 지원되는 최소 스택 크기 값입니다. 최소 스택 크기가 32 KiB 보다 커야 한다거나 시스템 메모리 페이지 크기의 배수로 할당해야 하는 등 일부 플랫폼에는 스택 크기 값에 대한 특정 제한이 있을 수 있습니다 - 자세한 내용은 플랫폼 설명서를 참조하십시오 (4 KiB 페이지는 흔합니다; 스택 크기에 4096의 배수를 사용하는 것이 더 구체적인 정보가 없을 때 제안하는 방법입니다).

> 가용성: Windows, POSIX 스레드를 지원하는 Unix 플랫폼.

`threading.TIMEOUT_MAX`
- 블로킹 함수(Lock.acquire(), RLock.acquire(), Condition.wait() 등)의 timeout 매개 변수에 허용되는 최댓값. 이 값보다 큰 timeout을 지정하면 OverflowError가 발생합니다.

> 버전 3.2에서 추가.


> [!NOTE]
> - 이 모듈은 아래 섹션에 자세히 설명되는 많은 클래스를 정의합니다.
> - 이 모듈의 설계는 Java의 스레딩 모델에 약하게 기반합니다. 그러나, Java가 록(locks)과 조건 변수(condition variables)를 모든 객체의 기본 동작으로 만들지만, 파이썬에서는 별도의 객체입니다. 파이썬의 Thread 클래스는 Java Thread 클래스 동작의 부분 집합을 지원합니다; 현재, 우선순위가 없고, 스레드 그룹이 없으며 스레드를 파괴, 중지, 일시 중지, 재개 또는 인터럽트 할 수 없습니다. 구현될 때, Java 스레드 클래스의 정적 메서드는 모듈 수준 함수에 매핑됩니다.
> - 아래에 설명된 모든 메서드는 원자적으로 실행됩니다.


## 스레드 로컬 데이터

- 스레드 로컬 데이터는 값이 스레드에만 한정되는 데이터입니다. 스레드 로컬 데이터를 관리하려면, local(또는 서브 클래스) 인스턴스를 만들고 그것에 어트리뷰트를 저장하십시오:

```python
mydata = threading.local()
mydata.x = 1
```

- 인스턴스 값은 개별 스레드마다 다릅니다.

`class threading.local`
- 스레드 로컬 데이터를 나타내는 클래스.
- 자세한 내용과 광범위한 예제는 threading_local 모듈의 문서 문자열을 참조하세요: [Lib/_threading_local.py](https://github.com/python/cpython/tree/3.12/Lib/_threading_local.py).

## Thread 객체
- Thread 클래스는 별도의 제어 스레드에서 실행되는 활동을 나타냅니다. 활동을 지정하는 방법에는 두 가지가 있습니다: 생성자에 호출 가능한 객체를 전달하거나 서브클래스에서 run() 메서드를 재정의하는 것입니다. 서브클래스에서 다른 메서드(생성자 제외)를 재정의해서는 안 됩니다. 다시 말해, 이 클래스의 __init__()과 run() 메서드만 재정의하십시오.
- 일단 스레드 객체가 만들어지면, 스레드의 start() 메서드를 호출하여 활동을 시작해야 합니다. 이것은 별도의 제어 스레드에서 run() 메서드를 호출합니다.
- 일단 스레드의 활동이 시작되면, 스레드는 '살아있는(alive)' 것으로 간주합니다. run() 메서드가 정상적으로 혹은 처리되지 않은 예외를 발생시켜서 종료할 때 살아있음을 멈춥니다. is_alive() 메서드는 스레드가 살아있는지 검사합니다.
- 다른 스레드는 스레드의 join() 메서드를 호출할 수 있습니다. 이것은 join() 메서드가 호출된 스레드가 종료될 때까지 호출하는 스레드를 블록 합니다.
- 스레드에는 이름이 있습니다. 이름은 생성자에 전달되고, name 어트리뷰트를 통해 읽거나 변경할 수 있습니다.
- run() 메서드에서 예외가 발생하면, 이를 처리하기 위해 threading.excepthook()이 호출됩니다. 기본적으로, threading.excepthook()은 SystemExit를 조용히 무시합니다.
- 스레드는 "데몬 스레드"로 플래그 할 수 있습니다. 이 플래그의 의미는 오직 데몬 스레드만 남았을 때 전체 파이썬 프로그램이 종료된다는 것입니다. 초깃값은 만드는 스레드에서 상속됩니다. 플래그는 daemon 프로퍼티나 daemon 생성자 인자를 통해 설정할 수 있습니다.

> 종료 시 데몬 스레드는 갑자기 중지됩니다. 그들의 자원(가령 열린 파일, 데이터베이스 트랜잭션 등)은 제대로 해제되지 않을 수 있습니다. 스레드가 우아하게 중지되도록 하려면, 스레드를 데몬이 아니도록 만들고 Event와 같은 적절한 신호 메커니즘을 사용하십시오.

- "메인 스레드" 객체가 있습니다; 이것은 파이썬 프로그램의 초기 제어 스레드에 해당합니다. 이것은 데몬 스레드가 아닙니다.
- "더미 스레드 객체"가 생성될 가능성이 있습니다. 이들은 threading 모듈 외부에서 시작된 "외부 스레드"에 해당하는 스레드 객체입니다(예: C 코드에서 직접). 더미 스레드 객체는 기능이 제한적입니다; 항상 살아있고 데몬으로 간주되며, join할 수 없습니다. 외부 스레드의 종료를 감지하는 것이 불가능하기 때문에 절대 삭제되지 않습니다.

`class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)`
- 이 생성자는 항상 키워드 인자로 호출해야 합니다. 인자는 다음과 같습니다:
- group은 None이어야 합니다; ThreadGroup 클래스가 구현될 때 미래의 확장을 위해 예약되어 있습니다.
- target은 run() 메서드에 의해 호출될 콜러블 객체입니다. 기본값은 None이며, 아무것도 호출되지 않습니다.
- name은 스레드 이름입니다. 기본적으로 "Thread-N" 형식의 고유한 이름이 구성됩니다. 여기서 N은 작은 십진수입니다. target 인자가 지정된 경우 "Thread-N (target)"이 됩니다. 여기서 "target"은 `target.__name__`입니다.
- args는 target 호출을 위한 인자의 리스트 또는 튜플입니다. 기본값은 ()입니다.
- kwargs는 target 호출을 위한 키워드 인자의 딕셔너리입니다. 기본값은 {}입니다.
- None이 아니면, daemon은 스레드가 데몬인지를 명시적으로 설정합니다. None(기본값)이면, 데몬 속성은 현재 스레드에서 상속됩니다.
- 서브 클래스가 생성자를 재정의하면, 스레드에 다른 작업을 수행하기 전에 베이스 클래스 생성자(Thread.__init__())를 호출해야 합니다.

> 버전 3.3에서 변경: daemon 매개변수가 추가되었습니다.
> 버전 3.10에서 변경: name 인자가 생략된 경우 target 이름을 사용합니다.

`start()`

- 스레드 활동을 시작합니다.
- 스레드 객체 당 최대 한 번 호출되어야 합니다. 객체의 run() 메서드가 별도의 제어 스레드에서 호출되도록 배치합니다.
- 이 메서드는 같은 스레드 객체에서 두 번 이상 호출되면, RuntimeError를 발생시킵니다.

`run()`
- 스레드의 활동을 표현하는 메서드.
- 서브 클래스에서 이 메서드를 재정의할 수 있습니다. 표준 run() 메서드는 target 인자로 객체의 생성자에 전달된 콜러블 객체를 호출합니다, 있다면 args와 kwargs 인자에서 각각 취한 위치와 키워드 인자로 호출합니다.
- Thread에 전달된 args 인자로 리스트나 튜플을 사용하면 같은 효과를 얻을 수 있습니다.

```python
>>> from threading import Thread
>>> t = Thread(target=print, args=[1])
>>> t.run()
1
>>> t = Thread(target=print, args=(1,))
>>> t.run()
1
```

`join(timeout=None)`
- 스레드가 종료할 때까지 기다립니다. join() 메서드가 호출된 스레드가 정상적으로 혹은 처리되지 않은 예외를 통해 종료하거나 선택적 시간제한 초과가 발생할 때까지 호출하는 스레드를 블록 합니다.
- timeout 인자가 있고 None이 아닌 경우, 초 단위(또는 그 분수)로 작업의 시간 제한을 지정하는 부동 소수점 숫자여야 합니다. join()은 항상 None을 반환하므로 시간 초과가 발생했는지 확인하려면 join() 후에 is_alive()를 호출해야 합니다 - 스레드가 여전히 살아있다면 join() 호출이 시간 초과된 것입니다.
- timeout 인자가 없거나 None이면, 스레드가 종료될 때까지 작업이 블록 됩니다.
- 스레드는 여러 번 join할 수 있습니다.
- 교착 상태를 유발할 수 있어서 현재 스레드를 조인하려고 시도하면 join()은 RuntimeError를 발생시킵니다. 스레드가 시작되기 전에 join() 하는 것도 에러이고 같은 예외가 발생합니다.

`name`
- 식별 목적으로만 사용되는 문자열. 의미는 없습니다. 여러 스레드에 같은 이름을 지정할 수 있습니다. 초기 이름은 생성자가 설정합니다.

`getName()`
`setName()`
- name에 대한 사용 중단된 getter/setter API; 대신 직접 속성으로 사용하십시오.

> 버전 3.10부터 폐지됨.

`ident`
- 이 스레드의 '스레드 식별자' 또는 스레드가 시작되지 않았으면 None. 이것은 0이 아닌 정수입니다. get_ident() 함수를 참조하십시오. 스레드 식별자는 스레드가 종료되고 다른 스레드가 만들어질 때 재활용될 수 있습니다. 스레드가 종료된 후에도 식별자를 사용할 수 있습니다.

`native_id`
- OS(커널)에 의해 할당된 이 스레드의 스레드 ID(TID)입니다. 이는 음이 아닌 정수이거나, 스레드가 시작되지 않았으면 None입니다. get_native_id() 함수를 참조하십시오. 이 값은 시스템 전체에서 이 특정 스레드를 고유하게 식별하는 데 사용될 수 있습니다(스레드가 종료될 때까지, 그 후에는 OS에 의해 값이 재사용될 수 있습니다).

> 프로세스 ID와 유사하게, 스레드 ID는 스레드가 만들어진 시점부터 스레드가 종료될 때까지만 유효(시스템 전체에서 고유함이 보장)합니다.

> 가용성: Windows, FreeBSD, Linux, macOS, OpenBSD, NetBSD, AIX, DragonFlyBSD.

> 버전 3.8에서 추가됨.

`is_alive()`
- 스레드가 살아있는지를 반환합니다.
- 이 메서드는 run() 메서드가 시작되기 직전부터 run() 메서드가 종료된 직후까지 True를 반환합니다. 모듈 함수 enumerate()는 모든 살아있는 스레드 리스트를 반환합니다.

`daemon`
- 이 스레드가 데몬 스레드인지(True) 아닌지(False)를 나타내는 부울 값입니다. 이는 start()가 호출되기 전에 설정되어야 합니다. 그렇지 않으면 RuntimeError가 발생합니다. 초기 값은 생성 스레드에서 상속됩니다; 메인 스레드는 데몬 스레드가 아니므로 메인 스레드에서 생성된 모든 스레드는 기본적으로 daemon = False입니다.
- 살아있는 데몬이 아닌 스레드가 남아 있지 않으면 전체 파이썬 프로그램이 종료됩니다.

`isDaemon()`
`setDaemon()`
- daemon에 대한 사용 중단된 getter/setter API; 대신 직접 속성으로 사용하십시오.

> 버전 3.10부터 폐지됨.

## 록 객체 (Lock objects)
- 프리미티브 록(primitive lock)은 잠겨있을 때 특정 스레드가 소유하지 않는 동기화 프리미티브입니다. 파이썬에서는 현재 [`_thread`](https://docs.python.org/ko/3/library/_thread.html#module-_thread) 확장 모듈에 의해 직접 구현되는 가장 낮은 수준의 동기화 프리미티브입니다.
- 프리미티브 록은 두 상태 중 하나입니다, "잠금(locked)"이나 "잠금 해제(unlocked)". 잠금 해제 상태로 만들어집니다. 두 가지 기본 메서드가 있습니다, [`acquire()`](https://docs.python.org/ko/3/library/threading.html#threading.Lock.acquire)와 [`release()`](https://docs.python.org/ko/3/library/threading.html#threading.Lock.release). 상태가 잠금 해제일 때, [`acquire()`](https://docs.python.org/ko/3/library/threading.html#threading.Lock.acquire)는 상태를 잠금으로 변경하고 즉시 반환합니다. 상태가 잠금일 때, [`acquire()`](https://docs.python.org/ko/3/library/threading.html#threading.Lock.acquire)는 다른 스레드에서의 [`release()`](https://docs.python.org/ko/3/library/threading.html#threading.Lock.release)에 호출이 잠금 해제로 변경할 때까지 블록 된 후, [`acquire()`](https://docs.python.org/ko/3/library/threading.html#threading.Lock.acquire) 호출이 이를 잠금으로 재설정하고 반환합니다. [`release()`](https://docs.python.org/ko/3/library/threading.html#threading.Lock.release) 메서드는 잠금 상태에서만 호출해야 합니다; 상태를 잠금 해제로 변경하고 즉시 반환합니다. 잠금 해제된 록을 해제하려고 하면, [`RuntimeError`](https://docs.python.org/ko/3/library/exceptions.html#RuntimeError)가 발생합니다.
- 록은 [컨텍스트 관리자 프로토콜](https://docs.python.org/ko/3/library/threading.html#with-locks)도 지원합니다.
- 둘 이상의 스레드가 [`acquire()`](https://docs.python.org/ko/3/library/threading.html#threading.Lock.acquire)에서 블록 되어 상태가 잠금 해제가 되기를 기다릴 때, [`release()`](https://docs.python.org/ko/3/library/threading.html#threading.Lock.release) 호출이 상태를 잠금 해제로 재설정하면 하나의 스레드만 진행됩니다; 대기 중인 스레드 중 어느 것이 진행하는지는 정의되지 않았으며, 구현에 따라 다를 수 있습니다.
- 모든 메서드는 원자 적으로 실행됩니다.

`class threading.Lock`
- 프리미티브 록 객체를 구현하는 클래스. 일단 스레드가 록을 획득하면, 이후에 해당 록을 확보하려고 시도하면 해제될 때까지 블록 합니다; 모든 스레드가 해제할 수 있습니다.
- `Lock`은 실제로는 플랫폼에서 지원하는 가장 효율적인 버전의 구상 Lock 클래스 인스턴스를 반환하는 팩토리 함수임에 유의하십시오.

`acquire(blocking=True, timeout=-1)`
- 블로킹이거나 비 블로킹으로, 록을 획득합니다.
- blocking 인자를 `True`(기본값)로 설정하여 호출하면, 록이 잠금 해제될 때까지 블록 한 다음, 잠금으로 설정하고 `True`를 반환합니다.
- blocking 인자를 `False`로 설정하여 호출하면, 블록 하지 않습니다. blocking이 `True`로 설정된 호출이 블록 될 것이라면, 즉시 `False`를 반환합니다; 그렇지 않으면, 록을 잠금으로 설정하고 `True`를 반환합니다.
- 부동 소수점 timeout 인자를 양수로 설정하여 호출하면, 지정된 시간(초) 동안 최대한 블록하며 록을 획득할 수 없을 때까지 기다립니다. timeout 인자가 `-1`이면 무제한 대기를 지정합니다. blocking이 `False`일 때 timeout을 지정하는 것은 금지됩니다.
- 록이 성공적으로 획득되면 반환 값은 `True`이고, 그렇지 않으면 (예를 들어 timeout이 만료되면) `False`입니다.

> 버전 3.2에서 변경: timeout 매개 변수가 추가되었습니다.
> 버전 3.2에서 변경: 하부 스레딩 구현이 지원한다면 POSIX에서 시그널로 록 획득을 중단할 수 있습니다.

`release()`

- 록을 해제합니다. 록을 획득한 스레드뿐만 아니라 모든 스레드에서 호출할 수 있습니다.
- 록이 잠금일 때, 잠금 해제로 재설정하고 반환합니다. 록이 잠금 해제될 때까지 다른 스레드가 블록 되어 기다리고 있으면, 그들 중 정확히 하나의 스레드가 진행되도록 합니다.
- 잠금 해제된 록에서 호출되면, [`RuntimeError`](https://docs.python.org/ko/3/library/exceptions.html#RuntimeError)가 발생합니다.
- 반환 값이 없습니다.

`locked()`

- 록이 획득되었다면 `True`를 반환합니다.

## RLock 객체 (RLock objects)

- 재진입 록(reentrant lock)은 같은 스레드에 의해 여러 번 획득될 수 있는 동기화 프리미티브입니다. 내부적으로, 프리미티브 록에서 사용하는 잠금/잠금 해제 상태에 더해 "소유하는 스레드(owning thread)"와 "재귀 수준(recursion level)" 개념을 사용합니다. 잠금 상태에서는, 어떤 스레드가 록을 소유합니다; 잠금 해제 상태에서는 아무런 스레드도 록을 소유하지 않습니다.
- 스레드는 록의 [`acquire()`](https://docs.python.org/ko/3/library/threading.html#threading.RLock.acquire) 메서드를 호출하여 잠그고, [`release()`](https://docs.python.org/ko/3/library/threading.html#threading.Lock.release) 메서드를 호출하여 잠금을 해제합니다.

> 재진입 록은 [컨텍스트 관리 프로토콜](https://docs.python.org/ko/3/library/threading.html#with-locks)을 지원하므로, 코드 블록에 대한 록의 획득과 해제를 처리하기 위해 수동으로 [`acquire()`](https://docs.python.org/ko/3/library/threading.html#threading.RLock.acquire)와 [`release()`](https://docs.python.org/ko/3/library/threading.html#threading.RLock.release)를 호출하는 대신 [`with`](https://docs.python.org/ko/3/reference/compound_stmts.html#with)를 사용하는 것이 좋습니다.

- RLock의 [`acquire()`](https://docs.python.org/ko/3/library/threading.html#threading.RLock.acquire)/[`release()`](https://docs.python.org/ko/3/library/threading.html#threading.RLock.release) 호출 쌍은 Lock의 [`acquire()`](https://docs.python.org/ko/3/library/threading.html#threading.Lock.acquire)/[`release()`](https://docs.python.org/ko/3/library/threading.html#threading.Lock.release)와 달리 중첩될 수 있습니다. 마지막 [`release()`](https://docs.python.org/ko/3/library/threading.html#threading.RLock.release)(가장 바깥쪽 쌍의 [`release()`](https://docs.python.org/ko/3/library/threading.html#threading.Lock.release))만이 록을 잠금 해제 상태로 재설정하고 [`acquire()`](https://docs.python.org/ko/3/library/threading.html#threading.RLock.acquire)에서 블록 된 다른 스레드가 진행할 수 있도록 합니다.
- [`acquire()`](https://docs.python.org/ko/3/library/threading.html#threading.RLock.acquire)/[`release()`](https://docs.python.org/ko/3/library/threading.html#threading.RLock.release)는 쌍으로 사용해야 합니다: 각 획득에는 록을 획득한 스레드에서 해제가 있어야 합니다. 록이 획득된 만큼 해제를 호출하지 않으면 교착 상태가 발생할 수 있습니다.

`class threading.RLock`
- 이 클래스는 재진입 록 객체를 구현합니다. 재진입 록은 획득한 스레드에서 해제해야 합니다. 일단 스레드가 재진입 록을 획득하면, 같은 스레드는 블록 하지 않고 다시 스레드를 획득할 수 있습니다; 스레드는 획득할 때마다 한 번씩 해제해야 합니다.
- `RLock`은 실제로는 플랫폼에서 지원하는 가장 효율적인 버전의 구상 RLock 클래스 인스턴스를 반환하는 팩토리 함수임에 유의하십시오.

`acquire(blocking=True, timeout=-1)`
- 블로킹이거나 비 블로킹으로, 록을 획득합니다.

> [RLock을 컨텍스트 관리자로 사용하기](https://docs.python.org/ko/3/library/threading.html#with-locks): 가능한 경우 수동 `acquire()`와 [`release()`](https://docs.python.org/ko/3/library/threading.html#threading.RLock.release) 호출보다 권장됩니다.

- blocking 인자를 `True`로 설정하여 호출할 때 (기본값):
	- 어떤 스레드도 록을 소유하지 않으면, 록을 획득하고 즉시 반환합니다.
	- 다른 스레드가 록을 소유하고 있으면, 록을 획득할 수 있을 때까지 또는 timeout이 양의 부동 소수점 값으로 설정된 경우 해당 시간까지 블록합니다.
	- 같은 스레드가 록을 소유하고 있으면, 록을 다시 획득하고 즉시 반환합니다. 이것이 [`Lock`](https://docs.python.org/ko/3/library/threading.html#threading.Lock)과 `RLock`의 차이점입니다; [`Lock`](https://docs.python.org/ko/3/library/threading.html#threading.Lock)은 이 경우를 이전 경우와 동일하게 처리하여 록을 획득할 수 있을 때까지 블록합니다.
- blocking 인자를 `False`로 설정하여 호출할 때:
	- 어떤 스레드도 록을 소유하지 않으면, 록을 획득하고 즉시 반환합니다.
	- 다른 스레드가 록을 소유하고 있으면, 즉시 반환합니다.
	- 같은 스레드가 록을 소유하고 있으면, 록을 다시 획득하고 즉시 반환합니다.

- 모든 경우에, 스레드가 록을 획득할 수 있었다면 `True`를 반환합니다. 스레드가 록을 획득할 수 없었다면 (즉, 블로킹하지 않거나 타임아웃에 도달했다면) `False`를 반환합니다.
- 여러 번 호출된 경우, [`release()`](https://docs.python.org/ko/3/library/threading.html#threading.RLock.release)를 같은 횟수만큼 호출하지 않으면 교착 상태가 발생할 수 있습니다. acquire/release를 직접 호출하는 대신 컨텍스트 관리자로 `RLock`을 사용하는 것을 고려하세요.

> 버전 3.2에서 변경: timeout 매개 변수가 추가되었습니다.

`release()`
- 재귀 수준을 낮추면서, 잠금을 해제합니다. 감소 후에 0이 되면, 록을 잠금 해제로 (아무런 스레드도 소유하지 않은) 재설정하고, 록이 잠금 해제되도록 기다리면서 블록 된 다른 스레드가 있으면, 그중 정확히 하나가 진행되도록 합니다. 감소 후에 재귀 수준이 여전히 0이 아니면, 록은 잠금이고, 호출하는 스레드에 의해 소유된 채로 유지됩니다.
- 호출하는 스레드가 잠금을 소유하고 있을 때만 이 메서드를 호출하세요. 잠금이 획득되지 않은 상태에서 이 메서드를 호출하면 [`RuntimeError`](https://docs.python.org/ko/3/library/exceptions.html#RuntimeError "RuntimeError")가 발생합니다.
- 반환 값이 없습니다.

## Condition 객체 (Condition objects)
- 조건 변수(condition variable)는 항상 어떤 종류의 록과 연관됩니다; 이것은 전달되거나 기본적으로 만들어집니다. 전달하는 것은 여러 조건 변수가 같은 록을 공유해야 할 때 유용합니다. 록은 조건 객체의 일부입니다: 별도로 추적할 필요가 없습니다.
- 조건 변수는 컨텍스트 관리자 프로토콜을 준수합니다: `with` 문을 사용해서 감싼 블록의 지속 시간 동안 연관된 록을 획득합니다. [acquire()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.acquire)와 [release()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.release) 메서드도 연관된 록의 해당 메서드를 호출합니다.
- 다른 메서드들은 연관된 록을 잡은 상태에서 호출해야 합니다. [wait()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.wait) 메서드는 록을 해제한 다음, 다른 스레드가 [notify()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.notify)나 [notify_all()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.notify_all)을 호출하여 록을 해제할 때까지 블록 합니다. 일단 깨어나면, [wait()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.wait)는 록을 다시 획득하고 반환합니다. 시간제한을 지정할 수도 있습니다.
- [notify()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.notify) 메서드는 있다면 조건 변수를 기다리는 스레드 중 하나를 깨웁니다. [notify_all()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.notify_all) 메서드는 조건 변수를 기다리는 모든 스레드를 깨웁니다.

> [notify()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.notify)와 [notify_all()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.notify_all) 메서드는 록을 해제하지 않습니다; 이것은 깨어난 스레드나 스레드들이 [wait()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.wait) 호출에서 즉시 반환되지 않지만, [notify()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.notify)나 [notify_all()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.notify_all)을 호출한 스레드가 최종적으로 록 소유권을 포기할 때만 반환됨을 의미합니다.

- 조건 변수를 사용하는 일반적인 프로그래밍 스타일은 록을 사용하여 어떤 공유 상태에 대한 액세스를 동기화합니다; 특정 상태 변경에 관심 있는 스레드는 원하는 상태를 볼 때까지 [wait()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.wait)를 반복적으로 호출하는 반면, 상태를 변경하는 스레드는 대기자 중 하나가 원하는 상태일 수 있도록 상태를 변경할 때 [notify()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.notify)나 [notify_all()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.notify_all)을 호출합니다. 예를 들어, 다음 코드는 무제한 버퍼 용량의 일반적인 생산자-소비자 상황입니다:

```python
# Consume one item
with cv:
    while not an_item_is_available():
        cv.wait()
    get_an_available_item()

# Produce one item
with cv:
    make_an_item_available()
    cv.notify()
```

- [wait()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.wait)가 임의의 긴 시간 후에 반환될 수 있고, [notify()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.notify) 호출을 유발한 조건이 더는 참이 아닐 수 있기 때문에, 응용 프로그램의 조건에 대한 `while` 루프 검사가 필요합니다. 이것은 다중 스레드 프로그래밍에 본질적으로 수반됩니다. [wait_for()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.wait_for) 메서드를 사용하면 조건 검사를 자동화하고 시간제한 계산을 쉽게 수행할 수 있습니다:

```python
# Consume an item
with cv:
    cv.wait_for(an_item_is_available)
    get_an_available_item()
```

- [notify()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.notify)와 [notify_all()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.notify_all) 중에서 선택하려면, 하나의 상태 변경에 흥미 있는 대기 중인 스레드가 하나일지 여러 개일지를 고려하십시오. 예를 들어 일반적인 생산자-소비자 상황에서, 하나의 항목을 버퍼에 추가하면 오직 하나의 소비자 스레드만 깨울 필요가 있습니다.

`class threading.Condition(lock=None)`

- 이 클래스는 조건 변수 객체를 구현합니다. 조건 변수를 사용하면 하나 이상의 스레드가 다른 스레드에 의해 통지될 때까지 기다릴 수 있습니다
- lock 인자가 제공되고 None이 아니면, Lock이나 RLock 객체여야 하며, 하부 록으로 사용됩니다. 그렇지 않으면, 새 RLock 객체가 만들어지고 하부 록으로 사용됩니다.

> 버전 3.3에서 변경: 팩토리 함수에서 클래스로 변경되었습니다.

`acquire(*args)`
- 하부 록을 획득합니다. 이 메서드는 하부 록에서 해당 메서드를 호출합니다; 반환 값은 그 메서드가 반환하는 것입니다.

`release()`
- 하부 록을 해제합니다. 이 메서드는 하부 록에서 해당 메서드를 호출합니다; 반환 값이 없습니다.

`wait(timeout=None)`
- 통지되거나 시간제한이 만료될 때까지 기다립니다. 이 메서드가 호출될 때 호출하는 스레드가 록을 획득하지 않았으면, RuntimeError가 발생합니다.
- 이 메서드는 하부 록을 해제한 다음, 같은 조건 변수에 대한 다른 스레드에서의 [notify()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.notify)나 [notify_all()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.notify_all) 호출에 의해 깨어날 때까지 또는 선택적 시간제한 만료가 발생할 때까지 블록 합니다. 일단 깨어나거나 시간제한이 만료되면, 록을 다시 획득하고 반환합니다.
- timeout 인자가 존재하고 None이 아닐 때, 초 단위(또는 그 일부)로 연산의 시간제한을 지정하는 부동소수점 숫자여야 합니다.
- 하부 록이 RLock일 때, 록이 여러 번 재귀적으로 획득되었을 때 록을 실제로 잠금 해제하지 못할 수 있기 때문에, [release()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.release) 메서드를 사용하여 록을 해제하지 않습니다. 대신, RLock 클래스의 내부 인터페이스가 사용되어, 재귀적으로 여러 번 획득한 경우에도 실제로 록을 잠금 해제합니다. 그런 다음 다른 내부 인터페이스를 사용하여 록을 다시 획득할 때 재귀 수준을 복원합니다.
- 주어진 timeout이 만료되지 않는 한 반환 값은 True이며, 만료되면 False입니다.

> 버전 3.2에서 변경: 이전에는, 메서드가 항상 None을 반환했습니다.

`wait_for(predicate, timeout=None)`

- 조건이 참으로 평가될 때까지 기다립니다. predicate는 불리언 값으로 해석될 결과를 반환하는 콜러블 이어야 합니다. 최대 대기 시간을 주는 timeout이 제공될 수 있습니다.
- 이 유틸리티 메서드는 술어(predicate)가 충족될 때까지, 또는 시간제한 만료가 발생할 때까지 [wait()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.wait)를 반복적으로 호출할 수 있습니다. 반환 값은 predicate의 마지막 반환 값이며 메서드가 시간제한 만료되면 False로 평가됩니다.
- 시간제한 기능을 무시할 때, 이 메서드를 호출하는 것은 대략 다음과 같이 작성하는 것과 동등합니다:

```python
while not predicate():
    cv.wait()
```

- 따라서, [wait()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.wait)와 같은 규칙이 적용됩니다: 호출될 때 록을 잡고 있어야 하며 반환할 때 다시 확보됩니다. predicate는 록을 잡고 있는 상태로 평가됩니다.

> 버전 3.2에서 추가되었습니다.

`notify(n=1)`

- 기본적으로, (있다면) 이 조건에서 대기 중인 하나의 스레드를 깨웁니다. 이 메서드가 호출될 때 호출하는 스레드가 잠금을 획득하지 않았으면 RuntimeError가 발생합니다.
- 이 메서드는 조건 변수를 기다리는 스레드를 최대 n 개 깨웁니다; 기다리는 스레드가 없으면 아무런 일도 하지 않습니다.
- 적어도 n 스레드가 대기 중이면, 현재 구현은 정확히 n 스레드를 깨웁니다. 그러나, 이 동작에 의존하는 것은 안전하지 않습니다. 미래에는, 최적화된 구현이 때때로 n 스레드보다 많이 깨울 수 있습니다.

> 깨어난 스레드는 록을 다시 획득할 때까지 [wait()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.wait) 호출에서 실제로 반환하지 않습니다. [notify()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.notify)가 록을 해제하지 않기 때문에, 호출자가 해제해야 합니다.

`notify_all()`
- 이 조건에서 대기 중인 모든 스레드를 깨웁니다. 이 메서드는 [notify()](https://docs.python.org/ko/3/library/threading.html#threading.Condition.notify)처럼 작동하지만, 하나 대신에 대기 중인 모든 스레드를 깨웁니다. 이 메서드가 호출될 때 호출하는 스레드가 잠금을 획득하지 않았으면 RuntimeError가 발생합니다.
- notifyAll 메서드는 이 메서드의 더 이상 사용되지 않는 별칭입니다.

## 세마포어 객체 (Semaphore objects)

- 이것은 일찌감치 네덜란드 컴퓨터 과학자 Edsger W. Dijkstra가 발명한, 컴퓨터 과학 역사상 가장 오래된 동기화 프리미티브 중 하나입니다 (그는 [`acquire()`](https://docs.python.org/ko/3/library/threading.html#threading.Semaphore.acquire "threading.Semaphore.acquire")와 [`release()`](https://docs.python.org/ko/3/library/threading.html#threading.Semaphore.release "threading.Semaphore.release") 대신 P()와 V()라는 이름을 사용했습니다).
- 세마포어는 각 [`acquire()`](https://docs.python.org/ko/3/library/threading.html#threading.Semaphore.acquire "threading.Semaphore.acquire") 호출에 의해 감소하고 각 [`release()`](https://docs.python.org/ko/3/library/threading.html#threading.Semaphore.release "threading.Semaphore.release") 호출에 의해 증가하는 내부 카운터를 관리합니다. 카운터는 절대 0 밑으로 떨어질 수 없습니다; [`acquire()`](https://docs.python.org/ko/3/library/threading.html#threading.Semaphore.acquire "threading.Semaphore.acquire")가 0임을 발견하면, 다른 스레드가 [`release()`](https://docs.python.org/ko/3/library/threading.html#threading.Semaphore.release "threading.Semaphore.release")를 호출할 때까지 대기하면서 블록 합니다.
- 세마포어도 [컨텍스트 관리자 프로토콜](https://docs.python.org/ko/3/library/threading.html#with-locks)을 지원합니다.

`class threading.Semaphore(value=1)`
- 이 클래스는 세마포어 객체를 구현합니다. 세마포어는 [`release()`](https://docs.python.org/ko/3/library/threading.html#threading.Semaphore.release "threading.Semaphore.release") 호출 수에서 [`acquire()`](https://docs.python.org/ko/3/library/threading.html#threading.Semaphore.acquire "threading.Semaphore.acquire") 호출 수를 빼고, 초깃값을 더한 원자 적 카운터를 관리합니다. [`acquire()`](https://docs.python.org/ko/3/library/threading.html#threading.Semaphore.acquire "threading.Semaphore.acquire") 메서드는 카운터를 음수로 만들지 않고 반환할 수 있을 때까지 필요하면 블록 합니다. 지정하지 않으면, value의 기본값은 1입니다.
- 선택적 인자는 내부 카운터의 초깃 value(value)을 제공합니다; 기본값은 1입니다. 주어진 value가 0보다 작으면 [`ValueError`](https://docs.python.org/ko/3/library/exceptions.html#ValueError "ValueError")가 발생합니다.

> 버전 3.3에서 변경: 팩토리 함수에서 클래스로 변경되었습니다.

`acquire(blocking=True, timeout=None)`

- 세마포어를 획득합니다.
- 인자 없이 호출될 때:
	- 진입 시 내부 카운터가 0보다 크면, 1 감소시키고 즉시 True를 반환합니다.
	- 진입 시 내부 카운터가 0이면, [`release()`](https://docs.python.org/ko/3/library/threading.html#threading.Semaphore.release "threading.Semaphore.release")를 호출하여 깨울 때까지 블록 합니다. 일단 깨어나면 (그리고 카운터가 0보다 크면), 카운터를 1줄이고 True를 반환합니다. [`release()`](https://docs.python.org/ko/3/library/threading.html#threading.Semaphore.release "threading.Semaphore.release")를 호출할 때마다 정확히 하나의 스레드가 깨어납니다. 스레드가 깨어나는 순서에 의존해서는 안 됩니다.
- blocking을 False로 설정하여 호출하면 블록하지 않습니다. 인수 없이 호출했을 때 블록될 경우 즉시 False를 반환합니다. 그렇지 않으면 인수 없이 호출했을 때와 동일한 작업을 수행하고 True를 반환합니다.
- None 이외의 timeout으로 호출하면, 최대 timeout 초 동안 블록 합니다. 그 기간 획득이 완료되지 않으면, False를 반환합니다. 그렇지 않으면 True를 반환합니다.

> 버전 3.2에서 변경: timeout 매개 변수가 추가되었습니다.

`release(n=1)`
- 내부 카운터를 n 증가시키면서 세마포어를 해제합니다. 진입 시 0이고 다른 스레드가 다시 0보다 커지기를 기다리고 있으면, 해당 스레드를 n개 깨웁니다.

> 버전 3.9에서 변경: 여러 대기 스레드를 한 번에 해제하기 위해 n 매개 변수를 추가했습니다.

`class threading.BoundedSemaphore(value=1)`

- 경계 세마포어 객체를 구현하는 클래스. 경계 세마포어는 현재 값이 초깃값을 초과하지 않는지 확인합니다. 그렇다면, [`ValueError`](https://docs.python.org/ko/3/library/exceptions.html#ValueError "ValueError")가 발생합니다. 대부분은 세마포어는 제한된 용량의 자원을 보호하는 데 사용됩니다. 세마포어가 너무 여러 번 해제되면 버그의 징조입니다. 지정하지 않으면, value의 기본값은 1입니다.

> 버전 3.3에서 변경: 팩토리 함수에서 클래스로 변경되었습니다.

### [`Semaphore`](https://docs.python.org/ko/3/library/threading.html#threading.Semaphore "threading.Semaphore") 예제 (Semaphore Example)
- 세마포어는 예를 들어 데이터베이스 서버와 같이 제한된 용량의 자원을 보호하는 데 종종 사용됩니다. 자원의 크기가 고정된 상황에서는, 경계 세마포어를 사용해야 합니다. 작업자 스레드를 만들기 전에, 메인 스레드가 세마포어를 초기화합니다:

```python
maxconnections = 5
# …
pool_sema = BoundedSemaphore(value=maxconnections)
```

- 일단 만들어지면, 작업자 스레드는 서버에 연결해야 할 때 세마포어의 acquire 및 release 메서드를 호출합니다:

```python
with pool_sema:
    conn = connectdb()
    try:
        # … use connection …
    finally:
        conn.close()
```

- 경계 세마포어를 사용하면 세마포어가 획득한 것보다 더 많이 해제되는 프로그래밍 에러가 감지되지 않을 가능성이 줄어듭니다.

## 이벤트 객체 (Event objects)
- 이것은 스레드 간 통신을 위한 가장 간단한 메커니즘 중 하나입니다: 하나의 스레드는 이벤트를 알리고 다른 스레드는 이를 기다립니다.
- 이벤트 객체는 [`set()`](https://docs.python.org/ko/3/library/threading.html#threading.Event.set "threading.Event.set") 메서드를 사용하여 참으로 설정하고 [`clear()`](https://docs.python.org/ko/3/library/threading.html#threading.Event.clear "threading.Event.clear") 메서드를 사용하여 거짓으로 재설정 할 수 있는 내부 플래그를 관리합니다. [`wait()`](https://docs.python.org/ko/3/library/threading.html#threading.Event.wait "threading.Event.wait") 메서드는 플래그가 참이 될 때까지 블록 합니다.

`class threading.Event`
- 이벤트 객체를 구현하는 클래스. 이벤트는 [`set()`](https://docs.python.org/ko/3/library/threading.html#threading.Event.set "threading.Event.set") 메서드로 참으로 설정하고 [`clear()`](https://docs.python.org/ko/3/library/threading.html#threading.Event.clear "threading.Event.clear") 메서드로 거짓으로 재설정 할 수 있는 플래그를 관리합니다. [`wait()`](https://docs.python.org/ko/3/library/threading.html#threading.Event.wait "threading.Event.wait") 메서드는 플래그가 참이 될 때까지 블록 합니다. 플래그는 처음에는 거짓입니다.

> 버전 3.3에서 변경: 팩토리 함수에서 클래스로 변경되었습니다.

`is_set()`

- 내부 플래그가 참이면 그리고 오직 그때만 True를 반환합니다.
- isSet 메서드는 이 메서드의 더 이상 사용되지 않는 별칭입니다.

`set()`

- 내부 플래그를 참으로 설정합니다. 이것이 참이 되기를 기다리는 모든 스레드가 깨어납니다. 일단 플래그가 참이면 [`wait()`](https://docs.python.org/ko/3/library/threading.html#threading.Event.wait "threading.Event.wait")를 호출하는 스레드는 전혀 블록 하지 않습니다.

`clear()`
- 내부 플래그를 거짓으로 재설정합니다. 이후 [`wait()`](https://docs.python.org/ko/3/library/threading.html#threading.Event.wait "threading.Event.wait")를 호출하는 스레드는 내부 플래그를 다시 참으로 설정하기 위해 [`set()`](https://docs.python.org/ko/3/library/threading.html#threading.Event.set "threading.Event.set")을 호출할 때까지 블록 합니다.

`wait(timeout=None)`
- 내부 플래그가 거짓이고 주어진 타임아웃이 만료되지 않은 한 블록합니다. 이 블록킹 메서드가 반환된 이유를 나타내는 반환 값; 내부 플래그가 참으로 설정되어 반환되는 경우 True, 또는 타임아웃이 주어지고 주어진 대기 시간 내에 내부 플래그가 참이 되지 않은 경우 False.
- 타임아웃 인수가 있고 None이 아닌 경우, 초 단위 또는 그 일부로 작업의 타임아웃을 지정하는 부동 소수점 숫자여야 합니다.

> 버전 3.1에서 변경: 이전에는, 메서드가 항상 None을 반환했습니다.

## 타이머 객체 (Timer objects)

- 이 클래스는 특정 시간이 지난 후에만 실행되어야 하는 조치를 나타냅니다 – 타이머. [`Timer`](https://docs.python.org/ko/3/library/threading.html#threading.Timer "threading.Timer")는 [`Thread`](https://docs.python.org/ko/3/library/threading.html#threading.Thread "threading.Thread")의 서브 클래스이며 사용자 정의 스레드를 만드는 예제로도 기능합니다.
- 타이머는 스레드와 마찬가지로 [`Timer.start`](https://docs.python.org/ko/3/library/threading.html#threading.Thread.start "threading.Thread.start") 메서드를 호출하여 시작됩니다. 타이머는 (동작이 시작되기 전에) [`cancel()`](https://docs.python.org/ko/3/library/threading.html#threading.Timer.cancel "threading.Timer.cancel") 메서드를 호출하여 중지할 수 있습니다. 타이머가 동작을 실행하기 전에 기다리는 간격은 사용자가 지정한 간격과 정확히 일치하지 않을 수 있습니다.

예를 들면:

```python
def hello():
    print("hello, world")

t = Timer(30.0, hello)
t.start()  # 30초 후에 "hello, world"가 출력됩니다
```

`class threading.Timer(interval, function, args=None, kwargs=None)`
- interval 초가 지난 후 args 인자와 kwargs 키워드 인자로 function을 실행하는 타이머를 만듭니다. args가 None(기본값)이면 빈 리스트가 사용됩니다. kwargs가 None(기본값)이면 빈 딕셔너리가 사용됩니다.
> 버전 3.3에서 변경: 팩토리 함수에서 클래스로 변경되었습니다.

`cancel()`
- 타이머를 중지하고, 타이머 조치의 실행을 취소합니다. 타이머가 아직 대기 상태에 있을 때만 작동합니다.

## Barrier 객체

> 버전 3.2에 추가.

- 이 클래스는 서로를 기다려야 하는 고정된 수의 스레드에서 사용할 수 있는 간단한 동기화 프리미티브를 제공합니다. 각 스레드는 [`wait()`](https://docs.python.org/ko/3/library/threading.html#threading.Barrier.wait) 메서드를 호출하여 장벽(barrier)을 통과하려고 시도하고 모든 스레드가 [`wait()`](https://docs.python.org/ko/3/library/threading.html#threading.Barrier.wait) 호출을 수행할 때까지 블록 합니다. 이 시점에서, 스레드가 동시에 해제됩니다.
- 장벽은 같은 수의 스레드에 대해 여러 번 재사용 할 수 있습니다.
- 예를 들어, 다음은 클라이언트와 서버 스레드를 동기화하는 간단한 방법입니다:

```python
b = Barrier(2, timeout=5)

def server():
    start_server()
    b.wait()
    while True:
        connection = accept_connection()
        process_server_connection(connection)

def client():
    b.wait()
    while True:
        connection = make_connection()
        process_client_connection(connection)
```

`class threading.Barrier(parties, action=None, timeout=None)`

- parties 수의 스레드에 대한 장벽 객체를 만듭니다. 제공되면, action은 해제될 때 스레드 중 하나가 호출할 콜러블입니다. timeout은 wait() 메서드에 대해 지정되지 않을 때 사용될 기본 시간제한 값입니다.

`wait(timeout=None)`

- 장벽을 통과합니다. 장벽에 속한 모든 스레드가 이 함수를 호출할 때, 모두 동시에 해제됩니다. timeout이 제공되면, 클래스 생성자에 제공된 것보다 우선하여 사용됩니다.
- 반환 값은 0에서 parties - 1 범위의 정수이며, 스레드마다 다릅니다. 이것은 특별한 하우스키핑을 수행할 스레드를 선택하는데 사용될 수 있습니다, 예를 들어:

```python
i = barrier.wait()
if i == 0:
    # Only one thread needs to print this
    print("passed the barrier")
```

- 생성자에 action이 제공되면, 스레드 중 하나가 해제되기 전에 호출합니다. 이 호출로 에러가 발생하면, 장벽은 망가진 상태가 됩니다.
- 호출 시간제한이 만료되면, 장벽은 망가진 상태가 됩니다.
- 스레드가 기다리는 동안 장벽이 망가지거나 재설정되면 이 메서드는 BrokenBarrierError 예외를 발생시킬 수 있습니다.

`reset()`

- 장벽을 기본의 빈 상태로 되돌립니다. 대기 중인 모든 스레드는 BrokenBarrierError 예외를 수신합니다.
- 상태를 알 수 없는 다른 스레드가 있을 때 이 함수를 사용하려면 외부 동기화가 필요할 수 있습니다. 장벽이 망가지면 그냥 두고 새 장벽을 만드는 것이 좋습니다.

`abort()`
- 장벽을 망가진 상태로 보냅니다. 이로 인해 wait()에 대한 활성 또는 미래의 호출이 BrokenBarrierError로 실패합니다. 예를 들어 응용 프로그램의 교착 상태를 피하고자 스레드 중 하나를 중단해야 할 때 이를 사용하십시오.
- 스레드 중 하나가 잘못되는 것을 막기 위해 단순히 적절한 timeout 값으로 장벽을 만드는 것이 바람직 할 수 있습니다.

`parties`
- 장벽을 통과하는 데 필요한 스레드 수.

`n_waiting`
- 현재 장벽에서 대기 중인 스레드 수.

`broken`
- 장벽이 망가진 상태이면 True인 불리언.

`exception threading.BrokenBarrierError`
- RuntimeError의 서브 클래스인, 이 예외는 Barrier 객체가 재설정되거나 망가질 때 발생합니다.

## with 문으로 록, 조건 및 세마포어 사용하기
- 이 모듈에서 제공하는 acquire와 release 메서드가 있는 모든 객체는 with 문의 컨텍스트 관리자로 사용할 수 있습니다. 블록에 진입할 때 acquire 메서드가 호출되고, 블록을 빠져나올 때 release가 호출됩니다. 따라서 다음 코드 조각은:

```python
with some_lock:
    # do something…
```

다음과 동등합니다:

```python
some_lock.acquire()
try:
    # do something…
finally:
    some_lock.release()
```

- 현재 Lock, RLock, Condition, Semaphore 및 BoundedSemaphore 객체는 with 문 컨텍스트 관리자로 사용될 수 있습니다.

---
## 참조

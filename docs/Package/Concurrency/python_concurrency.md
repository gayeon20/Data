---
title: "[Python] 동시 실행 (Concurrency)"
excerpt: 
categories:
  - Python
tags:
  - Python
  - Python-Library
  - Concurrency
last_modified_at: 2024-04-11T15:11:34+09:00
link: https://docs.python.org/ko/3/library/asyncio.html
상위 항목: "[[python_library|파이썬 라이브러리 (Python Library)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

**하위 항목**
- [[python_multiprocessing|파이썬 멀티 프로세싱 (Python Multiprocessing)]]
- [[python_threading|파이썬 쓰레딩 (Python Threading)]]

---

- [`threading` — Thread-based parallelism](https://docs.python.org/ko/3/library/threading.html)
- [`multiprocessing` — Process-based parallelism](https://docs.python.org/ko/3/library/multiprocessing.html)
- [`concurrent.futures` — Launching parallel tasks](https://docs.python.org/ko/3/library/concurrent.futures.html)
- [`subprocess` — Subprocess management](https://docs.python.org/ko/3/library/subprocess.html)
- [`contextvars` — Context Variables](https://docs.python.org/ko/3/library/contextvars.html)

## [큐 (Queue)](https://docs.python.org/ko/3/library/queue.html)
- queue 모듈은 다중 생산자, 다중 소비자 큐를 구현합니다. 정보가 여러 스레드 간에 안전하게 교환되어야 할 때 스레드 프로그래밍에서 특히 유용합니다. 이 모듈의 Queue 클래스는 필요한 모든 로킹 개념을 구현합니다.
- 이 모듈은 항목을 검색하는 순서만 다른 세 가지 유형의 큐를 구현합니다. FIFO 큐에서는 가장 먼저 추가된 작업이 가장 먼저 검색됩니다. LIFO 큐에서는 가장 최근에 추가된 항목이 가장 먼저 검색됩니다(스택처럼 작동). 우선순위 큐에서는 항목이 정렬된 상태로 유지되며(heapq 모듈 사용) 가장 낮은 값의 항목이 가장 먼저 검색됩니다.
- 내부적으로, 이러한 3가지 유형의 큐는 록을 사용하여 경쟁 스레드를 일시적으로 블록합니다; 그러나, 스레드 내에서의 재진입을 처리하도록 설계되지는 않았습니다.
- 또한, 이 모듈은 "간단한" FIFO 큐 유형인 SimpleQueue를 구현합니다. 이 특정 구현은 작은 기능을 포기하는 대신 추가 보장을 제공합니다.
- queue 모듈은 다음 클래스와 예외를 정의합니다:

`class queue.Queue(maxsize=0)`
- FIFO 큐의 생성자. maxsize는 큐에 배치할 수 있는 항목 수에 대한 상한을 설정하는 정수입니다. 일단, 이 크기에 도달하면, 큐 항목이 소비될 때까지 삽입이 블록 됩니다. maxsize가 0보다 작거나 같으면, 큐 크기는 무한합니다.

`class queue.LifoQueue(maxsize=0)`
- LIFO 큐의 생성자. maxsize는 큐에 배치할 수 있는 항목 수에 대한 상한을 설정하는 정수입니다. 일단, 이 크기에 도달하면, 큐 항목이 소비될 때까지 삽입이 블록 됩니다. maxsize가 0보다 작거나 같으면, 큐 크기는 무한합니다.

`class queue.PriorityQueue(maxsize=0)`
- 우선순위 큐의 생성자. maxsize는 큐에 배치할 수 있는 항목 수에 대한 상한을 설정하는 정수입니다. 일단, 이 크기에 도달하면, 큐 항목이 소비될 때까지 삽입이 블록 됩니다. maxsize가 0보다 작거나 같으면, 큐 크기는 무한합니다.
- 가장 낮은 값의 항목이 가장 먼저 검색됩니다(가장 낮은 값의 항목은 min(entries)가 반환할 항목입니다). 항목의 일반적인 패턴은 (priority_number, data) 형식의 튜플입니다.
- data 요소를 비교할 수 없으면, 데이터는 데이터 항목을 무시하고 우선순위 숫자만 비교하는 클래스로 감쌀 수 있습니다:

```python
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)
```

`class queue.SimpleQueue`
- 상한 없는 FIFO 큐의 생성자. 단순 큐에는 작업 추적과 같은 고급 기능이 없습니다.

> 버전 3.7에 추가되었습니다.

`exception queue.Empty`
- 비 블로킹 get()(또는 get_nowait())이 비어있는 Queue 객체에 호출될 때 발생하는 예외.

`exception queue.Full`
- 비 블로킹 put()(또는 put_nowait())이 가득 찬 Queue 객체에 호출될 때 발생하는 예외.

### 큐 객체 (Queue objects)
- 큐 객체(Queue, LifoQueue 또는 PriorityQueue)는 아래에 설명된 공용 메서드를 제공합니다.

`Queue.qsize()`
- 큐의 대략의 크기를 돌려줍니다. 주의하십시오, qsize() > 0 은 후속 get()이 블록 되지 않는다는 것을 보장하지 않으며, qsize() < maxsize 도 put()이 블록 되지 않는다고 보장하지 않습니다.

`Queue.empty()`
- 큐가 비어 있으면 True를, 그렇지 않으면 False를 반환합니다. empty()가 True를 반환하면, put()에 대한 후속 호출이 블록 되지 않는다고 보장하는 것은 아닙니다. 마찬가지로 empty()가 False를 반환하면, get()에 대한 후속 호출이 블록 되지 않는다고 보장하는 것은 아닙니다.

`Queue.full()`
- 큐가 가득 차면 True를, 그렇지 않으면 False를 반환합니다. full()이 True를 반환하면, get()에 대한 후속 호출이 블록 되지 않는다고 보장하는 것은 아닙니다. 마찬가지로 full()이 False를 반환하면, put()에 대한 후속 호출이 블록 되지 않는다고 보장하는 것은 아닙니다.

`Queue.put(item, block=True, timeout=None)`
- 큐에 item을 넣습니다. 선택적 인자 block이 true이고 timeout이 None(기본값)이면, 사용 가능한 빈 슬롯이 생길 때까지 필요하면 블록합니다. timeout이 양수이면, 최대 timeout 초 동안 블록하고 그 시간 내에 사용 가능한 빈 슬롯이 없으면 Full 예외를 발생시킵니다. 그렇지 않으면(block이 false), 즉시 사용 가능한 빈 슬롯이 있으면 항목을 큐에 넣고, 그렇지 않으면 Full 예외를 발생시킵니다(이 경우 timeout은 무시됩니다).

`Queue.put_nowait(item)`
- `put(item, block=False)`와 동등합니다.

`Queue.get(block=True, timeout=None)`
- 큐에서 항목을 제거하고 반환합니다. 선택적 인자 block이 참이고 timeout이 None(기본값)이면, 항목이 사용 가능할 때까지 필요하면 블록합니다. timeout이 양수면, 최대 timeout 초 동안 블록하고 그 시간 내에 사용 가능한 항목이 없으면 Empty 예외가 발생합니다. 그렇지 않으면 (block이 거짓), 즉시 사용할 수 있는 항목이 있으면 반환하고, 그렇지 않으면 Empty 예외를 발생시킵니다 (이때 timeout은 무시됩니다).
- 3.0 이전의 POSIX 시스템과 Windows의 모든 버전에서, block이 true이고 timeout이 None이면, 이 작업은 기본 락에 대해 중단할 수 없는 대기 상태로 들어갑니다. 이는 예외가 발생할 수 없으며, 특히 SIGINT가 KeyboardInterrupt를 트리거하지 않는다는 것을 의미합니다.

`Queue.get_nowait()`
- get(False)와 동등합니다.


큐에 넣은 작업이 데몬 소비자 스레드에 의해 완전히 처리되었는지를 추적하는 것을 지원하는 두 가지 메서드가 제공됩니다.


`Queue.task_done()`
- 앞서 큐에 넣은 작업이 완료되었음을 나타냅니다. 큐 소비자 스레드에서 사용됩니다. 작업을 꺼내는 데 사용되는 get()마다, 후속 task_done() 호출은 작업에 대한 처리가 완료되었음을 큐에 알려줍니다.
- join()이 현재 블로킹 중이면, 모든 항목이 처리되면 (큐로 put() 된 모든 항목에 대해 task_done() 호출이 수신되었음을 뜻합니다) 재개됩니다.
- 큐에 있는 항목보다 더 많이 호출되면 ValueError를 발생시킵니다.

`Queue.join()`
- 큐의 모든 항목을 꺼내서 처리할 때까지 블록합니다.
- 미완료 작업의 수는 큐에 항목이 추가될 때마다 증가합니다. 소비자 스레드가 항목을 검색하고 모든 작업이 완료되었음을 나타내기 위해 task_done()을 호출할 때마다 수가 감소합니다. 미완료 작업의 수가 0으로 떨어지면 join()의 블록이 해제됩니다.

큐에 포함된 작업이 완료될 때까지 대기하는 방법의 예:

```python
import threading
import queue

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()

# Turn-on the worker thread.
threading.Thread(target=worker, daemon=True).start()

# Send thirty task requests to the worker.
for item in range(30):
    q.put(item)

# Block until all tasks are done.
q.join()
print('All work completed')
```

### SimpleQueue 객체 (SimpleQueue objects)
- SimpleQueue 객체는 아래에서 설명하는 공용 메서드를 제공합니다.

`SimpleQueue.qsize()`
- 큐의 대략의 크기를 돌려줍니다. 주의하십시오, qsize() > 0 은 후속 get()이 블록 되지 않는다는 것을 보장하지 않습니다.

`SimpleQueue.empty()`
- 큐가 비어 있으면 True를, 그렇지 않으면 False를 반환합니다. empty()가 False를 반환해도 후속 get() 호출이 블록되지 않는다는 보장은 없습니다.

`SimpleQueue.put(item, block=True, timeout=None)`
- item을 큐에 넣습니다. 이 메서드는 결코 블록하지 않고 항상 성공합니다 (메모리 할당 실패와 같은 잠재적 저수준 에러 제외). 선택적 인자 block과 timeout은 무시되고 Queue.put()과의 호환성을 위해서만 제공됩니다.

> CPython 구현 상세: 이 메서드는 재진입 가능한 C 구현을 가지고 있습니다. 즉, put() 또는 get() 호출은 동일한 스레드의 다른 put() 호출에 의해 데드락이나 큐 내부 상태 손상 없이 중단될 수 있습니다. 이는 __del__ 메서드나 weakref 콜백과 같은 소멸자에서 사용하기에 적합합니다.

`SimpleQueue.put_nowait(item)`
- put(item, block=False)와 동등하며, Queue.put_nowait()와의 호환성을 위해 제공됩니다.

`SimpleQueue.get(block=True, timeout=None)`
- 큐에서 항목을 제거하고 반환합니다. 선택적 인자 block이 참이고 timeout이 None(기본값)이면, 항목이 사용 가능할 때까지 필요하면 블록합니다. timeout이 양수면, 최대 timeout 초 동안 블록하고 그 시간 내에 사용 가능한 항목이 없으면 Empty 예외가 발생합니다. 그렇지 않으면 (block이 거짓), 즉시 사용할 수 있는 항목이 있으면 반환하고, 그렇지 않으면 Empty 예외를 발생시킵니다 (이때 timeout은 무시됩니다).

`SimpleQueue.get_nowait()`
- get(False)와 동등합니다.

> [!seealso] 
> - multiprocessing.Queue 클래스: (다중 스레드 대신) 다중 프로세스 문맥에서 사용하기 위한 큐 클래스.
> - collections.deque는 록을 필요로하지 않고 인덱싱을 지원하는 빠른 원자적 append()와 popleft() 연산을 제공하는 크기 제한 없는 큐의 대체 구현입니다.



## [[python_threading|쓰레딩 (Threading)]]
- 이 모듈은 하위 수준 [`_thread`] 모듈 위에 상위 수준 스레딩 인터페이스를 구성합니다.
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

## [[python_multiprocessing|멀티 프로세싱 (Multiprocessing)]]
- 이 모듈은 WebAssembly 플랫폼 `wasm32-emscripten` 및 `wasm32-wasi`에서 작동하지 않거나 사용할 수 없습니다. 자세한 내용은 WebAssembly 플랫폼을 참조하세요.
- multiprocessing은 threading 모듈과 유사한 API를 사용하여 프로세스를 생성하는 것을 지원하는 패키지입니다. multiprocessing 패키지는 스레드 대신 서브프로세스를 사용하여 전역 인터프리터 잠금을 효과적으로 우회함으로써 로컬 및 원격 동시성을 모두 제공합니다. 이로 인해 multiprocessing 모듈을 사용하면 프로그래머가 주어진 기계의 여러 프로세서를 완전히 활용할 수 있습니다. POSIX와 Windows 모두에서 작동합니다.
- multiprocessing 모듈은 threading 모듈에 대응물이 없는 API도 제공합니다. 이것의 대표적인 예가 Pool 객체입니다. 이 객체는 여러 입력 값에 걸쳐 함수의 실행을 병렬 처리하고 입력 데이터를 프로세스에 분산시키는 편리한 방법을 제공합니다(데이터 병렬 처리). 다음 예제는 자식 프로세스가 해당 모듈을 성공적으로 임포트 할 수 있도록, 모듈에서 이러한 함수를 정의하는 일반적인 방법을 보여줍니다. 다음은 Pool을 사용하는 데이터 병렬 처리의 기본 예제입니다:

```python
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
```

표준 출력으로 다음과 같은 것을 인쇄합니다

```
[1, 4, 9]
```

### Async과 MultiProcessing
- **Multiprocessing**은 여러 CPU 코어를 활용하여 병렬 처리를 수행하며, CPU 집약적인 작업에 적합합니다.
- **Asyncio**는 단일 스레드 내에서 비동기 I/O 작업을 효율적으로 처리하며, I/O 집약적인 작업에 적합합니다

#### Multiprocessing

- **목적**: 여러 CPU 코어를 활용하여 병렬 처리를 수행합니다.
- **사용 사례**: CPU 집약적인 작업에 적합합니다. 예를 들어, 복잡한 수학 계산, 데이터 분석, 이미지 처리 등.
- **작동 방식**: 각 프로세스는 독립된 메모리 공간을 가지며, 여러 프로세스를 생성하여 작업을 병렬로 처리합니다.
- **장점**:
    - GIL(Global Interpreter Lock)의 제약을 받지 않습니다.
    - 각 프로세스가 독립적이므로, 한 프로세스의 오류가 다른 프로세스에 영향을 미치지 않습니다.
- **단점**:
    - 프로세스 간 통신이 비교적 복잡하고 비용이 많이 듭니다.
    - 메모리 사용량이 많아질 수 있습니다.

#### Asyncio

- **목적**: 비동기 I/O 작업을 효율적으로 처리합니다.
- **사용 사례**: I/O 집약적인 작업에 적합합니다. 예를 들어, 네트워크 요청, 파일 읽기/쓰기, 데이터베이스 쿼리 등.
- **작동 방식**: 단일 스레드 내에서 이벤트 루프와 코루틴을 사용하여 비동기적으로 작업을 처리합니다.
- **장점**:
    - 메모리와 리소스 사용이 효율적입니다.
    - 코드가 간결하고 이해하기 쉬운 경우가 많습니다.
- **단점**:
    - CPU 집약적인 작업에는 적합하지 않습니다.
    - GIL의 제약을 받습니다.




## [`sched` - 스케줄러 (Scheduler)](https://docs.python.org/ko/3/library/sched.html)
- [`sched`](https://docs.python.org/ko/3/library/sched.html#module-sched "sched: General purpose event scheduler.") 모듈은 범용 이벤트 스케줄러를 구현하는 클래스를 정의합니다:

`class sched.scheduler(timefunc=time.monotonic, delayfunc=time.sleep)`
- scheduler 클래스는 이벤트 스케줄링을 위한 일반적인 인터페이스를 정의합니다. "외부 세계"를 실제로 다루기 위해 두 개의 함수를 요구합니다 — timefunc는 인자 없이 호출할 수 있어야 하고, 숫자(단위가 무엇이든, "시간")를 반환합니다. delayfunc 함수는 하나의 인자로 호출 가능해야 하며, timefunc의 출력과 호환되어야 하고, 그 시간 동안 지연시켜야 합니다. delayfunc는 다중 스레드 응용 프로그램에서 다른 스레드가 실행할 기회를 주기 위해 각 이벤트가 실행된 후 0 인자로 호출되기도 합니다.

> 버전 3.3에서 변경: timefunc 와 delayfunc 매개 변수는 선택적입니다.
> 버전 3.3에서 변경: scheduler 클래스는 다중 스레드 환경에서 안전하게 사용할 수 있습니다.

예제:

```python
>>> import sched, time
>>> s = sched.scheduler(time.time, time.sleep)
>>> def print_time(a='default'):
…     print("From print_time", time.time(), a)
…
>>> def print_some_times():
…     print(time.time())
…     s.enter(10, 1, print_time)
…     s.enter(5, 2, print_time, argument=('positional',))
…     # despite having higher priority, 'keyword' runs after 'positional' as enter() is relative
…     s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
…     s.enterabs(1_650_000_000, 10, print_time, argument=("first enterabs",))
…     s.enterabs(1_650_000_000, 5, print_time, argument=("second enterabs",))
…     s.run()
…     print(time.time())
…
>>> print_some_times()
1652342830.3640375
From print_time 1652342830.3642538 second enterabs
From print_time 1652342830.3643398 first enterabs
From print_time 1652342835.3694863 positional
From print_time 1652342835.3696074 keyword
From print_time 1652342840.369612 default
1652342840.3697174
```

### 스케줄러 객체

- scheduler 인스턴스에는 다음과 같은 메서드와 어트리뷰트가 있습니다:

`scheduler.enterabs(time, priority, action, argument=(), kwargs={})`
- 새 이벤트를 예약합니다. time 인자는 생성자에 전달된 timefunc 함수의 반환 값과 호환되는 숫자 형이어야 합니다. 같은 time으로 예약된 이벤트는 priority 순으로 실행됩니다. 낮은 숫자는 높은 우선순위를 나타냅니다.
- 이벤트를 실행하는 것은 `action(*argument, **kwargs)`를 실행하는 것을 의미합니다. argument는 action에 대한 위치 인자가 들어있는 시퀀스입니다. kwargs는 action에 대한 키워드 인자가 들어있는 딕셔너리입니다.
- 반환 값은 나중에 이벤트를 취소하는 데 사용할 수 있는 이벤트입니다 (cancel() 참조).

> 버전 3.3에서 변경: argument 매개 변수는 선택적입니다.
> 버전 3.3에서 변경: kwargs 매개 변수가 추가되었습니다.

`scheduler.enter(delay, priority, action, argument=(), kwargs={})`

- delay 시간 단위 후로 이벤트를 예약합니다. 상대 시간 이외의 다른 인자, 효과 및 반환 값은 enterabs()와 같습니다.

> 버전 3.3에서 변경: argument 매개 변수는 선택적입니다.
> 버전 3.3에서 변경: kwargs 매개 변수가 추가되었습니다.

`scheduler.cancel(event)`

- 큐에서 이벤트를 제거합니다. event가 현재 큐에 없으면, 이 메서드는 ValueError를 발생시킵니다.

`scheduler.empty()`

- 이벤트 큐가 비어있으면 True를 반환합니다.

`scheduler.run(blocking=True)`

- 모든 예약된 이벤트를 실행합니다. 이 메서드는 (생성자에 전달된 delayfunc 함수를 사용하여) 다음 이벤트를 기다린 다음 실행하고, 더 이상 예약된 이벤트가 없을 때까지 이를 반복합니다.
- blocking이 거짓이면 시간이 도래한 (있다면) 예약된 이벤트를 모두 실행한 다음, 스케줄러에서 다음 예약된 호출까지의 (있다면) 대기시간을 반환합니다 .
- action 이나 delayfunc는 예외를 발생시킬 수 있습니다. 두 경우 모두, 스케줄러는 일관된 상태를 유지하고 예외를 전파합니다. action에 의해 예외가 발생하면, 이후에 run()을 호출할 때 이벤트를 실행하려고 하지 않습니다.
- 일련의 이벤트가 다음 이벤트 이전에 사용 가능한 시간보다 실행하는 데 더 오래 걸리면, 스케줄러는 단순히 지연됩니다. 어떤 이벤트도 삭제되지 않습니다; 더는 적절하지 않은 이벤트를 취소할 책임은 호출 코드에 있습니다.

> 버전 3.3에서 변경: blocking 매개 변수가 추가되었습니다.

`scheduler.queue`
- 남은 이벤트의 리스트를 실행될 순서대로 반환하는 읽기 전용 어트리뷰트입니다. 각 이벤트는 다음과 같은 필드를 갖는 네임드 튜플로 표시됩니다: time, priority, action, argument, kwargs.



---
## 참조

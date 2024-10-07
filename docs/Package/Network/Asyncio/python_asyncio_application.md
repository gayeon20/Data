---
title: "[Python] 비동기 입출력 - 응용 프로그램 (Asyncio - Application)"
excerpt: asyncio는 async/await 구문을 사용하여 동시성 코드를 작성하는 라이브러리입니다. 고성능 네트워크 및 웹 서버, 데이터베이스 연결 라이브러리, 분산 작업 큐 등을 제공하는 여러 파이썬 비동기 프레임워크의 기반으로 사용됩니다.
categories:
  - Python
tags:
  - Python
  - Python-Library
  - Concurrency
  - Asynchronous
  - Python-asyncio
last_modified_at: 2024-04-11T15:11:34+09:00
link: https://docs.python.org/ko/3/library/asyncio.html
상위 항목: "[[python_asyncio|파이썬 비동기 입출력 (Python Asyncio)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

---


### 러너 (Runners)

> **소스 코드:** [Lib/asyncio/runners.py](https://github.com/python/cpython/tree/3.12/Lib/asyncio/runners.py)

- 이 섹션에서는 asyncio 코드를 실행하기 위한 고수준 asyncio 프리미티브를 설명합니다.
- 이들은 일반적으로 널리 사용되는 시나리오에 대해 비동기 코드 사용을 단순화하기 위해 [이벤트 루프](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio-event-loop) 위에 구축되었습니다.
	- [asyncio 프로그램 실행하기](https://docs.python.org/ko/3/library/asyncio-runner.html#running-an-asyncio-program)
	- [Runner 컨텍스트 매니저](https://docs.python.org/ko/3/library/asyncio-runner.html#runner-context-manager)
	- [키보드 인터럽트 처리](https://docs.python.org/ko/3/library/asyncio-runner.html#handling-keyboard-interruption)

#### asyncio 프로그램 실행하기 (Running an asyncio Program)

```
asyncio.run(_coro_, _*_, _debug=None_, _loop_factory=None_)
```

- [코루틴](https://docs.python.org/ko/3/glossary.html#term-coroutine) coro 를 실행하고 결과를 반환합니다.
- 이 함수는 전달된 코루틴을 실행하며, asyncio 이벤트 루프 관리, 비동기 제너레이터 종료, 그리고 실행자 닫기를 처리합니다.
- 이 함수는 동일한 스레드에서 다른 asyncio 이벤트 루프가 실행 중일 때 호출할 수 없습니다.
- debug 가 `True`이면 이벤트 루프가 디버그 모드로 실행됩니다. `False`는 명시적으로 디버그 모드를 비활성화합니다. `None`은 전역 [디버그 모드](https://docs.python.org/ko/3/library/asyncio-dev.html#asyncio-debug-mode) 설정을 따릅니다.
- loop_factory 가 `None`이 아니면 새 이벤트 루프를 생성하는 데 사용됩니다. 그렇지 않으면 [`asyncio.new_event_loop()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.new_event_loop "asyncio.new_event_loop")가 사용됩니다. 루프는 끝에서 닫힙니다. 이 함수는 asyncio 프로그램의 주 진입점으로 사용되어야 하며, 이상적으로는 한 번만 호출되어야 합니다. 정책 대신 loop_factory 를 사용하여 이벤트 루프를 구성하는 것이 좋습니다.
- 실행자에게는 종료하기 위해 5분의 제한 시간이 주어집니다. 실행자가 그 시간 내에 끝나지 않으면 경고가 발생하고 실행자가 닫힙니다.

```python
async def main():
    await asyncio.sleep(1)
    print('hello')

asyncio.run(main())
```

> 버전 3.7에서 추가.
> 버전 3.9에서 변경: [`loop.shutdown_default_executor()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.shutdown_default_executor "asyncio.loop.shutdown_default_executor")를 사용하도록 업데이트되었습니다.
> 버전 3.10에서 변경: _debug_ 의 기본값이 `None`으로 변경되어 전역 디버그 모드 설정을 따릅니다.
> 버전 3.12에서 변경: _loop_factory_ 매개변수가 추가되었습니다.

#### Runner 컨텍스트 매니저 (Runner context manager)


`class asyncio.Runner(*, debug=None, loop_factory=None)`


- 동일한 컨텍스트에서 _여러_ 비동기 함수 호출을 단순화하는 컨텍스트 매니저입니다.
- 때때로 여러 최상위 비동기 함수를 동일한 [이벤트 루프](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio-event-loop)와 [`contextvars.Context`](https://docs.python.org/ko/3/library/contextvars.html#contextvars.Context "contextvars.Context")에서 호출해야 할 수 있습니다.
- _debug_ 가 `True`이면 이벤트 루프가 디버그 모드로 실행됩니다. `False`는 명시적으로 디버그 모드를 비활성화합니다. `None`은 전역 [디버그 모드](https://docs.python.org/ko/3/library/asyncio-dev.html#asyncio-debug-mode) 설정을 따릅니다.
- _loop_factory_ 는 루프 생성을 오버라이딩하는 데 사용될 수 있습니다. 생성된 루프를 현재 루프로 설정하는 것은 _loop_factory_ 의 책임입니다. _loop_factory_ 가 `None`이면 기본적으로 [`asyncio.new_event_loop()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.new_event_loop "asyncio.new_event_loop")가 사용되고 [`asyncio.set_event_loop()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.set_event_loop "asyncio.set_event_loop")로 현재 이벤트 루프로 설정됩니다.
- 기본적으로 [`asyncio.run()`](https://docs.python.org/ko/3/library/asyncio-runner.html#asyncio.run "asyncio.run") 예제는 runner 사용으로 다음과 같이 다시 작성될 수 있습니다:

```python
async def main():
    await asyncio.sleep(1)
    print('hello')

with asyncio.Runner() as runner:
    runner.run(main())
```

> 버전 3.11에서 추가.


`run(coro, *, context=None)`
- 내장된 루프에서 [코루틴](https://docs.python.org/ko/3/glossary.html#term-coroutine) _coro_ 를 실행합니다.
- 코루틴의 결과를 반환하거나 예외를 발생시킵니다.
- 선택적 키워드 전용 _context_ 인수를 사용하면 _coro_ 가 실행될 사용자 정의 [`contextvars.Context`](https://docs.python.org/ko/3/library/contextvars.html#contextvars.Context "contextvars.Context")를 지정할 수 있습니다. `None`이면 runner의 기본 컨텍스트가 사용됩니다.
- 이 함수는 동일한 스레드에서 다른 asyncio 이벤트 루프가 실행 중일 때 호출할 수 없습니다.

`close()`
- runner를 닫습니다.
- 비동기 제너레이터를 종료하고, 기본 실행자를 종료하며, 이벤트 루프를 닫고 내장된 [`contextvars.Context`](https://docs.python.org/ko/3/library/contextvars.html#contextvars.Context "contextvars.Context")를 해제합니다.

`get_loop()`
- runner 인스턴스와 연결된 이벤트 루프를 반환합니다.

> [`Runner`](https://docs.python.org/ko/3/library/asyncio-runner.html#asyncio.Runner "asyncio.Runner")는 지연 초기화 전략을 사용하므로 생성자는 기본 하위 수준 구조를 초기화하지 않습니다.
> 내장된 _loop_와 _context_는 [`with`](https://docs.python.org/ko/3/reference/compound_stmts.html#with) 본문에 들어갈 때나 [`run()`](https://docs.python.org/ko/3/library/asyncio-runner.html#asyncio.run "asyncio.run") 또는 [`get_loop()`](https://docs.python.org/ko/3/library/asyncio-runner.html#asyncio.Runner.get_loop "asyncio.Runner.get_loop")의 첫 호출 시 생성됩니다.

#### 키보드 인터럽트 처리 (Handling Keyboard Interruption)
> 버전 3.11에서 추가.
- Ctrl-C로 [`signal.SIGINT`](https://docs.python.org/ko/3/library/signal.html#signal.SIGINT "signal.SIGINT")가 발생하면 기본적으로 메인 스레드에서 [`KeyboardInterrupt`](https://docs.python.org/ko/3/library/exceptions.html#KeyboardInterrupt "KeyboardInterrupt") 예외가 발생합니다. 그러나 이는 [`asyncio`](https://docs.python.org/ko/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.")와 함께 작동하지 않습니다. asyncio 내부를 중단하고 프로그램이 종료되지 않고 멈출 수 있기 때문입니다.
- 이 문제를 완화하기 위해 [`asyncio`](https://docs.python.org/ko/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.")는 [`signal.SIGINT`](https://docs.python.org/ko/3/library/signal.html#signal.SIGINT "signal.SIGINT")를 다음과 같이 처리합니다:
1. [`asyncio.Runner.run()`](https://docs.python.org/ko/3/library/asyncio-runner.html#asyncio.Runner.run "asyncio.Runner.run")은 사용자 코드가 실행되기 전에 사용자 정의 [`signal.SIGINT`](https://docs.python.org/ko/3/library/signal.html#signal.SIGINT "signal.SIGINT") 핸들러를 설치하고 함수에서 나갈 때 제거합니다.
2. [`Runner`](https://docs.python.org/ko/3/library/asyncio-runner.html#asyncio.Runner "asyncio.Runner")는 실행을 위해 전달된 코루틴에 대한 메인 태스크를 생성합니다.
3. Ctrl-C로 [`signal.SIGINT`](https://docs.python.org/ko/3/library/signal.html#signal.SIGINT "signal.SIGINT")가 발생하면, 사용자 정의 시그널 핸들러가 [`asyncio.Task.cancel()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task.cancel "asyncio.Task.cancel")을 호출하여 메인 태스크를 취소합니다. 이는 메인 태스크 내에서 [`asyncio.CancelledError`](https://docs.python.org/ko/3/library/asyncio-exceptions.html#asyncio.CancelledError "asyncio.CancelledError")를 발생시킵니다. 이로 인해 Python 스택이 풀리며, `try/except`와 `try/finally` 블록을 리소스 정리에 사용할 수 있습니다. 메인 태스크가 취소된 후, [`asyncio.Runner.run()`](https://docs.python.org/ko/3/library/asyncio-runner.html#asyncio.Runner.run "asyncio.Runner.run")은 [`KeyboardInterrupt`](https://docs.python.org/ko/3/library/exceptions.html#KeyboardInterrupt "KeyboardInterrupt")를 발생시킵니다.
4. 사용자가 [`asyncio.Task.cancel()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task.cancel "asyncio.Task.cancel")로 중단할 수 없는 타이트 루프를 작성할 수 있습니다. 이 경우 두 번째로 이어지는 Ctrl-C는 메인 태스크를 취소하지 않고 즉시 [`KeyboardInterrupt`](https://docs.python.org/ko/3/library/exceptions.html#KeyboardInterrupt "KeyboardInterrupt")를 발생시킵니다.

### 코루틴과 태스크 (Coroutine & Task)
#### 코루틴 (Coroutine)

- 코루틴은 async/await 구문으로 선언되며, asyncio 애플리케이션을 작성하는 데 선호되는 방식입니다.
- 다음 코드 조각은 "hello"를 출력하고, 1초를 기다린 후 "world"를 출력합니다:

```python
import asyncio

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())
```

- 단순히 코루틴을 호출하는 것만으로는 실행되지 않습니다:

```python
main()
<coroutine object main at 0x1053bb7c8>
```

- 코루틴을 실제로 실행하기 위해 asyncio는 다음과 같은 메커니즘을 제공합니다:
- 최상위 진입점 "main()" 함수를 실행하는 [asyncio.run()](https://docs.python.org/ko/3/library/asyncio-runner.html#asyncio.run "asyncio.run") 함수 (위의 예를 보세요.)
- 코루틴을 기다리기. 다음 코드 조각은 1초를 기다린 후 "hello"를 인쇄한 다음 또 2초를 기다린 후 "world"를 인쇄합니다:

```python
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
```

- 예상 출력:

```
started at 17:13:52
hello
world
finished at 17:13:55
```

- 코루틴을 asyncio [태스크](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")로 동시에 실행하는 [asyncio.create_task()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.create_task "asyncio.create_task") 함수.
- 위의 예를 수정해서 두 개의 say_after 코루틴을 동시에 실행해 봅시다:

```python
async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
```

- 예상 출력은 이제 코드 조각이 이전보다 1초 빠르게 실행되었음을 보여줍니다:

```
started at 17:14:32
hello
world
finished at 17:14:34
```

- [asyncio.TaskGroup](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.TaskGroup "asyncio.TaskGroup") 클래스는 [create_task()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.create_task "asyncio.create_task")에 대한 더 현대적인 대안을 제공합니다. 이 API를 사용하면 마지막 예제는 다음과 같이 됩니다:

```python
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(1, 'hello'))

        task2 = tg.create_task(
            say_after(2, 'world'))

        print(f"started at {time.strftime('%X')}")

    # The await is implicit when the context manager exits.

    print(f"finished at {time.strftime('%X')}")
```

- 타이밍과 출력은 이전 버전과 동일해야 합니다.
- 버전 3.11에서 추가: [asyncio.TaskGroup](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.TaskGroup "asyncio.TaskGroup").

#### 어웨이터블 (Awaitables)

- 객체가 [await](https://docs.python.org/ko/3/reference/expressions.html#await) 표현식에서 사용될 수 있을 때 어웨이터블 객체라고 합니다.
- 많은 asyncio API는 어웨이터블을 받아들이도록 설계되었습니다.
- 어웨이터블 객체에는 세 가지 주요 유형이 있습니다: 코루틴, 태스크 및 퓨처.

**코루틴 (Coroutines)**

- 파이썬 코루틴은 어웨이터블이므로 다른 코루틴에서 기다릴 수 있습니다:

```python
import asyncio

async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())
```

- 중요: 이 설명서에서 "코루틴" 이라는 용어는 두 가지 밀접한 관련 개념에 사용될 수 있습니다:
  - 코루틴 함수: [async def](https://docs.python.org/ko/3/reference/compound_stmts.html#async-def) 함수;
  - 코루틴 객체: 코루틴 함수를 호출하여 반환된 객체.

**태스크 (Tasks)**

- 태스크는 코루틴을 동시에 예약하는 데 사용됩니다.
- 코루틴이 [asyncio.create_task()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.create_task "asyncio.create_task")와 같은 함수를 사용하여 태스크로 싸일 때 코루틴은 곧 실행되도록 자동으로 예약됩니다:

```python
import asyncio

async def nested():
    return 42

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task

asyncio.run(main())
```

**퓨처 (Futures)**

- [Future](https://docs.python.org/ko/3/library/asyncio-future.html#asyncio.Future "asyncio.Future")는 비동기 연산의 최종 결과를 나타내는 특별한 저수준 어웨이터블 객체입니다.
- Future 객체를 기다릴 때, 그것은 코루틴이 Future가 다른 곳에서 해결될 때까지 기다릴 것을 뜻합니다.
- 콜백 기반 코드를 async/await와 함께 사용하려면 asyncio의 Future 객체가 필요합니다.
- 일반적으로 응용 프로그램 수준 코드에서 Future 객체를 만들 필요는 없습니다.
- 때때로 라이브러리와 일부 asyncio API에 의해 노출되는 Future 객체를 기다릴 수 있습니다:

```python
async def main():
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )
```

- Future 객체를 반환하는 저수준 함수의 좋은 예는 [loop.run_in_executor()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "asyncio.loop.run_in_executor")입니다.

#### 태스크 만들기 (Creating Tasks)

- asyncio.create_task(coro, *, name=None, context=None)
  - coro [코루틴](https://docs.python.org/ko/3/library/asyncio-task.html#coroutine)을 [Task](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")로 감싸고 실행을 예약합니다. Task 객체를 반환합니다.
  - name이 None이 아니면, [Task.set_name()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task.set_name "asyncio.Task.set_name")을 사용하여 태스크의 이름으로 설정됩니다.
  - 선택적 키워드 전용 context 인수를 사용하면 coro가 실행될 사용자 정의 [contextvars.Context](https://docs.python.org/ko/3/library/contextvars.html#contextvars.Context "contextvars.Context")를 지정할 수 있습니다. context가 제공되지 않으면 현재 컨텍스트 복사본이 생성됩니다.
  - [get_running_loop()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.get_running_loop "asyncio.get_running_loop")에 의해 반환된 루프에서 태스크가 실행되고, 현재 스레드에 실행 중인 루프가 없으면 [RuntimeError](https://docs.python.org/ko/3/library/exceptions.html#RuntimeError "RuntimeError")가 발생합니다.
- 참고: [asyncio.TaskGroup.create_task()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.TaskGroup.create_task "asyncio.TaskGroup.create_task")는 구조적 동시성을 활용하는 새로운 대안입니다; 강력한 안전 보장과 함께 관련 태스크 그룹을 기다릴 수 있습니다.
- 중요: 이 함수의 결과에 대한 참조를 저장하여 태스크가 실행 중에 사라지는 것을 방지하세요. 이벤트 루프는 태스크에 대한 약한 참조만 유지합니다. 다른 곳에서 참조되지 않는 태스크는 완료되기 전에도 언제든지 가비지 수집될 수 있습니다. 신뢰할 수 있는 "fire-and-forget" 백그라운드 태스크를 위해 컬렉션에 모아둡니다:

```python
background_tasks = set()

for i in range(10):
    task = asyncio.create_task(some_coro(param=i))

    # Add task to the set. This creates a strong reference.
    background_tasks.add(task)

    # To prevent keeping references to finished tasks forever,
    # make each task remove its own reference from the set after
    # completion:
    task.add_done_callback(background_tasks.discard)
```

- 버전 3.7에서 추가되었습니다.
- 버전 3.8에서 변경: name 매개변수가 추가되었습니다.
- 버전 3.11에서 변경: context 매개변수가 추가되었습니다.

#### 태스크 취소 (Task Cancellation)

- 작업은 쉽고 안전하게 취소할 수 있습니다.
- 작업이 취소되면 다음 기회에 작업에서 [`asyncio.CancelledError`](https://docs.python.org/ko/3/library/asyncio-exceptions.html#asyncio.CancelledError "asyncio.CancelledError")가 발생합니다.
- 코루틴은 강력한 정리 로직을 수행하기 위해 `try/finally` 블록을 사용하는 것이 권장됩니다.
- [`asyncio.CancelledError`](https://docs.python.org/ko/3/library/asyncio-exceptions.html#asyncio.CancelledError "asyncio.CancelledError")가 명시적으로 잡힌 경우, 일반적으로 정리가 완료되면 전파해야 합니다.
- [`asyncio.CancelledError`](https://docs.python.org/ko/3/library/asyncio-exceptions.html#asyncio.CancelledError "asyncio.CancelledError")는 [`BaseException`](https://docs.python.org/ko/3/library/exceptions.html#BaseException "BaseException")을 직접 상속하므로 대부분의 코드에서는 이를 인식할 필요가 없습니다.
- [`asyncio.TaskGroup`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.TaskGroup "asyncio.TaskGroup")과 [`asyncio.timeout()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.timeout "asyncio.timeout")와 같은 구조화된 동시성을 가능하게 하는 asyncio 컴포넌트들은 내부적으로 취소를 사용하여 구현됩니다.
- 코루틴이 [`asyncio.CancelledError`](https://docs.python.org/ko/3/library/asyncio-exceptions.html#asyncio.CancelledError "asyncio.CancelledError")를 삼켜버리면 이러한 컴포넌트들이 오작동할 수 있습니다.
- 마찬가지로, 사용자 코드는 일반적으로 [`uncancel`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task.uncancel "asyncio.Task.uncancel")을 호출해서는 안 됩니다.
- 그러나 [`asyncio.CancelledError`](https://docs.python.org/ko/3/library/asyncio-exceptions.html#asyncio.CancelledError "asyncio.CancelledError")를 억제하는 것이 진정으로 필요한 경우, 취소 상태를 완전히 제거하기 위해 `uncancel()`을 호출하는 것도 필요합니다.

#### 태스크 그룹 (Task Groups)

- TaskGroup은 태스크 생성 API와 그룹 내 모든 태스크가 완료될 때까지 기다리는 편리하고 신뢰할 수 있는 방법을 결합합니다.

`class asyncio.TaskGroup`

- 태스크 그룹을 보유하는 비동기 컨텍스트 관리자입니다.
- create_task()를 사용하여 그룹에 태스크를 추가할 수 있습니다.
- 컨텍스트 관리자가 종료될 때 모든 태스크가 대기됩니다.

> 버전 3.11에서 추가되었습니다.

`create_task(coro, *, name=None, context=None)`

- 이 태스크 그룹에 태스크를 생성합니다.
- 서명은 asyncio.create_task()와 일치합니다.

예:

```python
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(some_coro(…))
        task2 = tg.create_task(another_coro(…))
    print(f"Both tasks have completed now: {task1.result()}, {task2.result()}")
```

- async with 문은 그룹의 모든 태스크가 완료될 때까지 기다립니다.
- 대기하는 동안 그룹에 새 태스크를 추가할 수 있습니다.
- 마지막 태스크가 완료되고 async with 블록이 종료되면 그룹에 새 태스크를 추가할 수 없습니다.
- 그룹에 속한 태스크 중 하나라도 asyncio.CancelledError 이외의 예외로 실패하면 그룹의 나머지 태스크가 취소됩니다.
- 이 시점에서 async with 문의 본문이 여전히 활성 상태인 경우 async with 문을 직접 포함하는 태스크도 취소됩니다.
- 모든 태스크가 완료되면 asyncio.CancelledError 이외의 예외로 실패한 태스크가 있는 경우 해당 예외가 ExceptionGroup 또는 BaseExceptionGroup으로 결합되어 발생합니다.
- KeyboardInterrupt 또는 SystemExit로 태스크가 실패하면 태스크 그룹은 여전히 나머지 태스크를 취소하고 기다리지만 초기 KeyboardInterrupt 또는 SystemExit가 다시 발생합니다.
- async with 문의 본문이 예외로 종료되면 태스크 중 하나가 실패한 것과 동일하게 처리됩니다.

#### 잠자기 (Sleeping)

(coroutine) `asyncio.sleep(delay, result=None)`

- delay 초 동안 블록합니다.
- result가 제공되면, 코루틴이 완료될 때 호출자에게 반환됩니다.
- sleep()은 항상 현재 태스크를 일시 중단해서 다른 태스크를 실행할 수 있도록 합니다.
- 지연을 0으로 설정하면 다른 태스크가 실행될 수 있도록 최적화된 경로를 제공합니다.

5초 동안 현재 날짜를 매초 표시하는 코루틴의 예:

```python
import asyncio
import datetime

async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

asyncio.run(display_date())
```

> 버전 3.10에서 변경: loop 매개변수가 제거되었습니다.

#### 동시에 태스크 실행하기 (Running Tasks Concurrently)

(awaitable) `asyncio.gather(*aws, return_exceptions=False)`

- aws 시퀀스에 있는 어웨이터블 객체를 동시에 실행합니다.
- aws에 있는 어웨이터블이 코루틴이면 자동으로 태스크로 예약됩니다.
- 모든 어웨이터블이 성공적으로 완료되면, 결과는 반환된 값들이 합쳐진 리스트입니다.
- return_exceptions가 False(기본값)면, 첫 번째 발생한 예외가 gather()를 기다리는 태스크로 즉시 전파됩니다.
- return_exceptions가 True면, 예외는 성공적인 결과처럼 처리되고, 결과 리스트에 집계됩니다.
- gather()가 취소되면, 모든 제출된 (아직 완료되지 않은) 어웨이터블도 취소됩니다.
- aws 시퀀스의 Task나 Future가 취소되면, 그것이 CancelledError를 일으킨 것처럼 처리됩니다.

> 참고: 동시에 태스크를 생성하고 실행하며 완료를 기다리는 새로운 대안은 asyncio.TaskGroup입니다. TaskGroup은 서브태스크 중첩을 예약하는 데 있어 gather보다 더 강력한 안전 보장을 제공합니다.

예:

```python
import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}…")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)

asyncio.run(main())
```

> 참고: return_exceptions가 false인 경우, gather()가 완료된 것으로 표시된 후 취소해도 제출된 어웨이터블은 취소되지 않습니다.

> 버전 3.7에서 변경: gather 자체가 취소되면, return_exceptions와 관계없이 취소가 전파됩니다.
> 버전 3.10에서 변경: loop 매개변수가 제거되었습니다.
> 버전 3.10부터 폐지됨: 위치 인수가 제공되지 않거나 모든 위치 인수가 Future와 유사한 객체가 아니고 실행 중인 이벤트 루프가 없는 경우 폐지 경고가 발생합니다.


#### 열성 작업 팩토리 (Eager Task Factory)
`asyncio.eager_task_factory(loop, coro, *, name=None, context=None)`
- 열성 작업 실행을 위한 작업 팩토리입니다.
- 이 팩토리를 사용할 때 ([loop.set_task_factory(asyncio.eager_task_factory)](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.set_task_factory "asyncio.loop.set_task_factory")를 통해), 코루틴은 Task 구성 중에 동기적으로 실행을 시작합니다.
- 작업은 블록될 때만 이벤트 루프에 예약됩니다.
- 이는 동기적으로 완료되는 코루틴의 경우 루프 예약 오버헤드를 피할 수 있어 성능 향상이 될 수 있습니다.
- 이것이 유익한 일반적인 예는 가능한 경우 실제 I/O를 피하기 위해 캐싱이나 메모화를 사용하는 코루틴입니다.

> 코루틴의 즉시 실행은 의미론적 변화입니다. 코루틴이 반환되거나 예외를 발생시키면 작업은 이벤트 루프에 예약되지 않습니다. 코루틴 실행이 블록되면 작업은 이벤트 루프에 예약됩니다. 이 변경은 기존 애플리케이션에 동작 변화를 도입할 수 있습니다. 예를 들어, 애플리케이션의 작업 실행 순서가 변경될 가능성이 높습니다.

> 버전 3.12에서 추가되었습니다.

`asyncio.create_eager_task_factory(custom_task_constructor)`
- eager_task_factory()와 유사한 열성 작업 팩토리를 생성하지만, 새 작업을 만들 때 기본 Task 대신 제공된 custom_task_constructor를 사용합니다.
- custom_task_constructor는 Task.__init__의 서명과 일치하는 서명을 가진 호출 가능 객체여야 합니다.
- 이 호출 가능 객체는 asyncio.Task와 호환되는 객체를 반환해야 합니다.
- 이 함수는 loop.set_task_factory(factory)를 통해 이벤트 루프의 작업 팩토리로 사용하기 위한 호출 가능 객체를 반환합니다.

> 버전 3.12에서 추가되었습니다.

#### 취소로부터 보호하기 (Shielding from cancellation)
(awaitable) `asyncio.shield(aw)`
- 어웨이터블 객체를 취소로부터 보호합니다.
- aw가 코루틴이면 자동으로 태스크로 예약됩니다.
- 다음 문장들의 동등성과 차이점을 설명합니다.
- shield() 함수를 사용할 때의 취소 동작에 대해 설명합니다.
- 취소를 완전히 무시하는 방법에 대해 설명하고, 이는 권장되지 않음을 명시합니다.

> [!important] 
> - 이 함수에 전달된 작업에 대한 참조를 저장하여 작업이 실행 중에 사라지는 것을 방지하세요. 이벤트 루프는 작업에 대한 약한 참조만 유지합니다. 다른 곳에서 참조되지 않는 작업은 완료되기 전에도 언제든 가비지 수집될 수 있습니다.

> 버전 3.10에서 변경: loop 매개변수가 제거되었습니다.
> 버전 3.10부터 폐지됨: aw가 Future와 유사한 객체가 아니고 실행 중인 이벤트 루프가 없는 경우 폐지 경고가 발생합니다.

#### 시간제한 (Timeouts)
`asyncio.timeout(delay)`
- 무언가를 기다리는 데 소요되는 시간을 제한하는 데 사용할 수 있는 비동기 컨텍스트 관리자를 반환합니다.
- delay는 None이거나 기다릴 초 수(float/int)일 수 있습니다. 
- delay가 None이면 시간 제한이 적용되지 않습니다. 이는 컨텍스트 관리자가 생성될 때 지연 시간을 알 수 없는 경우에 유용할 수 있습니다.
- 두 경우 모두 컨텍스트 관리자는 생성 후 Timeout.reschedule()을 사용하여 재조정할 수 있습니다.

예:

```python
async def main():
    async with asyncio.timeout(10):
        await long_running_task()
```

- long_running_task가 완료되는 데 10초 이상 걸리면 컨텍스트 관리자는 현재 작업을 취소하고 결과로 발생한 asyncio.CancelledError를 내부적으로 처리하여 이를 잡아서 처리할 수 있는 TimeoutError로 변환합니다.

> `asyncio.timeout()` 컨텍스트 관리자는 asyncio.CancelledError를 TimeoutError로 변환하는 것이므로 TimeoutError는 컨텍스트 관리자 외부에서만 잡을 수 있습니다.

TimeoutError 잡기 예시:

```python
async def main():
    try:
        async with asyncio.timeout(10):
            await long_running_task()
    except TimeoutError:
        print("The long operation timed out, but we've handled it.")

    print("This statement will run regardless.")
```

- asyncio.timeout()에 의해 생성된 컨텍스트 관리자는 다른 마감 시간으로 재조정하고 검사할 수 있습니다.

`class asyncio.Timeout(when)`
- 기한이 지난 코루틴을 취소하기 위한 비동기 컨텍스트 관리자입니다.
- when은 이벤트 루프의 시계로 측정된 컨텍스트가 시간 초과되어야 하는 절대 시간이어야 합니다:
	- when이 None이면 시간 초과가 절대 트리거되지 않습니다.
	- when < loop.time()이면 시간 초과는 이벤트 루프의 다음 반복에서 트리거됩니다.
- when() → float | None
	- 현재 마감 시간을 반환하거나, 현재 마감 시간이 설정되지 않은 경우 None을 반환합니다.
- reschedule(when: float | None)
	- 시간 초과를 재조정합니다.
- expired() → bool
	- 컨텍스트 관리자가 마감 시간을 초과했는지(만료되었는지) 여부를 반환합니다.

예:

```python
async def main():
    try:
        # 시작할 때 시간 초과를 모르므로 None을 전달합니다.
        async with asyncio.timeout(None) as cm:
            # 이제 시간 초과를 알고 있으므로 재조정합니다.
            new_deadline = get_running_loop().time() + 10
            cm.reschedule(new_deadline)

            await long_running_task()
    except TimeoutError:
        pass

    if cm.expired():
        print("Looks like we haven't finished on time.")
```

- 시간 초과 컨텍스트 관리자는 안전하게 중첩될 수 있습니다.

> 버전 3.11에 추가되었습니다.

`asyncio.timeout_at(when)`

- asyncio.timeout()과 유사하지만, when은 대기를 중지할 절대 시간 또는 None입니다.

예:

```python
async def main():
    loop = get_running_loop()
    deadline = loop.time() + 20
    try:
        async with asyncio.timeout_at(deadline):
            await long_running_task()
    except TimeoutError:
        print("The long operation timed out, but we've handled it.")

    print("This statement will run regardless.")
```

> 버전 3.11에 추가되었습니다.

(coroutine) `asyncio.wait_for(aw, timeout)`
- aw 어웨이터블이 제한된 시간 내에 완료될 때까지 기다립니다.
- aw가 코루틴이면 자동으로 태스크로 예약됩니다.
- timeout은 None 또는 대기할 float나 int 초 수입니다. timeout이 None이면 퓨처가 완료될 때까지 블록합니다.
- 시간 초과가 발생하면 태스크를 취소하고 TimeoutError를 발생시킵니다.
- 태스크 취소를 피하려면 shield()로 감싸십시오.
- 이 함수는 퓨처가 실제로 취소될 때까지 대기하므로, 총 대기 시간이 timeout을 초과할 수 있습니다. 취소하는 동안 예외가 발생하면, 전파됩니다.
- 대기가 취소되면, 퓨처 aw도 취소됩니다.

예:

```python
async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3600)
    print('yay!')

async def main():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except TimeoutError:
        print('timeout!')

asyncio.run(main())

# Expected output:
#
#     timeout!
```

> 버전 3.7에서 변경: aw가 시간 초과로 인해 취소되면 wait_for는 aw가 취소될 때까지 기다립니다. 이전에는 즉시 TimeoutError를 발생시켰습니다.
> 버전 3.10에서 변경: loop 매개변수가 제거되었습니다.
> 버전 3.11에서 변경: asyncio.TimeoutError 대신 TimeoutError를 발생시킵니다.

#### 대기 프리미티브 (Waiting Primitives)
(coroutine) `asyncio.wait(aws, *, timeout=None, return_when=ALL_COMPLETED)`
- aws 이터러블에 있는 Future와 Task 인스턴스를 동시에 실행하고 return_when에 지정된 조건이 충족될 때까지 블록합니다.
- aws 이터러블은 비어있을 수 없습니다.
- 두 집합의 태스크/퓨처를 반환합니다: (done, pending).

사용법:

```python
done, pending = await asyncio.wait(aws)
```

- timeout(float나 int)을 지정하면, 반환하기 전에 대기할 최대 시간(초)을 제어할 수 있습니다.
- 이 함수는 TimeoutError를 발생시키지 않습니다. 시간 초과가 발생했을 때 완료되지 않은 Future나 Task는 단순히 두 번째 집합에 반환됩니다.
- return_when은 이 함수가 언제 반환해야 하는지 나타냅니다. 다음 상수 중 하나여야 합니다:

| 상수 | 설명 |
|---|---|
| asyncio.FIRST_COMPLETED | 퓨처가 하나라도 끝나거나 취소될 때 함수가 반환됩니다. |
| asyncio.FIRST_EXCEPTION | 퓨처가 예외를 발생시켜 끝나면 함수가 반환됩니다. 예외를 발생시키는 퓨처가 없으면 ALL_COMPLETED와 동일합니다. |
| asyncio.ALL_COMPLETED | 모든 퓨처가 끝나거나 취소되면 함수가 반환됩니다. |

- wait_for()와 달리, wait()는 시간 초과가 발생할 때 퓨처를 취소하지 않습니다.

> 버전 3.10에서 변경: loop 매개변수가 제거되었습니다.
> 
> 버전 3.11에서 변경: wait()에 직접 코루틴 객체를 전달하는 것이 금지되었습니다.
> 
> 버전 3.12에서 변경: 태스크를 생성하는 제너레이터에 대한 지원이 추가되었습니다.

`asyncio.as_completed(aws, *, timeout=None)`

- aws 이터러블에 있는 어웨이터블 객체를 동시에 실행합니다. 코루틴의 이터레이터를 반환합니다. 반환된 각 코루틴은 남아있는 어웨이터블의 이터러블에서 가장 빠른 다음 결과를 얻기 위해 어웨이트 할 수 있습니다.
- 모든 Future가 완료되기 전에 시간 초과가 발생하면 TimeoutError를 발생시킵니다.

예:

```python
for coro in as_completed(aws):
    earliest_result = await coro
    # …
```

> 버전 3.10에서 변경: loop 매개변수가 제거되었습니다.
> 버전 3.10부터 폐지됨: aws 이터러블의 모든 어웨이터블 객체가 Future와 유사한 객체가 아니고 실행 중인 이벤트 루프가 없는 경우 폐지 경고가 발생합니다.
> 버전 3.12에서 변경: 태스크를 생성하는 제너레이터에 대한 지원이 추가되었습니다.

#### 스레드에서 실행하기 (Running in threads)

`coroutine asyncio.to_thread(func, /, *args, **kwargs)`

- 별도의 스레드에서 func 함수를 비동기적으로 실행합니다.
- 이 함수에 제공된 모든 `*args` 와 `**kwargs` 는 func로 직접 전달됩니다. 
- 또한, 현재 [contextvars.Context](https://docs.python.org/ko/3/library/contextvars.html#contextvars.Context "contextvars.Context")가 전파되어, 이벤트 루프 스레드의 컨텍스트 변수가 별도의 스레드에서 액세스 될 수 있습니다.
- func의 최종 결과를 얻기 위해 어웨이트 할 수 있는 코루틴을 반환합니다.
- 이 코루틴 함수는 주로 이벤트 루프를 차단할 수 있는 IO 바운드 함수/메서드를 메인 스레드 대신 실행하는 데 사용됩니다. 예를 들면:

```python
def blocking_io():
    print(f"start blocking_io at {time.strftime('%X')}")
    # Note that time.sleep() can be replaced with any blocking
    # IO-bound operation, such as file operations.
    time.sleep(1)
    print(f"blocking_io complete at {time.strftime('%X')}")

async def main():
    print(f"started main at {time.strftime('%X')}")

    await asyncio.gather(
        asyncio.to_thread(blocking_io),
        asyncio.sleep(1))

    print(f"finished main at {time.strftime('%X')}")

asyncio.run(main())

# Expected output:
#
# started main at 19:50:53
# start blocking_io at 19:50:53
# blocking_io complete at 19:50:54
# finished main at 19:50:54
```

- 모든 코루틴에서 blocking_io()를 직접 호출하면 이벤트 루프가 지속 시간 동안 차단되어 실행 시간이 1초 더 늘어납니다. 
- 대신 asyncio.to_thread()를 사용하면 이벤트 루프를 차단하지 않고 별도의 스레드에서 실행할 수 있습니다.

> GIL로 인해 asyncio.to_thread()는 일반적으로 IO 바운드 함수만 비차단으로 만드는 데 사용할 수 있습니다. 그러나 GIL을 해제하는 확장 모듈이나 GIL이 없는 대체 Python 구현의 경우 asyncio.to_thread()를 CPU 바운드 함수에도 사용할 수 있습니다.

> 버전 3.9에서 추가되었습니다.

#### 다른 스레드에서 예약하기 (Scheduling from other threads)

`asyncio.run_coroutine_threadsafe(coro, loop)`

- 주어진 이벤트 루프에 코루틴을 제출합니다. 스레드 안전합니다.
- 다른 OS 스레드에서 결과를 기다리는 [concurrent.futures.Future](https://docs.python.org/ko/3/library/concurrent.futures.html#concurrent.futures.Future "concurrent.futures.Future")를 반환합니다.
- 이 함수는 이벤트 루프가 실행 중인 스레드가 아닌, 다른 OS 스레드에서 호출하기 위한 것입니다. 예:

```python
# Create a coroutine
coro = asyncio.sleep(1, result=3)

# Submit the coroutine to a given loop
future = asyncio.run_coroutine_threadsafe(coro, loop)

# Wait for the result with an optional timeout argument
assert future.result(timeout) == 3
```

- 코루틴에서 예외가 발생하면, 반환된 Future에 통지됩니다. 
- 또한, 이벤트 루프에서 태스크를 취소하는 데 사용할 수 있습니다:

```python
try:
    result = future.result(timeout)
except TimeoutError:
    print('The coroutine took too long, cancelling the task…')
    future.cancel()
except Exception as exc:
    print(f'The coroutine raised an exception: {exc!r}')
else:
    print(f'The coroutine returned: {result!r}')
```

- 설명서의 [동시성과 다중 스레드](https://docs.python.org/ko/3/library/asyncio-dev.html#asyncio-multithreading) 절을 참조하십시오.
- 다른 asyncio 함수와 달리, 이 함수는 loop 인자가 명시적으로 전달되어야 합니다.

> 버전 3.5.1에서 추가되었습니다.

#### 인트로스펙션 (Introspection)

`asyncio.current_task(loop=None)`

- 현재 실행 중인 Task 인스턴스를 반환하거나 태스크가 실행되고 있지 않으면 None을 반환합니다.
- loop가 None이면, 현재 루프를 가져오는 데 [get_running_loop()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.get_running_loop "asyncio.get_running_loop")가 사용됩니다.

> 버전 3.7에서 추가되었습니다.

`asyncio.all_tasks(loop=None)`

- 루프에 의해 실행되는 아직 완료되지 않은 Task 객체 집합을 반환합니다.
- loop가 None이면, 현재 루프를 가져오는 데 [get_running_loop()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.get_running_loop "asyncio.get_running_loop")가 사용됩니다.

> 버전 3.7에서 추가되었습니다.

`asyncio.iscoroutine(obj)`

- obj가 코루틴 객체이면 True를 반환합니다.

> 버전 3.4에서 추가되었습니다.

#### Task 객체 (Task object)

`class asyncio.Task(coro, *, loop=None, name=None, context=None, eager_start=False)`

- 파이썬 코루틴을 실행하는 퓨처류 객체입니다. 스레드 안전하지 않습니다.
- 태스크는 이벤트 루프에서 코루틴을 실행하는 데 사용됩니다. 
- 만약 코루틴이 Future를 기다리고 있다면, 태스크는 코루틴의 실행을 일시 중지하고 Future의 완료를 기다립니다. 
- 퓨처가 완료되면, 감싸진 코루틴의 실행이 다시 시작됩니다.
- 이벤트 루프는 협업 스케줄링을 사용합니다: 이벤트 루프는 한 번에 하나의 Task를 실행합니다. 
- Task가 Future의 완료를 기다리는 동안, 이벤트 루프는 다른 태스크, 콜백을 실행하거나 IO 연산을 수행합니다.
- 테스크를 만들려면 고수준 [asyncio.create_task()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.create_task "asyncio.create_task") 함수를 사용하거나, 저수준 [loop.create_task()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_task "asyncio.loop.create_task") 나 [ensure_future()](https://docs.python.org/ko/3/library/asyncio-future.html#asyncio.ensure_future "asyncio.ensure_future") 함수를 사용하십시오. 
- 태스크의 인스턴스를 직접 만드는 것은 권장되지 않습니다.
- 실행 중인 Task를 취소하려면 [cancel()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task.cancel "asyncio.Task.cancel") 메서드를 사용하십시오. 
- 이를 호출하면 태스크가 감싼 코루틴으로 [CancelledError](https://docs.python.org/ko/3/library/asyncio-exceptions.html#asyncio.CancelledError "asyncio.CancelledError") 예외를 던집니다. 
- 코루틴이 취소 중에 Future 객체를 기다리고 있으면, Future 객체가 취소됩니다.
- [cancelled()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task.cancelled "asyncio.Task.cancelled")는 태스크가 취소되었는지 확인하는 데 사용할 수 있습니다. 
- 이 메서드는 감싼 코루틴이 [CancelledError](https://docs.python.org/ko/3/library/asyncio-exceptions.html#asyncio.CancelledError "asyncio.CancelledError") 예외를 억제하지 않고 실제로 취소되었으면 True를 반환합니다.
- asyncio.Task는 Future.set_result()와 Future.set_exception()을 제외한 모든 API를 Future에서 상속받습니다.
- 선택적 키워드 전용 context 인자를 사용하면 coro가 실행될 사용자 정의 [contextvars.Context](https://docs.python.org/ko/3/library/contextvars.html#contextvars.Context "contextvars.Context")를 지정할 수 있습니다. 
- context가 제공되지 않으면 Task는 현재 컨텍스트를 복사하고 나중에 복사된 컨텍스트에서 코루틴을 실행합니다.
- 선택적 키워드 전용 eager_start 인자를 사용하면 태스크 생성 시 asyncio.Task의 실행을 즉시 시작할 수 있습니다. 
- True로 설정하고 이벤트 루프가 실행 중이면 태스크는 코루틴이 처음 차단될 때까지 즉시 코루틴 실행을 시작합니다. 
- 코루틴이 차단 없이 반환되거나 예외를 발생시키면 태스크가 즉시 완료되고 이벤트 루프로의 스케줄링을 건너뜁니다.

> 버전 3.7에서 변경: contextvars 모듈에 대한 지원이 추가되었습니다.
> 버전 3.8에서 변경: name 매개변수가 추가되었습니다.
> 버전 3.10부터 폐지됨: loop가 지정되지 않고 실행 중인 이벤트 루프가 없는 경우 더 이상 사용되지 않는다는 경고가 발생합니다.
> 버전 3.11에서 변경: context 매개변수가 추가되었습니다.
> 버전 3.12에서 변경: eager_start 매개변수가 추가되었습니다.

`done()`
- Task가 완료되었으면 `True`를 반환합니다.
- 감싼 코루틴이 값을 반환하거나 예외를 일으키거나, Task가 취소되면 Task는 완료됩니다.
 
`result()`
- Task의 결과를 반환합니다.
- Task가 완료되었으면 감싼 코루틴의 결과가 반환됩니다 (또는 코루틴이 예외를 발생시켰으면 해당 예외가 다시 발생합니다).
- 태스크가 취소되었으면, 이 메서드는 [`CancelledError`](https://docs.python.org/ko/3/library/asyncio-exceptions.html#asyncio.CancelledError "asyncio.CancelledError") 예외를 발생시킵니다.
- If the Task's result isn't yet available, this method raises an [`InvalidStateError`](https://docs.python.org/ko/3/library/asyncio-exceptions.html#asyncio.InvalidStateError "asyncio.InvalidStateError") exception.

`exception()`
- Task의 예외를 반환합니다.
- 감싼 코루틴이 예외를 발생시키면, 그 예외가 반환됩니다. 감싼 코루틴이 정상적으로 반환되면, 이 메서드는 `None`을 반환합니다.
- 태스크가 취소되었으면, 이 메서드는 [`CancelledError`](https://docs.python.org/ko/3/library/asyncio-exceptions.html#asyncio.CancelledError "asyncio.CancelledError") 예외를 발생시킵니다.
- 태스크가 아직 완료되지 않았으면, 이 메서드는 [`InvalidStateError`](https://docs.python.org/ko/3/library/asyncio-exceptions.html#asyncio.InvalidStateError "asyncio.InvalidStateError") 예외를 발생시킵니다.

`add_done_callback(callback, *, context=None) (완료 콜백 추가)`
- 태스크가 완료될 때 실행할 콜백을 추가합니다.
- 이 메서드는 저수준 콜백 기반 코드에서만 사용해야 합니다.
- 자세한 내용은 [`Future.add_done_callback()`](https://docs.python.org/ko/3/library/asyncio-future.html#asyncio.Future.add_done_callback "asyncio.Future.add_done_callback") 설명서를 참조하십시오.

`remove_done_callback(callback)`
- 콜백 목록에서 callback을 제거합니다.
- 이 메서드는 저수준 콜백 기반 코드에서만 사용해야 합니다.
- 자세한 내용은 [`Future.remove_done_callback()`](https://docs.python.org/ko/3/library/asyncio-future.html#asyncio.Future.remove_done_callback "asyncio.Future.remove_done_callback") 설명서를 참조하십시오.

`get_stack(*, limit=None)`
- 이 Task의 스택 프레임 리스트를 돌려줍니다.
- 감싼 코루틴이 완료되지 않았으면, 일시 정지된 곳의 스택을 반환합니다. 코루틴이 성공적으로 완료되었거나 취소되었으면 빈 리스트가 반환됩니다. 코루틴이 예외로 종료되었으면, 이것은 트레이스백 프레임의 리스트를 반환합니다.
- 프레임은 항상 가장 오래된 것부터 순서대로 정렬됩니다.
- 일시 정지된 코루틴에서는 하나의 스택 프레임만 반환됩니다.
- 선택적 limit 인자는 반환할 최대 프레임 수를 설정합니다; 기본적으로 사용 가능한 모든 프레임이 반환됩니다. 반환되는 리스트의 순서는 스택과 트레이스백 중 어느 것이 반환되는지에 따라 다릅니다: 스택은 최신 프레임이 반환되지만, 트레이스백은 가장 오래된 프레임이 반환됩니다. (이는 traceback 모듈의 동작과 일치합니다.)

`print_stack(*, limit=None, file=None)`
- 이 Task의 스택이나 트레이스백을 인쇄합니다.
- 이것은 [`get_stack()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task.get_stack "asyncio.Task.get_stack")으로 얻은 프레임에 대해 traceback 모듈과 유사한 출력을 생성합니다.
- limit 인자는 [`get_stack()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task.get_stack "asyncio.Task.get_stack")에 직접 전달됩니다.
- The file argument is an I/O stream to which the output is written; by default output is written to [`sys.stdout`](https://docs.python.org/ko/3/library/sys.html#sys.stdout "sys.stdout").

`get_coro()`
- [`Task`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")로 싸인 코루틴 객체를 반환합니다.

> This will return `None` for Tasks which have already completed eagerly. See the [Eager Task Factory](https://docs.python.org/ko/3/library/asyncio-task.html#eager-task-factory).

> 버전 3.8에 추가되었습니다.
> 버전 3.12에서 변경: 새로 추가된 eager task execution은 결과가 `None`일 수 있음을 의미합니다.

`get_context()`
- 작업과 연관된 [`contextvars.Context`](https://docs.python.org/ko/3/library/contextvars.html#contextvars.Context “contextvars.Context”) 개체를 반환합니다.

> 버전 3.12에 추가되었습니다.

`get_name()`
- Task의 이름을 반환합니다.
- Task에 명시적으로 이름이 지정되지 않으면, 기본 asyncio Task 구현은 인스턴스화 중에 기본 이름을 생성합니다.

> 버전 3.8에 추가되었습니다.

`set_name(value)`
- Task의 이름을 설정합니다.
- value 인자는 모든 객체가 될 수 있으며, 문자열로 변환됩니다.
- 기본 Task 구현에서, 이름은 태스크 객체의 [`repr()`](https://docs.python.org/ko/3/library/functions.html#repr "repr") 출력에 표시됩니다.

> 버전 3.8에 추가되었습니다.

`cancel(msg=None)`
- Task 취소를 요청합니다.
- 이벤트 루프의 다음 사이클에서 감싼 코루틴으로 [`CancelledError`](https://docs.python.org/ko/3/library/asyncio-exceptions.html#asyncio.CancelledError "asyncio.CancelledError") 예외를 던져넣도록 합니다.
- 그런 다음 코루틴은 [`try`](https://docs.python.org/ko/3/reference/compound_stmts.html#try) ... ... `except CancelledError` ... [`finally`](https://docs.python.org/ko/3/reference/compound_stmts.html#finally) 블록으로 예외를 억제하여 요청을 정리하거나 거부할 기회를 갖습니다. 따라서 [`Future.cancel()`](https://docs.python.org/ko/3/library/asyncio-future.html#asyncio.Future.cancel “asyncio.Future.cancel”)와 달리 [`Task.cancel()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task.cancel “asyncio.Task.cancel”)는 태스크가 취소된다는 보장은 없지만 취소를 완전히 억제하는 것은 일반적이지 않으며 적극 권장하지 않습니다. 그럼에도 불구하고 코루틴이 취소를 억제하기로 결정한 경우 예외를 잡는 것 외에 [`Task.uncancel()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task.uncancel “asyncio.Task.uncancel”)을 호출해야 합니다.

> 버전 3.9에서 변경: msg 매개변수가 추가되었습니다.
> 버전 3.11에서 변경: msg 매개변수는 취소된 태스크에서 그 대기자로 전파됩니다.

- 다음 예는 코루틴이 취소 요청을 가로채는 방법을 보여줍니다:

```python
async def cancel_me():
    print('cancel_me(): before sleep')

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('cancel_me(): cancel sleep')
        raise
    finally:
        print('cancel_me(): after sleep')

async def main():
    # Create a "cancel_me" Task
    task = asyncio.create_task(cancel_me())

    # Wait for 1 second
    await asyncio.sleep(1)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main(): cancel_me is cancelled now")

asyncio.run(main())

# Expected output:
#
#     cancel_me(): before sleep
#     cancel_me(): cancel sleep
#     cancel_me(): after sleep
#     main(): cancel_me is cancelled now
```

`cancelled()`
- Task가 취소되었으면 `True`를 반환합니다.
- Task는 [`cancel()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task.cancel "asyncio.Task.cancel")로 취소가 요청되고 감싼 코루틴이 자신에게 전달된 [`CancelledError`](https://docs.python.org/ko/3/library/asyncio-exceptions.html#asyncio.CancelledError "asyncio.CancelledError") 예외를 확산할 때 취소됩니다.

`uncancel()`
- 이 Task에 대한 취소 요청 수를 감소시킵니다.
- 남아있는 취소 요청 수를 반환합니다.

> 취소된 태스크의 실행이 완료되면 이후 [uncancel()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task.uncancel "asyncio.Task.uncancel")을 호출해도 효과가 없습니다.

> 버전 3.11에 추가되었습니다.

- 이 메서드는 asyncio의 내부에서 사용되며 최종 사용자 코드에서 사용될 것으로 예상되지 않습니다.
- 특히, Task가 성공적으로 취소 해제되면 [Task Groups](https://docs.python.org/ko/3/library/asyncio-task.html#taskgroups)와 [asyncio.timeout()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.timeout "asyncio.timeout")과 같은 구조화된 동시성 요소가 계속 실행될 수 있어, 취소를 각 구조화된 블록으로 격리할 수 있습니다.
- 예를 들어:

```python
async def make_request_with_timeout():
    try:
        async with asyncio.timeout(1):
            # Structured block affected by the timeout:
            await make_request()
            await make_another_request()
    except TimeoutError:
        log("There was a timeout")
    # Outer code not affected by the timeout:
    await unrelated_code()
```

- make_request()와 make_another_request()가 있는 블록은 타임아웃으로 인해 취소될 수 있지만, unrelated_code()는 타임아웃 발생 시에도 계속 실행되어야 합니다.
- 이는 [uncancel()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task.uncancel "asyncio.Task.uncancel")을 사용하여 구현됩니다.
- [TaskGroup](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.TaskGroup "asyncio.TaskGroup") 컨텍스트 매니저도 비슷한 방식으로 [uncancel()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task.uncancel "asyncio.Task.uncancel")을 사용합니다.
- 최종 사용자 코드가 어떤 이유로 [CancelledError](https://docs.python.org/ko/3/library/asyncio-exceptions.html#asyncio.CancelledError "asyncio.CancelledError")를 잡아서 취소를 억제하는 경우, 취소 상태를 제거하기 위해 이 메서드를 호출해야 합니다.

`cancelling()`
- 이 Task에 대한 대기 중인 취소 요청 수를 반환합니다. 즉, [cancel()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task.cancel "asyncio.Task.cancel") 호출 횟수에서 [uncancel()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task.uncancel "asyncio.Task.uncancel") 호출 횟수를 뺀 값입니다.
- 이 숫자가 0보다 크지만 Task가 여전히 실행 중인 경우 [cancelled()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task.cancelled "asyncio.Task.cancelled")는 여전히 False를 반환한다는 점에 주의하세요.
- 이는 [uncancel()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task.uncancel "asyncio.Task.uncancel")을 호출하여 이 숫자를 낮출 수 있기 때문입니다. 취소 요청이 0으로 떨어지면 결국 태스크가 취소되지 않을 수 있습니다.
- 이 메서드는 asyncio의 내부에서 사용되며 최종 사용자 코드에서 사용될 것으로 예상되지 않습니다.
- 자세한 내용은 [uncancel()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task.uncancel "asyncio.Task.uncancel")을 참조하세요.

> 버전 3.11에 추가되었습니다.

### 스트림 (Stream)

- 스트림은 네트워크 연결로 작업하기 위해, async/await에서 사용할 수 있는 고수준 프리미티브입니다.
- 스트림은 콜백이나 저수준 프로토콜과 트랜스포트를 사용하지 않고 데이터를 송수신할 수 있게 합니다.
- 다음은 asyncio 스트림을 사용하여 작성된 TCP 메아리 클라이언트의 예입니다:

```python
import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client('Hello World!'))
```

**스트림 함수 (Stream Functions)**
- 다음 최상위 asyncio 함수를 사용하여 스트림을 만들고 작업할 수 있습니다:

(coroutine) `asyncio.open_connection(host=None, port=None, *, limit=None, ssl=None, family=0, proto=0, flags=0, sock=None, local_addr=None, server_hostname=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None, happy_eyeballs_delay=None, interleave=None)`

- 네트워크 연결을 만들고 (reader, writer) 객체 쌍을 반환합니다.
- 반환된 reader와 writer 객체는 [StreamReader](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.StreamReader "asyncio.StreamReader")와 [StreamWriter](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.StreamWriter "asyncio.StreamWriter") 클래스의 인스턴스입니다.
- limit는 반환된 [StreamReader](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.StreamReader "asyncio.StreamReader") 인스턴스가 사용하는 버퍼 크기 한계를 결정합니다. 기본적으로 limit는 64KiB로 설정됩니다.
- 나머지 인자는 [loop.create_connection()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection")로 직접 전달됩니다.

> sock 인자는 생성된 [StreamWriter](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.StreamWriter "asyncio.StreamWriter")에 소켓 소유권을 이전합니다. 소켓을 닫으려면 [close()](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.StreamWriter.close "asyncio.StreamWriter.close") 메서드를 호출하세요.

> 버전 3.7에서 변경: ssl_handshake_timeout 매개변수가 추가되었습니다.
> 버전 3.8에서 변경: happy_eyeballs_delay와 interleave 매개변수가 추가되었습니다.
> 버전 3.10에서 변경: loop 매개변수가 제거되었습니다.
> 버전 3.11에서 변경: ssl_shutdown_timeout 매개변수가 추가되었습니다.


(coroutine) `asyncio.start_server(client_connected_cb, host=None, port=None, *, limit=None, family=socket.AF_UNSPEC, flags=socket.AI_PASSIVE, sock=None, backlog=100, ssl=None, reuse_address=None, reuse_port=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None, start_serving=True)`

- 소켓 서버를 시작합니다.
- 새 클라이언트 연결이 만들어질 때마다 client_connected_cb 콜백이 호출됩니다.
- 이 콜백은 두 개의 인자로 (reader, writer) 쌍을 받는데, [StreamReader](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.StreamReader "asyncio.StreamReader")와 [StreamWriter](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.StreamWriter "asyncio.StreamWriter") 클래스의 인스턴스입니다.
- client_connected_cb는 일반 콜러블이나 [코루틴 함수](https://docs.python.org/ko/3/library/asyncio-task.html#coroutine)일 수 있습니다; 코루틴 함수면, 자동으로 [Task](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")로 예약됩니다.
- limit는 반환된 [StreamReader](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.StreamReader "asyncio.StreamReader") 인스턴스가 사용하는 버퍼 크기 한계를 결정합니다. 기본적으로 limit는 64KiB로 설정됩니다.
- 나머지 인자는 [loop.create_server()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server")로 직접 전달됩니다.

> sock 인자는 생성된 서버에 소켓 소유권을 이전합니다. 소켓을 닫으려면 서버의 [close()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Server.close "asyncio.Server.close") 메서드를 호출하세요.

> 버전 3.7에서 변경: ssl_handshake_timeout과 start_serving 매개변수가 추가되었습니다.
> 버전 3.10에서 변경: loop 매개변수가 제거되었습니다.
> 버전 3.11에서 변경: ssl_shutdown_timeout 매개변수가 추가되었습니다.

**유닉스 소켓 (Unix Sockets)**

(coroutine) `asyncio.open_unix_connection(path=None, *, limit=None, ssl=None, sock=None, server_hostname=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None)`

- 유닉스 소켓 연결을 만들고 (reader, writer) 쌍을 반환합니다.
- [open_connection()](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.open_connection "asyncio.open_connection")과 비슷하지만, 유닉스 소켓에서 작동합니다.
- [loop.create_unix_connection()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_connection "asyncio.loop.create_unix_connection")의 설명서도 참조하십시오.

> sock 인자는 생성된 [StreamWriter](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.StreamWriter "asyncio.StreamWriter")에 소켓 소유권을 이전합니다. 소켓을 닫으려면 [close()](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.StreamWriter.close "asyncio.StreamWriter.close") 메서드를 호출하세요.

> 가용성: 유닉스.

> 버전 3.7에서 변경: ssl_handshake_timeout 매개변수가 추가되었습니다. path 매개변수는 이제 [path-like object](https://docs.python.org/ko/3/glossary.html#term-path-like-object)가 될 수 있습니다.
> 버전 3.10에서 변경: loop 매개변수가 제거되었습니다.
> 버전 3.11에서 변경: ssl_shutdown_timeout 매개변수가 추가되었습니다.


(coroutine) `asyncio.start_unix_server(client_connected_cb, path=None, *, limit=None, sock=None, backlog=100, ssl=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None, start_serving=True)`

- 유닉스 소켓 서버를 시작합니다.
- [start_server()](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.start_server "asyncio.start_server")와 비슷하지만, 유닉스 소켓에서 작동합니다.
- [loop.create_unix_server()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_server "asyncio.loop.create_unix_server")의 설명서도 참조하십시오.

> sock 인자는 생성된 서버에 소켓 소유권을 이전합니다. 소켓을 닫으려면 서버의 [close()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Server.close "asyncio.Server.close") 메서드를 호출하세요.

> 가용성: 유닉스.

> 버전 3.7에서 변경: ssl_handshake_timeout과 start_serving 매개변수가 추가되었습니다. path 매개변수는 이제 [path-like object](https://docs.python.org/ko/3/glossary.html#term-path-like-object)가 될 수 있습니다.
> 버전 3.10에서 변경: loop 매개변수가 제거되었습니다.
> 버전 3.11에서 변경: ssl_shutdown_timeout 매개변수가 추가되었습니다.

#### StreamReader

`class asyncio.StreamReader`

- IO 스트림에서 데이터를 읽기 위한 API를 제공하는 리더 객체를 나타냅니다. 
- 비동기 이터러블 객체로서, async for 문을 지원합니다.
- StreamReader 객체를 직접 인스턴스화하는 것은 권장되지 않습니다. 대신 open_connection()과 start_server()를 사용하십시오.

`feed_eof()`

- EOF를 확인합니다.

(coroutine) `read(n=-1)`

- 스트림에서 최대 n 바이트를 읽습니다.
- n이 제공되지 않거나 -1로 설정된 경우, EOF까지 읽은 다음 모든 읽은 바이트를 반환합니다. EOF를 수신하고 내부 버퍼가 비어있으면 빈 bytes 객체를 반환합니다.
- n이 0이면 즉시 빈 bytes 객체를 반환합니다.
- n이 양수이면 내부 버퍼에 최소 1바이트가 사용 가능해지는 즉시 최대 n개의 사용 가능한 바이트를 반환합니다. 바이트를 읽기 전에 EOF를 수신하면 빈 bytes 객체를 반환합니다.

(coroutine) `readline()`

- 한 줄을 읽습니다. 여기서 "줄"은 `\n`로 끝나는 바이트의 시퀀스입니다.
- EOF를 수신했고 `\n`를 찾을 수 없으면, 이 메서드는 부분적으로 읽은 데이터를 반환합니다.
- EOF를 수신했고 내부 버퍼가 비어 있으면 빈 bytes 객체를 반환합니다.

(coroutine) `readexactly(n)`

- 정확히 n 바이트를 읽습니다.
- n 바이트를 읽기 전에 EOF에 도달하면, IncompleteReadError를 일으킵니다. 부분적으로 읽은 데이터를 가져오려면 IncompleteReadError.partial 어트리뷰트를 사용하십시오.

(coroutine) `readuntil(separator=b'\n')`
> 3.5.2 버전 추가

- separator가 발견될 때까지 스트림에서 데이터를 읽습니다.
- 성공하면, 데이터와 separator가 내부 버퍼에서 제거됩니다 (소비됩니다). 반환된 데이터에는 끝에 separator가 포함됩니다.
- 읽은 데이터의 양이 구성된 스트림 제한을 초과하면 LimitOverrunError 예외가 발생하고, 데이터는 내부 버퍼에 그대로 남아 있으며 다시 읽을 수 있습니다.
- 완전한 separator가 발견되기 전에 EOF에 도달하면 IncompleteReadError 예외가 발생하고, 내부 버퍼가 재설정됩니다. IncompleteReadError.partial 어트리뷰트에는 separator 일부가 포함될 수 있습니다.


`at_eof()`

- 버퍼가 비어 있고 feed_eof()가 호출되었으면 True를 반환합니다.

#### StreamWriter

`class asyncio.StreamWriter`

- IO 스트림에 데이터를 쓰는 API를 제공하는 기록기(writer) 객체를 나타냅니다.
- StreamWriter 객체를 직접 인스턴스화하는 것은 권장되지 않습니다. 대신 open_connection()과 start_server()를 사용하십시오.

`write(data)`

- 이 메서드는 하부 소켓에 data를 즉시 기록하려고 시도합니다. 실패하면, data는 보낼 수 있을 때까지 내부 쓰기 버퍼에 계류됩니다.
- 이 메서드는 drain() 메서드와 함께 사용해야 합니다:

```python
stream.write(data)
await stream.drain()
```

`writelines(data)`

- 이 메서드는 하부 소켓에 바이트열의 리스트(또는 임의의 이터러블)를 즉시 기록합니다. 실패하면, data는 보낼 수 있을 때까지 내부 쓰기 버퍼에 계류됩니다.
- 이 메서드는 drain() 메서드와 함께 사용해야 합니다:

```python
stream.writelines(lines)
await stream.drain()
```

`close()`

- 이 메서드는 스트림과 하부 소켓을 닫습니다.
- 이 메서드는 필수는 아니지만 wait_closed() 메서드와 함께 사용해야 합니다:

```python
stream.close()
await stream.wait_closed()
```

`can_write_eof()`

- 하부 트랜스포트가 write_eof() 메서드를 지원하면 True를 반환하고, 그렇지 않으면 False를 반환합니다.

`write_eof()`

- 버퍼링 된 쓰기 데이터가 플러시 된 후에 스트림의 쓰기 끝을 닫습니다.

`transport`

- 하부 asyncio 트랜스포트를 돌려줍니다.

`get_extra_info(name, default=None)`

- 선택적 트랜스포트 정보에 액세스합니다; 자세한 내용은 [BaseTransport.get_extra_info()](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.BaseTransport.get_extra_info)를 참조하십시오.

(coroutine) `drain()`

- 스트림에 기록을 다시 시작하는 것이 적절할 때까지 기다립니다. 예:

```python
writer.write(data)
await writer.drain()
```

- 이것은 하부 IO 쓰기 버퍼와 상호 작용하는 흐름 제어 메서드입니다. 버퍼의 크기가 높은 수위에 도달하면, 버퍼 크기가 낮은 수위까지 내려가서 쓰기가 다시 시작될 수 있을 때까지 drain()은 블록합니다. 기다릴 것이 없으면, drain()은 즉시 반환합니다.

(coroutine) `start_tls(sslcontext, *, server_hostname=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None)`

- 기존의 스트림 기반 연결을 TLS로 업그레이드합니다.

매개변수:
- sslcontext: 구성된 SSLContext 인스턴스.
- server_hostname: 대상 서버의 인증서와 일치시킬 호스트 이름을 설정하거나 재정의합니다.
- ssl_handshake_timeout: TLS 핸드셰이크가 완료될 때까지 기다리는 시간(초)입니다. None이면 60.0초(기본값).
- ssl_shutdown_timeout: SSL 셧다운이 완료될 때까지 기다리는 시간(초)입니다. None이면 30.0초(기본값).

> 버전 3.11에서 추가되었습니다.
> 버전 3.12에서 변경: ssl_shutdown_timeout 매개변수가 추가되었습니다.

`is_closing()`

- 스트림이 닫혔거나 닫히고 있으면 True를 반환합니다.

> 버전 3.7에서 추가되었습니다.

(coroutine) `wait_closed()`

- 스트림이 닫힐 때까지 기다립니다.
- close() 후에 호출되어야 하며, 기본 연결이 닫힐 때까지 기다립니다. 예를 들어 프로그램을 종료하기 전에 모든 데이터가 플러시되었는지 확인합니다.

> 버전 3.7에서 추가되었습니다.


### 동기화 프리미티브
- asyncio 동기화 프리미티브는 [`threading`](https://docs.python.org/ko/3/library/threading.html#module-threading "threading: Thread-based parallelism.") 모듈의 것과 유사하도록 설계되었습니다만 두 가지 중요한 주의 사항이 있습니다:
	- asyncio 프리미티브는 스레드 안전하지 않으므로, OS 스레드 동기화(이를 위해서는 [`threading`](https://docs.python.org/ko/3/library/threading.html#module-threading "threading: Thread-based parallelism.")을 사용하십시오)에 사용하면 안 됩니다.
	- 이러한 동기화 프리미티브의 메서드는 _timeout_ 인자를 받아들이지 않습니다; [`asyncio.wait_for()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.wait_for "asyncio.wait_for") 함수를 사용하여 시간제한이 있는 연산을 수행하십시오.
- asyncio에는 다음과 같은 기본 동기화 프리미티브가 있습니다:
	- [`Lock`](https://docs.python.org/ko/3/library/asyncio-sync.html#asyncio.Lock "asyncio.Lock")
	- [`Event`](https://docs.python.org/ko/3/library/asyncio-sync.html#asyncio.Event "asyncio.Event")
	- [`Condition`](https://docs.python.org/ko/3/library/asyncio-sync.html#asyncio.Condition "asyncio.Condition")
	- [`Semaphore`](https://docs.python.org/ko/3/library/asyncio-sync.html#asyncio.Semaphore "asyncio.Semaphore")
	- [`BoundedSemaphore`](https://docs.python.org/ko/3/library/asyncio-sync.html#asyncio.BoundedSemaphore "asyncio.BoundedSemaphore")
	- [`Barrier`](https://docs.python.org/ko/3/library/asyncio-sync.html#asyncio.Barrier "asyncio.Barrier")
 
#### 락 (Lock)

##### `class asyncio.Lock`

- asyncio 태스크를 위한 뮤텍스 락을 구현합니다.
- 스레드 안전하지 않습니다.
- asyncio 락은 공유 자원에 대한 독점 액세스를 보장하는 데 사용될 수 있습니다.

Lock을 사용하는 가장 좋은 방법은 `async with` 문입니다:

```python
lock = asyncio.Lock()

# … 나중에
async with lock:
    # 공유 상태에 접근
```

이는 다음과 동등합니다:

```python
lock = asyncio.Lock()

# … 나중에
await lock.acquire()
try:
    # 공유 상태에 접근
finally:
    lock.release()
```

> 버전 3.10에서 변경: loop 매개변수가 제거되었습니다.

(coroutine) `acquire()`

- 락을 얻습니다.
- 이 메서드는 락이 풀림(unlocked)이 될 때까지 기다리고, 잠김(locked)으로 설정한 다음 True를 반환합니다.
- 잠금이 해제되기를 기다리는 acquire()에서 둘 이상의 코루틴 블록 될 때, 결국 한 개의 코루틴만 진행됩니다.
- 락을 얻는 것은 공평(fair)합니다: 진행할 코루틴은 락을 기다리기 시작한 첫 번째 코루틴이 됩니다.

`release()`

- 락을 반납합니다.
- 락이 잠김(locked)이면 풀림(unlocked)으로 재설정하고 돌아옵니다.
- 락이 풀림(unlocked)이면 RuntimeError가 발생합니다.

`locked()`

- 락이 잠김(locked)이면 True를 반환합니다.

#### 이벤트 (Event)

##### `class asyncio.Event`

- 이벤트 객체. 스레드 안전하지 않습니다.
- asyncio 이벤트는 어떤 이벤트가 발생했음을 여러 asyncio 태스크에 알리는 데 사용할 수 있습니다.
- Event 객체는 set() 메서드로 참으로 설정하고 clear() 메서드로 거짓으로 재설정할 수 있는 내부 플래그를 관리합니다.
- wait() 메서드는 플래그가 참으로 설정될 때까지 블록합니다. 플래그는 초기에 거짓으로 설정됩니다.

> 버전 3.10에서 변경: loop 매개변수가 제거되었습니다.

예:

```python
async def waiter(event):
    print('waiting for it …')
    await event.wait()
    print('… got it!')

async def main():
    # Event 객체 생성
    event = asyncio.Event()

    # 'event'가 설정될 때까지 기다리는 Task 생성
    waiter_task = asyncio.create_task(waiter(event))

    # 1초 동안 대기 후 이벤트 설정
    await asyncio.sleep(1)
    event.set()

    # waiter 태스크가 완료될 때까지 대기
    await waiter_task

asyncio.run(main())
```

(coroutine) `wait()`

- 이벤트가 설정될 때까지 기다립니다.
- 이벤트가 설정되었으면 True를 즉시 반환합니다. 그렇지 않으면 다른 태스크가 set()을 호출할 때까지 블록합니다.

`set()`

- 이벤트를 설정합니다.
- 이벤트가 설정되기를 기다리는 모든 태스크는 즉시 깨어납니다.

`clear()`

- 이벤트를 지웁니다 (재설정).
- 이제 wait()를 기다리는 태스크는 set() 메서드가 다시 호출될 때까지 블록 됩니다.

`is_set()`

- 이벤트가 설정되면 True를 반환합니다.

#### 조건 (Condition)

##### `class asyncio.Condition(lock=None)`

- Condition 객체. 스레드 안전하지 않습니다.
- asyncio 조건 프리미티브는 태스크가 어떤 이벤트가 발생하기를 기다린 다음 공유 자원에 독점적으로 액세스하는데 사용할 수 있습니다.
- 본질에서, Condition 객체는 Event와 Lock의 기능을 결합합니다.
- 여러 개의 Condition 객체가 하나의 Lock을 공유할 수 있으므로, 공유 자원의 특정 상태에 관심이 있는 다른 태스크 간에 공유 자원에 대한 독점적 액세스를 조정할 수 있습니다.
- 선택적 lock 인자는 Lock 객체나 None이어야 합니다. 후자의 경우 새로운 Lock 객체가 자동으로 만들어집니다.

> 버전 3.10에서 변경: loop 매개변수가 제거되었습니다.

Condition을 사용하는 가장 좋은 방법은 `async with` 문입니다:

```python
cond = asyncio.Condition()

# … 나중에
async with cond:
    await cond.wait()
```

이는 다음과 동등합니다:

```python
cond = asyncio.Condition()

# … 나중에
await cond.acquire()
try:
    await cond.wait()
finally:
    cond.release()
```

(coroutine) `acquire()`

- 하부 락을 얻습니다.
- 이 메서드는 하부 락이 풀림(unlocked)이 될 때까지 대기하고, 잠김(locked)으로 설정한 다음 True를 반환합니다.

`notify(n=1)`

- 이 조건을 기다리는 최대 n 태스크(기본적으로 1개)를 깨웁니다. 대기 중인 태스크가 없으면 이 메서드는 no-op입니다.
- 이 메서드를 호출하기 전에 락을 얻어야 하고, 호출 직후에 반납해야 합니다. 풀린(unlocked) 락으로 호출하면 RuntimeError 에러가 발생합니다.

`locked()`

- 하부 락을 얻었으면 True를 돌려줍니다.

`notify_all()`

- 이 조건에 대기 중인 모든 태스크를 깨웁니다.
- 이 메서드는 notify()처럼 작동하지만, 대기 중인 모든 태스크를 깨웁니다.
- 이 메서드를 호출하기 전에 락을 얻어야 하고, 호출 직후에 반납해야 합니다. 풀린(unlocked) 락으로 호출하면 RuntimeError 에러가 발생합니다.

`release()`

- 하부 락을 반납합니다.
- 풀린 락으로 호출하면, RuntimeError가 발생합니다.

`coroutine wait()`

- 알릴 때까지 기다립니다.
- 이 메서드가 호출될 때 호출하는 태스크가 락을 얻지 않았으면 RuntimeError가 발생합니다.
- 이 메서드는 하부 잠금을 반납한 다음, notify()나 notify_all() 호출 때문에 깨어날 때까지 블록합니다.
- 일단 깨어나면, Condition은 락을 다시 얻고, 이 메서드는 True를 돌려줍니다.

(coroutine) `wait_for(predicate)`

- predicate가 참이 될 때까지 기다립니다.
- predicate는 논릿값으로 해석될 결과를 돌려주는 콜러블이어야 합니다. 최종값이 반환 값입니다.

#### 세마포어 (Semaphore)

`class asyncio.Semaphore(value=1)`

- Semaphore 객체. 스레드 안전하지 않습니다.
- 세마포어는 각 acquire() 호출로 감소하고, 각 release() 호출로 증가하는 내부 카운터를 관리합니다.
- 카운터는 절대로 0 밑으로 내려갈 수 없습니다; acquire()가 0을 만나면, release()를 호출할 때까지 기다리면서 블록합니다.
- 선택적 value 인자는 내부 카운터의 초깃값을 제공합니다 (기본적으로 1). 지정된 값이 0보다 작으면 ValueError가 발생합니다.

> 버전 3.10에서 변경: loop 매개변수가 제거되었습니다.

Semaphore를 사용하는 가장 좋은 방법은 `async with` 문입니다:

```python
sem = asyncio.Semaphore(10)

# … 나중에
async with sem:
    # 공유 자원으로 작업
```

이는 다음과 동등합니다:

```python
sem = asyncio.Semaphore(10)

# … 나중에
await sem.acquire()
try:
    # 공유 자원으로 작업
finally:
    sem.release()
```

(coroutine) `acquire()`

- 세마포어를 얻습니다.
- 내부 카운터가 0보다 크면, 1 감소시키고 True를 즉시 반환합니다.
- 0이면, release()가 호출될 때까지 기다린 다음 True를 반환합니다.

`locked()`

- 세마포어를 즉시 얻을 수 없으면 True를 반환합니다.

`release()`

- 세마포어를 반납하고 내부 카운터를 1 증가시킵니다.
- 세마포어를 얻기 위해 대기하는 태스크를 깨울 수 있습니다.
- BoundedSemaphore와 달리, Semaphore는 acquire() 호출보다 더 많은 release() 호출을 허용합니다.

#### BoundedSemaphore (제한된 세마포어)

- BoundedSemaphore 객체는 제한된 세마포어를 나타냅니다. 스레드 안전하지 않습니다.
- 제한된 세마포어는 초기 value 위로 내부 카운터를 증가시키면 release()에서 ValueError를 발생시키는 Semaphore 버전입니다.

> 버전 3.10에서 변경: loop 매개변수가 제거되었습니다.

#### Barrier (장벽)

- 장벽 객체입니다. 스레드 안전하지 않습니다.
- 장벽은 parties 수의 태스크가 대기할 때까지 블록하는 간단한 동기화 프리미티브입니다.
- 태스크는 wait() 메서드에서 대기할 수 있으며, 지정된 수의 태스크가 wait()에서 대기할 때까지 블록됩니다.
- 그 시점에 모든 대기 중인 태스크가 동시에 블록 해제됩니다.
- async with를 wait()를 기다리는 대안으로 사용할 수 있습니다.
- 장벽은 여러 번 재사용할 수 있습니다.

예:

```python
async def example_barrier():
   # barrier with 3 parties
   b = asyncio.Barrier(3)

   # create 2 new waiting tasks
   asyncio.create_task(b.wait())
   asyncio.create_task(b.wait())

   await asyncio.sleep(0)
   print(b)

   # The third .wait() call passes the barrier
   await b.wait()
   print(b)
   print("barrier passed")

   await asyncio.sleep(0)
   print(b)

asyncio.run(example_barrier())
```

이 예제의 결과는 다음과 같습니다:

```
<asyncio.locks.Barrier object at 0x… [filling, waiters:2/3]>
<asyncio.locks.Barrier object at 0x… [draining, waiters:0/3]>
barrier passed
<asyncio.locks.Barrier object at 0x… [filling, waiters:0/3]>
```

> 버전 3.11에서 추가되었습니다.

`wait()`

- 장벽을 통과합니다. 장벽에 참여하는 모든 태스크가 이 함수를 호출하면 모두 동시에 블록 해제됩니다.
- 장벽에서 대기 중이거나 블록된 태스크가 취소되면 이 태스크는 동일한 상태를 유지하는 장벽을 빠져나갑니다.
- 장벽의 상태가 "filling"이면 대기 중인 태스크 수가 1 감소합니다.
- 반환 값은 0에서 parties-1 범위의 정수로, 각 태스크마다 다릅니다.
- 이는 특별한 정리 작업을 수행할 태스크를 선택하는 데 사용할 수 있습니다.

예:

```python
async with barrier as position:
   if position == 0:
      # Only one task prints this
      print('End of *draining phase*')
```

- 이 메서드는 태스크가 대기하는 동안 장벽이 깨지거나 재설정되면 BrokenBarrierError 예외를 발생시킬 수 있습니다.
- 태스크가 취소되면 CancelledError를 발생시킬 수 있습니다.

`reset()`

- 장벽을 기본 빈 상태로 되돌립니다.
- 대기 중인 모든 태스크는 BrokenBarrierError 예외를 받게 됩니다.
- 장벽이 깨진 경우 그냥 두고 새로 만드는 것이 더 나을 수 있습니다.

`abort()`

- 장벽을 깨진 상태로 만듭니다.
- 이로 인해 wait()에 대한 활성 또는 향후 호출이 BrokenBarrierError로 실패하게 됩니다.
- 예를 들어 태스크 중 하나가 중단해야 하는 경우 무한 대기 태스크를 피하기 위해 사용합니다.

`parties`

- 장벽을 통과하는 데 필요한 태스크 수입니다.

`n_waiting`

- 채우는 동안 현재 장벽에서 대기 중인 태스크 수입니다.

`broken`

- 장벽이 깨진 상태이면 True인 부울 값입니다.

`BrokenBarrierError`

- 이 예외는 RuntimeError의 하위 클래스로, Barrier 객체가 재설정되거나 깨질 때 발생합니다.

> 버전 3.9에서 변경: await lock이나 yield from lock 및/또는 with 문(with await lock, with (yield from lock))을 사용하여 록을 얻는 것은 제거되었습니다. 대신 async with lock을 사용하십시오.

### 서브 프로세스 (Subprocess)
- 서브 프로세스를 만들고 관리하기 위한 고수준 async/await asyncio API에 관해 설명합니다.
- 다음은 asyncio가 셸 명령을 실행하고 결과를 얻는 방법의 예입니다:

```python
import asyncio

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')

asyncio.run(run('ls /zzz'))
```

는 다음과 같이 인쇄할 것입니다:

```
['ls /zzz' exited with 1]
[stderr]
ls: /zzz: No such file or directory
```

- 모든 asyncio 서브 프로세스 함수는 비동기이고, asyncio가 이러한 함수로 작업 할 수 있는 많은 도구를 제공하기 때문에, 여러 서브 프로세스를 병렬로 실행하고 감시하기가 쉽습니다. 여러 명령을 동시에 실행하도록 위 예제를 수정하는 것은 아주 간단합니다:

```python
async def main():
    await asyncio.gather(
        run('ls /zzz'),
        run('sleep 1; echo "hello"'))

asyncio.run(main())
```

[예제](https://docs.python.org/ko/3/library/asyncio-subprocess.html#examples) 하위 절도 참조하십시오.

#### 서브 프로세스 만들기 (Creating subprocesses)

(coroutine) `asyncio.create_subprocess_exec(program, *args, stdin=None, stdout=None, stderr=None, limit=None, **kwds)`

- 서브 프로세스를 만듭니다.
- limit 인자는 Process.stdout과 Process.stderr를 위한 StreamReader 래퍼의 버퍼 제한을 설정합니다 (subprocess.PIPE가 stdout과 stderr 인자로 전달된 경우).
- Process 인스턴스를 반환합니다.
- 다른 매개 변수에 관해서는 loop.subprocess_exec()의 설명서를 참조하십시오.

> 버전 3.10에서 변경: loop 매개변수가 제거되었습니다.

(coroutine) `asyncio.create_subprocess_shell(cmd, stdin=None, stdout=None, stderr=None, limit=None, **kwds)`
- cmd 셸 명령을 실행합니다.
- limit 인자는 Process.stdout과 Process.stderr를 위한 StreamReader 래퍼의 버퍼 제한을 설정합니다 (subprocess.PIPE가 stdout과 stderr 인자로 전달된 경우).
- Process 인스턴스를 반환합니다.
- 다른 매개 변수에 관해서는 loop.subprocess_shell()의 설명서를 참조하십시오.

> [!important] 
> - 셸 주입 취약점을 피하고자 모든 공백과 특수 문자를 적절하게 따옴표로 감싸는 것은 응용 프로그램의 책임입니다. shlex.quote() 함수는 셸 명령을 구성하는 데 사용될 문자열의 공백 문자와 특수 셸 문자를 올바르게 이스케이프 하는 데 사용할 수 있습니다.

> 버전 3.10에서 변경: loop 매개변수가 제거되었습니다.


> [!NOTE]
> - ProactorEventLoop를 쓰면 윈도우에서 서브 프로세스를 사용할 수 있습니다. 자세한 내용은 윈도우에서의 서브 프로세스 지원을 참조하십시오.

> [!seealso] 
> - 또한, asyncio에는 서브 프로세스와 함께 작동하는 다음과 같은 저수준 API가 있습니다: 서브 프로세스 트랜스포트와 서브 프로세스 프로토콜 뿐만 아니라 loop.subprocess_exec(), loop.subprocess_shell(), loop.connect_read_pipe(), loop.connect_write_pipe().

#### 상수 (Constants)

`asyncio.subprocess.PIPE`
- stdin, stdout 또는 stderr 매개 변수로 전달될 수 있습니다.
- PIPE가 stdin 인자로 전달되면, Process.stdin 어트리뷰트는 StreamWriter 인스턴스를 가리킵니다.
- PIPE가 stdout이나 stderr 인자로 전달되면, Process.stdout과 Process.stderr 어트리뷰트는 StreamReader 인스턴스를 가리킵니다.

`asyncio.subprocess.STDOUT`
- stderr 인자로 사용할 수 있는 특수 값이며, 표준 에러를 표준 출력으로 리디렉션해야 함을 나타냅니다.

`asyncio.subprocess.DEVNULL`
- 프로세스 생성 함수의 stdin, stdout 또는 stderr 인자로 사용할 수 있는 특수 값입니다. 특수 파일 os.devnull이 해당 서브 프로세스 스트림에 사용됨을 나타냅니다.

#### 서브 프로세스와 상호 작용하기 (Interacting with subprocesses)
- create_subprocess_exec()와 create_subprocess_shell() 함수는 모두 Process 클래스의 인스턴스를 반환합니다. Process는 서브 프로세스와 통신하고 완료를 관찰할 수 있는 고수준 래퍼입니다.

`class asyncio.subprocess.Process`
- create_subprocess_exec()와 create_subprocess_shell() 함수로 만들어진 OS 프로세스를 감싸는 객체.
- 이 클래스는 subprocess.Popen 클래스와 비슷한 API를 갖도록 설계되었지만, 주목할만한 차이점이 있습니다:
	- Popen과 달리, Process 인스턴스에는 poll() 메서드와 동등한 것이 없습니다;
	- `communicate()` 및 `wait()` 메서드에 시간 초과 매개변수가 없는 경우 `wait_for()` 함수를 사용합니다;
	- Process.wait() 메서드는 비동기이지만, subprocess.Popen.wait() 메서드는 블로킹 비지 루프(blocking busy loop)로 구현됩니다;
	- universal_newlines 매개 변수는 지원되지 않습니다.
- 이 클래스는 스레드 안전하지 않습니다.
- 서브 프로세스와 스레드 절도 참조하십시오.

(coroutine) `wait()`
- 자식 프로세스가 종료할 때까지 기다립니다.
- returncode 어트리뷰트를 설정하고 반환합니다.

> [!NOTE]
> - 이 메서드는 stdout=PIPE나 stderr=PIPE를 사용하고 자식 프로세스가 너무 많은 출력을 만들면 교착 상태가 될 수 있습니다. 자식 프로세스는 OS 파이프 버퍼가 더 많은 데이터를 받아들이도록 기다리면서 블록 됩니다. 이 조건을 피하고자, 파이프를 사용할 때는 communicate() 메서드를 사용하십시오.

(coroutine) `communicate(input=None)`
- 프로세스와 상호 작용합니다:
	1. 데이터를 stdin으로 보냅니다 (input이 None이 아니면);
	2. closes stdin;
	3. EOF에 도달할 때까지 stdout과 stderr에서 데이터를 읽습니다;
	4. 프로세스가 종료할 때까지 기다립니다.
- 선택적 input 인자는 자식 프로세스로 전송될 데이터(bytes 객체)입니다.
- 튜플 `(stdout_data, stderr_data)`를 반환합니다.
- input을 stdin에 쓸 때 `BrokenPipeError`나 `ConnectionResetError` 예외가 발생하면, 예외를 무시합니다. 이 조건은 모든 데이터가 stdin에 기록되기 전에 프로세스가 종료할 때 발생합니다.
- 프로세스의 stdin으로 데이터를 보내려면, 프로세스를 `stdin=PIPE`로 만들어야 합니다. 마찬가지로, 결과 튜플에서 None 이외의 것을 얻으려면, `stdout=PIPE` 와/나 `stderr=PIPE` 인자를 사용하여 프로세스를 만들어야 합니다.
- 데이터가 메모리에 버퍼링 되므로, 데이터 크기가 크거나 무제한이면 이 메서드를 사용하지 마십시오.

> 버전 3.12에서 변경: stdin gets closed when input=None too.

다음은 요청하신 조건에 따라 번역한 내용입니다:

`send_signal(signal)`
- 시그널 signal를 자식 프로세스로 보냅니다.

> [!NOTE]
> - 윈도우에서 SIGTERM은 terminate()의 별칭입니다. CTRL_C_EVENT와 CTRL_BREAK_EVENT는 CREATE_NEW_PROCESS_GROUP을 포함하는 creationflags 매개변수로 시작된 프로세스에 보낼 수 있습니다.

`terminate()`
- 자식 프로세스를 중지합니다.
- POSIX 시스템에서 이 메서드는 SIGTERM을 자식 프로세스로 보냅니다.
- 윈도우에서는 자식 프로세스를 중지하기 위해 Win32 API 함수 TerminateProcess()가 호출됩니다.

`kill()`
- 자식 프로세스를 강제 종료합니다.
- POSIX 시스템에서 이 메서드는 SIGKILL을 자식 프로세스로 보냅니다.
- 윈도우에서 이 메서드는 terminate()의 별칭입니다.

`stdin`
- 표준 입력 스트림(StreamWriter) 또는 프로세스가 stdin=None으로 만들어졌으면 None.

`stdout`
- 표준 출력 스트림(StreamReader) 또는 프로세스가 stdout=None으로 만들어졌으면 None.

`stderr`
- 표준 에러 스트림(StreamReader) 또는 프로세스가 stderr=None으로 만들어졌으면 None.

> [!warning]
> - process.stdin.write(), await process.stdout.read() 또는 await process.stderr.read() 대신 communicate() 메서드를 사용하세요. 이는 스트림이 읽기나 쓰기를 일시 중지하고 자식 프로세스를 차단하여 발생하는 교착 상태를 방지합니다.

`pid`
- 프로세스 식별 번호 (PID).
- `create_subprocess_shell()` 함수로 만들어진 프로세스의 경우, 이 어트리뷰트는 생성된 셸의 PID입니다.

`returncode`
- 프로세스가 종료할 때의 반환 코드.
- `None` 값은 프로세스가 아직 종료하지 않았음을 나타냅니다.
- 음수 값 `-N`은 자식이 시그널 `N`으로 종료되었음을 나타냅니다 (POSIX만 해당).

##### 서브 프로세스와 스레드 (Subprocess and threads)
- 표준 asyncio 이벤트 루프는 기본적으로 다른 스레드에서 서브 프로세스를 실행하는 것을 지원합니다.
- 윈도우에서 서브 프로세스는 [ProactorEventLoop](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop)(기본값)에서만 제공되며, [SelectorEventLoop](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop)에는 서브 프로세스 지원이 없습니다.
- 유닉스에서 child watchers는 서브 프로세스 종료 대기에 사용됩니다. 자세한 정보는 [프로세스 감시자](https://docs.python.org/ko/3/library/asyncio-policy.html#asyncio-watchers)를 참조하십시오.

> 버전 3.8에서 변경: 유닉스는 제한 없이 다른 스레드에서 서브 프로세스를 스폰하기 위해 [ThreadedChildWatcher](https://docs.python.org/ko/3/library/asyncio-policy.html#asyncio.ThreadedChildWatcher)를 사용하도록 전환했습니다.

- 활성화되지 않은 현재 자식 감시자를 사용하여 서브 프로세스를 스폰하면 [RuntimeError](https://docs.python.org/ko/3/library/exceptions.html#RuntimeError)가 발생합니다.
- 대체 이벤트 루프 구현에는 나름의 제한 사항이 있을 수 있습니다; 해당 설명서를 참조하십시오.

> [asyncio의 동시성과 다중 스레드](https://docs.python.org/ko/3/library/asyncio-dev.html#asyncio-multithreading) 절.

### 큐 (Queue)
- asyncio 큐는 [`queue`](https://docs.python.org/ko/3/library/queue.html#module-queue "queue: A synchronized queue class.") 모듈의 클래스와 유사하도록 설계되었습니다. asyncio 큐는 스레드 안전하지 않지만, async/await 코드에서 사용되도록 설계되었습니다.
- asyncio 큐의 메서드에는 _timeout_ 매개 변수가 없습니다; 시간제한이 있는 큐 연산을 하려면 [`asyncio.wait_for()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.wait_for "asyncio.wait_for") 함수를 사용하십시오.

`class asyncio.Queue(maxsize=0)`
- 선입 선출 (FIFO) 큐.
- maxsize가 0보다 작거나 같으면 큐 크기는 무한합니다. 0보다 큰 정수면, 큐가 maxsize에 도달했을 때 get()이 항목을 제거할 때까지 await put()이 블록합니다.
- 표준 라이브러리의 스레드를 쓰는 queue와는 달리, 큐의 크기는 항상 알려져 있으며 qsize() 메서드를 호출하여 얻을 수 있습니다.

> 버전 3.10에서 변경: Removed the loop parameter.

- 이 클래스는 스레드 안전하지 않습니다.

`maxsize`

- 큐에 허용되는 항목 수.

`empty()`
- 큐가 비어 있으면 True를 반환하고, 그렇지 않으면 False를 반환합니다.

`full()`
- 큐에 maxsize 항목이 있으면 True를 반환합니다.
- 큐가 maxsize=0 (기본값)으로 초기화되었으면, full()은 절대 True를 반환하지 않습니다.

`coroutine get()`
- 큐에서 항목을 제거하고 반환합니다. 큐가 비어 있으면, 항목이 들어올 때까지 기다립니다.

`get_nowait()`
- 항목을 즉시 사용할 수 있으면 항목을 반환하고, 그렇지 않으면 QueueEmpty를 발생시킵니다.

(coroutine) `join()`
- 큐의 모든 항목을 수신하여 처리할 때까지 블록합니다.
- 완료되지 않은 작업 수는 항목이 큐에 추가될 때마다 증가합니다. 이 수는 소비자 코루틴이 항목을 수신했고 그 항목에 관한 작업이 모두 완료되었음을 나타내는 task_done()를 호출할 때마다 감소합니다. 완료되지 않은 작업 수가 0으로 떨어지면 join()가 블록 해제됩니다.

(coroutine) `put(item)`
- 큐에 항목을 넣습니다. 큐가 가득 차면, 항목을 추가할 빈자리가 생길 때까지 기다립니다.

`put_nowait(item)`
- 블록하지 않고 항목을 큐에 넣습니다.
- 자리가 즉시 나지 않으면, QueueFull를 일으킵니다.

`qsize()`
- 큐에 있는 항목 수를 돌려줍니다.

`task_done()`
- 이전에 큐에 넣은 작업이 완료되었음을 나타냅니다.
- 큐 소비자가 사용합니다. 작업을 꺼내는 데 사용된 get() 마다, 뒤따르는 task_done() 호출은 작업에 관한 처리가 완료되었음을 큐에 알려줍니다.
- join()이 현재 블록 중이면, 모든 항목이 처리될 때 다시 시작됩니다 (큐에 put()한 모든 항목에 대해 task_done() 호출이 수신되었음을 뜻합니다).
- 큐에 넣은 항목보다 더 많이 호출되면 ValueError를 발생시킵니다.

##### 우선순위 큐 (Priority Queue)

`class asyncio.PriorityQueue`
- Queue의 변형; 우선순위 순서로 항목을 꺼냅니다 (가장 낮은 우선순위가 처음입니다).
- 엔트리는 일반적으로 (priority_number, data) 형식의 튜플입니다.

##### LIFO 큐 (LIFO Queue)

`class asyncio.LifoQueue`
- 가장 최근에 추가된 항목을 먼저 꺼내는 Queue의 변형 (후입 선출).

##### 예외 (Exceptions)
`exception asyncio.QueueEmpty`
- 이 예외는 `get_nowait()` 메서드가 빈 큐에 호출될 때 발생합니다.

`exception asyncio.QueueFull`
- `put_nowait()` 메서드가 maxsize에 도달한 큐에 호출될 때 발생하는 예외입니다.

### 예외 (Exceptions)
> **소스 코드:** [Lib/asyncio/exceptions.py](https://github.com/python/cpython/tree/3.12/Lib/asyncio/exceptions.py)

`asyncio.TimeoutError`
- 주어진 기한을 초과했을 때 발생하는 TimeoutError의 더 이상 사용되지 않는 별칭입니다.

> 버전 3.11에서 변경: 이 클래스는 [TimeoutError](https://docs.python.org/ko/3/library/exceptions.html#TimeoutError)의 별칭이 되었습니다.

`asyncio.CancelledError`
- 작업이 취소되었습니다.
- 이 예외는 asyncio 태스크가 취소될 때 사용자 정의 작업을 수행하기 위해 잡을 수 있습니다. 거의 모든 상황에서 예외를 다시 일으켜야 합니다.

> 버전 3.8에서 변경: [CancelledError](https://docs.python.org/ko/3/library/asyncio-exceptions.html#asyncio.CancelledError)는 이제 [Exception](https://docs.python.org/ko/3/library/exceptions.html#Exception)이 아닌 [BaseException](https://docs.python.org/ko/3/library/exceptions.html#BaseException)의 서브클래스입니다.

`asyncio.InvalidStateError`
- [Task](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task)나 [Future](https://docs.python.org/ko/3/library/asyncio-future.html#asyncio.Future)의 내부 상태가 잘못되었습니다.
- 이미 결괏값이 설정된 Future 객체에 대해 결괏값을 설정하는 것과 같은 상황에서 발생할 수 있습니다.

`asyncio.SendfileNotAvailableError`
- 주어진 소켓이나 파일 유형에서는 "sendfile" 시스템 호출을 사용할 수 없습니다.
- [RuntimeError](https://docs.python.org/ko/3/library/exceptions.html#RuntimeError)의 서브 클래스입니다.

`asyncio.IncompleteReadError`
- 요청한 읽기 작업이 완전히 완료되지 않았습니다.
- [asyncio 스트림 API](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio-streams)가 일으킵니다.
- 이 예외는 [EOFError](https://docs.python.org/ko/3/library/exceptions.html#EOFError)의 서브 클래스입니다.

`expected`
- 기대하는 바이트의 총수 ([int](https://docs.python.org/ko/3/library/functions.html#int)).

`partial
- 스트림이 끝나기 전에 읽은 [bytes](https://docs.python.org/ko/3/library/stdtypes.html#bytes) 문자열.

`asyncio.LimitOverrunError`
- 구분 기호를 찾는 동안 버퍼 크기 제한에 도달했습니다.
- [asyncio 스트림 API](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio-streams)가 일으킵니다.

`consumed`
- 소비된 바이트의 총수.

---
## 예제
### 스트림 (Stream)

#### 스트림을 사용하는 TCP 에코 클라이언트 (TCP echo client using streams)

- `asyncio.open_connection()` 함수를 사용하는 TCP 에코 클라이언트:

```python
import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client('Hello World!'))
```

> [TCP 에코 클라이언트 프로토콜](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio-example-tcp-echo-client-protocol) 예제는 저수준 `loop.create_connection()` 메서드를 사용합니다.

#### 스트림을 사용하는 TCP 에코 서버 (TCP echo server using streams)

- `asyncio.start_server()` 함수를 사용하는 TCP 에코 서버:

```python
import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
```

> [TCP 에코 서버 프로토콜](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio-example-tcp-echo-server-protocol) 예제는 `loop.create_server()` 메서드를 사용합니다.

#### HTTP 헤더 가져오기 (Get HTTP headers)

- 명령 줄로 전달된 URL의 HTTP 헤더를 조회하는 간단한 예제:

```python
import asyncio
import urllib.parse
import sys

async def print_http_headers(url):
    url = urllib.parse.urlsplit(url)
    if url.scheme == 'https':
        reader, writer = await asyncio.open_connection(
            url.hostname, 443, ssl=True)
    else:
        reader, writer = await asyncio.open_connection(
            url.hostname, 80)

    query = (
        f"HEAD {url.path or '/'} HTTP/1.0\r\n"
        f"Host: {url.hostname}\r\n"
        f"\r\n"
    )

    writer.write(query.encode('latin-1'))
    while True:
        line = await reader.readline()
        if not line:
            break

        line = line.decode('latin1').rstrip()
        if line:
            print(f'HTTP header> {line}')

    # Ignore the body, close the socket
    writer.close()
    await writer.wait_closed()

url = sys.argv[1]
asyncio.run(print_http_headers(url))
```

사용법:

```
python example.py http://example.com/path/page.html
```

또는 HTTPS를 사용하면:

```
python example.py https://example.com/path/page.html
```

#### 스트림을 사용하여 데이터를 기다리는 열린 소켓 등록 (Register an open socket to wait for data using streams)

- `open_connection()` 함수를 사용하여 소켓이 데이터를 수신할 때까지 기다리는 코루틴:

```python
import asyncio
import socket

async def wait_for_data():
    # Get a reference to the current event loop because
    # we want to access low-level APIs.
    loop = asyncio.get_running_loop()

    # Create a pair of connected sockets.
    rsock, wsock = socket.socketpair()

    # Register the open socket to wait for data.
    reader, writer = await asyncio.open_connection(sock=rsock)

    # Simulate the reception of data from the network
    loop.call_soon(wsock.send, 'abc'.encode())

    # Wait for data
    data = await reader.read(100)

    # Got data, we are done: close the socket
    print("Received:", data.decode())
    writer.close()
    await writer.wait_closed()

    # Close the second socket
    wsock.close()

asyncio.run(wait_for_data())
```

> [!seealso]
> - [프로토콜을 사용하여 데이터를 기다리는 열린 소켓 등록](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio-example-create-connection) 예제는 저수준 프로토콜과 `loop.create_connection()` 메서드를 사용합니다.
> - [파일 기술자에서 읽기 이벤트를 관찰하기](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio-example-watch-fd) 예제는 저수준 `loop.add_reader()` 메서드를 사용하여 파일 기술자를 관찰합니다.

### 서브 프로세스 (Subprocess)
- [Process](https://docs.python.org/ko/3/library/asyncio-subprocess.html#asyncio.subprocess.Process) 클래스를 사용하여 서브 프로세스를 제어하고 [StreamReader](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.StreamReader) 클래스를 사용하여 표준 출력을 읽는 예제.
- 서브 프로세스는 [create_subprocess_exec()](https://docs.python.org/ko/3/library/asyncio-subprocess.html#asyncio.create_subprocess_exec) 함수로 만듭니다:

```python
import asyncio
import sys

async def get_date():
    code = 'import datetime; print(datetime.datetime.now())'

    # Create the subprocess; redirect the standard output
    # into a pipe.
    proc = await asyncio.create_subprocess_exec(
        sys.executable, '-c', code,
        stdout=asyncio.subprocess.PIPE)

    # Read one line of output.
    data = await proc.stdout.readline()
    line = data.decode('ascii').rstrip()

    # Wait for the subprocess exit.
    await proc.wait()
    return line

date = asyncio.run(get_date())
print(f"Current date: {date}")
```

- 저수준 API를 사용하여 작성된 [같은 예제](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio-example-subprocess-proto)도 참조하십시오.

### 큐 (Queue)
- 큐를 사용하여 여러 동시 태스크로 작업 부하를 분산시킬 수 있습니다:

```python
import asyncio
import random
import time

async def worker(name, queue):
    while True:
        # Get a "work item" out of the queue.
        sleep_for = await queue.get()

        # Sleep for the "sleep_for" seconds.
        await asyncio.sleep(sleep_for)

        # Notify the queue that the "work item" has been processed.
        queue.task_done()

        print(f'{name} has slept for {sleep_for:f} seconds')

async def main():
    # Create a queue that we will use to store our "workload".
    queue = asyncio.Queue()

    # Generate random timings and put them into the queue.
    total_sleep_time = 0
    for _ in range(20):
        sleep_for = random.uniform(0.05, 1.0)
        total_sleep_time += sleep_for
        queue.put_nowait(sleep_for)

    # Create three worker tasks to process the queue concurrently.
    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(f'worker-{i}', queue))
        tasks.append(task)

    # Wait until the queue is fully processed.
    started_at = time.monotonic()
    await queue.join()
    total_slept_for = time.monotonic() - started_at

    # Cancel our worker tasks.
    for task in tasks:
        task.cancel()
    # Wait until all worker tasks are cancelled.
    await asyncio.gather(*tasks, return_exceptions=True)

    print('====')
    print(f'3 workers slept in parallel for {total_slept_for:f} seconds')
    print(f'total expected sleep time: {total_sleep_time:f} seconds')

asyncio.run(main())
```

## 참조

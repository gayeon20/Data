---
title: "[Python] 비동기 입출력 (Asyncio)"
excerpt: asyncio는 async/await 구문을 사용하여 동시성 코드를 작성하는 라이브러리입니다. 고성능 네트워크 및 웹 서버, 데이터베이스 연결 라이브러리, 분산 작업 큐 등을 제공하는 여러 파이썬 비동기 프레임워크의 기반으로 사용됩니다.
categories:
  - Python
tags:
  - Python
  - Python-Library
  - Network
  - Concurrency
  - Asynchronous
  - Python-asyncio
last_modified_at: 2024-04-11T15:11:34+09:00
link: https://docs.python.org/ko/3/library/asyncio.html
상위 항목: "[[python_network|파이썬 네트워크 (Python Network)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

**하위 항목**
- [[python_asyncio_application|파이썬 비동기 입출력 - 서비스 (Python Asyncio - Service)]]

---

- asyncio는 **async/await** 구문을 사용하여 **동시성** 코드를 작성하는 라이브러리입니다.
- asyncio는 고성능 네트워크 및 웹 서버, 데이터베이스 연결 라이브러리, 분산 작업 큐 등을 제공하는 여러 파이썬 비동기 프레임워크의 기반으로 사용됩니다.
- asyncio는 종종 IO 병목이면서 고수준의 **구조화된** 네트워크 코드에 가장 적합합니다.
- asyncio는 다음과 같은 작업을 위한 **고수준** API 집합을 제공합니다:
	- [파이썬 코루틴들](https://docs.python.org/ko/3/library/asyncio-task.html#coroutine)을 동시에 실행하고 실행을 완전히 제어할 수 있습니다.
	- [네트워크 IO와 IPC](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio-streams)를 수행합니다;
	- [자식 프로세스](https://docs.python.org/ko/3/library/asyncio-subprocess.html#asyncio-subprocess)를 제어합니다;
	- [큐](https://docs.python.org/ko/3/library/asyncio-queue.html#asyncio-queues)를 통해 작업을 분산합니다;
	- 동시성 코드를 [동기화](https://docs.python.org/ko/3/library/asyncio-sync.html#asyncio-sync)합니다;
- 또한, _라이브러리와 프레임워크 개발자_ 가 다음과 같은 작업을 할 수 있도록 하는 **저수준** API가 있습니다:
	- [이벤트 루프](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio-event-loop)를 생성하고 관리하여 [네트워킹](https://docs.python.org/ko/3/library/asyncio-eventloop.html#loop-create-server), [서브프로세스](https://docs.python.org/ko/3/library/asyncio-eventloop.html#loop-subprocess-exec) 실행, [OS 신호](https://docs.python.org/ko/3/library/asyncio-eventloop.html#loop-add-signal-handler) 처리 등을 위한 비동기 API를 제공합니다;
	- [트랜스포트](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio-transports-protocols)를 사용하여 효율적인 프로토콜을 구현합니다.
	- 콜백 기반 라이브러리와 async/await 구문을 사용한 코드 간에 [다리를 놓습니다](https://docs.python.org/ko/3/library/asyncio-future.html#asyncio-futures).

- [가용성](https://docs.python.org/ko/3/library/intro.html#availability): 엠스크립텐이 아닌, WASI가 아닙니다.
- 이 모듈은 웹어셈블리 플랫폼 `wasm32-emscripten` 및 `wasm32-wasi`에서 작동하지 않거나 사용할 수 없습니다. 자세한 내용은 [웹어셈블리 플랫폼](https://docs.python.org/ko/3/library/intro.html#wasm-availability)을 참조하십시오.
- 비동기 REPL: REPL에서 `asyncio` 동시 컨텍스트를 실험할 수 있습니다:

```sh
$ python -m asyncio
asyncio REPL …
Use "await" directly instead of "asyncio.run()".
Type "help", "copyright", "credits" or "license" for more information.
>>> import asyncio
>>> await asyncio.sleep(10, result='hello')
'hello'
```

- 인자 없이 [감사 이벤트](https://docs.python.org/ko/3/library/sys.html#auditing) `cpython.run_stdin`을 발생시킵니다.
> 버전 3.12.5에서 변경: (또한 3.11.10, 3.10.15, 3.9.20 및 3.8.20) 감사 이벤트를 발생시킵니다.


## 주요 내용
### 디버그 모드 (Debug mode)

- 기본적으로 asyncio는 프로덕션 모드로 실행됩니다. 개발을 쉽게 하려고 asyncio에는 디버그 모드를 제공합니다.
- 여러 가지 방법으로 asyncio 디버그 모드를 활성화할 수 있습니다:
	- [PYTHONASYNCIODEBUG](https://docs.python.org/ko/3/using/cmdline.html#envvar-PYTHONASYNCIODEBUG) 환경 변수를 1로 설정.
	- [파이썬 개발 모드](https://docs.python.org/ko/3/library/devmode.html#devmode) 사용.
	- debug=True를 [asyncio.run()](https://docs.python.org/ko/3/library/asyncio-runner.html#asyncio.run "asyncio.run")로 전달.
	- [loop.set_debug()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.set_debug "asyncio.loop.set_debug")를 호출.
- 디버그 모드를 활성화하는 것 외에도, 다음을 고려하십시오:
	- [asyncio 로거](https://docs.python.org/ko/3/library/asyncio-dev.html#asyncio-logger)의 로그 레벨을 [logging.DEBUG](https://docs.python.org/ko/3/library/logging.html#logging.DEBUG "logging.DEBUG")로 설정하는 것입니다. 예를 들어 다음 코드 스니펫을 애플리케이션 시작 시 실행할 수 있습니다:
	```python
	logging.basicConfig(level=logging.DEBUG)
	```
	- [ResourceWarning](https://docs.python.org/ko/3/library/exceptions.html#ResourceWarning "ResourceWarning") 경고를 표시하도록 [warnings](https://docs.python.org/ko/3/library/warnings.html#module-warnings "warnings: Issue warning messages and control their disposition.") 모듈을 구성. 이렇게 하는 한 가지 방법은 [-W](https://docs.python.org/ko/3/using/cmdline.html#cmdoption-W) default 명령 줄 옵션을 사용하는 것입니다.
- 디버그 모드가 활성화되면:
	- asyncio는 [기다리지 않은 코루틴](https://docs.python.org/ko/3/library/asyncio-dev.html#asyncio-coroutine-not-scheduled)을 검사하고 로그 합니다; 이것은 "잊힌 await" 함정을 완화합니다.
	- 많은 스레드 안전하지 않은 asyncio API([loop.call_soon()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.call_soon "asyncio.loop.call_soon")과 [loop.call_at()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.call_at "asyncio.loop.call_at") 메서드와 같은)가 잘못된 스레드에서 호출될 때 예외를 발생시킵니다.
	- I/O 선택기의 실행 시간은 I/O 연산 수행에 너무 오래 걸리면 로그 됩니다.
	- 100밀리초 이상 걸리는 콜백은 로그됩니다. [loop.slow_callback_duration](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.slow_callback_duration "asyncio.loop.slow_callback_duration") 속성을 사용하여 "느린" 것으로 간주되는 최소 실행 시간을 초 단위로 설정할 수 있습니다.

### 동시성과 다중 스레드 (Concurrency and multithreading)
- 이벤트 루프는 스레드(일반적으로 주 스레드)에서 실행되며 그 스레드에서 모든 콜백과 태스크를 실행합니다. 태스크가 이벤트 루프에서 실행되는 동안, 다른 태스크는 같은 스레드에서 실행될 수 없습니다. 태스크가 await 표현식을 실행하면, 실행 중인 태스크가 일시 중지되고 이벤트 루프는 다음 태스크를 실행합니다.
- 다른 OS 스레드에서 [콜백](https://docs.python.org/ko/3/glossary.html#term-callback)을 예약하려면, [loop.call_soon_threadsafe()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.call_soon_threadsafe "asyncio.loop.call_soon_threadsafe") 메서드를 사용해야 합니다. 예:

```python
loop.call_soon_threadsafe(callback, *args)
```

- 거의 모든 asyncio 객체는 스레드 안전하지 않습니다. 태스크나 콜백 외부에서 작동하는 코드가 없으면 일반적으로 문제가 되지 않습니다. 그러한 코드가 저수준 asyncio API를 호출해야 하면, [loop.call_soon_threadsafe()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.call_soon_threadsafe "asyncio.loop.call_soon_threadsafe") 메서드를 사용해야 합니다, 예를 들어:

```python
loop.call_soon_threadsafe(fut.cancel)
```

- 다른 OS 스레드에서 코루틴 객체를 예약하려면, [run_coroutine_threadsafe()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.run_coroutine_threadsafe "asyncio.run_coroutine_threadsafe") 함수를 사용해야 합니다. 결과에 액세스할 수 있도록 [concurrent.futures.Future](https://docs.python.org/ko/3/library/concurrent.futures.html#concurrent.futures.Future "concurrent.futures.Future")를 반환합니다:

```python
async def coro_func():
     return await asyncio.sleep(1, 42)

# Later in another OS thread:

future = asyncio.run_coroutine_threadsafe(coro_func(), loop)
# Wait for the result:
result = future.result()
```

- 신호를 처리하려면 이벤트 루프가 주 스레드에서 실행되어야 합니다.
- [loop.run_in_executor()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "asyncio.loop.run_in_executor") 메서드는 [concurrent.futures.ThreadPoolExecutor](https://docs.python.org/ko/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor")와 함께 사용되어, 이벤트 루프가 실행되는 OS 스레드를 블록하지 않고 다른 OS 스레드에서 블로킹 코드를 실행할 수 있습니다.
- 현재 다른 프로세스(예: [multiprocessing](https://docs.python.org/ko/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.")으로 시작된 프로세스)에서 코루틴이나 콜백을 직접 예약하는 방법은 없습니다. [이벤트 루프 메서드](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio-event-loop-methods) 섹션에는 이벤트 루프를 차단하지 않고 파이프에서 읽고 파일 디스크립터를 감시할 수 있는 API가 나열되어 있습니다. 또한 asyncio의 [Subprocess](https://docs.python.org/ko/3/library/asyncio-subprocess.html#asyncio-subprocess) API는 프로세스를 시작하고 이벤트 루프에서 해당 프로세스와 통신하는 방법을 제공합니다. 마지막으로, 앞서 언급한 [loop.run_in_executor()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "asyncio.loop.run_in_executor") 메서드는 [concurrent.futures.ProcessPoolExecutor](https://docs.python.org/ko/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor")와 함께 사용하여 다른 프로세스에서 코드를 실행할 수도 있습니다.

### 블로킹 코드 실행하기 (Running blocking code)
- 블로킹 (CPU 병목) 코드는 직접 호출하면 안 됩니다. 예를 들어, 함수가 CPU 집약적인 계산을 1초 동안 수행하면, 모든 동시 asyncio 태스크와 IO 연산이 1초 지연됩니다.
- 실행기를 사용하여, 블로킹이 이벤트 루프가 실행되는 OS 스레드를 블록하지 않도록, 다른 스레드 또는 다른 프로세스에서 태스크를 실행할 수 있습니다. 자세한 내용은 [loop.run_in_executor()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "asyncio.loop.run_in_executor") 메서드를 참조하십시오.

### 로깅 (Logging)
- asyncio는 [logging](https://docs.python.org/ko/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.") 모듈을 사용하고, 모든 로깅은 "asyncio" 로거를 통해 수행됩니다.
- 기본 로그 레벨은 [logging.INFO](https://docs.python.org/ko/3/library/logging.html#logging.INFO "logging.INFO")이며, 쉽게 조정할 수 있습니다:

```python
logging.getLogger("asyncio").setLevel(logging.WARNING)
```

- 네트워크 로깅은 이벤트 루프를 차단할 수 있습니다. 로그를 처리하기 위해 별도의 스레드를 사용하거나 비차단 IO를 사용하는 것이 좋습니다. 예를 들어, [블록 하는 처리기 다루기](https://docs.python.org/ko/3/howto/logging-cookbook.html#blocking-handlers)를 참조하세요.

### await 하지 않은 코루틴 감지 (Detect never-awaited coroutines)
- 코루틴 함수가 호출되었지만 기다리지 않을 때(예를 들어, await coro() 대신 coro())나 코루틴이 [asyncio.create_task()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.create_task "asyncio.create_task")로 예약되지 않으면 asyncio가 [RuntimeWarning](https://docs.python.org/ko/3/library/exceptions.html#RuntimeWarning "RuntimeWarning")을 방출합니다:

```python
import asyncio

async def test():
    print("never scheduled")

async def main():
    test()

asyncio.run(main())
```

출력:
```
test.py:7: RuntimeWarning: coroutine 'test' was never awaited
  test()
```

디그 모드에서의 출력:

```
test.py:7: RuntimeWarning: coroutine 'test' was never awaited
Coroutine created at (most recent call last)
  File "../t.py", line 9, in <module>
    asyncio.run(main(), debug=True)

  < .. >

  File "../t.py", line 7, in main
    test()
  test()
```

- 일반적인 수정법은 코루틴을 await 하거나 [asyncio.create_task()](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.create_task "asyncio.create_task") 함수를 호출하는 것입니다:

```python
async def main():
    await test()
```

### 전달되지 않은 예외 감지 (Detect never-retrieved exceptions)

- [Future.set_exception()](https://docs.python.org/ko/3/library/asyncio-future.html#asyncio.Future.set_exception "asyncio.Future.set_exception")가 호출되었지만, Future 객체가 await 되지 않으면, 예외는 절대로 사용자 코드로 전파되지 않습니다. 이럴 때, Future 객체가 가비지 수집될 때 asyncio가 로그 메시지를 출력합니다.

처리되지 않은 예외의 예:

```python
import asyncio

async def bug():
    raise Exception("not consumed")

async def main():
    asyncio.create_task(bug())

asyncio.run(main())
```

출력:

```
Task exception was never retrieved
future: <Task finished coro=<bug() done, defined at test.py:3>
  exception=Exception('not consumed')>

Traceback (most recent call last):
  File "test.py", line 4, in bug
    raise Exception("not consumed")
Exception: not consumed
```

- 태스크가 만들어진 곳의 트레이스백을 얻으려면 [디버그 모드를 활성화하세요](https://docs.python.org/ko/3/library/asyncio-dev.html#asyncio-debug-mode):

```python
asyncio.run(main(), debug=True)
```

- 디버그 모드에서의 출력:

```
Task exception was never retrieved
future: <Task finished coro=<bug() done, defined at test.py:3>
    exception=Exception('not consumed') created at asyncio/tasks.py:321>

source_traceback: Object created at (most recent call last):
  File "../t.py", line 9, in <module>
    asyncio.run(main(), debug=True)

< .. >

Traceback (most recent call last):
  File "../t.py", line 4, in bug
    raise Exception("not consumed")
Exception: not consumed
```

## [[python_asyncio_application|고수준 API - 서비스]]
- [Runners](https://docs.python.org/ko/3/library/asyncio-runner.html)
- [코루틴과 태스크](https://docs.python.org/ko/3/library/asyncio-task.html)
- [스트림](https://docs.python.org/ko/3/library/asyncio-stream.html)
- [동기화 프리미티브](https://docs.python.org/ko/3/library/asyncio-sync.html)
- [서브 프로세스](https://docs.python.org/ko/3/library/asyncio-subprocess.html)
- [큐](https://docs.python.org/ko/3/library/asyncio-queue.html)
- [예외](https://docs.python.org/ko/3/library/asyncio-exceptions.html)

### 태스크
- asyncio 프로그램을 실행하고, 태스크를 만들고, 시간제한 있게 여러 가지를 기다리는 유틸리티.

|   |   |
|---|---|
|[`run()`](https://docs.python.org/ko/3/library/asyncio-runner.html#asyncio.run "asyncio.run")|이벤트 루프를 만들고, 코루틴을 실행하고, 루프를 닫습니다.|
|[`Runner`](https://docs.python.org/ko/3/library/asyncio-runner.html#asyncio.Runner "asyncio.Runner")|A context manager that simplifies multiple async function calls.|
|[`Task`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")|Task 객체.|
|[`TaskGroup`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.TaskGroup "asyncio.TaskGroup")|A context manager that holds a group of tasks. Provides a convenient and reliable way to wait for all tasks in the group to finish.|
|[`create_task()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.create_task "asyncio.create_task")|Start an asyncio Task, then returns it.|
|[`current_task()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.current_task "asyncio.current_task")|현재 Task를 돌려줍니다.|
|[`all_tasks()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.all_tasks "asyncio.all_tasks")|Return all tasks that are not yet finished for an event loop.|
|`await` [`sleep()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.sleep "asyncio.sleep")|몇 초 동안 잠잡니다.|
|`await` [`gather()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.gather "asyncio.gather")|여러 가지를 동시에 예약하고 기다립니다.|
|`await` [`wait_for()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.wait_for "asyncio.wait_for")|시간제한 있게 실행합니다.|
|`await` [`shield()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.shield "asyncio.shield")|취소로부터 보호합니다.|
|`await` [`wait()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.wait "asyncio.wait")|완료를 감시합니다.|
|[`timeout()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.timeout "asyncio.timeout")|Run with a timeout. Useful in cases when `wait_for` is not suitable.|
|[`to_thread()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.to_thread "asyncio.to_thread")|Asynchronously run a function in a separate OS thread.|
|[`run_coroutine_threadsafe()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.run_coroutine_threadsafe "asyncio.run_coroutine_threadsafe")|다른 OS 스레드에서 코루틴을 예약합니다.|
|`for in` [`as_completed()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.as_completed "asyncio.as_completed")|`for` 루프로 완료를 감시합니다.|

예제
- [여러 가지를 병렬로 실행하기 위해 asyncio.gather() 사용하기](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio-example-gather).
- [시간제한을 주기 위해 asyncio.wait_for() 사용하기](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio-example-waitfor).
- [취소](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio-example-task-cancel).
- [asyncio.sleep() 사용하기](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio-example-sleep).
- 주 [태스크 설명서 페이지](https://docs.python.org/ko/3/library/asyncio-task.html#coroutine)를 참조하십시오.
    

### 큐
- 큐는 여러 asyncio 태스크 간에 작업을 분산하고, 연결 풀과 pub/sub 패턴을 구현하는 데 사용해야 합니다.

|                                                                                                                          |         |
| ------------------------------------------------------------------------------------------------------------------------ | ------- |
| [`Queue`](https://docs.python.org/ko/3/library/asyncio-queue.html#asyncio.Queue "asyncio.Queue")                         | FIFO 큐. |
| [`PriorityQueue`](https://docs.python.org/ko/3/library/asyncio-queue.html#asyncio.PriorityQueue "asyncio.PriorityQueue") | 우선순위 큐. |
| [`LifoQueue`](https://docs.python.org/ko/3/library/asyncio-queue.html#asyncio.LifoQueue "asyncio.LifoQueue")             | LIFO 큐. |

예제
- [여러 태스크로 작업부하를 분산하는데 asyncio.Queue 사용하기](https://docs.python.org/ko/3/library/asyncio-queue.html#asyncio-example-queue-dist).
- [큐 설명서 페이지](https://docs.python.org/ko/3/library/asyncio-queue.html#asyncio-queues)도 참조하십시오.

### 서브 프로세스
- 서브 프로세스를 생성하고 셸 명령을 실행하는 유틸리티.

|   |   |
|---|---|
|`await` [`create_subprocess_exec()`](https://docs.python.org/ko/3/library/asyncio-subprocess.html#asyncio.create_subprocess_exec "asyncio.create_subprocess_exec")|서브 프로세스를 만듭니다.|
|`await` [`create_subprocess_shell()`](https://docs.python.org/ko/3/library/asyncio-subprocess.html#asyncio.create_subprocess_shell "asyncio.create_subprocess_shell")|셸 명령을 실행합니다.|

예제
- [셸 명령 실행하기](https://docs.python.org/ko/3/library/asyncio-subprocess.html#asyncio-example-subprocess-shell).
- [서브 프로세스 API](https://docs.python.org/ko/3/library/asyncio-subprocess.html#asyncio-subprocess) 설명서도 참조하십시오.

### 스트림
네트워크 IO로 작업하는 고수준 API

|                                                                                                                                                          |                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| `await` [`open_connection()`](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.open_connection "asyncio.open_connection")                | TCP 연결을 만듭니다.                      |
| `await` [`open_unix_connection()`](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.open_unix_connection "asyncio.open_unix_connection") | 유닉스 소켓 연결을 만듭니다.                   |
| `await` [`start_server()`](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.start_server "asyncio.start_server")                         | TCP 서버를 시작합니다.                     |
| `await` [`start_unix_server()`](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.start_unix_server "asyncio.start_unix_server")          | 유닉스 소켓 서버를 시작합니다.                  |
| [`StreamReader`](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.StreamReader "asyncio.StreamReader")                                   | 네트워크 데이터를 수신하는 고수준 async/await 객체. |
| [`StreamWriter`](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.StreamWriter "asyncio.StreamWriter")                                   | 네트워크 데이터를 보내는 고수준 async/await 객체.  |

예제
- [예제 TCP 클라이언트](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio-example-stream).
- [스트림 API](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio-streams) 설명서도 참조하십시오.

### 동기화

태스크에 쓸 수 있는 threading과 유사한 동기화 프리미티브.

|   |   |
|---|---|
|[`Lock`](https://docs.python.org/ko/3/library/asyncio-sync.html#asyncio.Lock "asyncio.Lock")|뮤텍스 록.|
|[`Event`](https://docs.python.org/ko/3/library/asyncio-sync.html#asyncio.Event "asyncio.Event")|이벤트 객체.|
|[`Condition`](https://docs.python.org/ko/3/library/asyncio-sync.html#asyncio.Condition "asyncio.Condition")|조건 객체.|
|[`Semaphore`](https://docs.python.org/ko/3/library/asyncio-sync.html#asyncio.Semaphore "asyncio.Semaphore")|세마포어.|
|[`BoundedSemaphore`](https://docs.python.org/ko/3/library/asyncio-sync.html#asyncio.BoundedSemaphore "asyncio.BoundedSemaphore")|제한된 세마포어.|
|[`Barrier`](https://docs.python.org/ko/3/library/asyncio-sync.html#asyncio.Barrier "asyncio.Barrier")|A barrier object.|

예제
- [asyncio.Event 사용하기](https://docs.python.org/ko/3/library/asyncio-sync.html#asyncio-example-sync-event).
- [Using asyncio.Barrier](https://docs.python.org/ko/3/library/asyncio-sync.html#asyncio-example-barrier).
- asyncio [동기화 프리미티브](https://docs.python.org/ko/3/library/asyncio-sync.html#asyncio-sync)의 설명서도 참조하십시오.
    

### 예외

|   |   |
|---|---|
|[`asyncio.CancelledError`](https://docs.python.org/ko/3/library/asyncio-exceptions.html#asyncio.CancelledError "asyncio.CancelledError")|Task가 취소될 때 발생합니다. [`Task.cancel()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task.cancel "asyncio.Task.cancel")도 참조하십시오.|
|[`asyncio.BrokenBarrierError`](https://docs.python.org/ko/3/library/asyncio-sync.html#asyncio.BrokenBarrierError "asyncio.BrokenBarrierError")|Raised when a Barrier is broken. See also [`Barrier.wait()`](https://docs.python.org/ko/3/library/asyncio-sync.html#asyncio.Barrier.wait "asyncio.Barrier.wait").|

예제
- [취소 요청 시에 코드를 실행하기 위해 CancelledError 처리하기](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio-example-task-cancel).
- [asyncio 전용 예외](https://docs.python.org/ko/3/library/asyncio-exceptions.html#asyncio-exceptions)의 전체 목록도 참조하십시오.


## [[python_asyncio_system|저수준 API]]
- [이벤트 루프](https://docs.python.org/ko/3/library/asyncio-eventloop.html)
- [퓨처](https://docs.python.org/ko/3/library/asyncio-future.html)
- [트랜스포트와 프로토콜](https://docs.python.org/ko/3/library/asyncio-protocol.html)
- [정책](https://docs.python.org/ko/3/library/asyncio-policy.html)
- [플랫폼 지원](https://docs.python.org/ko/3/library/asyncio-platforms.html)
- [Extending](https://docs.python.org/ko/3/library/asyncio-extending.html)

### 이벤트 루프 얻기

|   |   |
|---|---|
|[`asyncio.get_running_loop()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.get_running_loop "asyncio.get_running_loop")|실행 중인 이벤트 루프를 가져오는 데 **선호되는** 함수.|
|[`asyncio.get_event_loop()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.get_event_loop "asyncio.get_event_loop")|Get an event loop instance (running or current via the current policy).|
|[`asyncio.set_event_loop()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.set_event_loop "asyncio.set_event_loop")|현재 정책을 통해 현재 이벤트 루프를 설정합니다.|
|[`asyncio.new_event_loop()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.new_event_loop "asyncio.new_event_loop")|새 이벤트 루프를 만듭니다.|

예제
- [asyncio.get_running_loop() 사용하기](https://docs.python.org/ko/3/library/asyncio-future.html#asyncio-example-future).


### 이벤트 루프 메서드
- See also the main documentation section about the [이벤트 루프 메서드](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio-event-loop-methods).

#### 수명주기

|                                                                                                                                                                      |                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| [`loop.run_until_complete()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.run_until_complete "asyncio.loop.run_until_complete")         | 완료할 때까지 퓨처/태스크/어웨이터블을 실행합니다.  |
| [`loop.run_forever()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.run_forever "asyncio.loop.run_forever")                              | 이벤트 루프를 영원히 실행합니다.            |
| [`loop.stop()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.stop "asyncio.loop.stop")                                                   | 이벤트 루프를 중지합니다.                |
| [`loop.close()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.close "asyncio.loop.close")                                                | 이벤트 루프를 닫습니다.                 |
| [`loop.is_running()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.is_running "asyncio.loop.is_running")                                 | 이벤트 루프가 실행 중이면 `True`를 반환합니다. |
| [`loop.is_closed()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.is_closed "asyncio.loop.is_closed")                                    | 이벤트 루프가 닫혔으면 `True`를 반환합니다.   |
| `await` [`loop.shutdown_asyncgens()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.shutdown_asyncgens "asyncio.loop.shutdown_asyncgens") | 비동기 제너레이터를 닫습니다.              |

#### 디버깅

|   |   |
|---|---|
|[`loop.set_debug()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.set_debug "asyncio.loop.set_debug")|디버그 모드를 활성화 또는 비활성화합니다.|
|[`loop.get_debug()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.get_debug "asyncio.loop.get_debug")|현재의 디버그 모드를 얻습니다.|

#### 콜백 예약하기

|   |   |
|---|---|
|[`loop.call_soon()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.call_soon "asyncio.loop.call_soon")|콜백을 곧 호출합니다.|
|[`loop.call_soon_threadsafe()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.call_soon_threadsafe "asyncio.loop.call_soon_threadsafe")|스레드 안전한 [`loop.call_soon()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.call_soon "asyncio.loop.call_soon")의 변형입니다.|
|[`loop.call_later()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.call_later "asyncio.loop.call_later")|주어진 시간 _후_에 콜백을 호출합니다.|
|[`loop.call_at()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.call_at "asyncio.loop.call_at")|주어진 시간 _에_ 콜백을 호출합니다.|

#### 스레드/프로세스 풀

|   |   |
|---|---|
|`await` [`loop.run_in_executor()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "asyncio.loop.run_in_executor")|[`concurrent.futures`](https://docs.python.org/ko/3/library/concurrent.futures.html#module-concurrent.futures "concurrent.futures: Execute computations concurrently using threads or processes.") 실행기에서 CPU-병목이나 다른 블로킹 함수를 실행합니다.|
|[`loop.set_default_executor()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.set_default_executor "asyncio.loop.set_default_executor")|[`loop.run_in_executor()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "asyncio.loop.run_in_executor")의 기본 실행기를 설정합니다.|

#### 태스크와 퓨처

|   |   |
|---|---|
|[`loop.create_future()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_future "asyncio.loop.create_future")|[`Future`](https://docs.python.org/ko/3/library/asyncio-future.html#asyncio.Future "asyncio.Future") 객체를 만듭니다.|
|[`loop.create_task()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_task "asyncio.loop.create_task")|코루틴을 [`Task`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")로 예약합니다.|
|[`loop.set_task_factory()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.set_task_factory "asyncio.loop.set_task_factory")|[`loop.create_task()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_task "asyncio.loop.create_task")가 [`태스크`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")를 만드는데 사용하는 팩토리를 설정합니다.|
|[`loop.get_task_factory()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.get_task_factory "asyncio.loop.get_task_factory")|[`loop.create_task()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_task "asyncio.loop.create_task")가 [`태스크`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")를 만드는데 사용하는 팩토리를 얻습니다.|

#### DNS

|   |   |
|---|---|
|`await` [`loop.getaddrinfo()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.getaddrinfo "asyncio.loop.getaddrinfo")|[`socket.getaddrinfo()`](https://docs.python.org/ko/3/library/socket.html#socket.getaddrinfo "socket.getaddrinfo")의 비동기 버전.|
|`await` [`loop.getnameinfo()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.getnameinfo "asyncio.loop.getnameinfo")|[`socket.getnameinfo()`](https://docs.python.org/ko/3/library/socket.html#socket.getnameinfo "socket.getnameinfo")의 비동기 버전.|

#### 네트워킹과 IPC

|   |   |
|---|---|
|`await` [`loop.create_connection()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection")|TCP 연결을 엽니다.|
|`await` [`loop.create_server()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server")|TCP 서버를 만듭니다.|
|`await` [`loop.create_unix_connection()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_connection "asyncio.loop.create_unix_connection")|유닉스 소켓 연결을 엽니다.|
|`await` [`loop.create_unix_server()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_server "asyncio.loop.create_unix_server")|Unix 소켓 서버를 만듭니다.|
|`await` [`loop.connect_accepted_socket()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.connect_accepted_socket "asyncio.loop.connect_accepted_socket")|[`socket`](https://docs.python.org/ko/3/library/socket.html#socket.socket "socket.socket")을 `(transport, protocol)` 쌍으로 감쌉니다.|
|`await` [`loop.create_datagram_endpoint()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint "asyncio.loop.create_datagram_endpoint")|데이터 그램 (UDP) 연결을 엽니다.|
|`await` [`loop.sendfile()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.sendfile "asyncio.loop.sendfile")|트랜스포트를 통해 파일을 보냅니다.|
|`await` [`loop.start_tls()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.start_tls "asyncio.loop.start_tls")|기존 연결을 TLS로 업그레이드합니다.|
|`await` [`loop.connect_read_pipe()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.connect_read_pipe "asyncio.loop.connect_read_pipe")|파이프의 읽기 끝을 `(transport, protocol)` 쌍으로 감쌉니다.|
|`await` [`loop.connect_write_pipe()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.connect_write_pipe "asyncio.loop.connect_write_pipe")|파이프의 쓰기 끝을 `(transport, protocol)` 쌍으로 감쌉니다.|

#### 소켓

|   |   |
|---|---|
|`await` [`loop.sock_recv()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.sock_recv "asyncio.loop.sock_recv")|[`socket`](https://docs.python.org/ko/3/library/socket.html#socket.socket "socket.socket")에서 데이터를 수신합니다.|
|`await` [`loop.sock_recv_into()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.sock_recv_into "asyncio.loop.sock_recv_into")|[`socket`](https://docs.python.org/ko/3/library/socket.html#socket.socket "socket.socket")에서 데이터를 버퍼로 수신합니다.|
|`await` [`loop.sock_recvfrom()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.sock_recvfrom "asyncio.loop.sock_recvfrom")|Receive a datagram from the [`socket`](https://docs.python.org/ko/3/library/socket.html#socket.socket "socket.socket").|
|`await` [`loop.sock_recvfrom_into()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.sock_recvfrom_into "asyncio.loop.sock_recvfrom_into")|Receive a datagram from the [`socket`](https://docs.python.org/ko/3/library/socket.html#socket.socket "socket.socket") into a buffer.|
|`await` [`loop.sock_sendall()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.sock_sendall "asyncio.loop.sock_sendall")|데이터를 [`socket`](https://docs.python.org/ko/3/library/socket.html#socket.socket "socket.socket")으로 보냅니다.|
|`await` [`loop.sock_sendto()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.sock_sendto "asyncio.loop.sock_sendto")|Send a datagram via the [`socket`](https://docs.python.org/ko/3/library/socket.html#socket.socket "socket.socket") to the given address.|
|`await` [`loop.sock_connect()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.sock_connect "asyncio.loop.sock_connect")|[`socket`](https://docs.python.org/ko/3/library/socket.html#socket.socket "socket.socket")을 연결합니다.|
|`await` [`loop.sock_accept()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.sock_accept "asyncio.loop.sock_accept")|[`socket`](https://docs.python.org/ko/3/library/socket.html#socket.socket "socket.socket") 연결을 수락합니다.|
|`await` [`loop.sock_sendfile()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.sock_sendfile "asyncio.loop.sock_sendfile")|[`socket`](https://docs.python.org/ko/3/library/socket.html#socket.socket "socket.socket")를 통해 파일을 보냅니다.|
|[`loop.add_reader()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.add_reader "asyncio.loop.add_reader")|파일 기술자가 읽기 가능한지 관찰하기 시작합니다.|
|[`loop.remove_reader()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.remove_reader "asyncio.loop.remove_reader")|파일 기술자가 읽기 가능한지 관찰하는 것을 중단합니다.|
|[`loop.add_writer()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.add_writer "asyncio.loop.add_writer")|파일 기술자가 쓰기 가능한지 관찰하기 시작합니다.|
|[`loop.remove_writer()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.remove_writer "asyncio.loop.remove_writer")|파일 기술자가 쓰기 가능한지 관찰하는 것을 중단합니다.|

#### 유닉스 시그널

|   |   |
|---|---|
|[`loop.add_signal_handler()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.add_signal_handler "asyncio.loop.add_signal_handler")|[`signal`](https://docs.python.org/ko/3/library/signal.html#module-signal "signal: Set handlers for asynchronous events.")에 대한 처리기를 추가합니다.|
|[`loop.remove_signal_handler()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.remove_signal_handler "asyncio.loop.remove_signal_handler")|[`signal`](https://docs.python.org/ko/3/library/signal.html#module-signal "signal: Set handlers for asynchronous events.")에 대한 처리기를 제거합니다.|

#### 서브 프로세스

|   |   |
|---|---|
|[`loop.subprocess_exec()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec "asyncio.loop.subprocess_exec")|서브 프로세스를 스폰합니다.|
|[`loop.subprocess_shell()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_shell "asyncio.loop.subprocess_shell")|셸 명령으로 서브 프로세스를 스폰합니다.|

#### 에러 처리

|   |   |
|---|---|
|[`loop.call_exception_handler()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.call_exception_handler "asyncio.loop.call_exception_handler")|예외 처리기를 호출합니다.|
|[`loop.set_exception_handler()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.set_exception_handler "asyncio.loop.set_exception_handler")|새로운 예외 처리기를 설정합니다.|
|[`loop.get_exception_handler()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.get_exception_handler "asyncio.loop.get_exception_handler")|현재 예외 처리기를 가져옵니다.|
|[`loop.default_exception_handler()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.default_exception_handler "asyncio.loop.default_exception_handler")|기본 예외 처리기 구현.|

예제
- [Using asyncio.new_event_loop() and loop.run_forever()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio-example-lowlevel-helloworld).
- [loop.call_later() 사용하기](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio-example-call-later).
- `loop.create_connection()`을 사용하여 [메아리 클라이언트](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio-example-tcp-echo-client-protocol) 구현하기.
- `loop.create_connection()`을 사용하여 [소켓 연결하기](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio-example-create-connection).
- [add_reader()를 사용하여 FD에서 읽기 이벤트 관찰하기](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio-example-watch-fd).
- [loop.add_signal_handler() 사용하기](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio-example-unix-signals).
- [loop.subprocess_exec() 사용하기](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio-example-subprocess-proto).

### 트랜스포트

- 모든 트랜스포트는 다음과 같은 메서드를 구현합니다:

|                                                                                                                                                                        |                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| [`transport.close()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.BaseTransport.close "asyncio.BaseTransport.close")                            | 트랜스포트를 닫습니다.                       |
| [`transport.is_closing()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.BaseTransport.is_closing "asyncio.BaseTransport.is_closing")             | 트랜스포트가 닫히고 있거나 닫혔으면 `True`를 반환합니다. |
| [`transport.get_extra_info()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.BaseTransport.get_extra_info "asyncio.BaseTransport.get_extra_info") | 트랜스포트에 대한 정보를 요청합니다.               |
| [`transport.set_protocol()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.BaseTransport.set_protocol "asyncio.BaseTransport.set_protocol")       | 새 프로토콜을 설정합니다.                     |
| [`transport.get_protocol()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.BaseTransport.get_protocol "asyncio.BaseTransport.get_protocol")       | 현재 프로토콜을 돌려줍니다.                    |

- 데이터를 받을 수 있는 트랜스포트 (TCP 및 유닉스 연결, 파이프 등). [`loop.create_connection()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection"), [`loop.create_unix_connection()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_connection "asyncio.loop.create_unix_connection"), [`loop.connect_read_pipe()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.connect_read_pipe "asyncio.loop.connect_read_pipe") 등의 메서드에서 반환됩니다:

#### 트랜스포트 읽기

|   |   |
|---|---|
|[`transport.is_reading()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.ReadTransport.is_reading "asyncio.ReadTransport.is_reading")|트랜스포트가 수신 중이면 `True`를 반환합니다.|
|[`transport.pause_reading()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.ReadTransport.pause_reading "asyncio.ReadTransport.pause_reading")|수신을 일시 정지합니다.|
|[`transport.resume_reading()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.ReadTransport.resume_reading "asyncio.ReadTransport.resume_reading")|수신을 재개합니다.|

- 데이터를 전송할 수 있는 트랜스포트 (TCP와 유닉스 연결, 파이프 등). [`loop.create_connection()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection"), [`loop.create_unix_connection()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_connection "asyncio.loop.create_unix_connection"), [`loop.connect_write_pipe()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.connect_write_pipe "asyncio.loop.connect_write_pipe") 등의 메서드에서 반환됩니다:

#### 트랜스포트 쓰기

|   |   |
|---|---|
|[`transport.write()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.WriteTransport.write "asyncio.WriteTransport.write")|데이터를 트랜스포트에 씁니다.|
|[`transport.writelines()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.WriteTransport.writelines "asyncio.WriteTransport.writelines")|버퍼들을 트랜스포트에 씁니다.|
|[`transport.can_write_eof()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.WriteTransport.can_write_eof "asyncio.WriteTransport.can_write_eof")|트랜스포트가 EOF 전송을 지원하면 [`True`](https://docs.python.org/ko/3/library/constants.html#True "True")를 반환합니다.|
|[`transport.write_eof()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.WriteTransport.write_eof "asyncio.WriteTransport.write_eof")|버퍼 된 데이터를 플러시 한 후 닫고 EOF를 보냅니다.|
|[`transport.abort()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.WriteTransport.abort "asyncio.WriteTransport.abort")|즉시 트랜스포트를 닫습니다.|
|[`transport.get_write_buffer_size()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.WriteTransport.get_write_buffer_size "asyncio.WriteTransport.get_write_buffer_size")|Return the current size of the output buffer.|
|[`transport.get_write_buffer_limits()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.WriteTransport.get_write_buffer_limits "asyncio.WriteTransport.get_write_buffer_limits")|쓰기 흐름 제어를 위한 높은 수위와 낮은 수위를 반환합니다.|
|[`transport.set_write_buffer_limits()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.WriteTransport.set_write_buffer_limits "asyncio.WriteTransport.set_write_buffer_limits")|쓰기 흐름 제어를 위한 새로운 높은 수위와 낮은 수위를 설정합니다.|

- [`loop.create_datagram_endpoint()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint "asyncio.loop.create_datagram_endpoint")에서 반환된 트랜스포트:

#### 데이터 그램 트랜스포트

|   |   |
|---|---|
|[`transport.sendto()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.DatagramTransport.sendto "asyncio.DatagramTransport.sendto")|데이터를 원격 피어로 보냅니다.|
|[`transport.abort()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.DatagramTransport.abort "asyncio.DatagramTransport.abort")|즉시 트랜스포트를 닫습니다.|

- 서브 프로세스에 대한 저수준 트랜스포트 추상화. [`loop.subprocess_exec()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec "asyncio.loop.subprocess_exec") 와 [`loop.subprocess_shell()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_shell "asyncio.loop.subprocess_shell")가 반환합니다:

#### 서브 프로세스 트랜스포트

|   |   |
|---|---|
|[`transport.get_pid()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.get_pid "asyncio.SubprocessTransport.get_pid")|서브 프로세스의 프로세스 ID를 돌려줍니다.|
|[`transport.get_pipe_transport()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.get_pipe_transport "asyncio.SubprocessTransport.get_pipe_transport")|요청한 통신 파이프 (_stdin_, _stdout_ 또는 _stderr_)에 대한 트랜스포트를 반환합니다.|
|[`transport.get_returncode()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.get_returncode "asyncio.SubprocessTransport.get_returncode")|서브 프로세스 반환 코드를 돌려줍니다.|
|[`transport.kill()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.kill "asyncio.SubprocessTransport.kill")|서브 프로세스를 죽입니다.|
|[`transport.send_signal()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.send_signal "asyncio.SubprocessTransport.send_signal")|서브 프로세스에 시그널을 보냅니다.|
|[`transport.terminate()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.terminate "asyncio.SubprocessTransport.terminate")|서브 프로세스를 중지합니다.|
|[`transport.close()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.SubprocessTransport.close "asyncio.SubprocessTransport.close")|서브 프로세스를 죽이고 모든 파이프를 닫습니다.|

### 프로토콜
프로토콜 클래스는 다음 **콜백 메서드를** 구현할 수 있습니다:

|                                                                                                                                                                          |                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------- |
| `callback` [`connection_made()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.BaseProtocol.connection_made "asyncio.BaseProtocol.connection_made") | 연결이 이루어질 때 호출됩니다.                |
| `callback` [`connection_lost()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.BaseProtocol.connection_lost "asyncio.BaseProtocol.connection_lost") | 연결이 끊어지거나 닫힐 때 호출됩니다.            |
| `callback` [`pause_writing()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.BaseProtocol.pause_writing "asyncio.BaseProtocol.pause_writing")       | 트랜스포트 버퍼가 높은 수위를 초과할 때 호출됩니다.    |
| `callback` [`resume_writing()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.BaseProtocol.resume_writing "asyncio.BaseProtocol.resume_writing")    | 트랜스포트 버퍼가 낮은 수위 아래로 내려갈 때 호출됩니다. |

#### 스트리밍 프로토콜 (TCP, 유닉스 소켓, 파이프)

|   |   |
|---|---|
|`callback` [`data_received()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.Protocol.data_received "asyncio.Protocol.data_received")|어떤 데이터가 수신될 때 호출됩니다.|
|`callback` [`eof_received()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.Protocol.eof_received "asyncio.Protocol.eof_received")|EOF가 수신될 때 호출됩니다.|

#### 버퍼 된 스트리밍 프로토콜

|   |   |
|---|---|
|`callback` [`get_buffer()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.BufferedProtocol.get_buffer "asyncio.BufferedProtocol.get_buffer")|새로운 수신 버퍼를 할당하기 위해서 호출됩니다.|
|`callback` [`buffer_updated()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.BufferedProtocol.buffer_updated "asyncio.BufferedProtocol.buffer_updated")|수신된 데이터로 버퍼가 갱신될 때 호출됩니다.|
|`callback` [`eof_received()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.BufferedProtocol.eof_received "asyncio.BufferedProtocol.eof_received")|EOF가 수신될 때 호출됩니다.|

#### 데이터 그램 프로토콜

|   |   |
|---|---|
|`callback` [`datagram_received()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.DatagramProtocol.datagram_received "asyncio.DatagramProtocol.datagram_received")|데이터 그램이 수신될 때 호출됩니다.|
|`callback` [`error_received()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.DatagramProtocol.error_received "asyncio.DatagramProtocol.error_received")|이전의 송신이나 수신 연산이 [`OSError`](https://docs.python.org/ko/3/library/exceptions.html#OSError "OSError")를 일으킬 때 호출됩니다.|

#### 서브 프로세스 프로토콜

|   |   |
|---|---|
|`callback` [`pipe_data_received()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.SubprocessProtocol.pipe_data_received "asyncio.SubprocessProtocol.pipe_data_received")|자식 프로세스가 _stdout_ 이나 _stderr_ 파이프에 데이터를 쓸 때 호출됩니다.|
|`callback` [`pipe_connection_lost()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.SubprocessProtocol.pipe_connection_lost "asyncio.SubprocessProtocol.pipe_connection_lost")|자식 프로세스와 통신하는 파이프 중 하나가 닫힐 때 호출됩니다.|
|`callback` [`process_exited()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.SubprocessProtocol.process_exited "asyncio.SubprocessProtocol.process_exited")|Called when the child process has exited. It can be called before [`pipe_data_received()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.SubprocessProtocol.pipe_data_received "asyncio.SubprocessProtocol.pipe_data_received") and [`pipe_connection_lost()`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.SubprocessProtocol.pipe_connection_lost "asyncio.SubprocessProtocol.pipe_connection_lost") methods.|

### 이벤트 루프 정책

- 정책은 [`asyncio.get_event_loop()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.get_event_loop "asyncio.get_event_loop")와 같은 함수의 동작을 변경하는 저수준 메커니즘입니다. 자세한 내용은 주 [정책 절](https://docs.python.org/ko/3/library/asyncio-policy.html#asyncio-policies)을 참조하십시오.

#### 정책 액세스하기

|   |   |
|---|---|
|[`asyncio.get_event_loop_policy()`](https://docs.python.org/ko/3/library/asyncio-policy.html#asyncio.get_event_loop_policy "asyncio.get_event_loop_policy")|현재 프로세스 전반의 정책을 돌려줍니다.|
|[`asyncio.set_event_loop_policy()`](https://docs.python.org/ko/3/library/asyncio-policy.html#asyncio.set_event_loop_policy "asyncio.set_event_loop_policy")|새로운 프로세스 전반의 정책을 설정합니다.|
|[`AbstractEventLoopPolicy`](https://docs.python.org/ko/3/library/asyncio-policy.html#asyncio.AbstractEventLoopPolicy "asyncio.AbstractEventLoopPolicy")|정책 객체의 베이스 클래스.|



---

## 참조

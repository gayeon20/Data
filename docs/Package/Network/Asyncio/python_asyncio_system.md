---
title: "[Python] 비동기 입출력 - 시스템 (Asyncio - System)"
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
## 이벤트 루프 (Event Loop)
- 이벤트 루프는 모든 asyncio 응용 프로그램의 핵심입니다. 이벤트 루프는 비동기 태스크 및 콜백을 실행하고 네트워크 IO 연산을 수행하며 자식 프로세스를 실행합니다.
- 응용 프로그램 개발자는 일반적으로 [asyncio.run()](https://docs.python.org/ko/3/library/asyncio-runner.html#asyncio.run "asyncio.run")과 같은 고수준의 asyncio 함수를 사용해야 하며, 루프 객체를 참조하거나 메서드를 호출할 필요가 거의 없습니다. 이 절은 주로 이벤트 루프 동작을 세부적으로 제어해야 하는 저수준 코드, 라이브러리 및 프레임워크의 작성자를 대상으로 합니다.

**이벤트 루프 얻기**
- 다음 저수준 함수를 사용하여 이벤트 루프를 가져오거나 설정하거나 만들 수 있습니다.:

`asyncio.get_running_loop()`
- 현재 OS 스레드에서 실행 중인 이벤트 루프를 반환합니다.
- 실행 중인 이벤트 루프가 없으면 RuntimeError를 발생시킵니다.
- 이 함수는 코루틴이나 콜백에서만 호출할 수 있습니다.
> 버전 3.7에서 추가되었습니다.

`asyncio.get_event_loop()`
- 현재의 이벤트 루프를 가져옵니다.
- 코루틴이나 콜백(예: call_soon 또는 유사한 API로 예약된)에서 호출되면, 이 함수는 항상 실행 중인 이벤트 루프를 반환합니다.
- 실행 중인 이벤트 루프가 설정되어 있지 않으면, 함수는 get_event_loop_policy().get_event_loop() 호출의 결과를 반환합니다.
- 이 함수는 (특히 사용자 정의 이벤트 루프 정책을 사용할 때) 다소 복잡한 동작을 하므로, 코루틴과 콜백에서 get_event_loop()보다 get_running_loop() 함수를 사용하는 것이 좋습니다.
- 위에서 언급했듯이, 이러한 저수준 함수를 사용하여 수동으로 이벤트 루프를 만들고 닫는 대신 더 높은 수준의 asyncio.run() 함수를 사용하는 것을 고려하세요.

> 버전 3.12부터 폐지됨: 현재 이벤트 루프가 없으면 폐지 경고가 발생합니다. 향후 Python 릴리스에서 이는 오류가 될 것입니다.

`asyncio.set_event_loop(loop)`
- 현재 OS 스레드의 현재 이벤트 루프로 loop를 설정합니다.

`asyncio.new_event_loop()`
- 새 이벤트 루프 객체를 생성하고 반환합니다.

> [!NOTE]
> - `get_event_loop()`, `set_event_loop()` 및 `new_event_loop()` 함수의 동작은 사용자 정의 이벤트 루프 정책 설정에 의해 변경될 수 있음에 유의하십시오.


## 이벤트 루프 메서드 (Event Loop Method)
이 설명서 페이지는 다음과 같은 절로 구성됩니다:
- 이벤트 루프 메서드 절은 이벤트 루프 API의 레퍼런스 설명서입니다.
- 콜백 핸들 절은 loop.call_soon() 및 loop.call_later()와 같은 예약 메서드에서 반환된 Handle 및 TimerHandle 인스턴스를 설명합니다.
- 서버 객체 절은 loop.create_server()와 같은 이벤트 루프 메서드에서 반환되는 형을 설명합니다.
- 이벤트 루프 구현 절은 SelectorEventLoop 및 ProactorEventLoop 클래스를 설명합니다.
- 예제 절에서는 일부 이벤트 루프 API로 작업하는 방법을 보여줍니다.

### 루프 실행 및 중지 (Running and stopping the loop)

`loop.run_until_complete(future)`
- future(Future의 인스턴스)가 완료할 때까지 실행합니다.
- 인자가 코루틴 객체면, asyncio.Task로 실행되도록 묵시적으로 예약 됩니다.
- 퓨처의 결과를 반환하거나 퓨처의 예외를 일으킵니다.

`loop.run_forever()`
- stop()가 호출될 때까지 이벤트 루프를 실행합니다.
- run_forever() 가 호출되기 전에 stop() 이 호출되었으면, 루프는 시간제한 0으로 I/O 셀렉터를 한 번 폴링하고, I/O 이벤트에 따라 예약된 모든 콜백(과 이미 예약된 것들)을 실행한 다음 종료합니다.
- 만약 stop() 이 run_forever() 가 실행 중일 때 호출되면, 루프는 현재 걸려있는 콜백들을 실행한 다음 종료합니다. 콜백에 의해 예약되는 새 콜백은 이 경우 실행되지 않습니다; 대신 그것들은 다음에 run_forever()나 run_until_complete()가 호출될 때 실행됩니다.

`loop.stop()`
- 이벤트 루프를 중지합니다.

`loop.is_running()`
- 이벤트 루프가 현재 실행 중이면 True 를 반환합니다.

`loop.is_closed()`
- 이벤트 루프가 닫혔으면 True 를 반환합니다.

`loop.close()`
- 이벤트 루프를 닫습니다.
- 이 함수를 호출할 때 루프는 반드시 실행 중이지 않아야 합니다. 계류 중인 모든 콜백을 버립니다.
- 이 메서드는 모든 큐를 비우고 실행기를 종료하지만, 실행기가 완료할 때까지 기다리지 않습니다.
- 이 메서드는 멱등적(itempotent)이고 되돌릴 수 없습니다. 이벤트 루프가 닫힌 후에 다른 메서드를 호출해서는 안 됩니다.

`coroutine loop.shutdown_asyncgens()`
- 현재 열려있는 비동기 제너레이터 객체를 모두 aclose() 호출로 닫도록 예약 합니다. 이 메서드를 호출한 후에는, 새 비동기 생성기가 이터레이트 되면 이벤트 루프에서 경고를 보냅니다. 예약된 모든 비동기 제너레이터를 신뢰성 있게 종료하는 데 사용해야 합니다.
- asyncio.run()가 사용될 때 이 함수를 호출할 필요는 없다는 점에 유의하세요.

예:

```python
try:
    loop.run_forever()
finally:
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()
```

> 버전 3.6에서 추가되었습니다.

`coroutine loop.shutdown_default_executor(timeout=None)`
- 기본 실행기의 종료를 예약하고 ThreadPoolExecutor의 모든 스레드가 조인될 때까지 기다립니다. 이 메서드를 호출한 후에는 loop.run_in_executor()로 기본 실행기를 사용하면 RuntimeError가 발생합니다.
- timeout 매개변수는 실행기가 조인을 마칠 때까지 주어질 시간(float 초)을 지정합니다. 기본값인 None을 사용하면 실행기에 무제한의 시간이 허용됩니다.
- timeout에 도달하면 RuntimeWarning이 발생하고 기본 실행기는 스레드가 조인을 마칠 때까지 기다리지 않고 종료됩니다.

> `asyncio.run()`을 사용할 때는 이 메서드를 호출하지 마세요. 후자는 기본 실행기 종료를 자동으로 처리합니다.

> 버전 3.9에서 추가되었습니다.
> 버전 3.12에서 변경: timeout 매개변수가 추가되었습니다.


### 콜백 예약하기

`loop.call_soon(callback, *args, context=None)`
- 이벤트 루프의 다음 이터레이션 때 args 인자로 호출할 callback 콜백을 예약합니다.
- asyncio.Handle의 인스턴스를 반환하는데, 나중에 콜백을 취소하는 데 사용할 수 있습니다.
- 콜백은 등록된 순서대로 호출됩니다. 각 콜백은 정확히 한 번 호출됩니다.
- 선택적 키워드 전용 context 인자는 callback이 실행될 사용자 정의 contextvars.Context를 지정합니다. context가 제공되지 않으면 콜백은 현재 컨텍스트를 사용합니다.
- `call_soon_threadsafe()`와 달리 이 메서드는 스레드 안전하지 않습니다.

`loop.call_soon_threadsafe(callback, *args, context=None)`
- call_soon()의 스레드 안전 변형입니다. 다른 스레드에서 콜백을 예약할 때는 call_soon()이 스레드 안전하지 않으므로 이 함수를 사용해야 합니다.
- 메인 애플리케이션이 종료 중일 때 보조 스레드에서 닫힌 루프에 대해 호출되면 RuntimeError를 발생시킵니다.
- 설명서의 [동시성과 다중 스레딩](https://docs.python.org/ko/3/library/asyncio-dev.html#asyncio-multithreading) 절을 참고하십시오.

> 버전 3.7에서 변경: context 키워드 전용 매개 변수가 추가되었습니다. 자세한 정보는 PEP 567을 보십시오.

> [!NOTE]
> - 대부분 asyncio 예약 함수는 키워드 인자 전달을 허용하지 않습니다. 그렇게 하려면 `functools.partial()`을 사용하십시오:
> 
> ```python
> # "print("Hello", flush=True)"를 예약할 것입니다
> loop.call_soon(
>     functools.partial(print, "Hello", flush=True))
> ```
> 
> - asyncio는 디버그 및 오류 메시지에서 partial 객체를 더욱 잘 표시할 수 있으므로, partial 객체를 사용하는 것이 람다를 사용하는 것보다 편리합니다.

### 지연된 콜백 예약 (Scheduling delayed callbacks)
- 이벤트 루프는 콜백 함수가 미래의 어떤 시점에서 호출되도록 예약하는 메커니즘을 제공합니다. 이벤트 루프는 단조 시계를 사용하여 시간을 추적합니다.

`loop.call_later(delay, callback, *args, context=None)`
- 지정된 delay 초 (int 또는 float) 뒤에 callback이 호출되도록 예약합니다.
- asyncio.TimerHandle의 인스턴스가 반환되는데, 콜백을 취소하는 데 사용할 수 있습니다.
- callback은 정확히 한번 호출됩니다. 두 콜백이 정확히 같은 시간에 예약되면, 어떤 것이 먼저 호출되는지는 정의되지 않습니다.
- 선택적 위치 args는 호출 될 때 콜백에 전달됩니다. 콜백을 키워드 인자로 호출하고 싶으면 functools.partial()를 사용하십시오.
- 선택적인 키워드 전용 context 인자는 callback을 실행할 사용자 정의 contextvars.Context를 지정할 수 있게 합니다. context가 제공되지 않을 때는 현재 컨텍스트가 사용됩니다.

> 버전 3.7에서 변경: context 키워드 전용 매개 변수가 추가되었습니다. 자세한 정보는 PEP 567을 보십시오.
> 버전 3.8에서 변경: 파이썬 3.7 및 이전 버전에서 기본 이벤트 루프 구현을 사용할 때, delay는 하루를 초과할 수 없었습니다. 이 문제는 파이썬 3.8에서 수정되었습니다.

`loop.call_at(when, callback, *args, context=None)`
- 지정된 절대 타임스탬프 when(int 또는 float)에 callback이 호출되도록 예약합니다. loop.time()과 같은 시간 참조를 사용하십시오.
- 이 메서드의 동작은 call_later()와 같습니다.
- asyncio.TimerHandle의 인스턴스가 반환되는데, 콜백을 취소하는 데 사용할 수 있습니다.

> 버전 3.7에서 변경: context 키워드 전용 매개 변수가 추가되었습니다. 자세한 정보는 PEP 567을 보십시오.
> 버전 3.8에서 변경: 파이썬 3.7 및 이전 버전에서 기본 이벤트 루프 구현을 사용할 때, when와 현재 시각의 차이는 하루를 초과할 수 없었습니다. 이 문제는 파이썬 3.8에서 수정되었습니다.

`loop.time()`
- 이벤트 루프의 내부 단조 시계에 따라, float 값으로 현재 시각을 반환합니다.

> 버전 3.8에서 변경: 파이썬 3.7 및 이전 버전에서 제한 시간(상대적인 delay나 절대적인 when)은 1일을 초과하지 않아야 했습니다. 이 문제는 파이썬 3.8에서 수정되었습니다.

> [`asyncio.sleep()`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.sleep "asyncio.sleep") 함수.

### 퓨처와 태스크 만들기 (Creating futures and tasks)

`loop.create_future()`
- 이벤트 루프에 연결된 asyncio.Future 객체를 만듭니다.
- 이것이 asyncio에서 퓨처를 만드는 데 선호되는 방법입니다. 이렇게 하면 제삼자 이벤트 루프가 Future 객체의 다른 구현(더 나은 성능이나 계측(instrumentation))을 제공할 수 있습니다

> 버전 3.5.2에서 추가.

`loop.create_task(coro, *, name=None, context=None)`
- 코루틴 coro의 실행을 예약합니다. Task 객체를 반환합니다.
- 제삼자 이벤트 루프는 상호 운용성을 위해 자신만의 Task의 서브 클래스를 사용할 수 있습니다. 이 경우, 결과 형은 Task의 서브 클래스입니다.
- name 인자가 제공되고 None이 아니면, Task.set_name()을 사용하여 태스크의 이름으로 설정됩니다.
- 선택적 키워드 전용 context 인자를 통해 coro가 실행될 사용자 정의 contextvars.Context를 지정할 수 있습니다. context가 제공되지 않으면 현재 컨텍스트의 복사본이 생성됩니다.

> 버전 3.8에서 변경: name 매개변수가 추가되었습니다.
> 버전 3.11에서 변경: context 매개변수가 추가되었습니다.

`loop.set_task_factory(factory)`
- `loop.create_task()`에 의해 사용되는 태스크 팩토리를 설정합니다.
- factory가 None이면 기본 태스크 팩토리가 설정됩니다. 그렇지 않으면, factory는 (loop, coro, context=None) 시그니처와 일치하는 호출 가능한 객체여야 합니다. 여기서 loop는 활성 이벤트 루프에 대한 참조이고 coro는 코루틴 객체입니다. 호출 가능한 객체는 asyncio.Future와 호환되는 객체를 반환해야 합니다.

`loop.get_task_factory()`
- 태스크 팩토리를 반환하거나, 기본값이 사용 중이면 None을 반환합니다.


### 네트워크 연결 열기 (Opening network connections)

`coroutine loop.create_connection(protocol_factory, host=None, port=None, *, ssl=None, family=0, proto=0, flags=0, sock=None, local_addr=None, server_hostname=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None, happy_eyeballs_delay=None, interleave=None, all_errors=False)`

- 주어진 host와 port로 지정된 주소로의 스트리밍 트랜스포트 연결을 엽니다.
- 소켓 패밀리는 host(또는 제공된 family 인자)에 따라 AF_INET 또는 AF_INET6가 될 수 있습니다.
- 소켓 타입은 SOCK_STREAM이 될 것입니다.
- protocol_factory는 반드시 asyncio 프로토콜 구현을 반환하는 콜러블이어야 합니다.
- 이 메서드는 백그라운드에서 연결을 맺으려고 시도합니다. 성공하면, (transport, protocol) 쌍을 반환합니다.
- 하부 연산의 시간순 개요는 다음과 같습니다:
	1. 연결이 맺어지고, 이를 위한 트랜스포트(transport)가 만들어집니다.
	2. protocol_factory가 인자 없이 호출되고, 프로토콜(protocol) 인스턴스를 반환할 것으로 기대됩니다.
	3. 프로토콜 인스턴스는 connection_made() 메서드를 호출함으로써 트랜스포트와 연결됩니다.
	4. 성공하면 (transport, protocol) 튜플이 반환됩니다.
- 만들어진 트랜스포트는 구현 의존적인 양방향 스트림입니다.
- `ssl`: 주어지고 거짓이 아니면, SSL/TLS 트랜스포트가 만들어집니다 (기본적으로는 평범한 TCP 트랜스포트가 만들어집니다). ssl이 ssl.SSLContext 객체면, 트랜스포트를 만들 때 이 컨텍스트가 사용됩니다; ssl이 True면, ssl.create_default_context()가 반환하는 기본 컨텍스트가 사용됩니다. ([SSL/TLS 보안 고려 사항](https://docs.python.org/ko/3/library/ssl.html#ssl-security))
- `server_hostname`는 대상 서버의 인증서가 일치될 호스트 이름을 설정하거나 대체합니다. ssl이 None이 아닐 때만 전달되어야 합니다. 기본적으로 host 인자의 값이 사용됩니다. host가 비어 있으면, 기본값이 없고 server_hostname 값을 전달해야 합니다. server_hostname이 빈 문자열이면, 호스트 이름 일치가 비활성화됩니다 (이것은 심각한 보안 위험으로, 잠재적인 중간자 공격을 허용하게 됩니다).
- family, proto, flags는 host 결정을 위해 getaddrinfo()에 전달할 선택적 주소 패밀리, 프로토콜, 플래그입니다. 주어지면, 이것들은 모두 해당하는 socket 모듈 상수에 대응하는 정수여야 합니다.
- 주어지면, happy_eyeballs_delay는 이 연결에 대해 Happy Eyeballs를 활성화합니다. 다음 시도를 병렬로 시작하기 전에, 연결 시도가 완료되기를 기다리는 시간(초)을 나타내는 부동 소수점 숫자여야 합니다. 이것은 RFC 8305에 정의된 "연결 시도 지연(Connection Attempt Delay)" 입니다. RFC에서 권장하는 적절한 기본값은 0.25(250밀리 초)입니다.
- interleave는 호스트 이름이 여러 IP 주소로 해석될 때 주소 재정렬을 제어합니다. 0이거나 지정되지 않으면, 재정렬이 수행되지 않고, 주소는 getaddrinfo()에 의해 반환된 순서대로 시도됩니다. 양의 정수가 지정되면, 주소는 주소 패밀리에 의해 인터리브 되고, 주어진 정수는 RFC 8305에 정의된 대로 "첫 번째 주소 패밀리 수(First Address Family Count)"로 해석됩니다. 기본값은 happy_eyeballs_delay가 지정되지 않으면 0이고, 지정되면 1입니다.
- sock이 주어지면, 트랜스포트가 사용할, 기존의 이미 연결된 socket.socket 객체여야 합니다. sock이 주어지면, host, port, family, proto, flags, happy_eyeballs_delay, interleave, local_addr를 지정해서는 안 됩니다.
 
> sock 인자는 생성된 트랜스포트에 소켓의 소유권을 이전합니다. 소켓을 닫으려면 트랜스포트의 close() 메서드를 호출하십시오.

- local_addr이 주어지면, 소켓을 로컬로 바인딩하는 데 사용되는 (local_host, local_port) 튜플입니다. local_host와 local_port는 host와 port와 유사하게 getaddrinfo()를 사용하여 조회됩니다.
- ssl_handshake_timeout은 (TLS 연결의 경우) 연결을 중단하기 전에 TLS 핸드 셰이크가 완료될 때까지 대기하는 시간(초)입니다. None (기본값) 이면 60.0 초가 사용됩니다.
- ssl_shutdown_timeout은 연결을 중단하기 전에 SSL 종료가 완료될 때까지 대기하는 시간(초)입니다. None (기본값)이면 30.0 초가 사용됩니다.
- all_errors는 연결을 생성할 수 없을 때 발생하는 예외를 결정합니다. 기본적으로 단일 Exception만 발생합니다: 예외가 하나뿐이거나 모든 오류의 메시지가 동일한 경우 첫 번째 예외, 또는 오류 메시지가 결합된 단일 OSError. all_errors가 True이면 모든 예외를 포함하는 ExceptionGroup이 발생합니다 (예외가 하나뿐이더라도).

> 버전 3.5에서 변경: ProactorEventLoop에 SSL/TLS에 대한 지원이 추가되었습니다.
> 버전 3.6에서 변경: 모든 TCP 연결에 대해 기본적으로 socket.TCP_NODELAY 소켓 옵션이 설정됩니다.
> 버전 3.7에서 변경: ssl_handshake_timeout 매개변수가 추가되었습니다.
> 버전 3.8에서 변경: happy_eyeballs_delay와 interleave 매개변수가 추가되었습니다.
> 
> Happy Eyeballs Algorithm: 이중 스택 호스트와의 성공. 서버의 IPv4 경로와 프로토콜이 작동하지만 서버의 IPv6 경로와 프로토콜이 작동하지 않을 때, 이중 스택 클라이언트 애플리케이션은 IPv4 전용 클라이언트에 비해 상당한 연결 지연을 경험합니다. 이는 이중 스택 클라이언트가 더 나쁜 사용자 경험을 갖게 되므로 바람직하지 않습니다. 이 문서는 이 사용자가 볼 수 있는 지연을 줄이는 알고리즘에 대한 요구 사항을 지정하고 알고리즘을 제공합니다.
> 자세한 정보: https://datatracker.ietf.org/doc/html/rfc6555
> 
> 버전 3.11에서 변경: ssl_shutdown_timeout 매개변수가 추가되었습니다.
> 버전 3.12에서 변경: all_errors가 추가되었습니다.

> open_connection() 함수는 고수준 대안 API입니다. async/await 코드에서 직접 사용할 수 있는 (StreamReader, StreamWriter) 쌍을 반환합니다.

`coroutine loop.create_datagram_endpoint(protocol_factory, local_addr=None, remote_addr=None, *, family=0, proto=0, flags=0, reuse_port=None, allow_broadcast=None, sock=None)`

- 데이터 그램 연결을 만듭니다.
- 소켓 패밀리는 host(또는 제공된 family 인자)에 따라 AF_INET, AF_INET6, 또는 AF_UNIX가 될 수 있습니다.
- 소켓 타입은 SOCK_DGRAM이 될 것입니다.
- protocol_factory는 반드시 프로토콜 구현을 반환하는 콜러블이어야 합니다.
- 성공하면 (transport, protocol) 튜플이 반환됩니다.
- local_addr이 주어지면, 소켓을 로컬로 바인딩하는 데 사용되는 (local_host, local_port) 튜플입니다. local_host와 local_port는 getaddrinfo()를 사용하여 조회됩니다.
- remote_addr이 주어지면, 소켓을 원격 주소에 연결하는 데 사용되는 (remote_host, remote_port) 튜플입니다. remote_host와 remote_port는 getaddrinfo()를 사용하여 조회됩니다.
- family, proto, flags는 host 결정을 위해 getaddrinfo()에 전달할 선택적 주소 패밀리, 프로토콜, 플래그입니다. 주어지면, 이것들은 모두 해당하는 socket 모듈 상수에 대응하는 정수여야 합니다.
- reuse_port는 이 엔드포인트가 다른 기존 엔드포인트들이 바인딩된 것과 동일한 포트에 바인딩될 수 있도록 커널에 알립니다. 단, 모든 엔드포인트가 생성될 때 이 플래그를 설정해야 합니다. 이 옵션은 Windows와 일부 Unix에서 지원되지 않습니다. socket.SO_REUSEPORT 상수가 정의되지 않은 경우 이 기능은 지원되지 않습니다.
- allow_broadcast는 이 말단이 브로드캐스트 주소로 메시지를 보낼 수 있도록 커널에 알립니다.
- sock은 트랜스포트가 사용할 소켓 객체로, 기존의 이미 연결된 socket.socket 객체를 사용하기 위해 선택적으로 지정할 수 있습니다. 지정되면 local_addr과 remote_addr를 생략해야 합니다 (반드시 None이어야 합니다).

> sock 인자는 생성된 트랜스포트에 소켓의 소유권을 이전합니다. 소켓을 닫으려면 트랜스포트의 close() 메서드를 호출하십시오.

- UDP 메아리 클라이언트 프로토콜과 UDP 메아리 서버 프로토콜 예제를 참고하세요.

> 버전 3.4.4에서 변경: family, proto, flags, reuse_address, reuse_port, allow_broadcast, sock 매개변수가 추가되었습니다.
> 버전 3.8에서 변경: 윈도우에 대한 지원이 추가되었습니다.
> 버전 3.8.1에서 변경: reuse_address 매개변수는 더 이상 지원되지 않습니다. socket.SO_REUSEADDR 사용은 UDP에 대해 중요한 보안 문제를 제기하기 때문입니다. 명시적으로 reuse_address=True를 전달하면 예외가 발생합니다.
> 
> UID가 다른 여러 프로세스가 SO_REUSEADDR를 사용하여 소켓을 같은 UDP 소켓 주소에 할당하면, 들어오는 패킷이 소켓 간에 무작위로 분산될 수 있습니다.
> 
> 지원되는 플랫폼의 경우, reuse_port를 유사한 기능의 대체로 사용할 수 있습니다. reuse_port를 사용하면 대신 socket.SO_REUSEPORT가 사용되며, 이는 특히 UID가 다른 프로세스가 소켓을 동일한 소켓 주소에 할당하는 것을 방지합니다.
>
>버전 3.11에서 변경: Python 3.8.1, 3.7.6 및 3.6.10 이후로 비활성화된 reuse_address 매개변수가 완전히 제거되었습니다.

`coroutine loop.create_unix_connection(protocol_factory, path=None, *, ssl=None, sock=None, server_hostname=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None)`

- 유닉스 연결을 만듭니다.
- 소켓 패밀리는 [`AF_UNIX`](https://docs.python.org/ko/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX")가 될 것입니다; 소켓 타입은 [`SOCK_STREAM`](https://docs.python.org/ko/3/library/socket.html#socket.SOCK_STREAM "socket.SOCK_STREAM")이 될 것입니다.
- 성공하면 (transport, protocol) 튜플이 반환됩니다.
- path는 유닉스 도메인 소켓의 이름이며, sock 매개 변수가 지정되지 않으면 필수입니다. 추상 유닉스 소켓, [`str`](https://docs.python.org/ko/3/library/stdtypes.html#str "str"), [`bytes`](https://docs.python.org/ko/3/library/stdtypes.html#bytes "bytes"), [`Path`](https://docs.python.org/ko/3/library/pathlib.html#pathlib.Path "pathlib.Path") 경로가 지원됩니다.
- 이 메서드의 인자에 관한 정보는 [`loop.create_connection()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection") 메서드의 설명서를 참조하십시오.

> 가용성: 유닉스.

> 버전 3.7에서 변경: ssl_handshake_timeout 매개변수가 추가되었습니다. path 매개변수는 이제 [경로와 유사한 객체](https://docs.python.org/ko/3/glossary.html#term-path-like-object)가 될 수 있습니다.
> 버전 3.11에서 변경: ssl_shutdown_timeout 매개변수가 추가되었습니다.

### 네트워크 서버 만들기 (Creating network servers)

`coroutine loop.create_server(protocol_factory, host=None, port=None, *, family=socket.AF_UNSPEC, flags=socket.AI_PASSIVE, sock=None, backlog=100, ssl=None, reuse_address=None, reuse_port=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None, start_serving=True)`

- TCP 서버(소켓 타입 [SOCK_STREAM](https://docs.python.org/ko/3/library/socket.html#socket.SOCK_STREAM "socket.SOCK_STREAM"))를 host 주소의 port에서 리스닝하도록 생성합니다.
- [Server](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Server "asyncio.Server") 객체를 반환합니다.
- protocol_factory는 반드시 [프로토콜](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio-protocol) 구현을 반환하는 콜러블이어야 합니다.
- host 매개 변수는 서버가 리스닝할 위치를 결정하는 여러 형으로 설정할 수 있습니다.:
    - host가 문자열이면, TCP 서버는 host로 지정된 단일 네트워크 인터페이스에 바인딩 됩니다.
    - host가 문자열의 시퀀스면, TCP 서버는 시퀀스로 지정된 모든 네트워크 인터페이스에 바인딩 됩니다.
    - host가 빈 문자열이거나 None이면, 모든 인터페이스가 사용되는 것으로 가정하고, 여러 소켓의 리스트가 반환됩니다 (대체로 IPv4 하나와 IPv6 하나).
- port 매개변수는 서버가 리스닝해야 할 포트를 지정하는 데 사용할 수 있습니다. 0이나 None(기본값)인 경우, 사용되지 않은 임의의 포트가 선택됩니다(host가 여러 네트워크 인터페이스로 해석되면 각 인터페이스마다 다른 임의의 포트가 선택됩니다).
- family는 [socket.AF_INET](https://docs.python.org/ko/3/library/socket.html#socket.AF_INET "socket.AF_INET")이나 [AF_INET6](https://docs.python.org/ko/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6")로 설정하여 소켓이 IPv4나 IPv6를 사용하도록 강제할 수 있습니다. 설정하지 않으면 family는 호스트 이름에서 결정됩니다(기본값은 [AF_UNSPEC](https://docs.python.org/ko/3/library/socket.html#socket.AF_UNSPEC "socket.AF_UNSPEC")).
- flags은 [getaddrinfo()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.getaddrinfo "asyncio.loop.getaddrinfo")를 위한 비트 마스크입니다.
- sock은 기존 소켓 객체를 사용하기 위해 선택적으로 지정할 수 있습니다. 지정되면, host 및 port는 지정할 수 없습니다.

> sock 인자는 생성된 서버에 소켓의 소유권을 이전합니다. 소켓을 닫으려면 서버의 [close()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Server.close "asyncio.Server.close") 메서드를 호출하세요.

- backlog은 [listen()](https://docs.python.org/ko/3/library/socket.html#socket.socket.listen "socket.socket.listen")으로 전달되는 최대 대기 연결 수 입니다 (기본값은 100).
- ssl을 [SSLContext](https://docs.python.org/ko/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") 인스턴스로 설정하면, 들어오는 연결에 TLS를 사용합니다.
- reuse_address는, 일반적인 시간제한이 만료될 때까지 기다리지 않고, TIME_WAIT 상태의 로컬 소켓을 재사용하도록 커널에 알려줍니다. 지정하지 않으면 유닉스에서 자동으로 True로 설정됩니다.
- reuse_port는 모두 만들 때 이 플래그를 설정하는 한, 이 말단이 다른 기존 말단이 바인드 된 것과 같은 포트에 바인드 되도록 허용하도록 커널에 알려줍니다. 이 옵션은 윈도우에서 지원되지 않습니다.
- ssl_handshake_timeout은 (TLS 서버의 경우) 연결을 중단하기 전에 TLS 핸드 셰이크가 완료될 때까지 대기하는 시간(초)입니다. None (기본값) 이면 60.0 초가 사용됩니다.
- ssl_shutdown_timeout은 연결을 중단하기 전에 SSL 종료가 완료될 때까지 대기하는 시간(초)입니다. None (기본값)이면 30.0초가 사용됩니다.
- start_serving을 True (기본값) 로 설정하면, 생성된 서버가 즉시 연결을 받아들입니다. False로 설정되면, 사용자는 서버가 연결을 받기 시작하도록 [Server.start_serving()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Server.start_serving "asyncio.Server.start_serving")이나 [Server.serve_forever()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Server.serve_forever "asyncio.Server.serve_forever")를 await 해야 합니다.

> 버전 3.5에서 변경: [ProactorEventLoop](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop")에 SSL/TLS에 대한 지원이 추가되었습니다.
> 버전 3.5.1에서 변경: host 매개 변수는 문자열의 시퀀스가 될 수 있습니다.
> 버전 3.6에서 변경: ssl_handshake_timeout 및 start_serving 매개변수가 추가되었습니다. 모든 TCP 연결에 대해 [socket.TCP_NODELAY](https://docs.python.org/ko/3/library/socket.html#socket-unix-constants) 소켓 옵션이 기본적으로 설정됩니다.
> 버전 3.11에서 변경: ssl_shutdown_timeout 매개변수가 추가되었습니다.

> [start_server()](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.start_server "asyncio.start_server") 함수는 async/await 코드에서 사용할 수 있는 [StreamReader](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.StreamReader "asyncio.StreamReader") 및 [StreamWriter](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.StreamWriter "asyncio.StreamWriter") 쌍을 반환하는 고수준의 대체 API입니다.

`coroutine loop.create_unix_server(protocol_factory, path=None, *, sock=None, backlog=100, ssl=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None, start_serving=True)`

- [loop.create_server()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server")와 유사하지만 [AF_UNIX](https://docs.python.org/ko/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX") 소켓 패밀리로 작동합니다.
- path는 유닉스 도메인 소켓의 이름이며, sock 매개 변수가 제공되지 않으면 필수입니다. 추상 유닉스 소켓, [str](https://docs.python.org/ko/3/library/stdtypes.html#str "str"), [bytes](https://docs.python.org/ko/3/library/stdtypes.html#bytes "bytes"), [Path](https://docs.python.org/ko/3/library/pathlib.html#pathlib.Path "pathlib.Path") 경로가 지원됩니다.
- 이 메서드의 인자에 대한 정보는 [loop.create_server()](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server") 메서드의 설명서를 참조하십시오.

> 가용성: 유닉스.

> 버전 3.7에서 변경: ssl_handshake_timeout 및 start_serving 매개변수가 추가되었습니다. path 매개변수는 이제 [Path](https://docs.python.org/ko/3/library/pathlib.html#pathlib.Path "pathlib.Path") 객체가 될 수 있습니다.
> 버전 3.11에서 변경: ssl_shutdown_timeout 매개변수가 추가되었습니다.

`coroutine loop.connect_accepted_socket(protocol_factory, sock, *, ssl=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None)`

- 이미 받아들인 연결을 트랜스포트/프로토콜 쌍으로 래핑합니다.
- 이 메서드는 asyncio 밖에서 연결을 받아들이지만, 그 연결을 처리하는데 asyncio를 사용하는 서버에서 사용됩니다.
- protocol_factory는 반드시 [프로토콜](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio-protocol) 구현을 반환하는 콜러블이어야 합니다.
- sock은 [socket.accept](https://docs.python.org/ko/3/library/socket.html#socket.socket.accept "socket.socket.accept")가 반환한 기존 소켓 객체입니다.

> sock 인자는 생성된 트랜스포트에 소켓의 소유권을 이전합니다. 소켓을 닫으려면 트랜스포트의 [close()](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.BaseTransport.close "asyncio.BaseTransport.close") 메서드를 호출하세요.

- ssl을 [SSLContext](https://docs.python.org/ko/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")로 설정하면, 들어오는 연결에 SSL을 사용합니다.
- ssl_handshake_timeout은 (SSL 연결의 경우) 연결을 중단하기 전에 SSL 핸드 셰이크가 완료될 때까지 대기하는 시간(초)입니다. None (기본값) 이면 60.0 초가 사용됩니다.
- ssl_shutdown_timeout은 연결을 중단하기 전에 SSL 종료가 완료될 때까지 대기하는 시간(초)입니다. None (기본값)이면 30.0초가 사용됩니다.
- (transport, protocol) 쌍을 반환합니다.

> 버전 3.5.3에서 추가.
> 버전 3.7에서 변경: ssl_handshake_timeout 매개변수가 추가되었습니다.
> 버전 3.11에서 변경: ssl_shutdown_timeout 매개변수가 추가되었습니다.

### 파일 전송 (Transferring files)

`coroutine loop.sendfile(transport, file, offset=0, count=None, *, fallback=True)`

- file을 transport로 보냅니다. 전송된 총 바이트 수를 반환합니다.
- 이 메서드는 가능한 경우 고성능 [os.sendfile()](https://docs.python.org/ko/3/library/os.html#os.sendfile "os.sendfile")을 사용합니다.
- file는 바이너리 모드로 열린 일반 파일 객체여야 합니다.
- offset은 파일 읽기 시작할 위치를 알려줍니다. count를 제공하면, EOF에 도달할 때까지 파일을 보내는 대신, 전송할 총 바이트 수를 지정합니다. 파일의 위치가 갱신됩니다, 이 메서드가 에러를 일으킬 때조차. 그리고, [file.tell()](https://docs.python.org/ko/3/library/io.html#io.IOBase.tell "io.IOBase.tell")는 실제 전송된 바이트 수를 얻는 데 사용될 수 있습니다.
- fallback을 True로 설정하면, 플랫폼이 sendfile 시스템 호출을 지원하지 않을 때 (가령 유닉스에서 SSL 소켓을 사용하거나 윈도우인 경우), asyncio가 파일을 수동으로 읽고 보내도록 합니다.
- 시스템이 sendfile 시스템 호출을 지원하지 않고 fallback 이 `False` 면 [`SendfileNotAvailableError`]([https://docs.python.org/ko/3/library/asyncio-exceptions.html#asyncio.SendfileNotAvailableError](https://docs.python.org/ko/3/library/asyncio-exceptions.html#asyncio.SendfileNotAvailableError) "asyncio.SendfileNotAvailableError") 를 발생시킵니다.

> Added in version 3.7.

### TLS 업그레이드 (TLS Upgrade)

`coroutine loop.start_tls(transport, protocol, sslcontext, *, server_side=False, server_hostname=None, ssl_handshake_timeout=None, ssl_shutdown_timeout=None)`

- 기존 트랜스포트 기반 연결을 TLS로 업그레이드합니다.
- TLS 코더/디코더 인스턴스를 생성하고 transport와 protocol 사이에 삽입합니다. 코더/디코더는 transport 측 프로토콜과 protocol 측 트랜스포트를 모두 구현합니다.
- 생성된 두 인터페이스 인스턴스를 반환합니다. await 이후에는 protocol이 원래의 transport 사용을 중지하고 반환된 객체와만 통신해야 합니다. 왜냐하면 코더가 protocol 측 데이터를 캐시하고 간헐적으로 transport와 추가 TLS 세션 패킷을 교환하기 때문입니다.
- 일부 상황(예: 전달된 트랜스포트가 이미 닫히고 있는 경우)에서는 None을 반환할 수 있습니다.
- create_server()와 create_connection() 같은 메서드가 반환하는 transport 와 protocol 인스턴스.
- sslcontext: 구성된 SSLContext 의 인스턴스.
- (create_server() 에 의해 생성된 것과 같은) 서버 측 연결이 업그레이드될 때 server_side 에 True 를 전달합니다.
- server_hostname: 대상 서버의 인증서가 일치될 호스트 이름을 설정하거나 대체합니다.
- ssl_handshake_timeout 은 (TLS 연결의 경우) 연결을 중단하기 전에 TLS 핸드 셰이크가 완료될 때까지 대기하는 시간(초)입니다. None (기본값) 이면 60.0 초가 사용됩니다.
- ssl_shutdown_timeout은 SSL 셧다운이 완료될 때까지 기다리는 시간(초)입니다. 연결을 중단하기 전에 기다립니다. None (기본값)이면 30.0 초가 사용됩니다.

> 버전 3.7에 추가되었습니다.
> 버전 3.11에서 변경: ssl_shutdown_timeout 매개변수가 추가되었습니다.

### 파일 기술자 관찰하기 (Watching File Descriptors)

loop.add_reader(fd, callback, *args)

fd 파일 기술자가 읽기 가능한지 관찰하기 시작하고, 일단 fd가 읽기 가능해지면 지정한 인자로 callback 을 호출합니다.

loop.remove_reader(fd)

fd 파일 기술자에 대한 읽기 가능 모니터링을 중지합니다. fd가 이전에 읽기를 위해 모니터링되고 있었다면 True를 반환합니다.

loop.add_writer(fd, callback, *args)

fd 파일 기술자가 쓰기 가능한지 관찰하기 시작하고, 일단 fd가 쓰기 가능해지면 지정한 인자로 callback 을 호출합니다.

callback 에 키워드 인자를 전달하려면 functools.partial()를 사용하십시오.

loop.remove_writer(fd)

fd 파일 기술자에 대한 쓰기 가능 모니터링을 중지합니다. fd가 이전에 쓰기를 위해 모니터링되고 있었다면 True를 반환합니다.

이 메서드의 일부 제한 사항은 플랫폼 지원 절을 참조하십시오.

### 소켓 객체로 직접 작업하기 (Working with Socket Objects Directly)

일반적으로 loop.create_connection() 및 loop.create_server()와 같은 트랜스포트 기반 API를 사용하는 프로토콜 구현은 소켓을 직접 사용하는 구현보다 빠릅니다. 그러나, 성능이 결정적이지 않고 socket 객체로 직접 작업하는 것이 더 편리한 사용 사례가 있습니다.

코루틴 loop.sock_recv(sock, nbytes)

sock 에서 최대 nbytes 를 수신합니다. socket.recv() 의 비동기 버전.

수신한 데이터를 바이트열 객체로 반환합니다.

sock 은 반드시 비 블로킹 소켓이어야 합니다.

버전 3.7에서 변경: 이 메서드가 항상 코루틴 메서드라고 설명되어왔지만, 파이썬 3.7 이전에는 Future를 반환했습니다. 파이썬 3.7부터, 이것은 async def 메서드입니다.

코루틴 loop.sock_recv_into(sock, buf)

sock 에서 buf 버퍼로 데이터를 수신합니다. 블로킹 socket.recv_into() 메서드를 따라 만들어졌습니다.

버퍼에 기록된 바이트 수를 돌려줍니다.

sock 은 반드시 비 블로킹 소켓이어야 합니다.

버전 3.7에 추가되었습니다.

코루틴 loop.sock_recvfrom(sock, bufsize)

sock에서 최대 bufsize의 데이터그램을 수신합니다. socket.recvfrom()의 비동기 버전입니다.

(수신된 데이터, 원격 주소) 튜플을 반환합니다.

sock 은 반드시 비 블로킹 소켓이어야 합니다.

버전 3.11에 추가되었습니다.

코루틴 loop.sock_recvfrom_into(sock, buf, nbytes=0)

sock에서 최대 nbytes의 데이터그램을 buf로 수신합니다. socket.recvfrom_into()의 비동기 버전입니다.

(수신된 바이트 수, 원격 주소) 튜플을 반환합니다.

sock 은 반드시 비 블로킹 소켓이어야 합니다.

버전 3.11에 추가되었습니다.

코루틴 loop.sock_sendall(sock, data)

data 를 sock 소켓으로 보냅니다. socket.sendall() 의 비동기 버전.

이 메서드는 data 의 모든 데이터가 송신되거나 에러가 발생할 때까지 소켓으로 계속 송신합니다. 성공하면 None 이 반환됩니다. 에러가 발생하면 예외가 발생합니다. 또한, 연결의 수신 단에서 성공적으로 처리한 (있기는 하다면) 데이터의 크기를 확인하는 방법은 없습니다.

sock 은 반드시 비 블로킹 소켓이어야 합니다.

버전 3.7에서 변경: 이 메서드가 항상 코루틴 메서드라고 설명되어왔지만, 파이썬 3.7 이전에는 Future를 반환했습니다. 파이썬 3.7부터, 이것은 async def 메서드입니다.

코루틴 loop.sock_sendto(sock, data, address)

sock에서 address로 데이터그램을 보냅니다. socket.sendto()의 비동기 버전입니다.

전송된 바이트 수를 반환합니다.

sock 은 반드시 비 블로킹 소켓이어야 합니다.

버전 3.11에 추가되었습니다.

코루틴 loop.sock_connect(sock, address)

sock을 address에 있는 원격 소켓에 연결합니다.

socket.connect() 의 비동기 버전.

sock 은 반드시 비 블로킹 소켓이어야 합니다.

버전 3.5.2에서 변경: address 는 더는 결정될 필요가 없습니다. sock_connect 는 socket.inet_pton()을 호출하여 address 가 이미 결정되었는지를 검사합니다. 그렇지 않으면, loop.getaddrinfo() 가 address 를 결정하는 데 사용됩니다.

참조

loop.create_connection()과 asyncio.open_connection().

코루틴 loop.sock_accept(sock)

연결을 받아들입니다. 블로킹 socket.accept() 메서드를 따라 만들어졌습니다.

소켓은 주소에 바인드 되어 연결을 리스닝해야 합니다. 반환 값은 (conn, address) 쌍인데, conn 은 연결로 데이터를 주고받을 수 있는 새 소켓 객체이고, address 는 연결의 반대편 끝의 소켓에 바인드 된 주소입니다.

sock 은 반드시 비 블로킹 소켓이어야 합니다.

버전 3.7에서 변경: 이 메서드가 항상 코루틴 메서드라고 설명되어왔지만, 파이썬 3.7 이전에는 Future를 반환했습니다. 파이썬 3.7부터, 이것은 async def 메서드입니다.

참조

loop.create_server()와 start_server().

코루틴 loop.sock_sendfile(sock, file, offset=0, count=None, *, fallback=True)

가능하면 고성능 os.sendfile 을 사용하여 파일을 보냅니다. 전송된 총 바이트 수를 반환합니다.

socket.sendfile()의 비동기 버전.

sock 은 반드시 비 블로킹 socket.SOCK_STREAM socket 이어야 합니다.

file 는 바이너리 모드로 열린 일반 파일 객체여야 합니다.

offset 은 파일 읽기 시작할 위치를 알려줍니다. count 를 제공하면, EOF에 도달할 때까지 파일을 보내는 대신, 전송할 총 바이트 수를 지정합니다. 파일의 위치가 갱신됩니다, 이 메서드가 에러를 일으킬 때조차. 그리고, file.tell() 는 실제 전송된 바이트 수를 얻는 데 사용될 수 있습니다.

fallback 을 True 로 설정하면, 플랫폼이 sendfile 시스템 호출을 지원하지 않을 때 (가령 유닉스에서 SSL 소켓을 사용하거나 윈도우인 경우), asyncio 가 파일을 수동으로 읽고 보내도록 합니다.

시스템이 sendfile 시스템 호출을 지원하지 않고 fallback 이 False 면 SendfileNotAvailableError 를 발생시킵니다.

sock 은 반드시 비 블로킹 소켓이어야 합니다.

버전 3.7에 추가되었습니다.

### [DNS](https://docs.python.org/ko/3/library/asyncio-eventloop.html#id12)[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#dns "Link to this heading")

_coroutine_ loop.getaddrinfo(_host_, _port_, _*_, _family=0_, _type=0_, _proto=0_, _flags=0_)[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.getaddrinfo "Link to this definition")

[`socket.getaddrinfo()`](https://docs.python.org/ko/3/library/socket.html#socket.getaddrinfo "socket.getaddrinfo") 의 비동기 버전.

_coroutine_ loop.getnameinfo(_sockaddr_, _flags=0_)[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.getnameinfo "Link to this definition")

[`socket.getnameinfo()`](https://docs.python.org/ko/3/library/socket.html#socket.getnameinfo "socket.getnameinfo") 의 비동기 버전.

참고

 

Both _getaddrinfo_ and _getnameinfo_ internally utilize their synchronous versions through the loop’s default thread pool executor. When this executor is saturated, these methods may experience delays, which higher-level networking libraries may report as increased timeouts. To mitigate this, consider using a custom executor for other user tasks, or setting a default executor with a larger number of workers.

버전 3.7에서 변경: _getaddrinfo_ 와 _getnameinfo_ 메서드는 모두 코루틴 메서드라고 설명되어왔지만, 파이썬 3.7 이전에 실제로는 [`asyncio.Future`](https://docs.python.org/ko/3/library/asyncio-future.html#asyncio.Future "asyncio.Future") 객체를 반환했습니다. 파이썬 3.7부터 두 가지 메서드 모두 코루틴입니다.

### [파이프로 작업하기](https://docs.python.org/ko/3/library/asyncio-eventloop.html#id13)[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#working-with-pipes "Link to this heading")

_coroutine_ loop.connect_read_pipe(_protocol_factory_, _pipe_)[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.connect_read_pipe "Link to this definition")

이벤트 루프에 _pipe_의 읽기용 끝을 등록합니다.

_protocol_factory_ 는 반드시 [asyncio 프로토콜](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio-protocol) 구현을 반환하는 콜러블이어야 합니다.

_pipe_는 [파일류 객체](https://docs.python.org/ko/3/glossary.html#term-file-object)입니다.

쌍 `(transport, protocol)`를 반환합니다. 여기서 _transport_는 [`ReadTransport`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.ReadTransport "asyncio.ReadTransport") 인터페이스를 지원하고, _protocol_은 _protocol_factory_에 의해 인스턴스로 만들어진 객체입니다.

[`SelectorEventLoop`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop") 이벤트 루프를 사용하면, _pipe_ 는 비 블로킹 모드로 설정됩니다.

_coroutine_ loop.connect_write_pipe(_protocol_factory_, _pipe_)[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.connect_write_pipe "Link to this definition")

이벤트 루프에 _pipe_의 쓰기용 끝을 등록합니다.

_protocol_factory_ 는 반드시 [asyncio 프로토콜](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio-protocol) 구현을 반환하는 콜러블이어야 합니다.

_pipe_는 [파일류 객체](https://docs.python.org/ko/3/glossary.html#term-file-object)입니다.

쌍 `(transport, protocol)`를 반환합니다. 여기서 _transport_는 [`WriteTransport`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.WriteTransport "asyncio.WriteTransport") 인터페이스를 지원하고, _protocol_은 _protocol_factory_에 의해 인스턴스로 만들어진 객체입니다.

[`SelectorEventLoop`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop") 이벤트 루프를 사용하면, _pipe_ 는 비 블로킹 모드로 설정됩니다.

참고

 

윈도우에서 [`SelectorEventLoop`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop")는 위의 메서드들을 지원하지 않습니다. 윈도우에서는 대신 [`ProactorEventLoop`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop")를 사용하십시오.

더 보기

 

[`loop.subprocess_exec()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec "asyncio.loop.subprocess_exec") 와 [`loop.subprocess_shell()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_shell "asyncio.loop.subprocess_shell") 메서드.

### [유닉스 시그널](https://docs.python.org/ko/3/library/asyncio-eventloop.html#id14)[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#unix-signals "Link to this heading")

loop.add_signal_handler(_signum_, _callback_, _*args_)[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.add_signal_handler "Link to this definition")

_callback_을 _signum_ 시그널의 처리기로 설정합니다.

콜백은 다른 대기 중인 콜백과 해당 이벤트 루프의 실행 가능한 코루틴과 함께 _loop_에 의해 호출됩니다. [`signal.signal()`](https://docs.python.org/ko/3/library/signal.html#signal.signal "signal.signal")을 사용하여 등록된 시그널 처리기와 달리, 이 함수로 등록된 콜백은 이벤트 루프와 상호 작용할 수 있습니다.

시그널 번호가 유효하지 않거나 잡을 수 없으면 [`ValueError`](https://docs.python.org/ko/3/library/exceptions.html#ValueError "ValueError") 를 발생시킵니다. 처리기를 설정하는 데 문제가 있는 경우 [`RuntimeError`](https://docs.python.org/ko/3/library/exceptions.html#RuntimeError "RuntimeError") 를 발생시킵니다.

_callback_ 에 [키워드 인자를 전달하려면](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio-pass-keywords) [`functools.partial()`](https://docs.python.org/ko/3/library/functools.html#functools.partial "functools.partial")를 사용하십시오.

[`signal.signal()`](https://docs.python.org/ko/3/library/signal.html#signal.signal "signal.signal")와 마찬가지로, 이 함수는 메인 스레드에서 호출되어야 합니다.

loop.remove_signal_handler(_sig_)[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.remove_signal_handler "Link to this definition")

_sig_ 시그널의 처리기를 제거합니다.

시그널 처리기가 제거되면 `True` 를, 주어진 시그널에 처리기가 설정되지 않았으면 `False` 를 반환합니다.

[가용성](https://docs.python.org/ko/3/library/intro.html#availability): 유닉스.

더 보기

 

[`signal`](https://docs.python.org/ko/3/library/signal.html#module-signal "signal: Set handlers for asynchronous events.") 모듈.

### [스레드 또는 프로세스 풀에서 코드를 실행하기](https://docs.python.org/ko/3/library/asyncio-eventloop.html#id15)[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#executing-code-in-thread-or-process-pools "Link to this heading")

_awaitable_ loop.run_in_executor(_executor_, _func_, _*args_)[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "Link to this definition")

지정된 실행기에서 _func_ 가 호출되도록 배치합니다.

The _executor_ argument should be an [`concurrent.futures.Executor`](https://docs.python.org/ko/3/library/concurrent.futures.html#concurrent.futures.Executor "concurrent.futures.Executor") instance. The default executor is used if _executor_ is `None`. The default executor can be set by [`loop.set_default_executor()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.set_default_executor "asyncio.loop.set_default_executor"), otherwise, a [`concurrent.futures.ThreadPoolExecutor`](https://docs.python.org/ko/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor") will be lazy-initialized and used by [`run_in_executor()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "asyncio.loop.run_in_executor") if needed.

예:

import asyncio
import concurrent.futures

def blocking_io():
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    with open('/dev/urandom', 'rb') as f:
        return f.read(100)

def cpu_bound():
    # CPU-bound operations will block the event loop:
    # in general it is preferable to run them in a
    # process pool.
    return sum(i * i for i in range(10 ** 7))

async def main():
    loop = asyncio.get_running_loop()

    ## Options:

    # 1. Run in the default loop's executor:
    result = await loop.run_in_executor(
        None, blocking_io)
    print('default thread pool', result)

    # 2. Run in a custom thread pool:
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, blocking_io)
        print('custom thread pool', result)

    # 3. Run in a custom process pool:
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, cpu_bound)
        print('custom process pool', result)

if __name__ == '__main__':
    asyncio.run(main())

Note that the entry point guard (`if __name__ == '__main__'`) is required for option 3 due to the peculiarities of [`multiprocessing`](https://docs.python.org/ko/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism."), which is used by [`ProcessPoolExecutor`](https://docs.python.org/ko/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor"). See [Safe importing of main module](https://docs.python.org/ko/3/library/multiprocessing.html#multiprocessing-safe-main-import).

이 메서드는 [`asyncio.Future`](https://docs.python.org/ko/3/library/asyncio-future.html#asyncio.Future "asyncio.Future") 객체를 반환합니다.

_func_ 에 [키워드 인자를 전달하려면](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio-pass-keywords) [`functools.partial()`](https://docs.python.org/ko/3/library/functools.html#functools.partial "functools.partial")를 사용하십시오.

버전 3.5.3에서 변경: [`loop.run_in_executor()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "asyncio.loop.run_in_executor") 는 더는 자신이 만드는 스레드 풀 실행기의 `max_workers` 를 설정하지 않습니다. 대신 스레드 풀 실행기([`ThreadPoolExecutor`](https://docs.python.org/ko/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor"))가 스스로 기본값을 설정하도록 합니다.

loop.set_default_executor(_executor_)[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.set_default_executor "Link to this definition")

Set _executor_ as the default executor used by [`run_in_executor()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "asyncio.loop.run_in_executor"). _executor_ must be an instance of [`ThreadPoolExecutor`](https://docs.python.org/ko/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor").

버전 3.11에서 변경: _executor_ must be an instance of [`ThreadPoolExecutor`](https://docs.python.org/ko/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor").

### [에러 처리 API](https://docs.python.org/ko/3/library/asyncio-eventloop.html#id16)[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#error-handling-api "Link to this heading")

이벤트 루프에서 예외를 처리하는 방법을 사용자 정의 할 수 있습니다.

loop.set_exception_handler(_handler_)[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.set_exception_handler "Link to this definition")

_handler_ 를 새 이벤트 루프 예외 처리기로 설정합니다.

_handler_가 `None` 이면, 기본 예외 처리기가 설정됩니다. 그렇지 않으면, _handler_는 반드시 `(loop, context)` 와 일치하는 서명을 가진 콜러블이어야 합니다. 여기서 `loop`는 활성 이벤트 루프에 대한 참조가 될 것이고, `context` 는 예외에 관한 세부 정보를 담고 있는 `dict` 객체가 됩니다 (context에 대한 자세한 내용은 [`call_exception_handler()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.call_exception_handler "asyncio.loop.call_exception_handler") 문서를 참조하십시오).

If the handler is called on behalf of a [`Task`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task "asyncio.Task") or [`Handle`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Handle "asyncio.Handle"), it is run in the [`contextvars.Context`](https://docs.python.org/ko/3/library/contextvars.html#contextvars.Context "contextvars.Context") of that task or callback handle.

버전 3.12에서 변경: The handler may be called in the [`Context`](https://docs.python.org/ko/3/library/contextvars.html#contextvars.Context "contextvars.Context") of the task or handle where the exception originated.

loop.get_exception_handler()[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.get_exception_handler "Link to this definition")

현재 예외 처리기를 반환하거나, 사용자 정의 예외 처리기가 설정되지 않았으면 `None` 을 반환합니다.

Added in version 3.5.2.

loop.default_exception_handler(_context_)[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.default_exception_handler "Link to this definition")

기본 예외 처리기.

예외가 발생하고 예외 처리기가 설정되지 않았을 때 호출됩니다. 기본 동작으로 위임하려는 사용자 정의 예외 처리기가 호출할 수 있습니다.

_context_ 매개 변수는 [`call_exception_handler()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.call_exception_handler "asyncio.loop.call_exception_handler") 에서와 같은 의미입니다.

loop.call_exception_handler(_context_)[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.call_exception_handler "Link to this definition")

현재 이벤트 루프 예외 처리기를 호출합니다.

_context_ 는 다음 키를 포함하는 `dict` 객체입니다 (새 키가 미래의 파이썬 버전에서 추가될 수 있습니다):

- ‘message’: 에러 메시지;
    
- ‘exception’ (선택적): 예외 객체;
    
- ‘future’ (선택적): [`asyncio.Future`](https://docs.python.org/ko/3/library/asyncio-future.html#asyncio.Future "asyncio.Future") 인스턴스;
    
- ‘task’ (optional): [`asyncio.Task`](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio.Task "asyncio.Task") instance;
    
- ‘handle’ (선택적): [`asyncio.Handle`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Handle "asyncio.Handle") 인스턴스;
    
- ‘protocol’ (선택적): [프로토콜](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio-protocol) 인스턴스;
    
- ‘transport’ (선택적): [트랜스포트](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio-transport) 인스턴스;
    
- ‘socket’ (optional): [`socket.socket`](https://docs.python.org/ko/3/library/socket.html#socket.socket "socket.socket") instance;
    
- ‘asyncgen’ (optional): Asynchronous generator that caused
    
    the exception.
    

참고

 

이 메서드는 서브 클래스 된 이벤트 루프에서 재정의되지 않아야 합니다. 사용자 정의 예외 처리를 위해서는 [`set_exception_handler()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.set_exception_handler "asyncio.loop.set_exception_handler") 메서드를 사용하십시오.

### [디버그 모드 활성화](https://docs.python.org/ko/3/library/asyncio-eventloop.html#id17)[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#enabling-debug-mode "Link to this heading")

loop.get_debug()[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.get_debug "Link to this definition")

이벤트 루프의 디버그 모드([`bool`](https://docs.python.org/ko/3/library/functions.html#bool "bool"))를 가져옵니다.

기본값은 환경 변수 [`PYTHONASYNCIODEBUG`](https://docs.python.org/ko/3/using/cmdline.html#envvar-PYTHONASYNCIODEBUG) 가 비어 있지 않은 문자열로 설정되면 `True` 이고, 그렇지 않으면 `False` 입니다.

loop.set_debug(_enabled: [bool](https://docs.python.org/ko/3/library/functions.html#bool "bool")_)[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.set_debug "Link to this definition")

이벤트 루프의 디버그 모드를 설정합니다.

버전 3.7에서 변경: 이제 새로운 [파이썬 개발 모드](https://docs.python.org/ko/3/library/devmode.html#devmode)를 사용하여 디버그 모드를 활성화할 수도 있습니다.

loop.slow_callback_duration[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.slow_callback_duration "Link to this definition")

This attribute can be used to set the minimum execution duration in seconds that is considered “slow”. When debug mode is enabled, “slow” callbacks are logged.

Default value is 100 milliseconds.

더 보기

 

[asyncio의 디버그 모드](https://docs.python.org/ko/3/library/asyncio-dev.html#asyncio-debug-mode).

### [자식 프로세스 실행하기](https://docs.python.org/ko/3/library/asyncio-eventloop.html#id18)[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#running-subprocesses "Link to this heading")

이 하위 절에서 설명하는 메서드는 저수준입니다. 일반적인 async/await 코드에서는 대신 고수준의 [`asyncio.create_subprocess_shell()`](https://docs.python.org/ko/3/library/asyncio-subprocess.html#asyncio.create_subprocess_shell "asyncio.create_subprocess_shell") 및 [`asyncio.create_subprocess_exec()`](https://docs.python.org/ko/3/library/asyncio-subprocess.html#asyncio.create_subprocess_exec "asyncio.create_subprocess_exec") 편리 함수를 사용하는 것을 고려하십시오.

참고

 

On Windows, the default event loop [`ProactorEventLoop`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop") supports subprocesses, whereas [`SelectorEventLoop`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop") does not. See [Subprocess Support on Windows](https://docs.python.org/ko/3/library/asyncio-platforms.html#asyncio-windows-subprocess) for details.

_coroutine_ loop.subprocess_exec(_protocol_factory_, _*args_, _stdin=subprocess.PIPE_, _stdout=subprocess.PIPE_, _stderr=subprocess.PIPE_, _**kwargs_)[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec "Link to this definition")

_args_로 지정된 하나 이상의 문자열 인자로 서브 프로세스를 만듭니다.

_args_는 반드시 다음과 같은 것으로 표현되는 문자열의 목록이어야 합니다:

- [`str`](https://docs.python.org/ko/3/library/stdtypes.html#str "str");
    
- 또는 [파일 시스템 인코딩](https://docs.python.org/ko/3/library/os.html#filesystem-encoding)으로로 인코딩된 [`bytes`](https://docs.python.org/ko/3/library/stdtypes.html#bytes "bytes").
    

첫 번째 문자열은 프로그램 실행 파일을 지정하고, 나머지 문자열은 인자를 지정합니다. 함께, 문자열 인자들은 프로그램의 `argv`를 구성합니다.

이것은 `shell=False`와 문자열의 목록을 첫 번째 인자로 호출된 표준 라이브러리 [`subprocess.Popen`](https://docs.python.org/ko/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") 클래스와 유사합니다. 그러나 [`Popen`](https://docs.python.org/ko/3/library/subprocess.html#subprocess.Popen "subprocess.Popen")이 문자열 목록인 단일 인자를 받아들이지만, _subprocess_exec_는 여러 문자열 인자를 받아들입니다.

_protocol_factory_는 반드시 [`asyncio.SubprocessProtocol`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.SubprocessProtocol "asyncio.SubprocessProtocol") 클래스의 서브 클래스를 반환하는 콜러블이어야 합니다.

다른 매개 변수:

- _stdin_은 다음 중 하나일 수 있습니다:
    
    - a file-like object
        
    - an existing file descriptor (a positive integer), for example those created with [`os.pipe()`](https://docs.python.org/ko/3/library/os.html#os.pipe "os.pipe")
        
    - [`subprocess.PIPE`](https://docs.python.org/ko/3/library/subprocess.html#subprocess.PIPE "subprocess.PIPE") 상수 (기본값), 새 파이프를 만들고 연결합니다,
        
    - 서브 프로세스가 이 프로세스의 파일 기술자를 상속하게 하는 값 `None`
        
    - 특수 [`os.devnull`](https://docs.python.org/ko/3/library/os.html#os.devnull "os.devnull") 파일이 사용될 것임을 나타내는 [`subprocess.DEVNULL`](https://docs.python.org/ko/3/library/subprocess.html#subprocess.DEVNULL "subprocess.DEVNULL") 상수
        
- _stdout_은 다음 중 하나일 수 있습니다:
    
    - a file-like object
        
    - [`subprocess.PIPE`](https://docs.python.org/ko/3/library/subprocess.html#subprocess.PIPE "subprocess.PIPE") 상수 (기본값), 새 파이프를 만들고 연결합니다,
        
    - 서브 프로세스가 이 프로세스의 파일 기술자를 상속하게 하는 값 `None`
        
    - 특수 [`os.devnull`](https://docs.python.org/ko/3/library/os.html#os.devnull "os.devnull") 파일이 사용될 것임을 나타내는 [`subprocess.DEVNULL`](https://docs.python.org/ko/3/library/subprocess.html#subprocess.DEVNULL "subprocess.DEVNULL") 상수
        
- _stderr_은 다음 중 하나일 수 있습니다:
    
    - a file-like object
        
    - [`subprocess.PIPE`](https://docs.python.org/ko/3/library/subprocess.html#subprocess.PIPE "subprocess.PIPE") 상수 (기본값), 새 파이프를 만들고 연결합니다,
        
    - 서브 프로세스가 이 프로세스의 파일 기술자를 상속하게 하는 값 `None`
        
    - 특수 [`os.devnull`](https://docs.python.org/ko/3/library/os.html#os.devnull "os.devnull") 파일이 사용될 것임을 나타내는 [`subprocess.DEVNULL`](https://docs.python.org/ko/3/library/subprocess.html#subprocess.DEVNULL "subprocess.DEVNULL") 상수
        
    - [`subprocess.STDOUT`](https://docs.python.org/ko/3/library/subprocess.html#subprocess.STDOUT "subprocess.STDOUT") 상수, 표준 에러 스트림을 프로세스의 표준 출력 스트림에 연결합니다
        
- 다른 모든 키워드 인자는 해석 없이 [`subprocess.Popen`](https://docs.python.org/ko/3/library/subprocess.html#subprocess.Popen "subprocess.Popen")로 전달됩니다. 다만, _bufsize_, _universal_newlines_, _shell_, _text_, _encoding_ 및 _errors_는 예외인데, 이것들은 지정되지 않아야 합니다.
    
    `asyncio` 서브 프로세스 API는 스트림을 텍스트로 디코딩하는 것을 지원하지 않습니다. [`bytes.decode()`](https://docs.python.org/ko/3/library/stdtypes.html#bytes.decode "bytes.decode")는 스트림에서 반환된 바이트열을 텍스트로 변환하는 데 사용될 수 있습니다.
    

If a file-like object passed as _stdin_, _stdout_ or _stderr_ represents a pipe, then the other side of this pipe should be registered with [`connect_write_pipe()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.connect_write_pipe "asyncio.loop.connect_write_pipe") or [`connect_read_pipe()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.connect_read_pipe "asyncio.loop.connect_read_pipe") for use with the event loop.

다른 인자에 관한 설명은 [`subprocess.Popen`](https://docs.python.org/ko/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") 클래스의 생성자를 참조하십시오.

`(transport, protocol)` 쌍을 반환합니다. 여기에서 _transport_는 [`asyncio.SubprocessTransport`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.SubprocessTransport "asyncio.SubprocessTransport") 베이스 클래스를 따르고, _protocol_은 _protocol_factory_에 의해 인스턴스로 만들어진 객체입니다.

_coroutine_ loop.subprocess_shell(_protocol_factory_, _cmd_, _*_, _stdin=subprocess.PIPE_, _stdout=subprocess.PIPE_, _stderr=subprocess.PIPE_, _**kwargs_)[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_shell "Link to this definition")

플랫폼의 “셸” 구문을 사용하는 _cmd_로 자식 프로세스를 만듭니다. _cmd_는 [`str`](https://docs.python.org/ko/3/library/stdtypes.html#str "str")이나 [파일 시스템 인코딩](https://docs.python.org/ko/3/library/os.html#filesystem-encoding)으로 인코딩된 [`bytes`](https://docs.python.org/ko/3/library/stdtypes.html#bytes "bytes") 일 수 있습니다.

이것은 `shell=True`로 호출된 표준 라이브러리 [`subprocess.Popen`](https://docs.python.org/ko/3/library/subprocess.html#subprocess.Popen "subprocess.Popen") 클래스와 유사합니다.

_protocol_factory_는 반드시 [`SubprocessProtocol`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.SubprocessProtocol "asyncio.SubprocessProtocol") 클래스의 서브 클래스를 반환하는 콜러블이어야 합니다.

나머지 인자에 관한 자세한 내용은 [`subprocess_exec()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec "asyncio.loop.subprocess_exec")를 참조하십시오.

`(transport, protocol)` 쌍을 반환합니다. 여기서 _transport_는 [`SubprocessTransport`](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio.SubprocessTransport "asyncio.SubprocessTransport") 베이스 클래스를 따르고, _protocol_은 _protocol_factory_에 의해 인스턴스로 만들어진 객체입니다.

참고

 

[셸 주입](https://en.wikipedia.org/wiki/Shell_injection#Shell_injection) 취약점을 피하고자 모든 공백과 특수 문자를 적절하게 따옴표 처리하는 것은 응용 프로그램의 책임입니다. [`shlex.quote()`](https://docs.python.org/ko/3/library/shlex.html#shlex.quote "shlex.quote") 함수를 사용하여 셸 명령을 구성하는 데 사용될 문자열에 있는 공백 및 특수 문자를 올바르게 이스케이프 할 수 있습니다.

## 콜백 핸들[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#callback-handles "Link to this heading")

_class_ asyncio.Handle[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Handle "Link to this definition")

[`loop.call_soon()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.call_soon "asyncio.loop.call_soon"), [`loop.call_soon_threadsafe()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.call_soon_threadsafe "asyncio.loop.call_soon_threadsafe") 에 의해 반환되는 콜백 래퍼 객체.

get_context()[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Handle.get_context "Link to this definition")

Return the [`contextvars.Context`](https://docs.python.org/ko/3/library/contextvars.html#contextvars.Context "contextvars.Context") object associated with the handle.

Added in version 3.12.

cancel()[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Handle.cancel "Link to this definition")

콜백을 취소합니다. 콜백이 이미 취소되었거나 실행되었다면 이 메서드는 아무 효과가 없습니다.

cancelled()[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Handle.cancelled "Link to this definition")

콜백이 취소되었으면 `True` 을 반환합니다.

Added in version 3.7.

_class_ asyncio.TimerHandle[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.TimerHandle "Link to this definition")

[`loop.call_later()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.call_later "asyncio.loop.call_later") 및 [`loop.call_at()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.call_at "asyncio.loop.call_at") 에 의해 반환되는 콜백 래퍼 객체.

이 클래스는 [`Handle`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Handle "asyncio.Handle")의 서브 클래스입니다.

when()[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.TimerHandle.when "Link to this definition")

예약된 콜백 시간을 [`float`](https://docs.python.org/ko/3/library/functions.html#float "float") 초로 반환합니다.

시간은 절대 타임스탬프입니다. [`loop.time()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.time "asyncio.loop.time") 과 같은 시간 참조를 사용합니다.

Added in version 3.7.

## 서버 객체[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#server-objects "Link to this heading")

Server 객체는 [`loop.create_server()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server"), [`loop.create_unix_server()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_server "asyncio.loop.create_unix_server"), [`start_server()`](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.start_server "asyncio.start_server"), [`start_unix_server()`](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.start_unix_server "asyncio.start_unix_server")로 만듭니다.

Do not instantiate the [`Server`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Server "asyncio.Server") class directly.

_class_ asyncio.Server[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Server "Link to this definition")

_Server_ 객체는 비동기 컨텍스트 관리자입니다. `async with` 문에서 사용될 때, `async with` 문이 완료되면 서버 객체가 닫혀 있고 새 연결을 받아들이지 않는다는 것이 보장됩니다:

srv = await loop.create_server(...)

async with srv:
    # some code

# At this point, srv is closed and no longer accepts new connections.

버전 3.7에서 변경: Server 객체는 파이썬 3.7부터 비동기 컨텍스트 관리자입니다.

버전 3.11에서 변경: This class was exposed publicly as `asyncio.Server` in Python 3.9.11, 3.10.3 and 3.11.

close()[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Server.close "Link to this definition")

서버를 중지합니다: 리스닝 소켓을 닫고 [`sockets`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Server.sockets "asyncio.Server.sockets") 어트리뷰트를 `None` 으로 설정합니다.

이미 받아들여진 클라이언트 연결을 나타내는 소켓은 열린 채로 있습니다.

The server is closed asynchronously; use the [`wait_closed()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Server.wait_closed "asyncio.Server.wait_closed") coroutine to wait until the server is closed (and no more connections are active).

get_loop()[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Server.get_loop "Link to this definition")

서버 객체와 연관된 이벤트 루프를 반환합니다.

Added in version 3.7.

_coroutine_ start_serving()[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Server.start_serving "Link to this definition")

연결을 받아들이기 시작합니다.

This method is idempotent, so it can be called when the server is already serving.

[`loop.create_server()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server")와 [`asyncio.start_server()`](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.start_server "asyncio.start_server") 의 _start_serving_ 키워드 전용 매개 변수는 즉시 연결을 받아들이지 않는 서버 객체를 만들 수 있도록 합니다. 이 경우 `Server.start_serving()`, 또는 [`Server.serve_forever()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Server.serve_forever "asyncio.Server.serve_forever")를 사용하여 Server가 연결을 받아들이기 시작하도록 할 수 있습니다.

Added in version 3.7.

_coroutine_ serve_forever()[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Server.serve_forever "Link to this definition")

코루틴이 취소될 때까지 연결을 받아들이기 시작합니다. `serve_forever` 태스크를 취소하면 서버가 닫힙니다.

이 메서드는 서버가 이미 연결을 받아들이고 있어도 호출 할 수 있습니다. 하나의 _Server_ 객체 당 하나의 `serve_forever` 태스크만 존재할 수 있습니다.

예:

async def client_connected(reader, writer):
    # Communicate with the client with
    # reader/writer streams.  For example:
    await reader.readline()

async def main(host, port):
    srv = await asyncio.start_server(
        client_connected, host, port)
    await srv.serve_forever()

asyncio.run(main('127.0.0.1', 0))

Added in version 3.7.

is_serving()[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Server.is_serving "Link to this definition")

서버가 새 연결을 받아들이고 있으면 `True` 를 반환합니다.

Added in version 3.7.

_coroutine_ wait_closed()[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Server.wait_closed "Link to this definition")

Wait until the [`close()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Server.close "asyncio.Server.close") method completes and all active connections have finished.

sockets[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.Server.sockets "Link to this definition")

List of socket-like objects, `asyncio.trsock.TransportSocket`, which the server is listening on.

버전 3.7에서 변경: 파이썬 3.7 이전에는 `Server.sockets` 가 서버 소켓의 내부 리스트를 직접 반환했습니다. 3.7에서는 그 리스트의 복사본이 반환됩니다.

## 이벤트 루프 구현[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#event-loop-implementations "Link to this heading")

asyncio에는 두 가지 이벤트 루프 구현이 함께 제공됩니다: [`SelectorEventLoop`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop") 및 [`ProactorEventLoop`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop").

기본적으로 asyncio는 유닉스에서 [`SelectorEventLoop`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop")를, 윈도우에서 [`ProactorEventLoop`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop")를 사용하도록 구성됩니다.

_class_ asyncio.SelectorEventLoop[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "Link to this definition")

[`selectors`](https://docs.python.org/ko/3/library/selectors.html#module-selectors "selectors: High-level I/O multiplexing.") 모듈을 기반으로 하는 이벤트 루프.

주어진 플랫폼에서 사용할 수 있는 가장 효율적인 _selector_를 사용합니다. 정확한 셀렉터 구현을 수동으로 구성하여 사용할 수도 있습니다.:

import asyncio
import selectors

class MyPolicy(asyncio.DefaultEventLoopPolicy):
   def new_event_loop(self):
      selector = selectors.SelectSelector()
      return asyncio.SelectorEventLoop(selector)

asyncio.set_event_loop_policy(MyPolicy())

[가용성](https://docs.python.org/ko/3/library/intro.html#availability): 유닉스, 윈도우.

_class_ asyncio.ProactorEventLoop[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "Link to this definition")

“I/O 완료 포트”(IOCP)를 사용하는 윈도우용 이벤트 루프.

[가용성](https://docs.python.org/ko/3/library/intro.html#availability): 윈도우.

더 보기

 

[I/O 완료 포트에 관한 MSDN 설명서](https://docs.microsoft.com/en-ca/windows/desktop/FileIO/i-o-completion-ports).

_class_ asyncio.AbstractEventLoop[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.AbstractEventLoop "Link to this definition")

asyncio 호환 이벤트 루프의 추상 베이스 클래스.

The [이벤트 루프 메서드](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio-event-loop-methods) section lists all methods that an alternative implementation of `AbstractEventLoop` should have defined.

## 예제[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#examples "Link to this heading")

이 절의 모든 예는 **의도적으로** [`loop.run_forever()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.run_forever "asyncio.loop.run_forever") 및 [`loop.call_soon()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.call_soon "asyncio.loop.call_soon")와 같은 저수준 이벤트 루프 API를 사용하는 방법을 보여줍니다. 현대 asyncio 응용 프로그램은 거의 이런 식으로 작성할 필요가 없습니다; [`asyncio.run()`](https://docs.python.org/ko/3/library/asyncio-runner.html#asyncio.run "asyncio.run")과 같은 고수준 함수를 사용하는 것을 고려하십시오.

### call_soon()을 사용하는 Hello World[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#hello-world-with-call-soon "Link to this heading")

콜백을 예약하기 위해 [`loop.call_soon()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.call_soon "asyncio.loop.call_soon") 메서드를 사용하는 예제. 콜백은 `"Hello World"` 를 표시한 다음 이벤트 루프를 중지합니다:

import asyncio

def hello_world(loop):
    """A callback to print 'Hello World' and stop the event loop"""
    print('Hello World')
    loop.stop()

loop = asyncio.new_event_loop()

# Schedule a call to hello_world()
loop.call_soon(hello_world, loop)

# Blocking call interrupted by loop.stop()
try:
    loop.run_forever()
finally:
    loop.close()

더 보기

 

코루틴과 [`run()`](https://docs.python.org/ko/3/library/asyncio-runner.html#asyncio.run "asyncio.run") 함수로 작성된 유사한 [Hello World](https://docs.python.org/ko/3/library/asyncio-task.html#coroutine) 예제.

### call_later()로 현재 날짜를 표시합니다.[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#display-the-current-date-with-call-later "Link to this heading")

초마다 현재 날짜를 표시하는 콜백의 예입니다. 콜백은 [`loop.call_later()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.call_later "asyncio.loop.call_later") 메서드를 사용하여 5초 동안 자신을 다시 예약한 다음 이벤트 루프를 중지합니다:

import asyncio
import datetime

def display_date(end_time, loop):
    print(datetime.datetime.now())
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, display_date, end_time, loop)
    else:
        loop.stop()

loop = asyncio.new_event_loop()

# Schedule the first call to display_date()
end_time = loop.time() + 5.0
loop.call_soon(display_date, end_time, loop)

# Blocking call interrupted by loop.stop()
try:
    loop.run_forever()
finally:
    loop.close()

더 보기

 

코루틴과 [`run()`](https://docs.python.org/ko/3/library/asyncio-runner.html#asyncio.run "asyncio.run") 함수로 작성된 유사한 [현재 날짜](https://docs.python.org/ko/3/library/asyncio-task.html#asyncio-example-sleep) 예제.

### 파일 기술자에서 읽기 이벤트를 관찰하기[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#watch-a-file-descriptor-for-read-events "Link to this heading")

[`loop.add_reader()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.add_reader "asyncio.loop.add_reader") 메서드를 사용하여 파일 기술자가 데이터를 수신할 때까지 기다렸다가 이벤트 루프를 닫습니다:

import asyncio
from socket import socketpair

# Create a pair of connected file descriptors
rsock, wsock = socketpair()

loop = asyncio.new_event_loop()

def reader():
    data = rsock.recv(100)
    print("Received:", data.decode())

    # We are done: unregister the file descriptor
    loop.remove_reader(rsock)

    # Stop the event loop
    loop.stop()

# Register the file descriptor for read event
loop.add_reader(rsock, reader)

# Simulate the reception of data from the network
loop.call_soon(wsock.send, 'abc'.encode())

try:
    # Run the event loop
    loop.run_forever()
finally:
    # We are done. Close sockets and the event loop.
    rsock.close()
    wsock.close()
    loop.close()

더 보기

- 트랜스포트, 프로토콜, [`loop.create_connection()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection") 메서드를 사용한 유사한 [예제](https://docs.python.org/ko/3/library/asyncio-protocol.html#asyncio-example-create-connection).
    
- 고수준의 [`asyncio.open_connection()`](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio.open_connection "asyncio.open_connection") 함수와 스트림을 사용하는 또 다른 유사한 [예제](https://docs.python.org/ko/3/library/asyncio-stream.html#asyncio-example-create-connection-streams).
    

### SIGINT 및 SIGTERM에 대한 시그널 처리기 설정[](https://docs.python.org/ko/3/library/asyncio-eventloop.html#set-signal-handlers-for-sigint-and-sigterm "Link to this heading")

(이 `signals` 예제는 유닉스에서만 작동합니다.)

Register handlers for signals [`SIGINT`](https://docs.python.org/ko/3/library/signal.html#signal.SIGINT "signal.SIGINT") and [`SIGTERM`](https://docs.python.org/ko/3/library/signal.html#signal.SIGTERM "signal.SIGTERM") using the [`loop.add_signal_handler()`](https://docs.python.org/ko/3/library/asyncio-eventloop.html#asyncio.loop.add_signal_handler "asyncio.loop.add_signal_handler") method:

import asyncio
import functools
import os
import signal

def ask_exit(signame, loop):
    print("got signal %s: exit" % signame)
    loop.stop()

async def main():
    loop = asyncio.get_running_loop()

    for signame in {'SIGINT', 'SIGTERM'}:
        loop.add_signal_handler(
            getattr(signal, signame),
            functools.partial(ask_exit, signame, loop))

    await asyncio.sleep(3600)

print("Event loop running for 1 hour, press Ctrl+C to interrupt.")
print(f"pid {os.getpid()}: send SIGINT or SIGTERM to exit.")

asyncio.run(main())

---
## 참조

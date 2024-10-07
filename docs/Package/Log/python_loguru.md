---
title: "[Python] 로구루 (Loguru)"
excerpt: 이 라이브러리는 표준 로거의 단점을 해결하는 유용한 기능들을 추가하여 Python 로깅을 덜 고통스럽게 만드는 것을 목표로 합니다. 애플리케이션에서 로그를 사용하는 것은 자동화되어야 하며, Loguru는 이를 즐겁고 강력하게 만들려고 노력합니다.
categories:
  - Python
tags:
  - Python
  - Python-Library
  - Log
  - Python-loguru
last_modified_at: 2024-04-11T15:11:34+09:00
link: https://loguru.readthedocs.io/en/stable/api/logger.html
상위 항목: "[[python_library|파이썬 라이브러리 (Python Library)]]"
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

> **Github**: [Delgan/loguru: Python logging made (stupidly) simple (github.com)](https://github.com/Delgan/loguru)

---
[![Loguru logo](https://raw.githubusercontent.com/Delgan/loguru/master/docs/_static/img/logo.png)](https://github.com/Delgan/loguru/blob/master/README.rst#readme)
[![Loguru logo](https://raw.githubusercontent.com/Delgan/loguru/master/docs/_static/img/demo.gif)](https://github.com/Delgan/loguru/blob/master/README.rst#readme)
**Loguru**는 Python에서 즐거운 로깅을 가능하게 하는 라이브러리입니다.

로거를 설정하는 것이 귀찮아서 `print()`를 사용한 적이 있나요?... 저도 그랬습니다. 하지만 로깅은 모든 애플리케이션의 기본이며 디버깅 과정을 쉽게 만듭니다. **Loguru**를 사용하면 처음부터 로깅을 사용하지 않을 이유가 없습니다. 단순히 `from loguru import logger`만으로 시작할 수 있습니다.

또한, 이 라이브러리는 표준 로거의 단점을 해결하는 유용한 기능들을 추가하여 Python 로깅을 덜 고통스럽게 만드는 것을 목표로 합니다. 애플리케이션에서 로그를 사용하는 것은 자동화되어야 하며, **Loguru**는 이를 즐겁고 강력하게 만들려고 노력합니다.

## 보일러플레이트 없이 바로 사용 가능 (Ready to use out of the box without boilerplate)

Loguru의 주요 개념은 **하나이며 유일한** [`logger`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger)가 있다는 것입니다.

편의를 위해 미리 구성되어 있으며 시작부터 `stderr`로 출력됩니다(하지만 이는 완전히 구성 가능합니다).

```python
from loguru import logger

logger.debug("바로 이거예요, 아름답고 간단한 로깅!")
```

[`logger`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger)는 단순히 로그 메시지를 구성된 핸들러로 전달하는 인터페이스일 뿐입니다. 간단하죠?

## 핸들러 없음, 포매터 없음, 필터 없음: 모든 것을 관리하는 하나의 함수 (No Handler, no Formatter, no Filter: one function to rule them all)

핸들러를 어떻게 추가하나요? 로그 포맷을 어떻게 설정하나요? 메시지를 어떻게 필터링하나요? 레벨을 어떻게 설정하나요?

한 가지 답변: [`add()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.add) 함수입니다.

```python
logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
```

이 함수는 [로그 메시지](https://loguru.readthedocs.io/en/stable/api/logger.html#message)를 [레코드 딕셔너리](https://loguru.readthedocs.io/en/stable/api/logger.html#record)로 컨텍스트화하여 관리하는 [싱크](https://loguru.readthedocs.io/en/stable/api/logger.html#sink)를 등록하는 데 사용해야 합니다. 싱크는 다양한 형태를 취할 수 있습니다: 단순한 함수, 문자열 경로, 파일과 유사한 객체, 코루틴 함수 또는 내장 핸들러.

이전에 추가한 핸들러를 [`remove()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.remove)할 수도 있습니다. 이는 추가할 때 반환된 식별자를 사용합니다. 이는 기본 `stderr` 핸들러를 대체하고 싶을 때 특히 유용합니다: 새로 시작하려면 `logger.remove()`를 호출하면 됩니다.

## 회전 / 보존 / 압축 기능이 있는 더 쉬운 파일 로깅 (Easier file logging with rotation / retention / compression)

로그 메시지를 파일로 보내고 싶다면 싱크로 문자열 경로만 사용하면 됩니다. 편의를 위해 자동으로 시간을 지정할 수도 있습니다:

```python
logger.add("file_{time}.log")
```

로그 회전이 필요하거나 오래된 로그를 제거하거나 파일을 닫을 때 압축하고 싶다면 [쉽게 구성](https://loguru.readthedocs.io/en/stable/api/logger.html#file)할 수 있습니다.

```python
logger.add("file_1.log", rotation="500 MB")    # 파일이 너무 커지면 자동으로 회전
logger.add("file_2.log", rotation="12:00")     # 매일 정오에 새 파일 생성
logger.add("file_3.log", rotation="1 week")    # 파일이 너무 오래되면 회전

logger.add("file_X.log", retention="10 days")  # 일정 시간 후 정리

logger.add("file_Y.log", compression="zip")    # 공간 절약
```

## 중괄호 스타일을 사용한 현대적인 문자열 포매팅 (Modern string formatting using braces style)

Loguru는 `%` 대신 훨씬 더 우아하고 강력한 `{}` 포매팅을 선호합니다. 로깅 함수는 실제로 `str.format()`과 동일합니다.

```python
logger.info("Python {}을(를) 사용한다면, 당연히 {feature}를 선호하세요!", 3.6, feature="f-strings")
```

## 스레드 또는 메인에서의 예외 캐치 (Exceptions catching within threads or main)

프로그램이 예기치 않게 충돌하는데 로그 파일에 아무것도 보이지 않은 적이 있나요? 스레드에서 발생하는 예외가 로깅되지 않는 것을 알아차린 적이 있나요? 이는 [`catch()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.catch) 데코레이터 / 컨텍스트 매니저를 사용하여 해결할 수 있습니다. 이는 모든 오류가 [`logger`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger)로 올바르게 전파되도록 보장합니다.

```python
@logger.catch
def my_function(x, y, z):
    # 오류가 발생해도 어쨌든 잡힙니다!
    return 1 / (x + y + z)
```

## 색상이 있는 예쁜 로깅 (Pretty logging with colors)

Loguru는 터미널이 호환되는 경우 자동으로 로그에 색상을 추가합니다. 싱크 포맷에서 [마크업 태그](https://loguru.readthedocs.io/en/stable/api/logger.html#color)를 사용하여 원하는 스타일을 정의할 수 있습니다.

```python
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")
```

## 비동기, 스레드 안전, 멀티프로세스 안전 (Asynchronous, Thread-safe, Multiprocess-safe)

[`logger`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger)에 추가된 모든 싱크는 기본적으로 스레드 안전합니다. 멀티프로세스 안전은 아니지만, 메시지를 `enqueue`하여 로그 무결성을 보장할 수 있습니다. 이 동일한 인수는 비동기 로깅을 원할 때도 사용할 수 있습니다.

```python
logger.add("somefile.log", enqueue=True)
```

싱크로 사용되는 코루틴 함수도 지원되며 [`complete()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.complete)로 대기해야 합니다.

## 완전히 설명적인 예외 (Fully descriptive exceptions)

코드에서 발생하는 예외를 로깅하는 것은 버그를 추적하는 데 중요하지만, 왜 실패했는지 모른다면 꽤 쓸모없습니다. Loguru는 변수 값을 포함한 전체 스택 트레이스를 표시할 수 있게 함으로써 문제를 식별하는 데 도움을 줍니다(이것은 [`better_exceptions`](https://github.com/Qix-/better-exceptions) 덕분입니다!).

코드:

```python
# 주의, "diagnose=True"는 기본값이며 프로덕션 환경에서 민감한 데이터를 유출할 수 있습니다
logger.add("out.log", backtrace=True, diagnose=True)

def func(a, b):
    return a / b

def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("뭐라고?!")

nested(0)
```

결과:

```
2018-07-17 01:38:43.975 | ERROR    | __main__:nested:10 - 뭐라고?!
Traceback (most recent call last):

  File "test.py", line 12, in <module>
    nested(0)
    └ <function nested at 0x7f5c755322f0>

> File "test.py", line 8, in nested
    func(5, c)
    │       └ 0
    └ <function func at 0x7f5c79fc2e18>

  File "test.py", line 4, in func
    return a / b
           │   └ 0
           └ 5

ZeroDivisionError: division by zero
```

이 기능은 프레임 데이터를 사용할 수 없기 때문에 기본 Python REPL에서는 작동하지 않습니다.

참고: [Loguru 사용 시 보안 고려 사항](https://loguru.readthedocs.io/en/stable/resources/recipes.html#security-considerations-when-using-loguru).

## 필요에 따른 구조화된 로깅 (Structured logging as needed)

로그를 쉽게 파싱하거나 전달하기 위해 직렬화하고 싶나요? `serialize` 인수를 사용하면 각 로그 메시지가 구성된 싱크로 전송되기 전에 JSON 문자열로 변환됩니다.

```python
logger.add(custom_sink_function, serialize=True)
```

[`bind()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.bind)를 사용하여 extra 레코드 속성을 수정함으로써 로거 메시지의 컨텍스트를 지정할 수 있습니다.

```python
logger.add("file.log", format="{extra[ip]} {extra[user]} {message}")
context_logger = logger.bind(ip="192.168.0.1", user="someone")
context_logger.info("로거의 컨텍스트를 쉽게 지정하세요")
context_logger.bind(user="someone_else").info("인라인 바인딩으로 extra 속성 추가")
context_logger.info("포매팅 중 kwargs를 사용하여 컨텍스트 추가: {user}", user="anybody")
```

[`contextualize()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.contextualize)를 사용하여 컨텍스트-로컬 상태를 일시적으로 수정할 수 있습니다:

```python
with logger.contextualize(task=task_id):
    do_something()
    logger.info("작업 종료")
```

[`bind()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.bind)와 `filter`를 결합하여 로그를 더 세밀하게 제어할 수도 있습니다:

```python
logger.add("special.log", filter=lambda record: "special" in record["extra"])
logger.debug("이 메시지는 파일에 로깅되지 않습니다")
logger.bind(special=True).info("하지만 이 메시지는 파일에 로깅됩니다!")
```

마지막으로, [`patch()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.patch) 메서드를 사용하면 각 새 메시지의 레코드 딕셔너리에 동적 값을 첨부할 수 있습니다:

```python
logger.add(sys.stderr, format="{extra[utc]} {message}")
logger = logger.patch(lambda record: record["extra"].update(utc=datetime.utcnow()))
```

여기 Loguru 라이브러리의 주요 기능들에 대한 한국어 번역입니다:

## 비용이 많이 드는 함수의 지연 평가 (Lazy evaluation of expensive functions)

때로는 프로덕션 환경에서 성능 저하 없이 상세한 정보를 로깅하고 싶을 수 있습니다. 이를 위해 [`opt()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.opt) 메서드를 사용할 수 있습니다.

```python
logger.opt(lazy=True).debug("If sink level <= DEBUG: {x}", x=lambda: expensive_function(2**64))

# 참고로, "opt()"는 다양한 용도로 사용됩니다
logger.opt(exception=True).info("Error stacktrace added to the log message (tuple accepted too)")
logger.opt(colors=True).info("Per message <blue>colors</blue>")
logger.opt(record=True).info("Display values from the record (eg. {record[thread]})")
logger.opt(raw=True).info("Bypass sink formatting\n")
logger.opt(depth=1).info("Use parent stack context (useful within wrapped functions)")
logger.opt(capture=False).info("Keyword arguments not added to {dest} dict", dest="extra")
```

## 사용자 정의 가능한 레벨 (Customizable levels)

Loguru는 모든 표준 [로깅 레벨](https://loguru.readthedocs.io/en/stable/api/logger.html#levels)과 함께 [`trace()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.trace)와 [`success()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.success)가 추가되어 제공됩니다. 더 필요하신가요? 그렇다면 [`level()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.level) 함수를 사용하여 직접 만들 수 있습니다.

```python
new_level = logger.level("SNAKY", no=38, color="<yellow>", icon="🐍")

logger.log("SNAKY", "Here we go!")
```

## 향상된 날짜시간 처리 (Better datetime handling)

표준 로깅은 `datefmt`나 `msecs`, `%(asctime)s`와 `%(created)s`, 시간대 정보가 없는 naive 날짜시간, 직관적이지 않은 포맷팅 등의 인자로 복잡합니다. Loguru는 [이를 해결합니다](https://loguru.readthedocs.io/en/stable/api/logger.html#time):

```python
logger.add("file.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")
```

## 스크립트와 라이브러리에 적합 (Suitable for scripts and libraries)

스크립트에서 로거를 사용하는 것은 쉬우며, 시작 시 [`configure()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.configure)할 수 있습니다. 라이브러리 내에서 Loguru를 사용할 때는 절대 [`add()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.add)를 호출하지 말고 대신 [`disable()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.disable)을 사용하여 로깅 함수를 no-op으로 만드세요. 개발자가 라이브러리의 로그를 보고 싶다면 다시 [`enable()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.enable)할 수 있습니다.

```python
# 스크립트용
config = {
    "handlers": [
        {"sink": sys.stdout, "format": "{time} - {message}"},
        {"sink": "file.log", "serialize": True},
    ],
    "extra": {"user": "someone"}
}
logger.configure(**config)

# 라이브러리용, 라이브러리의 `__name__`이어야 합니다
logger.disable("my_library")
logger.info("No matter added sinks, this message is not displayed")

# 애플리케이션에서 라이브러리의 로거를 활성화
logger.enable("my_library")
logger.info("This message however is propagated to the sinks")
```

추가적인 편의를 위해, [`loguru-config`](https://github.com/erezinman/loguru-config) 라이브러리를 사용하여 설정 파일에서 직접 `logger`를 설정할 수도 있습니다.

## 표준 로깅과 완전히 호환 (Entirely compatible with standard logging)

내장 로깅 `Handler`를 Loguru 싱크로 사용하고 싶으신가요?

```python
handler = logging.handlers.SysLogHandler(address=('localhost', 514))
logger.add(handler)
```

Loguru 메시지를 표준 로깅으로 전파해야 하나요?

```python
class PropagateHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        logging.getLogger(record.name).handle(record)

logger.add(PropagateHandler(), format="{message}")
```

표준 로깅 메시지를 Loguru 싱크로 가로채고 싶으신가요?

```python
class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        # 해당하는 Loguru 레벨이 있으면 가져옵니다.
        level: str | int
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # 로깅된 메시지가 시작된 호출자를 찾습니다.
        frame, depth = inspect.currentframe(), 0
        while frame and (depth == 0 or frame.f_code.co_filename == logging.__file__):
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())

logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)
```

## 환경 변수를 통한 개인화 가능한 기본값 (Personalizable defaults through environment variables)

기본 로거 포맷이 마음에 들지 않나요? `DEBUG` 색상을 다른 것으로 바꾸고 싶으신가요? [문제 없습니다](https://loguru.readthedocs.io/en/stable/api/logger.html#env):

```python
# Linux / OSX
export LOGURU_FORMAT="{time} | <lvl>{message}</lvl>"

# Windows
setx LOGURU_DEBUG_COLOR "<green>"
```

## 편리한 파서 (Convenient parser)

생성된 로그에서 특정 정보를 추출하는 것이 종종 유용합니다. 이를 위해 Loguru는 로그와 정규식을 처리하는 데 도움이 되는 [`parse()`](https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.parse) 메서드를 제공합니다.

```python
pattern = r"(?P<time>.*) - (?P<level>[0-9]+) - (?P<message>.*)"  # 이름 있는 그룹이 있는 정규식
caster_dict = dict(time=dateutil.parser.parse, level=int)        # 일치하는 그룹 변환

for groups in logger.parse("file.log", pattern, cast=caster_dict):
    print("Parsed:", groups)
    # {"level": 30, "message": "Log example", "time": datetime(2018, 12, 09, 11, 23, 55)}
```

## 종합적인 알림기 (Exhaustive notifier)

Loguru는 훌륭한 [`notifiers`](https://github.com/notifiers/notifiers) 라이브러리(별도로 설치해야 함)와 쉽게 결합하여 프로그램이 예기치 않게 실패할 때 이메일을 받거나 다양한 종류의 알림을 보낼 수 있습니다.

```python
import notifiers

params = {
    "username": "you@gmail.com",
    "password": "abc123",
    "to": "dest@gmail.com"
}

# 단일 알림 보내기
notifier = notifiers.get_notifier("gmail")
notifier.notify(message="The application is running!", **params)

# 각 오류 메시지에 대해 알림 받기
from notifiers.logging import NotificationHandler

handler = NotificationHandler("gmail", defaults=params)
logger.add(handler, level="ERROR")
```

> 대부분의 경우 로깅이 성능에 미치는 영향은 무시할 만하지만, 제로 비용 로거를 사용하면 큰 걱정 없이 어디서나 사용할 수 있습니다. 향후 릴리스에서는 Loguru의 중요 기능들이 최대 속도를 위해 C로 구현될 예정입니다.


---

## 참조

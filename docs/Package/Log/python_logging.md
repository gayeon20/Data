---
title: "[Python] 로깅 (Logging)"
excerpt: Python의 Logging 라이브러리에 대한 문서
categories:
  - Python
tags:
  - Python
  - Python-Library
  - Log
  - Python-logging
last_modified_at: 2024-04-11T15:11:34+09:00
link: https://docs.python.org/3/library/logging.html
상위 항목: "[[python_library|파이썬 라이브러리 (Python Library)]]"
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

**하위 항목**
- [[python_loguru|로구루 (Loguru)]]: 성능을 중시하는 로깅 라이브러리
- [[python_rich|리치 (Rich)]]: 자세한 정보 출력을 중시하는 로깅 라이브러리

---

```python
import logging
```

- `print()` 를 사용할 경우 상황에 따라 주석으로 변환하거나 새롭게 작성하는 등 유지보수에 큰 어려움을 겪을 수 있다. 쉽게 로그를 남기기 위한 모듈

## 1. 객체

### 1) Logger

```python
logger = logging.getLogger('__name__')

# 예시 (결과: ERROR:root:somthing wrong!!)
logger = logging.getLogger()
logging.error("something wrong!!")
```

- 소스 코드에서 바로 호출하여 사용할 수 있는 인터페이스를 제공한다. 로그 메시지 기록, 레벨 관리, 출력 위치 설정, 포맷 설정, 파일 분할, 레벨 필터링의 역할을 수행한다.
- 일반적으로 파이썬 모듈 단위로 로거를 생성하며 최상단의 root 로거 밑으로 부모 자식 관계를 형성한다. 모듈마다 개별적으로 로거를 생성하여 개별적으로 로그 레벨, 포맷을 지정하고 선택적 활성화 및 로그를 분리하여 관리할 수 있다.
- `getLogger` 에서 지정한 로그 이름은 다른 모듈에서도 불러와서 사용할 수 있다. 어떤 문자열을 입력해도 상관 없지만 모듈 단위 (`__name__`) 의 로거를 생성하여 사용하는 것을 권장한다.
- 기본값은 root logger 로 모든 logger 의 부모 형태가 된다. Root logger 의 기본 레벨은 WARNING 이다.

### 2) Handler

- Logger 에 의해 생성된 LogRecord 를 적절한 곳에 출력한다. 콘솔이나 파일, 데이터베이스 등에 저장할 수 있다.
- Logger 는 여러 Handler 를 보유할 수 있고, Handler 는 반드시 특정 Logger 객체에 귀속된다.
- handler 를 logger 에 추가하여 로그 위치를 관리한다.
- `StreamHandler` 는 출력 위치 설정으로 기본값은 콘솔 창이다. 파일, DB, Socket, Queue 등을 통해 출력할 수 있다.
- `FileHandler` 는 로그 파일 설정이다. `-a` 모드가 기본값이다.
- 여러 개의 파일 handler 를 만들면 레벨별 출력도 가능하다.

```python
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# 콘솔 출력 지정
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 파일 출력 지정
file_handler = logging.FileHandler(filename="run.log")
file_handler.setLevel(logging.INFO)

# add handler to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
```

- 하나의 파일에 로그를 저장하는 것을 권장하지만 따로 저장을 원할 경우 root logger 에서 handler 연결을 삭제하고 새로운 파일을 연결하면 된다.

```python
log = logging.getLogger()

for hdlr in log.handlers[:]:
    log.removeHandler(hdlr)

file_log = logging.FileHandler("log2.log")
file_log.setLevel(logging.INFO)

logging.basicConfig(handlers=[file_log])
logging.error("log2에러")
```

### 3) Formatter

```python
import logging

handler = logging.StreamHandler()
formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
handler.setFormatter(formatter)
```

- 로그의 출력 포맷을 결정한다. `'%(asctime)s - %(name)s - %(levelname)s - %(message)s'` 와 같은 형태로 작성한다.
- `%` 는 LogRecord 의 속성을 호출할 때 사용한다.

### 4) LogRecord

- 로그 한 줄을 생성할 때마다 메시지와 로거의 이름, 로그 레벨, 발생 시킨 소스 코드 위치 등의 정보를 저장한다.
- 다른 객체들에 전달되어 각자의 역할을 수행하게 한다.

## 2. 로그 단계

- 단계에 해당하는 함수를 호출하여 사용한다.

| 단계         | 설명                                                                                                 |
| ------------ |:---------------------------------------------------------------------------------------------------- |
| NOTSET(0)    | 로거가 루트 로거 일 때는 모든 메시지를 처리하게 하고, 루트 로거가 아니면 모든 메시지를 부모에게 위임 |
| DEBUG(10)    | 간단히 문제를 진단하고 싶을 때 필요한 자세한 정보를 기록함                                           |
| INFO(20)     | 계획대로 작동하고 있음을 알리는 확인 메시지                                                          |
| WARNING(30)  | 소프트웨어가 작동은 하고 있지만, 예상치 못한 일이 발생했거나 할 것으로 예측된다는 것을 알림          |
| ERROR(40)    | 중대한 문제로 인해 소프트웨어가 몇몇 기능들을 수행하지 못함을 알림                                   |
| CRITICAL(50) | 작동이 불가능한 수준의 심각한 에러가 발생함을 알림 (=FATAL)                                           |

```python
# WARNING 생성
logging.warn("message")
```

- log level 을 custom 하여 작성할 수도 있다.

```python
# 단계 추가
logging.addLevelName(15, "DATA")

# logger에 단계 변수 저장
logging.DATA = 15

# log 생성
logger.log(logging.DATA, "message")
```

### 1) 로그 조회

- `setLevel` 함수로 레벨을 설정하면 해당 레벨 이상의 로그만 조회할 수 있다. 기본은 `WARN` 으로 지정된다.

```python
# INFO 레벨 이상 로그 확인
logger.setLevel(logging.INFO)
```

## 3. Formatter

| 속성         | format         | 설명                               |
|:--------- |:------------- |:------------------------------- |
| asctime    | %(asctime)s    | 인간이 읽을 수 있는 시간 표시                |
| created    | %(created)f    | logRecord 가 만들어진 시간               |
| filename   | %(filename)s   | pathname 의 file 이름 부분             |
| funcName   | %(funcName)s   | logging call 을 포함하는 function 의 이름  |
| levelname  | %(levelname)s  | 메시지의 Text logging level: 예) INFO |
| lineno     | %(lineno)d     | logging call 이 발생한 코드의 line 숫자    |
| module     | %(module)s     | filename 의 모듈 이름 부분               |
| message    | %(message)s    | 메시지                              |
| name       | %(name)s       | logger 의 이름                       |
| pathname   | %(pathname)s   | full pathname                    |
| thread     | %(thread)d     | thread ID                        |
| threadName | %(threadName)s | thread 이름                        |

```python
logging.basicConfig(
    filename= , level = logging.INFO,
    datefmt = '%Y-%m-%d %H%M%S',
    format = '%(asctime)s | %(levelname)s | $(message)s'
)

```

- 실행 시작 시간, 소요 시간 등을 확인하기 위해 시간을 추가할 수 있다.
- `datefmt` 로 시간 포맷을 정한 뒤에 format 에 출력 메시지 레이아웃
을 정하면 됩니다. `asctime` 부분에 앞에서 정의한 시간이 출력됩니다.

```python
# formatter 생성
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# formatter 생성 2
formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] >> %(message)s')

# handler 생성 (stream, file)
streamHandler = logging.StreamHandler()

# logger instance에 fomatter 설정
str
eamHandler.setFormatter(formatter)
```

- `Formatter` 를 생성할 경우 위처럼 적용할 수 있다.

```python
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-8s - %(message)s')
```

- 옵션에 `-8` 과 같이 숫자를 붙이면 해당 옵션의 출력 글자 수를 고정할 수 있다.

## 4. Config 설정

### 1) Python 에서 적용

- `basicConfig` 함수를 이용한다. 파일로 로그를 저장하면 콘솔에서는 로그가 보이지 않는다.
- 최초 입력한 설정만 유지되고 다른 모듈에서 사용한 것은 적용되지 않는다.

```python
# 파일 이름 지정
logging.basicConfig(
    filename='example.log',
    level=logging.DEBUG
)
```

- `propagate` 는 로그 레코드 (로그 메시지) 가 부모 로거 (parent logger) 로 전파되는지 여부를 결정한다. 기본값은 True 이며 이 경우 로그가 부모와 자식 모두 작성된다.

```python
myLogger = logging.getLogger("my")
myLogger.propagate = False
```

### 2) Config 작성

- Python 에서 자체적으로 제공하는 파일 설정을 활용하여 적용할 수 있다. 아래처럼 `.conf` 파일을 작성할 수 있다.

#### (1) 전체 항목 나열

```conf
[loggers]
keys=root,infoLogger

[handlers]
keys=simpleHandler

[formatters]
keys=simpleFormatter
```

- 로거, 핸들러, 포매터의 이름을 설정하는 초기화 장소이다.
- 대괄호 기호, keys 등의 용어는 약속된 양식이므로 반드시 준수해야 한다.
- root 는 모든 로거의 부모이므로 반드시 기술해야 한다.
- 핸들러와 포매터의 이름은 자유롭게 설정할 수 있다. 단, 아래의 항목들에서 그에 맞게 작성해야 한다.

#### (2) 로거 설정

```conf
[logger_root]
level=NOTSET
handlers=

[logger_infoLogger]
level=INFO
handlers=simpleHandler
qualname=__main__
propagate=1
```

- 모든 로거가 같은 핸들러를 사용하는 것이 아니라면 root 로거에 핸들러를 설정하는 것은 권장하지 않는다. 설정에 따라 로거들의 레코드가 root 에 전달되면서 핸들러에 의해 다시 출력될 수 있다.
- 아래는 자체 로거들이다. `logger_` 뒤에 위에서 설정했던 로거명을 붙인 형태이다.
- `qualname` 은 프로그램 내 유일한 이름을 뜻하며 대부분 모듈이나 패키지명이 들어간다. (ex)`org.pythong.docs.logging`)
- `propagate` 는 전파 유무로 부모에게 전달할지 결정한다. `1` 일 때 전달된다.

#### (3) 핸들러 설정

```conf
[handler_simpleHandler]
class=StreamHandler
formatter=simpleFormatter
args=(sys.stdout,)
```

- `handler_` 뒤에 handler 명을 붙인 형태이다.
- `class` 는 어떤 타입의 핸들러를 설정할지 결정한다. `StreamHandler` 등에 해당한다.
- `args` 는 Handler 생성 시 생성자에 전달할 인자 값 리스트를 Tuple 형태로 입력하는 장소이다. 출력 시 시스템 표준 출력문을 통해 출력한다는 의미로 `sys.stdout` 을 입력할 수 있다.

```conf
[handler_fileHandler]
class=FileHandler
formatter=simpleFormatter
args=('python.log', 'w')
```

- `FileHandler` 를 사용할 경우 위처럼 작성할 수 있다.
- `python.log` 는 파일명을 나타내며 `w` 는 쓰기 권한을 의미한다.

#### (4) 포매터 설정

```conf
[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)-8s - %(message)s
datefmt=
```

- `formatter_` 뒤에 formatter 명을 붙인 형태이다.
- `datefmt=` 는 날짜의 출력 포맷을 설정한다. 비워두면 `YYYY-MM-DD HH:MM:SS,millsecond.` 의 형태로 설정된다.

#### (5) 파일 적용 [(공식 문서)](https://docs.python.org/3/library/logging.config.html)

```python
import logging
import logging.config

logging.config.fileConfig('<file name>.conf')
logger = logging.getLogger(__name__)
```

> [!NOTE] Dictionary 형태로 적용
>
> ```python
> import logging.config
> 
> log_config = {
> 'version': 1,
> 'formatters': {
> 'standard': {
> 'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
> },
> },
> 'handlers': {
> 'file_handler': {
> 'class': 'logging.FileHandler',
> 'filename': 'my_log_file.log',
> 'level': 'DEBUG',
> 'formatter': 'standard',
> },
> },
> 'root': {
> 'level': 'DEBUG',
> 'handlers': ['file_handler'],
> },
> }
> 
> logging.config.dictConfig(log_config)
> ```
>
> - Dictionary 형태로 설정을 받아서 구성으로 적용할 수 있다.

### 3) 모듈 Log 설정

```python
logging.getLogger('deepl').setLevel(logging.DEBUG)
```

- `getLogger` 에 모듈명을 입력하면 해당 모듈의 로그 단계를 설정할 수 있습니다.

## 5. Trackback 출력
```python
except Exception as e:
    logging.error(e, exc_info=True)
```


- `logger.exception` 메서드를 사용하면 현재 예외의 스택 트레이스를 자동으로 로그에 추가할 수 있습니다.


## 성능 테스트

```python
import logging
import time

def setup_logger(level):
    logger = logging.getLogger('performance_test')
    logger.setLevel(level)
    handler = logging.NullHandler()
    logger.addHandler(handler)
    return logger

def test_logging_performance(logger, iterations=1000000):
    start_time = time.time()
    for _ in range(iterations):
        logger.info("This is a test log message")
    end_time = time.time()
    return end_time - start_time

# INFO 레벨 테스트
info_logger = setup_logger(logging.INFO)
info_time = test_logging_performance(info_logger)
print(f"INFO 레벨에서 100만번 로깅 시간: {info_time:f} 초")

# WARNING 레벨 테스트
warning_logger = setup_logger(logging.WARNING)
warning_time = test_logging_performance(warning_logger)
print(f"WARNING 레벨에서 100만번 로깅 시간: {warning_time:f} 초")

# 차이 계산
time_difference = info_time - warning_time
print(f"시간 차이: {time_difference:f} 초")
print(f"WARNING 레벨이 INFO 레벨보다 {time_difference / info_time * 100:f}% 더 빠름")
```

```
INFO 레벨에서 100만번 로깅 시간: 22.2013 초
WARNING 레벨에서 100만번 로깅 시간: 0.8069 초
시간 차이: 21.3944 초
WARNING 레벨이 INFO 레벨보다 96.37% 더 빠름
```
- 필요한 로그만, 적절한 단계로 조절하기

---

## 예시

### logging

```python
import logging

# 로그 생성
logger = logging.getLogger()

# 로그의 출력 기준 설정
logger.setLevel(logging.INFO)

#log 출력 형식
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(messages)s")

# log를 console에 출력
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

#log를 파일에 출력
file_handler = logging.FileHandler("my.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

for i in range(10):
	logger.info(f"{i}번째 방문입니다.")
```

## 참조
[The 5 Best Logging Libraries for Python (highlight.io)](https://www.highlight.io/blog/5-best-python-logging-libraries)
[파이썬 로깅 멋지게 하기 (velog.io)](https://velog.io/@otzslayer/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A1%9C%EA%B9%85-%EB%A9%8B%EC%A7%80%EA%B2%8C-%ED%95%98%EA%B8%B0)
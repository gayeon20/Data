---
title: "[Python] 리치 (Rich)"
excerpt: 
categories:
  - Python
tags:
  - Python
  - Python-Library
  - Log
  - Python-rich
last_modified_at: 2024-04-11T15:11:34+09:00
link: https://rich.readthedocs.io/en/latest/
상위 항목: "[[python_library|파이썬 라이브러리 (Python Library)]]"
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

> **Github**: [Textualize/rich: Rich is a Python library for rich text and beautiful formatting in the terminal. (github.com)](https://github.com/Textualize/rich)

---
![Logo](https://github.com/textualize/rich/raw/master/imgs/logo.svg)

Rich는 터미널에서 _풍부한(rich)_ 텍스트와 아름다운 서식을 지원하기 위한 파이썬 라이브러리입니다.

[Rich API](https://rich.readthedocs.io/en/latest/)는 터미널 출력에 색깔과 스타일을 입히기 쉽게 도와줍니다. 또한 Rich는 별다른 설정 없이 표, 진행 바, 마크다운, 소스코드 구문 강조, tracebacks 등을 예쁘게 보여줄 수 있습니다.

![Features](https://github.com/textualize/rich/raw/master/imgs/features.png)

Rich에 대한 동영상 설명을 보시려면 [@fishnets88](https://twitter.com/fishnets88)의 [calmcode.io](https://calmcode.io/rich/introduction.html)를 확인 바랍니다.

[사람들의 Rich에 대한 의견](https://www.willmcgugan.com/blog/pages/post/rich-tweets/)을 확인해보세요.

## 호환성

Rich는 리눅스, OSX, 윈도우에서 동작합니다. 트루 컬러 / 이모지는 새로운 윈도우 터미널에서 동작하지만 구형 터미널에서는 16가지 색으로 제한됩니다. Rich는 파이썬 3.6.3 버전 혹은 그 이후 버전이 필요합니다.

Rich는 [Jupyter notebooks](https://jupyter.org/)에서 별도의 설정없이 바로 동작합니다.

## 설치

`pip` 또는 좋아하는 PyPI 패키지 매니저로 설치하세요.

```sh
python -m pip install rich
```

아래 명령어를 통해 터미널에서 Rich 출력을 테스트해보세요.

```sh
python -m rich
```

## Rich Print

간단하게 당신의 어플리케이션에 rich한 출력을 추가하려면, 파이썬 내장 함수와 signature가 같은 [rich print](https://rich.readthedocs.io/en/latest/introduction.html#quick-start) 메서드를 import 할 수 있습니다.
따라해보세요:

```python
from rich import print

print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())
```

![Hello World](https://github.com/textualize/rich/raw/master/imgs/print.png)

## Rich REPL

Rich는 파이썬 REPL에도 설치할 수 있습니다. 어떤 데이터 구조라도 예쁘게 출력하거나 강조할 수 있습니다.

```python
>>> from rich import pretty
>>> pretty.install()
```

![REPL](https://github.com/textualize/rich/raw/master/imgs/repl.png)

## 콘솔 사용하기

rich 터미널을 더욱 잘 활용하려면, import 한 뒤 [Console](https://rich.readthedocs.io/en/latest/reference/console.html#rich.console.Console) 객체를 생성해주세요.

```python
from rich.console import Console

console = Console()
```

콘솔 객체에는 `print` 메서드가 있는데, 내부적으로 내장 `print` 함수와 유사한 인터페이스를 가지고 있습니다. 아래는 예제입니다:

```python
console.print("Hello", "World!")
```

예상대로 `"Hello World!"`이 터미널에 출력될 것입니다. 내장 `print` 함수와 달리, Rich는 터미널 폭에 맞춰 자동 줄바꿈(word-wrap)을 적용하는 것에 유의하세요.

출력에 색깔과 스타일을 입히는 방법은 몇가지가 있습니다. `style` 키워드 전달인자를 추가해 전체 출력에 대해 스타일을 변경할 수 있습니다. 예제는 다음과 같습니다:

```python
console.print("Hello", "World!", style="bold red")
```

다음과 같이 출력됩니다:

![Hello World](https://github.com/textualize/rich/raw/master/imgs/hello_world.png)

텍스트 한 줄을 한 번에 수정하는 것도 좋습니다. 더욱 세세하게 스타일을 변경하기 위해, Rich는 [bbcode](https://en.wikipedia.org/wiki/BBCode)와 구문이 비슷한 별도의 마크업을 렌더링 할 수 있습니다. 예제는 다음과 같습니다.

```python
console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")
```

![Console Markup](https://github.com/textualize/rich/raw/master/imgs/where_there_is_a_will.png)

Console 객체를 활용해 적은 노력으로 복잡한 출력을 손쉽게 만들 수 있습니다. 자세한 내용은 [Console API](https://rich.readthedocs.io/en/latest/console.html) 문서를 확인해주세요.

## Rich Inspect

Rich는 class나 instance, builtin 같은 파이썬 객체의 레포트를 생성하는 [inspect](https://rich.readthedocs.io/en/latest/reference/init.html?highlight=inspect#rich.inspect) 함수를 포함합니다

```python
>>> my_list = ["foo", "bar"]
>>> from rich import inspect
>>> inspect(my_list, methods=True)
```

![Log](https://github.com/textualize/rich/raw/master/imgs/inspect.png)

자세한 내용은 [inspect docs](https://rich.readthedocs.io/en/latest/reference/init.html#rich.inspect) 문서를 확인해주세요.

## Rich Library
> 모든 Rich로 표현 가능한 것들은 [Console Protocol](https://rich.readthedocs.io/en/latest/protocol.html)를 사용합니다. 이것을 사용해서 자신의 Rich 컨텐츠를 렌더링할 수도 있습니다.


Rich는 CLI에서 우아하게 출력하거나 코드 디버깅을 돕도록 다양한 빌트인 _렌더링을_ 포함하고 있습니다.

자세한 내용을 확인하려면 제목을 눌러주세요:


### Log
Console 객체는 `print()`와 인터페이스가 유사한 `log()` 메서드를 가지고 있습니다. `Log()`는 호출이 이루어진 파일과 라인, 현재 시간도 같이 출력합니다. 기본적으로 Rich는 파이썬 구조체와 repr string에 대해 신택스 하이라이팅을 지원합니다. 만약 당신이 collection(예를 들어 dict나 list)을 로깅한다면, Rich는 표현 가능한 공간에 맞춰 예쁘게 출력해줍니다. 이러한 기능들에 대한 예시입니다:

```python
from rich.console import Console
console = Console()

test_data = [
    {"jsonrpc": "2.0", "method": "sum", "params": [None, 1, 2, 4, False, True], "id": "1",},
    {"jsonrpc": "2.0", "method": "notify_hello", "params": [7]},
    {"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": "2"},
]

def test_log():
    enabled = False
    context = {
        "foo": "bar",
    }
    movies = ["Deadpool", "Rise of the Skywalker"]
    console.log("Hello from", console, "!")
    console.log(test_data, log_locals=True)

test_log()
```

위 코드의 실행 결과는 다음과 같습니다:

[![Log](https://github.com/textualize/rich/raw/master/imgs/log.png)](https://github.com/textualize/rich/raw/master/imgs/log.png)

`log_locals` 인자를 사용하면 log 메서드가 호출된 곳의 로컬 변수들을 표로 보여준다는 것도 알아두세요.

로그 메서드는 서버처럼 오랫동안 실행되는 어플리케이션을 터미널로 로깅할때 사용할 수 있지만 디버깅 할 때도 매우 좋습니다.


### Logging Handler
또한 내장된 [Handler class](https://rich.readthedocs.io/en/latest/logging.html)를 사용해 파이썬의 로깅 모듈의 출력을 형태를 꾸미거나 색을 입힐 수 있습니다. 다음은 예제입니다:

[![Logging](https://github.com/textualize/rich/raw/master/imgs/logging.png)](https://github.com/textualize/rich/raw/master/imgs/logging.png)

Rich는 Python의 logging 모듈이 작성한 텍스트를 형식화하고 색상을 입힐 [로깅 핸들러](https://rich.readthedocs.io/en/latest/reference/logging.html#logging)를 제공합니다.

다음은 Rich 로거를 설정하는 방법의 예시입니다:

```python
import logging
from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")
log.info("Hello, World!")
```

Rich 로그는 기본적으로 로깅에서 [콘솔 마크업](https://rich.readthedocs.io/en/latest/markup.html#console-markup)을 렌더링하지 않습니다. 대부분의 라이브러리는 리터럴 대괄호를 이스케이프해야 할 필요성을 인식하지 못하기 때문입니다. 하지만 핸들러에서 `markup=True`를 설정하여 활성화할 수 있습니다. 또는 다음과 같이 `extra` 인수를 제공하여 로그 메시지별로 활성화할 수 있습니다:

```python
log.error("[bold red blink]Server is shutting down![/]", extra={"markup": True})
```

마찬가지로 하이라이터는 로그 메시지별로 재정의될 수 있습니다:

```python
log.error("123 will not be highlighted", extra={"highlighter": None})
```

#### 예외 처리 (Handle exceptions)

[`RichHandler`](https://rich.readthedocs.io/en/latest/reference/logging.html#rich.logging.RichHandler "rich.logging.RichHandler") 클래스는 Rich의 [`Traceback`](https://rich.readthedocs.io/en/latest/reference/traceback.html#rich.traceback.Traceback "rich.traceback.Traceback") 클래스를 사용하여 예외를 형식화하도록 구성될 수 있습니다. 이는 내장 예외보다 더 많은 컨텍스트를 제공합니다. 로그에 아름다운 예외를 얻으려면 핸들러 생성자에서 `rich_tracebacks=True`를 설정하세요:

```python
import logging
from rich.logging import RichHandler

logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)

log = logging.getLogger("rich")
try:
    print(1 / 0)
except Exception:
    log.exception("unable print!")
```

로깅 출력을 구성하는 데 사용할 수 있는 다른 옵션들이 있습니다. 자세한 내용은 [`RichHandler`](https://rich.readthedocs.io/en/latest/reference/logging.html#rich.logging.RichHandler "rich.logging.RichHandler") 참조를 확인하세요.

#### 프레임 억제 (Suppressing Frames)

프레임워크(click, django 등)와 작업하는 경우, 트레이스백 내에서 자신의 애플리케이션 코드만 보고 싶을 수 있습니다. Traceback, install, Console.print_exception에서 suppress 인수를 설정하여 프레임워크 코드를 제외할 수 있습니다. 이는 모듈 또는 문자열 경로의 리스트여야 합니다.

다음은 Rich 예외에서 [click](https://click.palletsprojects.com/en/8.0.x/)을 제외하는 방법입니다:

```python
import click
import logging
from rich.logging import RichHandler

logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True, tracebacks_suppress=[click])]
)
```

억제된 프레임은 코드 없이 라인과 파일만 표시합니다.


### 이모지 (Emoji)
콘솔 출력에 이모지를 넣으려면 두 콜론(:) 사이에 이모지 이름을 넣어주세요. 다음은 예제입니다:

```python
>>> console.print(":smiley: :vampire: :pile_of_poo: :thumbs_up: :raccoon:")
😃 🧛 💩 👍 🦝
```

### 표 (Tables)
Rich는 유니코드 박스 문자와 함께 [표](https://rich.readthedocs.io/en/latest/tables.html)를 자유롭게 렌더링할 수 있습니다. 가장자리, 스타일, 셀 정렬 등을 정말 다양하게 구성할 수 있습니다.

[![table movie](https://github.com/textualize/rich/raw/master/imgs/table_movie.gif)](https://github.com/textualize/rich/raw/master/imgs/table_movie.gif)

위의 애니메이션은 example 디렉토리의 [table_movie.py](https://github.com/textualize/rich/blob/master/examples/table_movie.py)로 생성되었습니다.

더 간단한 표 예제입니다:

```python
from rich.console import Console
from rich.table import Table

console = Console()

table = Table(show_header=True, header_style="bold magenta")
table.add_column("Date", style="dim", width=12)
table.add_column("Title")
table.add_column("Production Budget", justify="right")
table.add_column("Box Office", justify="right")
table.add_row(
    "Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$275,000,000", "$375,126,118"
)
table.add_row(
    "May 25, 2018",
    "[red]Solo[/red]: A Star Wars Story",
    "$275,000,000",
    "$393,151,347",
)
table.add_row(
    "Dec 15, 2017",
    "Star Wars Ep. VIII: The Last Jedi",
    "$262,000,000",
    "[bold]$1,332,539,889[/bold]",
)

console.print(table)
```

이는 다음과 같이 출력됩니다:

[![table](https://github.com/textualize/rich/raw/master/imgs/table.png)](https://github.com/textualize/rich/raw/master/imgs/table.png)

콘솔 출력은 `print()`나 `log()`와 같은 방식으로 렌더링 된다는 것을 주의하세요. 사실, Rich로 표현할 수 있는 것은 무엇이든 headers / rows (심지어 다른 표들도)에 포함할 수 있습니다.

`Table` 클래스는 터미널의 폭에 맞춰 필요한 만큼 줄을 내리고 열 길이를 스스로 조절합니다. 위의 표보다 작은 터미널에서 만들어진 표 예시입니다:

[![table2](https://github.com/textualize/rich/raw/master/imgs/table2.png)](https://github.com/textualize/rich/raw/master/imgs/table2.png)

### 진행 바 (Progress Bars)
Rich는 오래 걸리는 작업들을 위해 깜빡임 없는 [진행](https://rich.readthedocs.io/en/latest/progress.html) 바를 여러개 표현할 수 있습니다.

기본적인 사용을 위해선 아무 sequence나 `track` 함수로 감싸고 결과를 반복해주세요. 다음은 예제입니다:

```python
from rich.progress import track

for step in track(range(100)):
    do_step(step)
```

여러개의 진행 바를 추가하는 것도 어렵지 않습니다. 아래는 공식문서에서 따온 예시입니다:

[![progress](https://github.com/textualize/rich/raw/master/imgs/progress.gif)](https://github.com/textualize/rich/raw/master/imgs/progress.gif)

칼럼들은 수정해 원하는 세부정보를 보여줄 수도 있습니다. 기본으로 내장된 칼럼들은 완료 퍼센티지, 파일 크기, 파일 속도, 남은 시간입니다. 다운로드 진행을 보여주는 다른 예제입니다:

[![progress](https://github.com/textualize/rich/raw/master/imgs/downloader.gif)](https://github.com/textualize/rich/raw/master/imgs/downloader.gif)

Rich는 장시간 실행되는 작업/파일 복사 등의 진행 상황에 대한 지속적으로 업데이트되는 정보를 표시할 수 있습니다. 표시되는 정보는 구성 가능하며, 기본값은 '작업'에 대한 설명, 진행 막대, 완료 백분율 및 예상 남은 시간을 표시합니다.

Rich 진행 상황 표시는 각각 막대와 진행 정보가 있는 여러 작업을 지원합니다. 이를 사용하여 작업이 스레드나 프로세스에서 발생하는 동시 작업을 추적할 수 있습니다.

진행 상황 표시가 어떻게 보이는지 확인하려면 명령줄에서 다음을 시도해보세요:

```
python -m rich.progress
```

> Progress는 Jupyter 노트북에서도 작동하지만, 자동 새로 고침이 비활성화됩니다. [`refresh()`](https://rich.readthedocs.io/en/latest/reference/progress.html#rich.progress.Progress.refresh "rich.progress.Progress.refresh")를 명시적으로 호출하거나 [`update()`](https://rich.readthedocs.io/en/latest/reference/progress.html#rich.progress.Progress.update "rich.progress.Progress.update")를 호출할 때 `refresh=True`를 설정해야 합니다. 또는 각 루프에서 자동으로 새로 고침을 수행하는 [`track()`](https://rich.readthedocs.io/en/latest/reference/progress.html#rich.progress.track "rich.progress.track") 함수를 사용하세요.

#### 기본 사용법 (Basic Usage)

기본 사용법의 경우 [`track()`](https://rich.readthedocs.io/en/latest/reference/progress.html#rich.progress.track "rich.progress.track") 함수를 호출하세요. 이 함수는 시퀀스(예: 리스트 또는 range 객체)와 작업 중인 작업에 대한 선택적 설명을 받습니다. track 함수는 시퀀스에서 값을 산출하고 각 반복에서 진행 정보를 업데이트합니다. 다음은 예시입니다:

```python
import time
from rich.progress import track

for i in track(range(20), description="Processing…"):
    time.sleep(1)  # 작업 수행 시뮬레이션
```

#### 고급 사용법 (Advanced usage)

표시에 여러 작업이 필요하거나 진행 상황 표시의 열을 구성하려면 [`Progress`](https://rich.readthedocs.io/en/latest/reference/progress.html#rich.progress.Progress "rich.progress.Progress") 클래스를 직접 사용할 수 있습니다. Progress 객체를 생성한 후 ([`add_task()`](https://rich.readthedocs.io/en/latest/reference/progress.html#rich.progress.Progress.add_task "rich.progress.Progress.add_task"))로 작업을 추가하고 [`update()`](https://rich.readthedocs.io/en/latest/reference/progress.html#rich.progress.Progress.update "rich.progress.Progress.update")로 진행 상황을 업데이트합니다.

Progress 클래스는 진행 상황 표시를 자동으로 시작하고 중지하는 _컨텍스트 관리자_ 로 설계되었습니다.

다음은 간단한 예시입니다:

```python
import time

from rich.progress import Progress

with Progress() as progress:

    task1 = progress.add_task("[red]Downloading…", total=1000)
    task2 = progress.add_task("[green]Processing…", total=1000)
    task3 = progress.add_task("[cyan]Cooking…", total=1000)

    while not progress.finished:
        progress.update(task1, advance=0.5)
        progress.update(task2, advance=0.3)
        progress.update(task3, advance=0.9)
        time.sleep(0.02)
```

작업과 관련된 `total` 값은 진행 상황이 100%에 도달하기 위해 완료해야 하는 단계 수입니다. 이 맥락에서 _단계_ 는 애플리케이션에 맞는 것이면 무엇이든 될 수 있습니다. 읽은 파일의 바이트 수나 처리된 이미지 수 등이 될 수 있습니다.

##### 작업 업데이트 (Updating tasks)

[`add_task()`](https://rich.readthedocs.io/en/latest/reference/progress.html#rich.progress.Progress.add_task "rich.progress.Progress.add_task")를 호출하면 작업 ID를 받습니다. 이 ID를 사용하여 작업을 완료했거나 정보가 변경될 때마다 [`update()`](https://rich.readthedocs.io/en/latest/reference/progress.html#rich.progress.Progress.update "rich.progress.Progress.update")를 호출합니다. 일반적으로 단계를 완료할 때마다 `completed`를 업데이트해야 합니다. `completed`를 직접 업데이트하거나 현재 `completed` 값에 추가하는 `advance`를 설정하여 이를 수행할 수 있습니다.

[`update()`](https://rich.readthedocs.io/en/latest/reference/progress.html#rich.progress.Progress.update "rich.progress.Progress.update") 메서드는 작업과 연관된 키워드 인수도 수집합니다. 이를 사용하여 진행 상황 표시에 렌더링하고 싶은 추가 정보를 제공하세요. 추가 인수는 `task.fields`에 저장되며 [Column 클래스](https://rich.readthedocs.io/en/latest/progress.html#columns)에서 참조될 수 있습니다.

##### 작업 숨기기 (Hiding tasks)

작업의 `visible` 값을 업데이트하여 작업을 표시하거나 숨길 수 있습니다. 작업은 기본적으로 표시되지만, `visible=False`로 [`add_task()`](https://rich.readthedocs.io/en/latest/reference/progress.html#rich.progress.Progress.add_task "rich.progress.Progress.add_task")를 호출하여 보이지 않는 작업을 추가할 수도 있습니다.

##### 일시적 진행 상황 (Transient progress)

일반적으로 진행 상황 컨텍스트 관리자를 종료하면(또는 [`stop()`](https://rich.readthedocs.io/en/latest/reference/progress.html#rich.progress.Progress.stop "rich.progress.Progress.stop")을 호출하면) 마지막으로 새로 고침된 표시가 터미널에 남아 있고 커서는 다음 줄에 있습니다. Progress 생성자에 `transient=True`를 설정하여 종료 시 진행 상황 표시가 사라지도록 할 수도 있습니다. 다음은 예시입니다:

```python
with Progress(transient=True) as progress:
    task = progress.add_task("Working", total=100)
    do_work(task)
```

일시적 진행 상황 표시는 작업이 완료될 때 터미널에 더 최소한의 출력을 원할 때 유용합니다.

##### 불확정 진행 상황 (Indeterminate progress)

작업을 추가하면 자동으로 _시작_ 되어 0%에서 진행 막대를 표시하고 남은 시간은 현재 시간부터 계산됩니다. 진행 상황 업데이트를 시작하기 전에 긴 지연이 있는 경우 이 방식이 잘 작동하지 않을 수 있습니다. 서버의 응답을 기다리거나 디렉토리의 파일을 계산해야 할 수 있습니다(예를 들어). 이러한 경우 `start=False` 또는 `total=None`으로 [`add_task()`](https://rich.readthedocs.io/en/latest/reference/progress.html#rich.progress.Progress.add_task "rich.progress.Progress.add_task")를 호출하여 작업 중임을 사용자에게 알리는 맥동 애니메이션을 표시할 수 있습니다. 이를 _불확정_ 진행 막대라고 합니다. 단계 수를 알게 되면 [`start_task()`](https://rich.readthedocs.io/en/latest/reference/progress.html#rich.progress.Progress.start_task "rich.progress.Progress.start_task")를 호출하여 0%에서 진행 막대를 표시한 다음 평소와 같이 [`update()`](https://rich.readthedocs.io/en/latest/reference/progress.html#rich.progress.Progress.update "rich.progress.Progress.update")를 호출합니다.

##### 자동 새로 고침 (Auto refresh)

기본적으로 진행 정보는 초당 10번 새로 고쳐집니다. [`Progress`](https://rich.readthedocs.io/en/latest/reference/progress.html#rich.progress.Progress "rich.progress.Progress") 생성자의 `refresh_per_second` 인수로 새로 고침 속도를 설정할 수 있습니다. 업데이트가 그렇게 자주 이루어지지 않을 것을 알고 있다면 이를 10보다 낮은 값으로 설정해야 합니다.

업데이트가 매우 빈번하지 않은 경우 생성자에 `auto_refresh=False`를 설정하여 자동 새로 고침을 완전히 비활성화할 수 있습니다. 자동 새로 고침을 비활성화하면 작업을 업데이트한 후 수동으로 [`refresh()`](https://rich.readthedocs.io/en/latest/reference/progress.html#rich.progress.Progress.refresh "rich.progress.Progress.refresh")를 호출해야 합니다.

##### 확장 (Expand)

진행 막대는 작업 정보를 표시하는 데 필요한 터미널 너비만큼만 사용합니다. Progress 생성자에 `expand` 인수를 설정하면 Rich가 진행 상황 표시를 사용 가능한 전체 너비로 늘립니다.

다음은 요청하신 대로 번역한 내용입니다:

##### 열 (Columns)

`Progress` 생성자의 위치 인자를 사용하여 진행 상황 표시의 열을 사용자 정의할 수 있습니다. 열은 [형식 문자열](https://docs.python.org/3/library/string.html#formatspec) 또는 `ProgressColumn` 객체로 지정됩니다.

형식 문자열은 `Task` 인스턴스인 단일 값 "task"로 렌더링됩니다. 예를 들어 `"{task.description}"`은 열에 작업 설명을 표시하고, `"{task.completed} of {task.total}"`은 총 단계 중 몇 개가 완료되었는지 표시합니다. ~rich.progress.Progress.update에 키워드 인자로 전달된 추가 필드는 `task.fields`에 저장됩니다. 다음 구문을 사용하여 형식 문자열에 추가할 수 있습니다: `"extra info: {task.fields[extra]}"`

기본 열은 다음과 동일합니다:

```python
progress = Progress(
    TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    TaskProgressColumn(),
    TimeRemainingColumn(),
)
```

기본값 외에 자신만의 열을 포함하는 Progress를 만들려면 `get_default_columns()`를 사용하세요:

```python
progress = Progress(
    SpinnerColumn(),
    *Progress.get_default_columns(),
    TimeElapsedColumn(),
)
```

다음 열 객체를 사용할 수 있습니다:

- `BarColumn` 바를 표시합니다.
- `TextColumn` 텍스트를 표시합니다.
- `TimeElapsedColumn` 경과 시간을 표시합니다.
- `TimeRemainingColumn` 예상 남은 시간을 표시합니다.
- `MofNCompleteColumn` 완료 진행 상황을 `"{task.completed}/{task.total}"` 형식으로 표시합니다(completed와 total이 정수일 때 가장 잘 작동합니다).
- `FileSizeColumn` 파일 크기로 진행 상황을 표시합니다(단계가 바이트라고 가정).
- `TotalFileSizeColumn` 총 파일 크기를 표시합니다(단계가 바이트라고 가정).
- `DownloadColumn` 다운로드 진행 상황을 표시합니다(단계가 바이트라고 가정).
- `TransferSpeedColumn` 전송 속도를 표시합니다(단계가 바이트라고 가정).
- `SpinnerColumn` "스피너" 애니메이션을 표시합니다.
- `RenderableColumn` 열에 임의의 Rich 렌더링 가능한 객체를 표시합니다.

자신만의 열을 구현하려면 `ProgressColumn` 클래스를 확장하고 다른 열과 같이 사용하세요.

##### 테이블 열 (Table Columns)

Rich는 Progress 인스턴스의 작업을 위한 `Table`을 생성합니다. Column 생성자에서 `table_column` 인수를 지정하여 이 _작업 테이블_의 열이 생성되는 방식을 사용자 정의할 수 있으며, 이는 `Column` 인스턴스여야 합니다.

다음 예제는 설명이 터미널 너비의 1/3을 차지하고 바가 나머지 2/3을 차지하는 진행 막대를 보여줍니다:

```python
from time import sleep

from rich.table import Column
from rich.progress import Progress, BarColumn, TextColumn

text_column = TextColumn("{task.description}", table_column=Column(ratio=1))
bar_column = BarColumn(bar_width=None, table_column=Column(ratio=2))
progress = Progress(text_column, bar_column, expand=True)

with progress:
    for n in progress.track(range(100)):
        progress.print(n)
        sleep(0.1)
```

##### 출력 / 로그 (Print / log)

Progress 클래스는 `progress.console`을 통해 액세스할 수 있는 내부 Console 객체를 생성합니다. 이 콘솔에 출력하거나 로그를 기록하면 진행 상황 표시 _위에_ 출력이 표시됩니다. 다음은 예시입니다:

```python
with Progress() as progress:
    task = progress.add_task("twiddling thumbs", total=10)
    for job in range(10):
        progress.console.print(f"Working on job #{job}")
        run_job(job)
        progress.advance(task)
```

사용하고 싶은 다른 Console 객체가 있다면 `Progress` 생성자에 전달하세요. 다음은 예시입니다:

```python
from my_project import my_console

with Progress(console=my_console) as progress:
    my_console.print("[bold blue]Starting work!")
    do_work(progress)
```

##### stdout / stderr 리디렉션 (Redirecting stdout / stderr)

진행 상황 표시 시각화가 깨지는 것을 방지하기 위해 Rich는 기본 제공 `print` 문을 사용할 수 있도록 `stdout`과 `stderr`을 리디렉션합니다. 이 기능은 기본적으로 활성화되어 있지만 `redirect_stdout` 또는 `redirect_stderr`를 `False`로 설정하여 비활성화할 수 있습니다.

##### 사용자 정의 (Customizing)

`Progress` 클래스가 진행 상황 표시에 대해 정확히 필요한 것을 제공하지 않는 경우, `get_renderables` 메서드를 오버라이드할 수 있습니다. 예를 들어, 다음 클래스는 진행 상황 표시 주위에 `Panel`을 렌더링합니다:

```python
from rich.panel import Panel
from rich.progress import Progress

class MyProgress(Progress):
    def get_renderables(self):
        yield Panel(self.make_tasks_table(self.tasks))
```

##### 파일에서 읽기 (Reading from a file)

Rich는 파일을 읽는 동안 진행 막대를 생성하는 쉬운 방법을 제공합니다. `open()`을 호출하면 읽는 동안 진행 막대를 표시하는 컨텍스트 관리자를 반환합니다. 이는 읽기를 수행하는 코드를 쉽게 수정할 수 없을 때 특히 유용합니다.

다음 예제는 JSON 파일을 읽을 때 진행 상황을 표시하는 방법을 보여줍니다:

```python
import json
import rich.progress

with rich.progress.open("data.json", "rb") as file:
    data = json.load(file)
print(data)
```

이미 파일 객체가 있다면 `wrap_file()`을 호출할 수 있습니다. 이 함수는 진행 막대를 표시하는 파일을 래핑하는 컨텍스트 관리자를 반환합니다. 이 함수를 사용할 때는 읽을 것으로 예상되는 바이트 또는 문자 수를 설정해야 합니다.

다음은 인터넷에서 URL을 읽는 예제입니다:

```python
from time import sleep
from urllib.request import urlopen

from rich.progress import wrap_file

response = urlopen("https://www.textualize.io")
size = int(response.headers["Content-Length"])

with wrap_file(response, size) as file:
    for line in file:
        print(line.decode("utf-8"), end="")
        sleep(0.1)
```

여러 파일을 읽을 것으로 예상되는 경우, 기존 Progress 인스턴스에 파일 진행 상황을 추가하기 위해 `open()` 또는 `wrap_file()`을 사용할 수 있습니다.

파일이 복사될 때 진행 막대를 보여주는 `cp` 명령어의 최소한의 클론인 cp_progress.py <https://github.com/willmcgugan/rich/blob/master/examples/cp_progress.py>를 참조하세요.

#### 다중 Progress (Multiple Progress)

단일 Progress 인스턴스로는 작업별로 다른 열을 가질 수 없습니다. 그러나 [Live Display](https://rich.readthedocs.io/en/latest/live.html#live)에서 원하는 만큼 많은 Progress 인스턴스를 가질 수 있습니다. 여러 Progress 인스턴스를 사용하는 예제는 [live_progress.py](https://github.com/willmcgugan/rich/blob/master/examples/live_progress.py)와 [dynamic_progress.py](https://github.com/willmcgugan/rich/blob/master/examples/dynamic_progress.py)를 참조하세요.

#### 예제 (Example)

진행 상황 표시의 현실적인 응용을 보려면 [downloader.py](https://github.com/willmcgugan/rich/blob/master/examples/downloader.py)를 참조하세요. 이 스크립트는 진행 막대, 전송 속도 및 파일 크기와 함께 여러 파일을 동시에 다운로드할 수 있습니다.


### 상태 (Status)
진행 상황을 계산하기 어려운 경우, [상태](https://rich.readthedocs.io/en/latest/reference/console.html#rich.console.Console.status) 메서드를 사용할 수 있습니다. 이 메서드는 '스피너' 애니메이션과 메세지를 표시합니다. 애니메이션은 당신이 콘솔을 정상적으로 사용하는 것을 막지 못합니다. 다음은 예제입니다:

```python
from time import sleep
from rich.console import Console

console = Console()
tasks = [f"task {n}" for n in range(1, 11)]

with console.status("[bold green]Working on tasks…") as status:
    while tasks:
        task = tasks.pop(0)
        sleep(1)
        console.log(f"{task} complete")
```

이 예제는 터미널에 아래와 같이 출력합니다.

[![status](https://github.com/textualize/rich/raw/master/imgs/status.gif)](https://github.com/textualize/rich/raw/master/imgs/status.gif)

스피너 애니메이션은 [cli-spinners](https://www.npmjs.com/package/cli-spinners)에서 빌려왔습니다. `spinner` 파라미터를 선택해서 특정 스피너를 선택할 수도 있습니다. 어떤 값을 선택할 수 있는지는 아래 명령어를 통해 확인할 수 있습니다:

```
python -m rich.spinner
```

위의 명령어를 입력하면 아래와 같은 출력됩니다:

[![spinners](https://github.com/textualize/rich/raw/master/imgs/spinners.gif)](https://github.com/textualize/rich/raw/master/imgs/spinners.gif)


### 트리 (Tree)
Rich는 가이드라인과 함께 [트리](https://rich.readthedocs.io/en/latest/tree.html)를 표현할 수 있습니다. 파일 구조나, 계층적 데이터를 보여주는데 적합합니다.

트리의 라벨은 간단한 텍스트나 Rich로 표현할 수 있는 것은 모든지 가능합니다. 아래의 예시를 따라해보세요:

```
python -m rich.tree
```

이는 아래와 같이 출력됩니다:

[![markdown](https://github.com/textualize/rich/raw/master/imgs/tree.png)](https://github.com/textualize/rich/raw/master/imgs/tree.png)

리눅스의 `tree` 명령어처럼 아무 디렉토리의 트리를 보여주는 스크립트 예제를 보시려면 [tree.py](https://github.com/textualize/rich/blob/master/examples/tree.py)를 확인해주세요.


### 칼럼 (Columns)
Rich는 내용을 같거나 적절한 폭으로 깔끔하게 [칼럼](https://rich.readthedocs.io/en/latest/columns.html)을 표현할 수 있습니다. 아래 예제는 종렬로 디렉토리 리스트를 보여주는 (MacOS / Linux)의 `ls` 명령어의 기본적인 클론입니다:

```python
import os
import sys

from rich import print
from rich.columns import Columns

directory = os.listdir(sys.argv[1])
print(Columns(directory))
```

아래 스크린샷은 API에서 뽑은 데이터를 종렬로 표현하는 [칼럼 예제](https://github.com/textualize/rich/blob/master/examples/columns.py)의 출력 결과입니다:

[![columns](https://github.com/textualize/rich/raw/master/imgs/columns.png)](https://github.com/textualize/rich/raw/master/imgs/columns.png)


### 마크다운 (Markdown)
Rich는 [마크다운](https://rich.readthedocs.io/en/latest/markdown.html)을 표현하거나 형태를 터미널에 맞추어 적절히 변환할 수 있습니다.

마크다운을 표현하기 위해서는 `Markdown` 클래스를 import하고 마크다운을 포함하고 있는 문자열을 통해 객체를 생성해주세요. 다음은 예제입니다:

```python
from rich.console import Console
from rich.markdown import Markdown

console = Console()
with open("README.md") as readme:
    markdown = Markdown(readme.read())
console.print(markdown)
```

위 코드는 아래와 같은 출력 결과를 만들 것입니다:

[![markdown](https://github.com/textualize/rich/raw/master/imgs/markdown.png)](https://github.com/textualize/rich/raw/master/imgs/markdown.png)

### 구문 강조 (Syntax Highlighting)
Rich는 [구문 강조](https://rich.readthedocs.io/en/latest/syntax.html) 기능을 수행하기 위해 [pygments](https://pygments.org/) 라이브러리를 사용합니다. 사용법은 마크다운과 유사합니다. `Syntax` 객체를 생성하고 콘솔에 출력하세요. 예제는 다음과 같습니다:

```python
from rich.console import Console
from rich.syntax import Syntax

my_code = '''
def iter_first_last(values: Iterable[T]) -> Iterable[Tuple[bool, bool, T]]:
    """Iterate and generate a tuple with a flag for first and last value."""
    iter_values = iter(values)
    try:
        previous_value = next(iter_values)
    except StopIteration:
        return
    first = True
    for value in iter_values:
        yield first, False, previous_value
        first = False
        previous_value = value
    yield first, True, previous_value
'''
syntax = Syntax(my_code, "python", theme="monokai", line_numbers=True)
console = Console()
console.print(syntax)
```

위 코드는 아래와 같은 출력 결과를 만들 것입니다:

[![syntax](https://github.com/textualize/rich/raw/master/imgs/syntax.png)](https://github.com/textualize/rich/raw/master/imgs/syntax.png)

### 트레이스백 (Traceback)
Rich는 [예쁜 tracebacks](https://rich.readthedocs.io/en/latest/traceback.html)을 표현할 수 있습니다. 이것은 읽기도 더 쉽고 일반적인 파이썬 tracebacks 보다 더 많은 코드를 보여줍니다. uncaught exceptions가 Rich로 출력되도록 Rich를 기본 Traceback 핸들러로 설정할 수도 있습니다.

OSX에서는 이렇게 출력됩니다 (리눅스도 유사함):

[![traceback](https://github.com/textualize/rich/raw/master/imgs/traceback.png)](https://github.com/textualize/rich/raw/master/imgs/traceback.png)

#### 트레이스백 출력 (Printing tracebacks)

[`print_exception()`](https://rich.readthedocs.io/en/latest/reference/console.html#rich.console.Console.print_exception "rich.console.Console.print_exception") 메서드는 현재 처리 중인 예외에 대한 트레이스백을 출력합니다. 예시는 다음과 같습니다:

```python
from rich.console import Console
console = Console()

try:
    do_something()
except Exception:
    console.print_exception(show_locals=True)
```

`show_locals=True` 매개변수는 Rich가 트레이스백의 각 프레임에 대한 로컬 변수 값을 표시하도록 합니다.

더 큰 예시는 [exception.py](https://github.com/willmcgugan/rich/blob/master/examples/exception.py)를 참조하세요.

#### 트레이스백 핸들러 (Traceback Handler)

Rich를 기본 트레이스백 핸들러로 설치하여 모든 잡히지 않은 예외가 강조 표시와 함께 렌더링되도록 할 수 있습니다. 방법은 다음과 같습니다:

```python
from rich.traceback import install
install(show_locals=True)
```

트레이스백 핸들러를 구성하는 몇 가지 옵션이 있습니다. 자세한 내용은 [`install()`](https://rich.readthedocs.io/en/latest/reference/traceback.html#rich.traceback.install "rich.traceback.install")을 참조하세요.

##### 자동 트레이스백 핸들러 (Automatic Traceback Handler)

경우에 따라 모듈에서 코드를 가져오는 것을 걱정하지 않고 트레이스백 핸들러를 자동으로 설치하고 싶을 수 있습니다. 가상 환경의 sitecustomize.py를 수정하여 이를 수행할 수 있습니다. 일반적으로 가상 환경 경로의 site-packages 폴더 아래에 있을 것입니다. 예를 들면 다음과 같습니다:

```
./.venv/lib/python3.9/site-packages/sitecustomize.py
```

대부분의 경우 이 파일은 존재하지 않을 것입니다. 존재하지 않는 경우 다음과 같이 생성할 수 있습니다:

```
$ touch .venv/lib/python3.9/site-packages/sitecustomize.py
```

파일에 다음 코드를 추가하세요:

```python
from rich.traceback import install
install(show_locals=True)
```

이 시점에서 가상 환경 내에서 실행되는 모든 코드에 대해 트레이스백이 설치됩니다.

> 코드를 공유할 계획이라면 주 진입점 모듈에 트레이스백 설치를 포함하는 것이 가장 좋습니다.

#### 프레임 억제 (Suppressing Frames)

프레임워크(click, django 등)로 작업하는 경우 트레이스백 내에서 자신의 애플리케이션 코드만 보고 싶을 수 있습니다. Traceback, install, Console.print_exception 및 RichHandler의 suppress 인수를 모듈 또는 문자열 경로 목록으로 설정하여 프레임워크 코드를 제외할 수 있습니다.

다음은 Rich 예외에서 [click](https://click.palletsprojects.com/en/8.0.x/)을 제외하는 방법입니다:

```python
import click
from rich.traceback import install
install(suppress=[click])
```

억제된 프레임은 코드 없이 줄과 파일만 표시합니다.

#### 최대 프레임 (Max Frames)

재귀 오류는 렌더링하는 데 시간이 오래 걸리고 반복적인 프레임이 많이 포함된 매우 큰 트레이스백을 생성할 수 있습니다. Rich는 기본값이 100인 max_frames 인수로 이를 방지합니다. 트레이스백에 100개 이상의 프레임이 포함된 경우 처음 50개와 마지막 50개만 표시됩니다. max_frames를 0으로 설정하여 이 기능을 비활성화할 수 있습니다.

다음은 재귀 오류를 출력하는 예시입니다:

```python
from rich.console import Console

def foo(n):
    return bar(n)

def bar(n):
    return foo(n)

console = Console()

try:
    foo(1)
except Exception:
    console.print_exception(max_frames=20)
```


# 엔터프라이즈를 위한 Rich

Tidelift 구독의 일환으로 가능합니다.

Rich를 포함한 수천가지 다른 패키지들의 메인테이너들은 당신이 앱을 만들기 위해 사용하는 오픈소스 패키지의 상업적인 지원과 유지보수를 위해 Tidelift와 함께 일하고 있습니다. 당신이 사용하는 패키지의 메인테이너에게 비용을 지불하는 대신 시간을 절약하고, 리스크를 줄이고, 코드의 품질을 향상시킬 수 있습니다. [더 자세한 정보는 여기를 참고바랍니다.](https://tidelift.com/subscription/pkg/pypi-rich?utm_source=pypi-rich&utm_medium=referral&utm_campaign=enterprise&utm_term=repo)

# Rich를 사용하는 프로젝트들

Rich를 사용하는 몇가지 프로젝트들입니다:

- [BrancoLab/BrainRender](https://github.com/BrancoLab/BrainRender)
  신경해부학 데이터의 3차원 시각화를 위한 파이썬 패키지
- [Ciphey/Ciphey](https://github.com/Ciphey/Ciphey)
  자동 암호해독 툴
- [emeryberger/scalene](https://github.com/emeryberger/scalene)
  파이썬을 위한 고성능, 높은 정밀도의 CPU / Memory 프로파일러
- [hedythedev/StarCli](https://github.com/hedythedev/starcli)
  당신의 커맨드라인에서 GitHub 트렌딩 프로젝트들을 검색해보세요
- [intel/cve-bin-tool](https://github.com/intel/cve-bin-tool)
  이 툴은 여러 공통적이고 취약한 컴포넨트들(openssl, libpng, libxml2, expat 과 몇가지 더)을 스캔해, 이미 알려진 취약점을 가진 일반 라이브러리가 당신의 시스템에 있는지 알려줍니다.
- [nf-core/tools](https://github.com/nf-core/tools)
  nf-core 커뮤니티를 위한 도우미 도구를 포함한 파이썬 패키지.
- [cansarigol/pdbr](https://github.com/cansarigol/pdbr)
  개선된 디버깅을 위한 pdb + Rich 라이브러리
- [plant99/felicette](https://github.com/plant99/felicette)
  더미 위성 이미지
- [seleniumbase/SeleniumBase](https://github.com/seleniumbase/SeleniumBase)
  Selenium & pytest로 10배 더 빠르게 자동화 & 테스트하세요. 배터리도 포함되어 있습니다.
- [smacke/ffsubsync](https://github.com/smacke/ffsubsync)
  자동으로 자막과 영상의 싱크를 맞추세요.
- [tryolabs/norfair](https://github.com/tryolabs/norfair)
  모든 탐지된 것에 실시간으로 2D 오브젝트 트래킹을 추가하는 경량화된 파이썬 라이브러리.
- [ansible/ansible-lint](https://github.com/ansible/ansible-lint)
  Ansible-lint가 playbooks를 확인해 잠재적으로 개선될 수 있는 practices나 동작을 확인합니다.
- [ansible-community/molecule](https://github.com/ansible-community/molecule)
  Ansible Molecule의 테스트 프레임워크
- +[Many more](https://github.com/textualize/rich/network/dependents)!

<!-- This is a test, no need to translate -->


---

## 참조

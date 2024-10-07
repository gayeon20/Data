---
title: "[Python] Poetry"
excerpt: Python의 패키지 & 의존성 관리 도구 Poetry 에 대한 문서
categories:
  - Python
tags:
  - Python
  - Python-Environment
  - Python-Dependency
  - Poetry
last_modified_at: 2024-04-11T15:11:38+09:00
link: https://python-poetry.org/
상위 항목:
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

**하위 항목**
- [[python_poetry_command|명령어 (Command)]]

---

> 23 년도 기준으로 많은 업데이트를 통해 사용 가능한 수준이 되면서 도입되는 추세

- Python 은 `pip`, `pipenv`, `setuptools`, `distutils`, (가상 환경만으로) `venv` 등과 같은 여러 패키지 및 의존성 관리 도구를 가지고 있습니다. 하지만 해당 도구들은 " 각각 특별한 사용 사례를 목표로 설계 " 되었기 때문에, 파이썬 커뮤니티는 " 통합된, 일관된, 및 사용자 친화적인 도구 " 에 대한 니즈가 계속 있었고 이러한 필요성이 "poetry" 의 탄생 배경이 되었습니다.
- Poetry 는 Python 개발시 패키지의 의존성을 관리하는 라이브러리 이며, 자바의 maven 이나 gradle 비슷한 툴이라고 볼 수 있습니다.
- Virtualenv 와 같이 가상환경 설정을 지원하여, 보다 포괄적인 의미의 기능도 있으며, build/publish 같은 배포까지도 가능한 범용적인 tool 로도 사용할 수 있습니다

## 1. 특징

### 1) 의존성 해결과 잠금

- 내 프로젝트에 필요한 A, B 가 있고, B 는 A 의 2.0 버전 이상 (>= A 2.0) 을 요구한다고 할 때, pip 으로 설치하게 되면 내가 A 을 1.0 버전으로 설치한다고 해도 아무런 문제가 발생하지 않아서 실행해 보고 에러메시지를 마주한 뒤에 깨닫는 경우가 대부분입니다. 하지만 poetry 는 " 버전 관련 정보를 확인하고 " **특정 버전 이상이 아닐 경우에 아예 설치가 되지 않습니다.
- **`pip` 은 `lock` 파일이 없고, 직접 `requirements.txt` 를 작성해야 합니다. 게다가 사실 이 리콰파일도 그냥 출력 `>>` 으로 만든다. 반면 `poetry` 는 `lock` 파일과 ``pyproject.toml`` 을 자동으로 생성 및 업데이트해줍니다. 더 정확하게는 ``pyproject.toml`` 중심으로 모든 라이브러리 및 프로젝트 관리가 시작됩니다.

### 2) 가상 환경

- 가상환경을 구성하지 않으면 `pip` 은 전역에 패키지를 설치하기 때문에, 해당 설치툴로는 다른 환경에서의 버전 관리가 불가합니다. 그래서 기본적으로 존재하는 `venv` 또는 미니콘다나 `virtualenv` 같은 툴이 부가적으로 필요하게 됩니다.
- 사용자마다 결국 다 다른 가상환경이며 특수 목적으로 만들어진 가상환경 겸 라이브러리도 있습니다. 반면 poetry 는 가상환경 여부를 확인하고 기존 환경, 혹은 새로 만들어 설치하는 등 자동으로 관리합니다.

### 3) 통합된 도구

- python 진영에서는 " 가상환경 " 그리고 " 의존성 " 그리고 " 빌드 " 그리고 … 등 과 같이 특수 목적에 따라 다른 라이브러리, 써드파티 (필요하 경우 make file 도) 등 다양한 도구를 사용했습니다.
- 이제 그러한 모든 부분을 `poetry` 를 중심으로 세팅할 수 있습니다.

### 4) 멀티버전 패키징과 플러그인 시스템

- 기본적으로 Poetry 는 프로젝트의 Python " 버전을 명시 " 하기때문에 다양한 버전의 Python 에 대해 패키지를 생성하거나 테스트할 수 있도록 지원합니다.
- Poetry 1.2.0 부터 플러그인 시스템을 지원하게 되어, 커뮤니티에서 다양한 확장 기능을 개발하고 공유할 수 있게 되었습니다. [링크](https://python-poetry.org/docs/master/plugins/)

## 2. [설치](https://python-poetry.org/docs/#installing-with-the-official-installer)

- pipx 는 파이썬 CLI 애플리케이션을 가상 환경에서 격리시키면서 전역적으로 설치하는 데 사용됩니다. pipx 를 사용하여 Poetry 를 설치할 경우, 업그레이드와 제거를 관리할 수 있습니다.
- pipx 가 아직 설치되지 않았다면, [공식 pipx 설치 지침](https://pipx.pypa.io/stable/installation/) 의 옵션 중 하나를 따를 수 있습니다. pipx 의 어떤 최신이 아닌 버전이라도 괜찮습니다.

### (1) Poetry 설치

```bash
pipx install poetry
```

#### 수동 설치

- pipx 는 pip 와 동일한 문법을 사용하여 Poetry 의 다른 버전들을 설치할 수 있습니다:

```bash
pipx install poetry==1.2.0
```

- pipx 는 또한 병렬로 Poetry 의 버전을 설치할 수 있으며, 이를 통해 대체 버전이나 사전 릴리스 버전의 테스트가 쉬워집니다. 각 버전은 사용자가 지정한 고유한 접미사를 받아 고유한 바이너리 이름을 생성합니다:

```bash
pipx install --suffix=@1.2.0 poetry==1.2.0
poetry@1.2.0 --version

pipx install --suffix=@preview --pip-args=--pre poetry
poetry@preview --version
```

- 마지막으로, pipx 는 git 에서 개발 버전을 설치하거나, 심지어 풀 리퀘스트의 로컬 테스팅을 위해 유효한 pip 요구 사항 스펙을 설치할 수 있습니다:

```bash
pipx install --suffix @main git+https://github.com/python-poetry/poetry.git@main
pipx install --suffix @pr1234 git+https://github.com/python-poetry/poetry.git@refs/pull/1234/head
```

#### WSL
Official Installer 를 이용하여 별도의 설치를 진행해야 합니다.

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

이후 PATH에 poetry 경로를 등록해야 합니다. `.bashrc`, `.zshrc`의 경우 아래 명령어를 추가합니다.

```sh
export PATH="$HOME/.local/bin:$PATH"
```

`~/.config/fish/config.fish`의 경우 아래 명령어를 추가합니다.

```sh
set -gx PATH $HOME/.local/bin $PATH
```


### (2) 업데이트

```bash
pipx upgrade poetry
```

### (3) 제거

```
pipx uninstall poetry
```

#### 캐시 삭제

- Poetry 는 다양한 캐시 파일을 사용합니다. 이러한 캐시 파일들을 삭제하기 위해 다음과 같은 명령어를 실행할 수 있습니다.

```bash
poetry cache clear --all
```

- 이 명령어는 Poetry 가 관리하는 모든 캐시를 삭제합니다.
- Poetry 는 또한 홈 디렉토리에 캐시 폴더를 생성할 수 있습니다. 이러한 캐시 폴더를 수동으로 삭제하기 위해 다음 명령어를 사용할 수 있습니다.

```bash
rm -rf $(poetry config cache-dir)
```

- 만약 `poetry` 명령어가 더 이상 사용 가능하지 않다면, 대신 기본 캐시 경로를 직접 삭제할 수 있습니다. 일반적으로 캐시 경로는 다음과 같습니다:

```bash
rm -rf ~/Library/Caches/pypoetry
```

- Ubuntu 에서의 경로는 위와 다를 수 있으며, 일반적으로 `~/.cache/pypoetry` 또는 `~/.poetry/cache` 와 같은 경로일 수 있습니다. 해당 경로가 정확하지 않다면, 홈 디렉토리에서 캐시 디렉토리를 찾기 위해 `find` 명령어를 사용할 수 있습니다:

```bash
find ~ -type d -name 'pypoetry' -or -name 'poetry'
```

- 이 명령어로 찾은 경로에 있는 폴더를 삭제하면 됩니다. 아래 경로가 검색될 수 있습니다.

```
~/.local/share/pypoetry
~/.local/share/pypoetry/venv/bin/poetry
~/.local/share/pypoetry/venv/lib/python3.11/site-packages/poetry
```


## 3. 자동 완성 설정

### 1) Bash

#### (1) Auto-loaded (recommended)

```bash
poetry completions bash >> ~/.bash_completion
```

#### (2) Lazy-loaded

```bash
poetry completions bash > ${XDG_DATA_HOME:-~/.local/share}/bash-completion/completions/poetry
```

### 2) Fish

```bash
poetry completions fish > ~/.config/fish/completions/poetry.fish
```

### 3) Zsh

```zsh
poetry completions zsh > ~/.zfunc/_poetry
```

- 그런 다음 `~/.zshrc` 에 다음 줄을 추가해야 합니다 (아직 존재하지 않는 경우):

```bash
fpath+=~/.zfunc
autoload -Uz compinit && compinit
```

#### Oh My Zsh

```zsh
mkdir $ZSH_CUSTOM/plugins/poetry
poetry completions zsh > $ZSH_CUSTOM/plugins/poetry/_poetry
```

- 그런 다음 `~/.zshrc` 의 플러그인 배열에 poetry 를 추가해야 합니다:

```text
plugins(
	poetry
	…
	)
```

#### prezto

```zsh
poetry completions zsh > ~/.zprezto/modules/completion/external/src/_poetry
```

## 4. 기본 사용법
> Python 버전 관리는 [[python_pyenv|pyenv]]를 사용합니다.


### 1) 프로젝트 생성

- 먼저, 새 프로젝트를 만들어봅시다. 이 프로젝트의 이름을 `poetry-demo` 라고 합시다:

```bash
poetry new poetry-demo
```

- 이 명령어는 다음과 같은 내용을 포함하는 `poetry-demo` 디렉토리를 생성합니다:

```
poetry-demo
├── `pyproject.toml`
├── README.md
├── poetry_demo
│   └── __init__.py
└── tests
    └── __init__.py
```

- 여기에서 가장 중요한 파일은 ``pyproject.toml`` 파일입니다. 이 파일이 프로젝트와 그 의존성을 관리합니다. 초기 파일:

```toml
[tool.poetry]
name = "poetry-demo"
version = "0.1.0"
description = ""
authors = ["Sébastien Eustace <sebastien@eustace.io>"]
readme = "README.md"
packages = [{include = "poetry_demo"}]

[tool.poetry.dependencies]
python = "^3.7"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

- Poetry 는 프로젝트의 루트에 `tool.poetry.name` 과 동일한 이름의 패키지가 포함되어 있다고 가정합니다. 만약 그렇지 않다면, `tool.poetry.packages` 를 채워 패키지와 그 위치를 지정해야 합니다.
- 마찬가지로, 전통적인 `MANIFEST.in` 파일은 `tool.poetry.readme`, `tool.poetry.include`, 그리고 `tool.poetry.exclude` 섹션으로 대체됩니다. `tool.poetry.exclude` 는 추가적으로 `.gitignore` 에 의해 암묵적으로 채워집니다. 프로젝트 포맷에 대한 전체 문서는 문서의 pyproject 섹션을 참조하세요.
- `tool.poetry` 과 같은 테이블을 표시하면 다음 테이블 전까지는 Key-Value 가 모두 해당 테이블에 포함됩니다.
- Poetry 는 지원하려는 Python 버전을 명시적으로 지정하도록 요구하며, 그것의 범용 잠금은 프로젝트가 지원하는 모든 Python 버전에 대해 설치 가능하며 (모든 의존성이 지원을 주장함) 보장합니다.

### 2) 기존 프로젝트에 설정

새 프로젝트를 생성하는 대신, Poetry 는 이미 채워진 디렉토리를 ' 초기화 ' 하는 데 사용될 수 있습니다. 이미 존재하는 디렉토리 pre-existing-project 에 `pyproject.toml` 파일을 대화형으로 생성하려면:

```bash
cd pre-existing-project
poetry init
```

### 3) 운영 모드

- Poetry 는 두 가지 다른 모드로 운영될 수 있습니다. 기본 모드는 패키지 모드로, 프로젝트를 sdist 나 wheel 로 패키징하고 패키지 인덱스에 게시하고 싶은 경우에 적합한 모드입니다. 이 모드에서는 패키징에 필요한 이름과 버전과 같은 일부 메타데이터가 필수입니다. 또한, `poetry install` 을 실행할 때 프로젝트 자체가 편집 가능 모드로 설치됩니다.
- Poetry 를 패키징용이 아닌 의존성 관리만을 위해 사용하고 싶다면, 비 - 패키지 모드를 사용할 수 있습니다:

```toml
[tool.poetry]
package-mode = false
```

- 이 모드에서는 이름과 버전과 같은 메타데이터가 선택 사항입니다. 따라서, 배포물을 빌드하거나 프로젝트를 패키지 인덱스에 게시하는 것이 불가능합니다. 또한, `poetry install` 을 실행할 때 Poetry 는 프로젝트 자체를 설치하려고 시도하지 않고, 그 의존성만 설치합니다 (`poetry install --no-root` 와 동일).

> [pyproject](https://python-poetry.org/docs/pyproject/) 섹션에서 패키지 모드에서 필요한 필드를 볼 수 있습니다.

### 4) 가상 환경 사용

- Poetry 는 기본적으로 `{cache-dir}/virtualenvs` 에 가상 환경을 생성합니다. `cache-dir` 값을 변경하려면 Poetry 설정을 편집하세요. 또한, 프로젝트 디렉토리 내에 가상 환경을 생성하기 위해 `virtualenvs.in-project` 구성 변수를 사용할 수 있습니다.
- `poetry shell` 을 통해 가상환경에 진입하면 `…/virtualenvs/my_project-ZdOTN-ZS-py3.9` 와 같은 경로로 세팅되어 있는 것이 확인 가능합니다.
- `poetry env info` 로 구성된 가상환경 확인이 가능하며 `poetry env list` 로 사용 가능한 가상환경 리스트를 볼 수 있습니다.
- `poetry env remove python3` 와 같이 지금 세팅된 가상 환경을 remove 할 수 있습니다. (python3 자리에는 우리가 사용하는 python 버전의 path, 심볼릭 링크 걸려있거나 path 등록되어 있으면 당연히 python3 그대로 사용 가능)
- 이렇게 자동 세팅되는 `cache-dir` 는 `poetry config` 명령어를 통해 임의로 설정할 수 있으며, `virtualenvs.in-project` 설정 변경을 통해 가상환경이 프로젝트 내에 위치하도록 할 수도 있습니다. `poetry config virtualenvs.in-project true` 와 같이 입력하고 `poetry env use python3` 을 입력하면 아래와 같이 깔끔하게 프로젝트 내부에 가상환경 파일을 위치시킬 수 있습니다.

> [!NOTE] 외부 가상 환경 관리
> - Poetry 는 외부에서 활성화된 기존 가상 환경을 감지하고 존중합니다. 이는 Poetry 의 내장된, 단순화된 환경 관리에 대한 대안이 될 수 있는 강력한 메커니즘입니다.
> - 이를 활용하려면, 환경을 조작하기 위한 Poetry 명령어를 실행하기 전에 선호하는 방법이나 도구를 사용하여 가상 환경을 활성화하십시오.

#### (1) `poetry run` 사용하기

- 스크립트를 실행하려면 `poetry run python your_script.py` 를 사용하십시오. 마찬가지로 pytest 나 black 과 같은 명령줄 도구가 있으면 `poetry run pytest` 를 사용하여 실행할 수 있습니다.
- 외부에서 자체 가상 환경을 관리하는 경우, 이미 해당 가상 환경을 활성화했고 올바른 파이썬 인스턴스를 사용할 수 있게 했으므로 `poetry run` 이나 `poetry shell` 을 사용할 필요가 없습니다. 예를 들어, 이러한 명령어는 같은 파이썬 경로를 출력해야 합니다:

```bash
conda activate your_env_name
which python
poetry run which python
poetry shell
which python
```

#### (2) 가상 환경 활성화하기

- 가장 쉬운 방법은 `poetry shell` 로 중첩 쉘을 생성하는 것입니다.
- 이 새로운 쉘을 탈퇴하고 가상 환경을 비활성화하려면 `exit` 를 입력하세요. 쉘을 떠나지 않고 가상 환경을 비활성화하려면 `deactivate` 를 사용하세요.

> [!question] 중첩 쉘을 왜 사용하나요?
> - 자식 프로세스는 부모로부터 환경을 상속받지만, 공유하지는 않습니다. 따라서 자식 프로세스가 만든 모든 수정 사항은 자식 프로세스가 종료된 후에는 유지되지 않습니다.
> - 파이썬 애플리케이션 (Poetry) 은 자식 프로세스로서, 호출된 쉘의 환경을 수정할 수 없어 가상 환경이 활성화된 채로 Poetry 명령어가 실행 완료된 후에도 유지됩니다.

- 따라서 Poetry 는 가상 환경이 활성화된 새로운 서브 쉘을 생성해야 하며, 이후의 명령어가 가상 환경 내에서 실행될 수 있도록 해야 합니다.
- 가상 환경 활성화 시 `poetry hsell` 이 쉘 프롬프트를 수정하지 않게 하려면, 명령어를 실행하기 전에 환경 변수로 `VIRTUAL_ENV_DISABLE_PROMPT=1` 을 설정해야 합니다.
- 새로운 쉘을 생성하지 않고 가상 환경을 수동으로 활성화하려면, `source {path_to_venv}/bin/activate` (`{path_to_venv}\Scripts\activate.ps1` in PowerShell) 를 실행하세요. 가상 환경의 경로를 얻으려면 `poetry env info --path` 를 실행하세요. 이를 한 줄로 결합할 수도 있습니다, 예를 들어 `source $(poetry env info --path)/bin/activate` (`& ((poetry env info --path) + "\Scripts\activate.ps1")`

| POSIX SHELL       | WINDOWS (POWERSHELL)                            | EXIT/DEACTIVATE                                          |              |
| ----------------- | ----------------------------------------------- | -------------------------------------------------------- | ------------ |
| Sub-shell         | `poetry shell`                                  | `poetry shell`                                           | `exit`       |
| Manual Activation | `source {path_to_venv}/bin/activate`            | `{path_to_venv}\Scripts\activate.ps1`                    | `deactivate` |
| One-liner         | `source $(poetry env info --path)/bin/activate` | `& ((poetry env info --path) + "\Scripts\activate.ps1")` | `deactivate` |

#### (3) Pyenv 활용

- Pyenv 로 Local 파이썬 버전을 설정하고, Poetry 로 Local 파이썬 버전에 해당하는 가상 환경을 생성합니다.

```bash
# local 파이썬 버전 설정
pyenv local 3.8.10

# Poetry로 가상환경 생성
poetry env use python3

# 쉘을 활성화
poetry shell
```

### 5) 의존성 지정

- 프로젝트에 의존성을 추가하고 싶다면, `tool.poetry.dependencies` 섹션에서 지정할 수 있습니다.

```toml
[tool.poetry.dependencies]
pendulum = "^2.1"
```

- 보시다시피, 패키지 이름과 버전 제약의 매핑을 사용합니다.
- Poetry 는 이 정보를 사용하여 등록한 `tool.poetry.source` 섹션의 패키지 " 저장소 " 나 기본적으로 PyPI 에서 적합한 파일 세트를 검색합니다.
- 또한, ``pyproject.toml`` 파일을 직접 수정하는 대신, add 명령어를 사용할 수 있습니다.

```bash
poetry add pendulum
```

- 이 명령어는 자동으로 적합한 버전 제약을 찾아 패키지와 하위 의존성을 설치합니다.
- Poetry 는 캐럿, 틸드, 와일드카드, 부등호 및 다중 제약 조건 요구 사항을 포함한 풍부한 의존성 명세 구문을 지원합니다.

[Dependency specification | Documentation | Poetry - Python dependency management and packaging made easy (python-poetry.org)](https://python-poetry.org/docs/dependency-specification/#python-restricted-dependencies)

### 6) 버전 제약 조건

- 우리의 예시에서, 우리는 ^2.1 이라는 버전 제약 조건을 가진 pendulum 패키지를 요청하고 있습니다. 이는 2.1.0 이상 그리고 3.0.0 미만 (>=2.1.0 <3.0.0) 의 어떤 버전이라도 의미합니다. 버전, 버전 간의 관계, 그리고 의존성을 지정하는 다양한 방법에 대한 보다 심층적인 정보를 얻으려면 [의존성 명세](https://python-poetry.org/docs/dependency-specification/) 를 읽어보시기 바랍니다.

> [!question] Poetry 는 어떻게 올바른 파일을 다운로드하나요?
> `pyproject.toml` 에 의존성을 지정할 때, Poetry 는 먼저 요청한 패키지의 이름을 취하고 `repositories` 키를 사용하여 등록한 모든 저장소에서 검색합니다. 추가 저장소를 등록하지 않았거나 지정한 저장소에서 해당 이름의 패키지를 찾지 못한 경우, PyPI 로 되돌아갑니다.
>
> Poetry 가 올바른 패키지를 찾으면, 지정한 버전 제약 조건에 가장 잘 맞는 것을 찾으려고 시도합니다.

### 7) 의존성 설치하기

- 프로젝트에 정의된 의존성을 설치하려면, 그냥 설치 명령어를 실행하면 됩니다.

```bash
# 의존성 설치
poetry install

# 개발환경의 의존성은 빼고 설치
poetry install --no-dev

# -E 또는 --extras 로 추가 의존성을 설정가능
poetry install --extras "mysql redis"
poerty install -E mysql -E redis
```

#### (1) `poetry.lock` 없이 설치하기

- 이전에 이 명령어를 실행한 적이 없고 `poetry.lock` 파일도 없는 경우, Poetry 는 단순히 `pyproject.toml` 파일에 나열된 모든 의존성을 해결하고 그들의 파일의 최신 버전을 다운로드합니다.
- Poetry 가 설치를 완료하면, 다운로드한 모든 패키지와 그들의 정확한 버전을 `poetry.lock` 파일에 기록하여 프로젝트를 그 특정 버전에 고정합니다. 프로젝트에 참여하는 모든 사람이 동일한 버전의 의존성에 고정되도록 `poetry.lock` 파일을 프로젝트 리포지토리에 커밋해야 합니다 (아래에서 더 자세히 설명합니다).

#### (2) `poetry.lock` 이 있는 상태에서 설치하기

- poetry install 을 실행할 때 이미 `poetry.lock` 파일과 `pyproject.toml` 파일이 있다면, 설치 명령어를 이전에 실행했거나 프로젝트의 다른 누군가가 설치 명령어를 실행하고 `poetry.lock` 파일을 프로젝트에 커밋했다는 의미입니다 (이는 좋은 일입니다).
- 어느 쪽이든, `poetry.lock` 파일이 있을 때 install 을 실행하면 `pyproject.toml` 에 나열된 모든 의존성을 해결하고 설치하지만, Poetry 는 `poetry.lock` 에 나열된 정확한 버전을 사용하여 프로젝트에서 일하는 모든 사람에게 패키지 버전이 일관되게 유지되도록 합니다. 결과적으로, `pyproject.toml` 파일에 요청된 모든 의존성을 가지게 될 것이지만, 모든 것이 가장 최신 버전일 수는 없습니다 (파일이 생성된 이후에 일부 의존성이 더 새로운 버전을 출시했을 수 있음). 이는 설계에 의한 것으로, 의존성의 예기치 않은 변화로 인해 프로젝트가 중단되는 것을 방지합니다.

#### (3) 버전 관리에 `poetry.lock` 파일 커밋하기

- 애플리케이션 개발자들은 더 재현 가능한 빌드를 얻기 위해 `poetry.lock` 을 커밋합니다.
- 이 파일을 VC 에 커밋하는 것은 프로젝트를 설정하는 모든 사람이 당신이 사용하는 것과 정확히 동일한 버전의 의존성을 사용하게 만들기 때문에 중요합니다. CI 서버, 생산 머신, 팀의 다른 개발자들, 모든 것과 모든 사람이 동일한 의존성에서 작동하여, 배포의 일부 부분에만 영향을 미치는 버그의 가능성을 줄입니다. 혼자 개발한다 하더라도, 6 개월 후 프로젝트를 다시 설치할 때 당시에 의존성이 많은 새로운 버전을 출시했더라도 설치된 의존성이 여전히 작동한다는 것을 확신할 수 있습니다. (update 명령어 사용에 대한 아래 참고 사항 참조)
- 프로젝트의 `pyproject.toml` 에 권장되는 `[build-system]` 섹션을 추가했다면, `pip install -e.` 와 같은 명령어를 사용하여 프로젝트와 그 의존성을 가상 환경에 성공적으로 설치할 수 있습니다. 그러나 pip 은 poetry-core 빌드 시스템이 라이브러리 개발자를 위한 것으로, lock 파일을 사용하여 의존성 버전을 결정하지 않습니다.

#### (4) 라이브러리 개발자로서

- 라이브러리 개발자들은 더 많은 것을 고려해야 합니다. 사용자는 애플리케이션 개발자이며, 당신의 라이브러리는 당신이 제어하지 않는 파이썬 환경에서 실행될 것입니다.
- 애플리케이션은 당신의 라이브러리의 lock 파일을 무시합니다. 이는 `pyproject.toml` 에 있는 제약 조건을 충족하는 어떤 의존성 버전도 사용할 수 있음을 의미합니다. 애플리케이션은 아마도 최신 호환 의존성 버전을 사용할 것입니다. 만약 당신의 라이브러리의 `poetry.lock` 이 사용자에게 문제를 일으키는 새로운 의존성 버전에 뒤처진다면, 당신이 그것에 대해 마지막으로 알게 될 가능성이 높습니다.
- 이러한 시나리오를 피하는 간단한 방법은 `poetry.lock` 파일을 생략하는 것입니다. 그러나 이렇게 함으로써, 재현성과 성능을 어느 정도 희생합니다. lockfile 없이는, 눈에 띄지 않는 라이브러리 업데이트가 원인일 수 있는 실패하는 테스트의 원인을 찾기 어려울 수 있습니다. 더욱이, `poetry.lock` 이 생략되었다면, Poetry 는 의존성을 설치하기 전에 lock 을 해야 합니다. 의존성의 수에 따라, locking 은 상당한 시간을 소요할 수 있습니다.
- 재현성과 성능 혜택을 포기하고 싶지 않다면, 정기적으로 `poetry.lock` 을 새로고침하여 최신 상태를 유지하고 사용자에게 갑작스러운 중단의 위험을 줄이는 것을 고려하세요.

#### (5) 의존성만 설치하기

- 현재 프로젝트는 기본적으로 편집 가능 모드로 설치됩니다. 의존성만 설치하고 싶다면, `--no-root` 플래그와 함께 install 명령어를 실행하세요:

```python
poetry install --no-root
```

### 8) 의존성을 최신 버전으로 업데이트하기

- `poetry.lock` 파일은 자동으로 의존성의 최신 버전을 가져오는 것을 방지합니다. 최신 버전으로 업데이트하려면, `update` 명령어를 사용하세요. 이는 `pyproject.toml` 파일에 따라 최신 일치 버전을 가져오고 lock 파일을 새 버전으로 업데이트합니다. (이는 `poetry.lock` 파일을 삭제하고 다시 install 을 실행하는 것과 동일합니다.)
- `poetry.lock` 과 `pyproject.toml` 이 동기화되지 않은 경우 install 명령어를 실행할 때 Poetry 는 경고를 표시할 것입니다.

### 9) 린팅 (Linting)

- `poetry add --group dev black flake8` 을 통해 패키지를 추가하고 `pyproject.toml` 파일에 아래 설정값을 추가하자

```yaml
# 아래 섹션은 black의 설정
[tool.black]
line-length = 88
target-version = ['py38']
include = '\.pyi?$'
exclude = '''
/(
    \.git
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
)/
'''

# 아래 섹션은 flake8의 설정
[tool.flake8]
ignore = "E203, E501, W503"
max-line-length = 88
exclude = ".git,__pycache__,docs/,old/,build/,dist/"
```

- 이제 `poetry run black.` & `poetry run flake8` 과 같이 실행해서 해당 린팅을 세팅할 수 있다. 위 설정 그대로 vscode 에서도 IDE level 에서 린팅을 적용하고 싶다면 `./.vscode/settings.json` 을 만들어 아래 값으로 세팅하면 된다.

```json
{
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": [
        "--line-length",
        "88"
    ],
    "[python]": {
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    },
    "python.linting.flake8Args": [
        "--ignore=E203,E501,W503",
        "--max-line-length=88"
    ]
}
```

### 10) Build & PyPI Publish

- 만든 프로젝트를 하나의 패키지로 묶어 라이브러리로 배포하려면 `poetry build` 와 `poetry publish --build` 를 진행하면 된다. 이 경우 [https://pypi.org/](https://pypi.org/) 의 계정이 필요하다!
- 이 단계에서 다양한 설정값이 필요할 수 있고 추가되면 좋은 정보도 많다. [poetry 공식 깃허브](https://github.com/python-poetry/poetry) 에서 해당 설정값을 확인하길 바란다!
- 참고로 이 `toml` 파일은 `Tom's Obvious, Minimal Language` 약자이며 " 명확하고 읽기 쉬운 최소한의 구성 파일 형식을 목표 " 로 하는 프로젝트 설정 설명 파일이다. `ini` 에서 영감을 받아서 발전되었다고 한다. [PEP 518 – Specifying Minimum Build System Requirements for Python Projects](https://peps.python.org/pep-0518/) 에서 `pyproject.toml` 파일을 이용해 패키지 빌드에 필요한 도구와 설정을 명세하고 이로써 Python 패키지의 빌드 프로세스를 표준화하고 있다.
- 더 나아가 [PEP 621 – Storing project metadata in pyproject.toml](https://peps.python.org/pep-0621/) 에서 파일에서 프로젝트 메타데이터를 정의하는 방법을 제안하고 있다. 이는 패키지의 이름, 버전, 설명, 저자 등의 정보를 TOML 형식으로 어떻게 하면 좋은지 적혀져 있다.

## 5. 오류

- 의존성이 충돌할 경우: `poetry update` 명령어를 실행하여 모든 패키지의 최신 버전을 사용하도록 업데이트합니다.

### Error: Python packaging tool 'setuptools' not found

```bash
poetry add --group dev setuptools
```

### Poetry Add 로 패키지 추가 시 작동이 멈추는 Issue

- Ubuntu 에서 `poetry init` 나 `poetry add` 로 패키지를 추가할 때 작동이 멈추는 Issue 가 발견되었습니다.
- `-vvv` 로 로그를 확인해보니 다음과 같이 keyring.backend 관련 로딩에서 다음으로 넘어가지 않습니다.
![](https://velog.velcdn.com/images/whattsup_kim/post/17d37156-3154-42e1-b9ce-e19461b57336/image.png)
- **Solution:** 다음 코드를 입력한 후, `poetry add` 하면 정상적으로 동작됩니다.

```bash
export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring
```

### vscode 에서 poetry 가상 환경 인터프리터가 잡히지 않는 Issue

- **Solution:** 생성되는 virtualenv 환경을 프로젝트 폴더 내부에 생성 (.venv) 되게 설정합니다.

```bash
# config 변경
poetry config virtualenvs.in-project true
poetry config virtualenvs.path "./.venv"

# 이후 vscode에서 사용할 가상환경 내 파이썬의 인터프리터를 선택하여 사용하면 됩니다.
# 만약, vscode에 원하는 경로의 파이썬 인터프리터가 나오지 않는다면, 
# 다음 명령어를 입력하여 인터프리터 위치를 찾아 수동으로 입력하세요.
which python
```

---

## 참조

[python - poetry 설치부터 project initializing, 활용하기 (velog.io)](https://velog.io/@qlgks1/python-poetry-%EC%84%A4%EC%B9%98%EB%B6%80%ED%84%B0-project-initializing-%ED%99%9C%EC%9A%A9%ED%95%98%EA%B8%B0)
[[Python] 파이썬 환경 구축하기 (2) Poetry (velog.io)](https://velog.io/@whattsup_kim/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%99%98%EA%B2%BD-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0-2-Poetry)

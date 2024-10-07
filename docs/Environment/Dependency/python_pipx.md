---
title: "[Python] PipX"
excerpt: Python 패키지 매니저 pipx에 대한 문서
categories:
  - Python
tags:
  - Python
  - Python-Environment
  - Python-Dependency
  - Package-Manager
  - pip
  - pipx
last_modified_at: 2024-04-11T15:11:37+09:00
link: https://pipx.pypa.io/stable/
상위 항목: "[[python_pip|pip]]"
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

> [Github](https://github.com/pypa/pipx?tab=readme-ov-file)

---

- `pipx` 는 파이썬 애플리케이션을 격리된 환경에서 설치하고 관리할 수 있게 해주는 도구입니다. 이는 각 파이썬 애플리케이션을 독립적인 가상 환경에 설치함으로써 서로 다른 애플리케이션 간의 종속성 충돌을 방지합니다. `pipx` 를 사용하면 사용자의 시스템 파이썬 환경을 깔끔하게 유지하면서 다양한 파이썬 도구를 쉽게 설치하고 사용할 수 있습니다.
- 파이썬의 패키지 관리자인 pip 는 " 패키지를 전역적으로 설치 " 하는 잘못된 초기 설계를 갖고 있었습니다. 이 때문에 시스템 관리자가 아닐 경우 패키지 설치 자체를 못하는 문제가 생겼고 나중에 user mode 를 추가했지만 일일이 옵션을 주지 않으면 실수하는 경우도 많았습니다.
- pipx 는 cli application 설치/관리에 초점을 맞춘 패키지 관리자로 libraries 보다는 cli application 의 package 를 설치/관리하는데 중점을 두고 있습니다.

## 1. [설치](https://pipx.pypa.io/stable/installation/)

> [!NOTE]
> `pipx` 를 `pipx` 로 설치하는 것은 권장되지 않습니다. 이 방법을 사용하고 싶다면, [`pipx-in-pipx`](https://github.com/mattsb42-meta/pipx-in-pipx) 프로젝트를 살펴보고 거기에 있는 제한 사항을 읽어보세요.


### 1) macOS

```bash
brew install pipx
pipx ensurepath
```

- brew 로 pipx 를 업그레이드하려면 `brew update && brew upgrade pipx` 를 실행하세요.

### 2) Linux

#### (1) Ubuntu 23.04 이상

```bash
sudo apt update
sudo apt install pipx
pipx ensurepath
```

#### (2) Ubuntu 22.04 이하

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

- pipx 를 업그레이드하려면 `python3 -m pip install --user --upgrade pipx` 를 실행하세요.

### 3) Windows

#### (1) Scoop 을 통해 설치

```bash
scoop install pipx
pipx ensurepath
```

- pipx 를 업그레이드하려면 `scoop update pipx` 를 실행하세요.

#### (2) pip 을 통해 설치 (pip 19.0 이상 필요)

```bash
# 만약 당신이 Microsoft Store를 통해 python을 설치했다면, 다음 줄에서 `py`를 `python3`으로 바꾸세요.
py -m pip install --user pipx
```

위의 명령이 다음과 비슷한 경고로 끝날 가능성이 높습니다:

```text
경고: 스크립트 pipx.exe가 `<사용자 폴더>\AppData\Roaming\Python\Python3x\Scripts`에 설치되어 있는데, 이 폴더가 PATH에 포함되어 있지 않습니다.
```

- 만약 그렇다면, 언급된 폴더로 이동하여 pipx 실행 파일을 직접 실행할 수 있습니다. 다음 줄을 입력하세요 (경고를 받지 않았더라도):

```bash
.\pipx.exe ensurepath
```

- 이는 언급된 경로와 `%USERPROFILE%\.local\bin` 폴더를 검색 경로에 추가합니다. 터미널 세션을 재시작하고 pipx 가 실행되는지 확인하세요.
- pipx 를 업그레이드하려면 `py -m pip install --user --upgrade pipx` 를 실행하세요.

### 4) 설치하지 않고 pipx 사용하기 (zipapp 을 통해)

- pipx 를 설치하지 않고도 사용할 수 있습니다. zipapp 은 Github 릴리스에서 다운로드할 수 있으며 Python 3.7+ 인터프리터로 호출할 수 있습니다:

```bash
python pipx.pyz ensurepath
```

### 5) pre-commit 과 함께 사용하기

pipx 는 [pre-commit support](https://pipx.pypa.io/stable/installation/#pre-commit) 이 있습니다.

### 6) 셸 완성

- 셀 완성 기능은 이 명령어로 출력되는 지침을 따라서 사용할 수 있습니다:

```
pipx completions
```

## 2. 삭제

1. **pipx 로 설치된 모든 패키지 제거**: pipx 로 설치된 모든 패키지를 제거합니다. 커맨드 라인이나 PowerShell 에서 다음 명령을 실행합니다:

   ```bash
   pipx uninstall --all
   ```

2. **pipx 자체 제거**: pip 를 사용하여 pipx 자체를 제거합니다.

   ```bash
   scoop uninstall pipx
   ```

3. **pipx 데이터 및 캐시 삭제**: pipx 는 기본적으로 `~/.local/pipx` (Linux 및 macOS) 또는 `%LOCALAPPDATA%\pipx` (Windows) 에 데이터와 캐시를 저장합니다. 해당 디렉토리를 삭제하여 데이터와 캐시를 제거합니다. Windows 에서는 다음 명령을 사용할 수 있습니다:

   ```powershell
   Remove-Item $env:LOCALAPPDATA\pipx -Recurse -Force
   ```

   Linux 나 macOS 에서는 다음 명령을 사용합니다:

   ```bash
   rm -rf ~/.local/pipx
   ```

4. **환경 변수 정리**: pipx 설치 과정에서 추가된 환경 변수를 정리합니다. 필요한 경우 시스템 환경 변수에서 pipx 관련 경로를 제거하세요.



---

## 예제

## 참조

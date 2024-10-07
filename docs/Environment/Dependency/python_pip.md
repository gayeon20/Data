---
title: "[] "
excerpt: ""
categories:
  - Python
tags:
  - Python
  - Python-Environment
  - Python-Dependency
last_modified_at: 2024-04-11T15:11:37+09:00
link: ""
상위 항목: "[[]]"
---

## [Python] Pip [(개발 문서)]()

### 상위 항목

#### [[python_setting|Setting]]

### 1. 설치

> [!info] requirement.txt
> - `requirement.txt` 는 가상 환경 (venv) 이나 현재 python 설치된 패키지와 그 버전을 목록으로 작성한 파일이다.
>
> ![requirement 예시](requirement_1.png)
>
> ```bash
> pip freeze > requirements.txt
> ```
>
> - 위 명령어로 현재 설치된 `pip` 패키지들의 `requirements.txt` 파일을 생성할 수 있다.
>
> > @file 형식으로 저장될 경우
> > `pip list --format=freeze > requirements.txt`
> > 명령어를 사용할 수 있다.

```bash
# Python Package 설치
pip install [Package name]

# 여러 Package 설치
pip install [package1] [package2] ...

# 사용자 권한 설치
pip install [package name] --user

# Requirements.txt 파일 활용
pip install -r requirements.txt
```

설치되지 않는 패키지는 넘기고 나머지만 설치하고 싶을 경우 (linux, centos) `cat requirements.txt | xargs -n 1 pip install` 명령어를 사용할 수 있다.

```bash
# Python Package 오프라인 다운로드
pip download -d [Destination/] [Package name]

## Requirements.txt 파일 활용
pip download -r requirements.txt -d [Destination/]
```

```bash
# Python Package 오프라인 설치
pip install --no-index --find-links=[Destination/] [Package name]

## Requirements.txt 파일 활용
pip install --no-index --find-links=[Destination/] -r requirements.txt
```

### 2. 관리

```bash
# 현재 설치된 Package List 확인
pip list

# 오래된 버전을 나열하고 업그레이드 가능한 최신 버전 목록 표시
pip list --outdated

# 설치된 Package 세부 사항 확인
pip show [Package name]
```

```bash
# pip 버전 확인
pip --version

# pip 업그레이드
python -m pip install —upgrade pip # Windows
pip install -U pip

# pip 다운그레이드 (오류 발생 시)
python -m pip install pip==[Version]
```

### 3. 삭제

```bash
# Python Package 삭제
pip uninstall [Package name]

# Package 검색 (PyPI)
# 이름과 내용을 요약하여 출력
pip search "query"
```

### 오류

#### 1) The script `<Package>` is installed in '/home/`<user>`/.local/bin' which is not on PATH.

```bash
 export PATH="/usr/local/bin:$PATH"
```

`.bash_profile` 또는 `~/.bashrc` 파일에 다음 줄을 추가해야 한다.

```bash
source ~/.bash_profile
```

이후 변경 내용을 적용하면 된다. (명령어 수행 혹은 터미널 재시작)

```bash
echo $PATH
```

위 명령어로 등록 여부를 확인할 수 있다.

### 2) error: externally-managed-environment" every time I use pip 3?
> [python - How do I solve "error: externally-managed-environment" every time I use pip 3? - Stack Overflow](https://stackoverflow.com/questions/75608323/how-do-i-solve-error-externally-managed-environment-every-time-i-use-pip-3)
> Python 3.11에서 발생, 가상 환경 없이 설치하는 것을 경고

#### (1) `--break-system-packages`
- `pip` 명령어에 `--break-system-packages` 옵션을 설정하여 경고를 무시할 수 있습니다.

#### (2) `~/.config/pip/pip.conf`
- config 파일을 아래와 같이 작성하여 경고를 무시할 수 있습니다.
```ini
[global]
break-system-packages = true
```

#### (3) EXTERNALLY-MANAGED 삭제
- 관련 파일을 삭제하여 경고 기능을 제거할 수 있습니다.
```bash
sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED
```


### 예제

### 참조

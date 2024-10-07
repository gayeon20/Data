---
title: "[Poetry] 명령어 (Command)"
excerpt: Poetry의 명령어에 대한 문서
categories:
  - Python
tags:
  - Python
  - Poetry
last_modified_at: 2024-04-11T15:11:38+09:00
link: 
상위 항목: "[[python_poetry|Poetry]]"
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

---

## 1. 패키지

### 1) 추가 (Add)

```bash
# 개발환경에서 필요한 패키지 설치
# (옵션) --dev or -D 옵션을 통해 Dev 환경에서만 사용할 패키지를 추가
poetry add --group dev pytest
poetry add -D pandas

# 버전 명시
poetry add pandas@^1.0.0  # 1.0.0 이상, 2.0.0 미만
poetry add "pandas~1.0.0"  # 1.0.0 이상, 1.1.0 미만
poetry add pandas==1.0.0  # 버전을 명확히 명시
poetry add "pandas>=1.0.0"  # 해당하는 버전 이상(상한x)
poetry add pandas@latest  # 최신 버전

# 최신버전을 설치
poetry add django@latest

# 깃 저장소에 있는 패키지 설치
poetry add git+https://github.com/django/django.git

# 깃 저장소의 패키지에서 브랜치를 지정
poetry add git+https://github.com/django/django.git#stable/2.2.x

# 로컬에 디렉토리의 파일로 설치하기
poetry add ./my-package/
poetry add ./my-package/dist/my-package-0.1.0.tar.gz
poetry add ./my-package/dist/my-package-0.1.0.whl
```

### 2) 삭제 (Remove)

```bash
poetry remove pendulum
poetry remove mkdocs --group docs  # 특정 그룹에 속한 패키지 삭제
```

### 3) 업데이트 (Update)

```bash
# 패키지 업데이트
poetry update
# 하나씩 지정해서 업데이트도 가능
poetry update requests toml
# 업데이트는 하지 않고 poetry.lock 만 업데이트
poerty update --lock
```

### 4) 조회 (Show)

```bash
# 설치된 모든 패키지를 보여준다.
poetry show

# 개발환경용 제외하고 보여준다.
poetry show --no-dev

# 특정패키지를 지정하면 상세내용을 보여줍니다.
poetry show django

# 최신 버전을 보여준다.
poetry show --latest (-l)

# 업데이트를 해야하는 패키지들을 보여준다.
poetry show --outdate (-o)

# 의존성 트리를 보여준다.
poetry show --tree
```

### 5) 검색 (Search)

- 사용 가능한 패키지를 찾습니다.

```bash
poetry search pandas numpy
```

### 6) 설치 (Install)

```bash
# poetry install으로 pyproject.toml에 저장된 내용에 기반해 라이브러리를 설치
poetry install

# (옵션) 개발환경의 라이브러리는 빼고 설치
poetry install --no-dev

# (옵션) 캐시를 저장하지 않습니다.
poetry install --no-cache
```

### 7) 추출 (Export)

- lock 파일을 사용해서 다른 의존성 포맷으로 변경할 수 있다.

```bash
poetry export -f requirements.txt > requirements.txt
```

```bash
poetry export --without-hashes --format=requirements.txt > requirements.txt
```

- `--without-hashes` 로 hash 를 제외할 수 있습니다.
- `--without dev` 로 개발용 라이브러리를 제외할 수 있습니다.

## 2. 프로젝트

### 1) 설정 (Config)

- poetry 관련 설정을 변경할 수 있습니다.

```bash
# 설정보기
poetry config --list
# 설정법
poetry config [options] [setting-key] [setting-value1] … [setting-valueN]
```

```
cache-dir = "<경로>"
experimental.system-git-client = false
installer.max-workers = null
installer.modern-installation = true
installer.no-binary = null
installer.parallel = true
keyring.enabled = true
solver.lazy-wheel = true
virtualenvs.create = true
virtualenvs.in-project = true
virtualenvs.options.always-copy = false
virtualenvs.options.no-pip = false
virtualenvs.options.no-setuptools = false
virtualenvs.options.system-site-packages = false
virtualenvs.path = ".venv"
virtualenvs.prefer-active-python = false
virtualenvs.prompt = "{project_name}-py{python_version}"
warnings.export = true
```

- `virtualenvs.in-project`: 가상 환경을 프로젝트 내에 생성합니다.
- `virtualenvs.path`: 생성할 가상 환경 경로를 지정합니다.

### 2) 프로젝트 생성 (New)

```bash
# path에 파이썬 프로젝트를 생성
poetry new <path>

# poetry new 로 생성한 프로젝트의 구조
.
├── poetry_test
│   └── __init__.py
├── pyproject.toml
├── README.md
└── tests
    └── __init__.py
```

## 2. 가상 환경

### 1) info

- 현재 활성화된 가상 환경에 대한 정보를 얻습니다.

```bash
poetry env info
```

### 2) use

- Poetry 로 가상 환경을 생성합니다.

```bash
# 가상환경 생성
poetry env use </full/path/to/python>

# 만약 파이썬이 PATH에 잡혀있다면, 다음 명령어만 입력하면 가상환경을 생성합니다.
poetry env use python3
```

### 3) list

- 가상 환경 리스트를 출력합니다.

```bash
poetry env list
```

### 4) remove

- 가상환경을 삭제합니다.

```bash
poetry env remove poetry-test-4oQtH5dM-py3.8
```

### 5) 명령어 실행 (Run)

- virtualenv 내에 주어진 명령을 실행합니다.

```bash
poetry run python -V
```

---

## 예제

## 참조

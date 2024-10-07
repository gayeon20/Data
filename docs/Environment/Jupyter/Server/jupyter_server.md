---
title: "[] "
excerpt: ""
categories: - 
tags: - 
last_modified_at: 2024-04-11T15:12:28+09:00
link: ""
상위 항목: "[[]]"
---

## [Jupyter] Server [(개발 문서)](https://jupyter-server.readthedocs.io/en/latest/index.html)

> [!info] 파일 경로
>
> ```bash
> # 생성 명령어
> jupyter server --generate-config
> ```
>
> - Windows: `C:\Users\USERNAME\.jupyter\jupyter_server_config.py`
> - OS X: `/Users/USERNAME/.jupyter/jupyter_server_config.py`
> - Linux: `/home/USERNAME/.jupyter/jupyter_server_config.py

### 상위 항목

#### [[jupyter_home|Jupyter]]

### 하위 항목

#### [[jupyter_hub|Hub]]

### 1. 비밀번호 설정

- 간단한 단일 비밀번호로 Jupyter 서버를 보호할 수 있다. 노트북 5.0 부터는 자동으로 설정할 수 있다.
- 비밀번호를 수동으로 설정하려면 `jupyter_server_config.py` 에서 `ServerApp.password` 설정을 구성하면 된다.

#### 1) 자동 설정

- 노트북 5.3 버전부터 첫 로그인할 때 토큰 사용해서 로그인하면 사용자 인터페이스에서 비밀번호 설정할 기회를 준다.
- 현재 토큰과 새 비밀번호를 묻는 양식이 나타나고, 이 둘을 입력한 후 ' 로그인 및 새 비밀번호 설정 ' 을 클릭해야 한다.
- 다음에 로그인할 때는 이제 새로 설정한 비밀번호를 사용할 수 있게 된다. 그렇지 않으면 명령줄에서 비밀번호 설정 절차를 따라야 한다.
- 첫 로그인 시 비밀번호를 변경하는 기능은 `--ServerApp.allow_password_change=False` 설정해서 비활성화할 수 있다.
- 노트북 버전 5.0 부터는 서버의 비밀번호를 한 번의 명령으로 입력하고 저장할 수 있다. `jupyter server password` 명령을 실행하면 비밀번호를 입력하라는 메시지가 나오고, 입력한 비밀번호의 해시 값을 `jupyter_server_config.json` 에 저장한다.

#### 2) Hashed Password 사용

```python
from jupyter_server.auth import passwd
passwd()
```

- 준비한 Hashed Password 를 사용하려면 `jupyter_server.auth.passwd()` 를 사용한다.
- `passwd()` 함수는 인자 없이 호출될 때, 위 코드 스니펫처럼 비밀번호를 입력하고 확인하라는 메시지를 표시한다.
- 함수에는 `passwd('mypassword')` 처럼 문자열 인자를 전달할 수도 있지만, IPython 세션 안에서 문자열 인자를 전달하는 것은 권장하지 않는다. 그 이유는 전달한 문자열이 입력 이력에 저장되기 때문이다.

```python
c.ServerApp.password = u'sha1:67c9e60bb8b6:9ffede0825894254b2e042ea597d771089e11aed'
```

- 해시된 비밀번호를 `jupyter_server_config.py` 에 추가할 수 있다. 이 파일의 기본 위치는 홈 디렉토리 안의 Jupyter 폴더인 `~/.jupyter` 다.
- 자동 비밀번호 설정은 해시를 `jupyter_server_config.json` 에 저장하는 반면, 이 방법은 해시를 `jupyter_server_config.py` 에 저장한다. `.json` 설정 옵션은 `.py` 보다 우선시되므로, Json 파일에 비밀번호가 설정되어 있다면 수동 비밀번호가 효력을 발휘하지 않을 수 있다.

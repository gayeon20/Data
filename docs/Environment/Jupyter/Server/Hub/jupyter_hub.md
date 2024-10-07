---
title: "[] "
excerpt: ""
categories: - 
tags: - 
last_modified_at: 2024-04-11T15:12:48+09:00
link: ""
상위 항목: "[[]]"
---

## [Server] JupyterHub [(개발 문서)]()

- 간단한 설명

### 상위 항목

#### [[jupyter_server|Jupyter Server]]

### 하위 항목

#### [[jupyterhub_kubernetes|On Kubernetes]]

### 1. 실행

```bash
jupyterhub
```

- `jupyterhub` 로 서버를 실행할 수 있다.

```bash
jupyterhub -f /path/to/jupyterhub_config.py
```

- 특정 경로에 있는 설정 파일을 사용하여 서버를 실행하려면 위 명령어를 사용한다.

```bash
jupyterhub --Spawner.notebook_dir='~/assignments'
```

- 이외에 특정 옵션 (예: `Spawner.notebook_dir`) 을 설정하면서 실행하려면 위처럼 `--` 를 붙여서 실행한다.

### 2. 설정

```bash
jupyterhub --generate-config
```

- 위 명령어를 실행하면 설정 파일이 생성된다.

#### 1) 네트워크 설정

```python
c.JupyterHub.ip = '192.168.1.2'
c.JupyterHub.port = 443
```

- 위 옵션을 설정하여 IP, Port 를 설정할 수 있다.

##### (1) Proxy 설정: Docker - Apache

```python
c.JupyterHub.bind_url = 'http://:8000/jhub/'
```

- 허브는 대부분 자체 호스트 네임에서 실행된다. 그렇지 않은 경우 (예: 허브가 리버스 프록시되어 `https://proxy.example.org/jupyter/` 같은 URL 에 노출되는 경우) JupyterHub 에 서비스의 기본 URL 을 알려주어야 한다.
- 이러한 경우 구성에서 `c.JupyterHub.bind_url` 을 위와 같이 작성하면 Proxy 가 적용된다.

```yml
services:
  jupyterhub:
    image: jupyterhub/jupyterhub:latest
    volumes:
      - ./jupyterhub/jupyterhub_config.py:/srv/jupyterhub/jupyterhub_config.py
    ports:
      - "8000:8000"
    restart: unless-stopped
    networks:
      - apache2
  apache2:
    image: httpd:latest
    volumes:
      - ./apache2/httpd.conf:/usr/local/apache2/conf/httpd.conf
    ports:
      - "80:80"
    restart: unless-stopped
    networks:
      - apache2
    depends_on:
      - jupyterhub

networks:
  apache2:
    driver: bridge
```

- `docker-compose.yml` 파일은 위와 같이 작성했다.

```conf
<VirtualHost *:80>
    ProxyPreserveHost On
    
    ProxyPass /jupyterhub/ http://jupyterhub:8000/jupyterhub/
    ProxyPassReverse /jupyterhub/ http://jupyterhub:8000/jupyterhub/
</VirtualHost>
```

- Apache 설정 파일은 위와 같이 작성했다.

##### (2) 원격 & 컨테이너 설정 (수정 필요)

- 허브 서비스는 기본적으로 로컬 호스트 (포트 8081) 에서만 수신 대기한다. 프록시와 모든 스포너 모두에서 허브에 액세스할 수 있어야 한다.
- 프록시 또는 스포너가 원격이거나 컨테이너에 격리되어 있는 경우 허브는 액세스 가능한 IP 에서 수신 대기해야 한다.

```python
c.JupyterHub.hub_ip = '10.0.1.4'
c.JupyterHub.hub_port = 54321
```

- `c.JupyterHub.hub_connect_ip` 설정은 다른 서비스가 허브에 연결할 때 사용해야 하는 IP 주소 또는 호스트 이름이다.

```python
c.JupyterHub.hub_ip = '0.0.0.0'  # listen on all interfaces
c.JupyterHub.hub_connect_ip = '10.0.1.4'  # IP as seen on the docker network. Can also be a hostname.
```

- 예를 들어 docker 에 대한 일반적인 구성은 위와 같다.

#### 1) 기본 프로그램 설정

```python
c.Spawner.default_url = '/lab'
```

- `jupyterhub_config.py` 파일에서 `c.Spawner.default_url` 을 `'/lab'` 로 할당하면 Jupyter Lab 이 된다.
- 이외에는 Jupyter Notebook 이 기본 프로그램이 된다.

#### 2) 사용자 설정

- 사용자 생성은 터미널에서 Linux 의 `useradd` 명령어 등으로 직접 생성하면 된다.

```python
c.Authenticator.admin_users = {'admin'}
```

- 위 `c.Authenticator.admin_users` 에 속한 사용자는 root 권한을 얻는다.
- `allowed_users` 에서 사용자를 추가하거나 제거할 수 있으며, 다른 사용자를 대신하여 서버 중지 및 재시작 등의 작업을 수행할 수 있다.
- `admin_users` 의 사용자를 `allowed_users` 에 추가하지 않은 경우 자동으로 추가된다.

```python
c.Authenticator.allowed_users = {'user1', 'user2', 'user3'}
```

- `c.Authenticator.allowed_users` 를 작성하면 해당 사용자들만 로그인이 가능하다.
- 작성하지 않으면 모든 사용자가 접근할 수 있다.

```python
c.PAMAuthenticator.admin_groups = {'wheel'}
```

- `admin_users` 의 전체 권한 대신 필요한 범위만 사용자 또는 그룹에 역할 할당이 가능하다.
- `admin_groups` 옵션을 제공하고 사용자 그룹에 따라 관리자 상태를 설정할 수 있는 PAMAuthenticator 를 사용한다. 예를 들어 `wheel` 그룹에 속한 모든 사용자를 관리자로 설정할 수 있다
- `JupyterHub.admin_access` 를 활성화하면 관리자가 다른 사용자로 로그인할 수 있게 된다. (디버깅 용도, 설정한다면 사용자에게 알리는 것이 예의이다.)

####) OTP 설정

```python
c.Authenticator.request_otp = True
```

- `c.Authenticator.request_otp` 설정을 켜면 OTP 입력을 요구할 수 있다.

```python
c.Authenticator.otp_prompt = 'Google Authenticator:'
```

- 기본 설정인 `OTP:` 외에도 다른 [`otp_prompt`](https://jupyterhub.readthedocs.io/en/latest/tutorial/getting-started/authenticators-users-basics.html#use-localauthenticator-to-create-system-users) 를 사용할 수 있다.

####) Proxy 설정

### 2. Kubernetes

<https://z2jh.jupyter.org/en/stable/index.html>
<https://swalloow.github.io/jupyterhub-on-kubernetes/>
<https://velog.io/>@tkfka/JupyterHub%EB%A5%BC-Kubernetes%EC%97%90-Helm%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0
<https://justkode.kr/data-engineering/jupyterhub-on-k8s/>
<https://right1203.tistory.com/29>

### 오류

#### 1) Spawn failed

- Jupyter Notebook 을 설치했는지 다시 한번 확인하기

### 참조

<https://metamath1.github.io/2018/12/24/jupyterhub.html>
<https://tljh.jupyter.org/en/latest/howto/user-env/user-environment.html>

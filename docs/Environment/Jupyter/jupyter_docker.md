---
title: "[] "
excerpt: ""
categories: - 
tags: - 
last_modified_at: 2024-04-11T15:11:36+09:00
link: ""
상위 항목: "[[]]"
---

## [Jupyter] Docker [(개발 문서)](https://jupyter-docker-stacks.readthedocs.io/en/latest/)

### 상위 항목

#### [[jupyter_home|Jupyter]]

### 하위 항목

#### [[]]

### 1. Jupyter Frontend

- Docker Container 를 생성할 때 `DOCKER_STACKS_JUPYTER_CMD=notebook` 와 같이 `DOCKER_STACKS_JUPYTER_CMD` 환경 변수를 전달하여 선택할 수 있다.

### 2. 종류

<img src="https://jupyter-docker-stacks.readthedocs.io/en/latest/_images/inherit.svg" style="width: 800px" />

#### 1) Docker-stacks [(Github)](https://github.com/jupyter/docker-stacks/tree/main/images/docker-stacks-foundation)

- `tini` 및 컨테이너 진입점으로 `start.sh` 스크립트 - 애플리케이션이 추가될 때 컨테이너에서 대체 명령을 실행하는 데 유용 (예: `ipython`, `jupyter kernelgateway`, `jupyter lab`).
- 지정된 디렉터리에서 파일을 소싱/실행할 수 있는 `run-hooks.sh` 스크립트.
- 비밀번호 없는 sudo 를 위한 옵션
- `bzip2`, `ca-certificates`, `locales` 과 같은 일반적인 시스템 라이브러리
- 외부 파일 다운로드를 위한 `wget`
- 사전 설치된 과학 컴퓨팅 패키지 없음

#### 2) Base [(Github)](https://github.com/jupyter/docker-stacks/tree/main/images/base-notebook) (`jupyter/docker-stacks-foundation` 파생)

> `jupyter/base-notebook` 은 JupyterLab, Jupyter Notebook, JupyterHub, NBClassic 과 같은 기본 Jupyter 애플리케이션을 추가하고 `jupyter/docker-stacks-foundation` 이외의 다른 모든 스택의 기초 역할을 한다.

- LaTeX 지원 없이 PDF 로 노트북을 저장하는 등 최소한으로 기능하는 서버
- `notebook`, `jupyterhub`, 및 ` jupyterlab` 패키지
- 기본 명령으로 사용되는 `start-notebook.py` 스크립트
- JupyterHub 에서 컨테이너를 시작하는 데 유용한 `start-singleuser.py` 스크립트
- 자체 서명된 HTTPS 인증서에 대한 옵션

> [!warning]
> `jupyter/base-notebook` 에는 이전 버전과의 호환성을 유지하기 위해 `start-notebook.sh` 및 `start-singleuser.sh` 파일도 포함되어 있다. 이러한 파일을 명시적으로 참조하는 외부 구성은 `start-notebook.py` 및 `start-singleuser.py` 를 참조하도록 업데이트해야 한다. shim `.sh` 파일은 추후에 제거될 예정이다.

#### 3) Minimal [(Github)](https://github.com/jupyter/docker-stacks/tree/main/images/minimal-notebook) (`jupyter/base-notebook` 파생)

- [curl](https://curl.se/), [git](https://git-scm.com/), [nano](https://www.nano-editor.org/) (actually `nano-tiny`), [tzdata](https://www.iana.org/time-zones), [unzip](https://code.launchpad.net/ubuntu/+source/unzip), and [vi](https://www.vim.org/) (actually `vim-tiny`) 같은 흔히 쓰이는 유용한 유틸리티들
- 노트북 문서 변환을 위한 [TeX Live](https://www.tug.org/texlive/)

#### 4) R [(Github)](https://github.com/jupyter/docker-stacks/tree/main/images/r-notebook) (`jupyter/minimal-notebook` 파생)

- R 인터프리터와 기본 환경
- Jupyter 노트북에서 R 코드를 지원하는 [IRKernel](https://irkernel.github.io/)
- [conda-forge](https://conda-forge.org/feedstock-outputs/index.html) 에서 [tidyverse](https://www.tidyverse.org/) 패키지
- conda-forge 에서 [caret](https://topepo.github.io/caret/index.html), [crayon](https://cran.r-project.org/web/packages/crayon/index.html), [devtools](https://cran.r-project.org/web/packages/devtools/index.html), [forecast](https://cran.r-project.org/web/packages/forecast/index.html), [hexbin](https://cran.r-project.org/web/packages/hexbin/index.html), [htmltools](https://cran.r-project.org/web/packages/htmltools/index.html), [htmlwidgets](https://www.htmlwidgets.org/), [nycflights13](https://cran.r-project.org/web/packages/nycflights13/index.html), [randomforest](https://cran.r-project.org/web/packages/randomForest/index.html), [rcurl](https://cran.r-project.org/web/packages/RCurl/index.html), [rmarkdown](https://rmarkdown.rstudio.com/), [rodbc](https://cran.r-project.org/web/packages/RODBC/index.html), [rsqlite](https://cran.r-project.org/web/packages/RSQLite/index.html), [shiny](https://shiny.posit.co/), [tidymodels](https://www.tidymodels.org/), [unixodbc](https://www.unixodbc.org/) 패키지

#### 5) Julia [(Github)](https://github.com/jupyter/docker-stacks/tree/main/images/julia-notebook) (`jupyter-minimal-notebook` 파생)

- [Julia](https://julialang.org/) 컴파일러와 기본 환경
- Jupyter 노트북에서 Julia 코드를 지원하는 [IJulia](https://github.com/JuliaLang/IJulia.jl)
- [jupyter-pluto-proxy](https://github.com/yuvipanda/jupyter-pluto-proxy) 를 통해 접근 가능한 반응형 Julia 노트북 인터페이스인 [Pluto.jl](https://plutojl.org/)
- [HDF5](https://github.com/JuliaIO/HDF5.jl) 패키지

#### 6) Scipy [(Github)](https://github.com/jupyter/docker-stacks/tree/main/images/scipy-notebook)(`jupyter-minimal-notebook` 파생)

- [altair](https://altair-viz.github.io/), [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/), [bokeh](https://docs.bokeh.org/en/latest/), [bottleneck](https://bottleneck.readthedocs.io/en/latest/), [cloudpickle](https://github.com/cloudpipe/cloudpickle), [`conda-forge::blas=*=openblas`](https://www.openblas.net/), [cython](https://cython.org/), [dask](https://www.dask.org/), [dill](https://pypi.org/project/dill/), [h5py](https://www.h5py.org/), [jupyterlab-git](https://github.com/jupyterlab/jupyterlab-git), [matplotlib-base](https://matplotlib.org/), [numba](https://numba.pydata.org/), [numexpr](https://github.com/pydata/numexpr), [openpyxl](https://openpyxl.readthedocs.io/en/stable/), [pandas](https://pandas.pydata.org/), [patsy](https://patsy.readthedocs.io/en/latest/), [protobuf](https://protobuf.dev/getting-started/pythontutorial/), [pytables](https://www.pytables.org/), [scikit-image](https://scikit-image.org/), [scikit-learn](https://scikit-learn.org/stable/), [scipy](https://scipy.org/), [seaborn](https://seaborn.pydata.org/), [sqlalchemy](https://www.sqlalchemy.org/), [statsmodel](https://www.statsmodels.org/stable/index.html), [sympy](https://www.sympy.org/en/index.html), [widgetsnbextension](https://ipywidgets.readthedocs.io/en/latest/user_install.html#installing-in-classic-jupyter-notebook), [xlrd](https://www.python-excel.org/)
- Python 노트북에서 상호작용적인 시각화와 플롯을 위한 [ipympl](https://github.com/matplotlib/ipympl) and [ipywidgets](https://ipywidgets.readthedocs.io/en/stable/)
- 머신러닝 데이터셋을 시각화하기 위한 [Facets](https://github.com/PAIR-code/facets)

#### 7) Tensorflow (`jupyter-scipy-notebook` 파생)

- [tensorflow](https://www.tensorflow.org/) 머신 러닝 라이브러리

#### 8) Pytorch (`jupyter-scipy-notebook` 파생)

- [pytorch](https://pytorch.org/) 머신 러닝 라이브러리

#### 9. DataScience (`jupyter-scipy-notebook`, `jupyter-r-notebook`, `jupyter-julia-notebook` 파생)

- [rpy2](https://rpy2.github.io/doc/latest/html/index.html) package

#### 10) Pyspark (`jupyter-scipy-notebook` 파생)

- [Apache Spark](https://spark.apache.org/) with Hadoop binaries
- [grpcio-status](https://github.com/grpc/grpc/tree/master/src/python/grpcio_status)
- [grpcio](https://grpc.io/docs/languages/python/quickstart/)
- [pyarrow](https://arrow.apache.org/docs/python/)

#### 11) All-Spark (`jupyter-pyspark-notebook` 파생) (Python + R)

- [IRKernel](https://irkernel.github.io/) to support R code in Jupyter notebooks
- [rcurl](https://cran.r-project.org/web/packages/RCurl/index.html), [sparklyr](https://spark.rstudio.com/), [ggplot2](https://ggplot2.tidyverse.org/) packages

### 3. 설정

#### 1) 서버

##### (1) 비밀번호

```bash
docker run -it --rm -p 8888:8888 quay.io/jupyter/base-notebook start-notebook.py --PasswordIdentityProvider.hashed_password='argon2:$argon2id$v=19$m=10240,t=10,p=8$JdAN3fe9J45NvK/EPuGCvA$O/tbxglbwRpOFuBNTYrymAEH6370Q2z+eS1eF4GM6Do'
```

- Jupyter 서버를 기본 토큰 대신 `jupyter_server.auth.passwd()` 를 사용해 해시된 사용자 지정 비밀번호로 보호하려면 다음과 같이 실행할 수 있다 (이 해시는 'my-password' 비밀번호에 대해 생성된 것이다.)

##### (2) Base URL

```bash
docker run -it --rm -p 8888:8888 quay.io/jupyter/base-notebook \
    start-notebook.py --ServerApp.base_url=/customized/url/prefix/
```

- 원하는 url 을 입력하여 사용할 수 있다.

#### 2) 사용자

- `-e NB_USER=<username>` 옵션은 원하는 사용자 이름과 관련된 홈 폴더를 설정하는 데 사용된다. 기본값은 `jovyan` 이다. `NB_USER` 를 설정하면 `jovyan` 기본 사용자를 원하는 사용자로 변경하고, `/home/<username>` 에 생성된 새 홈 디렉토리에 대해 올바른 파일 권한이 부여되도록 한다. 이 옵션이 효력을 발휘하려면, 컨테이너를 `--user root` 와 함께 실행하고, 작업 디렉토리를 `-w "/home/<username>"` 로 설정하며, 환경 변수 `-e CHOWN_HOME=yes` 를 설정해야 한다. 이 설정을 통해 사용자는 컨테이너 내에서 원하는 사용자 이름으로 홈 디렉토리를 사용할 수 있으며, 해당 디렉토리에 대한 적절한 소유권과 권한이 설정된다.
- `-e NB_UID=<numeric uid>` - 시작 스크립트에 `${NB_USER}` 의 숫자 사용자 ID 를 주어진 값으로 바꾸도록 지시함. 기본값은 1000 임. 특정 소유권 권한을 가진 호스트 볼륨을 마운트할 때 유용함. 이 옵션이 효과를 발휘하려면 컨테이너를 `--user root` 로 실행해야 함. (사용자 ID 를 조정한 후 시작 스크립트가 `${NB_USER}` 로 `su` 함.) 대신, 현대적인 Docker 네이티브 옵션인 `--user` 와 `--group-add` 를 사용하는 것을 고려할 수 있음 - 이 섹션의 마지막 항목에서 더 자세한 내용을 참조. `--user` 와 `--group-add` 에 관한 항목을 참조함.
- `-e NB_GID=<numeric gid>` - 시작 스크립트에 `${NB_USER}` 의 기본 그룹을 `${NB_GID}` 로 변경하도록 지시함 (새 그룹은 `${NB_GROUP}` 이 정의된 경우 그 이름으로 추가됨. 그렇지 않으면 그룹 이름은 `${NB_USER}` 가 됨). 특정 그룹 권한을 가진 호스트 볼륨을 마운트할 때 유용함. 이 옵션이 효과를 발휘하려면 컨테이너를 `--user root` 로 실행해야 함. (그룹 ID 를 조정한 후 시작 스크립트가 `${NB_USER}` 로 `su` 함.) 대신, 현대적인 Docker 옵션인 `--user` 와 `--group-add` 를 사용하는 것을 고려할 수 있음. `--user` 와 `--group-add` 에 관한 항목을 참조함. 사용자는 보조 그룹 사용자 (gid 100) 에 추가되어 홈 디렉토리와 `/opt/conda` 에 대한 쓰기 권한을 부여받음. 사용자/그룹 로직을 오버라이드하는 경우, 이미지 내 파일을 수정하고 싶다면 사용자가 사용자 그룹에 계속 속하도록 해야 함.
- `-e NB_GROUP=<name>` - `${NB_GID}` 에 사용되는 이름으로, 기본값은 `${NB_USER}` 임. 이 그룹 이름은 `${NB_GID}` 가 지정된 경우에만 사용되며 완전히 선택적임: 오직 코스메틱 효과만 있음.
- `--user 5000 --group-add users` - 특정 사용자 ID 로 컨테이너를 시작하고 해당 사용자를 사용자 그룹에 추가하여 기본 홈 디렉토리와 `/opt/conda` 에서 파일을 수정할 수 있게 함. 이 인자들을 `${NB_UID}` 와 `${NB_GID}` 를 설정하는 대안으로 사용할 수 있음.

#### 3) 접근 권한

- `-e NB_UMASK=<umask>` - 기본값인 022 와 다른 umask 값을 사용하도록 Jupyter 를 구성함. 예를 들어, umask 를 002 로 설정하면 새 파일이 소유자만이 아닌 그룹 구성원에 의해 읽고 쓸 수 있게 됨. umask 와 다양한 필요에 적합한 값에 대한 심층 설명은 위키피디아 기사를 참조. 대부분의 사용 사례에는 기본 umask 값이 충분하지만, 요구 사항에 맞게 NB_UMASK 값을 설정할 수 있음.

> `NB_UMASK` 가 설정되면 Jupyter 프로세스 자체에만 적용됨 - `run-hooks.sh` 동안 생성된 추가 파일에 대해 umask 를 설정하는 데 사용할 수 없음. 예를 들어, `pip` 또는 `conda` 를 통해 생성된 경우. 이러한 경우에 umask 를 설정해야 하는 경우, 각 명령에 대해 umask 값을 설정해야 함.

- `-e CHOWN_HOME=yes` - 시작 스크립트에 `${NB_USER}` 홈 디렉토리의 소유자와 그룹을 현재 `${NB_UID}` 와 `${NB_GID}` 값으로 변경하도록 지시함. 이 변경은 사용자 홈 디렉토리가 아래 설명된 대로 `-v` 를 사용해 호스트에서 마운트되었을 경우에도 적용됨. 기본적으로 변경은 재귀적으로 적용되지 않음. CHOWN_HOME_OPTS 를 설정하여 chown 동작을 수정할 수 있음 (예: `-e CHOWN_HOME_OPTS='-R'`).
- `-e CHOWN_EXTRA="<some dir>,<some other dir>"` - 시작 스크립트에 각각 쉼표로 구분된 컨테이너 디렉토리의 소유자와 그룹을 현재 `${NB_UID}` 와 `${NB_GID}` 값으로 변경하도록 지시함. 기본적으로 변경은 재귀적으로 적용되지 않음. CHOWN_EXTRA_OPTS 를 설정하여 chown 동작을 수정할 수 있음 (예: `-e CHOWN_EXTRA_OPTS='-R'`).
- `-e GRANT_SUDO=yes` - 시작 스크립트에 NB_USER 사용자에게 비밀번호 없는 sudo 권한을 부여하도록 지시함. 사용자가 추가 패키지를 conda 또는 pip 로 설치하는 것을 허용하려면 이 옵션이 필요하지 않음. 이 옵션은 `${NB_USER}` 에게 apt 를 사용하여 OS 패키지를 설치하거나 컨테이너 내의 다른 root 소유 파일을 수정할 수 있는 능력을 부여하고 싶은 경우에 유용함. 이 옵션이 효과를 발휘하려면 컨테이너를 `--user root` 로 실행해야 함. (start-notebook.py 스크립트가 `${NB_USER}` 를 sudoers 에 추가한 후 `${NB_USER}` 로 `su` 함.) sudo 를 활성화해야 하는 경우는 사용자를 신뢰하거나 컨테이너가 격리된 호스트에서 실행될 때만 함.

#### 4) 실행 설정

- `-e GEN_CERT=yes` - 시작 스크립트에 자체 서명 SSL 인증서를 생성하도록 지시함. Jupyter 서버가 암호화된 HTTPS 연결을 수락하도록 구성함.
- `-e DOCKER_STACKS_JUPYTER_CMD=<jupyter command>` - 시작 스크립트에 기본 `jupyter lab` 명령 대신 `jupyter ${DOCKER_STACKS_JUPYTER_CMD}` 를 실행하도록 지시함. 사용 가능한 옵션에 대해서는 클래식 노트북으로 돌아가기 또는 다른 시작 명령 사용하기를 참조. 이 설정은 명령줄 매개변수를 변경하는 것보다 환경 변수를 설정하는 것이 더 간단한 컨테이너 오케스트레이션 환경에서 유용함.
- `-e RESTARTABLE=yes` - Jupyter 를 반복적으로 실행하여 Jupyter 를 종료해도 컨테이너가 종료되지 않도록 함. Jupyter 를 재시작해야 하는 확장 프로그램을 설치할 때 유용할 수 있음.
- `-v /some/host/folder/for/work:/home/jovyan/work` - 호스트 기계 디렉토리를 컨테이너 내의 폴더로 마운트함. 이 구성은 컨테이너가 파괴된 후에도 노트북과 기타 작업을 보존하는 데 유용함. 호스트 디렉토리에 컨테이너 내 노트북 사용자 또는 그룹 (NB_UID 또는 NB_GID) 에 쓰기 권한을 부여해야 함 (예: `sudo chown 1000 /some/host/folder/for/work`).
- `-e JUPYTER_ENV_VARS_TO_UNSET=ADMIN_SECRET_1,ADMIN_SECRET_2` - 기본 시작 스크립트에서 지정된 환경 변수를 해제함. 변수는 후크가 실행된 후, 스타트업 스크립트에 제공된 명령이 실행되기 전에 해제됨.
- `-e NOTEBOOK_ARGS="--log-level='DEBUG' --dev-mode"` - jupyter 명령에 추가할 사용자 정의 옵션을 추가함. 이 방법을 통해 사용자는 jupyter 서브커맨드에서 지원하는 모든 옵션을 사용할 수 있음.
- `-e JUPYTER_PORT=8117` - 컨테이너에서 Jupyter 가 사용하는 포트를 `${JUPYTER_PORT}` 환경 변수의 값으로 변경함. 스웜 모드에서 여러 인스턴스의 Jupyter 를 실행하고 각 인스턴스마다 다른 포트를 사용하고 싶을 때 유용할 수 있음.

#### 5) Hooks 설정

- 컨테이너 환경을 더 사용자화하려면, 아래 경로에 소스로 추가될 셸 스크립트 (`*.sh`) 나 실행될 실행 파일 (`chmod +x`) 을 추가할 수 있다.
- `/usr/local/bin/start-notebook.d/` - 위에 언급된 표준 옵션들이 적용되기 전에 처리됨
- `/usr/local/bin/before-notebook.d/` - 위에 언급된 모든 표준 옵션이 적용된 후, 서버가 시작되기 바로 전에 처리됨

> 실행 세부 정보에 대해서는 `run-hooks.sh` 스크립트와 실행을 위해 `start.sh` 스크립트에서 어떻게 사용되는지를 [참조](https://github.com/jupyter/docker-stacks/blob/main/images/docker-stacks-foundation/run-hooks.sh) 하기

#### 6) SSL 인증 설정

```bash
docker run -it --rm -p 8888:8888 \
    -v /some/host/folder:/etc/ssl/notebook \
    quay.io/jupyter/base-notebook \
    start-notebook.py \
    --ServerApp.keyfile=/etc/ssl/notebook/notebook.key \
    --ServerApp.certfile=/etc/ssl/notebook/notebook.crt
```

- SSL 키와 인증서 파일을 컨테이너에 마운트하고 Jupyter 서버를 구성하여 HTTPS 연결을 수락하도록 할 수 있다. 예를 들어, `notebook.key` 와 `notebook.crt` 를 포함하는 호스트 폴더를 마운트하고 사용하기 위해 다음과 같이 실행할 수 있다.

```bash
docker run -it --rm -p 8888:8888 \
    -v /some/host/folder/notebook.pem:/etc/ssl/notebook.pem \
    quay.io/jupyter/base-notebook \
    start-notebook.py \
    --ServerApp.certfile=/etc/ssl/notebook.pem
```

- 키와 인증서를 모두 포함하는 단일 PEM 파일을 마운트할 수도 있다. 어느 경우든, Jupyter 서버는 키와 인증서가 base64 로 인코딩된 텍스트 파일이길 기대함. 인증서 파일이나 PEM 은 하나 이상의 인증서 (예: 서버, 중간, 루트) 를 포함할 수 있음.
- 공개적으로 볼 수 있는 도메인에서 이 스택을 실행할 때 Let's Encrypt 인증서를 사용하는 방법에 대한 정보를 제공하는 `docker-stacks/examples`.
- 이 Docker 이미지가 자체 서명된 인증서를 생성하는 방법에 대한 `jupyter_server_config.py` 파일.
- 일반적으로 공개 서버를 보호하는 최선의 관행에 대한 Jupyter 서버 문서.

#### 7) Frontend

- Jupyter 서버를 기반으로 구축된 JupyterLab 은 이제 스택의 모든 이미지에 대한 기본값이다. 그러나 클래식 노트북으로 돌아가거나 다른 시작 명령을 사용하는 것이 여전히 가능하다. 이를 달성하기 위해 컨테이너 시작 시 환경 변수 `DOCKER_STACKS_JUPYTER_CMD` 를 설정할 수 있다.
- Jupyter Notebook v7 부터는 백엔드로 `jupyter-server` 가 사용된다.

|`DOCKER_STACKS_JUPYTER_CMD`|Frontend|
|---|---|
|`lab` (default)|JupyterLab|
|`notebook`|Jupyter Notebook|
|`nbclassic`|NbClassic|
|`server`|None|
|`retro`*|RetroLab|

#### 8) `start.sh`

- `start-notebook.py` 스크립트의 대부분의 구성 옵션은 컨테이너에 제공된 명령어 전에 자동으로 실행되는 내부 `start.sh` 스크립트에 의해 처리된다. 이는 모든 이러한 기능을 활용하는 임의의 명령어를 지정할 수 있게 한다. 예를 들어, 컨테이너에서 텍스트 기반 ipython 콘솔을 실행하려면 다음을 수행한다.

```
docker run -it --rm quay.io/jupyter/base-notebook ipython
```

- 이 스크립트는 이 이미지에서 새로운 Dockerfile 을 파생시키고 `jupyter console`, `jupyter kernelgateway` 등과 같은 서브커맨드를 가진 추가 Jupyter 애플리케이션을 설치할 때 유용하다.

#### 9) Conda

기본 Python 3.x Conda 환경은 `/opt/conda` 에 위치한다. `/opt/conda/bin` 디렉토리는 기본 jovyan 사용자의 `${PATH}` 에 포함되어 있다. 이 디렉토리는 `sudo` 를 사용하여 실행할 때도 바이너리를 찾는 데 검색됨 (`sudo my_binary` 는 `/opt/conda/bin/` 에서 `my_binary` 를 찾음).

jovyan 사용자는 `/opt/conda` 디렉토리에 대한 전체 읽기/쓰기 권한을 가지고 있다. 추가 권한 없이 새 패키지를 설치하기 위해 mamba, pip, 또는 conda(묌은 mamba 사용을 권장) 를 사용할 수 있다.

> [!NOTE] 기본 (python 3.x) 환경에 패키지를 설치하고 설치 후 정리하기
>
> ```bash
> mamba install --yes some-package && \
> mamba clean --all -f -y && \
> fix-permissions "${CONDA_DIR}" && \
> fix-permissions "/home/${NB_USER}"
> ```
>
> ```bash
> pip install --no-cache-dir some-package && \
> fix-permissions "${CONDA_DIR}" && \
> fix-permissions "/home/${NB_USER}"
> ```
>
> ```bash
> conda install --yes some-package && \
> conda clean --all -f -y && \
> fix-permissions "${CONDA_DIR}" && \
> fix-permissions "/home/${NB_USER}"
> ```

> [!NOTE] Channel
> - Conda 는 기본적으로 오직 conda-forge 채널만 사용하도록 구성되어 있다. 하지만, 설치 명령에서 기본 채널을 덮어쓰는 일회성 방법이나 mamba 를 다른 채널을 사용하도록 구성하는 방법을 통해 대체 채널을 사용할 수 있다. 아래 예시는 conda-forge 대신 anaconda 기본 채널을 사용하여 패키지를 설치하는 방법을 보여준다.
>
> ```
> # 기본 채널을 사용하여 패키지 설치
> mamba install --channel defaults humanize
> ```
>
> ```
> # conda에 기본 채널을 리스트 상단에 추가하도록 구성
> conda config --system --prepend channels defaults
> ```
>
> ```
> # 패키지 설치
> mamba install --yes humanize && \
> mamba clean --all -f -y && \
> fix-permissions "${CONDA_DIR}" && \
> fix-permissions "/home/${NB_USER}"
> ```

### 4. Spark [(Spark 사이트 문서)](https://spark.apache.org/docs/latest/configuration.html)

- `-p 4040:4040` - `jupyter/pyspark-notebook` 및 `jupyter/all-spark-notebook` 이미지는 SparkUI(Spark 모니터링 및 계측 UI) 를 기본 포트 4040 에서 열기 때문에, 이 옵션은 도커 컨테이너 내의 4040 포트를 호스트 기계의 4040 포트에 매핑한다.

> [!info]
> - 생성되는 모든 새 스파크 컨텍스트는 증가하는 포트 (즉, 4040, 4041, 4042 등) 에 배치되며, 여러 포트를 열어야 할 필요가 있을 수 있다.
> - 예시: `docker run --detach -p 8888:8888 -p 4040:4040 -p 4041:4041 quay.io/jupyter/pyspark-notebook`

#### 1) IPython low-level output capture and forward

- Spark 이미지 (`pyspark-notebook` 및 `all-spark-notebook`) 는 IPython 저수준 출력 캡처 및 전달 기능을 시스템 전체에서 비활성화하도록 구성되었다.
- 이 선택의 이유는 Spark 로그가 매우 자세할 수 있으며, 특히 Ivy 를 사용하여 추가 jars 를 로드할 때 시작 시에 그렇다. 이러한 로그는 여전히 사용 가능하지만 컨테이너의 로그에서만 볼 수 있다.

```python
c.IPKernelApp.capture_fd_output = True
```

- 노트북에서 이러한 로그를 보려면, 사용자 레벨의 IPython 커널 프로필에서 구성을 덮어쓸 수 있다. 그렇게 하려면, `~/.ipython/profile_default/ipython_kernel_config.py` 에서 다음 줄의 주석 처리를 해제하고 커널을 재시작해야 한다.

```
ipython profile create
# [ProfileCreate] 기본 설정 파일 생성: '/home/jovyan/.ipython/profile_default/ipython_config.py'
# [ProfileCreate] 기본 설정 파일 생성: '/home/jovyan/.ipython/profile_default/ipython_kernel_config.py'
```

- IPython 프로필이 없다면, 새로운 프로필을 시작할 수 있다.

#### 2) Spark 버전 변경 [(Spark Download)](https://spark.apache.org/downloads.html) [(Archive)](https://archive.apache.org/dist/spark/)

```bash
# From the root of the project
# Build the image with different arguments
docker build --rm --force-rm \
    -t my-pyspark-notebook ./images/pyspark-notebook \
    --build-arg openjdk_version=11 \
    --build-arg spark_version=3.2.0 \
    --build-arg hadoop_version=3.2 \
    --build-arg spark_download_url="https://archive.apache.org/dist/spark/"

# Check the newly built image
docker run -it --rm my-pyspark-notebook pyspark --version

# Welcome to
#       ____              __
#      / __/__  ___ _____/ /__
#     _\ \/ _ \/ _ `/ __/  '_/
#    /___/ .__/\_,_/_/ /_/\_\   version 3.2.0
#       /_/

# Using Scala version 2.12.15, OpenJDK 64-Bit Server VM, 11.0.21
# Branch HEAD
# Compiled by user ubuntu on 2021-10-06T12:46:30Z
# Revision 5d45a415f3a29898d92380380cfd82bfc7f579ea
# Url https://github.com/apache/spark
# Type --help for more information.
```

- 다른 Spark 버전의 `pyspark-notebook` 이미지를 빌드하려면, 빌드 시 다음 인자들의 기본값을 덮어쓸 수 있다.
- `all-spark-notebook` 은 `pyspark-notebook` 에서 상속되기 때문에, 먼저 `pyspark-notebook` 을 빌드하고 그 다음 `all-spark-notebook` 을 빌드해야 `all-spark-notebook` 에서 같은 버전을 얻을 수 있다.
- Spark 배포는 Spark, Hadoop, Scala 버전의 조합으로 정의된다. 더 많은 정보는 Apache Spark 다운로드 및 아카이브 리포지토리에서 확인할 수 있다.
- `openjdk_version`: OpenJDK(JRE 헤드리스) 배포판의 버전 (기본값은 17).
  - 이 버전은 위에서 사용된 Spark 배포가 지원하는 버전과 일치해야 한다.
  - Spark 개요 및 Ubuntu 패키지를 참조하라.
- `spark_version` (선택사항): 설치할 Spark 버전, 예를 들어 3.5.0. 지정하지 않으면 (이것이 기본값), 최신 안정 버전의 Spark 가 설치된다.
- `hadoop_version`: Hadoop 버전 (기본값은 3). 주의할 점은, Spark < 3.3 은 Hadoop 버전을 major.minor 형식 (예: 3.2) 으로 지정해야 한다.
- `scala_version` (선택사항): Scala 버전, 예를 들어 2.13(기본적으로 지정되지 않음). Spark >= 3.2 부터는 배포 파일에 Scala 버전이 포함될 수 있다.
- `spark_download_url`: Spark 다운로드에 사용할 URL. 오래된 Spark 버전을 다운로드하려면 <https://archive.apache.org/dist/spark/> URL 을 사용해야 할 수 있다.

#### 3) Local Mode

- Spark 로컬 모드는 Spark 클러스터를 사용할 수 없을 때 작은 데이터에 대한 실험을 위해 유용하다.
- 예시에서, Spark 는 모든 주요 실행 구성 요소를 동일한 단일 JVM 안에서 생성한다. 로컬 모드에 대한 추가 정보는 여기에서 읽을 수 있다. 모든 CPU 를 사용하고 싶다면, 가장 간단한 방법 중 하나는 Spark 스탠드얼론 클러스터를 설정하는 것이다.

##### (1) Python

```python
from pyspark.sql import SparkSession

# Spark session & context
spark = SparkSession.builder.master("local").getOrCreate()
sc = spark.sparkContext

# Sum of the first 100 whole numbers
rdd = sc.parallelize(range(100 + 1))
rdd.sum()
# 5050
```

##### (2) R (SparkR)

```R
library(SparkR)

# Spark session & context
sc <sparkR.session("local")

# Sum of the first 100 whole numbers
sdf <createDataFrame(list(1:100))
dapplyCollect(sdf,
              function(x)
              { x <sum(x)}
             )
# 5050
```

##### (3) R (sparklyr)

```R
library(sparklyr)

# Spark configuration
conf <spark_config()
# Set the catalog implementation in-memory
conf$spark.sql.catalogImplementation <- "in-memory"

# Spark session & context
sc <spark_connect(master = "local", config = conf)

# Sum of the first 100 whole numbers
sdf_len(sc, 100, repartition = 1) %>%
    spark_apply(function(e) sum(e))
# 5050
```

#### 4) Standalone Mode

> [!NOTE] Spark Cluster 연결
> 1. 도커 이미지 (도커파일 확인) 와 배포되는 Spark 클러스터가 동일한 버전의 Spark 를 실행하는지 확인한다.
> 2. 스탠드얼론 모드에서 Spark 를 배포한다.
> 3. 모든 Spark 워커가 네트워크로 접근 가능한 위치에서 `--net=host` 를 사용하여 도커 컨테이너를 실행한다. (이것은 Spark 네트워킹 요구 사항이다.)

- `--net=host` 를 사용할 때, 반드시 `--pid=host -e TINI_SUBREAPER=true` 플래그를 사용해야 한다. 자세한 내용은 [jupyter/docker-stacks#64](https://github.com/jupyter/docker-stacks/issues/64) 를 참조하기
- 예시에서는 Spark 마스터 URL `spark://master:7077` 을 사용하고 있는데, 이는 Spark 마스터의 URL 로 교체해야 한다.

##### (1) Python

```python
from pyspark.sql import SparkSession

# Spark session & context
spark = SparkSession.builder.master("spark://master:7077").getOrCreate()
sc = spark.sparkContext

# Sum of the first 100 whole numbers
rdd = sc.parallelize(range(100 + 1))
rdd.sum()
# 5050
```

- 노트북 (드라이버가 위치한 곳) 과 Spark 워커 모두에서 동일한 Python 버전을 사용해야 한다.
- 드라이버와 워커 측에서 사용되는 Python 버전은 환경 변수 `PYSPARK_PYTHON` 및/또는 `PYSPARK_DRIVER_PYTHON` 을 설정함으로써 조정할 수 있다.

##### (2) R (SparkR)

```R
library(SparkR)

# Spark session & context
sc <sparkR.session("spark://master:7077")

# Sum of the first 100 whole numbers
sdf <createDataFrame(list(1:100))
dapplyCollect(sdf,
              function(x)
              { x <sum(x)}
             )
# 5050
```

##### (3) R (sparklyr)

```R
library(sparklyr)

# Spark session & context
# Spark configuration
conf <spark_config()
# Set the catalog implementation in-memory
conf$spark.sql.catalogImplementation <- "in-memory"
sc <spark_connect(master = "spark://master:7077", config = conf)

# Sum of the first 100 whole numbers
sdf_len(sc, 100, repartition = 1) %>%
    spark_apply(function(e) sum(e))
# 5050
```

#### 5) Dependencies

> 예시로 [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/hadoop/current/install.html) 을 구성한다.

```python
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("elasticsearch")
    .config(
        "spark.jars.packages", "org.elasticsearch:elasticsearch-spark-30_2.12:7.13.0"
    )
    .getOrCreate()
)
```

- Spark 의존성은 `spark.jars.packages` 속성을 통해 선언될 수 있다.
- 이들은 Spark 세션 생성 시 쉼표로 구분된 Maven 좌표 목록으로 정의될 수 있다.
- 의존성은 `spark-defaults.conf` 에서도 정의될 수 있다. 하지만, root 에 의해서만 수행될 수 있으므로, 사용자 정의 이미지를 빌드할 때만 고려해야 한다.

```dockerfile
USER root
RUN echo "spark.jars.packages org.elasticsearch:elasticsearch-spark-30_2.12:7.13.0" >> "${SPARK_HOME}/conf/spark-defaults.conf"
USER ${NB_UID}
```

- Jars 는 Spark 세션 생성 시 동적으로 다운로드되며 기본적으로 `${HOME}/.ivy2/jars` 에 저장된다 (`spark.jars.ivy` 를 설정하여 변경 가능).

### 5. Tensorflow

#### 1) Single Machine Mode

```python
import tensorflow as tf

hello = tf.Variable("Hello World!")

sess = tf.Session()
init = tf.global_variables_initializer()

sess.run(init)
sess.run(hello)
```

#### 2) Distributed Mode

```python
import tensorflow as tf

hello = tf.Variable("Hello Distributed World!")

server = tf.train.Server.create_local_server()
sess = tf.Session(server.target)
init = tf.global_variables_initializer()

sess.run(init)
sess.run(hello)
```

### 참조

#### [주요 사례](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/recipes.html#)

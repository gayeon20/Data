---
title: "[Data] 넘파이 (Numpy)"
excerpt: "과학 컴퓨팅을 위한 기본 패키지입니다. 다차원 배열 객체, 다양한 파생 객체(예: 마스크 배열 및 행렬), 수학, 논리, 모양 조작, 정렬, 선택, I/O, 이산 푸리에 변환, 기본 선형 대수, 기본 통계 연산, 랜덤 시뮬레이션 등 배열에서 빠른 연산을 위한 다양한 루틴을 제공하는 Python 라이브러리입니다."
categories:
  - Numpy
tags:
  - Data
  - AI
  - Scientific-Computing
  - Python
  - Numpy
last_modified_at: 2024-03-01T00:00:00-00:00
link: https://numpy.org/
상위 항목: "[[Software/Code/Language/Python/Package/AI/python_ai|파이썬 과학 컴퓨팅 (Python Scientific Computing)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

**하위 항목**
- [[numpy_grammer|넘파이 문법 (Numpy Grammer)]]

---
- NumPy는 파이썬에서 과학 컴퓨팅을 위한 기본 패키지입니다. 다차원 배열 객체, 다양한 파생 객체(예: 마스크 배열 및 행렬), 수학, 논리, 모양 조작, 정렬, 선택, I/O, 이산 푸리에 변환, 기본 선형 대수, 기본 통계 연산, 랜덤 시뮬레이션 등 배열에서 빠른 연산을 위한 다양한 루틴을 제공하는 Python 라이브러리입니다.
- NumPy 패키지의 핵심은 [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") 객체입니다. 이것은 동종 데이터 유형의 _n_ 차원 배열을 캡슐화하며, 성능을 위해 컴파일된 코드에서 많은 연산이 수행됩니다. NumPy 배열과 표준 파이썬 시퀀스 사이에는 몇 가지 중요한 차이점이 있습니다:
	- (동적으로 커질 수 있는) 파이썬 리스트와 달리 NumPy 배열은 생성 시 크기가 고정되어 있습니다. `ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")의 크기를 변경하면 새 배열이 생성되고 원래 배열은 삭제됩니다.
	- NumPy 배열의 요소는 모두 동일한 데이터 유형이어야 하며, 따라서 메모리에서 동일한 크기가 됩니다. 예외: (NumPy를 포함한 Python) 객체의 배열을 가질 수 있으므로 크기가 다른 요소의 배열을 허용할 수 있습니다.
	- NumPy 배열은 많은 수의 데이터에 대한 고급 수학적 연산 및 기타 유형의 연산을 용이하게 합니다. 일반적으로 이러한 연산은 Python의 기본 제공 시퀀스를 사용할 때보다 더 적은 코드로 더 효율적으로 실행됩니다.
	- 점점 더 많은 과학 및 수학 Python 기반 패키지가 NumPy 배열을 사용하고 있으며, 이러한 패키지는 일반적으로 Python 시퀀스 입력을 지원하지만 처리하기 전에 이러한 입력을 NumPy 배열로 변환하고, 종종 NumPy 배열을 출력합니다. 다시 말해, 오늘날 대부분의 과학/수학 Python 기반 소프트웨어를 효율적으로 사용하려면 Python의 내장 시퀀스 유형을 사용하는 방법만 아는 것만으로는 충분하지 않으며, NumPy 배열을 사용하는 방법도 알아야 합니다.
- NumPy는 객체 지향 접근 방식을 완벽하게 지원하며, 다시 한 번 [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")로 시작합니다. 예를 들어, [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")는 수많은 메서드와 어트리뷰트를 가진 클래스입니다. 이 클래스의 많은 메서드는 가장 바깥쪽에 있는 NumPy 네임스페이스의 함수에 의해 미러링되므로 프로그래머가 선호하는 패러다임으로 코딩할 수 있습니다. 이러한 유연성 덕분에 NumPy 배열 방언과 NumPy [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") 클래스는 Python에서 사용되는 다차원 데이터 교환의 _사실상_ 언어가 될 수 있었습니다.

## 1. 장점
- 수열의 크기와 속도에 관한 사항은 과학 컴퓨팅에서 특히 중요합니다. 간단한 예로, 1-D 수열의 각 원소를 같은 길이의 다른 수열에 있는 해당 원소와 곱하는 경우를 생각해 보겠습니다. 데이터가 `a`와 `b`라는 두 개의 파이썬 리스트에 저장되어 있다면 각 요소를 반복할 수 있습니다:


```python
c = []
for i in range(len(a)):
    c.append(a[i]*b[i])
```

- 이렇게 하면 정답이 나오지만 `a`와 `b`에 각각 수백만 개의 숫자가 포함되어 있으면 파이썬에서 루핑의 비효율성에 대한 대가를 치르게 됩니다. C로 작성하면 동일한 작업을 훨씬 더 빠르게 수행할 수 있습니다(명확성을 위해 변수 선언과 초기화, 메모리 할당 등은 생략합니다).

```C
for (i = 0; i < rows; i++) {...
  c[i] = a[i]*b[i];
}
```

- 이렇게 하면 파이썬 코드를 해석하고 파이썬 객체를 조작하는 데 드는 모든 오버헤드를 절약할 수 있지만, 파이썬 코딩을 통해 얻을 수 있는 이점을 희생해야 합니다. 게다가 필요한 코딩 작업은 데이터의 차원에 따라 증가합니다. 예를 들어 2-D 배열의 경우, C 코드(이전과 같이 요약)는 다음과 같이 확장됩니다.

```C
for (i = 0; i < rows; i++) {''
  for (j = 0; j < 열; j++) {
    c[i][j] = a[i][j]*b[i][j];
  }
}
```

- NumPy는 두 가지 장점을 모두 제공합니다. 요소별 연산은 [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")가 포함될 때 "기본 모드"이지만 요소별 연산은 미리 컴파일된 C 코드에 의해 빠르게 실행됩니다:

```python
c = a * b
```

- NumPy에서 위는 앞의 예제에서 수행한 작업을 C에 가까운 속도로 수행하지만, 파이썬 기반에서 기대할 수 있는 코드 간소화를 제공합니다. 실제로 NumPy 관용구는 훨씬 더 간단합니다! 이 마지막 예제는 NumPy의 많은 기능의 기반이 되는 두 가지 기능, 즉 벡터화와 브로드캐스팅을 보여줍니다.

### 1) 벡터화와 브로드캐스팅

- 벡터화란 코드에 명시적인 루핑, 인덱싱 등이 없는 것을 말합니다. 물론 이러한 작업은 최적화된 사전 컴파일된 C 코드에서 '보이지 않는 곳'에서 이루어집니다. 벡터화된 코드에는 다음과 같은 많은 장점이 있습니다:
	- 벡터화된 코드는 더 간결하고 읽기 쉽습니다.
	- 코드 줄 수가 적다는 것은 일반적으로 버그가 적다는 것을 의미합니다.
	- 코드가 표준 수학 표기법과 더 유사합니다(일반적으로 수학적 구조를 올바르게 코딩하기가 더 쉬워집니다).
	- 벡터화는 더 많은 "파이토닉" 코드를 생성합니다. 벡터화가 없다면 코드는 비효율적이고 읽기 어려운 'for' 루프로 가득 차게 될 것입니다.
- 브로드캐스팅은 연산의 암시적인 요소별 동작을 설명하는 데 사용되는 용어로, 일반적으로 NumPy에서는 산술 연산뿐만 아니라 논리, 비트, 함수 등 모든 연산이 이러한 암시적인 요소별 방식, 즉 브로드캐스팅으로 동작합니다. 또한, 위의 예시에서 `a`와 `b`는 같은 모양의 다차원 배열일 수도 있고, 스칼라와 배열일 수도 있으며, 심지어 모양이 다른 두 배열일 수도 있지만, 결과 브로드캐스트가 모호하지 않은 방식으로 작은 배열이 큰 배열의 모양으로 "확장 가능"하다는 전제 하에 가능합니다. 방송에 대한 자세한 '규칙'은 [방송](https://numpy.org/doc/stable/user/basics.broadcasting.html#basics-broadcasting)을 참조하세요.


## 2. 설치
The only prerequisite for installing NumPy is Python itself. If you don’t have Python yet and want the simplest way to get started, we recommend you use the [Anaconda Distribution](https://www.anaconda.com/download) - it includes Python, NumPy, and many other commonly used packages for scientific computing and data science.

NumPy can be installed with `conda`, with `pip`, with a package manager on macOS and Linux, or [from source](https://numpy.org/devdocs/building). For more detailed instructions, consult our [Python and NumPy installation guide](https://numpy.org/install/#python-numpy-install-guide) below.

**CONDA**

If you use `conda`, you can install NumPy from the `defaults` or `conda-forge` channels:

```bash
# Best practice, use an environment rather than install in the base env
conda create -n my-env
conda activate my-env
# If you want to install from conda-forge
conda config --env --add channels conda-forge
# The actual install command
conda install numpy
```

**PIP**

If you use `pip`, you can install NumPy with:

```bash
pip install numpy
```

Also when using pip, it’s good practice to use a virtual environment - see [Reproducible Installs](https://numpy.org/install/#reproducible-installs) below for why, and [this guide](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko#howto) for details on using virtual environments.

# Python and NumPy installation guide

Installing and managing packages in Python is complicated, there are a number of alternative solutions for most tasks. This guide tries to give the reader a sense of the best (or most popular) solutions, and give clear recommendations. It focuses on users of Python, NumPy, and the PyData (or numerical computing) stack on common operating systems and hardware.

## Recommendations

We’ll start with recommendations based on the user’s experience level and operating system of interest. If you’re in between “beginning” and “advanced”, please go with “beginning” if you want to keep things simple, and with “advanced” if you want to work according to best practices that go a longer way in the future.

### Beginning users

On all of Windows, macOS, and Linux:

- Install [Anaconda](https://www.anaconda.com/download) (it installs all packages you need and all other tools mentioned below).
- For writing and executing code, use notebooks in [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html) for exploratory and interactive computing, and [Spyder](https://www.spyder-ide.org/) or [Visual Studio Code](https://code.visualstudio.com/) for writing scripts and packages.
- Use [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/) to manage your packages and start JupyterLab, Spyder, or Visual Studio Code.

### Advanced users

#### Conda

- Install [Miniforge](https://github.com/conda-forge/miniforge).
- Keep the `base` conda environment minimal, and use one or more [conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) to install the package you need for the task or project you’re working on.

#### Alternative if you prefer pip/PyPI

For users who know, from personal preference or reading about the main differences between conda and pip below, they prefer a pip/PyPI-based solution, we recommend:

- Install Python from [python.org](https://www.python.org/downloads/), [Homebrew](https://brew.sh/), or your Linux package manager.
- Use [Poetry](https://python-poetry.org/) as the most well-maintained tool that provides a dependency resolver and environment management capabilities in a similar fashion as conda does.

## Python package management

Managing packages is a challenging problem, and, as a result, there are lots of tools. For web and general purpose Python development there’s a whole [host of tools](https://packaging.python.org/guides/tool-recommendations/) complementary with pip. For high-performance computing (HPC), [Spack](https://github.com/spack/spack) is worth considering. For most NumPy users though, [conda](https://conda.io/en/latest/) and [pip](https://pip.pypa.io/en/stable/) are the two most popular tools.

### Pip & conda

The two main tools that install Python packages are `pip` and `conda`. Their functionality partially overlaps (e.g. both can install `numpy`), however, they can also work together. We’ll discuss the major differences between pip and conda here - this is important to understand if you want to manage packages effectively.

The first difference is that conda is cross-language and it can install Python, while pip is installed for a particular Python on your system and installs other packages to that same Python install only. This also means conda can install non-Python libraries and tools you may need (e.g. compilers, CUDA, HDF5), while pip can’t.

The second difference is that pip installs from the Python Packaging Index (PyPI), while conda installs from its own channels (typically “defaults” or “conda-forge”). PyPI is the largest collection of packages by far, however, all popular packages are available for conda as well.

The third difference is that conda is an integrated solution for managing packages, dependencies and environments, while with pip you may need another tool (there are many!) for dealing with environments or complex dependencies.

### Reproducible installs

As libraries get updated, results from running your code can change, or your code can break completely. It’s important to be able to reconstruct the set of packages and versions you’re using. Best practice is to:

1. use a different environment per project you’re working on,
2. record package names and versions using your package installer; each has its own metadata format for this:
    - Conda: [conda environments and environment.yml](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
    - Pip: [virtual environments](https://docs.python.org/3/tutorial/venv.html) and [requirements.txt](https://pip.readthedocs.io/en/latest/user_guide/#requirements-files)
    - Poetry: [virtual environments and pyproject.toml](https://python-poetry.org/docs/basic-usage/)

## NumPy packages & accelerated linear algebra libraries

NumPy doesn’t depend on any other Python packages, however, it does depend on an accelerated linear algebra library - typically [Intel MKL](https://software.intel.com/en-us/mkl) or [OpenBLAS](https://www.openblas.net/). Users don’t have to worry about installing those (they’re automatically included in all NumPy install methods). Power users may still want to know the details, because the used BLAS can affect performance, behavior and size on disk:

- The NumPy wheels on PyPI, which is what pip installs, are built with OpenBLAS. The OpenBLAS libraries are included in the wheel. This makes the wheel larger, and if a user installs (for example) SciPy as well, they will now have two copies of OpenBLAS on disk.
    
- In the conda defaults channel, NumPy is built against Intel MKL. MKL is a separate package that will be installed in the users’ environment when they install NumPy.
    
- In the conda-forge channel, NumPy is built against a dummy “BLAS” package. When a user installs NumPy from conda-forge, that BLAS package then gets installed together with the actual library - this defaults to OpenBLAS, but it can also be MKL (from the defaults channel), or even [BLIS](https://github.com/flame/blis) or reference BLAS.
    
- The MKL package is a lot larger than OpenBLAS, it’s about 700 MB on disk while OpenBLAS is about 30 MB.
    
- MKL is typically a little faster and more robust than OpenBLAS.
    

Besides install sizes, performance and robustness, there are two more things to consider:

- Intel MKL is not open source. For normal use this is not a problem, but if a user needs to redistribute an application built with NumPy, this could be an issue.
- Both MKL and OpenBLAS will use multi-threading for function calls like `np.dot`, with the number of threads being determined by both a build-time option and an environment variable. Often all CPU cores will be used. This is sometimes unexpected for users; NumPy itself doesn’t auto-parallelize any function calls. It typically yields better performance, but can also be harmful - for example when using another level of parallelization with Dask, scikit-learn or multiprocessing.

## Troubleshooting

If your installation fails with the message below, see [Troubleshooting ImportError](https://numpy.org/doc/stable/user/troubleshooting-importerror.html).

IMPORTANT: PLEASE READ THIS FOR ADVICE ON HOW TO SOLVE THIS ISSUE!

Importing the numpy c-extensions failed. This error can happen for
different reasons, often due to issues with your setup.


---
## 참조
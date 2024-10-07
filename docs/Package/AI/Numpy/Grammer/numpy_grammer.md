---
title: "[Numpy] 넘파이 문법 (Numpy Grammer)"
excerpt: "과학 컴퓨팅을 위한 기본 패키지입니다. 다차원 배열 객체, 다양한 파생 객체(예: 마스크 배열 및 행렬), 수학, 논리, 차원 조작, 정렬, 선택, I/O, 이산 푸리에 변환, 기본 선형 대수, 기본 통계 연산, 랜덤 시뮬레이션 등 배열에서 빠른 연산을 위한 다양한 루틴을 제공하는 Python 라이브러리입니다."
categories:
  - Numpy
tags:
  - Numpy
  - Array
  - Linear-Algebra
last_modified_at: 2024-03-01T00:00:00-00:00
link: https://numpy.org/doc/stable/user/absolute_beginners.html
상위 항목: "[[Software/Code/Language/Python/Package/AI/python_ai|파이썬 과학 컴퓨팅 (Python Scientific Computing)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

---

- NumPy의 주요 객체는 동종 다차원 배열입니다. 이는 모두 같은 유형의 요소(보통 숫자)로 구성된 테이블로, 음수가 아닌 정수의 튜플로 인덱싱됩니다. NumPy에서는 차원을 축이라고 합니다.
- 예를 들어, 3D 공간에서 한 점의 좌표 배열인 `[1, 2, 1]`은 하나의 축을 가집니다. 이 축에는 3개의 요소가 있으므로 길이가 3이라고 합니다. 아래 그림의 예에서는 배열의 축이 2개입니다. 첫 번째 축의 길이는 2, 두 번째 축의 길이는 3입니다.

```python
[[1., 0., 0.],
 [0., 1., 2.]]
```

## 기본 문법

### 속성
- NumPy의 배열 클래스는 N차원 배열 객체로 `ndarray`라고 불립니다. 별칭 `array`로도 알려져 있습니다. `numpy.array`는 1차원 배열만 처리하고 기능이 적은 표준 파이썬 라이브러리 클래스 `array.array`와 동일하지 않다는 점에 유의하세요. `ndarray` 객체의 더 중요한 속성은 다음과 같습니다:
- `ndarray`는 같은 데이터 타입만 가질 수 있습니다. 다른 타입의 데이터를 입력할 경우 데이터가 변환됩니다. 데이터 타입은 `astype()`를 사용하여 변환할 수 있습니다.
  ex) 0, 1, 2 등의 작은 값만 가질 경우 64bit의 float 형보다는 8bit나 16bit의 integer가 유리

| 속성                   | 설명                                                                                                                                                              |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ndarray.ndim**     | 배열의 축(차원) 수입니다.                                                                                                                                                 |
| **ndarray.shape**    | 배열의 차원. 이는 각 차원에서 배열의 크기를 나타내는 정수 튜플입니다. 행이 _n_개, 열이 _m_개인 행렬의 경우 `shape`는 `(n,m)`가 됩니다. 따라서 `shape` 튜플의 길이는 축의 수인 `ndim`입니다.                                   |
| **ndarray.size**     | 배열의 총 요소 수입니다. 이것은 `shape` 요소의 곱과 같습니다.                                                                                                                         |
| **ndarray.dtype**    | 배열에 있는 요소의 유형을 설명하는 객체. 표준 파이썬 형을 사용하여 dtype을 생성하거나 지정할 수 있습니다. 또한 NumPy는 자체 타입을 제공합니다. numpy.int32, numpy.int16, numpy.float64가 몇 가지 예입니다.                     |
| **ndarray.itemsize** | 배열의 각 요소의 바이트 단위 크기입니다. 예를 들어, `float64` 타입의 요소로 구성된 배열은 `itemsize` 8(=64/8)이고, `complex32` 타입의 배열은 `itemsize` 4(=32/8)입니다. 이는 `ndarray.dtype.itemsize`와 동일합니다. |
| **ndarray.data**     | 배열의 실제 요소를 포함하는 버퍼입니다. 일반적으로 인덱싱 기능을 사용하여 배열의 요소에 액세스하기 때문에 이 속성을 사용할 필요가 없습니다.                                                                                 |

```python
>>> import numpy as np
>>> a = np.arange(15).reshape(3, 5)
>>> a
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
>>> a.shape
(3, 5)
>>> a.ndim
2
>>> a.dtype.name
'int64'
>>> a.itemsize
8
>>> a.size
15
>>> type(a)
<class 'numpy.ndarray'>
>>> b = np.array([6, 7, 8])
>>> b
array([6, 7, 8])
>>> type(b)
<class 'numpy.ndarray'>
```

### 배열 생성 (Array Creation)

- 배열을 만드는 방법에는 여러 가지가 있습니다.
- 예를 들어 `array` 함수를 사용하여 일반 Python 리스트나 튜플에서 배열을 만들 수 있습니다. 결과 배열의 유형은 시퀀스에 있는 요소의 유형에서 추론됩니다.

```python
>>> import numpy as np
>>> a = np.array([2, 3, 4])
>>> a
array([2, 3, 4])
>>> a.dtype
dtype('int64')
>>> b = np.array([1.2, 3.5, 5.1])
>>> b.dtype
dtype('float64')
```

- 자주 발생하는 오류는 단일 시퀀스를 인수로 제공하지 않고 여러 개의 인수를 사용하여 `array`를 호출하는 경우입니다.

```python
>>> a = np.array(1, 2, 3, 4)    # WRONG
Traceback (most recent call last):
  …
TypeError: array() takes from 1 to 2 positional arguments but 4 were given
>>> a = np.array([1, 2, 3, 4])  # RIGHT
```

- `array`는 시퀀스의 시퀀스를 2차원 배열로, 시퀀스의 시퀀스를 3차원 배열로 변환하는 등의 작업을 수행합니다.

```python
>>> b = np.array([(1.5, 2, 3), (4, 5, 6)])
>>> b
array([[1.5, 2. , 3. ],
       [4. , 5. , 6. ]])
```

- 배열의 유형은 생성 시 명시적으로 지정할 수도 있습니다:

```python
>>> c = np.array([[1, 2], [3, 4]], dtype=complex)
>>> c
array([[1.+0.j, 2.+0.j],
       [3.+0.j, 4.+0.j]])
```
- 배열의 요소는 원래 알려지지 않았지만 그 크기는 알려진 경우가 많습니다. 따라서 NumPy는 초기 자리 표시자 콘텐츠로 배열을 생성하는 여러 함수를 제공합니다. 이러한 함수는 값비싼 작업인 배열을 늘릴 필요성을 최소화합니다.
- `zeros` 함수는 0으로 가득 찬 배열을 만들고, `ones` 함수는 1로 가득 찬 배열을 만들고, `empty` 함수는 초기 내용이 무작위이며 메모리 상태에 따라 달라지는 배열을 만듭니다. 기본적으로 생성된 배열의 dtype은 `float64`이지만 키워드 인자 `dtype`을 통해 지정할 수 있습니다.

```python
>>> np.zeros((3, 4))
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
>>> np.ones((2, 3, 4), dtype=np.int16)
array([[[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]],

       [[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]]], dtype=int16)
>>> np.empty((2, 3)) 
array([[3.73603959e-262, 6.02658058e-154, 6.55490914e-260],  # may vary
       [5.30498948e-313, 3.14673309e-307, 1.00000000e+000]])
```

- 숫자 시퀀스를 생성하기 위해 NumPy는 파이썬 내장 `range`와 유사하지만 배열을 반환하는 `arange` 함수를 제공합니다.

```python
>>> np.arange(10, 30, 5)
array([10, 15, 20, 25])
>>> np.arange(0, 2, 0.3)  # it accepts float arguments
array([0. , 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])
```

- `arange`를 부동 소수점 인자와 함께 사용하면 일반적으로 부동 소수점 정밀도가 유한하기 때문에 얻은 요소의 수를 예측할 수 없습니다. 따라서 일반적으로 단계 대신 원하는 요소의 수를 인수로 받는 함수 `linspace`를 사용하는 것이 좋습니다:

```python
>>> from numpy import pi
>>> np.linspace(0, 2, 9)                   # 9 numbers from 0 to 2
array([0.  , 0.25, 0.5 , 0.75, 1.  , 1.25, 1.5 , 1.75, 2.  ])
>>> x = np.linspace(0, 2 * pi, 100)        # useful to evaluate function at lots of points
>>> f = np.sin(x)
```


> [!seealso] 
> [`array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array"), [`zeros`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros"), [`zeros_like`](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like"), [`ones`](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones"), [`ones_like`](https://numpy.org/doc/stable/reference/generated/numpy.ones_like.html#numpy.ones_like "numpy.ones_like"), [`empty`](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty"), [`empty_like`](https://numpy.org/doc/stable/reference/generated/numpy.empty_like.html#numpy.empty_like "numpy.empty_like"), [`arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange"), [`linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace"), [`random.Generator.random`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random "numpy.random.Generator.random"), [`random.Generator.normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html#numpy.random.Generator.normal "numpy.random.Generator.normal"), [`fromfunction`](https://numpy.org/doc/stable/reference/generated/numpy.fromfunction.html#numpy.fromfunction "numpy.fromfunction"), [`fromfile`](https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html#numpy.fromfile "numpy.fromfile")

### 배열 출력 (Printing Arrays)

- 배열을 출력할 때 NumPy는 중첩된 목록과 비슷한 방식으로 배열을 표시하지만 다음과 같은 레이아웃을 사용합니다:
	- 마지막 축은 왼쪽에서 오른쪽으로 인쇄됩니다,
	- 두 번째에서 마지막 축은 위에서 아래로 인쇄됩니다,
	- 나머지도 위에서 아래로 인쇄되며 각 슬라이스는 빈 줄로 다음 슬라이스와 구분됩니다.
- 그런 다음 1차원 배열은 행으로, 2차원 배열은 행렬로, 3차원 배열은 행렬의 목록으로 인쇄됩니다.

```python
>>> a = np.arange(6)                    # 1d array
>>> print(a)
[0 1 2 3 4 5]
>>>
>>> b = np.arange(12).reshape(4, 3)     # 2d array
>>> print(b)
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
>>>
>>> c = np.arange(24).reshape(2, 3, 4)  # 3d array
>>> print(c)
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
```

- [[#2. 차원 조작 (Shape manipulation)|아래]]를 참조하여 `reshape`에 대한 자세한 내용을 확인하세요.
- 배열이 너무 커서 인쇄할 수 없는 경우 NumPy는 배열의 중앙 부분을 자동으로 건너뛰고 모서리 부분만 인쇄합니다:

```python
>>> print(np.arange(10000))
[   0    1    2 … 9997 9998 9999]
>>>
>>> print(np.arange(10000).reshape(100, 100))
[[   0    1    2 …   97   98   99]
 [ 100  101  102 …  197  198  199]
 [ 200  201  202 …  297  298  299]
 …
 [9700 9701 9702 … 9797 9798 9799]
 [9800 9801 9802 … 9897 9898 9899]
 [9900 9901 9902 … 9997 9998 9999]]
```

- 이 동작을 비활성화하고 NumPy가 전체 배열을 인쇄하도록 하려면 `set_printoptions`를 사용하여 인쇄 옵션을 변경하면 됩니다.

```python
>>> np.set_printoptions(threshold=sys.maxsize)  # sys module should be imported
```

### 기본 연산 (Basic operations)

- 배열의 산술 연산자는 요소 순으로 적용됩니다. 새 배열이 생성되고 그 결과로 채워집니다.

```python
>>> a = np.array([20, 30, 40, 50])
>>> b = np.arange(4)
>>> b
array([0, 1, 2, 3])
>>> c = a - b
>>> c
array([20, 29, 38, 47])
>>> b**2
array([0, 1, 4, 9])
>>> 10 * np.sin(a)
array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])
>>> a < 35
array([ True,  True, False, False])
```

- 많은 행렬 언어와 달리, NumPy 배열에서는 곱하기 연산자 `*`가 요소 단위로 작동합니다. 행렬 곱은 `@` 연산자(파이썬 >=3.5에서는) 또는 `dot` 함수 또는 메서드를 사용하여 수행할 수 있습니다:

```python
>>> A = np.array([[1, 1],
…               [0, 1]])
>>> B = np.array([[2, 0],
…               [3, 4]])
>>> A * B     # elementwise product
array([[2, 0],
       [0, 4]])
>>> A @ B     # matrix product
array([[5, 4],
       [3, 4]])
>>> A.dot(B)  # another matrix product
array([[5, 4],
       [3, 4]])
```

- `+=` 및 `*=`와 같은 일부 연산은 새 배열을 생성하는 대신 기존 배열을 수정하는 역할을 합니다.

```python
>>> rg = np.random.default_rng(1)  # create instance of default random number generator
>>> a = np.ones((2, 3), dtype=int)
>>> b = rg.random((2, 3))
>>> a *= 3
>>> a
array([[3, 3, 3],
       [3, 3, 3]])
>>> b += a
>>> b
array([[3.51182162, 3.9504637 , 3.14415961],
       [3.94864945, 3.31183145, 3.42332645]])
>>> a += b  # b is not automatically converted to integer type
Traceback (most recent call last):
    …
numpy._core._exceptions._UFuncOutputCastingError: Cannot cast ufunc 'add' output from dtype('float64') to dtype('int64') with casting rule 'same_kind'
```

- 서로 다른 유형의 배열로 작업할 때 결과 배열의 유형은 더 일반적이거나 정확한 배열에 해당합니다(업캐스팅이라고 알려진 동작).

```python
>>> a = np.ones(3, dtype=np.int32)
>>> b = np.linspace(0, pi, 3)
>>> b.dtype.name
'float64'
>>> c = a + b
>>> c
array([1.        , 2.57079633, 4.14159265])
>>> c.dtype.name
'float64'
>>> d = np.exp(c * 1j)
>>> d
array([ 0.54030231+0.84147098j, -0.84147098+0.54030231j,
       -0.54030231-0.84147098j])
>>> d.dtype.name
'complex128'
```

- 배열의 모든 요소의 합을 계산하는 것과 같은 많은 단항 연산은 `ndarray` 클래스의 메서드로 구현됩니다.

```python
>>> a = rg.random((2, 3))
>>> a
array([[0.82770259, 0.40919914, 0.54959369],
       [0.02755911, 0.75351311, 0.53814331]])
>>> a.sum()
3.1057109529998157
>>> a.min()
0.027559113243068367
>>> a.max()
0.8277025938204418
```

- 기본적으로 이러한 연산은 배열의 차원에 관계없이 배열이 숫자의 목록인 것처럼 적용됩니다. 그러나 `axis` 매개변수를 지정하면 배열의 지정된 축을 따라 연산을 적용할 수 있습니다:

```python
>>> b = np.arange(12).reshape(3, 4)
>>> b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>>
>>> b.sum(axis=0)     # sum of each column
array([12, 15, 18, 21])
>>>
>>> b.min(axis=1)     # min of each row
array([0, 4, 8])
>>>
>>> b.cumsum(axis=1)  # cumulative sum along each row
array([[ 0,  1,  3,  6],
       [ 4,  9, 15, 22],
       [ 8, 17, 27, 38]])
```

### 범용 함수 (Universal Functions)

- NumPy는 sin, cos, exp와 같은 친숙한 수학 함수를 제공합니다. NumPy에서는 이러한 함수를 "범용 함수"(`ufunc`)라고 합니다. NumPy 내에서 이러한 함수는 배열에서 요소 단위로 작동하여 배열을 출력으로 생성합니다.

```python
>>> B = np.arange(3)
>>> B
array([0, 1, 2])
>>> np.exp(B)
array([1.        , 2.71828183, 7.3890561 ])
>>> np.sqrt(B)
array([0.        , 1.        , 1.41421356])
>>> C = np.array([2., -1., 4.])
>>> np.add(B, C)
array([2., 0., 6.])
```

#### 정렬
- `np.sort(ndarray)`는 입력 받은 `ndarray`의 정렬된 행렬을 반환합니다.
- `ndarray.sort()`는 `ndarray`를 정렬한 형태로 변환합니다. 반환 값은 `None`입니다.
- `sort()`에 인자로 어떤 `axis`를 기준으로 정렬할 것인지 입력할 수 있습니다.
  
  `np.sort(A,axis=0)`

- `np.argsort()`는 정렬된 행렬의 원래 인덱스를 반환합니다.
  
```python
>> np.argsort([3, 1, 9, 5])
1, 0, 3, 2
```

> [!seealso] 
> [`all`](https://numpy.org/doc/stable/reference/generated/numpy.all.html#numpy.all "numpy.all"), [`any`](https://numpy.org/doc/stable/reference/generated/numpy.any.html#numpy.any "numpy.any"), [`apply_along_axis`](https://numpy.org/doc/stable/reference/generated/numpy.apply_along_axis.html#numpy.apply_along_axis "numpy.apply_along_axis"), [`argmax`](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy.argmax "numpy.argmax"), [`argmin`](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin "numpy.argmin"), [`argsort`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort"), [`average`](https://numpy.org/doc/stable/reference/generated/numpy.average.html#numpy.average "numpy.average"), [`bincount`](https://numpy.org/doc/stable/reference/generated/numpy.bincount.html#numpy.bincount "numpy.bincount"), [`ceil`](https://numpy.org/doc/stable/reference/generated/numpy.ceil.html#numpy.ceil "numpy.ceil"), [`clip`](https://numpy.org/doc/stable/reference/generated/numpy.clip.html#numpy.clip "numpy.clip"), [`conj`](https://numpy.org/doc/stable/reference/generated/numpy.conj.html#numpy.conj "numpy.conj"), [`corrcoef`](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef "numpy.corrcoef"), [`cov`](https://numpy.org/doc/stable/reference/generated/numpy.cov.html#numpy.cov "numpy.cov"), [`cross`](https://numpy.org/doc/stable/reference/generated/numpy.cross.html#numpy.cross "numpy.cross"), [`cumprod`](https://numpy.org/doc/stable/reference/generated/numpy.cumprod.html#numpy.cumprod "numpy.cumprod"), [`cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum"), [`diff`](https://numpy.org/doc/stable/reference/generated/numpy.diff.html#numpy.diff "numpy.diff"), [`dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot"), [`floor`](https://numpy.org/doc/stable/reference/generated/numpy.floor.html#numpy.floor "numpy.floor"), [`inner`](https://numpy.org/doc/stable/reference/generated/numpy.inner.html#numpy.inner "numpy.inner"), [`invert`](https://numpy.org/doc/stable/reference/generated/numpy.invert.html#numpy.invert "numpy.invert"), [`lexsort`](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html#numpy.lexsort "numpy.lexsort"), [`max`](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max"), [`maximum`](https://numpy.org/doc/stable/reference/generated/numpy.maximum.html#numpy.maximum "numpy.maximum"), [`mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean"), [`median`](https://numpy.org/doc/stable/reference/generated/numpy.median.html#numpy.median "numpy.median"), [`min`](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "numpy.min"), [`minimum`](https://numpy.org/doc/stable/reference/generated/numpy.minimum.html#numpy.minimum "numpy.minimum"), [`nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero"), [`outer`](https://numpy.org/doc/stable/reference/generated/numpy.outer.html#numpy.outer "numpy.outer"), [`prod`](https://numpy.org/doc/stable/reference/generated/numpy.prod.html#numpy.prod "numpy.prod"), [`re`](https://docs.python.org/3/library/re.html#module-re "(in Python v3.12)"), [`round`](https://numpy.org/doc/stable/reference/generated/numpy.round.html#numpy.round "numpy.round"), [`sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort"), [`std`](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std"), [`sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum"), [`trace`](https://numpy.org/doc/stable/reference/generated/numpy.trace.html#numpy.trace "numpy.trace"), [`transpose`](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy.transpose "numpy.transpose"), [`var`](https://numpy.org/doc/stable/reference/generated/numpy.var.html#numpy.var "numpy.var"), [`vdot`](https://numpy.org/doc/stable/reference/generated/numpy.vdot.html#numpy.vdot "numpy.vdot"), [`vectorize`](https://numpy.org/doc/stable/reference/generated/numpy.vectorize.html#numpy.vectorize "numpy.vectorize"), [`where`](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where "numpy.where")

### 인덱싱, 슬라이싱 및 반복하기 (Indexing, slicing and iterating)

- **1차원** 배열은 [목록](https://docs.python.org/tutorial/introduction.html#lists) 및 다른 Python 시퀀스와 마찬가지로 색인, 슬라이스 및 반복 처리할 수 있습니다.

```python
>>> a = np.arange(10)**3
>>> a
array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])
>>> a[2]
8
>>> a[2:5]
array([ 8, 27, 64])
>>> # equivalent to a[0:6:2] = 1000;
>>> # from start to position 6, exclusive, set every 2nd element to 1000
>>> a[:6:2] = 1000
>>> a
array([1000,    1, 1000,   27, 1000,  125,  216,  343,  512,  729])
>>> a[::-1]  # reversed a
array([ 729,  512,  343,  216,  125, 1000,   27, 1000,    1, 1000])
>>> for i in a:
…     print(i**(1 / 3.))
…
9.999999999999998  # may vary
1.0
9.999999999999998
3.0
9.999999999999998
4.999999999999999
5.999999999999999
6.999999999999999
7.999999999999999
8.999999999999998
```

- **다차원** 배열은 축당 하나의 인덱스를 가질 수 있습니다. 이러한 인덱스는 쉼표로 구분된 튜플로 제공됩니다:

```python
>>> def f(x, y):
…     return 10 * x + y
…
>>> b = np.fromfunction(f, (5, 4), dtype=int)
>>> b
array([[ 0,  1,  2,  3],
       [10, 11, 12, 13],
       [20, 21, 22, 23],
       [30, 31, 32, 33],
       [40, 41, 42, 43]])
>>> b[2, 3]
23
>>> b[0:5, 1]  # each row in the second column of b
array([ 1, 11, 21, 31, 41])
>>> b[:, 1]    # equivalent to the previous example
array([ 1, 11, 21, 31, 41])
>>> b[1:3, :]  # each column in the second and third row of b
array([[10, 11, 12, 13],
       [20, 21, 22, 23]])
```

- 축 수보다 적은 수의 인덱스가 제공되면 누락된 인덱스는 완전한 슬라이스 `:`로 간주됩니다.

```python
>>> b[-1]   # the last row. Equivalent to b[-1, :]
array([40, 41, 42, 43])
```

- 대괄호 안의 `b[i]` 표현식은 `i` 뒤에 나머지 축을 나타내는 데 필요한 만큼의 `:` 인스턴스가 있는 것으로 취급됩니다. NumPy를 사용하면 점을 사용하여 `b[i, …]`로 작성할 수도 있습니다.
- 점**(`…`)은 완전한 인덱싱 튜플을 생성하는 데 필요한 만큼의 콜론을 나타냅니다. 예를 들어, `x`가 축이 5개인 배열인 경우
	- `x[1, 2, …]`는 `x[1, 2, :, :, :]`와 동일합니다,
	- `x[…, 3]`은 `x[:, :, :, :, 3]`으로, 그리고
	- `x[4, …, 5, :]`는 `x[4, :, :, 5, :]`로 바뀝니다.
    

```python
>>> c = np.array([[[  0,  1,  2],  # a 3D array (two stacked 2D arrays)
…                [ 10, 12, 13]],
…               [[100, 101, 102],
…                [110, 112, 113]]])
>>> c.shape
(2, 2, 3)
>>> c[1, …]  # same as c[1, :, :] or c[1]
array([[100, 101, 102],
       [110, 112, 113]])
>>> c[…, 2]  # same as c[:, :, 2]
array([[  2,  13],
       [102, 113]])
```

**다차원 배열에 대한 반복**은 첫 번째 축을 기준으로 수행됩니다:

```python
>>> for row in b:
…     print(row)
…
[0 1 2 3]
[10 11 12 13]
[20 21 22 23]
[30 31 32 33]
[40 41 42 43]
```

- 그러나 배열의 각 요소에 대해 연산을 수행하려면 배열의 모든 요소에 대해 [반복자](https://docs.python.org/tutorial/classes.html#iterators)인 `flat` 속성을 사용할 수 있습니다:

```python
>>> for element in b.flat:
…     print(element)
…
0
1
2
3
10
11
12
13
20
21
22
23
30
31
32
33
40
41
42
43
```

> [!seealso] 
> [Indexing on ndarrays](https://numpy.org/doc/stable/user/basics.indexing.html#basics-indexing), [Indexing routines](https://numpy.org/doc/stable/reference/routines.indexing.html#arrays-indexing) (reference), [`newaxis`](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis"), [`ndenumerate`](https://numpy.org/doc/stable/reference/generated/numpy.ndenumerate.html#numpy.ndenumerate "numpy.ndenumerate"), [`indices`](https://numpy.org/doc/stable/reference/generated/numpy.indices.html#numpy.indices "numpy.indices")

## 차원 조작 (Shape manipulation)
- `shape`는 행, 열, 높이 단위가 아니라 axis0, axis1, axis2와 같이 axis 단위로 부여됩니다.


### 배열의 차원 변경하기 (Changing the shape of an array)

- 배열은 각 축에 있는 요소의 수에 따라 차원이 정해집니다:
```python
>>> a = np.floor(10 * rg.random((3, 4)))
>>> a
array([[3., 7., 3., 4.],
       [1., 4., 2., 2.],
       [7., 2., 4., 9.]])
>>> a.shape
(3, 4)
```

- 배열의 차원은 다양한 명령어로 변경할 수 있습니다. 다음 세 가지 명령은 모두 수정된 배열을 반환하지만 원래 배열은 변경하지 않습니다:

```python
>>> a.ravel()  # returns the array, flattened
array([3., 7., 3., 4., 1., 4., 2., 2., 7., 2., 4., 9.])
>>> a.reshape(6, 2)  # returns the array with a modified shape
array([[3., 7.],
       [3., 4.],
       [1., 4.],
       [2., 2.],
       [7., 2.],
       [4., 9.]])
>>> a.T  # returns the array, transposed
array([[3., 1., 7.],
       [7., 4., 2.],
       [3., 2., 4.],
       [4., 2., 9.]])
>>> a.T.shape
(4, 3)
>>> a.shape
(3, 4)
```

- 배열의 요소 순서는 일반적으로 "C 스타일", 즉 가장 오른쪽 인덱스가 "가장 빠르게 변경"되므로 `a[0, 0]` 뒤의 요소는 `a[0, 1]`입니다. 배열이 다른 차원으로 재형성되면 다시 배열은 "C 스타일"로 처리됩니다. NumPy는 일반적으로 이 순서대로 저장된 배열을 생성하므로 `ravel`은 일반적으로 인수를 복사할 필요가 없지만, 배열이 다른 배열의 조각을 가져와서 만들어졌거나 특이한 옵션으로 만들어진 경우 복사해야 할 수 있습니다. 또한 `ravel` 및 `reshape` 함수는 선택적 인수를 사용하여 가장 왼쪽 인덱스가 가장 빠르게 변경되는 FORTRAN 스타일 배열을 사용하도록 지시할 수 있습니다.
- [`reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape") 함수는 수정된 차원으로 인수를 반환하는 반면, [`ndarray.resize`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.resize.html#numpy.ndarray.resize "numpy.ndarray.resize") 메서드는 배열 자체를 수정합니다:
- `np.transpose(ndarray)` 혹은 `ndarray.T`는 전치 행렬을 반환합니다.

```python
>>> a
array([[3., 7., 3., 4.],
       [1., 4., 2., 2.],
       [7., 2., 4., 9.]])
>>> a.resize((2, 6))
>>> a
array([[3., 7., 3., 4., 1., 4.],
       [2., 2., 7., 2., 4., 9.]])
```

- 재구성 작업에서 차원이 '-1'로 지정되면 다른 차원은 자동으로 계산됩니다:

```python
>>> a.reshape(3, -1)
array([[3., 7., 3., 4.],
       [1., 4., 2., 2.],
       [7., 2., 4., 9.]])
```

> [!seealso] 
> [`ndarray.shape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html#numpy.ndarray.shape "numpy.ndarray.shape"), [`reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape"), [`resize`](https://numpy.org/doc/stable/reference/generated/numpy.resize.html#numpy.resize "numpy.resize"), [`ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel")

### 서로 다른 배열을 함께 쌓기 (Stacking together different arrays)

- 여러 배열을 서로 다른 축을 따라 함께 쌓을 수 있습니다:

```python
>>> a = np.floor(10 * rg.random((2, 2)))
>>> a
array([[9., 7.],
       [5., 2.]])
>>> b = np.floor(10 * rg.random((2, 2)))
>>> b
array([[1., 9.],
       [5., 1.]])
>>> np.vstack((a, b))
array([[9., 7.],
       [5., 2.],
       [1., 9.],
       [5., 1.]])
>>> np.hstack((a, b))
array([[9., 7., 1., 9.],
       [5., 2., 5., 1.]])
```

- [`column_stack`](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack") 함수는 1D 배열을 열로 2D 배열로 스택합니다. 2D 배열에 대해서만 [`hstack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")과 동일합니다:

```python
>>> from numpy import newaxis
>>> np.column_stack((a, b))  # with 2D arrays
array([[9., 7., 1., 9.],
       [5., 2., 5., 1.]])
>>> a = np.array([4., 2.])
>>> b = np.array([3., 8.])
>>> np.column_stack((a, b))  # returns a 2D array
array([[4., 3.],
       [2., 8.]])
>>> np.hstack((a, b))        # the result is different
array([4., 2., 3., 8.])
>>> a[:, newaxis]  # view `a` as a 2D column vector
array([[4.],
       [2.]])
>>> np.column_stack((a[:, newaxis], b[:, newaxis]))
array([[4., 3.],
       [2., 8.]])
>>> np.hstack((a[:, newaxis], b[:, newaxis]))  # the result is the same
array([[4., 3.],
       [2., 8.]])
```

- 일반적으로 두 개 이상의 차원을 가진 배열의 경우, [`hstack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")은 두 번째 축을 따라 쌓고, [`vstack`](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")은 첫 번째 축을 따라 쌓으며 [`concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")는 연결할 축의 수를 나타내는 옵션 인자를 사용할 수 있습니다.

> [!NOTE]
> - 복잡한 경우, [`r_`](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_") 및 [`c_`](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")는 한 축을 따라 숫자를 쌓아서 배열을 만드는 데 유용합니다. 범위 리터럴 `:`을 사용할 수 있습니다.
> 
> ```python
> >>> np.r_[1:4, 0, 4]
> array([1, 2, 3, 0, 4])
> ```
> 
> - 배열을 인자로 사용하는 경우, [`r_`](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_") 및 [`c_`](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_"는 기본 동작은 [`vstack`](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack") 및 [`hstack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack"과 유사하지만 연결할 축의 수를 나타내는 옵션 인수를 사용할 수 있도록 합니다.
> 
> > [!seealso] 
> > [`hstack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack"), [`vstack`](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack"), [`column_stack`](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack"), [`concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate"), [`c_`](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_"), [`r_`](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_")
> 

### 하나의 배열을 여러 개의 작은 배열로 분할하기 (Splitting one array into several smaller ones)

- [`hsplit`](https://numpy.org/doc/stable/reference/generated/numpy.hsplit.html#numpy.hsplit "numpy.hsplit")을 사용하면 반환할 동일한 차원의 배열의 수를 지정하거나 분할이 발생할 열을 지정하여 가로 축을 따라 배열을 분할할 수 있습니다:

```python
>>> a = np.floor(10 * rg.random((2, 12)))
>>> a
array([[6., 7., 6., 9., 0., 5., 4., 0., 6., 8., 5., 2.],
       [8., 5., 5., 7., 1., 8., 6., 7., 1., 8., 1., 0.]])
>>> # Split `a` into 3
>>> np.hsplit(a, 3)
[array([[6., 7., 6., 9.],
       [8., 5., 5., 7.]]), array([[0., 5., 4., 0.],
       [1., 8., 6., 7.]]), array([[6., 8., 5., 2.],
       [1., 8., 1., 0.]])]
>>> # Split `a` after the third and the fourth column
>>> np.hsplit(a, (3, 4))
[array([[6., 7., 6.],
       [8., 5., 5.]]), array([[9.],
       [7.]]), array([[0., 5., 4., 0., 6., 8., 5., 2.],
       [1., 8., 6., 7., 1., 8., 1., 0.]])]
```

- [`vsplit`](https://numpy.org/doc/stable/reference/generated/numpy.vsplit.html#numpy.vsplit "numpy.vsplit") splits along the vertical axis, and [`array_split`](https://numpy.org/doc/stable/reference/generated/numpy.array_split.html#numpy.array_split "numpy.array_split") allows one to specify along which axis to split.


## 복사 및 보기 (Copies and views)

- 배열을 조작하고 조작할 때 데이터가 새 배열에 복사되는 경우도 있고 복사되지 않는 경우도 있습니다. 이는 초보자에게 종종 혼란을 야기하는 원인이 됩니다. 세 가지 경우가 있습니다:

### 전혀 복사되지 않음 (No copy at all)

- 단순 할당은 개체나 해당 데이터의 복사본을 만들지 않습니다.

```python
>>> a = np.array([[ 0,  1,  2,  3],
…               [ 4,  5,  6,  7],
…               [ 8,  9, 10, 11]])
>>> b = a            # no new object is created
>>> b is a           # a and b are two names for the same ndarray object
True
```

- 파이썬은 변경 가능한 객체를 참조로 전달하므로 함수 호출은 복사본을 만들지 않습니다.

```python
>>> def f(x):
…     print(id(x))
…
>>> id(a)  # id is a unique identifier of an object 
148293216  # may vary
>>> f(a)   
148293216  # may vary
```

### 보기 또는 얕은 복사 (View or shallow copy)

- 서로 다른 배열 객체는 동일한 데이터를 공유할 수 있습니다. `view` 메서드는 동일한 데이터를 보는 새 배열 객체를 만듭니다.

```python
>>> c = a.view()
>>> c is a
False
>>> c.base is a            # c is a view of the data owned by a
True
>>> c.flags.owndata
False
>>>
>>> c = c.reshape((2, 6))  # a's shape doesn't change
>>> a.shape
(3, 4)
>>> c[0, 4] = 1234         # a's data changes
>>> a
array([[   0,    1,    2,    3],
       [1234,    5,    6,    7],
       [   8,    9,   10,   11]])
```

- 배열을 슬라이스하면 배열의 뷰가 반환됩니다:

```python
>>> s = a[:, 1:3]
>>> s[:] = 10  # s[:] is a view of s. Note the difference between s = 10 and s[:] = 10
>>> a
array([[   0,   10,   10,    3],
       [1234,   10,   10,    7],
       [   8,   10,   10,   11]])
```

### 깊은 복사 (Deep copy)

- `copy` 메서드는 배열과 해당 데이터의 전체 복사본을 만듭니다.

```python
>>> d = a.copy()  # a new array object with new data is created
>>> d is a
False
>>> d.base is a  # d doesn't share anything with a
False
>>> d[0, 0] = 9999
>>> a
array([[   0,   10,   10,    3],
       [1234,   10,   10,    7],
       [   8,   10,   10,   11]])
```

- 슬라이싱 후 원본 배열이 더 이상 필요하지 않은 경우 `copy`를 호출해야 하는 경우도 있습니다. 예를 들어, `a`가 거대한 중간 결과이고 최종 결과인 `b`에는 `a`의 일부만 포함되어 있다고 가정하면 슬라이싱으로 `b`를 구성할 때 딥 카피를 만들어야 합니다:

```python
>>> a = np.arange(int(1e8))
>>> b = a[:100].copy()
>>> del a  # the memory of ``a`` can be released.
```

- 대신 `b = a[:100]`을 사용하면 `a`는 `b`에 의해 참조되며 `del a`가 실행되더라도 메모리에 유지됩니다.


> [!NOTE] 함수 및 메서드 개요
> 
> > 다음은 카테고리별로 정렬된 몇 가지 유용한 NumPy 함수와 메서드 이름 목록입니다. 전체 목록은 [주제별 루틴 및 객체](https://numpy.org/doc/stable/reference/routines.html#routines)를 참조하세요.
> 
> - **Array Creation**
> 
> [`arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange"), [`array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array"), [`copy`](https://numpy.org/doc/stable/reference/generated/numpy.copy.html#numpy.copy "numpy.copy"), [`empty`](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty"), [`empty_like`](https://numpy.org/doc/stable/reference/generated/numpy.empty_like.html#numpy.empty_like "numpy.empty_like"), [`eye`](https://numpy.org/doc/stable/reference/generated/numpy.eye.html#numpy.eye "numpy.eye"), [`fromfile`](https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html#numpy.fromfile "numpy.fromfile"), [`fromfunction`](https://numpy.org/doc/stable/reference/generated/numpy.fromfunction.html#numpy.fromfunction "numpy.fromfunction"), [`identity`](https://numpy.org/doc/stable/reference/generated/numpy.identity.html#numpy.identity "numpy.identity"), [`linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace"), [`logspace`](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace"), [`mgrid`](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid"), [`ogrid`](https://numpy.org/doc/stable/reference/generated/numpy.ogrid.html#numpy.ogrid "numpy.ogrid"), [`ones`](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones"), [`ones_like`](https://numpy.org/doc/stable/reference/generated/numpy.ones_like.html#numpy.ones_like "numpy.ones_like"), [`r_`](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_"), [`zeros`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros"), [`zeros_like`](https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")
> 
> - **Conversions**
> 
> [`ndarray.astype`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.astype.html#numpy.ndarray.astype "numpy.ndarray.astype"), [`atleast_1d`](https://numpy.org/doc/stable/reference/generated/numpy.atleast_1d.html#numpy.atleast_1d "numpy.atleast_1d"), [`atleast_2d`](https://numpy.org/doc/stable/reference/generated/numpy.atleast_2d.html#numpy.atleast_2d "numpy.atleast_2d"), [`atleast_3d`](https://numpy.org/doc/stable/reference/generated/numpy.atleast_3d.html#numpy.atleast_3d "numpy.atleast_3d"), _mat_
> 
> - **Manipulations**
> 
> [`array_split`](https://numpy.org/doc/stable/reference/generated/numpy.array_split.html#numpy.array_split "numpy.array_split"), [`column_stack`](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack"), [`concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate"), [`diagonal`](https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html#numpy.diagonal "numpy.diagonal"), [`dsplit`](https://numpy.org/doc/stable/reference/generated/numpy.dsplit.html#numpy.dsplit "numpy.dsplit"), [`dstack`](https://numpy.org/doc/stable/reference/generated/numpy.dstack.html#numpy.dstack "numpy.dstack"), [`hsplit`](https://numpy.org/doc/stable/reference/generated/numpy.hsplit.html#numpy.hsplit "numpy.hsplit"), [`hstack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack"), [`ndarray.item`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.item.html#numpy.ndarray.item "numpy.ndarray.item"), [`newaxis`](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis"), [`ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel"), [`repeat`](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy.repeat "numpy.repeat"), [`reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape"), [`resize`](https://numpy.org/doc/stable/reference/generated/numpy.resize.html#numpy.resize "numpy.resize"), [`squeeze`](https://numpy.org/doc/stable/reference/generated/numpy.squeeze.html#numpy.squeeze "numpy.squeeze"), [`swapaxes`](https://numpy.org/doc/stable/reference/generated/numpy.swapaxes.html#numpy.swapaxes "numpy.swapaxes"), [`take`](https://numpy.org/doc/stable/reference/generated/numpy.take.html#numpy.take "numpy.take"), [`transpose`](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy.transpose "numpy.transpose"), [`vsplit`](https://numpy.org/doc/stable/reference/generated/numpy.vsplit.html#numpy.vsplit "numpy.vsplit"), [`vstack`](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
> 
> - **Questions**
> 
> [`all`](https://numpy.org/doc/stable/reference/generated/numpy.all.html#numpy.all "numpy.all"), [`any`](https://numpy.org/doc/stable/reference/generated/numpy.any.html#numpy.any "numpy.any"), [`nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero"), [`where`](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where "numpy.where")
> 
> - **Ordering**
> 
> [`argmax`](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html#numpy.argmax "numpy.argmax"), [`argmin`](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html#numpy.argmin "numpy.argmin"), [`argsort`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort"), [`max`](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max"), [`min`](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "numpy.min"), [`ptp`](https://numpy.org/doc/stable/reference/generated/numpy.ptp.html#numpy.ptp "numpy.ptp"), [`searchsorted`](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted "numpy.searchsorted"), [`sort`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
> 
> - **Operations**
> 
> [`choose`](https://numpy.org/doc/stable/reference/generated/numpy.choose.html#numpy.choose "numpy.choose"), [`compress`](https://numpy.org/doc/stable/reference/generated/numpy.compress.html#numpy.compress "numpy.compress"), [`cumprod`](https://numpy.org/doc/stable/reference/generated/numpy.cumprod.html#numpy.cumprod "numpy.cumprod"), [`cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum"), [`inner`](https://numpy.org/doc/stable/reference/generated/numpy.inner.html#numpy.inner "numpy.inner"), [`ndarray.fill`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.fill.html#numpy.ndarray.fill "numpy.ndarray.fill"), [`imag`](https://numpy.org/doc/stable/reference/generated/numpy.imag.html#numpy.imag "numpy.imag"), [`prod`](https://numpy.org/doc/stable/reference/generated/numpy.prod.html#numpy.prod "numpy.prod"), [`put`](https://numpy.org/doc/stable/reference/generated/numpy.put.html#numpy.put "numpy.put"), [`putmask`](https://numpy.org/doc/stable/reference/generated/numpy.putmask.html#numpy.putmask "numpy.putmask"), [`real`](https://numpy.org/doc/stable/reference/generated/numpy.real.html#numpy.real "numpy.real"), [`sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
> 
> - **Basic Statistics**
> 
> [`cov`](https://numpy.org/doc/stable/reference/generated/numpy.cov.html#numpy.cov "numpy.cov"), [`mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean"), [`std`](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std"), [`var`](https://numpy.org/doc/stable/reference/generated/numpy.var.html#numpy.var "numpy.var")
> 
> - **Basic Linear Algebra**
> 
> [`cross`](https://numpy.org/doc/stable/reference/generated/numpy.cross.html#numpy.cross "numpy.cross"), [`dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot"), [`outer`](https://numpy.org/doc/stable/reference/generated/numpy.outer.html#numpy.outer "numpy.outer"), [`linalg.svd`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html#numpy.linalg.svd "numpy.linalg.svd"), [`vdot`](https://numpy.org/doc/stable/reference/generated/numpy.vdot.html#numpy.vdot "numpy.vdot")

## 심화 (Less basic)

### 브로드캐스팅 규칙 (Broadcasting rules)

브로드캐스팅은 유니버설 함수가 정확히 같은 차원이 아닌 입력도 의미 있는 방식으로 처리할 수 있게 해줍니다.

브로드캐스팅의 첫 번째 규칙은 모든 입력 배열의 차원 수가 같지 않으면 모든 배열의 차원 수가 같을 때까지 작은 배열의 차원에 "1"이 반복적으로 앞에 붙는 것입니다.

두 번째 방송 규칙은 특정 차원을 따라 크기가 1인 배열은 해당 차원에서 가장 큰 차원을 가진 배열의 크기를 가진 것처럼 작동하도록 합니다. 배열 요소의 값은 '브로드캐스트' 배열의 경우 해당 차원을 따라 동일하다고 가정합니다.

브로드캐스트 규칙을 적용한 후에는 모든 배열의 크기가 일치해야 합니다. 자세한 내용은 [브로드캐스팅](https://numpy.org/doc/stable/user/basics.broadcasting.html#basics-broadcasting)에서 확인할 수 있습니다.

## 고급 인덱싱 및 인덱스 트릭 (Advanced indexing and index tricks)

- NumPy는 일반 파이썬 시퀀스보다 더 많은 인덱싱 기능을 제공합니다. 앞서 살펴본 것처럼 정수와 슬라이스로 인덱싱하는 것 외에도 정수 배열과 부울 배열로 배열을 인덱싱할 수 있습니다.

### 인덱스 배열로 인덱싱하기 (Indexing with arrays of indices)
- 일정한 인덱싱 집합을 리스트 또는 `ndarray` 형태로 지정해 해당 위치에 있는 `ndarray`를 반환하는 것을 **팬시 인덱싱 (Fancy Indexing)** 이라 합니다.
  
  예시:
  `array1[[2, 4, 7]] = [3, 5, 8]`

```python
>>> a = np.arange(12)**2  # the first 12 square numbers
>>> i = np.array([1, 1, 3, 8, 5])  # an array of indices
>>> a[i]  # the elements of `a` at the positions `i`
array([ 1,  1,  9, 64, 25])
>>>
>>> j = np.array([[3, 4], [9, 7]])  # a bidimensional array of indices
>>> a[j]  # the same shape as `j`
array([[ 9, 16],
       [81, 49]])
```

- 인덱싱된 배열 `a`가 다차원인 경우 인덱스의 단일 배열은 `a`의 첫 번째 차원을 참조합니다. 다음 예는 팔레트를 사용하여 레이블 이미지를 컬러 이미지로 변환하여 이 동작을 보여줍니다.

```python
>>> palette = np.array([[0, 0, 0],         # black
…                     [255, 0, 0],       # red
…                     [0, 255, 0],       # green
…                     [0, 0, 255],       # blue
…                     [255, 255, 255]])  # white
>>> image = np.array([[0, 1, 2, 0],  # each value corresponds to a color in the palette
…                   [0, 3, 4, 0]])
>>> palette[image]  # the (2, 4, 3) color image
array([[[  0,   0,   0],
        [255,   0,   0],
        [  0, 255,   0],
        [  0,   0,   0]],

       [[  0,   0,   0],
        [  0,   0, 255],
        [255, 255, 255],
        [  0,   0,   0]]])
```

- 둘 이상의 차원에 대한 인덱스를 제공할 수도 있습니다. 각 차원에 대한 인덱스 배열은 동일한 차원이어야 합니다.

```python
>>> a = np.arange(12).reshape(3, 4)
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>> i = np.array([[0, 1],  # indices for the first dim of `a`
…               [1, 2]])
>>> j = np.array([[2, 1],  # indices for the second dim
…               [3, 3]])
>>>
>>> a[i, j]  # i and j must have equal shape
array([[ 2,  5],
       [ 7, 11]])
>>>
>>> a[i, 2]
array([[ 2,  6],
       [ 6, 10]])
>>>
>>> a[:, j]
array([[[ 2,  1],
        [ 3,  3]],

       [[ 6,  5],
        [ 7,  7]],

       [[10,  9],
        [11, 11]]])
```

- 파이썬에서 `arr[i, j]`는 `arr[(i, j)]`와 완전히 동일하므로 `i`와 `j`를 `튜플`에 넣은 다음 이를 이용해 인덱싱을 수행할 수 있습니다.

```python
>>> l = (i, j)
>>> # equivalent to a[i, j]
>>> a[l]
array([[ 2,  5],
       [ 7, 11]])
```

- 그러나 이 배열은 `a`의 첫 번째 차원을 인덱싱하는 것으로 해석되므로 `i`와 `j`를 배열에 넣으면 이 작업을 수행할 수 없습니다.

```python
>>> s = np.array([i, j])
>>> # not what we want
>>> a[s]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: index 3 is out of bounds for axis 0 with size 3
>>> # same as `a[i, j]`
>>> a[tuple(s)]
array([[ 2,  5],
       [ 7, 11]])
```

- 배열을 사용한 인덱싱의 또 다른 일반적인 용도는 시간에 따른 시계열의 최대값을 검색하는 것입니다:

```python
>>> time = np.linspace(20, 145, 5)  # time scale
>>> data = np.sin(np.arange(20)).reshape(5, 4)  # 4 time-dependent series
>>> time
array([ 20.  ,  51.25,  82.5 , 113.75, 145.  ])
>>> data
array([[ 0.        ,  0.84147098,  0.90929743,  0.14112001],
       [-0.7568025 , -0.95892427, -0.2794155 ,  0.6569866 ],
       [ 0.98935825,  0.41211849, -0.54402111, -0.99999021],
       [-0.53657292,  0.42016704,  0.99060736,  0.65028784],
       [-0.28790332, -0.96139749, -0.75098725,  0.14987721]])
>>> # index of the maxima for each series
>>> ind = data.argmax(axis=0)
>>> ind
array([2, 0, 3, 1])
>>> # times corresponding to the maxima
>>> time_max = time[ind]
>>>
>>> data_max = data[ind, range(data.shape[1])]  # => data[ind[0], 0], data[ind[1], 1]…
>>> time_max
array([ 82.5 ,  20.  , 113.75,  51.25])
>>> data_max
array([0.98935825, 0.84147098, 0.99060736, 0.6569866 ])
>>> np.all(data_max == data.max(axis=0))
True
```

- 배열을 할당 대상으로 사용하여 인덱싱을 사용할 수도 있습니다:

```python
>>> a = np.arange(5)
>>> a
array([0, 1, 2, 3, 4])
>>> a[[1, 3, 4]] = 0
>>> a
array([0, 0, 2, 0, 0])
```

- 그러나 인덱스 목록에 반복이 포함된 경우 할당이 여러 번 수행되어 마지막 값이 남게 됩니다:

```python
>>> a = np.arange(5)
>>> a[[0, 0, 2]] = [1, 2, 3]
>>> a
array([2, 1, 3, 3, 4])
```

- 이는 충분히 합리적이지만 파이썬의 `+=` 구문을 사용하려는 경우 예상한 대로 작동하지 않을 수 있으므로 주의하세요:

```python
>>> a = np.arange(5)
>>> a[[0, 0, 2]] += 1
>>> a
array([1, 1, 3, 3, 4])
```

- 인덱스 목록에서 0이 두 번 나오더라도 0번째 요소는 한 번만 증가합니다. 이는 파이썬에서 `a += 1`이 `a = a + 1`과 같아야 하기 때문입니다.

### 부울 배열로 인덱싱하기 (Indexing with boolean arrays)
- 특정 조건에 해당하는지 여부인 `True`/`False` 값 인덱싱 집합을 기반으로 `True`에 해당하는 인덱스 위치에 있는 `ndarray`를 반환하는 것을 **불린 인덱싱 (Boolean Indexing)** 이라 합니다.
- 조건 필터링과 추출이 동시에 가능하여 매우 자주 사용되는 인덱싱 방식입니다.

```python
array1d = np.arange(start=1, stop=10)
target = []

for i in range(0, 9):
    if array1d[i] > 5:
        target.append(array1d[i])

array_selected = np.array(target)
```
- (정수) 인덱스 배열로 배열을 색인할 때는 선택할 인덱스 목록을 제공합니다. 부울 인덱스에서는 접근 방식이 다릅니다. 배열에서 원하는 항목과 원하지 않는 항목을 명시적으로 선택합니다.
- 부울 인덱싱에 대해 생각할 수 있는 가장 자연스러운 방법은 원래 배열과 같은 차원을 가진 부울 배열을 사용하는 것입니다:

```python
>>> a = np.arange(12).reshape(3, 4)
>>> b = a > 4
>>> b  # `b` is a boolean with `a`'s shape
array([[False, False, False, False],
       [False,  True,  True,  True],
       [ True,  True,  True,  True]])
>>> a[b]  # 1d array with the selected elements
array([ 5,  6,  7,  8,  9, 10, 11])
```

- 이 속성은 과제에서 매우 유용할 수 있습니다:

```python
>>> a[b] = 0  # All elements of `a` higher than 4 become 0
>>> a
array([[0, 1, 2, 3],
       [4, 0, 0, 0],
       [0, 0, 0, 0]])
```

- 다음 예시를 통해 부울 인덱싱을 사용하여 [만델브로 세트](https://en.wikipedia.org/wiki/Mandelbrot_set)의 이미지를 생성하는 방법을 확인할 수 있습니다:

```python
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> def mandelbrot(h, w, maxit=20, r=2):
… """Returns an image of the Mandelbrot fractal of size (h,w)."""
…     x = np.linspace(-2.5, 1.5, 4*h+1)
…     y = np.linspace(-1.5, 1.5, 3*w+1)
…     A, B = np.meshgrid(x, y)
…     C = A + B*1j
…     z = np.zeros_like(C)
…     divtime = maxit + np.zeros(z.shape, dtype=int)
…
…     for i in range(maxit):
…         z = z**2 + C
…         diverge = abs(z) > r                    # who is diverging
…         div_now = diverge & (divtime == maxit)  # who is diverging now
…         divtime[div_now] = i                    # note when
…         z[diverge] = r                          # avoid diverging too much
…
…     return divtime
>>> plt.clf()
>>> plt.imshow(mandelbrot(400, 400))
```

![../_images/quickstart-1.png](https://numpy.org/doc/stable/_images/quickstart-1.png)

- 부울로 인덱싱하는 두 번째 방법은 정수 인덱싱과 더 유사합니다. 배열의 각 차원에 대해 원하는 슬라이스를 선택하는 1D 부울 배열을 제공합니다:

```python
>>> a = np.arange(12).reshape(3, 4)
>>> b1 = np.array([False, True, True])         # first dim selection
>>> b2 = np.array([True, False, True, False])  # second dim selection
>>>
>>> a[b1, :]                                   # selecting rows
array([[ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>>
>>> a[b1]                                      # same thing
array([[ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>>
>>> a[:, b2]                                   # selecting columns
array([[ 0,  2],
       [ 4,  6],
       [ 8, 10]])
>>>
>>> a[b1, b2]                                  # a weird thing to do
array([ 4, 10])
```

- 1D 부울 배열의 길이는 슬라이스하려는 차원(또는 축)의 길이와 일치해야 한다는 점에 유의하세요. 앞의 예에서 `b1`은 길이가 3(`a`의 _rows_ 개수)이고, `b2`(길이 4)는 `a`의 두 번째 축(열)을 인덱싱하는 데 적합합니다.

### ix_() 함수 (The ix_() function)

- [`ix_`](https://numpy.org/doc/stable/reference/generated/numpy.ix_.html#numpy.ix_ "numpy.ix_") 함수를 사용하면 서로 다른 벡터를 결합하여 각 n-퍼릿에 대한 결과를 얻을 수 있습니다. 예를 들어 각 벡터 a, b, c에서 가져온 모든 삼중집합에 대해 $a+b*c$를 모두 계산하려는 경우입니다:

```python
>>> a = np.array([2, 3, 4, 5])
>>> b = np.array([8, 5, 4])
>>> c = np.array([5, 4, 6, 8, 3])
>>> ax, bx, cx = np.ix_(a, b, c)
>>> ax
array([[[2]],

       [[3]],

       [[4]],

       [[5]]])
>>> bx
array([[[8],
        [5],
        [4]]])
>>> cx
array([[[5, 4, 6, 8, 3]]])
>>> ax.shape, bx.shape, cx.shape
((4, 1, 1), (1, 3, 1), (1, 1, 5))
>>> result = ax + bx * cx
>>> result
array([[[42, 34, 50, 66, 26],
        [27, 22, 32, 42, 17],
        [22, 18, 26, 34, 14]],

       [[43, 35, 51, 67, 27],
        [28, 23, 33, 43, 18],
        [23, 19, 27, 35, 15]],

       [[44, 36, 52, 68, 28],
        [29, 24, 34, 44, 19],
        [24, 20, 28, 36, 16]],

       [[45, 37, 53, 69, 29],
        [30, 25, 35, 45, 20],
        [25, 21, 29, 37, 17]]])
>>> result[3, 2, 4]
17
>>> a[3] + b[2] * c[4]
17
```

- 다음과 같이 축소 기능을 구현할 수도 있습니다:

```python
>>> def ufunc_reduce(ufct, *vectors):
…    vs = np.ix_(*vectors)
…    r = ufct.identity
…    for v in vs:
…        r = ufct(r, v)
…    return r
```

- 로 설정한 다음 사용하세요:

```python
>>> ufunc_reduce(np.add, a, b, c)
array([[[15, 14, 16, 18, 13],
        [12, 11, 13, 15, 10],
        [11, 10, 12, 14,  9]],

       [[16, 15, 17, 19, 14],
        [13, 12, 14, 16, 11],
        [12, 11, 13, 15, 10]],

       [[17, 16, 18, 20, 15],
        [14, 13, 15, 17, 12],
        [13, 12, 14, 16, 11]],

       [[18, 17, 19, 21, 16],
        [15, 14, 16, 18, 13],
        [14, 13, 15, 17, 12]]])
```

이 버전의 reduce는 일반 ufunc.reduce에 비해 [방송 규칙](https://numpy.org/doc/stable/user/quickstart.html#broadcasting-rules)을 사용하여 출력 크기에 벡터 수를 곱한 크기의 인자 배열을 생성하지 않는다는 장점이 있습니다.

### 문자열로 인덱싱하기 (Indexing with strings)
- [구조화된 배열](https://numpy.org/doc/stable/user/basics.rec.html#structured-arrays)을 참조하세요.

## 트릭과 팁 (Tricks and tips)

> 여기에서는 짧고 유용한 팁 목록을 제공합니다.

### "자동" 재구성 (“Automatic” reshaping)

- 배열의 크기를 변경하려면 크기 중 하나를 생략하면 자동으로 추론됩니다:

```python
>>> a = np.arange(30)
>>> b = a.reshape((2, -1, 3))  # -1 means "whatever is needed"
>>> b.shape
(2, 5, 3)
>>> b
array([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8],
        [ 9, 10, 11],
        [12, 13, 14]],

       [[15, 16, 17],
        [18, 19, 20],
        [21, 22, 23],
        [24, 25, 26],
        [27, 28, 29]]])
```

### 벡터 스태킹 (Vector stacking)

- 크기가 같은 행 벡터의 목록에서 2D 배열을 만들려면 어떻게 해야 할까요? MATLAB에서는 `x`와 `y`가 같은 길이의 두 벡터인 경우 `m=[x;y]`만 수행하면 됩니다. NumPy에서는 스태킹을 수행하려는 차원에 따라 `column_stack`, `dstack`, `hstack` 및 `vstack` 함수를 통해 이 작업을 수행할 수 있습니다. 예를 들어

```python
>>> x = np.arange(0, 10, 2)
>>> y = np.arange(5)
>>> m = np.vstack([x, y])
>>> m
array([[0, 2, 4, 6, 8],
       [0, 1, 2, 3, 4]])
>>> xy = np.hstack([x, y])
>>> xy
array([0, 2, 4, 6, 8, 0, 1, 2, 3, 4])
```

- 2차원 이상의 함수 뒤에 숨어 있는 논리는 이상할 수 있습니다.

> [!seealso] 
> [NumPy for MATLAB users](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html)

### 히스토그램 (Histograms)

- 배열에 적용된 NumPy `histogram` 함수는 한 쌍의 벡터, 즉 배열의 히스토그램과 구간차원 가장자리의 벡터를 반환합니다. 주의: `matplotlib`에도 히스토그램을 작성하는 함수(Matlab에서 `hist`라고 함)가 있는데, 이는 NumPy의 그것과는 다릅니다. 가장 큰 차이점은 `pylab.hist`는 히스토그램을 자동으로 그리는 반면, `numpy.histogram`은 데이터만 생성한다는 점입니다.

```python
>>> import numpy as np
>>> rg = np.random.default_rng(1)
>>> import matplotlib.pyplot as plt
>>> # Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
>>> mu, sigma = 2, 0.5
>>> v = rg.normal(mu, sigma, 10000)
>>> # Plot a normalized histogram with 50 bins
>>> plt.hist(v, bins=50, density=True)       # matplotlib version (plot)
(array…)
>>> # Compute the histogram with numpy and then plot it
>>> (n, bins) = np.histogram(v, bins=50, density=True)  # NumPy version (no plot)
>>> plt.plot( * (bins[1:] + bins[:-1]), n) 
```

![../_images/quickstart-2.png](https://numpy.org/doc/stable/_images/quickstart-2.png)

- Matplotlib >=3.4에서는 `plt.stairs(n, bins)`를 사용할 수도 있습니다.

> [!example] 
> - The [Python tutorial](https://docs.python.org/tutorial/)
> - [NumPy reference](https://numpy.org/doc/stable/reference/index.html#reference)
> - [SciPy Tutorial](https://docs.scipy.org/doc/scipy/tutorial/index.html)
> - [SciPy Lecture Notes](https://scipy-lectures.org/)
> - A [matlab, R, IDL, NumPy/SciPy dictionary](https://mathesaurus.sourceforge.net/)
> - [tutorial-svd](https://numpy.org/numpy-tutorials/content/tutorial-svd.html "(in NumPy tutorials)")
> 



---
## 참조
[NumPy fundamentals — NumPy v2.0 Manual](https://numpy.org/doc/stable/user/basics.html)
[NumPy: the absolute basics for beginners — NumPy v2.0 Manual](https://numpy.org/doc/stable/user/absolute_beginners.html)

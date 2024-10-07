---
title: "[Pandas] 데이터 구조 (Data Structures)"
excerpt: 에 대한 문서
categories:
  - Pandas
tags:
  - Pandas
  - Series
  - DataFrame
last_modified_at: 2024-03-01T00:00:00-00:00
link: https://pandas.pydata.org/docs/user_guide/dsintro.html
상위 항목: "[[pandas_home|판다스 (Pandas)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`



---

## 기본 데이터 구조 (Basic data structures)

> [!summary] 
> - Pandas는 데이터를 처리하기 위한 두 가지 유형의 클래스를 제공합니다:
> 1. [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series"): 모든 유형의 데이터를 포함하는 1차원 레이블이 지정된 배열로
>     정수, 문자열, 파이썬 객체 등 모든 유형의 데이터를 저장하는 1차원 레이블 배열입니다.
> 2. [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame"): 2차원 배열이나 행과 열이 있는 테이블처럼 데이터를 보관하는 2차원 데이터 구조입니다. Index는 오직 식별용으로 사용되며 연산에서 제외됩니다.

> [!NOTE] 인덱스 (Index)
> - Index 객체는 RDBMS의 PK(Primary Key)와 유사하게 레코드를 고유하게 식별하는 객체입니다. (별도의 컬럼값이 아닙니다.)
> - 오직 식별용으로만 사용되며, Series 객체에 연산 함수를 적용할 때 Index는 연산에서 제외됩니다.
> - Index만 추출하려면 `.index` 속성으로 접근해야 합니다.
> - 고유한 값만 유지한다면 숫자형이 아닌 문자형/Datetime도 가능합니다.
> - `Series`나 `DataFrame`의 `reset_index()` 메소드를 실행하면 인덱스를 새로 할당하며 기존 인덱스는 'index'라는 컬럼 명으로 새로 추가합니다. 단, `drop` 옵션을 `True`로 설정하면 기존 인덱스를 제거합니다.

판다스의 기본 데이터 구조에 대한 간단하고 포괄적이지 않은 개요로 시작하겠습니다. 데이터 유형, 인덱싱, 축 라벨링 및 정렬에 대한 기본적인 동작은 모든 객체에 적용됩니다. 시작하려면 NumPy를 가져오고 판다스를 네임스페이스에 로드하세요:

```python
import numpy as np
import pandas as pd
```

기본적으로 데이터 정렬은 본질적입니다. 레이블과 데이터 간의 연결은 사용자가 명시적으로 끊지 않는 한 유지됩니다.

데이터 구조에 대해 간단히 소개한 다음, 기능과 메서드의 모든 광범위한 범주를 별도의 섹션에서 다루겠습니다.

## 시리즈 (Series)

시리즈는 모든 데이터 유형(정수, 문자열, 부동 소수점 숫자, Python 객체 등)을 보유할 수 있는 1차원 레이블 배열입니다. 축 레이블을 총칭하여 인덱스라고 합니다. 시리즈를 만드는 기본 방법은 다음과 같습니다:

```python
s = pd.Series(data, index=index)
```

여기서 data는 다음과 같은 여러 가지 형태일 수 있습니다:

- Python 딕셔너리
- ndarray
- 스칼라 값 (예: 5)

전달된 인덱스는 축 레이블의 목록입니다. 따라서 이는 데이터가 무엇인지에 따라 몇 가지 경우로 나뉩니다:

**ndarray에서**

data가 ndarray인 경우, 인덱스는 data와 같은 길이여야 합니다. 인덱스가 전달되지 않으면 `[0, …, len(data) - 1]` 값을 가진 인덱스가 생성됩니다.

```python
s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])

s
```

출력:
```
a    0.469112
b   -0.282863
c   -1.509059
d   -1.135632
e    1.212112
dtype: float64
```

```python
s.index
```

출력:
```
Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
```

```python
pd.Series(np.random.randn(5))
```

출력:
```
0   -0.173215
1    0.119209
2   -1.044236
3   -0.861849
4   -2.104569
dtype: float64
```

> 판다스는 고유하지 않은 인덱스 값을 지원합니다. 중복 인덱스 값을 지원하지 않는 작업을 시도하면 그 시점에 예외가 발생합니다.

**딕셔너리에서**

시리즈는 딕셔너리에서 인스턴스화될 수 있습니다:

```python
d = {"b": 1, "a": 0, "c": 2}
pd.Series(d)
```

출력:
```
b    1
a    0
c    2
dtype: int64
```

인덱스가 전달되면 인덱스의 레이블에 해당하는 데이터의 값이 추출됩니다.

```python
d = {"a": 0.0, "b": 1.0, "c": 2.0}
pd.Series(d)
```

출력:
```
a    0.0
b    1.0
c    2.0
dtype: float64
```

```python
pd.Series(d, index=["b", "c", "d", "a"])
```

출력:
```
b    1.0
c    2.0
d    NaN
a    0.0
dtype: float64
```

> NaN(숫자가 아님)은 판다스에서 사용되는 표준 결측 데이터 표시입니다.

**스칼라 값에서**

data가 스칼라 값인 경우 인덱스를 제공해야 합니다. 값은 인덱스의 길이와 일치하도록 반복됩니다.

```python
pd.Series(5.0, index=["a", "b", "c", "d", "e"])
```

출력:
```
a    5.0
b    5.0
c    5.0
d    5.0
e    5.0
dtype: float64
```

### 시리즈는 ndarray와 유사합니다 (Series is ndarray-like)

시리즈는 ndarray와 매우 유사하게 작동하며 대부분의 NumPy 함수에 유효한 인수입니다. 그러나 슬라이싱과 같은 작업은 인덱스도 슬라이스합니다.

```python
s.iloc[0]
```

출력:
```
0.4691122999071863
```

```python
s.iloc[:3]
```

출력:
```
a    0.469112
b   -0.282863
c   -1.509059
dtype: float64
```

```python
s[s > s.median()]
```

출력:
```
a    0.469112
e    1.212112
dtype: float64
```

```python
s.iloc[[4, 3, 1]]
```

출력:
```
e    1.212112
d   -1.135632
b   -0.282863
dtype: float64
```

```python
np.exp(s)
```

출력:
```
a    1.598575
b    0.753623
c    0.221118
d    0.321219
e    3.360575
dtype: float64
```

> `s.iloc[[4, 3, 1]]`와 같은 배열 기반 인덱싱은 인덱싱 섹션에서 다룰 것입니다.

NumPy 배열과 마찬가지로 판다스 시리즈에는 단일 dtype이 있습니다.

```python
s.dtype
```

출력:
```
dtype('float64')
```

이는 종종 NumPy dtype입니다. 그러나 판다스와 서드파티 라이브러리는 몇 가지 경우에 NumPy의 유형 시스템을 확장하며, 이 경우 dtype은 ExtensionDtype이 됩니다. 판다스 내의 일부 예로는 범주형 데이터와 Nullable 정수 데이터 유형이 있습니다. 자세한 내용은 dtypes를 참조하세요.

시리즈를 지원하는 실제 배열이 필요한 경우 Series.array를 사용하세요.

```python
s.array
```

출력:
```
<NumpyExtensionArray>
[ 0.4691122999071863, -0.2828633443286633, -1.5090585031735124,
 -1.1356323710171934,  1.2121120250208506]
Length: 5, dtype: float64
```

배열에 접근하는 것은 인덱스 없이 어떤 작업을 수행해야 할 때 유용할 수 있습니다(예를 들어, 자동 정렬을 비활성화하기 위해).

Series.array는 항상 ExtensionArray가 됩니다. 간단히 말해, ExtensionArray는 numpy.ndarray와 같은 하나 이상의 구체적인 배열을 감싸는 얇은 래퍼입니다. 판다스는 ExtensionArray를 가져와 시리즈나 데이터프레임의 열에 저장하는 방법을 알고 있습니다. 자세한 내용은 dtypes를 참조하세요.

시리즈가 ndarray와 유사하지만 실제 ndarray가 필요한 경우 Series.to_numpy()를 사용하세요.

```python
s.to_numpy()
```

출력:
```
array([ 0.4691, -0.2829, -1.5091, -1.1356,  1.2121])
```

시리즈가 ExtensionArray로 지원되는 경우에도 Series.to_numpy()는 NumPy ndarray를 반환합니다.


### Series는 딕셔너리와 유사함 (Series is dict-like)

Series는 고정 크기의 딕셔너리와 유사하여 인덱스 레이블로 값을 가져오고 설정할 수 있습니다:

```python
In [21]: s["a"]
Out[21]: 0.4691122999071863

In [22]: s["e"] = 12.0

In [23]: s
Out[23]: 
a     0.469112
b    -0.282863
c    -1.509059
d    -1.135632
e    12.000000
dtype: float64

In [24]: "e" in s
Out[24]: True

In [25]: "f" in s
Out[25]: False
```

레이블이 인덱스에 포함되지 않은 경우 예외가 발생합니다:

```python
In [26]: s["f"]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
File ~/work/pandas/pandas/pandas/core/indexes/base.py:3805, in Index.get_loc(self, key)
   3804 try:
-> 3805     return self._engine.get_loc(casted_key)
   3806 except KeyError as err:

File index.pyx:167, in pandas._libs.index.IndexEngine.get_loc()

File index.pyx:196, in pandas._libs.index.IndexEngine.get_loc()

File pandas/_libs/hashtable_class_helper.pxi:7081, in pandas._libs.hashtable.PyObjectHashTable.get_item()

File pandas/_libs/hashtable_class_helper.pxi:7089, in pandas._libs.hashtable.PyObjectHashTable.get_item()

KeyError: 'f'

The above exception was the direct cause of the following exception:

KeyError                                  Traceback (most recent call last)
Cell In[26], line 1
----> 1 s["f"]

File ~/work/pandas/pandas/pandas/core/series.py:1121, in Series.__getitem__(self, key)
   1118     return self._values[key]
   1120 elif key_is_scalar:
-> 1121     return self._get_value(key)
   1123 # Convert generator to list before going through hashable part
   1124 # (We will iterate through the generator there to check for slices)
   1125 if is_iterator(key):

File ~/work/pandas/pandas/pandas/core/series.py:1237, in Series._get_value(self, label, takeable)
   1234     return self._values[label]
   1236 # Similar to Index.get_value, but we do not fall back to positional
-> 1237 loc = self.index.get_loc(label)
   1239 if is_integer(loc):
   1240     return self._values[loc]

File ~/work/pandas/pandas/pandas/core/indexes/base.py:3812, in Index.get_loc(self, key)
   3807     if isinstance(casted_key, slice) or (
   3808         isinstance(casted_key, abc.Iterable)
   3809         and any(isinstance(x, slice) for x in casted_key)
   3810     ):
   3811         raise InvalidIndexError(key)
-> 3812     raise KeyError(key) from err
   3813 except TypeError:
   3814     # If we have a listlike key, _check_indexing_error will raise
   3815     #  InvalidIndexError. Otherwise we fall through and re-raise
   3816     #  the TypeError.
   3817     self._check_indexing_error(key)

KeyError: 'f'
```

Series.get() 메서드를 사용하면 누락된 레이블은 None 또는 지정된 기본값을 반환합니다:

```python
In [27]: s.get("f")

In [28]: s.get("f", np.nan)
Out[28]: nan
```

이러한 레이블은 속성으로도 접근할 수 있습니다.

### Series와의 벡터화 연산 및 레이블 정렬 (Vectorized operations and label alignment with Series)

원시 NumPy 배열로 작업할 때는 일반적으로 값별로 반복할 필요가 없습니다. pandas에서 Series로 작업할 때도 마찬가지입니다. Series는 ndarray를 기대하는 대부분의 NumPy 메서드에 전달될 수 있습니다.

```python
In [29]: s + s
Out[29]: 
a     0.938225
b    -0.565727
c    -3.018117
d    -2.271265
e    24.000000
dtype: float64

In [30]: s * 2
Out[30]: 
a     0.938225
b    -0.565727
c    -3.018117
d    -2.271265
e    24.000000
dtype: float64

In [31]: np.exp(s)
Out[31]: 
a         1.598575
b         0.753623
c         0.221118
d         0.321219
e    162754.791419
dtype: float64
```

Series와 ndarray의 주요 차이점은 Series 간의 연산이 자동으로 레이블을 기반으로 데이터를 정렬한다는 것입니다. 따라서 관련된 Series가 동일한 레이블을 가지고 있는지 고려하지 않고도 계산을 작성할 수 있습니다.

```python
In [32]: s.iloc[1:] + s.iloc[:-1]
Out[32]: 
a         NaN
b   -0.565727
c   -3.018117
d   -2.271265
e         NaN
dtype: float64
```

정렬되지 않은 Series 간의 연산 결과는 관련된 인덱스의 합집합을 가집니다. 한 Series나 다른 Series에서 레이블을 찾을 수 없는 경우 결과는 누락된 NaN으로 표시됩니다. 명시적인 데이터 정렬 없이 코드를 작성할 수 있다는 것은 대화형 데이터 분석 및 연구에서 엄청난 자유와 유연성을 제공합니다. pandas 데이터 구조의 통합된 데이터 정렬 기능은 pandas를 레이블이 있는 데이터 작업을 위한 대부분의 관련 도구와 차별화합니다.

참고: 일반적으로 우리는 정보 손실을 피하기 위해 인덱스가 다른 객체 간의 연산의 기본 결과가 인덱스의 합집합이 되도록 선택했습니다. 계산의 일부로 데이터가 누락되었더라도 인덱스 레이블을 갖는 것은 일반적으로 중요한 정보입니다. 물론 dropna 함수를 통해 누락된 데이터가 있는 레이블을 삭제할 수 있는 옵션이 있습니다.

### 이름 속성 (Name attribute)

Series에는 name 속성도 있습니다:

```python
In [33]: s = pd.Series(np.random.randn(5), name="something")

In [34]: s
Out[34]: 
0   -0.494929
1    1.071804
2    0.721555
3   -0.706771
4   -1.039575
Name: something, dtype: float64

In [35]: s.name
Out[35]: 'something'
```

Series의 name은 많은 경우에 자동으로 할당될 수 있습니다. 특히 DataFrame에서 단일 열을 선택할 때 name은 열 레이블로 할당됩니다.

`pandas.Series.rename()` 메서드를 사용하여 Series의 이름을 바꿀 수 있습니다.

```python
In [36]: s2 = s.rename("different")

In [37]: s2.name
Out[37]: 'different'
```

s와 s2가 서로 다른 객체를 참조한다는 점에 유의하세요.

## DataFrame (데이터프레임)

DataFrame은 잠재적으로 서로 다른 유형의 열을 가진 2차원 라벨링된 데이터 구조입니다. 스프레드시트나 SQL 테이블, 또는 Series 객체의 딕셔너리로 생각할 수 있습니다. 일반적으로 가장 흔히 사용되는 pandas 객체입니다. Series와 마찬가지로 DataFrame은 다양한 종류의 입력을 받아들입니다:

- 1D ndarray, 리스트, 딕셔너리 또는 Series의 딕셔너리
- 2D numpy.ndarray
- 구조화되거나 레코드 형태의 ndarray
- Series
- 다른 DataFrame

데이터와 함께 선택적으로 index(행 라벨)와 columns(열 라벨) 인수를 전달할 수 있습니다. index 및/또는 columns를 전달하면 결과 DataFrame의 index 및/또는 `columns`를 보장하게 됩니다. 따라서 Series의 딕셔너리와 특정 index를 함께 전달하면 전달된 index와 일치하지 않는 모든 데이터는 버려집니다.

축 라벨이 전달되지 않으면 일반적인 규칙에 따라 입력 데이터로부터 구성됩니다.

### Series나 딕셔너리의 딕셔너리로부터 (From dict of Series or dicts)

결과 index는 다양한 Series의 index의 합집합이 됩니다. 중첩된 딕셔너리가 있다면 먼저 Series로 변환됩니다. `columns`가 전달되지 않으면 `columns`는 정렬된 딕셔너리 키 목록이 됩니다.

```python
d = {
   "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
   "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}

df = pd.DataFrame(d)

df
```

```
   one  two
a  1.0  1.0
b  2.0  2.0
c  3.0  3.0
d  NaN  4.0
```

```python
pd.DataFrame(d, index=["d", "b", "a"])
```

```
   one  two
d  NaN  4.0
b  2.0  2.0
a  1.0  1.0
```

```python
pd.DataFrame(d, index=["d", "b", "a"], columns=["two", "three"])
```

```
   two three
d  4.0   NaN
b  2.0   NaN
a  1.0   NaN
```

행과 열 라벨은 각각 `index`와 `columns` 속성에 접근하여 얻을 수 있습니다:

> 특정 열 집합이 데이터 딕셔너리와 함께 전달될 때, 전달된 열이 딕셔너리의 키를 재정의합니다.

```python
df.index
```

```
Index(['a', 'b', 'c', 'd'], dtype='object')
```

```python
df.columns
```

```
Index(['one', 'two'], dtype='object')
```

### ndarray/리스트의 딕셔너리로부터 (From dict of ndarrays / lists)

모든 ndarray는 같은 길이를 공유해야 합니다. index가 전달되면 배열의 길이와 동일해야 합니다. index가 전달되지 않으면 결과는 range(n)이 됩니다. 여기서 n은 배열의 길이입니다.

```python
d = {"one": [1.0, 2.0, 3.0, 4.0], "two": [4.0, 3.0, 2.0, 1.0]}

pd.DataFrame(d)
```

```
   one  two
0  1.0  4.0
1  2.0  3.0
2  3.0  2.0
3  4.0  1.0
```

```python
pd.DataFrame(d, index=["a", "b", "c", "d"])
```

```
   one  two
a  1.0  4.0
b  2.0  3.0
c  3.0  2.0
d  4.0  1.0
```

### 구조화된 또는 레코드 배열로부터 (From structured or record array)

이 경우는 배열의 딕셔너리와 동일하게 처리됩니다.

```python
data = np.zeros((2,), dtype=[("A", "i4"), ("B", "f4"), ("C", "a10")])

data[:] = [(1, 2.0, "Hello"), (2, 3.0, "World")]

pd.DataFrame(data)
```

```
   A    B         C
0  1  2.0  b'Hello'
1  2  3.0  b'World'
```

```python
pd.DataFrame(data, index=["first", "second"])
```

```
        A    B         C
first   1  2.0  b'Hello'
second  2  3.0  b'World'
```

```python
pd.DataFrame(data, columns=["C", "A", "B"])
```

```
          C  A    B
0  b'Hello'  1  2.0
1  b'World'  2  3.0
```

> DataFrame은 2차원 NumPy ndarray와 정확히 동일하게 작동하도록 의도되지 않았습니다.

### 딕셔너리 리스트로부터 (From a list of dicts)

```python
data2 = [{"a": 1, "b": 2}, {"a": 5, "b": 10, "c": 20}]

pd.DataFrame(data2)
```

```
   a   b     c
0  1   2   NaN
1  5  10  20.0
```

```python
pd.DataFrame(data2, index=["first", "second"])
```

```
        a   b     c
first   1   2   NaN
second  5  10  20.0
```

```python
pd.DataFrame(data2, columns=["a", "b"])
```

```
   a   b
0  1   2
1  5  10
```

### 튜플의 딕셔너리로부터 (From a dict of tuples)

튜플 딕셔너리를 전달하여 자동으로 MultiIndexed 프레임을 생성할 수 있습니다.

```python
pd.DataFrame(
   {
       ("a", "b"): {("A", "B"): 1, ("A", "C"): 2},
       ("a", "a"): {("A", "C"): 3, ("A", "B"): 4},
       ("a", "c"): {("A", "B"): 5, ("A", "C"): 6},
       ("b", "a"): {("A", "C"): 7, ("A", "B"): 8},
       ("b", "b"): {("A", "D"): 9, ("A", "B"): 10},
   }
)
```

```
       a              b      
       b    a    c    a     b
A B  1.0  4.0  5.0  8.0  10.0
  C  2.0  3.0  6.0  7.0   NaN
  D  NaN  NaN  NaN  NaN   9.0
```

### Series로부터 (From a Series)

결과는 입력 Series와 동일한 index를 가진 DataFrame이 되며, 하나의 열을 가집니다. 열 이름은 Series의 원래 이름이 됩니다(다른 열 이름이 제공되지 않은 경우에만).

```python
ser = pd.Series(range(3), index=list("abc"), name="ser")

pd.DataFrame(ser)
```

```
   ser
a    0
b    1
c    2
```

### namedtuple 리스트로부터 (From a list of namedtuples)

리스트의 첫 번째 namedtuple의 필드 이름이 DataFrame의 열을 결정합니다. 나머지 namedtuple(또는 튜플)은 단순히 언패킹되어 그 값들이 DataFrame의 행에 채워집니다. 이러한 튜플 중 하나라도 첫 번째 namedtuple보다 짧으면 해당 행의 나머지 열은 결측값으로 표시됩니다. 첫 번째 namedtuple보다 길면 ValueError가 발생합니다.

```python
from collections import namedtuple

Point = namedtuple("Point", "x y")

pd.DataFrame([Point(0, 0), Point(0, 3), (2, 3)])
```

```
   x  y
0  0  0
1  0  3
2  2  3
```

```python
Point3D = namedtuple("Point3D", "x y z")

pd.DataFrame([Point3D(0, 0, 0), Point3D(0, 3, 5), Point(2, 3)])
```

```
   x  y    z
0  0  0  0.0
1  0  3  5.0
2  2  3  NaN
```

### dataclass 리스트로부터 (From a list of dataclasses)

PEP557에서 소개된 Data Classes는 DataFrame 생성자에 전달될 수 있습니다. dataclass 리스트를 전달하는 것은 딕셔너리 리스트를 전달하는 것과 동일합니다.

리스트의 모든 값은 dataclass여야 하며, 리스트에 유형을 혼합하면 TypeError가 발생한다는 점에 유의하세요.

```python
from dataclasses import make_dataclass

Point = make_dataclass("Point", [("x", int), ("y", int)])

pd.DataFrame([Point(0, 0), Point(0, 3), Point(2, 3)])
```

```
   x  y
0  0  0
1  0  3
2  2  3
```

> [!NOTE] 결측 데이터 (Missing data)
> 
> 결측 데이터가 있는 DataFrame을 구성하려면 np.nan을 사용하여 결측값을 표현합니다. 또는 DataFrame 생성자의 data 인수로 numpy.MaskedArray를 전달할 수 있으며, 마스킹된 항목은 결측으로 간주됩니다. 자세한 내용은 결측 데이터를 참조하세요.

### 대체 생성자 (Alternate constructors)

`DataFrame.from_dict`

`DataFrame.from_dict()`는 딕셔너리의 딕셔너리 또는 배열 같은 시퀀스의 딕셔너리를 받아 DataFrame을 반환합니다. 기본적으로 'columns'로 설정되어 있지만 딕셔너리 키를 행 라벨로 사용하기 위해 'index'로 설정할 수 있는 orient 매개변수를 제외하고는 DataFrame 생성자와 동일하게 작동합니다.

```python
pd.DataFrame.from_dict(dict([("A", [1, 2, 3]), ("B", [4, 5, 6])]))
```

```
   A  B
0  1  4
1  2  5
2  3  6
```

`orient='index'`를 전달하면 키가 행 라벨이 됩니다. 이 경우 원하는 열 이름도 전달할 수 있습니다:

```python
pd.DataFrame.from_dict(
   dict([("A", [1, 2, 3]), ("B", [4, 5, 6])]),
   orient="index",
   columns=["one", "two", "three"],
)
```

```
   one  two  three
A    1    2      3
B    4    5      6
```

`DataFrame.from_records`

`DataFrame.from_records()`는 튜플 리스트 또는 구조화된 dtype을 가진 ndarray를 받습니다. 결과 DataFrame의 index가 구조화된 dtype의 특정 필드가 될 수 있다는 점을 제외하고는 일반 DataFrame 생성자와 유사하게 작동합니다.

```python
data
```

```
array([(1, 2., b'Hello'), (2, 3., b'World')],
      dtype=[('A', '<i4'), ('B', '<f4'), ('C', 'S10')])
```

```python
pd.DataFrame.from_records(data, index="C")
```

```
          A    B
C               
b'Hello'  1  2.0
b'World'  2  3.0
```

### 열 선택, 추가, 삭제 (Column selection, addition, deletion)

[`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame)을 의미상 같은 인덱스를 가진 [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series) 객체들의 딕셔너리처럼 다룰 수 있습니다. 열을 가져오고, 설정하고, 삭제하는 작업은 딕셔너리의 유사한 연산과 같은 구문으로 수행됩니다:

```python
In [72]: df["one"]
Out[72]: 
a    1.0
b    2.0
c    3.0
d    NaN
Name: one, dtype: float64

In [73]: df["three"] = df["one"] * df["two"]

In [74]: df["flag"] = df["one"] > 2

In [75]: df
Out[75]: 
   one  two  three   flag
a  1.0  1.0    1.0  False
b  2.0  2.0    4.0  False
c  3.0  3.0    9.0   True
d  NaN  4.0    NaN  False
```

딕셔너리와 마찬가지로 열을 삭제하거나 팝할 수 있습니다:

```python
In [76]: del df["two"]

In [77]: three = df.pop("three")

In [78]: df
Out[78]: 
   one   flag
a  1.0  False
b  2.0  False
c  3.0   True
d  NaN  False
```

스칼라 값을 삽입할 때는 자연스럽게 열 전체에 채워집니다:

```python
In [79]: df["foo"] = "bar"

In [80]: df
Out[80]: 
   one   flag  foo
a  1.0  False  bar
b  2.0  False  bar
c  3.0   True  bar
d  NaN  False  bar
```

[`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame)과 같은 인덱스를 갖지 않은 [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series)를 삽입할 때는 DataFrame의 인덱스에 맞춰집니다:

```python
In [81]: df["one_trunc"] = df["one"][:2]

In [82]: df
Out[82]: 
   one   flag  foo  one_trunc
a  1.0  False  bar        1.0
b  2.0  False  bar        2.0
c  3.0   True  bar        NaN
d  NaN  False  bar        NaN
```

원시 ndarray도 삽입할 수 있지만 길이가 DataFrame의 인덱스 길이와 일치해야 합니다.

기본적으로 열은 끝에 삽입됩니다. [`DataFrame.insert()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html#pandas.DataFrame.insert)는 열의 특정 위치에 삽입합니다:

```python
In [83]: df.insert(1, "bar", df["one"])

In [84]: df
Out[84]: 
   one  bar   flag  foo  one_trunc
a  1.0  1.0  False  bar        1.0
b  2.0  2.0  False  bar        2.0
c  3.0  3.0   True  bar        NaN
d  NaN  NaN  False  bar        NaN
```

### 메서드 체인에서 새 열 할당하기 (Assigning new columns in method chains)

[dplyr의](https://dplyr.tidyverse.org/reference/mutate.html) mutate 동사에서 영감을 받아, DataFrame에는 기존 열로부터 파생될 수 있는 새 열을 쉽게 만들 수 있는 [`assign()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html#pandas.DataFrame.assign) 메서드가 있습니다.

```python
In [85]: iris = pd.read_csv("data/iris.data")

In [86]: iris.head()
Out[86]: 
   SepalLength  SepalWidth  PetalLength  PetalWidth         Name
0          5.1         3.5          1.4         0.2  Iris-setosa
1          4.9         3.0          1.4         0.2  Iris-setosa
2          4.7         3.2          1.3         0.2  Iris-setosa
3          4.6         3.1          1.5         0.2  Iris-setosa
4          5.0         3.6          1.4         0.2  Iris-setosa

In [87]: iris.assign(sepal_ratio=iris["SepalWidth"] / iris["SepalLength"]).head()
Out[87]: 
   SepalLength  SepalWidth  PetalLength  PetalWidth         Name  sepal_ratio
0          5.1         3.5          1.4         0.2  Iris-setosa     0.686275
1          4.9         3.0          1.4         0.2  Iris-setosa     0.612245
2          4.7         3.2          1.3         0.2  Iris-setosa     0.680851
3          4.6         3.1          1.5         0.2  Iris-setosa     0.673913
4          5.0         3.6          1.4         0.2  Iris-setosa     0.720000
```

위의 예에서는 미리 계산된 값을 삽입했습니다. 할당되는 DataFrame에 대해 평가될 한 개의 인수를 가진 함수를 전달할 수도 있습니다.

```python
In [88]: iris.assign(sepal_ratio=lambda x: (x["SepalWidth"] / x["SepalLength"])).head()
Out[88]: 
   SepalLength  SepalWidth  PetalLength  PetalWidth         Name  sepal_ratio
0          5.1         3.5          1.4         0.2  Iris-setosa     0.686275
1          4.9         3.0          1.4         0.2  Iris-setosa     0.612245
2          4.7         3.2          1.3         0.2  Iris-setosa     0.680851
3          4.6         3.1          1.5         0.2  Iris-setosa     0.673913
4          5.0         3.6          1.4         0.2  Iris-setosa     0.720000
```

[`assign()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html#pandas.DataFrame.assign)은 항상 데이터의 복사본을 반환하며, 원본 DataFrame은 변경되지 않습니다.

실제 삽입할 값이 아닌 호출 가능한 객체를 전달하는 것은 DataFrame에 대한 참조가 없을 때 유용합니다. 이는 [`assign()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html#pandas.DataFrame.assign)을 연산 체인에서 사용할 때 흔합니다. 예를 들어, DataFrame을 Sepal Length가 5보다 큰 관측치로만 제한하고, 비율을 계산한 다음 플롯할 수 있습니다:

```python
In [89]: (
   ....:    iris.query("SepalLength > 5")
   ....:    .assign(
   ....:        SepalRatio=lambda x: x.SepalWidth / x.SepalLength,
   ....:        PetalRatio=lambda x: x.PetalWidth / x.PetalLength,
   ....:    )
   ....:    .plot(kind="scatter", x="SepalRatio", y="PetalRatio")
   ....: )
   ....: 
Out[89]: <Axes: xlabel='SepalRatio', ylabel='PetalRatio'>
```

함수가 전달되므로 할당되는 DataFrame에 대해 함수가 계산됩니다. 중요한 점은 이것이 sepal length가 5보다 큰 행으로 필터링된 DataFrame이라는 것입니다. 필터링이 먼저 일어나고, 그 다음 비율 계산이 이루어집니다. 이는 필터링된 DataFrame에 대한 참조를 사용할 수 없는 경우의 예입니다.

[`assign()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html#pandas.DataFrame.assign)의 함수 시그니처는 단순히 `**kwargs`입니다. 키는 새 필드의 열 이름이고, 값은 삽입할 값(예: [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series) 또는 NumPy 배열) 또는 [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame)에 대해 호출될 한 개의 인수를 가진 함수입니다. 원본 [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame)의 복사본이 반환되며, 새 값이 삽입됩니다.

`**kwargs`의 순서는 유지됩니다. 이를 통해 종속적 할당이 가능하며, `**kwargs`의 후반부 표현식에서 같은 [`assign()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html#pandas.DataFrame.assign)에서 앞서 생성된 열을 참조할 수 있습니다.

```python
In [90]: dfa = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

In [91]: dfa.assign(C=lambda x: x["A"] + x["B"], D=lambda x: x["A"] + x["C"])
Out[91]: 
   A  B  C   D
0  1  4  5   6
1  2  5  7   9
2  3  6  9  12
```

두 번째 표현식에서 `x['C']`는 새로 생성된 열을 참조하며, 이는 `dfa['A'] + dfa['B']`와 같습니다.

### 인덱싱 / 선택 (Indexing / selection)

인덱싱의 기본 사항은 다음과 같습니다:

|연산|구문|결과|
|---|---|---|
|열 선택|df[col]|Series|
|레이블로 행 선택|df.loc[label]|Series|
|정수 위치로 행 선택|df.iloc[loc]|Series|
|행 슬라이싱|df[5:10]|DataFrame|
|불리언 벡터로 행 선택|df[bool_vec]|DataFrame|

예를 들어, 행 선택은 [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame)의 열을 인덱스로 하는 [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series)를 반환합니다:

```python
In [92]: df.loc["b"]
Out[92]: 
one            2.0
bar            2.0
flag         False
foo            bar
one_trunc      2.0
Name: b, dtype: object

In [93]: df.iloc[2]
Out[93]: 
one           3.0
bar           3.0
flag         True
foo           bar
one_trunc     NaN
Name: c, dtype: object
```

더 복잡한 레이블 기반 인덱싱과 슬라이싱에 대한 자세한 내용은 [인덱싱 섹션](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing)을 참조하세요. 새로운 레이블 세트에 대한 재인덱싱/적합화의 기본 사항은 [재인덱싱 섹션](https://pandas.pydata.org/docs/user_guide/basics.html#basics-reindexing)에서 다룹니다.

### 데이터 정렬 및 산술 연산 (Data alignment and arithmetic)

DataFrame 객체 간의 데이터 정렬은 열과 인덱스(행 레이블) 모두에서 자동으로 이루어집니다. 결과 객체는 열과 행 레이블의 합집합을 가지게 됩니다.

```python
df = pd.DataFrame(np.random.randn(10, 4), columns=["A", "B", "C", "D"])

df2 = pd.DataFrame(np.random.randn(7, 3), columns=["A", "B", "C"])

df + df2
```

DataFrame과 Series 간의 연산을 수행할 때, 기본 동작은 Series 인덱스를 DataFrame 열에 맞추는 것입니다. 이는 행 방향으로 브로드캐스팅됩니다. 예를 들어:

```python
df - df.iloc[0]
```

매칭 및 브로드캐스팅 동작을 명시적으로 제어하려면 유연한 이진 연산 섹션을 참조하세요.

스칼라와의 산술 연산은 요소별로 수행됩니다:

```python
df * 5 + 2

1 / df

df ** 4
```

불리언 연산자도 요소별로 작동합니다:

```python
df1 = pd.DataFrame({"a": [1, 0, 1], "b": [0, 1, 1]}, dtype=bool)

df2 = pd.DataFrame({"a": [0, 1, 1], "b": [1, 1, 0]}, dtype=bool)

df1 & df2

df1 | df2

df1 ^ df2

-df1
```

### 전치 (Transposing)

전치를 위해 T 속성이나 DataFrame.transpose()를 사용할 수 있습니다. ndarray와 유사합니다:

```python
# 처음 5행만 보여줍니다
df[:5].T
```

### DataFrame과 NumPy 함수의 상호 운용성 (DataFrame interoperability with NumPy functions)

대부분의 NumPy 함수는 Series와 DataFrame에서 직접 호출할 수 있습니다.

```python
np.exp(df)

np.asarray(df)
```

DataFrame은 n차원 배열을 대체하기 위한 것이 아닙니다. 인덱싱 의미와 데이터 모델이 n차원 배열과 여러 면에서 다릅니다.

Series는 array_ufunc을 구현하여 NumPy의 범용 함수와 함께 작동할 수 있습니다.

ufunc은 Series의 기본 배열에 적용됩니다.

```python
ser = pd.Series([1, 2, 3, 4])

np.exp(ser)
```

여러 Series가 ufunc에 전달될 때, 연산을 수행하기 전에 정렬됩니다.

라이브러리의 다른 부분과 마찬가지로, pandas는 여러 입력이 있는 ufunc의 일부로 레이블이 지정된 입력을 자동으로 정렬합니다. 예를 들어, 다르게 정렬된 레이블을 가진 두 Series에 numpy.remainder()를 사용하면 연산 전에 정렬됩니다.

```python
ser1 = pd.Series([1, 2, 3], index=["a", "b", "c"])

ser2 = pd.Series([1, 3, 5], index=["b", "a", "c"])

ser1

ser2

np.remainder(ser1, ser2)
```

일반적으로, 두 인덱스의 합집합이 취해지고, 겹치지 않는 값은 누락된 값으로 채워집니다.

```python
ser3 = pd.Series([2, 4, 6], index=["b", "c", "d"])

ser3

np.remainder(ser1, ser3)
```

이진 ufunc이 Series와 Index에 적용될 때, Series 구현이 우선되며 Series가 반환됩니다.

```python
ser = pd.Series([1, 2, 3])

idx = pd.Index([4, 5, 6])

np.maximum(ser, idx)
```

NumPy ufunc은 ndarray가 아닌 배열로 지원되는 Series에도 안전하게 적용할 수 있습니다. 예를 들어 arrays.SparseArray (희소 계산 참조). 가능한 경우 ufunc은 기본 데이터를 ndarray로 변환하지 않고 적용됩니다.

### 콘솔 표시 (Console display)

콘솔에 표시하기 위해 매우 큰 [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame “pandas.DataFrame”)이 잘립니다. 또한 [`info()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html#pandas.DataFrame.info “pandas.DataFrame.info”)를 사용하여 요약을 얻을 수도 있습니다. (**baseball** 데이터 세트는 **plyr** R 패키지에서 가져온 것입니다):

```python
In [123]: baseball = pd.read_csv("data/baseball.csv")

In [124]: print(baseball)
       id     player  year  stint team  lg  …    so  ibb  hbp   sh   sf  gidp
0   88641  womacto01  2006      2  CHN  NL  …   4.0  0.0  0.0  3.0  0.0   0.0
1   88643  schilcu01  2006      1  BOS  AL  …   1.0  0.0  0.0  0.0  0.0   0.0
..    …        …   …    …  …  ..  …   …  …  …  …  …   …
98  89533   aloumo01  2007      1  NYN  NL  …  30.0  5.0  2.0  0.0  3.0  13.0
99  89534  alomasa02  2007      1  NYN  NL  …   3.0  0.0  0.0  0.0  0.0   0.0

[100 rows x 23 columns]

In [125]: baseball.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 23 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   id      100 non-null    int64  
 1   player  100 non-null    object 
 2   year    100 non-null    int64  
 3   stint   100 non-null    int64  
 4   team    100 non-null    object 
 5   lg      100 non-null    object 
 6   g       100 non-null    int64  
 7   ab      100 non-null    int64  
 8   r       100 non-null    int64  
 9   h       100 non-null    int64  
 10  X2b     100 non-null    int64  
 11  X3b     100 non-null    int64  
 12  hr      100 non-null    int64  
 13  rbi     100 non-null    float64
 14  sb      100 non-null    float64
 15  cs      100 non-null    float64
 16  bb      100 non-null    int64  
 17  so      100 non-null    float64
 18  ibb     100 non-null    float64
 19  hbp     100 non-null    float64
 20  sh      100 non-null    float64
 21  sf      100 non-null    float64
 22  gidp    100 non-null    float64
dtypes: float64(9), int64(11), object(3)
memory usage: 18.1+ KB
```

그러나 [`DataFrame.to_string()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html#pandas.DataFrame.to_string “pandas.DataFrame.to_string”)을 사용하면 콘솔 너비에 항상 맞지는 않지만 표 형식으로 [`데이터 프레임`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame “pandas.DataFrame”)의 문자열 표현을 반환할 수 있습니다:

```python
In [126]: print(baseball.iloc[-20:, :12].to_string())
       id     player  year  stint team  lg    g   ab   r    h  X2b  X3b
80  89474  finlest01  2007      1  COL  NL   43   94   9   17    3    0
81  89480  embreal01  2007      1  OAK  AL    4    0   0    0    0    0
82  89481  edmonji01  2007      1  SLN  NL  117  365  39   92   15    2
83  89482  easleda01  2007      1  NYN  NL   76  193  24   54    6    0
84  89489  delgaca01  2007      1  NYN  NL  139  538  71  139   30    0
85  89493  cormirh01  2007      1  CIN  NL    6    0   0    0    0    0
86  89494  coninje01  2007      2  NYN  NL   21   41   2    8    2    0
87  89495  coninje01  2007      1  CIN  NL   80  215  23   57   11    1
88  89497  clemero02  2007      1  NYA  AL    2    2   0    1    0    0
89  89498  claytro01  2007      2  BOS  AL    8    6   1    0    0    0
90  89499  claytro01  2007      1  TOR  AL   69  189  23   48   14    0
91  89501  cirilje01  2007      2  ARI  NL   28   40   6    8    4    0
92  89502  cirilje01  2007      1  MIN  AL   50  153  18   40    9    2
93  89521  bondsba01  2007      1  SFN  NL  126  340  75   94   14    0
94  89523  biggicr01  2007      1  HOU  NL  141  517  68  130   31    3
95  89525  benitar01  2007      2  FLO  NL   34    0   0    0    0    0
96  89526  benitar01  2007      1  SFN  NL   19    0   0    0    0    0
97  89530  ausmubr01  2007      1  HOU  NL  117  349  38   82   16    3
98  89533   aloumo01  2007      1  NYN  NL   87  328  51  112   19    1
99  89534  alomasa02  2007      1  NYN  NL    8   22   1    3    1    0
```

```python
Wide DataFrames will be printed across multiple rows by default:

In [127]: pd.DataFrame(np.random.randn(3, 12))
Out[127]: 
         0         1         2   …        9         10        11
0 -1.226825  0.769804 -1.281247  … -1.110336 -0.619976  0.149748
1 -0.732339  0.687738  0.176444  …  1.462696 -1.743161 -0.826591
2 -0.345352  1.314232  0.690579  …  0.896171 -0.487602 -0.082240

[3 rows x 12 columns]
```

`'display.width` 옵션을 설정하여 한 행에 인쇄할 양을 변경할 수 있습니다:

```python
In [128]: pd.set_option("display.width", 40)  # default is 80

In [129]: pd.DataFrame(np.random.randn(3, 12))
Out[129]: 
         0         1         2   …        9         10        11
0 -2.182937  0.380396  0.084844  … -0.023688  2.410179  1.450520
1  0.206053 -0.251905 -2.213588  … -0.025747 -0.988387  0.094055
2  1.262731  1.289997  0.082423  … -0.281461  0.030711  0.109121

[3 rows x 12 columns]
```

`display.max_colwidth`를 설정하여 개별 열의 최대 너비를 조정할 수 있습니다.
```python
In [130]: datafile = {
   …..:    "filename": ["filename_01", "filename_02"],
   …..:    "path": [
   …..:        "media/user_name/storage/folder_01/filename_01",
   …..:        "media/user_name/storage/folder_02/filename_02",
   …..:    ],
   …..: }
   …..: 

In [131]: pd.set_option("display.max_colwidth", 30)

In [132]: pd.DataFrame(datafile)
Out[132]: 
      filename                           path
0  filename_01  media/user_name/storage/fo…
1  filename_02  media/user_name/storage/fo…

In [133]: pd.set_option("display.max_colwidth", 100)

In [134]: pd.DataFrame(datafile)
Out[134]: 
      filename                                           path
0  filename_01  media/user_name/storage/folder_01/filename_01
1  filename_02  media/user_name/storage/folder_02/filename_02
```

`expand_frame_repr` 옵션을 통해 이 기능을 비활성화할 수도 있습니다. 그러면 테이블이 한 블록으로 인쇄됩니다.

### 데이터 프레임 열 속성 액세스 및 IPython 완성 (DataFrame column attribute access and IPython completion)

[`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame “pandas.DataFrame”) 열 레이블이 유효한 Python 변수 이름인 경우, 열은 속성처럼 액세스할 수 있습니다:

```python
In [135]: df = pd.DataFrame({"foo1": np.random.randn(5), "foo2": np.random.randn(5)})

In [136]: df
Out[136]: 
       foo1      foo2
0  1.126203  0.781836
1 -0.977349 -1.071357
2  1.474071  0.441153
3 -0.064034  2.353925
4 -1.282782  0.583787

In [137]: df.foo1
Out[137]: 
0    1.126203
1   -0.977349
2    1.474071
3   -0.064034
4   -1.282782
Name: foo1, dtype: float64
```

열은 [IPython](https://ipython.org/) 완성 메커니즘에 연결되어 탭으로 완성할 수도 있습니다:

```
In [5]: df.foo<TAB>  # noqa: E225, E999
df.foo1  df.foo2
```


---
## 참조

---
title: "[Pandas] 데이터 다루기 (Data Handling)"
excerpt: 에 대한 문서
categories:
  - Pandas
tags:
  - Pandas
last_modified_at: 2024-03-01T00:00:00-00:00
link: https://pandas.pydata.org/docs/user_guide/basics.html
상위 항목: "[[pandas_home|판다스 (Pandas)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`


---
여기서는 pandas 데이터 구조에 공통적으로 필요한 많은 필수 기능에 대해 논의합니다. 몇 가지 예제 객체를 만들어 보겠습니다:

```python
In [1]: index = pd.date_range("1/1/2000", periods=8)
In [2]: s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
In [3]: df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=["A", "B", "C"])
```

## 헤드와 테일 (Head and tail)

Series나 DataFrame 객체의 작은 샘플을 보려면 head()와 tail() 메서드를 사용하세요. 기본적으로 표시되는 요소의 수는 5개이지만, 원하는 수를 지정할 수 있습니다.

```python
In [4]: long_series = pd.Series(np.random.randn(1000))
In [5]: long_series.head()
Out[5]: 
0   -1.157892
1   -1.344312
2    0.844885
3    1.075770
4   -0.109050
dtype: float64
In [6]: long_series.tail(3)
Out[6]: 
997   -0.289388
998   -1.020544
999    0.589993
dtype: float64
```

## 속성과 기본 데이터 (Attributes and underlying data)

pandas 객체에는 메타데이터에 접근할 수 있는 여러 속성이 있습니다.

- **shape**: 객체의 축 차원을 제공하며, ndarray와 일관됩니다
    
- 축 레이블
    
    - **Series**: index (유일한 축)
        
    - **DataFrame**: index (행)과 columns
        

참고로, **이러한 속성들은 안전하게 할당할 수 있습니다**!

```python
In [7]: df[:2]
Out[7]: 
                   A         B         C
2000-01-01 -0.173215  0.119209 -1.044236
2000-01-02 -0.861849 -2.104569 -0.494929

In [8]: df.columns = [x.lower() for x in df.columns]

In [9]: df
Out[9]: 
                   a         b         c
2000-01-01 -0.173215  0.119209 -1.044236
2000-01-02 -0.861849 -2.104569 -0.494929
2000-01-03  1.071804  0.721555 -0.706771
2000-01-04 -1.039575  0.271860 -0.424972
2000-01-05  0.567020  0.276232 -1.087401
2000-01-06 -0.673690  0.113648 -1.478427
2000-01-07  0.524988  0.404705  0.577046
2000-01-08 -1.715002 -1.039268 -0.370647
```

pandas 객체([Index](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index), [Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series), [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame))는 실제 데이터를 보유하고 실제 계산을 수행하는 배열의 컨테이너로 생각할 수 있습니다. 많은 유형에서 기본 배열은 [numpy.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)입니다. 그러나 pandas와 제3자 라이브러리는 사용자 정의 배열을 지원하기 위해 NumPy의 타입 시스템을 확장할 수 있습니다([dtypes](https://pandas.pydata.org/docs/user_guide/basics.html#basics-dtypes) 참조).

[Index](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index) 또는 [Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series) 내부의 실제 데이터를 얻으려면 .array 속성을 사용하세요.

```python
In [10]: s.array
Out[10]: 
<NumpyExtensionArray>
[ 0.4691122999071863, -0.2828633443286633, -1.5090585031735124,
 -1.1356323710171934,  1.2121120250208506]
Length: 5, dtype: float64

In [11]: s.index.array
Out[11]: 
<NumpyExtensionArray>
['a', 'b', 'c', 'd', 'e']
Length: 5, dtype: object
```

array는 항상 [ExtensionArray](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray)가 될 것입니다. [ExtensionArray](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray)가 무엇이고 왜 pandas가 이를 사용하는지에 대한 정확한 세부 사항은 이 소개의 범위를 벗어납니다. 자세한 내용은 [dtypes](https://pandas.pydata.org/docs/user_guide/basics.html#basics-dtypes)를 참조하세요.

NumPy 배열이 필요하다는 것을 알고 있다면 [to_numpy()](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy) 또는 numpy.asarray()를 사용하세요.

```python
In [12]: s.to_numpy()
Out[12]: array([ 0.4691, -0.2829, -1.5091, -1.1356,  1.2121])

In [13]: np.asarray(s)
Out[13]: array([ 0.4691, -0.2829, -1.5091, -1.1356,  1.2121])
```

Series나 Index가 [ExtensionArray](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray)로 뒷받침될 때, [to_numpy()](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy)는 데이터 복사와 값 강제 변환을 포함할 수 있습니다. 자세한 내용은 [dtypes](https://pandas.pydata.org/docs/user_guide/basics.html#basics-dtypes)를 참조하세요.

[to_numpy()](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy)는 결과 [numpy.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)의 dtype에 대한 일부 제어를 제공합니다. 예를 들어, 시간대가 있는 날짜/시간을 고려해보세요. NumPy는 시간대를 인식하는 날짜/시간을 표현하기 위한 dtype이 없으므로 두 가지 유용한 표현이 가능합니다:

1. 각각 올바른 tz를 가진 [Timestamp](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp) 객체를 포함하는 object-dtype [numpy.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
    
2. 값이 UTC로 변환되고 시간대가 제거된 datetime64[ns]-dtype [numpy.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
    

시간대는 dtype=object로 보존될 수 있습니다

```python
In [14]: ser = pd.Series(pd.date_range("2000", periods=2, tz="CET"))

In [15]: ser.to_numpy(dtype=object)
Out[15]: 
array([Timestamp('2000-01-01 00:00:00+0100', tz='CET'),
       Timestamp('2000-01-02 00:00:00+0100', tz='CET')], dtype=object)
```

또는 dtype='datetime64[ns]'로 제거될 수 있습니다

```python
In [16]: ser.to_numpy(dtype="datetime64[ns]")
Out[16]: 
array(['1999-12-31T23:00:00.000000000', '2000-01-01T23:00:00.000000000'],
      dtype='datetime64[ns]')
```

[DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame) 내부의 "원시 데이터"를 얻는 것은 약간 더 복잡할 수 있습니다. DataFrame의 모든 열에 대해 단일 데이터 유형만 있는 경우, [DataFrame.to_numpy()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy)는 기본 데이터를 반환합니다:

```python
In [17]: df.to_numpy()
Out[17]: 
array([[-0.1732,  0.1192, -1.0442],
       [-0.8618, -2.1046, -0.4949],
       [ 1.0718,  0.7216, -0.7068],
       [-1.0396,  0.2719, -0.425 ],
       [ 0.567 ,  0.2762, -1.0874],
       [-0.6737,  0.1136, -1.4784],
       [ 0.525 ,  0.4047,  0.577 ],
       [-1.715 , -1.0393, -0.3706]])
```

DataFrame에 동일한 유형의 데이터가 포함되어 있는 경우, ndarray를 실제로 제자리에서 수정할 수 있으며 변경 사항이 데이터 구조에 반영됩니다. 이질적인 데이터의 경우(예: DataFrame의 일부 열이 모두 동일한 dtype이 아님) 이는 해당되지 않습니다. 축 레이블과 달리 values 속성 자체는 할당할 수 없습니다.

> 이질적인 데이터로 작업할 때, 결과 ndarray의 dtype은 관련된 모든 데이터를 수용하도록 선택됩니다. 예를 들어, 문자열이 포함된 경우 결과는 object dtype이 됩니다. 부동 소수점과 정수만 있는 경우 결과 배열은 float dtype이 됩니다.

과거에는 pandas가 Series나 DataFrame에서 데이터를 추출하기 위해 [Series.values](https://pandas.pydata.org/docs/reference/api/pandas.Series.values.html#pandas.Series.values) 또는 [DataFrame.values](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.values.html#pandas.DataFrame.values)를 권장했습니다. 이전 코드 베이스와 온라인에서 여전히 이에 대한 참조를 찾을 수 있습니다. 앞으로는 ==`.values`를 피하고 `.array` 또는 `.to_numpy()`를 사용==하는 것이 좋습니다. .values에는 다음과 같은 단점이 있습니다:
1. Series에 확장 타입이 포함되어 있을 때, [Series.values](https://pandas.pydata.org/docs/reference/api/pandas.Series.values.html#pandas.Series.values)가 NumPy 배열을 반환하는지 확장 배열을 반환하는지 불분명합니다. [Series.array](https://pandas.pydata.org/docs/reference/api/pandas.Series.array.html#pandas.Series.array)는 항상 [ExtensionArray](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray)를 반환하며 데이터를 복사하지 않습니다. [Series.to_numpy()](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy)는 항상 NumPy 배열을 반환하며, 잠재적으로 값을 복사/강제 변환하는 비용이 들 수 있습니다.
2. DataFrame에 다양한 데이터 유형이 혼합되어 있을 때, [DataFrame.values](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.values.html#pandas.DataFrame.values)는 데이터 복사와 공통 dtype으로의 값 강제 변환을 포함할 수 있으며, 이는 비교적 비용이 많이 드는 작업입니다. [DataFrame.to_numpy()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy)는 메서드이므로 반환된 NumPy 배열이 DataFrame의 동일한 데이터에 대한 뷰가 아닐 수 있다는 점을 더 명확히 합니다.

## 가속화된 연산 (Accelerated operations)

pandas는 `numexpr` 라이브러리와 `bottleneck` 라이브러리를 사용하여 특정 유형의 이진 숫자 및 부울 연산을 가속화하는 기능을 지원합니다.

이 라이브러리들은 특히 대규모 데이터 세트를 다룰 때 유용하며 큰 속도 향상을 제공합니다. `numexpr`은 스마트 청킹, 캐싱 및 다중 코어를 사용합니다. `bottleneck`은 특히 `nan`이 있는 배열을 다룰 때 매우 빠른 특수화된 cython 루틴 집합입니다.

다음은 샘플입니다 (100 열 x 100,000 행 `DataFrame` 사용):

|연산|0.11.0 (ms)|이전 버전 (ms)|이전 버전 대비 비율|
|---|---|---|---|
|`df1 > df2`|13.32|125.35|0.1063|
|`df1 * df2`|21.71|36.63|0.5928|
|`df1 + df2`|22.04|36.50|0.6039|

두 라이브러리를 모두 설치하는 것이 좋습니다. 설치에 대한 자세한 정보는 [권장 종속성](https://pandas.pydata.org/docs/getting_started/install.html#install-recommended-dependencies) 섹션을 참조하세요.

이들은 기본적으로 사용되도록 설정되어 있으며, 다음 옵션을 설정하여 이를 제어할 수 있습니다:

```python
pd.set_option("compute.use_bottleneck", False)
pd.set_option("compute.use_numexpr", False)
```

## 유연한 이진 연산 (Flexible binary operations)

pandas 데이터 구조 간의 이진 연산에서는 두 가지 주요 관심사가 있습니다:

- 고차원(예: DataFrame)과 저차원(예: Series) 객체 간의 브로드캐스팅 동작.
    
- 계산에서의 결측 데이터.
    

이러한 문제를 독립적으로 관리하는 방법을 보여드리겠지만, 동시에 처리할 수도 있습니다.

### 매칭 / 브로드캐스팅 동작 (Matching / broadcasting behavior)

DataFrame은 [`add()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add.html#pandas.DataFrame.add "pandas.DataFrame.add"), [`sub()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sub.html#pandas.DataFrame.sub "pandas.DataFrame.sub"), [`mul()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mul.html#pandas.DataFrame.mul "pandas.DataFrame.mul"), [`div()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.div.html#pandas.DataFrame.div "pandas.DataFrame.div") 메서드와 관련 함수 [`radd()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.radd.html#pandas.DataFrame.radd "pandas.DataFrame.radd"), [`rsub()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rsub.html#pandas.DataFrame.rsub "pandas.DataFrame.rsub"), … 를 가지고 있어 이진 연산을 수행할 수 있습니다. 브로드캐스팅 동작의 경우, Series 입력이 주요 관심사입니다. 이러한 함수를 사용하면 **axis** 키워드를 통해 인덱스나 열에 매칭할 수 있습니다:

```python
In [18]: df = pd.DataFrame(
   ….:    {
   ….:        "one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
   ….:        "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
   ….:        "three": pd.Series(np.random.randn(3), index=["b", "c", "d"]),
   ….:    }
   ….: )
   ….: 

In [19]: df
Out[19]: 
        one       two     three
a  1.394981  1.772517       NaN
b  0.343054  1.912123 -0.050390
c  0.695246  1.478369  1.227435
d       NaN  0.279344 -0.613172

In [20]: row = df.iloc[1]

In [21]: column = df["two"]

In [22]: df.sub(row, axis="columns")
Out[22]: 
        one       two     three
a  1.051928 -0.139606       NaN
b  0.000000  0.000000  0.000000
c  0.352192 -0.433754  1.277825
d       NaN -1.632779 -0.562782

In [23]: df.sub(row, axis=1)
Out[23]: 
        one       two     three
a  1.051928 -0.139606       NaN
b  0.000000  0.000000  0.000000
c  0.352192 -0.433754  1.277825
d       NaN -1.632779 -0.562782

In [24]: df.sub(column, axis="index")
Out[24]: 
        one  two     three
a -0.377535  0.0       NaN
b -1.569069  0.0 -1.962513
c -0.783123  0.0 -0.250933
d       NaN  0.0 -0.892516

In [25]: df.sub(column, axis=0)
Out[25]: 
        one  two     three
a -0.377535  0.0       NaN
b -1.569069  0.0 -1.962513
c -0.783123  0.0 -0.250933
d       NaN  0.0 -0.892516
```

또한 MultiIndexed DataFrame의 레벨을 Series와 정렬할 수 있습니다.

```python
In [26]: dfmi = df.copy()

In [27]: dfmi.index = pd.MultiIndex.from_tuples(
   ….:    [(1, "a"), (1, "b"), (1, "c"), (2, "a")], names=["first", "second"]
   ….: )
   ….: 

In [28]: dfmi.sub(column, axis=0, level="second")
Out[28]: 
                   one       two     three
first second                              
1     a      -0.377535  0.000000       NaN
      b      -1.569069  0.000000 -1.962513
      c      -0.783123  0.000000 -0.250933
2     a            NaN -1.493173 -2.385688
```

Series와 Index는 또한 [`divmod()`](https://docs.python.org/3/library/functions.html#divmod "(in Python v3.12)") 내장 함수를 지원합니다. 이 함수는 floor division과 modulo 연산을 동시에 수행하여 왼쪽 피연산자와 동일한 유형의 두 개의 튜플을 반환합니다. 예를 들어:

```python
In [29]: s = pd.Series(np.arange(10))

In [30]: s
Out[30]: 
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8
9    9
dtype: int64

In [31]: div, rem = divmod(s, 3)

In [32]: div
Out[32]: 
0    0
1    0
2    0
3    1
4    1
5    1
6    2
7    2
8    2
9    3
dtype: int64

In [33]: rem
Out[33]: 
0    0
1    1
2    2
3    0
4    1
5    2
6    0
7    1
8    2
9    0
dtype: int64

In [34]: idx = pd.Index(np.arange(10))

In [35]: idx
Out[35]: Index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype='int64')

In [36]: div, rem = divmod(idx, 3)

In [37]: div
Out[37]: Index([0, 0, 0, 1, 1, 1, 2, 2, 2, 3], dtype='int64')

In [38]: rem
Out[38]: Index([0, 1, 2, 0, 1, 2, 0, 1, 2, 0], dtype='int64')
```

요소별 [`divmod()`](https://docs.python.org/3/library/functions.html#divmod "(in Python v3.12)")도 수행할 수 있습니다:

```python
In [39]: div, rem = divmod(s, [2, 2, 3, 3, 4, 4, 5, 5, 6, 6])

In [40]: div
Out[40]: 
0    0
1    0
2    0
3    1
4    1
5    1
6    1
7    1
8    1
9    1
dtype: int64

In [41]: rem
Out[41]: 
0    0
1    1
2    2
3    0
4    0
5    1
6    1
7    2
8    2
9    3
dtype: int64
```

### 결측 데이터 / 채우기 값을 사용한 연산 (Missing data / operations with fill values)

Series와 DataFrame에서 산술 함수는 fill_value를 입력하는 옵션이 있습니다. 이는 특정 위치에서 값 중 하나만 누락된 경우 대체할 값을 의미합니다. 예를 들어, 두 DataFrame 객체를 더할 때 NaN을 0으로 처리하고 싶을 수 있습니다. 단, 두 DataFrame 모두에서 해당 값이 누락된 경우에는 결과가 NaN이 됩니다 (나중에 fillna를 사용하여 NaN을 다른 값으로 대체할 수 있습니다).

```python
In [42]: df2 = df.copy()

In [43]: df2.loc["a", "three"] = 1.0

In [44]: df
Out[44]: 
        one       two     three
a  1.394981  1.772517       NaN
b  0.343054  1.912123 -0.050390
c  0.695246  1.478369  1.227435
d       NaN  0.279344 -0.613172

In [45]: df2
Out[45]: 
        one       two     three
a  1.394981  1.772517  1.000000
b  0.343054  1.912123 -0.050390
c  0.695246  1.478369  1.227435
d       NaN  0.279344 -0.613172

In [46]: df + df2
Out[46]: 
        one       two     three
a  2.789963  3.545034       NaN
b  0.686107  3.824246 -0.100780
c  1.390491  2.956737  2.454870
d       NaN  0.558688 -1.226343

In [47]: df.add(df2, fill_value=0)
Out[47]: 
        one       two     three
a  2.789963  3.545034  1.000000
b  0.686107  3.824246 -0.100780
c  1.390491  2.956737  2.454870
d       NaN  0.558688 -1.226343
```

### 유연한 비교 (Flexible comparisons)

Series와 DataFrame은 위에서 설명한 이진 산술 연산과 유사한 동작을 하는 이진 비교 메서드 `eq`, `ne`, `lt`, `gt`, `le`, `ge`를 가지고 있습니다:

```python
In [48]: df.gt(df2)
Out[48]: 
     one    two  three
a  False  False  False
b  False  False  False
c  False  False  False
d  False  False  False

In [49]: df2.ne(df)
Out[49]: 
     one    two  three
a  False  False   True
b  False  False  False
c  False  False  False
d   True  False  False
```

이러한 연산은 입력된 왼쪽 피연산자와 동일한 유형의 pandas 객체를 생성하며, 이는 dtype이 bool인 객체입니다. 이러한 부울 객체는 인덱싱 연산에 사용될 수 있습니다. [부울 인덱싱](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-boolean) 섹션을 참조하세요.

### 불리언 축소 (Boolean reductions)

불리언 축소를 적용할 수 있습니다: empty, any(), all(), bool()은 불리언 결과를 요약하는 방법을 제공합니다.

```python
In [50]: (df > 0).all()
Out[50]: 
one      False
two       True
three    False
dtype: bool

In [51]: (df > 0).any()
Out[51]: 
one      True
two      True
three    True
dtype: bool
```

최종 불리언 값으로 축소할 수 있습니다.

```python
In [52]: (df > 0).any().any()
Out[52]: True
```

empty 속성을 통해 판다스 객체가 비어 있는지 테스트할 수 있습니다.

```python
In [53]: df.empty
Out[53]: False

In [54]: pd.DataFrame(columns=list("ABC")).empty
Out[54]: True
```

경고

판다스 객체의 참/거짓을 주장하면 오류가 발생합니다. 이는 비어 있음이나 값의 테스트가 모호하기 때문입니다.

```python
In [55]: if df:
   ….:    print(True)
   ….: 
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-55-318d08b2571a> in ?()
----> 1 if df:
      2     print(True)

~/work/pandas/pandas/pandas/core/generic.py in ?(self)
   1575     @final
   1576     def __nonzero__(self) -> NoReturn:
-> 1577         raise ValueError(
   1578             f"The truth value of a {type(self).__name__} is ambiguous. "
   1579             "Use a.empty, a.bool(), a.item(), a.any() or a.all()."
   1580         )

ValueError: The truth value of a DataFrame is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().

In [56]: df and df2
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-56-b241b64bb471> in ?()
----> 1 df and df2

~/work/pandas/pandas/pandas/core/generic.py in ?(self)
   1575     @final
   1576     def __nonzero__(self) -> NoReturn:
-> 1577         raise ValueError(
   1578             f"The truth value of a {type(self).__name__} is ambiguous. "
   1579             "Use a.empty, a.bool(), a.item(), a.any() or a.all()."
   1580         )

ValueError: The truth value of a DataFrame is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
```

더 자세한 논의는 [gotchas](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-truth)를 참조하세요.

### 객체가 동등한지 비교하기 (Comparing if objects are equivalent)

종종 같은 결과를 계산하는 방법이 하나 이상 있다는 것을 알게 될 것입니다. 간단한 예로, df + df와 df * 2를 생각해 보세요. 이 두 계산이 같은 결과를 생성하는지 테스트하기 위해, 위에서 보여준 도구를 사용하여 (df + df == df * 2).all()을 상상할 수 있습니다. 하지만 실제로 이 표현식은 False입니다:

```python
In [57]: df + df == df * 2
Out[57]: 
     one   two  three
a   True  True  False
b   True  True   True
c   True  True   True
d  False  True   True

In [58]: (df + df == df * 2).all()
Out[58]: 
one      False
two       True
three    False
dtype: bool
```

불리언 DataFrame df + df == df * 2에 일부 False 값이 포함되어 있다는 점에 주목하세요! 이는 NaN이 동등하게 비교되지 않기 때문입니다:

```python
In [59]: np.nan == np.nan
Out[59]: False
```

따라서 NDFrames(Series와 DataFrame과 같은)는 대응하는 위치에 있는 NaN을 동등하게 취급하여 동등성을 테스트하는 equals() 메서드를 가지고 있습니다.

```python
In [60]: (df + df).equals(df * 2)
Out[60]: True
```

동등성이 True가 되려면 Series나 DataFrame 인덱스가 같은 순서여야 합니다:

```python
In [61]: df1 = pd.DataFrame({"col": ["foo", 0, np.nan]})

In [62]: df2 = pd.DataFrame({"col": [np.nan, 0, "foo"]}, index=[2, 1, 0])

In [63]: df1.equals(df2)
Out[63]: False

In [64]: df1.equals(df2.sort_index())
Out[64]: True
```

### 배열 유사 객체 비교하기 (Comparing array-like objects)

판다스 데이터 구조를 스칼라 값과 비교할 때 편리하게 요소별 비교를 수행할 수 있습니다:

```python
In [65]: pd.Series(["foo", "bar", "baz"]) == "foo"
Out[65]: 
0     True
1    False
2    False
dtype: bool

In [66]: pd.Index(["foo", "bar", "baz"]) == "foo"
Out[66]: array([ True, False, False])
```

판다스는 또한 같은 길이의 서로 다른 배열 유사 객체 간의 요소별 비교도 처리합니다:

```python
In [67]: pd.Series(["foo", "bar", "baz"]) == pd.Index(["foo", "bar", "qux"])
Out[67]: 
0     True
1     True
2    False
dtype: bool

In [68]: pd.Series(["foo", "bar", "baz"]) == np.array(["foo", "bar", "qux"])
Out[68]: 
0     True
1     True
2    False
dtype: bool
```

길이가 다른 Index나 Series 객체를 비교하려고 하면 ValueError가 발생합니다:

```python
In [69]: pd.Series(['foo', 'bar', 'baz']) == pd.Series(['foo', 'bar'])
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[69], line 1
----> 1 pd.Series(['foo', 'bar', 'baz']) == pd.Series(['foo', 'bar'])

File ~/work/pandas/pandas/pandas/core/ops/common.py:76, in _unpack_zerodim_and_defer.<locals>.new_method(self, other)
     72             return NotImplemented
     74 other = item_from_zerodim(other)
---> 76 return method(self, other)

File ~/work/pandas/pandas/pandas/core/arraylike.py:40, in OpsMixin.__eq__(self, other)
     38 @unpack_zerodim_and_defer("__eq__")
     39 def __eq__(self, other):
---> 40     return self._cmp_method(other, operator.eq)

File ~/work/pandas/pandas/pandas/core/series.py:6114, in Series._cmp_method(self, other, op)
   6111 res_name = ops.get_op_result_name(self, other)
   6113 if isinstance(other, Series) and not self._indexed_same(other):
-> 6114     raise ValueError("Can only compare identically-labeled Series objects")
   6116 lvalues = self._values
   6117 rvalues = extract_array(other, extract_numpy=True, extract_range=True)

ValueError: Can only compare identically-labeled Series objects

In [70]: pd.Series(['foo', 'bar', 'baz']) == pd.Series(['foo'])
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[70], line 1
----> 1 pd.Series(['foo', 'bar', 'baz']) == pd.Series(['foo'])

File ~/work/pandas/pandas/pandas/core/ops/common.py:76, in _unpack_zerodim_and_defer.<locals>.new_method(self, other)
     72             return NotImplemented
     74 other = item_from_zerodim(other)
---> 76 return method(self, other)

File ~/work/pandas/pandas/pandas/core/arraylike.py:40, in OpsMixin.__eq__(self, other)
     38 @unpack_zerodim_and_defer("__eq__")
     39 def __eq__(self, other):
---> 40     return self._cmp_method(other, operator.eq)

File ~/work/pandas/pandas/pandas/core/series.py:6114, in Series._cmp_method(self, other, op)
   6111 res_name = ops.get_op_result_name(self, other)
   6113 if isinstance(other, Series) and not self._indexed_same(other):
-> 6114     raise ValueError("Can only compare identically-labeled Series objects")
   6116 lvalues = self._values
   6117 rvalues = extract_array(other, extract_numpy=True, extract_range=True)

ValueError: Can only compare identically-labeled Series objects
```

### 중복되는 데이터 세트 결합 (Combining overlapping data sets)

때때로 한 세트의 값이 다른 세트보다 선호되는 두 개의 유사한 데이터 세트를 결합해야 하는 문제가 발생합니다. 예를 들어, 하나가 "더 높은 품질"로 간주되는 특정 경제 지표를 나타내는 두 개의 데이터 시리즈가 있을 수 있습니다. 그러나 낮은 품질의 시리즈가 더 오랜 기간의 역사를 가지고 있거나 더 완전한 데이터 범위를 가질 수 있습니다. 따라서 한 DataFrame의 누락된 값이 다른 DataFrame의 유사한 레이블이 지정된 값으로 조건부로 채워지는 두 DataFrame 객체를 결합하고자 합니다. 이 작업을 구현하는 함수는 combine_first()이며, 다음과 같이 설명합니다:

```python
In [71]: df1 = pd.DataFrame(
   …:    {"A": [1.0, np.nan, 3.0, 5.0, np.nan], "B": [np.nan, 2.0, 3.0, np.nan, 6.0]}
   …: )
   …: 

In [72]: df2 = pd.DataFrame(
   …:    {
   …:        "A": [5.0, 2.0, 4.0, np.nan, 3.0, 7.0],
   …:        "B": [np.nan, np.nan, 3.0, 4.0, 6.0, 8.0],
   …:    }
   …: )
   …: 

In [73]: df1
Out[73]: 
     A    B
0  1.0  NaN
1  NaN  2.0
2  3.0  3.0
3  5.0  NaN
4  NaN  6.0

In [74]: df2
Out[74]: 
     A    B
0  5.0  NaN
1  2.0  NaN
2  4.0  3.0
3  NaN  4.0
4  3.0  6.0
5  7.0  8.0

In [75]: df1.combine_first(df2)
Out[75]: 
     A    B
0  1.0  NaN
1  2.0  2.0
2  3.0  3.0
3  5.0  4.0
4  3.0  6.0
5  7.0  8.0
```

### 일반 DataFrame 결합 (General DataFrame combine)

위의 combine_first() 메서드는 더 일반적인 DataFrame.combine()을 호출합니다. 이 메서드는 다른 DataFrame과 결합 함수를 받아 입력 DataFrame을 정렬한 다음 결합 함수를 Series 쌍(즉, 이름이 같은 열)에 전달합니다.

예를 들어, 위의 combine_first()를 재현하려면:

```python
In [76]: def combiner(x, y):
   …:    return np.where(pd.isna(x), y, x)
   …: 

In [77]: df1.combine(df2, combiner)
Out[77]: 
     A    B
0  1.0  NaN
1  2.0  2.0
2  3.0  3.0
3  5.0  4.0
4  3.0  6.0
5  7.0  8.0
```

## 기술 통계 (Descriptive statistics)

Series, DataFrame에 대한 기술 통계와 기타 관련 작업을 계산하는 많은 메서드가 있습니다. 이들 대부분은 sum(), mean(), quantile()과 같은 집계 (따라서 낮은 차원의 결과를 생성)이지만, cumsum()과 cumprod()와 같은 일부는 동일한 크기의 객체를 생성합니다. 일반적으로 이러한 메서드는 ndarray.{sum, std, …}와 마찬가지로 axis 인수를 받지만, 축은 이름이나 정수로 지정할 수 있습니다:

- Series: 축 인수 필요 없음
- DataFrame: "index" (axis=0, 기본값), "columns" (axis=1)

예를 들어:

```python
In [78]: df
Out[78]: 
        one       two     three
a  1.394981  1.772517       NaN
b  0.343054  1.912123 -0.050390
c  0.695246  1.478369  1.227435
d       NaN  0.279344 -0.613172

In [79]: df.mean(0)
Out[79]: 
one      0.811094
two      1.360588
three    0.187958
dtype: float64

In [80]: df.mean(1)
Out[80]: 
a    1.583749
b    0.734929
c    1.133683
d   -0.166914
dtype: float64
```

이러한 모든 메서드에는 누락된 데이터를 제외할지 여부를 나타내는 skipna 옵션이 있습니다(기본값은 True):

```python
In [81]: df.sum(0, skipna=False)
Out[81]: 
one           NaN
two      5.442353
three         NaN
dtype: float64

In [82]: df.sum(axis=1, skipna=True)
Out[82]: 
a    3.167498
b    2.204786
c    3.401050
d   -0.333828
dtype: float64
```

브로드캐스팅/산술 동작과 결합하면 표준화(데이터를 평균 0, 표준편차 1로 만들기)와 같은 다양한 통계 절차를 매우 간결하게 설명할 수 있습니다:

```python
In [83]: ts_stand = (df - df.mean()) / df.std()

In [84]: ts_stand.std()
Out[84]: 
one      1.0
two      1.0
three    1.0
dtype: float64

In [85]: xs_stand = df.sub(df.mean(1), axis=0).div(df.std(1), axis=0)

In [86]: xs_stand.std(1)
Out[86]: 
a    1.0
b    1.0
c    1.0
d    1.0
dtype: float64
```

cumsum()와 cumprod()와 같은 메서드는 NaN 값의 위치를 유지한다는 점에 유의하세요. 이는 expanding()과 rolling()과는 다소 다릅니다. NaN 동작은 min_periods 매개변수에 의해 추가로 지시됩니다.

```python
In [87]: df.cumsum()
Out[87]: 
        one       two     three
a  1.394981  1.772517       NaN
b  1.738035  3.684640 -0.050390
c  2.433281  5.163008  1.177045
d       NaN  5.442353  0.563873
```

다음은 일반적인 함수의 빠른 참조 요약 표입니다. 각 함수는 객체에 계층적 인덱스가 있는 경우에만 적용되는 선택적 level 매개변수도 사용합니다.

| 함수 | 설명 |
|---|---|
| count | NA가 아닌 관측치의 수 |
| sum | 값의 합계 |
| mean | 값의 평균 |
| median | 값의 산술 중앙값 |
| min | 최소값 |
| max | 최대값 |
| mode | 최빈값 |
| abs | 절대값 |
| prod | 값의 곱 |
| std | Bessel 수정된 표본 표준편차 |
| var | 불편 분산 |
| sem | 평균의 표준 오차 |
| skew | 표본 왜도 (3차 모멘트) |
| kurt | 표본 첨도 (4차 모멘트) |
| quantile | 표본 분위수 (%에서의 값) |
| cumsum | 누적 합계 |
| cumprod | 누적 곱 |
| cummax | 누적 최대값 |
| cummin | 누적 최소값 |

우연히도 일부 NumPy 메서드(예: mean, std, sum)는 기본적으로 Series 입력에서 NA를 제외합니다:

```python
In [88]: np.mean(df["one"])
Out[88]: 0.8110935116651192

In [89]: np.mean(df["one"].to_numpy())
Out[89]: nan
```

Series.nunique()는 Series에서 고유한 NA가 아닌 값의 수를 반환합니다:

```python
In [90]: series = pd.Series(np.random.randn(500))

In [91]: series[20:500] = np.nan

In [92]: series[10:20] = 5

In [93]: series.nunique()
Out[93]: 11
```

### 데이터 요약: describe (Summarizing data: describe)

Series나 DataFrame의 열에 대한 다양한 요약 통계를 계산하는 편리한 [`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe) 함수가 있습니다(물론 NA는 제외):

```python
series = pd.Series(np.random.randn(1000))
series[::2] = np.nan
series.describe()
```

```
count    500.000000
mean      -0.021292
std        1.015906
min       -2.683763
25%       -0.699070
50%       -0.069718
75%        0.714483
max        3.160915
dtype: float64
```

```python
frame = pd.DataFrame(np.random.randn(1000, 5), columns=["a", "b", "c", "d", "e"])
frame.iloc[::2] = np.nan
frame.describe()
```

```
                a           b           c           d           e
count  500.000000  500.000000  500.000000  500.000000  500.000000
mean     0.033387    0.030045   -0.043719   -0.051686    0.005979
std      1.017152    0.978743    1.025270    1.015988    1.006695
min     -3.000951   -2.637901   -3.303099   -3.159200   -3.188821
25%     -0.647623   -0.576449   -0.712369   -0.691338   -0.691115
50%      0.047578   -0.021499   -0.023888   -0.032652   -0.025363
75%      0.729907    0.775880    0.618896    0.670047    0.649748
max      2.740139    2.752332    3.004229    2.728702    3.240991
```

출력에 포함할 특정 백분위수를 선택할 수 있습니다:

```python
series.describe(percentiles=[0.05, 0.25, 0.75, 0.95])
```

```
count    500.000000
mean      -0.021292
std        1.015906
min       -2.683763
5%        -1.645423
25%       -0.699070
50%       -0.069718
75%        0.714483
95%        1.711409
max        3.160915
dtype: float64
```

기본적으로 중앙값은 항상 포함됩니다.

숫자가 아닌 Series 객체의 경우, [`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.describe.html#pandas.Series.describe)는 고유 값의 수와 가장 자주 발생하는 값에 대한 간단한 요약을 제공합니다:

```python
s = pd.Series(["a", "a", "b", "b", "a", "a", np.nan, "c", "d", "a"])
s.describe()
```

```
count     9
unique    4
top       a
freq      5
dtype: object
```

혼합 유형의 DataFrame 객체에서 [`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe)는 숫자 열만 포함하도록 요약을 제한하거나, 숫자 열이 없는 경우 범주형 열만 포함합니다:

```python
frame = pd.DataFrame({"a": ["Yes", "Yes", "No", "No"], "b": range(4)})
frame.describe()
```

```
              b
count  4.000000
mean   1.500000
std    1.290994
min    0.000000
25%    0.750000
50%    1.500000
75%    2.250000
max    3.000000
```

이 동작은 include/exclude 인수로 유형 목록을 제공하여 제어할 수 있습니다. all 특수 값도 사용할 수 있습니다:

```python
frame.describe(include=["object"])
frame.describe(include=["number"])
frame.describe(include="all")
```

이 기능은 [select_dtypes](https://pandas.pydata.org/docs/user_guide/basics.html#basics-selectdtypes)에 의존합니다. 허용되는 입력에 대한 자세한 내용은 해당 섹션을 참조하세요.

### 최소/최대 값의 인덱스 (Index of min/max values)

Series와 DataFrame의 [`idxmin()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmin.html#pandas.DataFrame.idxmin)과 [`idxmax()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html#pandas.DataFrame.idxmax) 함수는 최소 및 최대 해당 값을 가진 인덱스 라벨을 계산합니다:

```python
s1 = pd.Series(np.random.randn(5))
s1
s1.idxmin(), s1.idxmax()

df1 = pd.DataFrame(np.random.randn(5, 3), columns=["A", "B", "C"])
df1
df1.idxmin(axis=0)
df1.idxmax(axis=1)
```

최소값 또는 최대값과 일치하는 여러 행(또는 열)이 있을 때, [`idxmin()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmin.html#pandas.DataFrame.idxmin)과 [`idxmax()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html#pandas.DataFrame.idxmax)는 첫 번째 일치하는 인덱스를 반환합니다:

```python
df3 = pd.DataFrame([2, 1, 1, 3, np.nan], columns=["A"], index=list("edcba"))
df3
df3["A"].idxmin()
```

> idxmin과 idxmax는 NumPy에서 argmin과 argmax로 불립니다.

### 값 개수 (히스토그래밍) / 최빈값 (Value counts (histogramming) / mode)

[`value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html#pandas.Series.value_counts) Series 메서드는 1D 값 배열의 히스토그램을 계산합니다. 일반 배열에서도 함수로 사용할 수 있습니다:

```python
data = np.random.randint(0, 7, size=50)
data
s = pd.Series(data)
s.value_counts()
```

[`value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html#pandas.DataFrame.value_counts) 메서드는 여러 열에 걸쳐 조합을 세는 데 사용할 수 있습니다. 기본적으로 모든 열이 사용되지만 subset 인수를 사용하여 하위 집합을 선택할 수 있습니다.

```python
data = {"a": [1, 2, 3, 4], "b": ["x", "x", "y", "y"]}
frame = pd.DataFrame(data)
frame.value_counts()
```

마찬가지로 Series나 DataFrame의 값 중 가장 자주 발생하는 값(들), 즉 최빈값을 얻을 수 있습니다:

```python
s5 = pd.Series([1, 1, 3, 3, 3, 5, 5, 7, 7, 7])
s5.mode()

df5 = pd.DataFrame(
   {
       "A": np.random.randint(0, 7, size=50),
       "B": np.random.randint(-10, 15, size=50),
   }
)
df5.mode()
```

### 이산화 및 분위수화 (Discretization and quantiling)

연속 값은 [`cut()`](https://pandas.pydata.org/docs/reference/api/pandas.cut.html#pandas.cut) (값 기반 구간)과 [`qcut()`](https://pandas.pydata.org/docs/reference/api/pandas.qcut.html#pandas.qcut) (표본 분위수 기반 구간) 함수를 사용하여 이산화할 수 있습니다:

```python
arr = np.random.randn(20)
factor = pd.cut(arr, 4)
factor

factor = pd.cut(arr, [-5, -1, 0, 1, 5])
factor
```

[`qcut()`](https://pandas.pydata.org/docs/reference/api/pandas.qcut.html#pandas.qcut)은 표본 분위수를 계산합니다. 예를 들어, 정규 분포된 데이터를 동일한 크기의 사분위수로 나눌 수 있습니다:

```python
arr = np.random.randn(30)
factor = pd.qcut(arr, [0, 0.25, 0.5, 0.75, 1])
factor
```

구간을 정의하기 위해 무한대 값을 전달할 수도 있습니다:

```python
arr = np.random.randn(20)
factor = pd.cut(arr, [-np.inf, 0, np.inf])
factor
```

## 함수 적용 (Function application)

pandas 객체에 자신의 함수나 다른 라이브러리의 함수를 적용하려면 아래 세 가지 방법을 알아야 합니다. 적절한 방법은 함수가 전체 DataFrame이나 Series에 대해 작동하는지, 행 또는 열 단위로 작동하는지, 요소별로 작동하는지에 따라 다릅니다.

1. 테이블 단위 함수 적용: [pipe()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html#pandas.DataFrame.pipe)
    
2. 행 또는 열 단위 함수 적용: [apply()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply)
    
3. 집계 API: [agg()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html#pandas.DataFrame.agg)와 [transform()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transform.html#pandas.DataFrame.transform)
    
4. 요소별 함수 적용: [map()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html#pandas.DataFrame.map)
    

### 테이블 단위 함수 적용 (Tablewise function application)

DataFrame과 Series를 함수에 전달할 수 있습니다. 그러나 함수를 체인으로 호출해야 하는 경우 [pipe()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html#pandas.DataFrame.pipe) 메서드 사용을 고려하세요.

먼저 설정을 해봅시다:

```python
def extract_city_name(df):
    """
    Chicago, IL -> Chicago for city_name column
    """
    df["city_name"] = df["city_and_code"].str.split(",").str.get(0)
    return df

def add_country_name(df, country_name=None):
    """
    Chicago -> Chicago-US for city_name column
    """
    col = "city_name"
    df["city_and_country"] = df[col] + country_name
    return df

df_p = pd.DataFrame({"city_and_code": ["Chicago, IL"]})
```

extract_city_name과 add_country_name은 DataFrame을 받아 DataFrame을 반환하는 함수입니다.

이제 다음을 비교해보세요:

```python
add_country_name(extract_city_name(df_p), country_name="US")
```

결과:
```
  city_and_code city_name city_and_country
0   Chicago, IL   Chicago        ChicagoUS
```

다음과 같습니다:

```python
df_p.pipe(extract_city_name).pipe(add_country_name, country_name="US")
```

결과:
```
  city_and_code city_name city_and_country
0   Chicago, IL   Chicago        ChicagoUS
```

pandas는 메서드 체이닝이라고 알려진 두 번째 스타일을 권장합니다. pipe를 사용하면 pandas 메서드와 함께 자신의 함수나 다른 라이브러리의 함수를 메서드 체인에서 쉽게 사용할 수 있습니다.

위의 예에서 extract_city_name과 add_country_name 함수는 각각 첫 번째 위치 인수로 DataFrame을 예상했습니다. 만약 적용하려는 함수가 데이터를 두 번째 인수로 받는다면 어떻게 해야 할까요? 이 경우 pipe에 (callable, data_keyword) 튜플을 제공합니다. pipe는 DataFrame을 튜플에 지정된 인수로 라우팅합니다.

예를 들어, statsmodels를 사용하여 회귀를 수행할 수 있습니다. 그들의 API는 공식을 첫 번째로, DataFrame을 두 번째 인수인 data로 예상합니다. 우리는 (sm.ols, 'data') 함수와 키워드 쌍을 pipe에 전달합니다:

```python
import statsmodels.formula.api as sm

bb = pd.read_csv("data/baseball.csv", index_col="id")

(
   bb.query("h > 0")
   .assign(ln_h=lambda df: np.log(df.h))
   .pipe((sm.ols, "data"), "hr ~ ln_h + year + g + C(lg)")
   .fit()
   .summary()
)
```

pipe 메서드는 유닉스 파이프와 최근의 dplyr과 magrittr에서 영감을 받았습니다. 이들은 R에 인기 있는 (%>%) (파이프로 읽음) 연산자를 도입했습니다. 여기서 pipe의 구현은 매우 깔끔하고 Python에 잘 어울립니다. [pipe()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html#pandas.DataFrame.pipe)의 소스 코드를 확인해보시기 바랍니다.


### 행 또는 열 단위 함수 적용 (Row or column-wise function application)

DataFrame의 축을 따라 임의의 함수를 적용할 수 있습니다. 이는 apply() 메서드를 사용하며, 설명 통계 메서드와 마찬가지로 선택적 axis 인수를 받습니다:

```python
In [145]: df.apply(lambda x: np.mean(x))
Out[145]: 
one      0.811094
two      1.360588
three    0.187958
dtype: float64

In [146]: df.apply(lambda x: np.mean(x), axis=1)
Out[146]: 
a    1.583749
b    0.734929
c    1.133683
d   -0.166914
dtype: float64

In [147]: df.apply(lambda x: x.max() - x.min())
Out[147]: 
one      1.051928
two      1.632779
three    1.840607
dtype: float64

In [148]: df.apply(np.cumsum)
Out[148]: 
        one       two     three
a  1.394981  1.772517       NaN
b  1.738035  3.684640 -0.050390
c  2.433281  5.163008  1.177045
d       NaN  5.442353  0.563873

In [149]: df.apply(np.exp)
Out[149]: 
        one       two     three
a  4.034899  5.885648       NaN
b  1.409244  6.767440  0.950858
c  2.004201  4.385785  3.412466
d       NaN  1.322262  0.541630
```

apply() 메서드는 문자열 메서드 이름으로도 작동합니다.

```python
In [150]: df.apply("mean")
Out[150]: 
one      0.811094
two      1.360588
three    0.187958
dtype: float64

In [151]: df.apply("mean", axis=1)
Out[151]: 
a    1.583749
b    0.734929
c    1.133683
d   -0.166914
dtype: float64
```

apply()에 전달된 함수의 반환 타입은 기본 동작에서 DataFrame.apply의 최종 출력 타입에 영향을 줍니다:

- 적용된 함수가 Series를 반환하면 최종 출력은 DataFrame입니다. 열은 적용된 함수가 반환한 Series의 인덱스와 일치합니다.
- 적용된 함수가 다른 타입을 반환하면 최종 출력은 Series입니다.

이 기본 동작은 result_type을 사용하여 재정의할 수 있습니다. result_type은 reduce, broadcast, expand 세 가지 옵션을 받습니다. 이들은 리스트와 유사한 반환 값이 DataFrame으로 확장되는 방식(또는 확장되지 않는 방식)을 결정합니다.

apply()를 약간의 창의성과 결합하면 데이터 세트에 대한 많은 질문에 답할 수 있습니다. 예를 들어, 각 열의 최대값이 발생한 날짜를 추출하고 싶다고 가정해 봅시다:

```python
In [152]: tsdf = pd.DataFrame(
   …..:    np.random.randn(1000, 3),
   …..:    columns=["A", "B", "C"],
   …..:    index=pd.date_range("1/1/2000", periods=1000),
   …..: )
   …..: 

In [153]: tsdf.apply(lambda x: x.idxmax())
Out[153]: 
A   2000-08-06
B   2001-01-18
C   2001-07-18
dtype: datetime64[ns]
```

apply() 메서드에 추가 인수와 키워드 인수를 전달할 수도 있습니다.

```python
In [154]: def subtract_and_divide(x, sub, divide=1):
   …..:    return (x - sub) / divide
   …..: 

In [155]: df_udf = pd.DataFrame(np.ones((2, 2)))

In [156]: df_udf.apply(subtract_and_divide, args=(5,), divide=3)
Out[156]: 
          0         1
0 -1.333333 -1.333333
1 -1.333333 -1.333333
```

또 다른 유용한 기능은 각 열이나 행에서 Series 연산을 수행하기 위해 Series 메서드를 전달할 수 있다는 것입니다:

```python
In [157]: tsdf = pd.DataFrame(
   …..:    np.random.randn(10, 3),
   …..:    columns=["A", "B", "C"],
   …..:    index=pd.date_range("1/1/2000", periods=10),
   …..: )
   …..: 

In [158]: tsdf.iloc[3:7] = np.nan

In [159]: tsdf
Out[159]: 
                   A         B         C
2000-01-01 -0.158131 -0.232466  0.321604
2000-01-02 -1.810340 -3.105758  0.433834
2000-01-03 -1.209847 -1.156793 -0.136794
2000-01-04       NaN       NaN       NaN
2000-01-05       NaN       NaN       NaN
2000-01-06       NaN       NaN       NaN
2000-01-07       NaN       NaN       NaN
2000-01-08 -0.653602  0.178875  1.008298
2000-01-09  1.007996  0.462824  0.254472
2000-01-10  0.307473  0.600337  1.643950

In [160]: tsdf.apply(pd.Series.interpolate)
Out[160]: 
                   A         B         C
2000-01-01 -0.158131 -0.232466  0.321604
2000-01-02 -1.810340 -3.105758  0.433834
2000-01-03 -1.209847 -1.156793 -0.136794
2000-01-04 -1.098598 -0.889659  0.092225
2000-01-05 -0.987349 -0.622526  0.321243
2000-01-06 -0.876100 -0.355392  0.550262
2000-01-07 -0.764851 -0.088259  0.779280
2000-01-08 -0.653602  0.178875  1.008298
2000-01-09  1.007996  0.462824  0.254472
2000-01-10  0.307473  0.600337  1.643950
```

마지막으로, apply()는 기본적으로 False인 raw 인수를 받습니다. 이는 함수를 적용하기 전에 각 행이나 열을 Series로 변환합니다. True로 설정하면, 전달된 함수는 대신 ndarray 객체를 받게 되며, 인덱싱 기능이 필요하지 않은 경우 성능에 긍정적인 영향을 미칩니다.

### 집계 API (Aggregation API)

집계 API를 사용하면 하나의 간결한 방식으로 여러 집계 연산을 표현할 수 있습니다. 이 API는 pandas 객체 전반에 걸쳐 유사하며, groupby API, window API, resample API를 참조하세요. 집계의 진입점은 DataFrame.aggregate()이며, DataFrame.agg()라는 별칭도 있습니다.

위와 유사한 시작 프레임을 사용하겠습니다:

```python
In [161]: tsdf = pd.DataFrame(
   …..:    np.random.randn(10, 3),
   …..:    columns=["A", "B", "C"],
   …..:    index=pd.date_range("1/1/2000", periods=10),
   …..: )
   …..: 

In [162]: tsdf.iloc[3:7] = np.nan

In [163]: tsdf
Out[163]: 
                   A         B         C
2000-01-01  1.257606  1.004194  0.167574
2000-01-02 -0.749892  0.288112 -0.757304
2000-01-03 -0.207550 -0.298599  0.116018
2000-01-04       NaN       NaN       NaN
2000-01-05       NaN       NaN       NaN
2000-01-06       NaN       NaN       NaN
2000-01-07       NaN       NaN       NaN
2000-01-08  0.814347 -0.257623  0.869226
2000-01-09 -0.250663 -1.206601  0.896839
2000-01-10  2.169758 -1.333363  0.283157
```

단일 함수를 사용하는 것은 apply()와 동일합니다. 문자열로 명명된 메서드를 전달할 수도 있습니다. 이들은 집계된 출력의 Series를 반환합니다:

```python
In [164]: tsdf.agg(lambda x: np.sum(x))
Out[164]: 
A    3.033606
B   -1.803879
C    1.575510
dtype: float64

In [165]: tsdf.agg("sum")
Out[165]: 
A    3.033606
B   -1.803879
C    1.575510
dtype: float64

# 단일 함수에 대해 집계하기 때문에 이들은 .sum()과 동일합니다
In [166]: tsdf.sum()
Out[166]: 
A    3.033606
B   -1.803879
C    1.575510
dtype: float64
```

Series에 대한 단일 집계는 스칼라 값을 반환합니다:

```python
In [167]: tsdf["A"].agg("sum")
Out[167]: 3.033606102414146
```

#### 여러 함수로 집계하기 (Aggregating with multiple functions)

리스트로 여러 집계 인수를 전달할 수 있습니다. 전달된 각 함수의 결과는 결과 DataFrame의 행이 됩니다. 이들은 자연스럽게 집계 함수의 이름을 따릅니다.

```python
In [168]: tsdf.agg(["sum"])
Out[168]: 
            A         B        C
sum  3.033606 -1.803879  1.57551

In [169]: tsdf.agg(["sum", "mean"])
Out[169]: 
             A         B         C
sum   3.033606 -1.803879  1.575510
mean  0.505601 -0.300647  0.262585
```

Series에서 여러 함수는 함수 이름으로 인덱싱된 Series를 반환합니다:

```python
In [170]: tsdf["A"].agg(["sum", "mean"])
Out[170]: 
sum     3.033606
mean    0.505601
Name: A, dtype: float64
```

lambda 함수를 전달하면 `<lambda>`라는 이름의 행이 생성됩니다:

```python
In [171]: tsdf["A"].agg(["sum", lambda x: x.mean()])
Out[171]: 
sum         3.033606
<lambda>    0.505601
Name: A, dtype: float64
```

명명된 함수를 전달하면 해당 이름이 행 이름이 됩니다:

```python
In [172]: def mymean(x):
   …..:    return x.mean()
   …..: 

In [173]: tsdf["A"].agg(["sum", mymean])
Out[173]: 
sum       3.033606
mymean    0.505601
Name: A, dtype: float64
```

#### 딕셔너리로 집계하기 (Aggregating with a dict)

DataFrame.agg에 열 이름을 스칼라나 스칼라 리스트에 매핑하는 딕셔너리를 전달하면 어떤 함수를 어떤 열에 적용할지 사용자 정의할 수 있습니다. 결과는 특정 순서를 따르지 않으며, 순서를 보장하려면 OrderedDict를 대신 사용할 수 있습니다.

```python
In [174]: tsdf.agg({"A": "mean", "B": "sum"})
Out[174]: 
A    0.505601
B   -1.803879
dtype: float64
```

리스트와 유사한 객체를 전달하면 DataFrame 출력이 생성됩니다. 모든 집계자의 행렬과 유사한 출력을 얻게 됩니다. 출력은 모든 고유 함수로 구성됩니다. 특정 열에 대해 언급되지 않은 함수는 NaN이 됩니다:

```python
In [175]: tsdf.agg({"A": ["mean", "min"], "B": "sum"})
Out[175]: 
             A         B
mean  0.505601       NaN
min  -0.749892       NaN
sum        NaN -1.803879
```

#### 사용자 정의 설명 (Custom describe)

.agg()를 사용하면 내장된 describe 함수와 유사한 사용자 정의 설명 함수를 쉽게 만들 수 있습니다.

```python
In [176]: from functools import partial

In [177]: q_25 = partial(pd.Series.quantile, q=0.25)

In [178]: q_25.__name__ = "25%"

In [179]: q_75 = partial(pd.Series.quantile, q=0.75)

In [180]: q_75.__name__ = "75%"

In [181]: tsdf.agg(["count", "mean", "std", "min", q_25, "median", q_75, "max"])
Out[181]: 
               A         B         C
count   6.000000  6.000000  6.000000
mean    0.505601 -0.300647  0.262585
std     1.103362  0.887508  0.606860
min    -0.749892 -1.333363 -0.757304
25%    -0.239885 -0.979600  0.128907
median  0.303398 -0.278111  0.225365
75%     1.146791  0.151678  0.722709
max     2.169758  1.004194  0.896839
```

### 변환 API (Transform API)

[`transform()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transform.html#pandas.DataFrame.transform) 메서드는 원본과 동일한 인덱스(동일한 크기)를 가진 객체를 반환합니다. 이 API를 사용하면 한 번에 하나씩이 아닌 여러 작업을 동시에 제공할 수 있습니다. 이 API는 `.agg` API와 매우 유사합니다.

위 섹션에서 사용한 것과 유사한 프레임을 만들어 보겠습니다.

```python
In [182]: tsdf = pd.DataFrame(
   .....:    np.random.randn(10, 3),
   .....:    columns=["A", "B", "C"],
   .....:    index=pd.date_range("1/1/2000", periods=10),
   .....: )
   .....: 

In [183]: tsdf.iloc[3:7] = np.nan

In [184]: tsdf
Out[184]: 
                   A         B         C
2000-01-01 -0.428759 -0.864890 -0.675341
2000-01-02 -0.168731  1.338144 -1.279321
2000-01-03 -1.621034  0.438107  0.903794
2000-01-04       NaN       NaN       NaN
2000-01-05       NaN       NaN       NaN
2000-01-06       NaN       NaN       NaN
2000-01-07       NaN       NaN       NaN
2000-01-08  0.254374 -1.240447 -0.201052
2000-01-09 -0.157795  0.791197 -1.144209
2000-01-10 -0.030876  0.371900  0.061932
```

전체 프레임을 변환합니다. `.transform()`은 NumPy 함수, 문자열 함수 이름 또는 사용자 정의 함수를 입력 함수로 허용합니다.

```python
In [185]: tsdf.transform(np.abs)
Out[185]: 
                   A         B         C
2000-01-01  0.428759  0.864890  0.675341
2000-01-02  0.168731  1.338144  1.279321
2000-01-03  1.621034  0.438107  0.903794
2000-01-04       NaN       NaN       NaN
2000-01-05       NaN       NaN       NaN
2000-01-06       NaN       NaN       NaN
2000-01-07       NaN       NaN       NaN
2000-01-08  0.254374  1.240447  0.201052
2000-01-09  0.157795  0.791197  1.144209
2000-01-10  0.030876  0.371900  0.061932

In [186]: tsdf.transform("abs")
Out[186]: 
                   A         B         C
2000-01-01  0.428759  0.864890  0.675341
2000-01-02  0.168731  1.338144  1.279321
2000-01-03  1.621034  0.438107  0.903794
2000-01-04       NaN       NaN       NaN
2000-01-05       NaN       NaN       NaN
2000-01-06       NaN       NaN       NaN
2000-01-07       NaN       NaN       NaN
2000-01-08  0.254374  1.240447  0.201052
2000-01-09  0.157795  0.791197  1.144209
2000-01-10  0.030876  0.371900  0.061932

In [187]: tsdf.transform(lambda x: x.abs())
Out[187]: 
                   A         B         C
2000-01-01  0.428759  0.864890  0.675341
2000-01-02  0.168731  1.338144  1.279321
2000-01-03  1.621034  0.438107  0.903794
2000-01-04       NaN       NaN       NaN
2000-01-05       NaN       NaN       NaN
2000-01-06       NaN       NaN       NaN
2000-01-07       NaN       NaN       NaN
2000-01-08  0.254374  1.240447  0.201052
2000-01-09  0.157795  0.791197  1.144209
2000-01-10  0.030876  0.371900  0.061932
```

여기서 [`transform()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transform.html#pandas.DataFrame.transform)은 단일 함수를 받았습니다. 이는 [ufunc](https://numpy.org/doc/stable/reference/ufuncs.html) 응용과 동일합니다.

```python
In [188]: np.abs(tsdf)
Out[188]: 
                   A         B         C
2000-01-01  0.428759  0.864890  0.675341
2000-01-02  0.168731  1.338144  1.279321
2000-01-03  1.621034  0.438107  0.903794
2000-01-04       NaN       NaN       NaN
2000-01-05       NaN       NaN       NaN
2000-01-06       NaN       NaN       NaN
2000-01-07       NaN       NaN       NaN
2000-01-08  0.254374  1.240447  0.201052
2000-01-09  0.157795  0.791197  1.144209
2000-01-10  0.030876  0.371900  0.061932
```

Series와 함께 단일 함수를 `.transform()`에 전달하면 단일 Series가 반환됩니다.

```python
In [189]: tsdf["A"].transform(np.abs)
Out[189]: 
2000-01-01    0.428759
2000-01-02    0.168731
2000-01-03    1.621034
2000-01-04         NaN
2000-01-05         NaN
2000-01-06         NaN
2000-01-07         NaN
2000-01-08    0.254374
2000-01-09    0.157795
2000-01-10    0.030876
Freq: D, Name: A, dtype: float64
```

#### 여러 함수로 변환 (Transform with multiple functions)

여러 함수를 전달하면 열 MultiIndexed DataFrame이 생성됩니다. 첫 번째 레벨은 원래 프레임 열 이름이고 두 번째 레벨은 변환 함수의 이름입니다.

```python
In [190]: tsdf.transform([np.abs, lambda x: x + 1])
Out[190]: 
                   A                   B                   C          
            absolute  <lambda>  absolute  <lambda>  absolute  <lambda>
2000-01-01  0.428759  0.571241  0.864890  0.135110  0.675341  0.324659
2000-01-02  0.168731  0.831269  1.338144  2.338144  1.279321 -0.279321
2000-01-03  1.621034 -0.621034  0.438107  1.438107  0.903794  1.903794
2000-01-04       NaN       NaN       NaN       NaN       NaN       NaN
2000-01-05       NaN       NaN       NaN       NaN       NaN       NaN
2000-01-06       NaN       NaN       NaN       NaN       NaN       NaN
2000-01-07       NaN       NaN       NaN       NaN       NaN       NaN
2000-01-08  0.254374  1.254374  1.240447 -0.240447  0.201052  0.798948
2000-01-09  0.157795  0.842205  0.791197  1.791197  1.144209 -0.144209
2000-01-10  0.030876  0.969124  0.371900  1.371900  0.061932  1.061932
```

Series에 여러 함수를 전달하면 DataFrame이 생성됩니다. 결과 열 이름은 변환 함수가 됩니다.

```python
In [191]: tsdf["A"].transform([np.abs, lambda x: x + 1])
Out[191]: 
            absolute  <lambda>
2000-01-01  0.428759  0.571241
2000-01-02  0.168731  0.831269
2000-01-03  1.621034 -0.621034
2000-01-04       NaN       NaN
2000-01-05       NaN       NaN
2000-01-06       NaN       NaN
2000-01-07       NaN       NaN
2000-01-08  0.254374  1.254374
2000-01-09  0.157795  0.842205
2000-01-10  0.030876  0.969124
```

#### 딕셔너리로 변환 (Transforming with a dict)

함수의 딕셔너리를 전달하면 열별로 선택적 변환이 가능합니다.

```python
In [192]: tsdf.transform({"A": np.abs, "B": lambda x: x + 1})
Out[192]: 
                   A         B
2000-01-01  0.428759  0.135110
2000-01-02  0.168731  2.338144
2000-01-03  1.621034  1.438107
2000-01-04       NaN       NaN
2000-01-05       NaN       NaN
2000-01-06       NaN       NaN
2000-01-07       NaN       NaN
2000-01-08  0.254374 -0.240447
2000-01-09  0.157795  1.791197
2000-01-10  0.030876  1.371900
```

리스트의 딕셔너리를 전달하면 이러한 선택적 변환으로 MultiIndexed DataFrame이 생성됩니다.

```python
In [193]: tsdf.transform({"A": np.abs, "B": [lambda x: x + 1, "sqrt"]})
Out[193]: 
                   A         B          
            absolute  <lambda>      sqrt
2000-01-01  0.428759  0.135110       NaN
2000-01-02  0.168731  2.338144  1.156782
2000-01-03  1.621034  1.438107  0.661897
2000-01-04       NaN       NaN       NaN
2000-01-05       NaN       NaN       NaN
2000-01-06       NaN       NaN       NaN
2000-01-07       NaN       NaN       NaN
2000-01-08  0.254374 -0.240447       NaN
2000-01-09  0.157795  1.791197  0.889493
2000-01-10  0.030876  1.371900  0.609836
```

### 요소별 함수 적용 (Applying elementwise functions)

모든 함수가 벡터화될 수 없기 때문에(NumPy 배열을 받아 다른 배열이나 값을 반환), DataFrame의 [`map()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html#pandas.DataFrame.map)과 마찬가지로 Series의 [`map()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html#pandas.Series.map)은 단일 값을 받아 단일 값을 반환하는 모든 Python 함수를 허용합니다. 예를 들어:

```python
In [194]: df4 = df.copy()

In [195]: df4
Out[195]: 
        one       two     three
a  1.394981  1.772517       NaN
b  0.343054  1.912123 -0.050390
c  0.695246  1.478369  1.227435
d       NaN  0.279344 -0.613172

In [196]: def f(x):
   .....:    return len(str(x))
   .....: 

In [197]: df4["one"].map(f)
Out[197]: 
a    18
b    19
c    18
d     3
Name: one, dtype: int64

In [198]: df4.map(f)
Out[198]: 
   one  two  three
a   18   17      3
b   19   18     20
c   18   18     16
d    3   19     19
```

[`Series.map()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html#pandas.Series.map)에는 추가 기능이 있습니다. 보조 시리즈에 의해 정의된 값을 쉽게 "연결" 또는 "매핑"하는 데 사용할 수 있습니다. 이는 [병합/조인 기능](https://pandas.pydata.org/docs/user_guide/merging.html#merging)과 밀접하게 관련되어 있습니다:

```python
In [199]: s = pd.Series(
   .....:    ["six", "seven", "six", "seven", "six"], index=["a", "b", "c", "d", "e"]
   .....: )
   .....: 

In [200]: t = pd.Series({"six": 6.0, "seven": 7.0})

In [201]: s
Out[201]: 
a      six
b    seven
c      six
d    seven
e      six
dtype: object

In [202]: s.map(t)
Out[202]: 
a    6.0
b    7.0
c    6.0
d    7.0
e    6.0
dtype: float64
```

## 재색인 및 라벨 변경 (Reindexing and altering labels)

[`reindex()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.reindex.html#pandas.Series.reindex "pandas.Series.reindex")는 pandas의 기본적인 데이터 정렬 메서드입니다. 이는 레이블 정렬 기능에 의존하는 거의 모든 다른 기능을 구현하는 데 사용됩니다. 재색인은 특정 축을 따라 주어진 레이블 세트와 일치하도록 데이터를 맞추는 것을 의미합니다. 이는 다음과 같은 여러 가지를 수행합니다:

- 기존 데이터를 새로운 레이블 세트와 일치하도록 재정렬합니다
    
- 해당 레이블에 대한 데이터가 존재하지 않는 레이블 위치에 누락 값(NA) 표시를 삽입합니다
    
- 지정된 경우, 논리를 사용하여 누락된 레이블에 대한 데이터를 채웁니다(시계열 데이터 작업과 매우 관련됨)
    

다음은 간단한 예시입니다:

```python
In [203]: s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])

In [204]: s
Out[204]: 
a    1.695148
b    1.328614
c    1.234686
d   -0.385845
e   -1.326508
dtype: float64

In [205]: s.reindex(["e", "b", "f", "d"])
Out[205]: 
e   -1.326508
b    1.328614
f         NaN
d   -0.385845
dtype: float64
```

여기서 f 레이블은 Series에 포함되지 않았으므로 결과에 NaN으로 나타납니다.

DataFrame을 사용하면 인덱스와 열을 동시에 재색인할 수 있습니다:

```python
In [206]: df
Out[206]: 
        one       two     three
a  1.394981  1.772517       NaN
b  0.343054  1.912123 -0.050390
c  0.695246  1.478369  1.227435
d       NaN  0.279344 -0.613172

In [207]: df.reindex(index=["c", "f", "b"], columns=["three", "two", "one"])
Out[207]: 
      three       two       one
c  1.227435  1.478369  0.695246
f       NaN       NaN       NaN
b -0.050390  1.912123  0.343054
```

실제 축 레이블을 포함하는 Index 객체는 객체 간에 공유될 수 있습니다. 따라서 Series와 DataFrame이 있는 경우 다음과 같이 할 수 있습니다:

```python
In [208]: rs = s.reindex(df.index)

In [209]: rs
Out[209]: 
a    1.695148
b    1.328614
c    1.234686
d   -0.385845
dtype: float64

In [210]: rs.index is df.index
Out[210]: True
```

이는 재색인된 Series의 인덱스가 DataFrame의 인덱스와 동일한 Python 객체임을 의미합니다.

[`DataFrame.reindex()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html#pandas.DataFrame.reindex "pandas.DataFrame.reindex")는 또한 단일 labels 인수와 적용되는 axis를 지정하는 "축 스타일" 호출 규칙을 지원합니다.

```python
In [211]: df.reindex(["c", "f", "b"], axis="index")
Out[211]: 
        one       two     three
c  0.695246  1.478369  1.227435
f       NaN       NaN       NaN
b  0.343054  1.912123 -0.050390

In [212]: df.reindex(["three", "two", "one"], axis="columns")
Out[212]: 
      three       two       one
a       NaN  1.772517  1.394981
b -0.050390  1.912123  0.343054
c  1.227435  1.478369  0.695246
d -0.613172  0.279344       NaN
```

참고

[MultiIndex / Advanced Indexing](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced)은 재색인을 수행하는 더욱 간결한 방법입니다.

참고

성능에 민감한 코드를 작성할 때 재색인 닌자가 되는 데 시간을 투자할 만한 좋은 이유가 있습니다: 많은 작업이 사전 정렬된 데이터에서 더 빠릅니다. 정렬되지 않은 두 DataFrame을 내부적으로 추가하면 재색인 단계가 트리거됩니다. 탐색적 분석에서는 거의 차이를 느끼지 못할 것입니다(reindex가 많이 최적화되었기 때문에), 하지만 CPU 사이클이 중요할 때 여기저기에 몇 가지 명시적인 reindex 호출을 뿌려두면 영향을 미칠 수 있습니다.

### 다른 객체와 정렬하기 위한 재색인 (Reindexing to align with another object)

객체를 가져와 그 축을 다른 객체와 동일하게 레이블을 지정하도록 재색인하고 싶을 수 있습니다. 이에 대한 구문이 직관적이지만 다소 장황하기는 하지만, 이는 충분히 일반적인 작업이므로 이를 단순화하기 위해 [`reindex_like()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex_like.html#pandas.DataFrame.reindex_like "pandas.DataFrame.reindex_like") 메서드를 사용할 수 있습니다:

```python
In [213]: df2 = df.reindex(["a", "b", "c"], columns=["one", "two"])

In [214]: df3 = df2 - df2.mean()

In [215]: df2
Out[215]: 
        one       two
a  1.394981  1.772517
b  0.343054  1.912123
c  0.695246  1.478369

In [216]: df3
Out[216]: 
        one       two
a  0.583888  0.051514
b -0.468040  0.191120
c -0.115848 -0.242634

In [217]: df.reindex_like(df2)
Out[217]: 
        one       two
a  1.394981  1.772517
b  0.343054  1.912123
c  0.695246  1.478369
```

### align을 사용하여 객체를 서로 정렬하기 (Aligning objects with each other with align)

[`align()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.align.html#pandas.Series.align "pandas.Series.align") 메서드는 두 객체를 동시에 정렬하는 가장 빠른 방법입니다. 이는 join 인수를 지원합니다(결합 및 병합과 관련됨):

- join='outer': 인덱스의 합집합을 취함(기본값)
- join='left': 호출 객체의 인덱스를 사용
- join='right': 전달된 객체의 인덱스를 사용
- join='inner': 인덱스의 교집합을 취함

이는 재색인된 두 Series를 포함하는 튜플을 반환합니다:

```python
In [218]: s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])

In [219]: s1 = s[:4]

In [220]: s2 = s[1:]

In [221]: s1.align(s2)
Out[221]: 
(a   -0.186646
 b   -1.692424
 c   -0.303893
 d   -1.425662
 e         NaN
 dtype: float64,
 a         NaN
 b   -1.692424
 c   -0.303893
 d   -1.425662
 e    1.114285
 dtype: float64)

In [222]: s1.align(s2, join="inner")
Out[222]: 
(b   -1.692424
 c   -0.303893
 d   -1.425662
 dtype: float64,
 b   -1.692424
 c   -0.303893
 d   -1.425662
 dtype: float64)

In [223]: s1.align(s2, join="left")
Out[223]: 
(a   -0.186646
 b   -1.692424
 c   -0.303893
 d   -1.425662
 dtype: float64,
 a         NaN
 b   -1.692424
 c   -0.303893
 d   -1.425662
 dtype: float64)
```

DataFrame의 경우, join 메서드는 기본적으로 인덱스와 열 모두에 적용됩니다:

```python
In [224]: df.align(df2, join="inner")
Out[224]: 
(        one       two
 a  1.394981  1.772517
 b  0.343054  1.912123
 c  0.695246  1.478369,
         one       two
 a  1.394981  1.772517
 b  0.343054  1.912123
 c  0.695246  1.478369)
```

axis 옵션을 전달하여 지정된 축에서만 정렬할 수도 있습니다:

```python
In [225]: df.align(df2, join="inner", axis=0)
Out[225]: 
(        one       two     three
 a  1.394981  1.772517       NaN
 b  0.343054  1.912123 -0.050390
 c  0.695246  1.478369  1.227435,
         one       two
 a  1.394981  1.772517
 b  0.343054  1.912123
 c  0.695246  1.478369)
```

[`DataFrame.align()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.align.html#pandas.DataFrame.align "pandas.DataFrame.align")에 Series를 전달하는 경우, axis 인수를 사용하여 DataFrame의 인덱스나 열 중 하나를 선택하여 두 객체를 정렬할 수 있습니다:

```python
In [226]: df.align(df2.iloc[0], axis=1)
Out[226]: 
(        one     three       two
 a  1.394981       NaN  1.772517
 b  0.343054 -0.050390  1.912123
 c  0.695246  1.227435  1.478369
 d       NaN -0.613172  0.279344,
 one      1.394981
 three         NaN
 two      1.772517
 Name: a, dtype: float64)
```

### 재색인하면서 채우기 (Filling while reindexing)

[`reindex()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.reindex.html#pandas.Series.reindex "pandas.Series.reindex")는 다음 표에서 선택한 채우기 메서드인 선택적 매개변수 method를 사용합니다:

|메서드|동작|
|---|---|
|pad / ffill|값을 앞으로 채우기|
|bfill / backfill|값을 뒤로 채우기|
|nearest|가장 가까운 인덱스 값에서 채우기|

간단한 Series에서 이러한 채우기 메서드를 설명합니다:

```python
In [227]: rng = pd.date_range("1/3/2000", periods=8)

In [228]: ts = pd.Series(np.random.randn(8), index=rng)

In [229]: ts2 = ts.iloc[[0, 3, 6]]

In [230]: ts
Out[230]: 
2000-01-03    0.183051
2000-01-04    0.400528
2000-01-05   -0.015083
2000-01-06    2.395489
2000-01-07    1.414806
2000-01-08    0.118428
2000-01-09    0.733639
2000-01-10   -0.936077
Freq: D, dtype: float64

In [231]: ts2
Out[231]: 
2000-01-03    0.183051
2000-01-06    2.395489
2000-01-09    0.733639
Freq: 3D, dtype: float64

In [232]: ts2.reindex(ts.index)
Out[232]: 
2000-01-03    0.183051
2000-01-04         NaN
2000-01-05         NaN
2000-01-06    2.395489
2000-01-07         NaN
2000-01-08         NaN
2000-01-09    0.733639
2000-01-10         NaN
Freq: D, dtype: float64

In [233]: ts2.reindex(ts.index, method="ffill")
Out[233]: 
2000-01-03    0.183051
2000-01-04    0.183051
2000-01-05    0.183051
2000-01-06    2.395489
2000-01-07    2.395489
2000-01-08    2.395489
2000-01-09    0.733639
2000-01-10    0.733639
Freq: D, dtype: float64

In [234]: ts2.reindex(ts.index, method="bfill")
Out[234]: 
2000-01-03    0.183051
2000-01-04    2.395489
2000-01-05    2.395489
2000-01-06    2.395489
2000-01-07    0.733639
2000-01-08    0.733639
2000-01-09    0.733639
2000-01-10         NaN
Freq: D, dtype: float64

In [235]: ts2.reindex(ts.index, method="nearest")
Out[235]: 
2000-01-03    0.183051
2000-01-04    0.183051
2000-01-05    2.395489
2000-01-06    2.395489
2000-01-07    2.395489
2000-01-08    0.733639
2000-01-09    0.733639
2000-01-10    0.733639
Freq: D, dtype: float64
```

이러한 방법들은 인덱스가 증가하거나 감소하는 순서로 정렬되어 있어야 합니다.

같은 결과를 [ffill](https://pandas.pydata.org/docs/user_guide/missing_data.html#missing-data-fillna) (method='nearest' 제외) 또는 [interpolate](https://pandas.pydata.org/docs/user_guide/missing_data.html#missing-data-interpolate)를 사용하여 얻을 수 있다는 점에 유의하세요:

```python
In [236]: ts2.reindex(ts.index).ffill()
Out[236]: 
2000-01-03    0.183051
2000-01-04    0.183051
2000-01-05    0.183051
2000-01-06    2.395489
2000-01-07    2.395489
2000-01-08    2.395489
2000-01-09    0.733639
2000-01-10    0.733639
Freq: D, dtype: float64
```

[reindex()](https://pandas.pydata.org/docs/reference/api/pandas.Series.reindex.html#pandas.Series.reindex "pandas.Series.reindex")는 인덱스가 단조 증가 또는 감소하지 않으면 ValueError를 발생시킵니다. [fillna()](https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html#pandas.Series.fillna "pandas.Series.fillna")와 [interpolate()](https://pandas.pydata.org/docs/reference/api/pandas.Series.interpolate.html#pandas.Series.interpolate "pandas.Series.interpolate")는 인덱스 순서에 대한 검사를 수행하지 않습니다.

### 리인덱싱 중 채우기 제한 (Limits on filling while reindexing)

`limit`와 `tolerance` 인수는 리인덱싱 중 채우기에 대한 추가 제어를 제공합니다. Limit은 연속 일치의 최대 수를 지정합니다:

```python
In [237]: ts2.reindex(ts.index, method="ffill", limit=1)
Out[237]: 
2000-01-03    0.183051
2000-01-04    0.183051
2000-01-05         NaN
2000-01-06    2.395489
2000-01-07    2.395489
2000-01-08         NaN
2000-01-09    0.733639
2000-01-10    0.733639
Freq: D, dtype: float64
```

반면에 tolerance는 인덱스와 인덱서 값 사이의 최대 거리를 지정합니다:

```python
In [238]: ts2.reindex(ts.index, method="ffill", tolerance="1 day")
Out[238]: 
2000-01-03    0.183051
2000-01-04    0.183051
2000-01-05         NaN
2000-01-06    2.395489
2000-01-07    2.395489
2000-01-08         NaN
2000-01-09    0.733639
2000-01-10    0.733639
Freq: D, dtype: float64
```

DatetimeIndex, TimedeltaIndex 또는 PeriodIndex에서 사용될 때 tolerance가 가능한 경우 Timedelta로 강제 변환된다는 점에 주의하세요. 이를 통해 적절한 문자열로 tolerance를 지정할 수 있습니다.

### 축에서 레이블 삭제하기 (Dropping labels from an axis)

reindex와 밀접하게 관련된 메서드는 drop() 함수입니다. 이는 축에서 레이블 세트를 제거합니다:

```python
In [239]: df
Out[239]: 
        one       two     three
a  1.394981  1.772517       NaN
b  0.343054  1.912123 -0.050390
c  0.695246  1.478369  1.227435
d       NaN  0.279344 -0.613172

In [240]: df.drop(["a", "d"], axis=0)
Out[240]: 
        one       two     three
b  0.343054  1.912123 -0.050390
c  0.695246  1.478369  1.227435

In [241]: df.drop(["one"], axis=1)
Out[241]: 
        two     three
a  1.772517       NaN
b  1.912123 -0.050390
c  1.478369  1.227435
d  0.279344 -0.613172
```

다음 방법도 작동하지만 조금 덜 명확/깔끔합니다:

```python
In [242]: df.reindex(df.index.difference(["a", "d"]))
Out[242]: 
        one       two     three
b  0.343054  1.912123 -0.050390
c  0.695246  1.478369  1.227435
```

### 레이블 이름 변경 / 매핑 (Renaming / mapping labels)

rename() 메서드를 사용하면 일부 매핑(dict 또는 Series) 또는 임의의 함수를 기반으로 축의 레이블을 변경할 수 있습니다.

```python
In [243]: s
Out[243]: 
a   -0.186646
b   -1.692424
c   -0.303893
d   -1.425662
e    1.114285
dtype: float64

In [244]: s.rename(str.upper)
Out[244]: 
A   -0.186646
B   -1.692424
C   -0.303893
D   -1.425662
E    1.114285
dtype: float64
```

함수를 전달하면 레이블 중 하나로 호출될 때 값을 반환해야 합니다(그리고 고유한 값 세트를 생성해야 합니다). dict나 Series도 사용할 수 있습니다:

```python
In [245]: df.rename(
   …..:    columns={"one": "foo", "two": "bar"},
   …..:    index={"a": "apple", "b": "banana", "d": "durian"},
   …..: )
   …..: 
Out[245]: 
             foo       bar     three
apple   1.394981  1.772517       NaN
banana  0.343054  1.912123 -0.050390
c       0.695246  1.478369  1.227435
durian       NaN  0.279344 -0.613172
```

매핑에 열/인덱스 레이블이 포함되지 않으면 이름이 변경되지 않습니다. 매핑에 추가 레이블이 있어도 오류가 발생하지 않습니다.

DataFrame.rename()은 단일 매퍼와 해당 매핑을 적용할 축을 지정하는 "축 스타일" 호출 규칙도 지원합니다.

```python
In [246]: df.rename({"one": "foo", "two": "bar"}, axis="columns")
Out[246]: 
        foo       bar     three
a  1.394981  1.772517       NaN
b  0.343054  1.912123 -0.050390
c  0.695246  1.478369  1.227435
d       NaN  0.279344 -0.613172

In [247]: df.rename({"a": "apple", "b": "banana", "d": "durian"}, axis="index")
Out[247]: 
             one       two     three
apple   1.394981  1.772517       NaN
banana  0.343054  1.912123 -0.050390
c       0.695246  1.478369  1.227435
durian       NaN  0.279344 -0.613172
```

마지막으로, rename()은 Series.name 속성을 변경하기 위해 스칼라 또는 리스트와 유사한 형태도 허용합니다.

```python
In [248]: s.rename("scalar-name")
Out[248]: 
a   -0.186646
b   -1.692424
c   -0.303893
d   -1.425662
e    1.114285
Name: scalar-name, dtype: float64
```

DataFrame.rename_axis()와 Series.rename_axis() 메서드를 사용하면 MultiIndex의 특정 이름을 변경할 수 있습니다(레이블과는 반대).

```python
In [249]: df = pd.DataFrame(
   …..:    {"x": [1, 2, 3, 4, 5, 6], "y": [10, 20, 30, 40, 50, 60]},
   …..:    index=pd.MultiIndex.from_product(
   …..:        [["a", "b", "c"], [1, 2]], names=["let", "num"]
   …..:    ),
   …..: )
   …..: 

In [250]: df
Out[250]: 
         x   y
let num       
a   1    1  10
    2    2  20
b   1    3  30
    2    4  40
c   1    5  50
    2    6  60

In [251]: df.rename_axis(index={"let": "abc"})
Out[251]: 
         x   y
abc num       
a   1    1  10
    2    2  20
b   1    3  30
    2    4  40
c   1    5  50
    2    6  60

In [252]: df.rename_axis(index=str.upper)
Out[252]: 
         x   y
LET NUM       
a   1    1  10
    2    2  20
b   1    3  30
    2    4  40
c   1    5  50
    2    6  60
```

## 반복 (Iteration)

pandas 객체에 대한 기본 반복의 동작은 유형에 따라 다릅니다. Series를 반복할 때는 배열과 유사하게 간주되며 기본 반복은 값을 생성합니다. DataFrame은 객체의 "키"를 반복하는 딕셔너리와 유사한 규칙을 따릅니다.

간단히 말해, 기본 반복 (for i in object)은 다음을 생성합니다:

- Series: 값
- DataFrame: 열 레이블

따라서 예를 들어 DataFrame을 반복하면 열 이름이 제공됩니다:

```python
In [253]: df = pd.DataFrame(
   …..:    {"col1": np.random.randn(3), "col2": np.random.randn(3)}, index=["a", "b", "c"]
   …..: )
   …..: 

In [254]: for col in df:
   …..:    print(col)
   …..: 
col1
col2
```

pandas 객체에는 또한 (키, 값) 쌍을 반복하는 딕셔너리와 유사한 items() 메서드가 있습니다.

DataFrame의 행을 반복하려면 다음 메서드를 사용할 수 있습니다:

- iterrows(): DataFrame의 행을 (인덱스, Series) 쌍으로 반복합니다. 이는 행을 Series 객체로 변환하며, 이는 데이터 유형을 변경할 수 있고 일부 성능 영향이 있습니다.
- itertuples(): DataFrame의 행을 값의 namedtuples로 반복합니다. 이는 iterrows()보다 훨씬 빠르며, 대부분의 경우 DataFrame의 값을 반복하는 데 사용하는 것이 좋습니다.

> [!warning]
> pandas 객체를 반복하는 것은 일반적으로 느립니다. 많은 경우에 행을 수동으로 반복할 필요가 없으며 다음 접근 방식 중 하나로 피할 수 있습니다:
> 
> - 벡터화된 솔루션을 찾으세요: 많은 작업은 내장 메서드나 NumPy 함수, (불리언) 인덱싱 등을 사용하여 수행할 수 있습니다.
> - 전체 DataFrame/Series에서 한 번에 작동할 수 없는 함수가 있는 경우, 값을 반복하는 대신 apply()를 사용하는 것이 좋습니다. 함수 적용에 대한 문서를 참조하세요.
> - 값에 대해 반복적인 조작을 해야 하지만 성능이 중요한 경우, cython이나 numba로 내부 루프를 작성하는 것을 고려하세요. 이 접근 방식의 몇 가지 예는 성능 향상 섹션을 참조하세요.

> [!warning]
> 반복 중인 것을 절대 수정하지 마세요. 이는 모든 경우에 작동한다고 보장되지 않습니다. 데이터 유형에 따라 반복자는 복사본을 반환하고 뷰를 반환하지 않으며, 여기에 쓰는 것은 아무런 효과가 없습니다!
> 
> 예를 들어, 다음 경우에는 값을 설정해도 아무런 효과가 없습니다:
> 
> ```python
> In [255]: df = pd.DataFrame({"a": [1, 2, 3], "b": ["a", "b", "c"]})
> 
> In [256]: for index, row in df.iterrows():
>    …..:    row["a"] = 10
>    …..: 
> 
> In [257]: df
> Out[257]: 
>    a  b
> 0  1  a
> 1  2  b
> 2  3  c
> ```

### items (아이템)

일관된 딕셔너리형 인터페이스에 맞게, items()는 키-값 쌍을 순회합니다:

- Series: (인덱스, 스칼라 값) 쌍
    
- DataFrame: (열, Series) 쌍
    

예를 들어:

```python
for label, ser in df.items():
   print(label)
   print(ser)

a
0    1
1    2
2    3
Name: a, dtype: int64
b
0    a
1    b
2    c
Name: b, dtype: object
```

### iterrows (행 순회)

iterrows()를 사용하면 DataFrame의 행을 Series 객체로 순회할 수 있습니다. 각 인덱스 값과 함께 각 행의 데이터를 포함하는 Series를 반환하는 반복자를 반환합니다:

```python
for row_index, row in df.iterrows():
   print(row_index, row, sep="\n")

0
a    1
b    a
Name: 0, dtype: object
1
a    2
b    b
Name: 1, dtype: object
2
a    3
b    c
Name: 2, dtype: object
```

> [!NOTE]
> iterrows()는 각 행에 대해 Series를 반환하므로 행 간에 데이터 타입을 보존하지 않습니다 (데이터 타입은 DataFrame의 열 간에 보존됩니다). 예를 들어,
> 
> ```python
> df_orig = pd.DataFrame([[1, 1.5]], columns=["int", "float"])
> 
> df_orig.dtypes
> int        int64
> float    float64
> dtype: object
> 
> row = next(df_orig.iterrows())[1]
> 
> row
> int      1.0
> float    1.5
> Name: 0, dtype: float64
> ```
> 
> Series로 반환된 row의 모든 값은 이제 float으로 변환되었으며, 열 x의 원래 정수 값도 포함됩니다:
> 
> ```python
> row["int"].dtype
> dtype('float64')
> 
> df_orig["int"].dtype
> dtype('int64')
> ```
> 
> 행을 순회하면서 데이터 타입을 보존하려면 itertuples()를 사용하는 것이 더 좋습니다. 이는 값의 namedtuple을 반환하며 일반적으로 iterrows()보다 훨씬 빠릅니다.

예를 들어, DataFrame을 전치하는 인위적인 방법은 다음과 같습니다:

```python
df2 = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})

print(df2)
   x  y
0  1  4
1  2  5
2  3  6

print(df2.T)
   0  1  2
x  1  2  3
y  4  5  6

df2_t = pd.DataFrame({idx: values for idx, values in df2.iterrows()})

print(df2_t)
   0  1  2
x  1  2  3
y  4  5  6
```

### itertuples (튜플 순회)

itertuples() 메서드는 DataFrame의 각 행에 대해 namedtuple을 생성하는 반복자를 반환합니다. 튜플의 첫 번째 요소는 해당 행의 인덱스 값이며, 나머지 값들은 행 값입니다.

예를 들어:

```python
for row in df.itertuples():
   print(row)

Pandas(Index=0, a=1, b='a')
Pandas(Index=1, a=2, b='b')
Pandas(Index=2, a=3, b='c')
```

이 메서드는 행을 Series 객체로 변환하지 않습니다. 단순히 namedtuple 내부의 값만 반환합니다. 따라서 itertuples()는 값의 데이터 타입을 보존하며 일반적으로 iterrows()보다 빠릅니다.

> 열 이름이 유효한 Python 식별자가 아니거나, 반복되거나, 밑줄로 시작하는 경우 위치 이름으로 변경됩니다. 열이 많은 경우 (>255), 일반 튜플이 반환됩니다.

## .dt 접근자

Series는 datetime/period와 유사한 Series인 경우 Series의 값에 대한 datetime과 유사한 속성을 간결하게 반환하기 위한 접근자를 가지고 있습니다. 이는 기존 Series와 같은 인덱스를 가진 Series를 반환합니다.


```python
# datetime
s = pd.Series(pd.date_range("20130101 09:10:12", periods=4))

s
0   2013-01-01 09:10:12
1   2013-01-02 09:10:12
2   2013-01-03 09:10:12
3   2013-01-04 09:10:12
dtype: datetime64[ns]

s.dt.hour
0    9
1    9
2    9
3    9
dtype: int32

s.dt.second
0    12
1    12
2    12
3    12
dtype: int32

s.dt.day
0    1
1    2
2    3
3    4
dtype: int32
```

이를 통해 다음과 같은 멋진 표현이 가능합니다:

```python
s[s.dt.day == 2]
1   2013-01-02 09:10:12
dtype: datetime64[ns]
```

시간대를 인식하는 변환을 쉽게 생성할 수 있습니다:

```python
stz = s.dt.tz_localize("US/Eastern")

stz
0   2013-01-01 09:10:12-05:00
1   2013-01-02 09:10:12-05:00
2   2013-01-03 09:10:12-05:00
3   2013-01-04 09:10:12-05:00
dtype: datetime64[ns, US/Eastern]

stz.dt.tz
<DstTzInfo 'US/Eastern' LMT-1 day, 19:04:00 STD>
```

이러한 유형의 작업을 연결할 수도 있습니다:

```python
s.dt.tz_localize("UTC").dt.tz_convert("US/Eastern")
0   2013-01-01 04:10:12-05:00
1   2013-01-02 04:10:12-05:00
2   2013-01-03 04:10:12-05:00
3   2013-01-04 04:10:12-05:00
dtype: datetime64[ns, US/Eastern]
```

Series.dt.strftime()를 사용하여 datetime 값을 문자열로 포맷할 수도 있습니다. 이는 표준 strftime()과 동일한 형식을 지원합니다.


```python
# DatetimeIndex
s = pd.Series(pd.date_range("20130101", periods=4))

s
0   2013-01-01
1   2013-01-02
2   2013-01-03
3   2013-01-04
dtype: datetime64[ns]

s.dt.strftime("%Y/%m/%d")
0    2013/01/01
1    2013/01/02
2    2013/01/03
3    2013/01/04
dtype: object
```


```python
# PeriodIndex
s = pd.Series(pd.period_range("20130101", periods=4))

s
0    2013-01-01
1    2013-01-02
2    2013-01-03
3    2013-01-04
dtype: period[D]

s.dt.strftime("%Y/%m/%d")
0    2013/01/01
1    2013/01/02
2    2013/01/03
3    2013/01/04
dtype: object
```

.dt 접근자는 period와 timedelta 데이터 타입에도 작동합니다.


```python
# period
s = pd.Series(pd.period_range("20130101", periods=4, freq="D"))

s
0    2013-01-01
1    2013-01-02
2    2013-01-03
3    2013-01-04
dtype: period[D]

s.dt.year
0    2013
1    2013
2    2013
3    2013
dtype: int64

s.dt.day
0    1
1    2
2    3
3    4
dtype: int64
```


```python
# timedelta
s = pd.Series(pd.timedelta_range("1 day 00:00:05", periods=4, freq="s"))

s
0   1 days 00:00:05
1   1 days 00:00:06
2   1 days 00:00:07
3   1 days 00:00:08
dtype: timedelta64[ns]

s.dt.days
0    1
1    1
2    1
3    1
dtype: int64

s.dt.seconds
0    5
1    6
2    7
3    8
dtype: int32

s.dt.components
   days  hours  minutes  seconds  milliseconds  microseconds  nanoseconds
0     1      0        0        5             0             0            0
1     1      0        0        6             0             0            0
2     1      0        0        7             0             0            0
3     1      0        0        8             0             0            0
```

> Series.dt는 datetime과 유사하지 않은 값에 접근하면 TypeError를 발생시킵니다.

## 벡터화된 문자열 메서드

Series는 배열의 각 요소에 대해 쉽게 작업할 수 있는 문자열 처리 메서드 집합을 갖추고 있습니다. 아마도 가장 중요한 점은 이러한 메서드가 누락/NA 값을 자동으로 제외한다는 것입니다. 이들은 Series의 str 속성을 통해 접근되며 일반적으로 해당하는 (스칼라) 내장 문자열 메서드와 일치하는 이름을 가집니다. 예를 들어:

```python
s = pd.Series(
   ["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"], dtype="string"
)

s.str.lower()
0       a
1       b
2       c
3    aaba
4    baca
5    <NA>
6    caba
7     dog
8     cat
dtype: string
```

강력한 패턴 매칭 메서드도 제공되지만, 패턴 매칭은 일반적으로 기본적으로 정규 표현식을 사용하며 (일부 경우에는 항상 사용합니다).

> pandas 1.0 이전에는 문자열 메서드가 object-dtype Series에서만 사용 가능했습니다. pandas 1.0은 문자열 전용인 StringDtype을 추가했습니다. 자세한 내용은 텍스트 데이터 타입을 참조하세요.

전체 설명은 벡터화된 문자열 메서드를 참조하세요.


## 정렬 (Sorting)

pandas는 세 가지 종류의 정렬을 지원합니다: 인덱스 레이블로 정렬, 열 값으로 정렬, 그리고 둘의 조합으로 정렬하는 방법입니다.

### 인덱스로 정렬 (By index)

[Series.sort_index()](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_index.html#pandas.Series.sort_index "pandas.Series.sort_index")와 [DataFrame.sort_index()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html#pandas.DataFrame.sort_index "pandas.DataFrame.sort_index") 메서드는 pandas 객체를 인덱스 레벨로 정렬하는 데 사용됩니다.

```python
df = pd.DataFrame(
   {
       "one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
       "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
       "three": pd.Series(np.random.randn(3), index=["b", "c", "d"]),
   }
)

unsorted_df = df.reindex(
   index=["a", "d", "c", "b"], columns=["three", "two", "one"]
)

unsorted_df
```

```
      three       two       one
a       NaN -1.152244  0.562973
d -0.252916 -0.109597       NaN
c  1.273388 -0.167123  0.640382
b -0.098217  0.009797 -1.299504
```


```python
# DataFrame
unsorted_df.sort_index()
```

```
      three       two       one
a       NaN -1.152244  0.562973
b -0.098217  0.009797 -1.299504
c  1.273388 -0.167123  0.640382
d -0.252916 -0.109597       NaN
```

```python
unsorted_df.sort_index(ascending=False)
```

```
      three       two       one
d -0.252916 -0.109597       NaN
c  1.273388 -0.167123  0.640382
b -0.098217  0.009797 -1.299504
a       NaN -1.152244  0.562973
```

```python
unsorted_df.sort_index(axis=1)
```

```
        one     three       two
a  0.562973       NaN -1.152244
d       NaN -0.252916 -0.109597
c  0.640382  1.273388 -0.167123
b -1.299504 -0.098217  0.009797
```


```python
# Series
unsorted_df["three"].sort_index()
```

```
a         NaN
b   -0.098217
c    1.273388
d   -0.252916
Name: three, dtype: float64
```

인덱스로 정렬하는 것은 또한 정렬되는 인덱스에 적용할 수 있는 callable 함수를 취하는 key 파라미터를 지원합니다. MultiIndex 객체의 경우, key는 level로 지정된 레벨에 따라 적용됩니다.

```python
s1 = pd.DataFrame({"a": ["B", "a", "C"], "b": [1, 2, 3], "c": [2, 3, 4]}).set_index(
   list("ab")
)

s1
```

```
     c
a b   
B 1  2
a 2  3
C 3  4
```

```python
s1.sort_index(level="a")
```

```
     c
a b   
B 1  2
C 3  4
a 2  3
```

```python
s1.sort_index(level="a", key=lambda idx: idx.str.lower())
```

```
     c
a b   
a 2  3
B 1  2
C 3  4
```

값으로 키 정렬에 대한 정보는 [값 정렬](https://pandas.pydata.org/docs/user_guide/basics.html#basics-sort-value-key)을 참조하세요.

### 값으로 정렬 (By values)

[Series.sort_values()](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html#pandas.Series.sort_values "pandas.Series.sort_values") 메서드는 Series를 값으로 정렬하는 데 사용됩니다. [DataFrame.sort_values()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values "pandas.DataFrame.sort_values") 메서드는 DataFrame을 열 또는 행 값으로 정렬하는 데 사용됩니다. [DataFrame.sort_values()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values "pandas.DataFrame.sort_values")의 선택적 by 파라미터는 정렬된 순서를 결정하는 데 사용할 하나 이상의 열을 지정하는 데 사용될 수 있습니다.

```python
df1 = pd.DataFrame(
   {"one": [2, 1, 1, 1], "two": [1, 3, 2, 4], "three": [5, 4, 3, 2]}
)

df1.sort_values(by="two")
```

```
   one  two  three
0    2    1      5
2    1    2      3
1    1    3      4
3    1    4      2
```

by 파라미터는 열 이름 목록을 받을 수 있습니다. 예:

```python
df1[["one", "two", "three"]].sort_values(by=["one", "two"])
```

```
   one  two  three
2    1    2      3
1    1    3      4
3    1    4      2
0    2    1      5
```

이 메서드들은 na_position 인수를 통해 NA 값을 특별히 처리합니다:

```python
s[2] = np.nan

s.sort_values()
```

```
0       A
3    Aaba
1       B
4    Baca
6    CABA
8     cat
7     dog
2    <NA>
5    <NA>
dtype: string
```

```python
s.sort_values(na_position="first")
```

```
2    <NA>
5    <NA>
0       A
3    Aaba
1       B
4    Baca
6    CABA
8     cat
7     dog
dtype: string
```

정렬은 또한 정렬되는 값에 적용할 callable 함수를 취하는 key 파라미터를 지원합니다.

```python
s1 = pd.Series(["B", "a", "C"])

s1.sort_values()
```

```
0    B
2    C
1    a
dtype: object
```

```python
s1.sort_values(key=lambda x: x.str.lower())
```

```
1    a
0    B
2    C
dtype: object
```

key는 값의 [Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")를 받아 변환된 값으로 동일한 shape의 Series 또는 배열을 반환해야 합니다. DataFrame 객체의 경우, key는 열마다 적용되므로 key는 여전히 Series를 예상하고 Series를 반환해야 합니다. 예:

```python
df = pd.DataFrame({"a": ["B", "a", "C"], "b": [1, 2, 3]})

df.sort_values(by="a")
```

```
   a  b
0  B  1
2  C  3
1  a  2
```

```python
df.sort_values(by="a", key=lambda col: col.str.lower())
```

```
   a  b
1  a  2
0  B  1
2  C  3
```

각 열의 이름이나 유형을 사용하여 다른 열에 다른 함수를 적용할 수 있습니다.

### 인덱스와 값으로 정렬 (By indexes and values)

[DataFrame.sort_values()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values "pandas.DataFrame.sort_values")의 by 파라미터로 전달된 문자열은 열 또는 인덱스 레벨 이름을 참조할 수 있습니다.


```python
# MultiIndex 생성
idx = pd.MultiIndex.from_tuples(
   [("a", 1), ("a", 2), ("a", 2), ("b", 2), ("b", 1), ("b", 1)]
)

idx.names = ["first", "second"]

# DataFrame 생성
df_multi = pd.DataFrame({"A": np.arange(6, 0, -1)}, index=idx)

df_multi
```

```
              A
first second   
a     1       6
      2       5
      2       4
b     2       3
      1       2
      1       1
```

'second' (인덱스)와 'A' (열)로 정렬

```python
df_multi.sort_values(by=["second", "A"])
```

```
              A
first second   
b     1       1
      1       2
a     1       6
b     2       3
a     2       4
      2       5
```

> 문자열이 열 이름과 인덱스 레벨 이름 모두와 일치하는 경우 경고가 발생하고 열이 우선합니다. 이는 향후 버전에서 모호성 오류를 발생시킬 것입니다.

### searchsorted

Series는 [numpy.ndarray.searchsorted()](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.searchsorted.html#numpy.ndarray.searchsorted "(in NumPy v1.26)")와 유사하게 작동하는 [searchsorted()](https://pandas.pydata.org/docs/reference/api/pandas.Series.searchsorted.html#pandas.Series.searchsorted "pandas.Series.searchsorted") 메서드를 가지고 있습니다.

```python
ser = pd.Series([1, 2, 3])

ser.searchsorted([0, 3])
```

```
array([0, 2])
```

```python
ser.searchsorted([0, 4])
```

```
array([0, 3])
```

```python
ser.searchsorted([1, 3], side="right")
```

```
array([1, 3])
```

```python
ser.searchsorted([1, 3], side="left")
```

```
array([0, 2])
```

```python
ser = pd.Series([3, 1, 2])

ser.searchsorted([0, 3], sorter=np.argsort(ser))
```

```
array([0, 2])
```

### 가장 작은 / 가장 큰 값 (smallest / largest values)

Series는 가장 작은 또는 가장 큰 n개의 값을 반환하는 [nsmallest()](https://pandas.pydata.org/docs/reference/api/pandas.Series.nsmallest.html#pandas.Series.nsmallest "pandas.Series.nsmallest")와 [nlargest()](https://pandas.pydata.org/docs/reference/api/pandas.Series.nlargest.html#pandas.Series.nlargest "pandas.Series.nlargest") 메서드를 가지고 있습니다. 큰 Series의 경우 전체 Series를 정렬하고 결과에 대해 head(n)을 호출하는 것보다 훨씬 빠를 수 있습니다.

```python
s = pd.Series(np.random.permutation(10))

s
```

```
0    2
1    0
2    3
3    7
4    1
5    5
6    9
7    6
8    8
9    4
dtype: int64
```

```python
s.sort_values()
```

```
1    0
4    1
0    2
2    3
9    4
5    5
7    6
3    7
8    8
6    9
dtype: int64
```

```python
s.nsmallest(3)
```

```
1    0
4    1
0    2
dtype: int64
```

```python
s.nlargest(3)
```

```
6    9
8    8
3    7
dtype: int64
```

DataFrame도 nlargest와 nsmallest 메서드를 가지고 있습니다.

```python
df = pd.DataFrame(
   {
       "a": [-2, -1, 1, 10, 8, 11, -1],
       "b": list("abdceff"),
       "c": [1.0, 2.0, 4.0, 3.2, np.nan, 3.0, 4.0],
   }
)

df.nlargest(3, "a")
```

```
    a  b    c
5  11  f  3.0
3  10  c  3.2
4   8  e  NaN
```

```python
df.nlargest(5, ["a", "c"])
```

```
    a  b    c
5  11  f  3.0
3  10  c  3.2
4   8  e  NaN
2   1  d  4.0
6  -1  f  4.0
```

```python
df.nsmallest(3, "a")
```

```
   a  b    c
0 -2  a  1.0
1 -1  b  2.0
6 -1  f  4.0
```

```python
df.nsmallest(5, ["a", "c"])
```

```
   a  b    c
0 -2  a  1.0
1 -1  b  2.0
6 -1  f  4.0
2  1  d  4.0
4  8  e  NaN
```

### MultiIndex 컬럼으로 정렬하기 (Sorting by a MultiIndex column)

컬럼이 MultiIndex인 경우 정렬할 때 명시적으로 지정해야 하며, `by`에 모든 레벨을 완전히 지정해야 합니다.

```python
df1.columns = pd.MultiIndex.from_tuples(
   [("a", "one"), ("a", "two"), ("b", "three")]
)

df1.sort_values(by=("a", "two"))
```
```
    a         b
  one two three
0   2   1     5
2   1   2     3
1   1   3     4
3   1   4     2
```

## 복사 (Copying)

pandas 객체의 [copy()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.copy.html#pandas.DataFrame.copy) 메서드는 기본 데이터를 복사하고(축 인덱스는 불변이므로 복사하지 않음) 새 객체를 반환합니다. 객체를 복사할 필요가 거의 없다는 점에 유의하세요. 예를 들어, DataFrame을 제자리에서 변경하는 방법은 몇 가지밖에 없습니다:

- 열 삽입, 삭제 또는 수정.
    
- index 또는 columns 속성에 할당.
    
- 동종 데이터의 경우, values 속성이나 고급 인덱싱을 통해 값을 직접 수정.
    

명확히 말하면, pandas 메서드는 데이터를 수정하는 부작용이 없습니다. 거의 모든 메서드가 새 객체를 반환하며 원본 객체는 그대로 둡니다. 데이터가 수정된다면 그것은 당신이 명시적으로 그렇게 했기 때문입니다.

## dtypes

대부분의 경우 pandas는 Series나 DataFrame의 개별 열에 NumPy 배열과 dtypes를 사용합니다. NumPy는 float, int, bool, timedelta64[ns], datetime64[ns]를 지원합니다(NumPy는 시간대를 인식하는 날짜시간을 지원하지 않음에 유의).

pandas와 서드파티 라이브러리는 몇 군데에서 NumPy의 타입 시스템을 확장합니다. 이 섹션에서는 pandas가 내부적으로 만든 확장에 대해 설명합니다. pandas와 작동하는 자체 확장을 작성하는 방법은 [확장 타입](https://pandas.pydata.org/docs/development/extending.html#extending-extension-types)을 참조하세요. 확장을 구현한 서드파티 라이브러리 목록은 [생태계 페이지](https://pandas.pydata.org/community/ecosystem.html)를 참조하세요.

다음 표는 모든 pandas 확장 타입을 나열합니다. dtype 인수가 필요한 메서드의 경우 표시된 대로 문자열을 지정할 수 있습니다. 각 타입에 대한 자세한 내용은 해당 문서 섹션을 참조하세요.

| Kind of Data                                                                                        | Data Type                                                                                                                                         |     | Scalar                                                                                                                |     | Array                                                                                                                                                                        | String Aliases                                                                                                                 |
| --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --------------------------------------------------------------------------------------------------------------------- | --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [tz-aware datetime](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-timezone)  | [`DatetimeTZDtype`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeTZDtype.html#pandas.DatetimeTZDtype "pandas.DatetimeTZDtype")     |     | [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp") |     | [`arrays.DatetimeArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.DatetimeArray.html#pandas.arrays.DatetimeArray "pandas.arrays.DatetimeArray")            | `'datetime64[ns, <tz>]'`                                                                                                       |
| [Categorical](https://pandas.pydata.org/docs/user_guide/categorical.html#categorical)               | [`CategoricalDtype`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.html#pandas.CategoricalDtype "pandas.CategoricalDtype") |     | (none)                                                                                                                |     | [`Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")                                                | `'category'`                                                                                                                   |
| [period (time spans)](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-periods) | [`PeriodDtype`](https://pandas.pydata.org/docs/reference/api/pandas.PeriodDtype.html#pandas.PeriodDtype "pandas.PeriodDtype")                     |     | [`Period`](https://pandas.pydata.org/docs/reference/api/pandas.Period.html#pandas.Period "pandas.Period")             |     | [`arrays.PeriodArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.PeriodArray.html#pandas.arrays.PeriodArray "pandas.arrays.PeriodArray") `'Period[<freq>]'` | `'period[<freq>]'`,                                                                                                            |
| [sparse](https://pandas.pydata.org/docs/user_guide/sparse.html#sparse)                              | [`SparseDtype`](https://pandas.pydata.org/docs/reference/api/pandas.SparseDtype.html#pandas.SparseDtype "pandas.SparseDtype")                     |     | (none)                                                                                                                |     | [`arrays.SparseArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.SparseArray.html#pandas.arrays.SparseArray "pandas.arrays.SparseArray")                    | `'Sparse'`, `'Sparse[int]'`, `'Sparse[float]'`                                                                                 |
| [intervals](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced-intervalindex)         | [`IntervalDtype`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalDtype.html#pandas.IntervalDtype "pandas.IntervalDtype")             |     | [`Interval`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.html#pandas.Interval "pandas.Interval")     |     | [`arrays.IntervalArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntervalArray.html#pandas.arrays.IntervalArray "pandas.arrays.IntervalArray")            | `'interval'`, `'Interval'`, `'Interval[<numpy_dtype>]'`, `'Interval[datetime64[ns, <tz>]]'`, `'Interval[timedelta64[<freq>]]'` |
| [nullable integer](https://pandas.pydata.org/docs/user_guide/integer_na.html#integer-na)            | [`Int64Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Int64Dtype.html#pandas.Int64Dtype "pandas.Int64Dtype"), …                      |     | (none)                                                                                                                |     | [`arrays.IntegerArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.IntegerArray.html#pandas.arrays.IntegerArray "pandas.arrays.IntegerArray")                | `'Int8'`, `'Int16'`, `'Int32'`, `'Int64'`, `'UInt8'`, `'UInt16'`, `'UInt32'`, `'UInt64'`                                       |
| [nullable float](https://pandas.pydata.org/docs/reference/arrays.html#api-arrays-float-na)          | [`Float64Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Float64Dtype.html#pandas.Float64Dtype "pandas.Float64Dtype"), …              |     | (none)                                                                                                                |     | [`arrays.FloatingArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.FloatingArray.html#pandas.arrays.FloatingArray "pandas.arrays.FloatingArray")            | `'Float32'`, `'Float64'`                                                                                                       |
| [Strings](https://pandas.pydata.org/docs/user_guide/text.html#text)                                 | [`StringDtype`](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.html#pandas.StringDtype "pandas.StringDtype")                     |     | [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.12)")                                      |     | [`arrays.StringArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.StringArray.html#pandas.arrays.StringArray "pandas.arrays.StringArray")                    | `'string'`                                                                                                                     |
| [Boolean (with NA)](https://pandas.pydata.org/docs/reference/arrays.html#api-arrays-bool)           | [`BooleanDtype`](https://pandas.pydata.org/docs/reference/api/pandas.BooleanDtype.html#pandas.BooleanDtype "pandas.BooleanDtype")                 |     | [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.12)")                                   |     | [`arrays.BooleanArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.BooleanArray.html#pandas.arrays.BooleanArray "pandas.arrays.BooleanArray")                | `'boolean'`                                                                                                                    |

pandas에는 문자열을 저장하는 두 가지 방법이 있습니다.

1. 문자열을 포함한 모든 Python 객체를 보유할 수 있는 object dtype.
    
2. 문자열 전용인 [StringDtype](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.html#pandas.StringDtype).
    

일반적으로 [StringDtype](https://pandas.pydata.org/docs/reference/api/pandas.StringDtype.html#pandas.StringDtype)을 사용하는 것이 좋습니다. 자세한 내용은 [텍스트 데이터 타입](https://pandas.pydata.org/docs/user_guide/text.html#text-types)을 참조하세요.

마지막으로, 임의의 객체는 object dtype을 사용하여 저장할 수 있지만 가능한 한 피해야 합니다(성능 및 다른 라이브러리와 메서드와의 상호 운용성을 위해. [객체 변환](https://pandas.pydata.org/docs/user_guide/basics.html#basics-object-conversion) 참조).

DataFrame의 편리한 [dtypes](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html#pandas.DataFrame.dtypes) 속성은 각 열의 데이터 타입이 있는 Series를 반환합니다.

```python
dft = pd.DataFrame(
   {
       "A": np.random.rand(3),
       "B": 1,
       "C": "foo",
       "D": pd.Timestamp("20010102"),
       "E": pd.Series([1.0] * 3).astype("float32"),
       "F": False,
       "G": pd.Series([1] * 3, dtype="int8"),
   }
)

dft
```
```
          A  B    C          D    E      F  G
0  0.035962  1  foo 2001-01-02  1.0  False  1
1  0.701379  1  foo 2001-01-02  1.0  False  1
2  0.281885  1  foo 2001-01-02  1.0  False  1
```

```python
dft.dtypes
```
```
A          float64
B            int64
C           object
D    datetime64[s]
E          float32
F             bool
G             int8
dtype: object
```

Series 객체에서는 [dtype](https://pandas.pydata.org/docs/reference/api/pandas.Series.dtype.html#pandas.Series.dtype) 속성을 사용하세요.

```python
dft["A"].dtype
```
```
dtype('float64')
```

pandas 객체가 단일 열에 여러 dtypes의 데이터를 포함하는 경우, 해당 열의 dtype은 모든 데이터 타입을 수용하도록 선택됩니다(object가 가장 일반적임).

```python
# 이 정수들은 float으로 강제 변환됩니다
pd.Series([1, 2, 3, 4, 5, 6.0])
```
```
0    1.0
1    2.0
2    3.0
3    4.0
4    5.0
5    6.0
dtype: float64
```

```python
# 문자열 데이터는 object dtype을 강제합니다
pd.Series([1, 2, 3, 6.0, "foo"])
```
```
0      1
1      2
2      3
3    6.0
4    foo
dtype: object
```

DataFrame에서 각 타입의 열 수는 DataFrame.dtypes.value_counts()를 호출하여 찾을 수 있습니다.

```python
dft.dtypes.value_counts()
```
```
float64          1
int64            1
object           1
datetime64[s]    1
float32          1
bool             1
int8             1
Name: count, dtype: int64
```

숫자 dtypes는 전파되며 DataFrame에서 공존할 수 있습니다. dtype이 전달되면(dtype 키워드를 통해 직접 전달되거나, 전달된 ndarray 또는 전달된 Series를 통해) DataFrame 연산에서 보존됩니다. 또한 서로 다른 숫자 dtypes는 결합되지 않습니다. 다음 예제를 통해 이를 이해할 수 있습니다.

```python
df1 = pd.DataFrame(np.random.randn(8, 1), columns=["A"], dtype="float32")

df1
```
```
          A
0  0.224364
1  1.890546
2  0.182879
3  0.787847
4 -0.188449
5  0.667715
6 -0.011736
7 -0.399073
```

```python
df1.dtypes
```
```
A    float32
dtype: object
```

```python
df2 = pd.DataFrame(
   {
       "A": pd.Series(np.random.randn(8), dtype="float16"),
       "B": pd.Series(np.random.randn(8)),
       "C": pd.Series(np.random.randint(0, 255, size=8), dtype="uint8"),  # [0,255] (uint8의 범위)
   }
)

df2
```
```
          A         B    C
0  0.823242  0.256090   26
1  1.607422  1.426469   86
2 -0.333740 -0.416203   46
3 -0.063477  1.139976  212
4 -1.014648 -1.193477   26
5  0.678711  0.096706    7
6 -0.040863 -1.956850  184
7 -0.357422 -0.714337  206
```

```python
df2.dtypes
```
```
A    float16
B    float64
C      uint8
dtype: object
```

### 기본값 (defaults)

플랫폼(32비트 또는 64비트)에 관계없이 기본적으로 정수 유형은 `int64`이고 부동 소수점 유형은 `float64`입니다. 다음은 모두 `int64` dtype을 결과로 가집니다.

```python
In [359]: pd.DataFrame([1, 2], columns=["a"]).dtypes
Out[359]: 
a    int64
dtype: object

In [360]: pd.DataFrame({"a": [1, 2]}).dtypes
Out[360]: 
a    int64
dtype: object

In [361]: pd.DataFrame({"a": 1}, index=list(range(2))).dtypes
Out[361]: 
a    int64
dtype: object
```

Numpy는 배열을 생성할 때 플랫폼 의존적인 유형을 선택합니다. 다음은 32비트 플랫폼에서 `int32`를 결과로 가질 것입니다.

```python
In [362]: frame = pd.DataFrame(np.array([1, 2]))
```

### 업캐스팅 (upcasting)

다른 유형과 결합될 때 유형이 잠재적으로 업캐스트될 수 있습니다. 이는 현재 유형에서 승격됨을 의미합니다(예: `int`에서 `float`으로).

```python
In [363]: df3 = df1.reindex_like(df2).fillna(value=0.0) + df2

In [364]: df3
Out[364]: 
          A         B      C
0  1.047606  0.256090   26.0
1  3.497968  1.426469   86.0
2 -0.150862 -0.416203   46.0
3  0.724370  1.139976  212.0
4 -1.203098 -1.193477   26.0
5  1.346426  0.096706    7.0
6 -0.052599 -1.956850  184.0
7 -0.756495 -0.714337  206.0

In [365]: df3.dtypes
Out[365]: 
A    float32
B    float64
C    float64
dtype: object
```

[DataFrame.to_numpy()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy)는 dtype의 최소 공통 분모를 반환합니다. 이는 결과적으로 동질적인 dtype을 가진 NumPy 배열에서 모든 유형을 수용할 수 있는 dtype을 의미합니다. 이로 인해 일부 업캐스팅이 강제될 수 있습니다.

```python
In [366]: df3.to_numpy().dtype
Out[366]: dtype('float64')
```

### astype

[astype()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html#pandas.DataFrame.astype) 메서드를 사용하여 dtype을 명시적으로 한 유형에서 다른 유형으로 변환할 수 있습니다. 이는 기본적으로 dtype이 변경되지 않은 경우에도 복사본을 반환합니다(이 동작을 변경하려면 `copy=False`를 전달하세요). 또한 astype 연산이 유효하지 않으면 예외를 발생시킵니다.

업캐스팅은 항상 NumPy 규칙에 따릅니다. 연산에 두 가지 다른 dtype이 관련되어 있다면, 더 일반적인 것이 연산 결과로 사용됩니다.

```python
In [367]: df3
Out[367]: 
          A         B      C
0  1.047606  0.256090   26.0
1  3.497968  1.426469   86.0
2 -0.150862 -0.416203   46.0
3  0.724370  1.139976  212.0
4 -1.203098 -1.193477   26.0
5  1.346426  0.096706    7.0
6 -0.052599 -1.956850  184.0
7 -0.756495 -0.714337  206.0

In [368]: df3.dtypes
Out[368]: 
A    float32
B    float64
C    float64
dtype: object

# dtype 변환
In [369]: df3.astype("float32").dtypes
Out[369]: 
A    float32
B    float32
C    float32
dtype: object
```

[astype()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html#pandas.DataFrame.astype)을 사용하여 열의 하위 집합을 지정된 유형으로 변환합니다.

```python
In [370]: dft = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})

In [371]: dft[["a", "b"]] = dft[["a", "b"]].astype(np.uint8)

In [372]: dft
Out[372]: 
   a  b  c
0  1  4  7
1  2  5  8
2  3  6  9

In [373]: dft.dtypes
Out[373]: 
a    uint8
b    uint8
c    int64
dtype: object
```

[astype()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html#pandas.DataFrame.astype)에 dict를 전달하여 특정 열을 특정 dtype으로 변환합니다.

```python
In [374]: dft1 = pd.DataFrame({"a": [1, 0, 1], "b": [4, 5, 6], "c": [7, 8, 9]})

In [375]: dft1 = dft1.astype({"a": np.bool_, "c": np.float64})

In [376]: dft1
Out[376]: 
       a  b    c
0   True  4  7.0
1  False  5  8.0
2   True  6  9.0

In [377]: dft1.dtypes
Out[377]: 
a       bool
b      int64
c    float64
dtype: object
```


> [!NOTE]
> [astype()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html#pandas.DataFrame.astype)과 [loc()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc)을 사용하여 열의 하위 집합을 지정된 유형으로 변환하려고 할 때 업캐스팅이 발생합니다.
> 
> [loc()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc)은 현재 dtype에 맞추려고 시도하는 반면, `[]`는 오른쪽 dtype을 사용하여 덮어씁니다. 따라서 다음 코드는 의도하지 않은 결과를 생성합니다.
> 
> ```python
> In [378]: dft = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
> 
> In [379]: dft.loc[:, ["a", "b"]].astype(np.uint8).dtypes
> Out[379]: 
> a    uint8
> b    uint8
> dtype: object
> 
> In [380]: dft.loc[:, ["a", "b"]] = dft.loc[:, ["a", "b"]].astype(np.uint8)
> 
> In [381]: dft.dtypes
> Out[381]: 
> a    int64
> b    int64
> c    int64
> dtype: object
> ```

### 객체 변환 (object conversion)

pandas는 `object` dtype에서 다른 유형으로 강제 변환을 시도하는 다양한 함수를 제공합니다. 데이터가 이미 올바른 유형이지만 `object` 배열에 저장된 경우, [DataFrame.infer_objects()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.infer_objects.html#pandas.DataFrame.infer_objects) 및 [Series.infer_objects()](https://pandas.pydata.org/docs/reference/api/pandas.Series.infer_objects.html#pandas.Series.infer_objects) 메서드를 사용하여 올바른 유형으로 소프트 변환할 수 있습니다.

```python
import datetime

df = pd.DataFrame(
   [
       [1, 2],
       ["a", "b"],
       [datetime.datetime(2016, 3, 2), datetime.datetime(2016, 3, 2)],
   ]
)

df = df.T

df
Out[385]: 
   0  1                    2
0  1  a  2016-03-02 00:00:00
1  2  b  2016-03-02 00:00:00

df.dtypes
Out[386]: 
0    object
1    object
2    object
dtype: object
```

데이터가 전치되었기 때문에 원래의 추론은 모든 열을 객체로 저장했으며, `infer_objects`가 이를 수정할 것입니다.

```python
df.infer_objects().dtypes
Out[387]: 
0             int64
1            object
2    datetime64[ns]
dtype: object
```

다음 함수들은 1차원 객체 배열이나 스칼라에 대해 객체를 지정된 유형으로 강제 변환하는 데 사용할 수 있습니다:

- [to_numeric()](https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html#pandas.to_numeric) (숫자 dtype으로 변환)
    
```python
m = ["1.1", 2, 3]

pd.to_numeric(m)
Out[389]: array([1.1, 2. , 3. ])
```
    
- [to_datetime()](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime) (datetime 객체로 변환)
    
```python
import datetime

m = ["2016-07-09", datetime.datetime(2016, 3, 2)]

pd.to_datetime(m)
Out[392]: DatetimeIndex(['2016-07-09', '2016-03-02'], dtype='datetime64[ns]', freq=None)
```
    
- [to_timedelta()](https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html#pandas.to_timedelta) (timedelta 객체로 변환)
    
```python
m = ["5us", pd.Timedelta("1day")]

pd.to_timedelta(m)
Out[394]: TimedeltaIndex(['0 days 00:00:00.000005', '1 days 00:00:00'], dtype='timedelta64[ns]', freq=None)
```

강제 변환을 수행하기 위해 `errors` 인수를 전달할 수 있습니다. 이는 pandas가 원하는 dtype이나 객체로 변환할 수 없는 요소를 어떻게 처리해야 하는지 지정합니다. 기본적으로 `errors='raise'`이며, 이는 변환 과정에서 발생하는 모든 오류가 발생할 것임을 의미합니다. 그러나 `errors='coerce'`인 경우, 이러한 오류는 무시되고 pandas는 문제가 있는 요소를 `pd.NaT` (datetime 및 timedelta의 경우) 또는 `np.nan` (숫자의 경우)로 변환합니다. 이는 주로 원하는 dtype(예: 숫자, datetime)이지만 가끔 누락된 것으로 표현하고 싶은 비준수 요소가 섞여 있는 데이터를 읽을 때 유용할 수 있습니다:

```python
import datetime

m = ["apple", datetime.datetime(2016, 3, 2)]

pd.to_datetime(m, errors="coerce")
Out[397]: DatetimeIndex(['NaT', '2016-03-02'], dtype='datetime64[ns]', freq=None)

m = ["apple", 2, 3]

pd.to_numeric(m, errors="coerce")
Out[399]: array([nan,  2.,  3.])

m = ["apple", pd.Timedelta("1day")]

pd.to_timedelta(m, errors="coerce")
Out[401]: TimedeltaIndex([NaT, '1 days'], dtype='timedelta64[ns]', freq=None)
```

객체 변환 외에도 [to_numeric()](https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html#pandas.to_numeric)은 `downcast`라는 또 다른 인수를 제공하여 새로 (또는 이미) 숫자 데이터를 더 작은 dtype으로 다운캐스트하는 옵션을 제공하며, 이는 메모리를 절약할 수 있습니다:

```python
m = ["1", 2, 3]

pd.to_numeric(m, downcast="integer")  # 가장 작은 부호있는 정수 dtype
Out[403]: array([1, 2, 3], dtype=int8)

pd.to_numeric(m, downcast="signed")  # 'integer'와 동일
Out[404]: array([1, 2, 3], dtype=int8)

pd.to_numeric(m, downcast="unsigned")  # 가장 작은 부호없는 정수 dtype
Out[405]: array([1, 2, 3], dtype=uint8)

pd.to_numeric(m, downcast="float")  # 가장 작은 float dtype
Out[406]: array([1., 2., 3.], dtype=float32)
```

이러한 메서드는 1차원 배열, 리스트 또는 스칼라에만 적용되므로 DataFrame과 같은 다차원 객체에 직접 사용할 수 없습니다. 그러나 [apply()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply)를 사용하면 각 열에 효율적으로 함수를 "적용"할 수 있습니다:

```python
import datetime

df = pd.DataFrame([["2016-07-09", datetime.datetime(2016, 3, 2)]] * 2, dtype="O")

df
Out[409]: 
            0                    1
0  2016-07-09  2016-03-02 00:00:00
1  2016-07-09  2016-03-02 00:00:00

df.apply(pd.to_datetime)
Out[410]: 
           0          1
0 2016-07-09 2016-03-02
1 2016-07-09 2016-03-02

df = pd.DataFrame([["1.1", 2, 3]] * 2, dtype="O")

df
Out[412]: 
     0  1  2
0  1.1  2  3
1  1.1  2  3

df.apply(pd.to_numeric)
Out[413]: 
     0  1  2
0  1.1  2  3
1  1.1  2  3

df = pd.DataFrame([["5us", pd.Timedelta("1day")]] * 2, dtype="O")

df
Out[415]: 
     0                1
0  5us  1 days 00:00:00
1  5us  1 days 00:00:00

df.apply(pd.to_timedelta)
Out[416]: 
                       0      1
0 0 days 00:00:00.000005 1 days
1 0 days 00:00:00.000005 1 days
```

### 주의사항 (gotchas)

정수 유형 데이터에 대해 선택 작업을 수행하면 데이터를 쉽게 부동 소수점으로 변환할 수 있습니다. `nans`가 도입되지 않는 경우 입력 데이터의 dtype이 보존됩니다. [정수 NA 지원](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-intna)도 참조하세요.

```python
dfi = df3.astype("int32")

dfi["E"] = 1

dfi
Out[419]: 
   A  B    C  E
0  1  0   26  1
1  3  1   86  1
2  0  0   46  1
3  0  1  212  1
4 -1 -1   26  1
5  1  0    7  1
6  0 -1  184  1
7  0  0  206  1

dfi.dtypes
Out[420]: 
A    int32
B    int32
C    int32
E    int64
dtype: object

casted = dfi[dfi > 0]

casted
Out[422]: 
     A    B    C  E
0  1.0  NaN   26  1
1  3.0  1.0   86  1
2  NaN  NaN   46  1
3  NaN  1.0  212  1
4  NaN  NaN   26  1
5  1.0  NaN    7  1
6  NaN  NaN  184  1
7  NaN  NaN  206  1

casted.dtypes
Out[423]: 
A    float64
B    float64
C      int32
E      int64
dtype: object
```

float dtype은 변경되지 않습니다.

```python
dfa = df3.copy()

dfa["A"] = dfa["A"].astype("float32")

dfa.dtypes
Out[426]: 
A    float32
B    float64
C    float64
dtype: object

casted = dfa[df2 > 0]

casted
Out[428]: 
          A         B      C
0  1.047606  0.256090   26.0
1  3.497968  1.426469   86.0
2       NaN       NaN   46.0
3       NaN  1.139976  212.0
4       NaN       NaN   26.0
5  1.346426  0.096706    7.0
6       NaN       NaN  184.0
7       NaN       NaN  206.0

casted.dtypes
Out[429]: 
A    float32
B    float64
C    float64
dtype: object
```

## dtype에 기반한 열 선택 (Selecting columns based on dtype)

[`select_dtypes()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html#pandas.DataFrame.select_dtypes) 메서드는 dtype에 기반하여 열을 선택하는 기능을 구현합니다.

먼저, 다양한 dtype을 가진 [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame)을 생성해 보겠습니다:

```python
df = pd.DataFrame(
   {
       "string": list("abc"),
       "int64": list(range(1, 4)),
       "uint8": np.arange(3, 6).astype("u1"),
       "float64": np.arange(4.0, 7.0),
       "bool1": [True, False, True],
       "bool2": [False, True, False],
       "dates": pd.date_range("now", periods=3),
       "category": pd.Series(list("ABC")).astype("category"),
   }
)

df["tdeltas"] = df.dates.diff()

df["uint64"] = np.arange(3, 6).astype("u8")

df["other_dates"] = pd.date_range("20130101", periods=3)

df["tz_aware_dates"] = pd.date_range("20130101", periods=3, tz="US/Eastern")

df
```

그리고 dtypes:

```python
df.dtypes
```

[`select_dtypes()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html#pandas.DataFrame.select_dtypes)에는 include와 exclude라는 두 개의 매개변수가 있어 "이 dtype을 가진 열을 주세요" (include) 그리고/또는 "이 dtype을 가지지 않은 열을 주세요" (exclude)라고 지정할 수 있습니다.

예를 들어, bool 열을 선택하려면:

```python
df.select_dtypes(include=[bool])
```

[NumPy dtype 계층](https://numpy.org/doc/stable/reference/arrays.scalars.html)에 있는 dtype의 이름을 전달할 수도 있습니다:

```python
df.select_dtypes(include=["bool"])
```

[`select_dtypes()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html#pandas.DataFrame.select_dtypes)는 일반적인 dtype에도 작동합니다.

예를 들어, 부호 없는 정수를 제외한 모든 숫자와 불리언 열을 선택하려면:

```python
df.select_dtypes(include=["number", "bool"], exclude=["unsignedinteger"])
```

문자열 열을 선택하려면 object dtype을 사용해야 합니다:

```python
df.select_dtypes(include=["object"])
```

numpy.number와 같은 일반적인 dtype의 모든 하위 dtype을 보려면 하위 dtype의 트리를 반환하는 함수를 정의할 수 있습니다:

```python
def subdtypes(dtype):
   subs = dtype.__subclasses__()
   if not subs:
       return dtype
   return [dtype, [subdtypes(dt) for dt in subs]]
```

모든 NumPy dtype은 numpy.generic의 하위 클래스입니다:

```python
subdtypes(np.generic)
```

> pandas는 또한 category와 datetime64[ns, tz] 타입을 정의하는데, 이들은 일반적인 NumPy 계층에 통합되지 않아 위의 함수로는 나타나지 않습니다.

---
## 참조

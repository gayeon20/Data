---
title: "[Pandas] 문법 (Pandas Grammer)"
excerpt: 에 대한 문서
categories:
  - Pandas
tags:
  - Pandas
  - Series
  - DataFrame
last_modified_at: 2024-03-01T00:00:00-00:00
link: https://pandas.pydata.org/docs/user_guide/index.html
상위 항목: "[[pandas_home|판다스 (Pandas)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

**하위 항목**
- [[pandas_data_structures|판다스 데이터 구조 (Pandas Data Structures)]]
- [[pandas_data_handling|판다스 데이터 다루기 (Pandas Data Handling)]]
- [[pandas_pyarrow|판다스 파이에로우 (Pandas Pyarrow)]]
- [[pandas_io_tools|판다스 입출력 도구 (Pandas I/O Tools)]]

---

- 일반적으로 다음과 같이 임포트합니다:

```python
In [1]: import numpy as np
In [2]: import pandas as pd
```

## 기본 데이터 구조 (Basic data structures) [[pandas_data_structures|(자세히 보기)]]
- Pandas는 데이터를 처리하기 위한 두 가지 유형의 클래스를 제공합니다:
1. [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series"): 모든 유형의 데이터를 포함하는 1차원 레이블이 지정된 배열로
    정수, 문자열, 파이썬 객체 등 모든 유형의 데이터를 저장하는 1차원 레이블 배열입니다.
2. [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame"): 2차원 배열이나 행과 열이 있는 테이블처럼 데이터를 보관하는 2차원 데이터 구조입니다. Index는 오직 식별용으로 사용되며 연산에서 제외됩니다.

> [!NOTE] 인덱스 (Index)
> - Index 객체는 RDBMS의 PK(Primary Key)와 유사하게 레코드를 고유하게 식별하는 객체입니다. (별도의 컬럼값이 아닙니다.)
> - 오직 식별용으로만 사용되며, Series 객체에 연산 함수를 적용할 때 Index는 연산에서 제외됩니다.
> - Index만 추출하려면 `.index` 속성으로 접근해야 합니다.
> - 고유한 값만 유지한다면 숫자형이 아닌 문자형/Datetime도 가능합니다.
> - `Series`나 `DataFrame`의 `reset_index()` 메소드를 실행하면 인덱스를 새로 할당하며 기존 인덱스는 'index'라는 컬럼 명으로 새로 추가합니다. 단, `drop` 옵션을 `True`로 설정하면 기존 인덱스를 제거합니다.

### 객체 생성 (Object creation)
- 값 목록을 전달하여 [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")를 생성하고, 팬더가 기본 [`RangeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas.RangeIndex "pandas.RangeIndex")를 생성하도록 합니다.

```python
In [3]: s = pd.Series([1, 3, 5, np.nan, 6, 8])

In [4]: s
Out[4]: 
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
```

- [`date_range()`](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html#pandas.date_range "pandas.date_range")와 레이블이 지정된 열을 사용하여 날짜/시간 인덱스가 있는 NumPy 배열을 전달하여 [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")을 생성합니다:

```python
In [5]: dates = pd.date_range("20130101", periods=6)

In [6]: dates
Out[6]: 
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')

In [7]: df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

In [8]: df
Out[8]: 
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
```

- 키는 열 레이블이고 값은 열 값인 객체 사전을 전달하여 [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")을 생성합니다.

```python
In [9]: df2 = pd.DataFrame(
   …:    {
   …:        "A": 1.0,
   …:        "B": pd.Timestamp("20130102"),
   …:        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
   …:        "D": np.array([3] * 4, dtype="int32"),
   …:        "E": pd.Categorical(["test", "train", "test", "train"]),
   …:        "F": "foo",
   …:    }
   …: )
   …: 

In [10]: df2
Out[10]: 
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
```

- 결과 [`데이터프레임`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")의 열은 서로 다른 [dtypes](https://pandas.pydata.org/docs/user_guide/basics.html#basics-dtypes)를 갖습니다:

```python
In [11]: df2.dtypes
Out[11]: 
A          float64
B    datetime64[s]
C          float32
D            int32
E         category
F           object
dtype: object
```

- `DataFrame`의 특정 인덱스에 하나의 상수를 할당할 경우 모든 값이 할당한 상수를 갖습니다.

```python
import pandas as pd
import numpy as np

# 샘플 DataFrame 생성
>> df = pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])

>> df
# 원본 DataFrame:
          A         B         C
0  0.184988  0.580878  0.447348
1  0.203696  0.279242  0.465739
2  0.862412  0.979321  0.111583
3  0.842537  0.163121  0.104425
4  0.181041  0.428130  0.583490

# 인덱스 2에 상수 100 할당
>> df.loc[2] = 100
df
# 상수 할당 후 DataFrame:
            A           B           C
0    0.184988    0.580878    0.447348
1    0.203696    0.279242    0.465739
2  100.000000  100.000000  100.000000
3    0.842537    0.163121    0.104425
4    0.181041    0.428130    0.583490
```


- IPython을 사용하는 경우 열 이름(및 공개 속성)에 대한 탭 완성 기능이 자동으로 활성화됩니다. 다음은 완성되는 속성의 하위 집합입니다:

```python
In [12]: df2.<TAB>  # noqa: E225, E999
df2.A                  df2.bool
df2.abs                df2.boxplot
df2.add                df2.C
df2.add_prefix         df2.clip
df2.add_suffix         df2.columns
df2.align              df2.copy
df2.all                df2.count
df2.any                df2.combine
df2.append             df2.D
df2.apply              df2.describe
df2.applymap           df2.diff
df2.B                  df2.duplicated
```

- 보시다시피 `A`, `B`, `C`, `D` 열은 자동으로 탭이 완성됩니다. `E` 및 `F`도 있으며, 나머지 속성은 간결성을 위해 잘라냈습니다.

> [!NOTE] `DataFrame`과 리스트, 딕셔너리, 넘파이 `ndarray` 상호 변환
> | 변환 형태                          | 설명                                                                                                                                              |
> | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
> | 리스트(list)를 `DataFrame`으로 변환    | `df_list1 = pd.DataFrame(list, columns=col_name1)`와 같이 `DataFrame`생성 인자로 리스트 객체와 매핑되는 컬럼명들을 입력                                                  |
> | `ndarray`를 `DataFrame`으로 변환    | `df_array2 = pd.DataFrame(array2, columns=col_name2)`와 같이 `DataFrame` 생성 인자로 `ndarray`와 매핑되는 컬럼명들을 입력                                           |
> | 딕셔너리(dict)를 (`DataFrame`)으로 변환 | `dict = {'col1':[1, 11], 'col2': [2, 22], 'col3': [3, 33]}`<br>`df_dict = pd.DataFrame(dict)`<br>와 같이 딕셔너리의 키(Key)로 컬럼명을, 값(Value)을 리스트 형식으로 입력 |
> | `DataFrame`을 `ndarray`로 변환     | `DataFrame` 객체의 `values` 속성을 이용하여 `ndarray` 변환                                                                                                  |
> | `DataFrame`을 리스트로 변환           | `DataFrame` 객체의 `values` 속성을 이용하여 먼저 `ndarray`로 변환 후 `tolist()`를 이용하여 `list`로 변환                                                                |
> | `DataFrame`을 딕셔너리로 변환          | `DataFrame` 객체의 `to_dict()`를 이용하여 변환                                                                                                            |
> 

## ==데이터 보기 (Viewing data)== [[pandas_data_handling|(자세히 보기)]]

- [필수 기본 기능 섹션](https://pandas.pydata.org/docs/user_guide/basics.html#basics)을 참조하세요.
- 데이터 프레임의 상단과 하단 행을 각각 보려면 [`DataFrame.head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html#pandas.DataFrame.head "pandas.DataFrame.head") 및 [`DataFrame.tail()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html#pandas.DataFrame.tail "pandas.DataFrame.tail")을 사용합니다:

```python
In [13]: df.head()
Out[13]: 
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401

In [14]: df.tail(3)
Out[14]: 
                   A         B         C         D
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
```

- [`DataFrame.index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html#pandas.DataFrame.index "pandas.DataFrame.index") 또는 [`DataFrame.columns`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html#pandas.DataFrame.columns "pandas.DataFrame.columns")을 표시합니다:

```python
In [15]: df.index
Out[15]: 
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')

In [16]: df.columns
Out[16]: Index(['A', 'B', 'C', 'D'], dtype='object')
```

- `DataFrame.index.values` 명령어는 인덱스 값을 `ndarray`로 반환합니다.
- 인덱스나 열 레이블 없이 [`DataFrame.to_numpy()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy "pandas.DataFrame.to_numpy")를 사용하여 기초 데이터의 NumPy 표현을 반환합니다:

```python
In [17]: df.to_numpy()
Out[17]: 
array([[ 0.4691, -0.2829, -1.5091, -1.1356],
       [ 1.2121, -0.1732,  0.1192, -1.0442],
       [-0.8618, -2.1046, -0.4949,  1.0718],
       [ 0.7216, -0.7068, -1.0396,  0.2719],
       [-0.425 ,  0.567 ,  0.2762, -1.0874],
       [-0.6737,  0.1136, -1.4784,  0.525 ]])
```


> [!NOTE]
> - **NumPy 배열에는 전체 배열에 대해 하나의 dtype이 있는 반면, Pandas 데이터 프레임에는 열당 하나의 dtype이 있습니다**. `DataFrame.to_numpy()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy "pandas.DataFrame.to_numpy")를 호출하면 Pandas는 데이터 프레임의 _모든_ dtypes를 담을 수 있는 NumPy dtype을 찾습니다. 공통 데이터 유형이 `object`인 경우, [`DataFrame.to_numpy()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy "pandas.DataFrame.to_numpy")는 데이터를 복사해야 합니다.
> 
> ```python
> In [18]: df2.dtypes
> Out[18]: 
> A          float64
> B    datetime64[s]
> C          float32
> D            int32
> E         category
> F           object
> dtype: object
> 
> In [19]: df2.to_numpy()
> Out[19]: 
> array([[1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
>        [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo'],
>        [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
>        [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo']],
>       dtype=object)
> ```

- [`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe "pandas.DataFrame.describe")는 데이터에 대한 빠른 통계 요약을 보여줍니다. 평균, 표준편차, 4분위 분포도를 제공합니다. 숫자형 컬럼들에 대해 해당 정보를 제공합니다:

```python
In [20]: df.describe()
Out[20]: 
              A         B         C         D
count  6.000000  6.000000  6.000000  6.000000
mean   0.073711 -0.431125 -0.687758 -0.233103
std    0.843157  0.922818  0.779887  0.973118
min   -0.861849 -2.104569 -1.509059 -1.135632
25%   -0.611510 -0.600794 -1.368714 -1.076610
50%    0.022070 -0.228039 -0.767252 -0.386188
75%    0.658444  0.041933 -0.034326  0.461706
max    1.212112  0.567020  0.276232  1.071804
```

- 데이터 전치: `T`

```python
In [21]: df.T
Out[21]: 
   2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
A    0.469112    1.212112   -0.861849    0.721555   -0.424972   -0.673690
B   -0.282863   -0.173215   -2.104569   -0.706771    0.567020    0.113648
C   -1.509059    0.119209   -0.494929   -1.039575    0.276232   -1.478427
D   -1.135632   -1.044236    1.071804    0.271860   -1.087401    0.524988
```

- [`DataFrame.sort_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html#pandas.DataFrame.sort_index "pandas.DataFrame.sort_index")는 축을 기준으로 정렬합니다:

```python
In [22]: df.sort_index(axis=1, ascending=False)
Out[22]: 
                   D         C         B         A
2013-01-01 -1.135632 -1.509059 -0.282863  0.469112
2013-01-02 -1.044236  0.119209 -0.173215  1.212112
2013-01-03  1.071804 -0.494929 -2.104569 -0.861849
2013-01-04  0.271860 -1.039575 -0.706771  0.721555
2013-01-05 -1.087401  0.276232  0.567020 -0.424972
2013-01-06  0.524988 -1.478427  0.113648 -0.673690
```

- [`DataFrame.sort_values()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values "pandas.DataFrame.sort_values")는 값을 기준으로 정렬합니다:

```python
In [23]: df.sort_values(by="B")
Out[23]: 
                   A         B         C         D
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
```

- `DataFrame.info()` 명령어는 컬럼명, 데이터 타입, Null 건수, 데이터 건수 정보를 제공합니다.
- `pd.set_option` 명령어로 데이터 조회 옵션을 설정할 수 있습니다.

| 옵션                                         | 의미             |
| ------------------------------------------ | -------------- |
| `pd.set_option('display.max_rows', n)`     | 최대 n개의 row만 조회 |
| `pd.set_option('display.max_colwidth', n)` | 각 열의 최대 넓이 설정  |
| `pd.set_option('display.max_columns', n)`  | 최대 n개의 열만 조회   |

## 선택 (Selection)

> [!NOTE]
> - 선택 및 설정을 위한 표준 Python/NumPy 표현식은 직관적이고 대화형 작업에 유용하지만, 프로덕션 코드의 경우 최적화된 pandas 데이터 액세스 메서드인 [`DataFrame.at()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at.html#pandas.DataFrame.at "pandas.DataFrame.at"), [`DataFrame.iat()`](https://pandas.pydata. org/docs/reference/api/pandas.DataFrame.iat.html#pandas.DataFrame.iat"), [`DataFrame.loc()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc "pandas.DataFrame.loc") 및 [`DataFrame.iloc()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc "pandas.DataFrame.iloc") 입니다.

- 인덱싱 문서 [데이터 인덱싱 및 선택](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing) 및 [멀티 인덱스/고급 인덱싱](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced)을 참조하세요.

### 인덱싱 (Indexing)

- [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")의 경우 단일 레이블을 전달하면 열이 선택되고 `df.A`에 해당하는 [`시리즈`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")가 생성됩니다:

```python
In [24]: df["A"]
Out[24]: 
2013-01-01    0.469112
2013-01-02    1.212112
2013-01-03   -0.861849
2013-01-04    0.721555
2013-01-05   -0.424972
2013-01-06   -0.673690
Freq: D, Name: A, dtype: float64
```

[`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")의 경우, 슬라이스 `:`를 전달하면 일치하는 행이 선택됩니다:

```python
In [25]: df[0:3]
Out[25]: 
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804

In [26]: df["20130102":"20130104"]
Out[26]: 
                   A         B         C         D
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
```

### 레이블로 선택 (Selection by label)

- [레이블별 선택](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-label)에서 [`DataFrame.loc()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc "pandas.DataFrame.loc") 또는 [`DataFrame.at()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at.html#pandas.DataFrame.at "pandas.DataFrame.at")을 사용하여 자세한 내용을 참조하세요.
- 레이블과 일치하는 행을 선택합니다:

```python
In [27]: df.loc[dates[0]]
Out[27]: 
A    0.469112
B   -0.282863
C   -1.509059
D   -1.135632
Name: 2013-01-01 00:00:00, dtype: float64
```

- 열 레이블을 선택하여 모든 행(`:`)을 선택합니다:

```python
In [28]: df.loc[:, ["A", "B"]]
Out[28]: 
                   A         B
2013-01-01  0.469112 -0.282863
2013-01-02  1.212112 -0.173215
2013-01-03 -0.861849 -2.104569
2013-01-04  0.721555 -0.706771
2013-01-05 -0.424972  0.567020
2013-01-06 -0.673690  0.113648
```

- 라벨 슬라이싱의 경우 두 엔드포인트가 모두 포함됩니다:

```python
In [29]: df.loc["20130102":"20130104", ["A", "B"]]
Out[29]: 
                   A         B
2013-01-02  1.212112 -0.173215
2013-01-03 -0.861849 -2.104569
2013-01-04  0.721555 -0.706771
```

- 단일 행과 열 레이블을 선택하면 스칼라가 반환됩니다:

```python
In [30]: df.loc[dates[0], "A"]
Out[30]: 0.4691122999071863
```

- 스칼라에 빠르게 액세스하는 경우(이전 방법과 동일):

```python
In [31]: df.at[dates[0], "A"]
Out[31]: 0.4691122999071863
```

### 위치별 선택 (Selection by position)
- [위치별 선택](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-integer)에서 [`DataFrame.iloc()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc "pandas.DataFrame.iloc") 또는 [`DataFrame.iat()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iat.html#pandas.DataFrame.iat "pandas.DataFrame.iat")를 사용하여 자세한 내용을 참조하세요.
- 전달된 정수의 위치를 통해 선택합니다. `DataFrame`의 `index`가 아닌 리스트의 인덱스를 사용합니다.:

```python
In [32]: df.iloc[3]
Out[32]: 
A    0.721555
B   -0.706771
C   -1.039575
D    0.271860
Name: 2013-01-04 00:00:00, dtype: float64
```

- 정수 조각은 NumPy/Python과 유사하게 작동합니다:

```python
In [33]: df.iloc[3:5, 0:2]
Out[33]: 
                   A         B
2013-01-04  0.721555 -0.706771
2013-01-05 -0.424972  0.567020
```

- 정수 위치 목록입니다:

```python
In [34]: df.iloc[[1, 2, 4], [0, 2]]
Out[34]: 
                   A         C
2013-01-02  1.212112  0.119209
2013-01-03 -0.861849 -0.494929
2013-01-05 -0.424972  0.276232
```

- 행을 명시적으로 분할하는 경우:

```python
In [35]: df.iloc[1:3, :]
Out[35]: 
                   A         B         C         D
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
```

- 열을 명시적으로 분할하는 경우:

```python
In [36]: df.iloc[:, 1:3]
Out[36]: 
                   B         C
2013-01-01 -0.282863 -1.509059
2013-01-02 -0.173215  0.119209
2013-01-03 -2.104569 -0.494929
2013-01-04 -0.706771 -1.039575
2013-01-05  0.567020  0.276232
2013-01-06  0.113648 -1.478427
```

- 값을 명시적으로 가져오는 경우:

```python
In [37]: df.iloc[1, 1]
Out[37]: -0.17321464905330858

For getting fast access to a scalar (equivalent to the prior method):

In [38]: df.iat[1, 1]
Out[38]: -0.17321464905330858
```


### 불리언 인덱싱 (Boolean indexing)

- `df.A`가 `0`보다 큰 행을 선택합니다.

```python
In [39]: df[df["A"] > 0]
Out[39]: 
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
```

- 부울 조건이 충족되는 [`데이터프레임`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")에서 값 선택하기:

```python
In [40]: df[df > 0]
Out[40]: 
                   A         B         C         D
2013-01-01  0.469112       NaN       NaN       NaN
2013-01-02  1.212112       NaN  0.119209       NaN
2013-01-03       NaN       NaN       NaN  1.071804
2013-01-04  0.721555       NaN       NaN  0.271860
2013-01-05       NaN  0.567020  0.276232       NaN
2013-01-06       NaN  0.113648       NaN  0.524988
```

- 필터링에 [`isin()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html#pandas.Series.isin "pandas.Series.isin") 메서드 사용:

```python
In [41]: df2 = df.copy()

In [42]: df2["E"] = ["one", "one", "two", "three", "four", "three"]

In [43]: df2
Out[43]: 
                   A         B         C         D      E
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632    one
2013-01-02  1.212112 -0.173215  0.119209 -1.044236    one
2013-01-03 -0.861849 -2.10456ㄹ9 -0.494929  1.071804    two
2013-01-04  0.721555 -0.706771 -1.039575  0.271860  three
2013-01-05 -0.424972  0.567020  0.276232 -1.087401   four
2013-01-06 -0.673690  0.113648 -1.478427  0.524988  three

In [44]: df2[df2["E"].isin(["two", "four"])]
Out[44]: 
                   A         B         C         D     E
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804   two
2013-01-05 -0.424972  0.567020  0.276232 -1.087401  four
```

### 설정 (Setting)

- 새 열을 설정하면 인덱스에 따라 데이터가 자동으로 정렬됩니다:

```python
In [45]: s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))

In [46]: s1
Out[46]: 
2013-01-02    1
2013-01-03    2
2013-01-04    3
2013-01-05    4
2013-01-06    5
2013-01-07    6
Freq: D, dtype: int64

In [47]: df["F"] = s1
```

- 레이블별로 값을 설정합니다:

```python
In [48]: df.at[dates[0], "A"] = 0
```

- 레이블별로 위치를 설정합니다:

```python
In [49]: df.iat[0, 1] = 0
```

- NumPy 배열로 할당하여 설정합니다:

```python
In [50]: df.loc[:, "D"] = np.array([5] * len(df))
```

- 이전 설정 작업의 결과입니다:

```python
In [51]: df
Out[51]: 
                   A         B         C    D    F
2013-01-01  0.000000  0.000000 -1.509059  5.0  NaN
2013-01-02  1.212112 -0.173215  0.119209  5.0  1.0
2013-01-03 -0.861849 -2.104569 -0.494929  5.0  2.0
2013-01-04  0.721555 -0.706771 -1.039575  5.0  3.0
2013-01-05 -0.424972  0.567020  0.276232  5.0  4.0
2013-01-06 -0.673690  0.113648 -1.478427  5.0  5.0
```

- 설정이 있는 `where` 작업:

```python
In [52]: df2 = df.copy()

In [53]: df2[df2 > 0] = -df2

In [54]: df2
Out[54]: 
                   A         B         C    D    F
2013-01-01  0.000000  0.000000 -1.509059 -5.0  NaN
2013-01-02 -1.212112 -0.173215 -0.119209 -5.0 -1.0
2013-01-03 -0.861849 -2.104569 -0.494929 -5.0 -2.0
2013-01-04 -0.721555 -0.706771 -1.039575 -5.0 -3.0
2013-01-05 -0.424972 -0.567020 -0.276232 -5.0 -4.0
2013-01-06 -0.673690 -0.113648 -1.478427 -5.0 -5.0
```

## 데이터 삭제
- `Dataframe.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')` 함수는 해당 row나 column을 삭제합니다.
- `inplace`는 결과를 바로 반영할 것인지, 반환 받을 것인지 결정합니다.


## 누락된 데이터 (Missing data)

- NumPy 데이터 타입의 경우, `np.nan`은 누락된 데이터를 나타냅니다. 기본적으로 계산에 포함되지 않습니다. [누락된 데이터 섹션](https://pandas.pydata.org/docs/user_guide/missing_data.html#missing-data)을 참조하세요.
- 재색인을 사용하면 지정된 축의 인덱스를 변경/추가/삭제할 수 있습니다. 그러면 데이터 사본이 반환됩니다:

```python
In [55]: df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])

In [56]: df1.loc[dates[0] : dates[1], "E"] = 1

In [57]: df1
Out[57]: 
                   A         B         C    D    F    E
2013-01-01  0.000000  0.000000 -1.509059  5.0  NaN  1.0
2013-01-02  1.212112 -0.173215  0.119209  5.0  1.0  1.0
2013-01-03 -0.861849 -2.104569 -0.494929  5.0  2.0  NaN
2013-01-04  0.721555 -0.706771 -1.039575  5.0  3.0  NaN
```

- [`DataFrame.dropna()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna "pandas.DataFrame.dropna")는 누락된 데이터가 있는 모든 행을 삭제합니다:

```python
In [58]: df1.dropna(how="any")
Out[58]: 
                   A         B         C    D    F    E
2013-01-02  1.212112 -0.173215  0.119209  5.0  1.0  1.0
```

- [`DataFrame.fillna()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna "pandas.DataFrame.fillna")는 누락된 데이터를 채웁니다:

```python
In [59]: df1.fillna(value=5)
Out[59]: 
                   A         B         C    D    F    E
2013-01-01  0.000000  0.000000 -1.509059  5.0  5.0  1.0
2013-01-02  1.212112 -0.173215  0.119209  5.0  1.0  1.0
2013-01-03 -0.861849 -2.104569 -0.494929  5.0  2.0  5.0
2013-01-04  0.721555 -0.706771 -1.039575  5.0  3.0  5.0
```

- [`isna()`](https://pandas.pydata.org/docs/reference/api/pandas.isna.html#pandas.isna "pandas.isna")는 값이 `nan`인 부울 마스크를 가져옵니다:

```python
In [60]: pd.isna(df1)
Out[60]: 
                A      B      C      D      F      E
2013-01-01  False  False  False  False   True  False
2013-01-02  False  False  False  False  False  False
2013-01-03  False  False  False  False  False   True
2013-01-04  False  False  False  False  False   True
```

## 6. 연산 (Operations)

- [바이너리 운영의 기본 섹션](https://pandas.pydata.org/docs/user_guide/basics.html#basics-binop)을 참조하세요.
- 숫자형 데이터 타입을 갖는 `Series`에 특정 숫자를 `+`, `*`할 경우 `Series`가 가진 모든 값에 해당 연산을 적용하여 반환합니다.
```python
>> series1 = pd.Series([1, 2, 3, 4])
>> series2 = pd.Series([10, 20, 30, 40])
>> series1 + 10
0    11
1    12
2    13
3    14
dtype: int64
>> series2 * 10
0    100
1    200
2    300
3    400
dtype: int64
```

- `Series`끼리 더하거나 곱할 경우 두 `Series`의같은 Index 값끼리 해당 연산을 수행합니다.

```python
# 두 개의 Series 생성
>> series1 = pd.Series([1, 2, 3, 4])
>> series2 = pd.Series([10, 20, 30, 40])

# + 연산 (덧셈)
>> addition_result = series1 + series2
0    11
1    22
2    33
3    44
dtype: int64

# * 연산 (곱셈)
>> multiplication_result = series1 * series2
0    10
1    40
2    90
3    160
dtype: int64
```

### 1) 통계

- 연산은 일반적으로 누락된 데이터를 제외합니다.
- 각 열의 평균값을 계산합니다:

```python
In [61]: df.mean()
Out[61]: 
A   -0.004474
B   -0.383981
C   -0.687758
D    5.000000
F    3.000000
dtype: float64
```

- 각 행의 평균값을 계산합니다:

```python
In [62]: df.mean(axis=1)
Out[62]: 
2013-01-01    0.872735
2013-01-02    1.431621
2013-01-03    0.707731
2013-01-04    1.395042
2013-01-05    1.883656
2013-01-06    1.592306
Freq: D, dtype: float64
```

- 다른 인덱스나 열을 가진 다른 [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series") 또는 [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")으로 작업하면 결과가 인덱스 또는 열 레이블의 유니온에 맞춰 정렬됩니다. 또한 pandas는 지정된 차원을 따라 자동으로 브로드캐스트하고 정렬되지 않은 레이블을 `np.nan`으로 채웁니다.
- `DataFrame`에 적용할 경우 모든 컬럼에 적용됩니다.

```python
In [63]: s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)

In [64]: s
Out[64]: 
2013-01-01    NaN
2013-01-02    NaN
2013-01-03    1.0
2013-01-04    3.0
2013-01-05    5.0
2013-01-06    NaN
Freq: D, dtype: float64

In [65]: df.sub(s, axis="index")
Out[65]: 
                   A         B         C    D    F
2013-01-01       NaN       NaN       NaN  NaN  NaN
2013-01-02       NaN       NaN       NaN  NaN  NaN
2013-01-03 -1.861849 -3.104569 -1.494929  4.0  1.0
2013-01-04 -2.278445 -3.706771 -4.039575  2.0  0.0
2013-01-05 -5.424972 -4.432980 -4.723768  0.0 -1.0
2013-01-06       NaN       NaN       NaN  NaN  NaN
```

| 함수        | 의미                                      |
| --------- | --------------------------------------- |
| `count()` | null이 아닌 데이터의 수<br>(row의 수는 `shape` 권장) |
| `mean()`  | 평균                                      |
| `sum()`   | 합계                                      |
| ``        |                                         |

### 2) 사용자 정의 함수 (User defined functions)

- [`DataFrame.agg()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html#pandas.DataFrame.agg "pandas.DataFrame.agg")와 [`DataFrame.transform()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transform.html#pandas.DataFrame.transform "pandas.DataFrame.transform")은 각각 결과를 축소하거나 브로드캐스트하는 사용자 정의 함수를 적용합니다.

```python
In [66]: df.agg(lambda x: np.mean(x) * 5.6)
Out[66]: 
A    -0.025054
B    -2.150294
C    -3.851445
D    28.000000
F    16.800000
dtype: float64

In [67]: df.transform(lambda x: x * 101.2)
Out[67]: 
                     A           B           C      D      F
2013-01-01    0.000000    0.000000 -152.716721  506.0    NaN
2013-01-02  122.665737  -17.529322   12.063922  506.0  101.2
2013-01-03  -87.219115 -212.982405  -50.086843  506.0  202.4
2013-01-04   73.021382  -71.525239 -105.204988  506.0  303.6
2013-01-05  -43.007200   57.382459   27.954680  506.0  404.8
2013-01-06  -68.177398   11.501219 -149.616767  506.0  506.0
```

- Column에 여러 함수를 동시에 적용하고 싶을 경우 `list` 형태로 전달할 수 있습니다.

```python
df.groupby('Pclass')['Age'].agg([max, min])
```


- 서로 다른 column에 서로 다른 aggregation 함수를 적용할 경우 `dict` 형태로 적용할 column과 method를 입력할 수 있습니다.

```python
agg_format={"Age": "max", "SibSp": "sum", "Fare": "mean"}
df.groupby("PClass").agg(agg_format)
```

### ==3) 값 수 (Value Counts)==

- `Series.value_counts()`는 동일한 개별 데이터 값이 몇건이 있는지 제공합니다. 
- 기본은 `dropna=True`로 설정되어 있습니다. `dropna=False`로 설정하면 `null`도 확인할 수 있습니다.
- 자세한 내용은 [히스토그램 및 불연속화](https://pandas.pydata.org/docs/user_guide/basics.html#basics-discretization)에서 확인하세요.

```python
In [68]: s = pd.Series(np.random.randint(0, 7, size=10))

In [69]: s
Out[69]: 
0    4
1    2
2    1
3    2
4    6
5    4
6    4
7    6
8    4
9    4
dtype: int64

In [70]: s.value_counts()
Out[70]: 
4    5
2    2
6    2
1    1
Name: count, dtype: int64
```

- `DataFrame`에 대해서도 사용 가능합니다.

```python
# DataFrame 대상
titanic_df[['Pclass', 'Embarked']].value_counts()
```

### 4) 문자열 메서드 (String Methods)

- [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")에는 아래 코드 스니펫과 같이 배열의 각 요소를 쉽게 연산할 수 있는 문자열 처리 메서드 세트가 `str` 속성에 탑재되어 있습니다. 자세한 내용은 [벡터화된 문자열 메서드](https://pandas.pydata.org/docs/user_guide/text.html#text-string-methods)를 참조하세요.

```python
In [71]: s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])

In [72]: s.str.lower()
Out[72]: 
0       a
1       b
2       c
3    aaba
4    baca
5     NaN
6    caba
7     dog
8     cat
dtype: object
```

## 7. 병합 (Merge)

### 1) 결합 (Concatenate)
- pandas는 인덱스에 대한 다양한 종류의 집합 로직과 조인/병합 타입 작업의 경우 관계대수 기능을 사용하여 [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series") 및 [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 객체를 쉽게 결합할 수 있는 다양한 기능을 제공합니다.
- [병합 섹션](https://pandas.pydata.org/docs/user_guide/merging.html#merging)을 참조하세요.
- [`concat()`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html#pandas.concat "pandas.concat")을 사용하여 팬더 객체를 행 단위로 연결합니다:

```python
In [73]: df = pd.DataFrame(np.random.randn(10, 4))

In [74]: df
Out[74]: 
          0         1         2         3
0 -0.548702  1.467327 -1.015962 -0.483075
1  1.637550 -1.217659 -0.291519 -1.745505
2 -0.263952  0.991460 -0.919069  0.266046
3 -0.709661  1.669052  1.037882 -1.705775
4 -0.919854 -0.042379  1.247642 -0.009920
5  0.290213  0.495767  0.362949  1.548106
6 -1.131345 -0.089329  0.337863 -0.945867
7 -0.932132  1.956030  0.017587 -0.016692
8 -0.575247  0.254161 -1.143704  0.215897
9  1.193555 -0.077118 -0.408530 -0.862495

# break it into pieces
In [75]: pieces = [df[:3], df[3:7], df[7:]]

In [76]: pd.concat(pieces)
Out[76]: 
          0         1         2         3
0 -0.548702  1.467327 -1.015962 -0.483075
1  1.637550 -1.217659 -0.291519 -1.745505
2 -0.263952  0.991460 -0.919069  0.266046
3 -0.709661  1.669052  1.037882 -1.705775
4 -0.919854 -0.042379  1.247642 -0.009920
5  0.290213  0.495767  0.362949  1.548106
6 -1.131345 -0.089329  0.337863 -0.945867
7 -0.932132  1.956030  0.017587 -0.016692
8 -0.575247  0.254161 -1.143704  0.215897
9  1.193555 -0.077118 -0.408530 -0.862495
```

> [!NOTE]
> - [`DatraFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")에 열을 추가하는 것은 비교적 빠릅니다. 그러나 행을 추가하려면 복사본이 필요하며 비용이 많이 들 수 있습니다. 레코드를 반복적으로 추가하여 [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")을 만드는 대신 미리 작성된 레코드 목록을 [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") 생성자에 전달할 것을 권장합니다.

### 2) 조인 (Join)

- [`merge()`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html#pandas.merge "pandas.merge")는 특정 열을 따라 SQL 스타일 조인 유형을 활성화합니다. [데이터베이스 스타일 조인](https://pandas.pydata.org/docs/user_guide/merging.html#merging-join) 섹션을 참조하세요.

```python
In [77]: left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})

In [78]: right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})

In [79]: left
Out[79]: 
   key  lval
0  foo     1
1  foo     2

In [80]: right
Out[80]: 
   key  rval
0  foo     4
1  foo     5

In [81]: pd.merge(left, right, on="key")
Out[81]: 
   key  lval  rval
0  foo     1     4
1  foo     1     5
2  foo     2     4
3  foo     2     5
```

- 고유 키에 [`merge()`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html#pandas.merge "pandas.merge")를 추가합니다:

```python
In [82]: left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})

In [83]: right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})

In [84]: left
Out[84]: 
   key  lval
0  foo     1
1  bar     2

In [85]: right
Out[85]: 
   key  rval
0  foo     4
1  bar     5

In [86]: pd.merge(left, right, on="key")
Out[86]: 
   key  lval  rval
0  foo     1     4
1  bar     2     5
```

### 3) 그룹화 (Grouping)
- "그룹화 기준"이란 다음 단계 중 하나 이상을 포함하는 프로세스를 의미합니다:
	- 몇 가지 기준에 따라 데이터를 그룹으로 **분할**하기
	- 각 그룹에 독립적으로 함수 **적용**하기
	- 결과를 데이터 구조로 **결합**하기
- [그룹화 섹션](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby)을 참조하세요.

```python
In [87]: df = pd.DataFrame(
   ….:    {
   ….:        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
   ….:        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
   ….:        "C": np.random.randn(8),
   ….:        "D": np.random.randn(8),
   ….:    }
   ….: )
   ….: 

In [88]: df
Out[88]: 
     A      B         C         D
0  foo    one  1.346061 -1.577585
1  bar    one  1.511763  0.396823
2  foo    two  1.627081 -0.105381
3  bar  three -0.990582 -0.532532
4  foo    two -0.441652  1.453749
5  bar    two  1.211526  1.208843
6  foo    one  0.268520 -0.080952
7  foo  three  0.024580 -0.264610
```

- 열 레이블을 기준으로 그룹화하고, 열 레이블을 선택한 다음 [`DataFrameGroupBy.sum()`](https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.sum.html#pandas.core.groupby.DataFrameGroupBy.sum "pandas.core.groupby.DataFrameGroupBy.sum") 함수를 결과 그룹에 적용합니다:

```python
In [89]: df.groupby("A")[["C", "D"]].sum()
Out[89]: 
            C         D
A                      
bar  1.732707  1.073134
foo  2.824590 -0.574779
```

- 여러 열로 그룹화하기 [`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "Pandas.멀티인덱스") 레이블 양식.

```python
In [90]: df.groupby(["A", "B"]).sum()
Out[90]: 
                  C         D
A   B                        
bar one    1.511763  0.396823
    three -0.990582 -0.532532
    two    1.211526  1.208843
foo one    1.614581 -1.658537
    three  0.024580 -0.264610
    two    1.185429  1.348368
```

## 8. 재구성 (Reshaping)

- [계층적 인덱싱](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced-hierarchical) 및 [재구성](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping-stacking) 섹션을 참조하세요.

### 1) 스택 (Stack)

```python
In [91]: arrays = [
   ….:   ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
   ….:   ["one", "two", "one", "two", "one", "two", "one", "two"],
   ….: ]
   ….: 

In [92]: index = pd.MultiIndex.from_arrays(arrays, names=["first", "second"])

In [93]: df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])

In [94]: df2 = df[:4]

In [95]: df2
Out[95]: 
                     A         B
first second                    
bar   one    -0.727965 -0.589346
      two     0.339969 -0.693205
baz   one    -0.339355  0.593616
      two     0.884345  1.591431
```

- [`stack()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.stack.html#pandas.DataFrame.stack "pandas.DataFrame.stack") 메서드는 데이터프레임의 열에서 레벨을 '압축'합니다:

```python
In [96]: stacked = df2.stack(future_stack=True)

In [97]: stacked
Out[97]: 
first  second   
bar    one     A   -0.727965
               B   -0.589346
       two     A    0.339969
               B   -0.693205
baz    one     A   -0.339355
               B    0.593616
       two     A    0.884345
               B    1.591431
dtype: float64
```

- "스택된" 데이터 프레임 또는 시리즈([`멀티 인덱스`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")를 `인덱스`로 갖는)의 경우, [`stack()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.stack.html#pandas.DataFrame.stack "pandas.DataFrame.stack)의 역 연산은 기본적으로 **최근 레벨**을 언스택하는 [`unstack()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html#pandas.DataFrame.unstack "pandas.DataFrame.unstack)]입니다:

```python
In [98]: stacked.unstack()
Out[98]: 
                     A         B
first second                    
bar   one    -0.727965 -0.589346
      two     0.339969 -0.693205
baz   one    -0.339355  0.593616
      two     0.884345  1.591431

In [99]: stacked.unstack(1)
Out[99]: 
second        one       two
first                      
bar   A -0.727965  0.339969
      B -0.589346 -0.693205
baz   A -0.339355  0.884345
      B  0.593616  1.591431

In [100]: stacked.unstack(0)
Out[100]: 
first          bar       baz
second                      
one    A -0.727965 -0.339355
       B -0.589346  0.593616
two    A  0.339969  0.884345
       B -0.693205  1.591431
```

### 2) 피벗 테이블 (Pivot tables)

- [피벗 테이블](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping-pivot) 섹션을 참조하세요.

```python
In [101]: df = pd.DataFrame(
   …..:    {
   …..:        "A": ["one", "one", "two", "three"] * 3,
   …..:        "B": ["A", "B", "C"] * 4,
   …..:        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
   …..:        "D": np.random.randn(12),
   …..:        "E": np.random.randn(12),
   …..:    }
   …..: )
   …..: 

In [102]: df
Out[102]: 
        A  B    C         D         E
0     one  A  foo -1.202872  0.047609
1     one  B  foo -1.814470 -0.136473
2     two  C  foo  1.018601 -0.561757
3   three  A  bar -0.595447 -1.623033
4     one  B  bar  1.395433  0.029399
5     one  C  bar -0.392670 -0.542108
6     two  A  foo  0.007207  0.282696
7   three  B  foo  1.928123 -0.087302
8     one  C  foo -0.055224 -1.575170
9     one  A  bar  2.395985  1.771208
10    two  B  bar  1.552825  0.816482
11  three  C  bar  0.166599  1.100230
```

[`pivot_table()`](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html#pandas.pivot_table "pandas.pivot_table") pivots a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") specifying the `values`, `index` and `columns`

```python
In [103]: pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])
Out[103]: 
C             bar       foo
A     B                    
one   A  2.395985 -1.202872
      B  1.395433 -1.814470
      C -0.392670 -0.055224
three A -0.595447       NaN
      B       NaN  1.928123
      C  0.166599       NaN
two   A       NaN  0.007207
      B  1.552825       NaN
      C       NaN  1.018601
```

## 9. 시계열 (Time series)

- Pandas에는 주파수 변환 중 리샘플링 작업(예: 초 단위 데이터를 5분 단위 데이터로 변환)을 수행할 수 있는 간단하고 강력하며 효율적인 기능이 있습니다. 이는 금융 애플리케이션에서 매우 일반적이지만 이에 국한되지 않습니다. [시계열 섹션](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries)을 참조하세요.

```python
In [104]: rng = pd.date_range("1/1/2012", periods=100, freq="s")

In [105]: ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)

In [106]: ts.resample("5Min").sum()
Out[106]: 
2012-01-01    24182
Freq: 5min, dtype: int64
```

- [`Series.tz_localize()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.tz_localize.html#pandas.Series.tz_localize "pandas.Series.tz_localize")는 시계열을 시간대로 지역화합니다:

```python
In [107]: rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")

In [108]: ts = pd.Series(np.random.randn(len(rng)), rng)

In [109]: ts
Out[109]: 
2012-03-06    1.857704
2012-03-07   -1.193545
2012-03-08    0.677510
2012-03-09   -0.153931
2012-03-10    0.520091
Freq: D, dtype: float64

In [110]: ts_utc = ts.tz_localize("UTC")

In [111]: ts_utc
Out[111]: 
2012-03-06 00:00:00+00:00    1.857704
2012-03-07 00:00:00+00:00   -1.193545
2012-03-08 00:00:00+00:00    0.677510
2012-03-09 00:00:00+00:00   -0.153931
2012-03-10 00:00:00+00:00    0.520091
Freq: D, dtype: float64
```

- [`Series.tz_convert()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.tz_convert.html#pandas.Series.tz_convert "pandas.Series.tz_convert")는 시간대 인식 시계열을 다른 시간대로 변환합니다:

```python
In [112]: ts_utc.tz_convert("US/Eastern")
Out[112]: 
2012-03-05 19:00:00-05:00    1.857704
2012-03-06 19:00:00-05:00   -1.193545
2012-03-07 19:00:00-05:00    0.677510
2012-03-08 19:00:00-05:00   -0.153931
2012-03-09 19:00:00-05:00    0.520091
Freq: D, dtype: float64

Adding a non-fixed duration ([`BusinessDay`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.BusinessDay.html#pandas.tseries.offsets.BusinessDay "pandas.tseries.offsets.BusinessDay")) to a time series:

In [113]: rng
Out[113]: 
DatetimeIndex(['2012-03-06', '2012-03-07', '2012-03-08', '2012-03-09',
               '2012-03-10'],
              dtype='datetime64[ns]', freq='D')

In [114]: rng + pd.offsets.BusinessDay(5)
Out[114]: 
DatetimeIndex(['2012-03-13', '2012-03-14', '2012-03-15', '2012-03-16',
               '2012-03-16'],
              dtype='datetime64[ns]', freq=None)
```

## 10. 범주형 (Categoricals)

- Pandas는 [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")에 범주형 데이터를 포함할 수 있습니다. 전체 문서는 [범주형 소개](https://pandas.pydata.org/docs/user_guide/categorical.html#categorical) 및 [API 문서](https://pandas.pydata.org/docs/reference/arrays.html#api-arrays-categorical)를 참조하세요.

```python
In [115]: df = pd.DataFrame(
   …..:    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
   …..: )
   …..: 
```

- `raw_grade`를 범주형 데이터 유형으로 변환합니다.

```python
In [116]: df["grade"] = df["raw_grade"].astype("category")

In [117]: df["grade"]
Out[117]: 
0    a
1    b
2    b
3    a
4    a
5    e
Name: grade, dtype: category
Categories (3, object): ['a', 'b', 'e']
```

- 카테고리의 이름을 더 의미 있는 이름으로 변경합니다:

```python
In [118]: new_categories = ["very good", "good", "very bad"]

In [119]: df["grade"] = df["grade"].cat.rename_categories(new_categories)
```

- 카테고리의 순서를 바꾸고 동시에 누락된 카테고리를 추가합니다 ([`Series.cat()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.html#pandas.Series.cat) 아래의 메서드는 기본적으로 새 [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")를 반환합니다):

```python
In [120]: df["grade"] = df["grade"].cat.set_categories(
   …..:    ["very bad", "bad", "medium", "good", "very good"]
   …..: )
   …..: 

In [121]: df["grade"]
Out[121]: 
0    very good
1         good
2         good
3    very good
4    very good
5     very bad
Name: grade, dtype: category
Categories (5, object): ['very bad', 'bad', 'medium', 'good', 'very good']
```

- 정렬은 어휘 순서가 아닌 카테고리의 순서에 따라 이루어집니다:

```python
In [122]: df.sort_values(by="grade")
Out[122]: 
   id raw_grade      grade
5   6         e   very bad
1   2         b       good
2   3         b       good
0   1         a  very good
3   4         a  very good
4   5         a  very good
```

- `observed=False`으로 범주 열을 기준으로 그룹화하면 빈 범주도 표시됩니다:

```python
In [123]: df.groupby("grade", observed=False).size()
Out[123]: 
grade
very bad     1
bad          0
medium       0
good         2
very good    3
dtype: int64
```

## 11. 플로팅 (Plotting)
- [플로팅](https://pandas.pydata.org/docs/user_guide/visualization.html#visualization) 문서를 참조하세요.
- matplotlib API를 참조할 때는 표준 규칙을 사용합니다:

```python
In [124]: import matplotlib.pyplot as plt

In [125]: plt.close("all")
```

- `plt.close` 메서드는 그림 창을 [닫기](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html)하는 데 사용됩니다:

```python
In [126]: ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))

In [127]: ts = ts.cumsum()

In [128]: ts.plot();
```

![../_images/series_plot_basic.png](https://pandas.pydata.org/docs/_images/series_plot_basic.png)


> [!NOTE]
> - Jupyter를 사용하는 경우, [`plot()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.html#pandas.Series.plot "pandas.Series.plot")을 사용하여 플롯이 표시됩니다. 그렇지 않으면 [matplotlib.pyplot.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html)를 사용하여 표시하거나 [matplotlib.pyplot.savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html)를 사용하여 파일에 기록합니다.

- [`plot()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot "pandas.DataFrame.plot")은 모든 열을 플로팅합니다:

```python
In [129]: df = pd.DataFrame(
   …..:    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
   …..: )
   …..: 

In [130]: df = df.cumsum()

In [131]: plt.figure();

In [132]: df.plot();

In [133]: plt.legend(loc='best');
```

![../_images/frame_plot_basic.png](https://pandas.pydata.org/docs/_images/frame_plot_basic.png)

## 12. 데이터 가져오기 및 내보내기 (Importing and exporting data) [[pandas_io_tools|(자세히 보기)]]

### 1) CSV

- [데이터 프레임에 쓰기:](https://pandas.pydata.org/docs/user_guide/io.html#io-store-in-csv) [`DataFrame.to_csv()` 사용](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv "pandas.DataFrame.to_csv")
```python
In [134]: df = pd.DataFrame(np.random.randint(0, 5, (10, 5)))

In [135]: df.to_csv("foo.csv")
```

- [csv 파일에서 읽기:](https://pandas.pydata.org/docs/user_guide/io.html#io-read-csv-table) [`read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv") 사용

```python
In [136]: pd.read_csv("foo.csv")
Out[136]: 
   Unnamed: 0  0  1  2  3  4
0           0  4  3  1  1  2
1           1  1  0  2  3  2
2           2  1  4  2  1  2
3           3  0  4  0  2  2
4           4  4  2  2  3  4
5           5  4  0  4  3  1
6           6  2  1  2  0  3
7           7  4  0  4  4  4
8           8  4  4  1  0  1
9           9  0  4  3  0  3
```

### 2) Parquet

- Parquet 파일에 쓰기:

```python
In [137]: df.to_parquet("foo.parquet")
```

- Parquet 파일 저장소에서 읽기 [`read_parquet()`](https://pandas.pydata.org/docs/reference/api/pandas.read_parquet.html#pandas.read_parquet "pandas.read_parquet")를 사용합니다:

```python
In [138]: pd.read_parquet("foo.parquet")
Out[138]: 
   0  1  2  3  4
0  4  3  1  1  2
1  1  0  2  3  2
2  1  4  2  1  2
3  0  4  0  2  2
4  4  2  2  3  4
5  4  0  4  3  1
6  2  1  2  0  3
7  4  0  4  4  4
8  4  4  1  0  1
9  0  4  3  0  3
```

### 3) Excel

- [Excel](https://pandas.pydata.org/docs/user_guide/io.html#io-excel)에 읽기 및 쓰기.
- [`DataFrame.to_excel()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html#pandas.DataFrame.to_excel "pandas.DataFrame.to_excel")을 사용하여 엑셀 파일에 쓰기:

```python
In [139]: df.to_excel("foo.xlsx", sheet_name="Sheet1")
```

- [`read_excel()`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html#pandas.read_excel "pandas.read_excel")을 사용하여 엑셀 파일에서 읽습니다:

```python
In [140]: pd.read_excel("foo.xlsx", "Sheet1", index_col=None, na_values=["NA"])
Out[140]: 
   Unnamed: 0  0  1  2  3  4
0           0  4  3  1  1  2
1           1  1  0  2  3  2
2           2  1  4  2  1  2
3           3  0  4  0  2  2
4           4  4  2  2  3  4
5           5  4  0  4  3  1
6           6  2  1  2  0  3
7           7  4  0  4  4  4
8           8  4  4  1  0  1
9           9  0  4  3  0  3
```

## 13. 고쳐야 할 점 (Gotchas)

- [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series") 또는 [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame)에서 부울 연산을 수행하려고 하면 다음과 같은 예외가 발생할 수 있습니다:

```python
In [141]: if pd.Series([False, True, False]):
   …..:     print("I was true")
   …..: 
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-141-b27eb9c1dfc0> in ?()
----> 1 if pd.Series([False, True, False]):
      2      print("I was true")

~/work/pandas/pandas/pandas/core/generic.py in ?(self)
   1575     @final
   1576     def __nonzero__(self) -> NoReturn:
-> 1577         raise ValueError(
   1578             f"The truth value of a {type(self).__name__} is ambiguous. "
   1579             "Use a.empty, a.bool(), a.item(), a.any() or a.all()."
   1580         )

ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
```

- [비교](https://pandas.pydata.org/docs/user_guide/basics.html#basics-compare) 및 [고쳐야 할 점](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas)에서 설명과 해결 방법을 확인하세요.


---
## 참조
[API reference — pandas 2.2.2 documentation (pydata.org)](https://pandas.pydata.org/docs/reference/index.html)
---
title: "[]"
excerpt: 
categories: 
tags: 
last_modified_at: 2024-03-01T00:00:00-00:00
link: 
상위 항목: "[[]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

**하위 항목**
- 

---
## Indexing ([참고 자료](../csv/iphone.csv))

- DataFrame 에 Index 로 바로 접근할 경우 Column 에 접근할 수 있다.
- `loc` 에 Index 명만 입력하면 그 Row 에 접근한다.
- `loc` 나 `iloc` 에 행과 열을 모두 입력하면 하나의 값에 접근한다.

```python
# Index(loc), Index명, 원하는 Column순으로 입력
iphone_df.loc['iPhone 8', '메모리']

# 여러 Column 한번에 불러오기
iphone_df.loc['iPhone X', :] # Series로 반환
iphone_df.loc['iPhone X'] # 위와 같다.

# 여러 Index 한번에 불러오기
iphone_df.loc[:,'출시일']
iphone_df['출시일'] # Column명으로 바로 접근 가능

iphone_df.loc[:,['메모리','출시일']] # 리스트를 활용하여 여러 Column 접근 가능

# Index명도 슬라이싱 가능
iphone_df.loc['iPhone 8':'iPhone XS']
```

- Column 명으로 슬라이싱은 불가능하다. Column 명만 출력된다.
- Pandas 도 Boolean Indexing 을 지원한다. True 에 해당하는 Index 를 불러온다.

```python
# Boolean Indexing
iphone_df.loc[True,False,True,True,False,True,False]

# Column에도 적용 가능
iphone_df.loc[:,[True,False,False,True]]

# 조건을 활용하여 주로 사용
iphone_df.loc[iphone_df['디스플레이'] > 5]
iphone_df.loc[iphone_df['Face ID'] == 'Yes']
iphone_df.loc[iphone_df['디스플레이'] > 5 & iphone_df['Face ID'] == 'Yes']
```

- numpy 처럼 숫자로도 Indexing 이 가능하다.

```python
# 숫자로 Indexing (iloc)
iphone_df.iloc[2, 4]
iphone_df.iloc[[1, 3],[1, 4]]
iphone_df.iloc[3:, 1:4]
```

- 특정 문자열을 포함한 행만 불러올 수 있다.

```python
# 특정 문자열을 포함한 행 필터링 (True / False)
df[df['Genre'].str.contains('Blues')]

# 특정 문자열로 시작하는 행 필터링
df[df['Genre'].str.startswith('Blues')]

# 문자열 분리하기 (공백은 띄어쓰기 기준)
df['소재지도로명주소'].str.split()

# n=1일 경우 첫번째 띄어쓰기로만 분리한다.
df['소재지도로명주소'].str.split(n=1)

# expand=True일 경우 새로운 DataFrame을 반환한다.
df['소재지도로명주소'].str.split(n=1, expand=True)
```

---

### Groupby

- 원하는 Column 기준으로 묶어준다.
- 특정 Column 의 값을 기준으로 다른 Column 들의 최대값 등의 함수를 적용하여 확인하기 좋다.

```python
# Groupby 생성
nation_groups = df.groupby('brand_nation')
nation_groups.max()

# 두개 이상의 Column으로 그룹화
df.groupby(['sex', 'pclass']).mean()

# 그룹화한 데이터에서 원하는 Column 결과 확인
df.groupby(['sex', 'pclass'])['survived'].mean()

# 여러 Column의 결과 확인
df.groupby(['sex', 'pclass'])[['survived', 'age']].mean()

# 그룹화 이전으로 초기화
df.groupby(['sex', 'pclass'])['survived'].mean().reset_index()
```

---

### pivot_table()

- Excel 의 Pivot, `groupby()` 와 동작이 유사하다.
- index, columns, values 를 지정하여 pivot 한다.

```python
# index에 그룹을 표기
df.pivot_table(index='who', values='survived')

# columns에 그룹을 표기
df.pivot_table(columns='who', values='survived')

# 다중 그룹 표기
df.pivot_table(index=['who', 'pclass'], values='survived')

# 행과 열을 모두 적용하여 표기
df.pivot_table(index='who', columns='pclass', values='survived')

# 다중 통계 함수 적용
df.pivot_table(index='who', columns='pclass', values='survived', aggfunc=['sum', 'mean'])
```

---

### isin

- 특정 값의 포함 여부 확인, python 의 `in` 사용이 불가하므로 대신 사용한다.

```python
sample['name'].isin(['kim','lee'])
```

여기 pandas 객체의 축 라벨링 정보에 대한 한국어 번역입니다. 요청하신 조건들을 준수했습니다:

pandas 객체의 축 라벨링 정보는 여러 목적으로 사용됩니다:

- 알려진 지표를 사용하여 데이터를 식별(즉, 메타데이터 제공)하며, 이는 분석, 시각화 및 대화형 콘솔 표시에 중요합니다.
    
- 자동 및 명시적 데이터 정렬을 가능하게 합니다.
    
- 데이터 세트의 부분 집합을 직관적으로 가져오고 설정할 수 있게 합니다.
    

이 섹션에서는 마지막 요점에 초점을 맞추겠습니다. 즉, pandas 객체의 부분 집합을 어떻게 슬라이스하고, 자르고, 일반적으로 가져오고 설정하는지에 대해 설명하겠습니다. 주로 Series와 DataFrame에 초점을 맞출 것입니다. 이 영역에서 더 많은 개발 관심을 받았기 때문입니다.

참고

Python과 NumPy 인덱싱 연산자 []와 속성 연산자 .는 다양한 사용 사례에서 pandas 데이터 구조에 대한 빠르고 쉬운 접근을 제공합니다. 이는 Python 딕셔너리와 NumPy 배열을 다루는 방법을 이미 알고 있다면 직관적인 대화형 작업을 가능하게 합니다. 그러나 접근할 데이터의 유형을 미리 알 수 없기 때문에, 표준 연산자를 직접 사용하는 것에는 일부 최적화 한계가 있습니다. 프로덕션 코드의 경우, 이 장에서 설명하는 최적화된 pandas 데이터 접근 메서드를 활용하는 것이 좋습니다.

경고

설정 작업에서 복사본이 반환되는지 참조가 반환되는지는 상황에 따라 다를 수 있습니다. 이를 때때로 '연쇄 할당'이라고 하며 피해야 합니다. [뷰 대 복사본 반환](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-view-versus-copy)을 참조하세요.

MultiIndex와 더 고급 인덱싱 문서는 [MultiIndex / 고급 인덱싱](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced)을 참조하세요.

일부 고급 전략은 [요리책](https://pandas.pydata.org/docs/user_guide/cookbook.html#cookbook-selection)을 참조하세요.

## 인덱싱을 위한 다양한 선택 (Different choices for indexing)

객체 선택은 더 명시적인 위치 기반 인덱싱을 지원하기 위해 사용자 요청에 따라 여러 가지 추가 사항이 있었습니다. pandas는 현재 세 가지 유형의 다중 축 인덱싱을 지원합니다.

- .loc은 주로 레이블 기반이지만 불리언 배열과 함께 사용할 수도 있습니다. .loc은 항목을 찾을 수 없을 때 KeyError를 발생시킵니다. 허용되는 입력은 다음과 같습니다:
    
    > - 단일 레이블, 예: 5 또는 'a' (5는 인덱스의 레이블로 해석됩니다. 이 사용은 인덱스를 따라 정수 위치가 아닙니다.).
    >     
    > - 레이블의 리스트 또는 배열 ['a', 'b', 'c'].
    >     
    > - 레이블이 있는 슬라이스 객체 'a':'f' (일반적인 Python 슬라이스와 달리, 인덱스에 있을 때 시작과 끝 모두 포함됩니다! [레이블을 사용한 슬라이싱](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-slicing-with-labels)과 [끝점은 포함됨](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced-endpoints-are-inclusive)을 참조하세요.)
    >     
    > - 불리언 배열 (NA 값은 False로 처리됩니다).
    >     
    > - 하나의 인수(호출하는 Series 또는 DataFrame)를 가지고 인덱싱에 유효한 출력(위의 입력 중 하나)을 반환하는 호출 가능한 함수.
    >     
    > - 행 (및 열) 인덱스의 튜플로, 그 요소는 위의 입력 중 하나입니다.
    >     
    
    자세한 내용은 [레이블로 선택](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-label)을 참조하세요.
    
- .iloc은 주로 정수 위치 기반(축의 0부터 length-1까지)이지만 불리언 배열과 함께 사용할 수도 있습니다. .iloc은 요청된 인덱서가 범위를 벗어나면 IndexError를 발생시킵니다. 단, 범위를 벗어난 인덱싱을 허용하는 슬라이스 인덱서는 예외입니다(이는 Python/NumPy 슬라이스 의미론을 따릅니다). 허용되는 입력은 다음과 같습니다:
    
    > - 정수, 예: 5.
    >     
    > - 정수의 리스트 또는 배열 [4, 3, 0].
    >     
    > - 정수가 있는 슬라이스 객체 1:7.
    >     
    > - 불리언 배열 (NA 값은 False로 처리됩니다).
    >     
    > - 하나의 인수(호출하는 Series 또는 DataFrame)를 가지고 인덱싱에 유효한 출력(위의 입력 중 하나)을 반환하는 호출 가능한 함수.
    >     
    > - 행 (및 열) 인덱스의 튜플로, 그 요소는 위의 입력 중 하나입니다.
    >     
    
    자세한 내용은 [위치로 선택](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-integer), [고급 인덱싱](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced) 및 [고급 계층](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced-advanced-hierarchical)을 참조하세요.
    
- .loc, .iloc 및 [] 인덱싱도 호출 가능한 객체를 인덱서로 받을 수 있습니다. 자세한 내용은 [호출 가능한 객체로 선택](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-callable)을 참조하세요.
    
    참고
    
    행 (및 열) 인덱스로 튜플 키를 분해하는 것은 호출 가능한 객체가 적용되기 전에 발생하므로, 호출 가능한 객체에서 행과 열을 모두 인덱싱하기 위해 튜플을 반환할 수 없습니다.
    

다중 축 선택으로 객체에서 값을 가져오는 것은 다음 표기법을 사용합니다 (.loc을 예로 들지만 다음은 .iloc에도 적용됩니다). 축 접근자 중 어느 것이든 널 슬라이스 :일 수 있습니다. 명세에서 생략된 축은 :로 가정됩니다. 예를 들어, p.loc['a']는 p.loc['a', :]와 동일합니다.

|객체 유형|인덱서|
|---|---|
|Series|s.loc[indexer]|
|DataFrame|df.loc[row_indexer,column_indexer]|

## 기본 사항 (Basics)

[이전 섹션](https://pandas.pydata.org/docs/user_guide/basics.html#basics)에서 데이터 구조를 소개할 때 언급했듯이, []로 인덱싱하는 (Python에서 클래스 동작을 구현하는 데 익숙한 사람들에게는 __getitem__로 알려진) 주요 기능은 낮은 차원의 슬라이스를 선택하는 것입니다. 다음 표는 []로 pandas 객체를 인덱싱할 때의 반환 값 유형을 보여줍니다:

|객체 유형|선택|반환 값 유형|
|---|---|---|
|Series|series[label]|스칼라 값|
|DataFrame|frame[colname]|colname에 해당하는 Series|

여기서 인덱싱 기능을 설명하기 위해 간단한 시계열 데이터 세트를 구성합니다:

```python
In [1]: dates = pd.date_range('1/1/2000', periods=8)

In [2]: df = pd.DataFrame(np.random.randn(8, 4),
   ...:                  index=dates, columns=['A', 'B', 'C', 'D'])
   ...: 

In [3]: df
Out[3]: 
                   A         B         C         D
2000-01-01  0.469112 -0.282863 -1.509059 -1.135632
2000-01-02  1.212112 -0.173215  0.119209 -1.044236
2000-01-03 -0.861849 -2.104569 -0.494929  1.071804
2000-01-04  0.721555 -0.706771 -1.039575  0.271860
2000-01-05 -0.424972  0.567020  0.276232 -1.087401
2000-01-06 -0.673690  0.113648 -1.478427  0.524988
2000-01-07  0.404705  0.577046 -1.715002 -1.039268
2000-01-08 -0.370647 -1.157892 -1.344312  0.844885
```

참고

특별히 명시되지 않는 한 인덱싱 기능 중 어느 것도 시계열에만 특화된 것은 아닙니다.

따라서 위와 같이 [] 를 사용한 가장 기본적인 인덱싱이 있습니다:

```python
In [4]: s = df['A']

In [5]: s[dates[5]]
Out[5]: -0.6736897080883706
```

[]에 열의 리스트를 전달하여 해당 순서로 열을 선택할 수 있습니다. DataFrame에 포함되지 않은 열이 있으면 예외가 발생합니다. 여러 열도 이 방식으로 설정할 수 있습니다:

```python
In [6]: df
Out[6]: 
                   A         B         C         D
2000-01-01  0.469112 -0.282863 -1.509059 -1.135632
2000-01-02  1.212112 -0.173215  0.119209 -1.044236
2000-01-03 -0.861849 -2.104569 -0.494929  1.071804
2000-01-04  0.721555 -0.706771 -1.039575  0.271860
2000-01-05 -0.424972  0.567020  0.276232 -1.087401
2000-01-06 -0.673690  0.113648 -1.478427  0.524988
2000-01-07  0.404705  0.577046 -1.715002 -1.039268
2000-01-08 -0.370647 -1.157892 -1.344312  0.844885

In [7]: df[['B', 'A']] = df[['A', 'B']]

In [8]: df
Out[8]: 
                   A         B         C         D
2000-01-01 -0.282863  0.469112 -1.509059 -1.135632
2000-01-02 -0.173215  1.212112  0.119209 -1.044236
2000-01-03 -2.104569 -0.861849 -0.494929  1.071804
2000-01-04 -0.706771  0.721555 -1.039575  0.271860
2000-01-05  0.567020 -0.424972  0.276232 -1.087401
2000-01-06  0.113648 -0.673690 -1.478427  0.524988
2000-01-07  0.577046  0.404705 -1.715002 -1.039268
2000-01-08 -1.157892 -0.370647 -1.344312  0.844885
```

이는 열의 일부에 변환(제자리에서)을 적용하는 데 유용할 수 있습니다.

경고

pandas는 .loc에서 Series와 DataFrame을 설정할 때 모든 축을 정렬합니다.

이는 열 정렬이 값 할당 전에 이루어지기

## Attribute access[](https://pandas.pydata.org/docs/user_guide/indexing.html#attribute-access "Link to this heading")

You may access an index on a `Series` or column on a `DataFrame` directly as an attribute:

In [17]: sa = pd.Series([1, 2, 3], index=list('abc'))

In [18]: dfa = df.copy()

In [19]: sa.b
Out[19]: 2

In [20]: dfa.A
Out[20]: 
2000-01-01   -0.282863
2000-01-02   -0.173215
2000-01-03   -2.104569
2000-01-04   -0.706771
2000-01-05    0.567020
2000-01-06    0.113648
2000-01-07    0.577046
2000-01-08   -1.157892
Freq: D, Name: A, dtype: float64

In [21]: sa.a = 5

In [22]: sa
Out[22]: 
a    5
b    2
c    3
dtype: int64

In [23]: dfa.A = list(range(len(dfa.index)))  # ok if A already exists

In [24]: dfa
Out[24]: 
            A         B         C         D
2000-01-01  0  0.469112 -1.509059 -1.135632
2000-01-02  1  1.212112  0.119209 -1.044236
2000-01-03  2 -0.861849 -0.494929  1.071804
2000-01-04  3  0.721555 -1.039575  0.271860
2000-01-05  4 -0.424972  0.276232 -1.087401
2000-01-06  5 -0.673690 -1.478427  0.524988
2000-01-07  6  0.404705 -1.715002 -1.039268
2000-01-08  7 -0.370647 -1.344312  0.844885

In [25]: dfa['A'] = list(range(len(dfa.index)))  # use this form to create a new column

In [26]: dfa
Out[26]: 
            A         B         C         D
2000-01-01  0  0.469112 -1.509059 -1.135632
2000-01-02  1  1.212112  0.119209 -1.044236
2000-01-03  2 -0.861849 -0.494929  1.071804
2000-01-04  3  0.721555 -1.039575  0.271860
2000-01-05  4 -0.424972  0.276232 -1.087401
2000-01-06  5 -0.673690 -1.478427  0.524988
2000-01-07  6  0.404705 -1.715002 -1.039268
2000-01-08  7 -0.370647 -1.344312  0.844885

Warning

- You can use this access only if the index element is a valid Python identifier, e.g. `s.1` is not allowed. See [here for an explanation of valid identifiers](https://docs.python.org/3/reference/lexical_analysis.html#identifiers).
    
- The attribute will not be available if it conflicts with an existing method name, e.g. `s.min` is not allowed, but `s['min']` is possible.
    
- Similarly, the attribute will not be available if it conflicts with any of the following list: `index`, `major_axis`, `minor_axis`, `items`.
    
- In any of these cases, standard indexing will still work, e.g. `s['1']`, `s['min']`, and `s['index']` will access the corresponding element or column.
    

If you are using the IPython environment, you may also use tab-completion to see these accessible attributes.

You can also assign a `dict` to a row of a `DataFrame`:

In [27]: x = pd.DataFrame({'x': [1, 2, 3], 'y': [3, 4, 5]})

In [28]: x.iloc[1] = {'x': 9, 'y': 99}

In [29]: x
Out[29]: 
   x   y
0  1   3
1  9  99
2  3   5

You can use attribute access to modify an existing element of a Series or column of a DataFrame, but be careful; if you try to use attribute access to create a new column, it creates a new attribute rather than a new column and will this raise a `UserWarning`:

In [30]: df_new = pd.DataFrame({'one': [1., 2., 3.]})

In [31]: df_new.two = [4, 5, 6]

In [32]: df_new
Out[32]: 
   one
0  1.0
1  2.0
2  3.0

## Slicing ranges[](https://pandas.pydata.org/docs/user_guide/indexing.html#slicing-ranges "Link to this heading")

The most robust and consistent way of slicing ranges along arbitrary axes is described in the [Selection by Position](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-integer) section detailing the `.iloc` method. For now, we explain the semantics of slicing using the `[]` operator.

With Series, the syntax works exactly as with an ndarray, returning a slice of the values and the corresponding labels:

In [33]: s[:5]
Out[33]: 
2000-01-01    0.469112
2000-01-02    1.212112
2000-01-03   -0.861849
2000-01-04    0.721555
2000-01-05   -0.424972
Freq: D, Name: A, dtype: float64

In [34]: s[::2]
Out[34]: 
2000-01-01    0.469112
2000-01-03   -0.861849
2000-01-05   -0.424972
2000-01-07    0.404705
Freq: 2D, Name: A, dtype: float64

In [35]: s[::-1]
Out[35]: 
2000-01-08   -0.370647
2000-01-07    0.404705
2000-01-06   -0.673690
2000-01-05   -0.424972
2000-01-04    0.721555
2000-01-03   -0.861849
2000-01-02    1.212112
2000-01-01    0.469112
Freq: -1D, Name: A, dtype: float64

Note that setting works as well:

In [36]: s2 = s.copy()

In [37]: s2[:5] = 0

In [38]: s2
Out[38]: 
2000-01-01    0.000000
2000-01-02    0.000000
2000-01-03    0.000000
2000-01-04    0.000000
2000-01-05    0.000000
2000-01-06   -0.673690
2000-01-07    0.404705
2000-01-08   -0.370647
Freq: D, Name: A, dtype: float64

With DataFrame, slicing inside of `[]` **slices the rows**. This is provided largely as a convenience since it is such a common operation.

In [39]: df[:3]
Out[39]: 
                   A         B         C         D
2000-01-01 -0.282863  0.469112 -1.509059 -1.135632
2000-01-02 -0.173215  1.212112  0.119209 -1.044236
2000-01-03 -2.104569 -0.861849 -0.494929  1.071804

In [40]: df[::-1]
Out[40]: 
                   A         B         C         D
2000-01-08 -1.157892 -0.370647 -1.344312  0.844885
2000-01-07  0.577046  0.404705 -1.715002 -1.039268
2000-01-06  0.113648 -0.673690 -1.478427  0.524988
2000-01-05  0.567020 -0.424972  0.276232 -1.087401
2000-01-04 -0.706771  0.721555 -1.039575  0.271860
2000-01-03 -2.104569 -0.861849 -0.494929  1.071804
2000-01-02 -0.173215  1.212112  0.119209 -1.044236
2000-01-01 -0.282863  0.469112 -1.509059 -1.135632

## Selection by label[](https://pandas.pydata.org/docs/user_guide/indexing.html#selection-by-label "Link to this heading")

Warning

Whether a copy or a reference is returned for a setting operation, may depend on the context. This is sometimes called `chained assignment` and should be avoided. See [Returning a View versus Copy](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-view-versus-copy).

Warning

> `.loc` is strict when you present slicers that are not compatible (or convertible) with the index type. For example using integers in a `DatetimeIndex`. These will raise a `TypeError`.
> 
> In [41]: dfl = pd.DataFrame(np.random.randn(5, 4),
>    ....:                   columns=list('ABCD'),
>    ....:                   index=pd.date_range('20130101', periods=5))
>    ....: 
> 
> In [42]: dfl
> Out[42]: 
>                    A         B         C         D
> 2013-01-01  1.075770 -0.109050  1.643563 -1.469388
> 2013-01-02  0.357021 -0.674600 -1.776904 -0.968914
> 2013-01-03 -1.294524  0.413738  0.276662 -0.472035
> 2013-01-04 -0.013960 -0.362543 -0.006154 -0.923061
> 2013-01-05  0.895717  0.805244 -1.206412  2.565646
> 
> In [43]: dfl.loc[2:3]
> ---------------------------------------------------------------------------
> TypeError                                 Traceback (most recent call last)
> Cell In[43], line 1
> ----> 1 dfl.loc[2:3]
> 
> File ~/work/pandas/pandas/pandas/core/indexing.py:1191, in _LocationIndexer.__getitem__(self, key)
>    1189 maybe_callable = com.apply_if_callable(key, self.obj)
>    1190 maybe_callable = self._check_deprecated_callable_usage(key, maybe_callable)
> -> 1191 return self._getitem_axis(maybe_callable, axis=axis)
> 
> File ~/work/pandas/pandas/pandas/core/indexing.py:1411, in _LocIndexer._getitem_axis(self, key, axis)
>    1409 if isinstance(key, slice):
>    1410     self._validate_key(key, axis)
> -> 1411     return self._get_slice_axis(key, axis=axis)
>    1412 elif com.is_bool_indexer(key):
>    1413     return self._getbool_axis(key, axis=axis)
> 
> File ~/work/pandas/pandas/pandas/core/indexing.py:1443, in _LocIndexer._get_slice_axis(self, slice_obj, axis)
>    1440     return obj.copy(deep=False)
>    1442 labels = obj._get_axis(axis)
> -> 1443 indexer = labels.slice_indexer(slice_obj.start, slice_obj.stop, slice_obj.step)
>    1445 if isinstance(indexer, slice):
>    1446     return self.obj._slice(indexer, axis=axis)
> 
> File ~/work/pandas/pandas/pandas/core/indexes/datetimes.py:682, in DatetimeIndex.slice_indexer(self, start, end, step)
>     674 # GH#33146 if start and end are combinations of str and None and Index is not
>     675 # monotonic, we can not use Index.slice_indexer because it does not honor the
>     676 # actual elements, is only searching for start and end
>     677 if (
>     678     check_str_or_none(start)
>     679     or check_str_or_none(end)
>     680     or self.is_monotonic_increasing
>     681 ):
> --> 682     return Index.slice_indexer(self, start, end, step)
>     684 mask = np.array(True)
>     685 in_index = True
> 
> File ~/work/pandas/pandas/pandas/core/indexes/base.py:6662, in Index.slice_indexer(self, start, end, step)
>    6618 def slice_indexer(
>    6619     self,
>    6620     start: Hashable | None = None,
>    6621     end: Hashable | None = None,
>    6622     step: int | None = None,
>    6623 ) -> slice:
>    6624     """
>    6625     Compute the slice indexer for input labels and step.
>    6626 
>    (...)
>    6660     slice(1, 3, None)
>    6661     """
> -> 6662     start_slice, end_slice = self.slice_locs(start, end, step=step)
>    6664     # return a slice
>    6665     if not is_scalar(start_slice):
> 
> File ~/work/pandas/pandas/pandas/core/indexes/base.py:6879, in Index.slice_locs(self, start, end, step)
>    6877 start_slice = None
>    6878 if start is not None:
> -> 6879     start_slice = self.get_slice_bound(start, "left")
>    6880 if start_slice is None:
>    6881     start_slice = 0
> 
> File ~/work/pandas/pandas/pandas/core/indexes/base.py:6794, in Index.get_slice_bound(self, label, side)
>    6790 original_label = label
>    6792 # For datetime indices label may be a string that has to be converted
>    6793 # to datetime boundary according to its resolution.
> -> 6794 label = self._maybe_cast_slice_bound(label, side)
>    6796 # we need to look up the label
>    6797 try:
> 
> File ~/work/pandas/pandas/pandas/core/indexes/datetimes.py:642, in DatetimeIndex._maybe_cast_slice_bound(self, label, side)
>     637 if isinstance(label, dt.date) and not isinstance(label, dt.datetime):
>     638     # Pandas supports slicing with dates, treated as datetimes at midnight.
>     639     # https://github.com/pandas-dev/pandas/issues/31501
>     640     label = Timestamp(label).to_pydatetime()
> --> 642 label = super()._maybe_cast_slice_bound(label, side)
>     643 self._data._assert_tzawareness_compat(label)
>     644 return Timestamp(label)
> 
> File ~/work/pandas/pandas/pandas/core/indexes/datetimelike.py:378, in DatetimeIndexOpsMixin._maybe_cast_slice_bound(self, label, side)
>     376     return lower if side == "left" else upper
>     377 elif not isinstance(label, self._data._recognized_scalars):
> --> 378     self._raise_invalid_indexer("slice", label)
>     380 return label
> 
> File ~/work/pandas/pandas/pandas/core/indexes/base.py:4301, in Index._raise_invalid_indexer(self, form, key, reraise)
>    4299 if reraise is not lib.no_default:
>    4300     raise TypeError(msg) from reraise
> -> 4301 raise TypeError(msg)
> 
> TypeError: cannot do slice indexing on DatetimeIndex with these indexers [2] of type int

String likes in slicing _can_ be convertible to the type of the index and lead to natural slicing.

In [44]: dfl.loc['20130102':'20130104']
Out[44]: 
                   A         B         C         D
2013-01-02  0.357021 -0.674600 -1.776904 -0.968914
2013-01-03 -1.294524  0.413738  0.276662 -0.472035
2013-01-04 -0.013960 -0.362543 -0.006154 -0.923061

pandas provides a suite of methods in order to have **purely label based indexing**. This is a strict inclusion based protocol. Every label asked for must be in the index, or a `KeyError` will be raised. When slicing, both the start bound **AND** the stop bound are _included_, if present in the index. Integers are valid labels, but they refer to the label **and not the position**.

The `.loc` attribute is the primary access method. The following are valid inputs:

- A single label, e.g. `5` or `'a'` (Note that `5` is interpreted as a _label_ of the index. This use is **not** an integer position along the index.).
    
- A list or array of labels `['a', 'b', 'c']`.
    
- A slice object with labels `'a':'f'` (Note that contrary to usual Python slices, **both** the start and the stop are included, when present in the index! See [Slicing with labels](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-slicing-with-labels).
    
- A boolean array.
    
- A `callable`, see [Selection By Callable](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-callable).
    

In [45]: s1 = pd.Series(np.random.randn(6), index=list('abcdef'))

In [46]: s1
Out[46]: 
a    1.431256
b    1.340309
c   -1.170299
d   -0.226169
e    0.410835
f    0.813850
dtype: float64

In [47]: s1.loc['c':]
Out[47]: 
c   -1.170299
d   -0.226169
e    0.410835
f    0.813850
dtype: float64

In [48]: s1.loc['b']
Out[48]: 1.3403088497993827

Note that setting works as well:

In [49]: s1.loc['c':] = 0

In [50]: s1
Out[50]: 
a    1.431256
b    1.340309
c    0.000000
d    0.000000
e    0.000000
f    0.000000
dtype: float64

With a DataFrame:

In [51]: df1 = pd.DataFrame(np.random.randn(6, 4),
   ....:                   index=list('abcdef'),
   ....:                   columns=list('ABCD'))
   ....: 

In [52]: df1
Out[52]: 
          A         B         C         D
a  0.132003 -0.827317 -0.076467 -1.187678
b  1.130127 -1.436737 -1.413681  1.607920
c  1.024180  0.569605  0.875906 -2.211372
d  0.974466 -2.006747 -0.410001 -0.078638
e  0.545952 -1.219217 -1.226825  0.769804
f -1.281247 -0.727707 -0.121306 -0.097883

In [53]: df1.loc[['a', 'b', 'd'], :]
Out[53]: 
          A         B         C         D
a  0.132003 -0.827317 -0.076467 -1.187678
b  1.130127 -1.436737 -1.413681  1.607920
d  0.974466 -2.006747 -0.410001 -0.078638

Accessing via label slices:

In [54]: df1.loc['d':, 'A':'C']
Out[54]: 
          A         B         C
d  0.974466 -2.006747 -0.410001
e  0.545952 -1.219217 -1.226825
f -1.281247 -0.727707 -0.121306

For getting a cross section using a label (equivalent to `df.xs('a')`):

In [55]: df1.loc['a']
Out[55]: 
A    0.132003
B   -0.827317
C   -0.076467
D   -1.187678
Name: a, dtype: float64

For getting values with a boolean array:

In [56]: df1.loc['a'] > 0
Out[56]: 
A     True
B    False
C    False
D    False
Name: a, dtype: bool

In [57]: df1.loc[:, df1.loc['a'] > 0]
Out[57]: 
          A
a  0.132003
b  1.130127
c  1.024180
d  0.974466
e  0.545952
f -1.281247

NA values in a boolean array propagate as `False`:

In [58]: mask = pd.array([True, False, True, False, pd.NA, False], dtype="boolean")

In [59]: mask
Out[59]: 
<BooleanArray>
[True, False, True, False, <NA>, False]
Length: 6, dtype: boolean

In [60]: df1[mask]
Out[60]: 
          A         B         C         D
a  0.132003 -0.827317 -0.076467 -1.187678
c  1.024180  0.569605  0.875906 -2.211372

For getting a value explicitly:

# this is also equivalent to ``df1.at['a','A']``
In [61]: df1.loc['a', 'A']
Out[61]: 0.13200317033032932

### Slicing with labels[](https://pandas.pydata.org/docs/user_guide/indexing.html#slicing-with-labels "Link to this heading")

When using `.loc` with slices, if both the start and the stop labels are present in the index, then elements _located_ between the two (including them) are returned:

In [62]: s = pd.Series(list('abcde'), index=[0, 3, 2, 5, 4])

In [63]: s.loc[3:5]
Out[63]: 
3    b
2    c
5    d
dtype: object

If at least one of the two is absent, but the index is sorted, and can be compared against start and stop labels, then slicing will still work as expected, by selecting labels which _rank_ between the two:

In [64]: s.sort_index()
Out[64]: 
0    a
2    c
3    b
4    e
5    d
dtype: object

In [65]: s.sort_index().loc[1:6]
Out[65]: 
2    c
3    b
4    e
5    d
dtype: object

However, if at least one of the two is absent _and_ the index is not sorted, an error will be raised (since doing otherwise would be computationally expensive, as well as potentially ambiguous for mixed type indexes). For instance, in the above example, `s.loc[1:6]` would raise `KeyError`.

For the rationale behind this behavior, see [Endpoints are inclusive](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced-endpoints-are-inclusive).

In [66]: s = pd.Series(list('abcdef'), index=[0, 3, 2, 5, 4, 2])

In [67]: s.loc[3:5]
Out[67]: 
3    b
2    c
5    d
dtype: object

Also, if the index has duplicate labels _and_ either the start or the stop label is duplicated, an error will be raised. For instance, in the above example, `s.loc[2:5]` would raise a `KeyError`.

For more information about duplicate labels, see [Duplicate Labels](https://pandas.pydata.org/docs/user_guide/duplicates.html#duplicates).

## Selection by position[](https://pandas.pydata.org/docs/user_guide/indexing.html#selection-by-position "Link to this heading")

Warning

Whether a copy or a reference is returned for a setting operation, may depend on the context. This is sometimes called `chained assignment` and should be avoided. See [Returning a View versus Copy](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-view-versus-copy).

pandas provides a suite of methods in order to get **purely integer based indexing**. The semantics follow closely Python and NumPy slicing. These are `0-based` indexing. When slicing, the start bound is _included_, while the upper bound is _excluded_. Trying to use a non-integer, even a **valid** label will raise an `IndexError`.

The `.iloc` attribute is the primary access method. The following are valid inputs:

- An integer e.g. `5`.
    
- A list or array of integers `[4, 3, 0]`.
    
- A slice object with ints `1:7`.
    
- A boolean array.
    
- A `callable`, see [Selection By Callable](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-callable).
    
- A tuple of row (and column) indexes, whose elements are one of the above types.
    

In [68]: s1 = pd.Series(np.random.randn(5), index=list(range(0, 10, 2)))

In [69]: s1
Out[69]: 
0    0.695775
2    0.341734
4    0.959726
6   -1.110336
8   -0.619976
dtype: float64

In [70]: s1.iloc[:3]
Out[70]: 
0    0.695775
2    0.341734
4    0.959726
dtype: float64

In [71]: s1.iloc[3]
Out[71]: -1.110336102891167

Note that setting works as well:

In [72]: s1.iloc[:3] = 0

In [73]: s1
Out[73]: 
0    0.000000
2    0.000000
4    0.000000
6   -1.110336
8   -0.619976
dtype: float64

With a DataFrame:

In [74]: df1 = pd.DataFrame(np.random.randn(6, 4),
   ....:                   index=list(range(0, 12, 2)),
   ....:                   columns=list(range(0, 8, 2)))
   ....: 

In [75]: df1
Out[75]: 
           0         2         4         6
0   0.149748 -0.732339  0.687738  0.176444
2   0.403310 -0.154951  0.301624 -2.179861
4  -1.369849 -0.954208  1.462696 -1.743161
6  -0.826591 -0.345352  1.314232  0.690579
8   0.995761  2.396780  0.014871  3.357427
10 -0.317441 -1.236269  0.896171 -0.487602

Select via integer slicing:

In [76]: df1.iloc[:3]
Out[76]: 
          0         2         4         6
0  0.149748 -0.732339  0.687738  0.176444
2  0.403310 -0.154951  0.301624 -2.179861
4 -1.369849 -0.954208  1.462696 -1.743161

In [77]: df1.iloc[1:5, 2:4]
Out[77]: 
          4         6
2  0.301624 -2.179861
4  1.462696 -1.743161
6  1.314232  0.690579
8  0.014871  3.357427

Select via integer list:

In [78]: df1.iloc[[1, 3, 5], [1, 3]]
Out[78]: 
           2         6
2  -0.154951 -2.179861
6  -0.345352  0.690579
10 -1.236269 -0.487602

In [79]: df1.iloc[1:3, :]
Out[79]: 
          0         2         4         6
2  0.403310 -0.154951  0.301624 -2.179861
4 -1.369849 -0.954208  1.462696 -1.743161

In [80]: df1.iloc[:, 1:3]
Out[80]: 
           2         4
0  -0.732339  0.687738
2  -0.154951  0.301624
4  -0.954208  1.462696
6  -0.345352  1.314232
8   2.396780  0.014871
10 -1.236269  0.896171

# this is also equivalent to ``df1.iat[1,1]``
In [81]: df1.iloc[1, 1]
Out[81]: -0.1549507744249032

For getting a cross section using an integer position (equiv to `df.xs(1)`):

In [82]: df1.iloc[1]
Out[82]: 
0    0.403310
2   -0.154951
4    0.301624
6   -2.179861
Name: 2, dtype: float64

Out of range slice indexes are handled gracefully just as in Python/NumPy.

# these are allowed in Python/NumPy.
In [83]: x = list('abcdef')

In [84]: x
Out[84]: ['a', 'b', 'c', 'd', 'e', 'f']

In [85]: x[4:10]
Out[85]: ['e', 'f']

In [86]: x[8:10]
Out[86]: []

In [87]: s = pd.Series(x)

In [88]: s
Out[88]: 
0    a
1    b
2    c
3    d
4    e
5    f
dtype: object

In [89]: s.iloc[4:10]
Out[89]: 
4    e
5    f
dtype: object

In [90]: s.iloc[8:10]
Out[90]: Series([], dtype: object)

Note that using slices that go out of bounds can result in an empty axis (e.g. an empty DataFrame being returned).

In [91]: dfl = pd.DataFrame(np.random.randn(5, 2), columns=list('AB'))

In [92]: dfl
Out[92]: 
          A         B
0 -0.082240 -2.182937
1  0.380396  0.084844
2  0.432390  1.519970
3 -0.493662  0.600178
4  0.274230  0.132885

In [93]: dfl.iloc[:, 2:3]
Out[93]: 
Empty DataFrame
Columns: []
Index: [0, 1, 2, 3, 4]

In [94]: dfl.iloc[:, 1:3]
Out[94]: 
          B
0 -2.182937
1  0.084844
2  1.519970
3  0.600178
4  0.132885

In [95]: dfl.iloc[4:6]
Out[95]: 
         A         B
4  0.27423  0.132885

A single indexer that is out of bounds will raise an `IndexError`. A list of indexers where any element is out of bounds will raise an `IndexError`.

In [96]: dfl.iloc[[4, 5, 6]]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
File ~/work/pandas/pandas/pandas/core/indexing.py:1714, in _iLocIndexer._get_list_axis(self, key, axis)
   1713 try:
-> 1714     return self.obj._take_with_is_copy(key, axis=axis)
   1715 except IndexError as err:
   1716     # re-raise with different error message, e.g. test_getitem_ndarray_3d

File ~/work/pandas/pandas/pandas/core/generic.py:4153, in NDFrame._take_with_is_copy(self, indices, axis)
   4144 """
   4145 Internal version of the `take` method that sets the `_is_copy`
   4146 attribute to keep track of the parent dataframe (using in indexing
   (...)
   4151 See the docstring of `take` for full explanation of the parameters.
   4152 """
-> 4153 result = self.take(indices=indices, axis=axis)
   4154 # Maybe set copy if we didn't actually change the index.

File ~/work/pandas/pandas/pandas/core/generic.py:4133, in NDFrame.take(self, indices, axis, **kwargs)
   4129     indices = np.arange(
   4130         indices.start, indices.stop, indices.step, dtype=np.intp
   4131     )
-> 4133 new_data = self._mgr.take(
   4134     indices,
   4135     axis=self._get_block_manager_axis(axis),
   4136     verify=True,
   4137 )
   4138 return self._constructor_from_mgr(new_data, axes=new_data.axes).__finalize__(
   4139     self, method="take"
   4140 )

File ~/work/pandas/pandas/pandas/core/internals/managers.py:891, in BaseBlockManager.take(self, indexer, axis, verify)
    890 n = self.shape[axis]
--> 891 indexer = maybe_convert_indices(indexer, n, verify=verify)
    893 new_labels = self.axes[axis].take(indexer)

File ~/work/pandas/pandas/pandas/core/indexers/utils.py:282, in maybe_convert_indices(indices, n, verify)
    281     if mask.any():
--> 282         raise IndexError("indices are out-of-bounds")
    283 return indices

IndexError: indices are out-of-bounds

The above exception was the direct cause of the following exception:

IndexError                                Traceback (most recent call last)
Cell In[96], line 1
----> 1 dfl.iloc[[4, 5, 6]]

File ~/work/pandas/pandas/pandas/core/indexing.py:1191, in _LocationIndexer.__getitem__(self, key)
   1189 maybe_callable = com.apply_if_callable(key, self.obj)
   1190 maybe_callable = self._check_deprecated_callable_usage(key, maybe_callable)
-> 1191 return self._getitem_axis(maybe_callable, axis=axis)

File ~/work/pandas/pandas/pandas/core/indexing.py:1743, in _iLocIndexer._getitem_axis(self, key, axis)
   1741 # a list of integers
   1742 elif is_list_like_indexer(key):
-> 1743     return self._get_list_axis(key, axis=axis)
   1745 # a single integer
   1746 else:
   1747     key = item_from_zerodim(key)

File ~/work/pandas/pandas/pandas/core/indexing.py:1717, in _iLocIndexer._get_list_axis(self, key, axis)
   1714     return self.obj._take_with_is_copy(key, axis=axis)
   1715 except IndexError as err:
   1716     # re-raise with different error message, e.g. test_getitem_ndarray_3d
-> 1717     raise IndexError("positional indexers are out-of-bounds") from err

IndexError: positional indexers are out-of-bounds

In [97]: dfl.iloc[:, 4]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[97], line 1
----> 1 dfl.iloc[:, 4]

File ~/work/pandas/pandas/pandas/core/indexing.py:1184, in _LocationIndexer.__getitem__(self, key)
   1182     if self._is_scalar_access(key):
   1183         return self.obj._get_value(*key, takeable=self._takeable)
-> 1184     return self._getitem_tuple(key)
   1185 else:
   1186     # we by definition only have the 0th axis
   1187     axis = self.axis or 0

File ~/work/pandas/pandas/pandas/core/indexing.py:1690, in _iLocIndexer._getitem_tuple(self, tup)
   1689 def _getitem_tuple(self, tup: tuple):
-> 1690     tup = self._validate_tuple_indexer(tup)
   1691     with suppress(IndexingError):
   1692         return self._getitem_lowerdim(tup)

File ~/work/pandas/pandas/pandas/core/indexing.py:966, in _LocationIndexer._validate_tuple_indexer(self, key)
    964 for i, k in enumerate(key):
    965     try:
--> 966         self._validate_key(k, i)
    967     except ValueError as err:
    968         raise ValueError(
    969             "Location based indexing can only have "
    970             f"[{self._valid_types}] types"
    971         ) from err

File ~/work/pandas/pandas/pandas/core/indexing.py:1592, in _iLocIndexer._validate_key(self, key, axis)
   1590     return
   1591 elif is_integer(key):
-> 1592     self._validate_integer(key, axis)
   1593 elif isinstance(key, tuple):
   1594     # a tuple should already have been caught by this point
   1595     # so don't treat a tuple as a valid indexer
   1596     raise IndexingError("Too many indexers")

File ~/work/pandas/pandas/pandas/core/indexing.py:1685, in _iLocIndexer._validate_integer(self, key, axis)
   1683 len_axis = len(self.obj._get_axis(axis))
   1684 if key >= len_axis or key < -len_axis:
-> 1685     raise IndexError("single positional indexer is out-of-bounds")

IndexError: single positional indexer is out-of-bounds

## Selection by callable[](https://pandas.pydata.org/docs/user_guide/indexing.html#selection-by-callable "Link to this heading")

`.loc`, `.iloc`, and also `[]` indexing can accept a `callable` as indexer. The `callable` must be a function with one argument (the calling Series or DataFrame) that returns valid output for indexing.

Note

For `.iloc` indexing, returning a tuple from the callable is not supported, since tuple destructuring for row and column indexes occurs _before_ applying callables.

In [98]: df1 = pd.DataFrame(np.random.randn(6, 4),
   ....:                   index=list('abcdef'),
   ....:                   columns=list('ABCD'))
   ....: 

In [99]: df1
Out[99]: 
          A         B         C         D
a -0.023688  2.410179  1.450520  0.206053
b -0.251905 -2.213588  1.063327  1.266143
c  0.299368 -0.863838  0.408204 -1.048089
d -0.025747 -0.988387  0.094055  1.262731
e  1.289997  0.082423 -0.055758  0.536580
f -0.489682  0.369374 -0.034571 -2.484478

In [100]: df1.loc[lambda df: df['A'] > 0, :]
Out[100]: 
          A         B         C         D
c  0.299368 -0.863838  0.408204 -1.048089
e  1.289997  0.082423 -0.055758  0.536580

In [101]: df1.loc[:, lambda df: ['A', 'B']]
Out[101]: 
          A         B
a -0.023688  2.410179
b -0.251905 -2.213588
c  0.299368 -0.863838
d -0.025747 -0.988387
e  1.289997  0.082423
f -0.489682  0.369374

In [102]: df1.iloc[:, lambda df: [0, 1]]
Out[102]: 
          A         B
a -0.023688  2.410179
b -0.251905 -2.213588
c  0.299368 -0.863838
d -0.025747 -0.988387
e  1.289997  0.082423
f -0.489682  0.369374

In [103]: df1[lambda df: df.columns[0]]
Out[103]: 
a   -0.023688
b   -0.251905
c    0.299368
d   -0.025747
e    1.289997
f   -0.489682
Name: A, dtype: float64

You can use callable indexing in `Series`.

In [104]: df1['A'].loc[lambda s: s > 0]
Out[104]: 
c    0.299368
e    1.289997
Name: A, dtype: float64

Using these methods / indexers, you can chain data selection operations without using a temporary variable.

In [105]: bb = pd.read_csv('data/baseball.csv', index_col='id')

In [106]: (bb.groupby(['year', 'team']).sum(numeric_only=True)
   .....:   .loc[lambda df: df['r'] > 100])
   .....: 
Out[106]: 
           stint    g    ab    r    h  X2b  ...     so   ibb   hbp    sh    sf  gidp
year team                                   ...                                     
2007 CIN       6  379   745  101  203   35  ...  127.0  14.0   1.0   1.0  15.0  18.0
     DET       5  301  1062  162  283   54  ...  176.0   3.0  10.0   4.0   8.0  28.0
     HOU       4  311   926  109  218   47  ...  212.0   3.0   9.0  16.0   6.0  17.0
     LAN      11  413  1021  153  293   61  ...  141.0   8.0   9.0   3.0   8.0  29.0
     NYN      13  622  1854  240  509  101  ...  310.0  24.0  23.0  18.0  15.0  48.0
     SFN       5  482  1305  198  337   67  ...  188.0  51.0   8.0  16.0   6.0  41.0
     TEX       2  198   729  115  200   40  ...  140.0   4.0   5.0   2.0   8.0  16.0
     TOR       4  459  1408  187  378   96  ...  265.0  16.0  12.0   4.0  16.0  38.0

[8 rows x 18 columns]

## Combining positional and label-based indexing[](https://pandas.pydata.org/docs/user_guide/indexing.html#combining-positional-and-label-based-indexing "Link to this heading")

If you wish to get the 0th and the 2nd elements from the index in the ‘A’ column, you can do:

In [107]: dfd = pd.DataFrame({'A': [1, 2, 3],
   .....:                    'B': [4, 5, 6]},
   .....:                   index=list('abc'))
   .....: 

In [108]: dfd
Out[108]: 
   A  B
a  1  4
b  2  5
c  3  6

In [109]: dfd.loc[dfd.index[[0, 2]], 'A']
Out[109]: 
a    1
c    3
Name: A, dtype: int64

This can also be expressed using `.iloc`, by explicitly getting locations on the indexers, and using _positional_ indexing to select things.

In [110]: dfd.iloc[[0, 2], dfd.columns.get_loc('A')]
Out[110]: 
a    1
c    3
Name: A, dtype: int64

For getting _multiple_ indexers, using `.get_indexer`:

In [111]: dfd.iloc[[0, 2], dfd.columns.get_indexer(['A', 'B'])]
Out[111]: 
   A  B
a  1  4
c  3  6

### Reindexing[](https://pandas.pydata.org/docs/user_guide/indexing.html#reindexing "Link to this heading")

The idiomatic way to achieve selecting potentially not-found elements is via `.reindex()`. See also the section on [reindexing](https://pandas.pydata.org/docs/user_guide/basics.html#basics-reindexing).

In [112]: s = pd.Series([1, 2, 3])

In [113]: s.reindex([1, 2, 3])
Out[113]: 
1    2.0
2    3.0
3    NaN
dtype: float64

Alternatively, if you want to select only _valid_ keys, the following is idiomatic and efficient; it is guaranteed to preserve the dtype of the selection.

In [114]: labels = [1, 2, 3]

In [115]: s.loc[s.index.intersection(labels)]
Out[115]: 
1    2
2    3
dtype: int64

Having a duplicated index will raise for a `.reindex()`:

In [116]: s = pd.Series(np.arange(4), index=['a', 'a', 'b', 'c'])

In [117]: labels = ['c', 'd']

In [118]: s.reindex(labels)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[118], line 1
----> 1 s.reindex(labels)

File ~/work/pandas/pandas/pandas/core/series.py:5153, in Series.reindex(self, index, axis, method, copy, level, fill_value, limit, tolerance)
   5136 @doc(
   5137     NDFrame.reindex,  # type: ignore[has-type]
   5138     klass=_shared_doc_kwargs["klass"],
   (...)
   5151     tolerance=None,
   5152 ) -> Series:
-> 5153     return super().reindex(
   5154         index=index,
   5155         method=method,
   5156         copy=copy,
   5157         level=level,
   5158         fill_value=fill_value,
   5159         limit=limit,
   5160         tolerance=tolerance,
   5161     )

File ~/work/pandas/pandas/pandas/core/generic.py:5610, in NDFrame.reindex(self, labels, index, columns, axis, method, copy, level, fill_value, limit, tolerance)
   5607     return self._reindex_multi(axes, copy, fill_value)
   5609 # perform the reindex on the axes
-> 5610 return self._reindex_axes(
   5611     axes, level, limit, tolerance, method, fill_value, copy
   5612 ).__finalize__(self, method="reindex")

File ~/work/pandas/pandas/pandas/core/generic.py:5633, in NDFrame._reindex_axes(self, axes, level, limit, tolerance, method, fill_value, copy)
   5630     continue
   5632 ax = self._get_axis(a)
-> 5633 new_index, indexer = ax.reindex(
   5634     labels, level=level, limit=limit, tolerance=tolerance, method=method
   5635 )
   5637 axis = self._get_axis_number(a)
   5638 obj = obj._reindex_with_indexers(
   5639     {axis: [new_index, indexer]},
   5640     fill_value=fill_value,
   5641     copy=copy,
   5642     allow_dups=False,
   5643 )

File ~/work/pandas/pandas/pandas/core/indexes/base.py:4429, in Index.reindex(self, target, method, level, limit, tolerance)
   4426     raise ValueError("cannot handle a non-unique multi-index!")
   4427 elif not self.is_unique:
   4428     # GH#42568
-> 4429     raise ValueError("cannot reindex on an axis with duplicate labels")
   4430 else:
   4431     indexer, _ = self.get_indexer_non_unique(target)

ValueError: cannot reindex on an axis with duplicate labels

Generally, you can intersect the desired labels with the current axis, and then reindex.

In [119]: s.loc[s.index.intersection(labels)].reindex(labels)
Out[119]: 
c    3.0
d    NaN
dtype: float64

However, this would _still_ raise if your resulting index is duplicated.

In [120]: labels = ['a', 'd']

In [121]: s.loc[s.index.intersection(labels)].reindex(labels)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[121], line 1
----> 1 s.loc[s.index.intersection(labels)].reindex(labels)

File ~/work/pandas/pandas/pandas/core/series.py:5153, in Series.reindex(self, index, axis, method, copy, level, fill_value, limit, tolerance)
   5136 @doc(
   5137     NDFrame.reindex,  # type: ignore[has-type]
   5138     klass=_shared_doc_kwargs["klass"],
   (...)
   5151     tolerance=None,
   5152 ) -> Series:
-> 5153     return super().reindex(
   5154         index=index,
   5155         method=method,
   5156         copy=copy,
   5157         level=level,
   5158         fill_value=fill_value,
   5159         limit=limit,
   5160         tolerance=tolerance,
   5161     )

File ~/work/pandas/pandas/pandas/core/generic.py:5610, in NDFrame.reindex(self, labels, index, columns, axis, method, copy, level, fill_value, limit, tolerance)
   5607     return self._reindex_multi(axes, copy, fill_value)
   5609 # perform the reindex on the axes
-> 5610 return self._reindex_axes(
   5611     axes, level, limit, tolerance, method, fill_value, copy
   5612 ).__finalize__(self, method="reindex")

File ~/work/pandas/pandas/pandas/core/generic.py:5633, in NDFrame._reindex_axes(self, axes, level, limit, tolerance, method, fill_value, copy)
   5630     continue
   5632 ax = self._get_axis(a)
-> 5633 new_index, indexer = ax.reindex(
   5634     labels, level=level, limit=limit, tolerance=tolerance, method=method
   5635 )
   5637 axis = self._get_axis_number(a)
   5638 obj = obj._reindex_with_indexers(
   5639     {axis: [new_index, indexer]},
   5640     fill_value=fill_value,
   5641     copy=copy,
   5642     allow_dups=False,
   5643 )

File ~/work/pandas/pandas/pandas/core/indexes/base.py:4429, in Index.reindex(self, target, method, level, limit, tolerance)
   4426     raise ValueError("cannot handle a non-unique multi-index!")
   4427 elif not self.is_unique:
   4428     # GH#42568
-> 4429     raise ValueError("cannot reindex on an axis with duplicate labels")
   4430 else:
   4431     indexer, _ = self.get_indexer_non_unique(target)

ValueError: cannot reindex on an axis with duplicate labels

## Selecting random samples[](https://pandas.pydata.org/docs/user_guide/indexing.html#selecting-random-samples "Link to this heading")

A random selection of rows or columns from a Series or DataFrame with the [`sample()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html#pandas.DataFrame.sample "pandas.DataFrame.sample") method. The method will sample rows by default, and accepts a specific number of rows/columns to return, or a fraction of rows.

In [122]: s = pd.Series([0, 1, 2, 3, 4, 5])

# When no arguments are passed, returns 1 row.
In [123]: s.sample()
Out[123]: 
4    4
dtype: int64

# One may specify either a number of rows:
In [124]: s.sample(n=3)
Out[124]: 
0    0
4    4
1    1
dtype: int64

# Or a fraction of the rows:
In [125]: s.sample(frac=0.5)
Out[125]: 
5    5
3    3
1    1
dtype: int64

By default, `sample` will return each row at most once, but one can also sample with replacement using the `replace` option:

In [126]: s = pd.Series([0, 1, 2, 3, 4, 5])

# Without replacement (default):
In [127]: s.sample(n=6, replace=False)
Out[127]: 
0    0
1    1
5    5
3    3
2    2
4    4
dtype: int64

# With replacement:
In [128]: s.sample(n=6, replace=True)
Out[128]: 
0    0
4    4
3    3
2    2
4    4
4    4
dtype: int64

By default, each row has an equal probability of being selected, but if you want rows to have different probabilities, you can pass the `sample` function sampling weights as `weights`. These weights can be a list, a NumPy array, or a Series, but they must be of the same length as the object you are sampling. Missing values will be treated as a weight of zero, and inf values are not allowed. If weights do not sum to 1, they will be re-normalized by dividing all weights by the sum of the weights. For example:

In [129]: s = pd.Series([0, 1, 2, 3, 4, 5])

In [130]: example_weights = [0, 0, 0.2, 0.2, 0.2, 0.4]

In [131]: s.sample(n=3, weights=example_weights)
Out[131]: 
5    5
4    4
3    3
dtype: int64

# Weights will be re-normalized automatically
In [132]: example_weights2 = [0.5, 0, 0, 0, 0, 0]

In [133]: s.sample(n=1, weights=example_weights2)
Out[133]: 
0    0
dtype: int64

When applied to a DataFrame, you can use a column of the DataFrame as sampling weights (provided you are sampling rows and not columns) by simply passing the name of the column as a string.

In [134]: df2 = pd.DataFrame({'col1': [9, 8, 7, 6],
   .....:                    'weight_column': [0.5, 0.4, 0.1, 0]})
   .....: 

In [135]: df2.sample(n=3, weights='weight_column')
Out[135]: 
   col1  weight_column
1     8            0.4
0     9            0.5
2     7            0.1

`sample` also allows users to sample columns instead of rows using the `axis` argument.

In [136]: df3 = pd.DataFrame({'col1': [1, 2, 3], 'col2': [2, 3, 4]})

In [137]: df3.sample(n=1, axis=1)
Out[137]: 
   col1
0     1
1     2
2     3

Finally, one can also set a seed for `sample`’s random number generator using the `random_state` argument, which will accept either an integer (as a seed) or a NumPy RandomState object.

In [138]: df4 = pd.DataFrame({'col1': [1, 2, 3], 'col2': [2, 3, 4]})

# With a given seed, the sample will always draw the same rows.
In [139]: df4.sample(n=2, random_state=2)
Out[139]: 
   col1  col2
2     3     4
1     2     3

In [140]: df4.sample(n=2, random_state=2)
Out[140]: 
   col1  col2
2     3     4
1     2     3

## Setting with enlargement[](https://pandas.pydata.org/docs/user_guide/indexing.html#setting-with-enlargement "Link to this heading")

The `.loc/[]` operations can perform enlargement when setting a non-existent key for that axis.

In the `Series` case this is effectively an appending operation.

In [141]: se = pd.Series([1, 2, 3])

In [142]: se
Out[142]: 
0    1
1    2
2    3
dtype: int64

In [143]: se[5] = 5.

In [144]: se
Out[144]: 
0    1.0
1    2.0
2    3.0
5    5.0
dtype: float64

A `DataFrame` can be enlarged on either axis via `.loc`.

In [145]: dfi = pd.DataFrame(np.arange(6).reshape(3, 2),
   .....:                   columns=['A', 'B'])
   .....: 

In [146]: dfi
Out[146]: 
   A  B
0  0  1
1  2  3
2  4  5

In [147]: dfi.loc[:, 'C'] = dfi.loc[:, 'A']

In [148]: dfi
Out[148]: 
   A  B  C
0  0  1  0
1  2  3  2
2  4  5  4

This is like an `append` operation on the `DataFrame`.

In [149]: dfi.loc[3] = 5

In [150]: dfi
Out[150]: 
   A  B  C
0  0  1  0
1  2  3  2
2  4  5  4
3  5  5  5

## Fast scalar value getting and setting[](https://pandas.pydata.org/docs/user_guide/indexing.html#fast-scalar-value-getting-and-setting "Link to this heading")

Since indexing with `[]` must handle a lot of cases (single-label access, slicing, boolean indexing, etc.), it has a bit of overhead in order to figure out what you’re asking for. If you only want to access a scalar value, the fastest way is to use the `at` and `iat` methods, which are implemented on all of the data structures.

Similarly to `loc`, `at` provides **label** based scalar lookups, while, `iat` provides **integer** based lookups analogously to `iloc`

In [151]: s.iat[5]
Out[151]: 5

In [152]: df.at[dates[5], 'A']
Out[152]: 0.1136484096888855

In [153]: df.iat[3, 0]
Out[153]: -0.7067711336300845

You can also set using these same indexers.

In [154]: df.at[dates[5], 'E'] = 7

In [155]: df.iat[3, 0] = 7

`at` may enlarge the object in-place as above if the indexer is missing.

In [156]: df.at[dates[-1] + pd.Timedelta('1 day'), 0] = 7

In [157]: df
Out[157]: 
                   A         B         C         D    E    0
2000-01-01 -0.282863  0.469112 -1.509059 -1.135632  NaN  NaN
2000-01-02 -0.173215  1.212112  0.119209 -1.044236  NaN  NaN
2000-01-03 -2.104569 -0.861849 -0.494929  1.071804  NaN  NaN
2000-01-04  7.000000  0.721555 -1.039575  0.271860  NaN  NaN
2000-01-05  0.567020 -0.424972  0.276232 -1.087401  NaN  NaN
2000-01-06  0.113648 -0.673690 -1.478427  0.524988  7.0  NaN
2000-01-07  0.577046  0.404705 -1.715002 -1.039268  NaN  NaN
2000-01-08 -1.157892 -0.370647 -1.344312  0.844885  NaN  NaN
2000-01-09       NaN       NaN       NaN       NaN  NaN  7.0

## Boolean indexing[](https://pandas.pydata.org/docs/user_guide/indexing.html#boolean-indexing "Link to this heading")

Another common operation is the use of boolean vectors to filter the data. The operators are: `|` for `or`, `&` for `and`, and `~` for `not`. These **must** be grouped by using parentheses, since by default Python will evaluate an expression such as `df['A'] > 2 & df['B'] < 3` as `df['A'] > (2 & df['B']) < 3`, while the desired evaluation order is `(df['A'] > 2) & (df['B'] < 3)`.

Using a boolean vector to index a Series works exactly as in a NumPy ndarray:

In [158]: s = pd.Series(range(-3, 4))

In [159]: s
Out[159]: 
0   -3
1   -2
2   -1
3    0
4    1
5    2
6    3
dtype: int64

In [160]: s[s > 0]
Out[160]: 
4    1
5    2
6    3
dtype: int64

In [161]: s[(s < -1) | (s > 0.5)]
Out[161]: 
0   -3
1   -2
4    1
5    2
6    3
dtype: int64

In [162]: s[~(s < 0)]
Out[162]: 
3    0
4    1
5    2
6    3
dtype: int64

You may select rows from a DataFrame using a boolean vector the same length as the DataFrame’s index (for example, something derived from one of the columns of the DataFrame):

In [163]: df[df['A'] > 0]
Out[163]: 
                   A         B         C         D    E   0
2000-01-04  7.000000  0.721555 -1.039575  0.271860  NaN NaN
2000-01-05  0.567020 -0.424972  0.276232 -1.087401  NaN NaN
2000-01-06  0.113648 -0.673690 -1.478427  0.524988  7.0 NaN
2000-01-07  0.577046  0.404705 -1.715002 -1.039268  NaN NaN

List comprehensions and the `map` method of Series can also be used to produce more complex criteria:

In [164]: df2 = pd.DataFrame({'a': ['one', 'one', 'two', 'three', 'two', 'one', 'six'],
   .....:                    'b': ['x', 'y', 'y', 'x', 'y', 'x', 'x'],
   .....:                    'c': np.random.randn(7)})
   .....: 

# only want 'two' or 'three'
In [165]: criterion = df2['a'].map(lambda x: x.startswith('t'))

In [166]: df2[criterion]
Out[166]: 
       a  b         c
2    two  y  0.041290
3  three  x  0.361719
4    two  y -0.238075

# equivalent but slower
In [167]: df2[[x.startswith('t') for x in df2['a']]]
Out[167]: 
       a  b         c
2    two  y  0.041290
3  three  x  0.361719
4    two  y -0.238075

# Multiple criteria
In [168]: df2[criterion & (df2['b'] == 'x')]
Out[168]: 
       a  b         c
3  three  x  0.361719

With the choice methods [Selection by Label](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-label), [Selection by Position](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-integer), and [Advanced Indexing](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced) you may select along more than one axis using boolean vectors combined with other indexing expressions.

In [169]: df2.loc[criterion & (df2['b'] == 'x'), 'b':'c']
Out[169]: 
   b         c
3  x  0.361719

Warning

`iloc` supports two kinds of boolean indexing. If the indexer is a boolean `Series`, an error will be raised. For instance, in the following example, `df.iloc[s.values, 1]` is ok. The boolean indexer is an array. But `df.iloc[s, 1]` would raise `ValueError`.

In [170]: df = pd.DataFrame([[1, 2], [3, 4], [5, 6]],
   .....:                  index=list('abc'),
   .....:                  columns=['A', 'B'])
   .....: 

In [171]: s = (df['A'] > 2)

In [172]: s
Out[172]: 
a    False
b     True
c     True
Name: A, dtype: bool

In [173]: df.loc[s, 'B']
Out[173]: 
b    4
c    6
Name: B, dtype: int64

In [174]: df.iloc[s.values, 1]
Out[174]: 
b    4
c    6
Name: B, dtype: int64

## Indexing with isin[](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-with-isin "Link to this heading")

Consider the [`isin()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html#pandas.Series.isin "pandas.Series.isin") method of `Series`, which returns a boolean vector that is true wherever the `Series` elements exist in the passed list. This allows you to select rows where one or more columns have values you want:

In [175]: s = pd.Series(np.arange(5), index=np.arange(5)[::-1], dtype='int64')

In [176]: s
Out[176]: 
4    0
3    1
2    2
1    3
0    4
dtype: int64

In [177]: s.isin([2, 4, 6])
Out[177]: 
4    False
3    False
2     True
1    False
0     True
dtype: bool

In [178]: s[s.isin([2, 4, 6])]
Out[178]: 
2    2
0    4
dtype: int64

The same method is available for `Index` objects and is useful for the cases when you don’t know which of the sought labels are in fact present:

In [179]: s[s.index.isin([2, 4, 6])]
Out[179]: 
4    0
2    2
dtype: int64

# compare it to the following
In [180]: s.reindex([2, 4, 6])
Out[180]: 
2    2.0
4    0.0
6    NaN
dtype: float64

In addition to that, `MultiIndex` allows selecting a separate level to use in the membership check:

In [181]: s_mi = pd.Series(np.arange(6),
   .....:                 index=pd.MultiIndex.from_product([[0, 1], ['a', 'b', 'c']]))
   .....: 

In [182]: s_mi
Out[182]: 
0  a    0
   b    1
   c    2
1  a    3
   b    4
   c    5
dtype: int64

In [183]: s_mi.iloc[s_mi.index.isin([(1, 'a'), (2, 'b'), (0, 'c')])]
Out[183]: 
0  c    2
1  a    3
dtype: int64

In [184]: s_mi.iloc[s_mi.index.isin(['a', 'c', 'e'], level=1)]
Out[184]: 
0  a    0
   c    2
1  a    3
   c    5
dtype: int64

DataFrame also has an [`isin()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isin.html#pandas.DataFrame.isin "pandas.DataFrame.isin") method. When calling `isin`, pass a set of values as either an array or dict. If values is an array, `isin` returns a DataFrame of booleans that is the same shape as the original DataFrame, with True wherever the element is in the sequence of values.

In [185]: df = pd.DataFrame({'vals': [1, 2, 3, 4], 'ids': ['a', 'b', 'f', 'n'],
   .....:                   'ids2': ['a', 'n', 'c', 'n']})
   .....: 

In [186]: values = ['a', 'b', 1, 3]

In [187]: df.isin(values)
Out[187]: 
    vals    ids   ids2
0   True   True   True
1  False   True  False
2   True  False  False
3  False  False  False

Oftentimes you’ll want to match certain values with certain columns. Just make values a `dict` where the key is the column, and the value is a list of items you want to check for.

In [188]: values = {'ids': ['a', 'b'], 'vals': [1, 3]}

In [189]: df.isin(values)
Out[189]: 
    vals    ids   ids2
0   True   True  False
1  False   True  False
2   True  False  False
3  False  False  False

To return the DataFrame of booleans where the values are _not_ in the original DataFrame, use the `~` operator:

In [190]: values = {'ids': ['a', 'b'], 'vals': [1, 3]}

In [191]: ~df.isin(values)
Out[191]: 
    vals    ids  ids2
0  False  False  True
1   True  False  True
2  False   True  True
3   True   True  True

Combine DataFrame’s `isin` with the `any()` and `all()` methods to quickly select subsets of your data that meet a given criteria. To select a row where each column meets its own criterion:

In [192]: values = {'ids': ['a', 'b'], 'ids2': ['a', 'c'], 'vals': [1, 3]}

In [193]: row_mask = df.isin(values).all(1)

In [194]: df[row_mask]
Out[194]: 
   vals ids ids2
0     1   a    a

## The [`where()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.where.html#pandas.DataFrame.where "pandas.DataFrame.where") Method and Masking[](https://pandas.pydata.org/docs/user_guide/indexing.html#the-where-method-and-masking "Link to this heading")

Selecting values from a Series with a boolean vector generally returns a subset of the data. To guarantee that selection output has the same shape as the original data, you can use the `where` method in `Series` and `DataFrame`.

To return only the selected rows:

In [195]: s[s > 0]
Out[195]: 
3    1
2    2
1    3
0    4
dtype: int64

To return a Series of the same shape as the original:

In [196]: s.where(s > 0)
Out[196]: 
4    NaN
3    1.0
2    2.0
1    3.0
0    4.0
dtype: float64

Selecting values from a DataFrame with a boolean criterion now also preserves input data shape. `where` is used under the hood as the implementation. The code below is equivalent to `df.where(df < 0)`.

In [197]: dates = pd.date_range('1/1/2000', periods=8)

In [198]: df = pd.DataFrame(np.random.randn(8, 4),
   .....:                  index=dates, columns=['A', 'B', 'C', 'D'])
   .....: 

In [199]: df[df < 0]
Out[199]: 
                   A         B         C         D
2000-01-01 -2.104139 -1.309525       NaN       NaN
2000-01-02 -0.352480       NaN -1.192319       NaN
2000-01-03 -0.864883       NaN -0.227870       NaN
2000-01-04       NaN -1.222082       NaN -1.233203
2000-01-05       NaN -0.605656 -1.169184       NaN
2000-01-06       NaN -0.948458       NaN -0.684718
2000-01-07 -2.670153 -0.114722       NaN -0.048048
2000-01-08       NaN       NaN -0.048788 -0.808838

In addition, `where` takes an optional `other` argument for replacement of values where the condition is False, in the returned copy.

In [200]: df.where(df < 0, -df)
Out[200]: 
                   A         B         C         D
2000-01-01 -2.104139 -1.309525 -0.485855 -0.245166
2000-01-02 -0.352480 -0.390389 -1.192319 -1.655824
2000-01-03 -0.864883 -0.299674 -0.227870 -0.281059
2000-01-04 -0.846958 -1.222082 -0.600705 -1.233203
2000-01-05 -0.669692 -0.605656 -1.169184 -0.342416
2000-01-06 -0.868584 -0.948458 -2.297780 -0.684718
2000-01-07 -2.670153 -0.114722 -0.168904 -0.048048
2000-01-08 -0.801196 -1.392071 -0.048788 -0.808838

You may wish to set values based on some boolean criteria. This can be done intuitively like so:

In [201]: s2 = s.copy()

In [202]: s2[s2 < 0] = 0

In [203]: s2
Out[203]: 
4    0
3    1
2    2
1    3
0    4
dtype: int64

In [204]: df2 = df.copy()

In [205]: df2[df2 < 0] = 0

In [206]: df2
Out[206]: 
                   A         B         C         D
2000-01-01  0.000000  0.000000  0.485855  0.245166
2000-01-02  0.000000  0.390389  0.000000  1.655824
2000-01-03  0.000000  0.299674  0.000000  0.281059
2000-01-04  0.846958  0.000000  0.600705  0.000000
2000-01-05  0.669692  0.000000  0.000000  0.342416
2000-01-06  0.868584  0.000000  2.297780  0.000000
2000-01-07  0.000000  0.000000  0.168904  0.000000
2000-01-08  0.801196  1.392071  0.000000  0.000000

`where` returns a modified copy of the data.

Note

The signature for [`DataFrame.where()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.where.html#pandas.DataFrame.where "pandas.DataFrame.where") differs from [`numpy.where()`](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where "(in NumPy v1.26)"). Roughly `df1.where(m, df2)` is equivalent to `np.where(m, df1, df2)`.

In [207]: df.where(df < 0, -df) == np.where(df < 0, df, -df)
Out[207]: 
               A     B     C     D
2000-01-01  True  True  True  True
2000-01-02  True  True  True  True
2000-01-03  True  True  True  True
2000-01-04  True  True  True  True
2000-01-05  True  True  True  True
2000-01-06  True  True  True  True
2000-01-07  True  True  True  True
2000-01-08  True  True  True  True

**Alignment**

Furthermore, `where` aligns the input boolean condition (ndarray or DataFrame), such that partial selection with setting is possible. This is analogous to partial setting via `.loc` (but on the contents rather than the axis labels).

In [208]: df2 = df.copy()

In [209]: df2[df2[1:4] > 0] = 3

In [210]: df2
Out[210]: 
                   A         B         C         D
2000-01-01 -2.104139 -1.309525  0.485855  0.245166
2000-01-02 -0.352480  3.000000 -1.192319  3.000000
2000-01-03 -0.864883  3.000000 -0.227870  3.000000
2000-01-04  3.000000 -1.222082  3.000000 -1.233203
2000-01-05  0.669692 -0.605656 -1.169184  0.342416
2000-01-06  0.868584 -0.948458  2.297780 -0.684718
2000-01-07 -2.670153 -0.114722  0.168904 -0.048048
2000-01-08  0.801196  1.392071 -0.048788 -0.808838

Where can also accept `axis` and `level` parameters to align the input when performing the `where`.

In [211]: df2 = df.copy()

In [212]: df2.where(df2 > 0, df2['A'], axis='index')
Out[212]: 
                   A         B         C         D
2000-01-01 -2.104139 -2.104139  0.485855  0.245166
2000-01-02 -0.352480  0.390389 -0.352480  1.655824
2000-01-03 -0.864883  0.299674 -0.864883  0.281059
2000-01-04  0.846958  0.846958  0.600705  0.846958
2000-01-05  0.669692  0.669692  0.669692  0.342416
2000-01-06  0.868584  0.868584  2.297780  0.868584
2000-01-07 -2.670153 -2.670153  0.168904 -2.670153
2000-01-08  0.801196  1.392071  0.801196  0.801196

This is equivalent to (but faster than) the following.

In [213]: df2 = df.copy()

In [214]: df.apply(lambda x, y: x.where(x > 0, y), y=df['A'])
Out[214]: 
                   A         B         C         D
2000-01-01 -2.104139 -2.104139  0.485855  0.245166
2000-01-02 -0.352480  0.390389 -0.352480  1.655824
2000-01-03 -0.864883  0.299674 -0.864883  0.281059
2000-01-04  0.846958  0.846958  0.600705  0.846958
2000-01-05  0.669692  0.669692  0.669692  0.342416
2000-01-06  0.868584  0.868584  2.297780  0.868584
2000-01-07 -2.670153 -2.670153  0.168904 -2.670153
2000-01-08  0.801196  1.392071  0.801196  0.801196

`where` can accept a callable as condition and `other` arguments. The function must be with one argument (the calling Series or DataFrame) and that returns valid output as condition and `other` argument.

In [215]: df3 = pd.DataFrame({'A': [1, 2, 3],
   .....:                    'B': [4, 5, 6],
   .....:                    'C': [7, 8, 9]})
   .....: 

In [216]: df3.where(lambda x: x > 4, lambda x: x + 10)
Out[216]: 
    A   B  C
0  11  14  7
1  12   5  8
2  13   6  9

### Mask[](https://pandas.pydata.org/docs/user_guide/indexing.html#mask "Link to this heading")

[`mask()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mask.html#pandas.DataFrame.mask "pandas.DataFrame.mask") is the inverse boolean operation of `where`.

In [217]: s.mask(s >= 0)
Out[217]: 
4   NaN
3   NaN
2   NaN
1   NaN
0   NaN
dtype: float64

In [218]: df.mask(df >= 0)
Out[218]: 
                   A         B         C         D
2000-01-01 -2.104139 -1.309525       NaN       NaN
2000-01-02 -0.352480       NaN -1.192319       NaN
2000-01-03 -0.864883       NaN -0.227870       NaN
2000-01-04       NaN -1.222082       NaN -1.233203
2000-01-05       NaN -0.605656 -1.169184       NaN
2000-01-06       NaN -0.948458       NaN -0.684718
2000-01-07 -2.670153 -0.114722       NaN -0.048048
2000-01-08       NaN       NaN -0.048788 -0.808838

## Setting with enlargement conditionally using `numpy()`[](https://pandas.pydata.org/docs/user_guide/indexing.html#setting-with-enlargement-conditionally-using-numpy "Link to this heading")

An alternative to [`where()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.where.html#pandas.DataFrame.where "pandas.DataFrame.where") is to use [`numpy.where()`](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where "(in NumPy v1.26)"). Combined with setting a new column, you can use it to enlarge a DataFrame where the values are determined conditionally.

Consider you have two choices to choose from in the following DataFrame. And you want to set a new column color to ‘green’ when the second column has ‘Z’. You can do the following:

In [219]: df = pd.DataFrame({'col1': list('ABBC'), 'col2': list('ZZXY')})

In [220]: df['color'] = np.where(df['col2'] == 'Z', 'green', 'red')

In [221]: df
Out[221]: 
  col1 col2  color
0    A    Z  green
1    B    Z  green
2    B    X    red
3    C    Y    red

If you have multiple conditions, you can use [`numpy.select()`](https://numpy.org/doc/stable/reference/generated/numpy.select.html#numpy.select "(in NumPy v1.26)") to achieve that. Say corresponding to three conditions there are three choice of colors, with a fourth color as a fallback, you can do the following.

In [222]: conditions = [
   .....:    (df['col2'] == 'Z') & (df['col1'] == 'A'),
   .....:    (df['col2'] == 'Z') & (df['col1'] == 'B'),
   .....:    (df['col1'] == 'B')
   .....: ]
   .....: 

In [223]: choices = ['yellow', 'blue', 'purple']

In [224]: df['color'] = np.select(conditions, choices, default='black')

In [225]: df
Out[225]: 
  col1 col2   color
0    A    Z  yellow
1    B    Z    blue
2    B    X  purple
3    C    Y   black

## The [`query()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query "pandas.DataFrame.query") Method[](https://pandas.pydata.org/docs/user_guide/indexing.html#the-query-method "Link to this heading")

[`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") objects have a [`query()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query "pandas.DataFrame.query") method that allows selection using an expression.

You can get the value of the frame where column `b` has values between the values of columns `a` and `c`. For example:

In [226]: n = 10

In [227]: df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))

In [228]: df
Out[228]: 
          a         b         c
0  0.438921  0.118680  0.863670
1  0.138138  0.577363  0.686602
2  0.595307  0.564592  0.520630
3  0.913052  0.926075  0.616184
4  0.078718  0.854477  0.898725
5  0.076404  0.523211  0.591538
6  0.792342  0.216974  0.564056
7  0.397890  0.454131  0.915716
8  0.074315  0.437913  0.019794
9  0.559209  0.502065  0.026437

# pure python
In [229]: df[(df['a'] < df['b']) & (df['b'] < df['c'])]
Out[229]: 
          a         b         c
1  0.138138  0.577363  0.686602
4  0.078718  0.854477  0.898725
5  0.076404  0.523211  0.591538
7  0.397890  0.454131  0.915716

# query
In [230]: df.query('(a < b) & (b < c)')
Out[230]: 
          a         b         c
1  0.138138  0.577363  0.686602
4  0.078718  0.854477  0.898725
5  0.076404  0.523211  0.591538
7  0.397890  0.454131  0.915716

Do the same thing but fall back on a named index if there is no column with the name `a`.

In [231]: df = pd.DataFrame(np.random.randint(n / 2, size=(n, 2)), columns=list('bc'))

In [232]: df.index.name = 'a'

In [233]: df
Out[233]: 
   b  c
a      
0  0  4
1  0  1
2  3  4
3  4  3
4  1  4
5  0  3
6  0  1
7  3  4
8  2  3
9  1  1

In [234]: df.query('a < b and b < c')
Out[234]: 
   b  c
a      
2  3  4

If instead you don’t want to or cannot name your index, you can use the name `index` in your query expression:

In [235]: df = pd.DataFrame(np.random.randint(n, size=(n, 2)), columns=list('bc'))

In [236]: df
Out[236]: 
   b  c
0  3  1
1  3  0
2  5  6
3  5  2
4  7  4
5  0  1
6  2  5
7  0  1
8  6  0
9  7  9

In [237]: df.query('index < b < c')
Out[237]: 
   b  c
2  5  6

Note

If the name of your index overlaps with a column name, the column name is given precedence. For example,

In [238]: df = pd.DataFrame({'a': np.random.randint(5, size=5)})

In [239]: df.index.name = 'a'

In [240]: df.query('a > 2')  # uses the column 'a', not the index
Out[240]: 
   a
a   
1  3
3  3

You can still use the index in a query expression by using the special identifier ‘index’:

In [241]: df.query('index > 2')
Out[241]: 
   a
a   
3  3
4  2

If for some reason you have a column named `index`, then you can refer to the index as `ilevel_0` as well, but at this point you should consider renaming your columns to something less ambiguous.

### [`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex") [`query()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query "pandas.DataFrame.query") Syntax[](https://pandas.pydata.org/docs/user_guide/indexing.html#multiindex-query-syntax "Link to this heading")

You can also use the levels of a `DataFrame` with a [`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex") as if they were columns in the frame:

In [242]: n = 10

In [243]: colors = np.random.choice(['red', 'green'], size=n)

In [244]: foods = np.random.choice(['eggs', 'ham'], size=n)

In [245]: colors
Out[245]: 
array(['red', 'red', 'red', 'green', 'green', 'green', 'green', 'green',
       'green', 'green'], dtype='<U5')

In [246]: foods
Out[246]: 
array(['ham', 'ham', 'eggs', 'eggs', 'eggs', 'ham', 'ham', 'eggs', 'eggs',
       'eggs'], dtype='<U4')

In [247]: index = pd.MultiIndex.from_arrays([colors, foods], names=['color', 'food'])

In [248]: df = pd.DataFrame(np.random.randn(n, 2), index=index)

In [249]: df
Out[249]: 
                   0         1
color food                    
red   ham   0.194889 -0.381994
      ham   0.318587  2.089075
      eggs -0.728293 -0.090255
green eggs -0.748199  1.318931
      eggs -2.029766  0.792652
      ham   0.461007 -0.542749
      ham  -0.305384 -0.479195
      eggs  0.095031 -0.270099
      eggs -0.707140 -0.773882
      eggs  0.229453  0.304418

In [250]: df.query('color == "red"')
Out[250]: 
                   0         1
color food                    
red   ham   0.194889 -0.381994
      ham   0.318587  2.089075
      eggs -0.728293 -0.090255

If the levels of the `MultiIndex` are unnamed, you can refer to them using special names:

In [251]: df.index.names = [None, None]

In [252]: df
Out[252]: 
                   0         1
red   ham   0.194889 -0.381994
      ham   0.318587  2.089075
      eggs -0.728293 -0.090255
green eggs -0.748199  1.318931
      eggs -2.029766  0.792652
      ham   0.461007 -0.542749
      ham  -0.305384 -0.479195
      eggs  0.095031 -0.270099
      eggs -0.707140 -0.773882
      eggs  0.229453  0.304418

In [253]: df.query('ilevel_0 == "red"')
Out[253]: 
                 0         1
red ham   0.194889 -0.381994
    ham   0.318587  2.089075
    eggs -0.728293 -0.090255

The convention is `ilevel_0`, which means “index level 0” for the 0th level of the `index`.

### [`query()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query "pandas.DataFrame.query") Use Cases[](https://pandas.pydata.org/docs/user_guide/indexing.html#query-use-cases "Link to this heading")

A use case for [`query()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query "pandas.DataFrame.query") is when you have a collection of [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") objects that have a subset of column names (or index levels/names) in common. You can pass the same query to both frames _without_ having to specify which frame you’re interested in querying

In [254]: df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))

In [255]: df
Out[255]: 
          a         b         c
0  0.224283  0.736107  0.139168
1  0.302827  0.657803  0.713897
2  0.611185  0.136624  0.984960
3  0.195246  0.123436  0.627712
4  0.618673  0.371660  0.047902
5  0.480088  0.062993  0.185760
6  0.568018  0.483467  0.445289
7  0.309040  0.274580  0.587101
8  0.258993  0.477769  0.370255
9  0.550459  0.840870  0.304611

In [256]: df2 = pd.DataFrame(np.random.rand(n + 2, 3), columns=df.columns)

In [257]: df2
Out[257]: 
           a         b         c
0   0.357579  0.229800  0.596001
1   0.309059  0.957923  0.965663
2   0.123102  0.336914  0.318616
3   0.526506  0.323321  0.860813
4   0.518736  0.486514  0.384724
5   0.190804  0.505723  0.614533
6   0.891939  0.623977  0.676639
7   0.480559  0.378528  0.460858
8   0.420223  0.136404  0.141295
9   0.732206  0.419540  0.604675
10  0.604466  0.848974  0.896165
11  0.589168  0.920046  0.732716

In [258]: expr = '0.0 <= a <= c <= 0.5'

In [259]: map(lambda frame: frame.query(expr), [df, df2])
Out[259]: <map at 0x7ff2e57db2e0>

### [`query()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query "pandas.DataFrame.query") Python versus pandas Syntax Comparison[](https://pandas.pydata.org/docs/user_guide/indexing.html#query-python-versus-pandas-syntax-comparison "Link to this heading")

Full numpy-like syntax:

In [260]: df = pd.DataFrame(np.random.randint(n, size=(n, 3)), columns=list('abc'))

In [261]: df
Out[261]: 
   a  b  c
0  7  8  9
1  1  0  7
2  2  7  2
3  6  2  2
4  2  6  3
5  3  8  2
6  1  7  2
7  5  1  5
8  9  8  0
9  1  5  0

In [262]: df.query('(a < b) & (b < c)')
Out[262]: 
   a  b  c
0  7  8  9

In [263]: df[(df['a'] < df['b']) & (df['b'] < df['c'])]
Out[263]: 
   a  b  c
0  7  8  9

Slightly nicer by removing the parentheses (comparison operators bind tighter than `&` and `|`):

In [264]: df.query('a < b & b < c')
Out[264]: 
   a  b  c
0  7  8  9

Use English instead of symbols:

In [265]: df.query('a < b and b < c')
Out[265]: 
   a  b  c
0  7  8  9

Pretty close to how you might write it on paper:

In [266]: df.query('a < b < c')
Out[266]: 
   a  b  c
0  7  8  9

### The `in` and `not in` operators[](https://pandas.pydata.org/docs/user_guide/indexing.html#the-in-and-not-in-operators "Link to this heading")

[`query()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query "pandas.DataFrame.query") also supports special use of Python’s `in` and `not in` comparison operators, providing a succinct syntax for calling the `isin` method of a `Series` or `DataFrame`.

# get all rows where columns "a" and "b" have overlapping values
In [267]: df = pd.DataFrame({'a': list('aabbccddeeff'), 'b': list('aaaabbbbcccc'),
   .....:                   'c': np.random.randint(5, size=12),
   .....:                   'd': np.random.randint(9, size=12)})
   .....: 

In [268]: df
Out[268]: 
    a  b  c  d
0   a  a  2  6
1   a  a  4  7
2   b  a  1  6
3   b  a  2  1
4   c  b  3  6
5   c  b  0  2
6   d  b  3  3
7   d  b  2  1
8   e  c  4  3
9   e  c  2  0
10  f  c  0  6
11  f  c  1  2

In [269]: df.query('a in b')
Out[269]: 
   a  b  c  d
0  a  a  2  6
1  a  a  4  7
2  b  a  1  6
3  b  a  2  1
4  c  b  3  6
5  c  b  0  2

# How you'd do it in pure Python
In [270]: df[df['a'].isin(df['b'])]
Out[270]: 
   a  b  c  d
0  a  a  2  6
1  a  a  4  7
2  b  a  1  6
3  b  a  2  1
4  c  b  3  6
5  c  b  0  2

In [271]: df.query('a not in b')
Out[271]: 
    a  b  c  d
6   d  b  3  3
7   d  b  2  1
8   e  c  4  3
9   e  c  2  0
10  f  c  0  6
11  f  c  1  2

# pure Python
In [272]: df[~df['a'].isin(df['b'])]
Out[272]: 
    a  b  c  d
6   d  b  3  3
7   d  b  2  1
8   e  c  4  3
9   e  c  2  0
10  f  c  0  6
11  f  c  1  2

You can combine this with other expressions for very succinct queries:

# rows where cols a and b have overlapping values
# and col c's values are less than col d's
In [273]: df.query('a in b and c < d')
Out[273]: 
   a  b  c  d
0  a  a  2  6
1  a  a  4  7
2  b  a  1  6
4  c  b  3  6
5  c  b  0  2

# pure Python
In [274]: df[df['b'].isin(df['a']) & (df['c'] < df['d'])]
Out[274]: 
    a  b  c  d
0   a  a  2  6
1   a  a  4  7
2   b  a  1  6
4   c  b  3  6
5   c  b  0  2
10  f  c  0  6
11  f  c  1  2

Note

Note that `in` and `not in` are evaluated in Python, since `numexpr` has no equivalent of this operation. However, **only the** `in`/`not in` **expression itself** is evaluated in vanilla Python. For example, in the expression

df.query('a in b + c + d')

`(b + c + d)` is evaluated by `numexpr` and _then_ the `in` operation is evaluated in plain Python. In general, any operations that can be evaluated using `numexpr` will be.

### Special use of the `==` operator with `list` objects[](https://pandas.pydata.org/docs/user_guide/indexing.html#special-use-of-the-operator-with-list-objects "Link to this heading")

Comparing a `list` of values to a column using `==`/`!=` works similarly to `in`/`not in`.

In [275]: df.query('b == ["a", "b", "c"]')
Out[275]: 
    a  b  c  d
0   a  a  2  6
1   a  a  4  7
2   b  a  1  6
3   b  a  2  1
4   c  b  3  6
5   c  b  0  2
6   d  b  3  3
7   d  b  2  1
8   e  c  4  3
9   e  c  2  0
10  f  c  0  6
11  f  c  1  2

# pure Python
In [276]: df[df['b'].isin(["a", "b", "c"])]
Out[276]: 
    a  b  c  d
0   a  a  2  6
1   a  a  4  7
2   b  a  1  6
3   b  a  2  1
4   c  b  3  6
5   c  b  0  2
6   d  b  3  3
7   d  b  2  1
8   e  c  4  3
9   e  c  2  0
10  f  c  0  6
11  f  c  1  2

In [277]: df.query('c == [1, 2]')
Out[277]: 
    a  b  c  d
0   a  a  2  6
2   b  a  1  6
3   b  a  2  1
7   d  b  2  1
9   e  c  2  0
11  f  c  1  2

In [278]: df.query('c != [1, 2]')
Out[278]: 
    a  b  c  d
1   a  a  4  7
4   c  b  3  6
5   c  b  0  2
6   d  b  3  3
8   e  c  4  3
10  f  c  0  6

# using in/not in
In [279]: df.query('[1, 2] in c')
Out[279]: 
    a  b  c  d
0   a  a  2  6
2   b  a  1  6
3   b  a  2  1
7   d  b  2  1
9   e  c  2  0
11  f  c  1  2

In [280]: df.query('[1, 2] not in c')
Out[280]: 
    a  b  c  d
1   a  a  4  7
4   c  b  3  6
5   c  b  0  2
6   d  b  3  3
8   e  c  4  3
10  f  c  0  6

# pure Python
In [281]: df[df['c'].isin([1, 2])]
Out[281]: 
    a  b  c  d
0   a  a  2  6
2   b  a  1  6
3   b  a  2  1
7   d  b  2  1
9   e  c  2  0
11  f  c  1  2

### Boolean operators[](https://pandas.pydata.org/docs/user_guide/indexing.html#boolean-operators "Link to this heading")

You can negate boolean expressions with the word `not` or the `~` operator.

In [282]: df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))

In [283]: df['bools'] = np.random.rand(len(df)) > 0.5

In [284]: df.query('~bools')
Out[284]: 
          a         b         c  bools
2  0.697753  0.212799  0.329209  False
7  0.275396  0.691034  0.826619  False
8  0.190649  0.558748  0.262467  False

In [285]: df.query('not bools')
Out[285]: 
          a         b         c  bools
2  0.697753  0.212799  0.329209  False
7  0.275396  0.691034  0.826619  False
8  0.190649  0.558748  0.262467  False

In [286]: df.query('not bools') == df[~df['bools']]
Out[286]: 
      a     b     c  bools
2  True  True  True   True
7  True  True  True   True
8  True  True  True   True

Of course, expressions can be arbitrarily complex too:

# short query syntax
In [287]: shorter = df.query('a < b < c and (not bools) or bools > 2')

# equivalent in pure Python
In [288]: longer = df[(df['a'] < df['b'])
   .....:            & (df['b'] < df['c'])
   .....:            & (~df['bools'])
   .....:            | (df['bools'] > 2)]
   .....: 

In [289]: shorter
Out[289]: 
          a         b         c  bools
7  0.275396  0.691034  0.826619  False

In [290]: longer
Out[290]: 
          a         b         c  bools
7  0.275396  0.691034  0.826619  False

In [291]: shorter == longer
Out[291]: 
      a     b     c  bools
7  True  True  True   True

### Performance of [`query()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query "pandas.DataFrame.query")[](https://pandas.pydata.org/docs/user_guide/indexing.html#performance-of-query "Link to this heading")

`DataFrame.query()` using `numexpr` is slightly faster than Python for large frames.

![../_images/query-perf.png](https://pandas.pydata.org/docs/_images/query-perf.png)

You will only see the performance benefits of using the `numexpr` engine with `DataFrame.query()` if your frame has more than approximately 100,000 rows.

This plot was created using a `DataFrame` with 3 columns each containing floating point values generated using `numpy.random.randn()`.

In [292]: df = pd.DataFrame(np.random.randn(8, 4),
   .....:                  index=dates, columns=['A', 'B', 'C', 'D'])
   .....: 

In [293]: df2 = df.copy()

## Duplicate data[](https://pandas.pydata.org/docs/user_guide/indexing.html#duplicate-data "Link to this heading")

If you want to identify and remove duplicate rows in a DataFrame, there are two methods that will help: `duplicated` and `drop_duplicates`. Each takes as an argument the columns to use to identify duplicated rows.

- `duplicated` returns a boolean vector whose length is the number of rows, and which indicates whether a row is duplicated.
    
- `drop_duplicates` removes duplicate rows.
    

By default, the first observed row of a duplicate set is considered unique, but each method has a `keep` parameter to specify targets to be kept.

- `keep='first'` (default): mark / drop duplicates except for the first occurrence.
    
- `keep='last'`: mark / drop duplicates except for the last occurrence.
    
- `keep=False`: mark / drop all duplicates.
    

In [294]: df2 = pd.DataFrame({'a': ['one', 'one', 'two', 'two', 'two', 'three', 'four'],
   .....:                    'b': ['x', 'y', 'x', 'y', 'x', 'x', 'x'],
   .....:                    'c': np.random.randn(7)})
   .....: 

In [295]: df2
Out[295]: 
       a  b         c
0    one  x -1.067137
1    one  y  0.309500
2    two  x -0.211056
3    two  y -1.842023
4    two  x -0.390820
5  three  x -1.964475
6   four  x  1.298329

In [296]: df2.duplicated('a')
Out[296]: 
0    False
1     True
2    False
3     True
4     True
5    False
6    False
dtype: bool

In [297]: df2.duplicated('a', keep='last')
Out[297]: 
0     True
1    False
2     True
3     True
4    False
5    False
6    False
dtype: bool

In [298]: df2.duplicated('a', keep=False)
Out[298]: 
0     True
1     True
2     True
3     True
4     True
5    False
6    False
dtype: bool

In [299]: df2.drop_duplicates('a')
Out[299]: 
       a  b         c
0    one  x -1.067137
2    two  x -0.211056
5  three  x -1.964475
6   four  x  1.298329

In [300]: df2.drop_duplicates('a', keep='last')
Out[300]: 
       a  b         c
1    one  y  0.309500
4    two  x -0.390820
5  three  x -1.964475
6   four  x  1.298329

In [301]: df2.drop_duplicates('a', keep=False)
Out[301]: 
       a  b         c
5  three  x -1.964475
6   four  x  1.298329

Also, you can pass a list of columns to identify duplications.

In [302]: df2.duplicated(['a', 'b'])
Out[302]: 
0    False
1    False
2    False
3    False
4     True
5    False
6    False
dtype: bool

In [303]: df2.drop_duplicates(['a', 'b'])
Out[303]: 
       a  b         c
0    one  x -1.067137
1    one  y  0.309500
2    two  x -0.211056
3    two  y -1.842023
5  three  x -1.964475
6   four  x  1.298329

To drop duplicates by index value, use `Index.duplicated` then perform slicing. The same set of options are available for the `keep` parameter.

In [304]: df3 = pd.DataFrame({'a': np.arange(6),
   .....:                    'b': np.random.randn(6)},
   .....:                   index=['a', 'a', 'b', 'c', 'b', 'a'])
   .....: 

In [305]: df3
Out[305]: 
   a         b
a  0  1.440455
a  1  2.456086
b  2  1.038402
c  3 -0.894409
b  4  0.683536
a  5  3.082764

In [306]: df3.index.duplicated()
Out[306]: array([False,  True, False, False,  True,  True])

In [307]: df3[~df3.index.duplicated()]
Out[307]: 
   a         b
a  0  1.440455
b  2  1.038402
c  3 -0.894409

In [308]: df3[~df3.index.duplicated(keep='last')]
Out[308]: 
   a         b
c  3 -0.894409
b  4  0.683536
a  5  3.082764

In [309]: df3[~df3.index.duplicated(keep=False)]
Out[309]: 
   a         b
c  3 -0.894409

## Dictionary-like [`get()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.get.html#pandas.DataFrame.get "pandas.DataFrame.get") method[](https://pandas.pydata.org/docs/user_guide/indexing.html#dictionary-like-get-method "Link to this heading")

Each of Series or DataFrame have a `get` method which can return a default value.

In [310]: s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

In [311]: s.get('a')  # equivalent to s['a']
Out[311]: 1

In [312]: s.get('x', default=-1)
Out[312]: -1

## Looking up values by index/column labels[](https://pandas.pydata.org/docs/user_guide/indexing.html#looking-up-values-by-index-column-labels "Link to this heading")

Sometimes you want to extract a set of values given a sequence of row labels and column labels, this can be achieved by `pandas.factorize` and NumPy indexing. For instance:

In [313]: df = pd.DataFrame({'col': ["A", "A", "B", "B"],
   .....:                   'A': [80, 23, np.nan, 22],
   .....:                   'B': [80, 55, 76, 67]})
   .....: 

In [314]: df
Out[314]: 
  col     A   B
0   A  80.0  80
1   A  23.0  55
2   B   NaN  76
3   B  22.0  67

In [315]: idx, cols = pd.factorize(df['col'])

In [316]: df.reindex(cols, axis=1).to_numpy()[np.arange(len(df)), idx]
Out[316]: array([80., 23., 76., 67.])

Formerly this could be achieved with the dedicated `DataFrame.lookup` method which was deprecated in version 1.2.0 and removed in version 2.0.0.

## Index objects[](https://pandas.pydata.org/docs/user_guide/indexing.html#index-objects "Link to this heading")

The pandas [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index") class and its subclasses can be viewed as implementing an _ordered multiset_. Duplicates are allowed.

[`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index") also provides the infrastructure necessary for lookups, data alignment, and reindexing. The easiest way to create an [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index") directly is to pass a `list` or other sequence to [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index"):

In [317]: index = pd.Index(['e', 'd', 'a', 'b'])

In [318]: index
Out[318]: Index(['e', 'd', 'a', 'b'], dtype='object')

In [319]: 'd' in index
Out[319]: True

or using numbers:

In [320]: index = pd.Index([1, 5, 12])

In [321]: index
Out[321]: Index([1, 5, 12], dtype='int64')

In [322]: 5 in index
Out[322]: True

If no dtype is given, `Index` tries to infer the dtype from the data. It is also possible to give an explicit dtype when instantiating an [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index"):

In [323]: index = pd.Index(['e', 'd', 'a', 'b'], dtype="string")

In [324]: index
Out[324]: Index(['e', 'd', 'a', 'b'], dtype='string')

In [325]: index = pd.Index([1, 5, 12], dtype="int8")

In [326]: index
Out[326]: Index([1, 5, 12], dtype='int8')

In [327]: index = pd.Index([1, 5, 12], dtype="float32")

In [328]: index
Out[328]: Index([1.0, 5.0, 12.0], dtype='float32')

You can also pass a `name` to be stored in the index:

In [329]: index = pd.Index(['e', 'd', 'a', 'b'], name='something')

In [330]: index.name
Out[330]: 'something'

The name, if set, will be shown in the console display:

In [331]: index = pd.Index(list(range(5)), name='rows')

In [332]: columns = pd.Index(['A', 'B', 'C'], name='cols')

In [333]: df = pd.DataFrame(np.random.randn(5, 3), index=index, columns=columns)

In [334]: df
Out[334]: 
cols         A         B         C
rows                              
0     1.295989 -1.051694  1.340429
1    -2.366110  0.428241  0.387275
2     0.433306  0.929548  0.278094
3     2.154730 -0.315628  0.264223
4     1.126818  1.132290 -0.353310

In [335]: df['A']
Out[335]: 
rows
0    1.295989
1   -2.366110
2    0.433306
3    2.154730
4    1.126818
Name: A, dtype: float64

### Setting metadata[](https://pandas.pydata.org/docs/user_guide/indexing.html#setting-metadata "Link to this heading")

Indexes are “mostly immutable”, but it is possible to set and change their `name` attribute. You can use the `rename`, `set_names` to set these attributes directly, and they default to returning a copy.

See [Advanced Indexing](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced) for usage of MultiIndexes.

In [336]: ind = pd.Index([1, 2, 3])

In [337]: ind.rename("apple")
Out[337]: Index([1, 2, 3], dtype='int64', name='apple')

In [338]: ind
Out[338]: Index([1, 2, 3], dtype='int64')

In [339]: ind = ind.set_names(["apple"])

In [340]: ind.name = "bob"

In [341]: ind
Out[341]: Index([1, 2, 3], dtype='int64', name='bob')

`set_names`, `set_levels`, and `set_codes` also take an optional `level` argument

In [342]: index = pd.MultiIndex.from_product([range(3), ['one', 'two']], names=['first', 'second'])

In [343]: index
Out[343]: 
MultiIndex([(0, 'one'),
            (0, 'two'),
            (1, 'one'),
            (1, 'two'),
            (2, 'one'),
            (2, 'two')],
           names=['first', 'second'])

In [344]: index.levels[1]
Out[344]: Index(['one', 'two'], dtype='object', name='second')

In [345]: index.set_levels(["a", "b"], level=1)
Out[345]: 
MultiIndex([(0, 'a'),
            (0, 'b'),
            (1, 'a'),
            (1, 'b'),
            (2, 'a'),
            (2, 'b')],
           names=['first', 'second'])

### Set operations on Index objects[](https://pandas.pydata.org/docs/user_guide/indexing.html#set-operations-on-index-objects "Link to this heading")

The two main operations are `union` and `intersection`. Difference is provided via the `.difference()` method.

In [346]: a = pd.Index(['c', 'b', 'a'])

In [347]: b = pd.Index(['c', 'e', 'd'])

In [348]: a.difference(b)
Out[348]: Index(['a', 'b'], dtype='object')

Also available is the `symmetric_difference` operation, which returns elements that appear in either `idx1` or `idx2`, but not in both. This is equivalent to the Index created by `idx1.difference(idx2).union(idx2.difference(idx1))`, with duplicates dropped.

In [349]: idx1 = pd.Index([1, 2, 3, 4])

In [350]: idx2 = pd.Index([2, 3, 4, 5])

In [351]: idx1.symmetric_difference(idx2)
Out[351]: Index([1, 5], dtype='int64')

Note

The resulting index from a set operation will be sorted in ascending order.

When performing [`Index.union()`](https://pandas.pydata.org/docs/reference/api/pandas.Index.union.html#pandas.Index.union "pandas.Index.union") between indexes with different dtypes, the indexes must be cast to a common dtype. Typically, though not always, this is object dtype. The exception is when performing a union between integer and float data. In this case, the integer values are converted to float

In [352]: idx1 = pd.Index([0, 1, 2])

In [353]: idx2 = pd.Index([0.5, 1.5])

In [354]: idx1.union(idx2)
Out[354]: Index([0.0, 0.5, 1.0, 1.5, 2.0], dtype='float64')

### Missing values[](https://pandas.pydata.org/docs/user_guide/indexing.html#missing-values "Link to this heading")

Important

Even though `Index` can hold missing values (`NaN`), it should be avoided if you do not want any unexpected results. For example, some operations exclude missing values implicitly.

`Index.fillna` fills missing values with specified scalar value.

In [355]: idx1 = pd.Index([1, np.nan, 3, 4])

In [356]: idx1
Out[356]: Index([1.0, nan, 3.0, 4.0], dtype='float64')

In [357]: idx1.fillna(2)
Out[357]: Index([1.0, 2.0, 3.0, 4.0], dtype='float64')

In [358]: idx2 = pd.DatetimeIndex([pd.Timestamp('2011-01-01'),
   .....:                         pd.NaT,
   .....:                         pd.Timestamp('2011-01-03')])
   .....: 

In [359]: idx2
Out[359]: DatetimeIndex(['2011-01-01', 'NaT', '2011-01-03'], dtype='datetime64[ns]', freq=None)

In [360]: idx2.fillna(pd.Timestamp('2011-01-02'))
Out[360]: DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03'], dtype='datetime64[ns]', freq=None)

## Set / reset index[](https://pandas.pydata.org/docs/user_guide/indexing.html#set-reset-index "Link to this heading")

Occasionally you will load or create a data set into a DataFrame and want to add an index after you’ve already done so. There are a couple of different ways.

### Set an index[](https://pandas.pydata.org/docs/user_guide/indexing.html#set-an-index "Link to this heading")

DataFrame has a [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index "pandas.DataFrame.set_index") method which takes a column name (for a regular `Index`) or a list of column names (for a `MultiIndex`). To create a new, re-indexed DataFrame:

In [361]: data = pd.DataFrame({'a': ['bar', 'bar', 'foo', 'foo'],
   .....:                     'b': ['one', 'two', 'one', 'two'],
   .....:                     'c': ['z', 'y', 'x', 'w'],
   .....:                     'd': [1., 2., 3, 4]})
   .....: 

In [362]: data
Out[362]: 
     a    b  c    d
0  bar  one  z  1.0
1  bar  two  y  2.0
2  foo  one  x  3.0
3  foo  two  w  4.0

In [363]: indexed1 = data.set_index('c')

In [364]: indexed1
Out[364]: 
     a    b    d
c               
z  bar  one  1.0
y  bar  two  2.0
x  foo  one  3.0
w  foo  two  4.0

In [365]: indexed2 = data.set_index(['a', 'b'])

In [366]: indexed2
Out[366]: 
         c    d
a   b          
bar one  z  1.0
    two  y  2.0
foo one  x  3.0
    two  w  4.0

The `append` keyword option allow you to keep the existing index and append the given columns to a MultiIndex:

In [367]: frame = data.set_index('c', drop=False)

In [368]: frame = frame.set_index(['a', 'b'], append=True)

In [369]: frame
Out[369]: 
           c    d
c a   b          
z bar one  z  1.0
y bar two  y  2.0
x foo one  x  3.0
w foo two  w  4.0

Other options in `set_index` allow you not drop the index columns.

In [370]: data.set_index('c', drop=False)
Out[370]: 
     a    b  c    d
c                  
z  bar  one  z  1.0
y  bar  two  y  2.0
x  foo  one  x  3.0
w  foo  two  w  4.0

### Reset the index[](https://pandas.pydata.org/docs/user_guide/indexing.html#reset-the-index "Link to this heading")

As a convenience, there is a new function on DataFrame called [`reset_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html#pandas.DataFrame.reset_index "pandas.DataFrame.reset_index") which transfers the index values into the DataFrame’s columns and sets a simple integer index. This is the inverse operation of [`set_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index "pandas.DataFrame.set_index").

In [371]: data
Out[371]: 
     a    b  c    d
0  bar  one  z  1.0
1  bar  two  y  2.0
2  foo  one  x  3.0
3  foo  two  w  4.0

In [372]: data.reset_index()
Out[372]: 
   index    a    b  c    d
0      0  bar  one  z  1.0
1      1  bar  two  y  2.0
2      2  foo  one  x  3.0
3      3  foo  two  w  4.0

The output is more similar to a SQL table or a record array. The names for the columns derived from the index are the ones stored in the `names` attribute.

You can use the `level` keyword to remove only a portion of the index:

In [373]: frame
Out[373]: 
           c    d
c a   b          
z bar one  z  1.0
y bar two  y  2.0
x foo one  x  3.0
w foo two  w  4.0

In [374]: frame.reset_index(level=1)
Out[374]: 
         a  c    d
c b               
z one  bar  z  1.0
y two  bar  y  2.0
x one  foo  x  3.0
w two  foo  w  4.0

`reset_index` takes an optional parameter `drop` which if true simply discards the index, instead of putting index values in the DataFrame’s columns.

### Adding an ad hoc index[](https://pandas.pydata.org/docs/user_guide/indexing.html#adding-an-ad-hoc-index "Link to this heading")

You can assign a custom index to the `index` attribute:

In [375]: df_idx = pd.DataFrame(range(4))

In [376]: df_idx.index = pd.Index([10, 20, 30, 40], name="a")

In [377]: df_idx
Out[377]: 
    0
a    
10  0
20  1
30  2
40  3

## Returning a view versus a copy[](https://pandas.pydata.org/docs/user_guide/indexing.html#returning-a-view-versus-a-copy "Link to this heading")

Warning

[Copy-on-Write](https://pandas.pydata.org/docs/user_guide/copy_on_write.html#copy-on-write) will become the new default in pandas 3.0. This means than chained indexing will never work. As a consequence, the `SettingWithCopyWarning` won’t be necessary anymore. See [this section](https://pandas.pydata.org/docs/user_guide/copy_on_write.html#copy-on-write-chained-assignment) for more context. We recommend turning Copy-on-Write on to leverage the improvements with

`` ` pd.options.mode.copy_on_write = True ` ``

even before pandas 3.0 is available.

When setting values in a pandas object, care must be taken to avoid what is called `chained indexing`. Here is an example.

In [378]: dfmi = pd.DataFrame([list('abcd'),
   .....:                     list('efgh'),
   .....:                     list('ijkl'),
   .....:                     list('mnop')],
   .....:                    columns=pd.MultiIndex.from_product([['one', 'two'],
   .....:                                                        ['first', 'second']]))
   .....: 

In [379]: dfmi
Out[379]: 
    one          two       
  first second first second
0     a      b     c      d
1     e      f     g      h
2     i      j     k      l
3     m      n     o      p

Compare these two access methods:

In [380]: dfmi['one']['second']
Out[380]: 
0    b
1    f
2    j
3    n
Name: second, dtype: object

In [381]: dfmi.loc[:, ('one', 'second')]
Out[381]: 
0    b
1    f
2    j
3    n
Name: (one, second), dtype: object

These both yield the same results, so which should you use? It is instructive to understand the order of operations on these and why method 2 (`.loc`) is much preferred over method 1 (chained `[]`).

`dfmi['one']` selects the first level of the columns and returns a DataFrame that is singly-indexed. Then another Python operation `dfmi_with_one['second']` selects the series indexed by `'second'`. This is indicated by the variable `dfmi_with_one` because pandas sees these operations as separate events. e.g. separate calls to `__getitem__`, so it has to treat them as linear operations, they happen one after another.

Contrast this to `df.loc[:,('one','second')]` which passes a nested tuple of `(slice(None),('one','second'))` to a single call to `__getitem__`. This allows pandas to deal with this as a single entity. Furthermore this order of operations _can_ be significantly faster, and allows one to index _both_ axes if so desired.

### Why does assignment fail when using chained indexing?[](https://pandas.pydata.org/docs/user_guide/indexing.html#why-does-assignment-fail-when-using-chained-indexing "Link to this heading")

Warning

[Copy-on-Write](https://pandas.pydata.org/docs/user_guide/copy_on_write.html#copy-on-write) will become the new default in pandas 3.0. This means than chained indexing will never work. As a consequence, the `SettingWithCopyWarning` won’t be necessary anymore. See [this section](https://pandas.pydata.org/docs/user_guide/copy_on_write.html#copy-on-write-chained-assignment) for more context. We recommend turning Copy-on-Write on to leverage the improvements with

`` ` pd.options.mode.copy_on_write = True ` ``

even before pandas 3.0 is available.

The problem in the previous section is just a performance issue. What’s up with the `SettingWithCopy` warning? We don’t **usually** throw warnings around when you do something that might cost a few extra milliseconds!

But it turns out that assigning to the product of chained indexing has inherently unpredictable results. To see this, think about how the Python interpreter executes this code:

dfmi.loc[:, ('one', 'second')] = value
# becomes
dfmi.loc.__setitem__((slice(None), ('one', 'second')), value)

But this code is handled differently:

dfmi['one']['second'] = value
# becomes
dfmi.__getitem__('one').__setitem__('second', value)

See that `__getitem__` in there? Outside of simple cases, it’s very hard to predict whether it will return a view or a copy (it depends on the memory layout of the array, about which pandas makes no guarantees), and therefore whether the `__setitem__` will modify `dfmi` or a temporary object that gets thrown out immediately afterward. **That’s** what `SettingWithCopy` is warning you about!

Note

You may be wondering whether we should be concerned about the `loc` property in the first example. But `dfmi.loc` is guaranteed to be `dfmi` itself with modified indexing behavior, so `dfmi.loc.__getitem__` / `dfmi.loc.__setitem__` operate on `dfmi` directly. Of course, `dfmi.loc.__getitem__(idx)` may be a view or a copy of `dfmi`.

Sometimes a `SettingWithCopy` warning will arise at times when there’s no obvious chained indexing going on. **These** are the bugs that `SettingWithCopy` is designed to catch! pandas is probably trying to warn you that you’ve done this:

def do_something(df):
    foo = df[['bar', 'baz']]  # Is foo a view? A copy? Nobody knows!
    # ... many lines here ...
    # We don't know whether this will modify df or not!
    foo['quux'] = value
    return foo

Yikes!

### Evaluation order matters[](https://pandas.pydata.org/docs/user_guide/indexing.html#evaluation-order-matters "Link to this heading")

Warning

[Copy-on-Write](https://pandas.pydata.org/docs/user_guide/copy_on_write.html#copy-on-write) will become the new default in pandas 3.0. This means than chained indexing will never work. As a consequence, the `SettingWithCopyWarning` won’t be necessary anymore. See [this section](https://pandas.pydata.org/docs/user_guide/copy_on_write.html#copy-on-write-chained-assignment) for more context. We recommend turning Copy-on-Write on to leverage the improvements with

`` ` pd.options.mode.copy_on_write = True ` ``

even before pandas 3.0 is available.

When you use chained indexing, the order and type of the indexing operation partially determine whether the result is a slice into the original object, or a copy of the slice.

pandas has the `SettingWithCopyWarning` because assigning to a copy of a slice is frequently not intentional, but a mistake caused by chained indexing returning a copy where a slice was expected.

If you would like pandas to be more or less trusting about assignment to a chained indexing expression, you can set the [option](https://pandas.pydata.org/docs/user_guide/options.html#options) `mode.chained_assignment` to one of these values:

- `'warn'`, the default, means a `SettingWithCopyWarning` is printed.
    
- `'raise'` means pandas will raise a `SettingWithCopyError` you have to deal with.
    
- `None` will suppress the warnings entirely.
    

In [382]: dfb = pd.DataFrame({'a': ['one', 'one', 'two',
   .....:                          'three', 'two', 'one', 'six'],
   .....:                    'c': np.arange(7)})
   .....: 

# This will show the SettingWithCopyWarning
# but the frame values will be set
In [383]: dfb['c'][dfb['a'].str.startswith('o')] = 42

This however is operating on a copy and will not work.

In [384]: with pd.option_context('mode.chained_assignment','warn'):
   .....:    dfb[dfb['a'].str.startswith('o')]['c'] = 42
   .....: 

A chained assignment can also crop up in setting in a mixed dtype frame.

Note

These setting rules apply to all of `.loc/.iloc`.

The following is the recommended access method using `.loc` for multiple items (using `mask`) and a single item using a fixed index:

In [385]: dfc = pd.DataFrame({'a': ['one', 'one', 'two',
   .....:                          'three', 'two', 'one', 'six'],
   .....:                    'c': np.arange(7)})
   .....: 

In [386]: dfd = dfc.copy()

# Setting multiple items using a mask
In [387]: mask = dfd['a'].str.startswith('o')

In [388]: dfd.loc[mask, 'c'] = 42

In [389]: dfd
Out[389]: 
       a   c
0    one  42
1    one  42
2    two   2
3  three   3
4    two   4
5    one  42
6    six   6

# Setting a single item
In [390]: dfd = dfc.copy()

In [391]: dfd.loc[2, 'a'] = 11

In [392]: dfd
Out[392]: 
       a  c
0    one  0
1    one  1
2     11  2
3  three  3
4    two  4
5    one  5
6    six  6

The following _can_ work at times, but it is not guaranteed to, and therefore should be avoided:

In [393]: dfd = dfc.copy()

In [394]: dfd['a'][2] = 111

In [395]: dfd
Out[395]: 
       a  c
0    one  0
1    one  1
2    111  2
3  three  3
4    two  4
5    one  5
6    six  6

Last, the subsequent example will **not** work at all, and so should be avoided:

In [396]: with pd.option_context('mode.chained_assignment','raise'):
   .....:    dfd.loc[0]['a'] = 1111
   .....: 
---------------------------------------------------------------------------
SettingWithCopyError                      Traceback (most recent call last)
<ipython-input-396-32ce785aaa5b> in ?()
      1 with pd.option_context('mode.chained_assignment','raise'):
----> 2     dfd.loc[0]['a'] = 1111

~/work/pandas/pandas/pandas/core/series.py in ?(self, key, value)
   1284                 )
   1285 
   1286         check_dict_or_set_indexers(key)
   1287         key = com.apply_if_callable(key, self)
-> 1288         cacher_needs_updating = self._check_is_chained_assignment_possible()
   1289 
   1290         if key is Ellipsis:
   1291             key = slice(None)

~/work/pandas/pandas/pandas/core/series.py in ?(self)
   1489             ref = self._get_cacher()
   1490             if ref is not None and ref._is_mixed_type:
   1491                 self._check_setitem_copy(t="referent", force=True)
   1492             return True
-> 1493         return super()._check_is_chained_assignment_possible()

~/work/pandas/pandas/pandas/core/generic.py in ?(self)
   4395         single-dtype meaning that the cacher should be updated following
   4396         setting.
   4397         """
   4398         if self._is_copy:
-> 4399             self._check_setitem_copy(t="referent")
   4400         return False

~/work/pandas/pandas/pandas/core/generic.py in ?(self, t, force)
   4469                 "indexing.html#returning-a-view-versus-a-copy"
   4470             )
   4471 
   4472         if value == "raise":
-> 4473             raise SettingWithCopyError(t)
   4474         if value == "warn":
   4475             warnings.warn(t, SettingWithCopyWarning, stacklevel=find_stack_level())

SettingWithCopyError: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

Warning

The chained assignment warnings / exceptions are aiming to inform the user of a possibly invalid assignment. There may be false positives; situations where a chained assignment is inadvertently reported.


---
## 참조

---
title: "[Pandas] 파이에로우 (Pyarrow)"
excerpt: 에 대한 문서
categories:
  - Pandas
tags:
  - Pandas
  - Arrow
last_modified_at: 2024-03-01T00:00:00-00:00
link: https://pandas.pydata.org/docs/user_guide/pyarrow.html
상위 항목: "[[pandas_home|판다스 (Pandas)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`



---
pandas는 다양한 API의 기능을 확장하고 성능을 향상시키기 위해 [PyArrow](https://arrow.apache.org/docs/python/index.html)를 활용할 수 있습니다. 이는 다음을 포함합니다:

- NumPy와 비교하여 더 광범위한 [데이터 타입](https://arrow.apache.org/docs/python/api/datatypes.html)
    
- 모든 데이터 타입에 대한 결측치 지원 (NA)
    
- 성능이 좋은 IO 리더 통합
    
- Apache Arrow 사양을 기반으로 하는 다른 데이터프레임 라이브러리와의 상호 운용성 촉진 (예: polars, cuDF)
    

이 기능을 사용하려면 [최소 지원 PyArrow 버전을 설치](https://pandas.pydata.org/docs/getting_started/install.html#install-optional-dependencies)했는지 확인하세요.

## 데이터 구조 통합 (Data Structure Integration)

Series, Index 또는 DataFrame의 열은 NumPy 배열과 유사한 pyarrow.ChunkedArray에 의해 직접 지원될 수 있습니다. 주요 pandas 데이터 구조에서 이를 구성하려면 dtype 매개변수에 타입 문자열 뒤에 [pyarrow]를 붙여 전달할 수 있습니다. 예를 들어 "int64[pyarrow]"와 같이 사용합니다.

```python
ser = pd.Series([-1.5, 0.2, None], dtype="float32[pyarrow]")

ser
Out[2]: 
0    -1.5
1     0.2
2    <NA>
dtype: float[pyarrow]

idx = pd.Index([True, None], dtype="bool[pyarrow]")

idx
Out[4]: Index([True, <NA>], dtype='bool[pyarrow]')

df = pd.DataFrame([[1, 2], [3, 4]], dtype="uint64[pyarrow]")

df
Out[6]: 
   0  1
0  1  2
1  3  4
```

> [!NOTE]
> 문자열 별칭 "string[pyarrow]"는 pd.StringDtype("pyarrow")에 매핑되며, 이는 dtype=pd.ArrowDtype(pa.string())을 지정하는 것과 동일하지 않습니다. 일반적으로 데이터에 대한 연산은 유사하게 동작하지만 pd.StringDtype("pyarrow")는 NumPy 기반의 nullable 타입을 반환할 수 있는 반면, pd.ArrowDtype(pa.string())은 ArrowDtype을 반환합니다.
> 
> ```python
> import pyarrow as pa
> 
> data = list("abc")
> 
> ser_sd = pd.Series(data, dtype="string[pyarrow]")
> 
> ser_ad = pd.Series(data, dtype=pd.ArrowDtype(pa.string()))
> 
> ser_ad.dtype == ser_sd.dtype
> Out[11]: False
> 
> ser_sd.str.contains("a")
> Out[12]: 
> 0     True
> 1    False
> 2    False
> dtype: boolean
> 
> ser_ad.str.contains("a")
> Out[13]: 
> 0     True
> 1    False
> 2    False
> dtype: bool[pyarrow]
> ```

매개변수를 허용하는 PyArrow 타입의 경우, 해당 매개변수와 함께 PyArrow 타입을 ArrowDtype에 전달하여 dtype 매개변수에서 사용할 수 있습니다.

```python
import pyarrow as pa

list_str_type = pa.list_(pa.string())

ser = pd.Series([["hello"], ["there"]], dtype=pd.ArrowDtype(list_str_type))

ser
Out[17]: 
0    ['hello']
1    ['there']
dtype: list<item: string>[pyarrow]

from datetime import time

idx = pd.Index([time(12, 30), None], dtype=pd.ArrowDtype(pa.time64("us")))

idx
Out[20]: Index([12:30:00, <NA>], dtype='time64[us][pyarrow]')

from decimal import Decimal

decimal_type = pd.ArrowDtype(pa.decimal128(3, scale=2))

data = [[Decimal("3.19"), None], [None, Decimal("-1.23")]]

df = pd.DataFrame(data, dtype=decimal_type)

df
Out[25]: 
      0      1
0  3.19   <NA>
1  <NA>  -1.23
```

이미 pyarrow.Array 또는 pyarrow.ChunkedArray가 있는 경우, arrays.ArrowExtensionArray에 전달하여 관련 Series, Index 또는 DataFrame 객체를 구성할 수 있습니다.

```python
pa_array = pa.array(
   [{"1": "2"}, {"10": "20"}, None],
   type=pa.map_(pa.string(), pa.string()),
)

ser = pd.Series(pd.arrays.ArrowExtensionArray(pa_array))

ser
Out[28]: 
0      [('1', '2')]
1    [('10', '20')]
2              <NA>
dtype: map<string, string>[pyarrow]
```

Series 또는 Index에서 pyarrow.ChunkedArray를 검색하려면 Series 또는 Index에 대해 pyarrow 배열 생성자를 호출할 수 있습니다.

```python
ser = pd.Series([1, 2, None], dtype="uint8[pyarrow]")

pa.array(ser)
Out[30]: 
<pyarrow.lib.UInt8Array object at 0x7ff2a2968400>
[
  1,
  2,
  null
]

idx = pd.Index(ser)

pa.array(idx)
Out[32]: 
<pyarrow.lib.UInt8Array object at 0x7ff2a2968460>
[
  1,
  2,
  null
]
```

pyarrow.Table을 DataFrame으로 변환하려면 types_mapper=pd.ArrowDtype와 함께 pyarrow.Table.to_pandas() 메서드를 호출할 수 있습니다.

```python
table = pa.table([pa.array([1, 2, 3], type=pa.int64())], names=["a"])

df = table.to_pandas(types_mapper=pd.ArrowDtype)

df
Out[35]: 
   a
0  1
1  2
2  3

df.dtypes
Out[36]: 
a    int64[pyarrow]
dtype: object
```

## 연산 (Operations)

PyArrow 데이터 구조 통합은 pandas의 `ExtensionArray` 인터페이스를 통해 구현됩니다. 따라서 지원되는 기능은 이 인터페이스가 pandas API 내에 통합된 곳에 존재합니다. 또한, 이 기능은 가능한 경우 PyArrow 계산 함수로 가속화됩니다. 여기에는 다음이 포함됩니다:

- 숫자 집계
- 숫자 연산
- 숫자 반올림
- 논리 및 비교 함수
- 문자열 기능
- 날짜/시간 기능

다음은 네이티브 PyArrow 계산 함수로 가속화되는 연산의 몇 가지 예시입니다.

```python
import pyarrow as pa

ser = pd.Series([-1.545, 0.211, None], dtype="float32[pyarrow]")

ser.mean()
Out[39]: -0.6669999808073044

ser + ser
Out[40]: 
0    -3.09
1    0.422
2     <NA>
dtype: float[pyarrow]

ser > (ser + 1)
Out[41]: 
0    False
1    False
2     <NA>
dtype: bool[pyarrow]

ser.dropna()
Out[42]: 
0   -1.545
1    0.211
dtype: float[pyarrow]

ser.isna()
Out[43]: 
0    False
1    False
2     True
dtype: bool

ser.fillna(0)
Out[44]: 
0   -1.545
1    0.211
2      0.0
dtype: float[pyarrow]

ser_str = pd.Series(["a", "b", None], dtype=pd.ArrowDtype(pa.string()))

ser_str.str.startswith("a")
Out[46]: 
0     True
1    False
2     <NA>
dtype: bool[pyarrow]

from datetime import datetime

pa_type = pd.ArrowDtype(pa.timestamp("ns"))

ser_dt = pd.Series([datetime(2022, 1, 1), None], dtype=pa_type)

ser_dt.dt.strftime("%Y-%m")
Out[50]: 
0    2022-01
1       <NA>
dtype: string[pyarrow]
```

## I/O 읽기 (I/O Reading)

PyArrow는 또한 여러 pandas I/O 리더에 통합된 I/O 읽기 기능을 제공합니다. 다음 함수들은 PyArrow를 사용하여 I/O 소스에서 읽기를 가속화할 수 있는 engine 키워드를 제공합니다.

- read_csv()
- read_json()
- read_orc()
- read_feather()

```python
import io

data = io.StringIO("""a,b,c
  1,2.5,True
  3,4.5,False
""")

df = pd.read_csv(data, engine="pyarrow")

df
Out[54]: 
   a    b      c
0  1  2.5   True
1  3  4.5  False
```

기본적으로 이 함수들과 다른 모든 I/O 리더 함수는 NumPy 기반 데이터를 반환합니다. 이 리더들은 매개변수 dtype_backend="pyarrow"를 지정하여 PyArrow 기반 데이터를 반환할 수 있습니다. PyArrow 기반 데이터를 반환하기 위해 반드시 engine="pyarrow"를 설정할 필요는 없습니다.

```python
import io

data = io.StringIO("""a,b,c,d,e,f,g,h,i
   1,2.5,True,a,,,,,
   3,4.5,False,b.5,True,a,
""")

df_pyarrow = pd.read_csv(data, dtype_backend="pyarrow")

df_pyarrow.dtypes
Out[58]: 
a     int64[pyarrow]
b    double[pyarrow]
c      bool[pyarrow]
d    string[pyarrow]
e     int64[pyarrow]
f    double[pyarrow]
g      bool[pyarrow]
h    string[pyarrow]
i      null[pyarrow]
dtype: object
```

여러 비 I/O 리더 함수도 dtype_backend 인수를 사용하여 PyArrow 기반 데이터를 반환할 수 있습니다. 여기에는 다음이 포함됩니다:

- to_numeric()
- DataFrame.convert_dtypes()
- Series.convert_dtypes()


---
## 참조

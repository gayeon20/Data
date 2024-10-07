---
title: "[Pandas] 입출력 도구 (I/O Tools)"
excerpt: 에 대한 문서
categories:
  - Pandas
tags:
  - Pandas
  - CSV
  - FWF
  - JSON
  - HTML
  - LaTeX
  - XML
  - Clipboard
  - Excel
  - HDF
  - Feather
  - Parquet
  - ORC
  - Stata
  - SAS
  - SPSS
  - Pickle
  - SQL
  - Google-BigQuery
last_modified_at: 2024-03-01T00:00:00-00:00
link: https://pandas.pydata.org/docs/user_guide/io.html
상위 항목: "[[pandas_home|판다스 (Pandas)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`


---

판다스 I/O API는 일반적으로 판다스 객체를 반환하는 [`pandas.read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv “pandas.read_csv”)처럼 액세스되는 최상위 `reader` 함수의 집합입니다. 해당 `writer` 함수는 [`DataFrame.to_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv “pandas.DataFrame.to_csv”)와 같이 액세스되는 객체 메서드입니다. 아래는 사용 가능한 `reader`와 `writer`가 포함된 표입니다.

|Format Type|Data Description|Reader|Writer|
|---|---|---|---|
|text|[CSV](https://en.wikipedia.org/wiki/Comma-separated_values)|[read_csv](https://pandas.pydata.org/docs/user_guide/io.html#io-read-csv-table)|[to_csv](https://pandas.pydata.org/docs/user_guide/io.html#io-store-in-csv)|
|text|Fixed-Width Text File|[read_fwf](https://pandas.pydata.org/docs/user_guide/io.html#io-fwf-reader)||
|text|[JSON](https://www.json.org/)|[read_json](https://pandas.pydata.org/docs/user_guide/io.html#io-json-reader)|[to_json](https://pandas.pydata.org/docs/user_guide/io.html#io-json-writer)|
|text|[HTML](https://en.wikipedia.org/wiki/HTML)|[read_html](https://pandas.pydata.org/docs/user_guide/io.html#io-read-html)|[to_html](https://pandas.pydata.org/docs/user_guide/io.html#io-html)|
|text|[LaTeX](https://en.wikipedia.org/wiki/LaTeX)||[Styler.to_latex](https://pandas.pydata.org/docs/user_guide/io.html#io-latex)|
|text|[XML](https://www.w3.org/standards/xml/core)|[read_xml](https://pandas.pydata.org/docs/user_guide/io.html#io-read-xml)|[to_xml](https://pandas.pydata.org/docs/user_guide/io.html#io-xml)|
|text|Local clipboard|[read_clipboard](https://pandas.pydata.org/docs/user_guide/io.html#io-clipboard)|[to_clipboard](https://pandas.pydata.org/docs/user_guide/io.html#io-clipboard)|
|binary|[MS Excel](https://en.wikipedia.org/wiki/Microsoft_Excel)|[read_excel](https://pandas.pydata.org/docs/user_guide/io.html#io-excel-reader)|[to_excel](https://pandas.pydata.org/docs/user_guide/io.html#io-excel-writer)|
|binary|[OpenDocument](http://opendocumentformat.org/)|[read_excel](https://pandas.pydata.org/docs/user_guide/io.html#io-ods)||
|binary|[HDF5 Format](https://support.hdfgroup.org/HDF5/whatishdf5.html)|[read_hdf](https://pandas.pydata.org/docs/user_guide/io.html#io-hdf5)|[to_hdf](https://pandas.pydata.org/docs/user_guide/io.html#io-hdf5)|
|binary|[Feather Format](https://github.com/wesm/feather)|[read_feather](https://pandas.pydata.org/docs/user_guide/io.html#io-feather)|[to_feather](https://pandas.pydata.org/docs/user_guide/io.html#io-feather)|
|binary|[Parquet Format](https://parquet.apache.org/)|[read_parquet](https://pandas.pydata.org/docs/user_guide/io.html#io-parquet)|[to_parquet](https://pandas.pydata.org/docs/user_guide/io.html#io-parquet)|
|binary|[ORC Format](https://orc.apache.org/)|[read_orc](https://pandas.pydata.org/docs/user_guide/io.html#io-orc)|[to_orc](https://pandas.pydata.org/docs/user_guide/io.html#io-orc)|
|binary|[Stata](https://en.wikipedia.org/wiki/Stata)|[read_stata](https://pandas.pydata.org/docs/user_guide/io.html#io-stata-reader)|[to_stata](https://pandas.pydata.org/docs/user_guide/io.html#io-stata-writer)|
|binary|[SAS](https://en.wikipedia.org/wiki/SAS_(software))|[read_sas](https://pandas.pydata.org/docs/user_guide/io.html#io-sas-reader)||
|binary|[SPSS](https://en.wikipedia.org/wiki/SPSS)|[read_spss](https://pandas.pydata.org/docs/user_guide/io.html#io-spss-reader)||
|binary|[Python Pickle Format](https://docs.python.org/3/library/pickle.html)|[read_pickle](https://pandas.pydata.org/docs/user_guide/io.html#io-pickle)|[to_pickle](https://pandas.pydata.org/docs/user_guide/io.html#io-pickle)|
|SQL|[SQL](https://en.wikipedia.org/wiki/SQL)|[read_sql](https://pandas.pydata.org/docs/user_guide/io.html#io-sql)|[to_sql](https://pandas.pydata.org/docs/user_guide/io.html#io-sql)|
|SQL|[Google BigQuery](https://en.wikipedia.org/wiki/BigQuery)|[read_gbq](https://pandas.pydata.org/docs/user_guide/io.html#io-bigquery)|[to_gbq](https://pandas.pydata.org/docs/user_guide/io.html#io-bigquery)|

[여기](https://pandas.pydata.org/docs/user_guide/io.html#io-perf)는 이러한 IO 메서드 중 일부에 대한 비공식적인 성능 비교표입니다.

> `StringIO` 클래스를 사용하는 예제의 경우 파이썬 3의 경우 `from io import StringIO`를 사용하여 임포트해야 합니다.

> 전체 내용은 [IO tools (text, CSV, HDF5, …) — pandas 2.2.2 documentation (pydata.org)](https://pandas.pydata.org/docs/user_guide/io.html)참조

## Parquet

[Apache Parquet](https://parquet.apache.org/)는 데이터 프레임을 위한 분할된 이진 컬럼 직렬화를 제공합니다. 데이터 프레임의 읽기와 쓰기를 효율적으로 만들고 데이터 분석 언어 간에 데이터 공유를 쉽게 하기 위해 설계되었습니다. Parquet는 다양한 압축 기술을 사용하여 좋은 읽기 성능을 유지하면서도 파일 크기를 최대한 줄일 수 있습니다.

Parquet는 datetime과 tz와 같은 확장 dtypes를 포함한 모든 pandas dtypes를 지원하여 DataFrame을 충실하게 직렬화하고 역직렬화하도록 설계되었습니다.

몇 가지 주의사항이 있습니다.

- 중복된 열 이름과 문자열이 아닌 열 이름은 지원되지 않습니다.

- pyarrow 엔진은 항상 출력에 인덱스를 작성하지만 fastparquet는 기본값이 아닌 인덱스만 작성합니다. 이 추가 열은 예상하지 않은 비 pandas 소비자에게 문제를 일으킬 수 있습니다. 기본 엔진에 관계없이 index 인수를 사용하여 인덱스를 포함하거나 생략하도록 강제할 수 있습니다.

- 인덱스 레벨 이름이 지정된 경우 문자열이어야 합니다.

- pyarrow 엔진에서 문자열이 아닌 유형의 범주형 dtypes는 parquet로 직렬화될 수 있지만 기본 dtype으로 역직렬화됩니다.

- pyarrow 엔진은 문자열 유형의 범주형 dtypes의 ordered 플래그를 보존합니다. fastparquet는 ordered 플래그를 보존하지 않습니다.

- 지원되지 않는 유형에는 Interval 및 실제 Python 객체 유형이 포함됩니다. 이들은 직렬화 시도 시 도움이 되는 오류 메시지를 발생시킵니다. Period 유형은 pyarrow >= 0.16.0에서 지원됩니다.

- pyarrow 엔진은 nullable 정수 및 문자열 데이터 유형과 같은 확장 데이터 유형을 보존합니다(pyarrow >= 0.16.0 필요, 그리고 확장 유형이 필요한 프로토콜을 구현해야 함, 확장 유형 문서 참조).

직렬화를 지시하기 위해 engine을 지정할 수 있습니다. 이는 pyarrow, fastparquet 또는 auto 중 하나일 수 있습니다. 엔진이 지정되지 않은 경우 pd.options.io.parquet.engine 옵션이 확인됩니다. 이것도 auto인 경우 pyarrow를 시도하고 실패하면 fastparquet로 대체됩니다.

[pyarrow](https://arrow.apache.org/docs/python/)와 [fastparquet](https://fastparquet.readthedocs.io/en/latest/)의 문서를 참조하세요.

> [!NOTE]
> 이 엔진들은 매우 유사하며 거의 동일한 parquet 형식 파일을 읽고 쓸 수 있습니다. pyarrow>=8.0.0은 timedelta 데이터를 지원하고, fastparquet>=0.1.4는 시간대를 인식하는 datetime을 지원합니다. 이 라이브러리들은 기본 종속성이 다릅니다(fastparquet는 numba를 사용하고 pyarrow는 c-라이브러리를 사용합니다).

```python
df = pd.DataFrame(
   {
       "a": list("abc"),
       "b": list(range(1, 4)),
       "c": np.arange(3, 6).astype("u1"),
       "d": np.arange(4.0, 7.0, dtype="float64"),
       "e": [True, False, True],
       "f": pd.date_range("20130101", periods=3),
       "g": pd.date_range("20130101", periods=3, tz="US/Eastern"),
       "h": pd.Categorical(list("abc")),
       "i": pd.Categorical(list("abc"), ordered=True),
   }
)
```

```python
df
```

```
   a  b  c    d      e          f                         g  h  i
0  a  1  3  4.0   True 2013-01-01 2013-01-01 00:00:00-05:00  a  a
1  b  2  4  5.0  False 2013-01-02 2013-01-02 00:00:00-05:00  b  b
2  c  3  5  6.0   True 2013-01-03 2013-01-03 00:00:00-05:00  c  c
```

```python
df.dtypes
```

```
a                        object
b                         int64
c                         uint8
d                       float64
e                          bool
f                datetime64[ns]
g    datetime64[ns, US/Eastern]
h                      category
i                      category
dtype: object
```

parquet 파일에 쓰기.

```python
df.to_parquet("example_pa.parquet", engine="pyarrow")

df.to_parquet("example_fp.parquet", engine="fastparquet")
```

parquet 파일에서 읽기.

```python
result = pd.read_parquet("example_fp.parquet", engine="fastparquet")

result = pd.read_parquet("example_pa.parquet", engine="pyarrow")

result.dtypes
```

```
a                        object
b                         int64
c                         uint8
d                       float64
e                          bool
f                datetime64[ns]
g    datetime64[ns, US/Eastern]
h                      category
i                      category
dtype: object
```

dtype_backend 인수를 설정하여 결과 DataFrame에 사용되는 기본 dtypes를 제어할 수 있습니다.

```python
result = pd.read_parquet("example_pa.parquet", engine="pyarrow", dtype_backend="pyarrow")

result.dtypes
```

```
a                                      string[pyarrow]
b                                       int64[pyarrow]
c                                       uint8[pyarrow]
d                                      double[pyarrow]
e                                        bool[pyarrow]
f                               timestamp[ns][pyarrow]
g                timestamp[ns, tz=US/Eastern][pyarrow]
h    dictionary<values=string, indices=int32, order…
i    dictionary<values=string, indices=int32, order…
dtype: object
```


> [!NOTE] 
> fastparquet에서는 이것이 지원되지 않습니다.

parquet 파일의 특정 열만 읽기.

```python
result = pd.read_parquet(
   "example_fp.parquet",
   engine="fastparquet",
   columns=["a", "b"],
)

result = pd.read_parquet(
   "example_pa.parquet",
   engine="pyarrow",
   columns=["a", "b"],
)

result.dtypes
```

```
a    object
b     int64
dtype: object
```

네, 주어진 내용을 한국어로 번역하고 요청하신 조건들을 적용하겠습니다.

### 인덱스 처리 (Handling indexes)

DataFrame을 parquet으로 직렬화할 때 암시적 인덱스가 출력 파일의 하나 이상의 열로 포함될 수 있습니다. 따라서 다음 코드는:

```python
df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})

df.to_parquet("test.parquet", engine="pyarrow")
```

pyarrow를 직렬화에 사용하면 세 개의 열(a, b, 그리고 __index_level_0__)이 있는 parquet 파일을 생성합니다. fastparquet를 사용하는 경우, 인덱스는 파일에 기록될 수도 있고 그렇지 않을 수도 있습니다.

이 예상치 못한 추가 열로 인해 Amazon Redshift와 같은 일부 데이터베이스에서 해당 열이 대상 테이블에 존재하지 않기 때문에 파일을 거부할 수 있습니다.

쓰기 시 데이터프레임의 인덱스를 생략하려면 to_parquet()에 index=False를 전달하세요:

```python
df.to_parquet("test.parquet", index=False)
```

이렇게 하면 예상된 두 열(a와 b)만 있는 parquet 파일이 생성됩니다. DataFrame에 사용자 정의 인덱스가 있는 경우, 이 파일을 DataFrame으로 로드할 때 해당 인덱스를 다시 얻을 수 없습니다.

index=True를 전달하면 기본 엔진의 기본 동작과 관계없이 항상 인덱스를 기록합니다.

### Parquet 파일 분할 (Partitioning Parquet files)

Parquet는 하나 이상의 열 값을 기반으로 데이터 분할을 지원합니다.

```python
df = pd.DataFrame({"a": [0, 0, 1, 1], "b": [0, 1, 0, 1]})

df.to_parquet(path="test", engine="pyarrow", partition_cols=["a"], compression=None)
```

path는 데이터가 저장될 상위 디렉토리를 지정합니다. partition_cols는 데이터셋을 분할할 열 이름입니다. 열은 주어진 순서대로 분할됩니다. 분할은 분할 열의 고유 값에 의해 결정됩니다. 위의 예제는 다음과 같은 분할된 데이터셋을 생성할 수 있습니다:

```
test
├── a=0
│   ├── 0bac803e32dc42ae83fddfd029cbdebc.parquet
│   └── …
└── a=1
    ├── e6ab24a4f45147b49b54a662f0c412a3.parquet
    └── …
```

---
## 참조

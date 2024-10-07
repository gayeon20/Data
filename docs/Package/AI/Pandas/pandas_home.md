---
title: "[Data] 판다스 (Pandas)"
excerpt: 에 대한 문서
categories:
  - Pandas
tags:
  - Data
  - AI
  - Scientific-Computing
  - Python
  - Pandas
  - Linear-Algebra
  - Array
  - Matrix
last_modified_at: 2024-03-01T00:00:00-00:00
link: https://pandas.pydata.org/
상위 항목: "[[python_ai|파이썬 인공지능 (Python AI)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

**하위 항목**
- [[pandas_grammer|판다스 문법 (Pandas Grammer)]]

---
#TODO
- [ ] [Indexing and selecting data — pandas 2.2.2 documentation (pydata.org)](https://pandas.pydata.org/docs/user_guide/indexing.html)
- [ ] [MultiIndex / advanced indexing — pandas 2.2.2 documentation (pydata.org)](https://pandas.pydata.org/docs/user_guide/advanced.html)\
- [ ] [Copy-on-Write (CoW) — pandas 2.2.2 documentation (pydata.org)](https://pandas.pydata.org/docs/user_guide/copy_on_write.html)
- [ ] [Merge, join, concatenate and compare — pandas 2.2.2 documentation (pydata.org)](https://pandas.pydata.org/docs/user_guide/merging.html)
- [ ] [Reshaping and pivot tables — pandas 2.2.2 documentation (pydata.org)](https://pandas.pydata.org/docs/user_guide/reshaping.html)

pandas is a [Python](https://www.python.org/) package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, **real-world** data analysis in Python. Additionally, it has the broader goal of becoming **the most powerful and flexible open source data analysis/manipulation tool available in any language**. It is already well on its way toward this goal.

pandas is well suited for many different kinds of data:

> - Tabular data with heterogeneously-typed columns, as in an SQL table or Excel spreadsheet
>     
> - Ordered and unordered (not necessarily fixed-frequency) time series data.
>     
> - Arbitrary matrix data (homogeneously typed or heterogeneous) with row and column labels
>     
> - Any other form of observational / statistical data sets. The data need not be labeled at all to be placed into a pandas data structure
>     

The two primary data structures of pandas, [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series") (1-dimensional) and [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") (2-dimensional), handle the vast majority of typical use cases in finance, statistics, social science, and many areas of engineering. For R users, [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") provides everything that R’s `data.frame` provides and much more. pandas is built on top of [NumPy](https://numpy.org/) and is intended to integrate well within a scientific computing environment with many other 3rd party libraries.

Here are just a few of the things that pandas does well:

> - Easy handling of **missing data** (represented as NaN) in floating point as well as non-floating point data
>     
> - Size mutability: columns can be **inserted and deleted** from DataFrame and higher dimensional objects
>     
> - Automatic and explicit **data alignment**: objects can be explicitly aligned to a set of labels, or the user can simply ignore the labels and let `Series`, `DataFrame`, etc. automatically align the data for you in computations
>     
> - Powerful, flexible **group by** functionality to perform split-apply-combine operations on data sets, for both aggregating and transforming data
>     
> - Make it **easy to convert** ragged, differently-indexed data in other Python and NumPy data structures into DataFrame objects
>     
> - Intelligent label-based **slicing**, **fancy indexing**, and **subsetting** of large data sets
>     
> - Intuitive **merging** and **joining** data sets
>     
> - Flexible **reshaping** and pivoting of data sets
>     
> - **Hierarchical** labeling of axes (possible to have multiple labels per tick)
>     
> - Robust IO tools for loading data from **flat files** (CSV and delimited), Excel files, databases, and saving / loading data from the ultrafast **HDF5 format**
>     
> - **Time series**-specific functionality: date range generation and frequency conversion, moving window statistics, date shifting, and lagging.
>     

Many of these principles are here to address the shortcomings frequently experienced using other languages / scientific research environments. For data scientists, working with data is typically divided into multiple stages: munging and cleaning data, analyzing / modeling it, then organizing the results of the analysis into a form suitable for plotting or tabular display. pandas is the ideal tool for all of these tasks.

Some other notes

> - pandas is **fast**. Many of the low-level algorithmic bits have been extensively tweaked in [Cython](https://cython.org/) code. However, as with anything else generalization usually sacrifices performance. So if you focus on one feature for your application you may be able to create a faster specialized tool.
>     
> - pandas is a dependency of [statsmodels](https://www.statsmodels.org/), making it an important part of the statistical computing ecosystem in Python.
>     
> - pandas has been used extensively in production in financial applications.
>     

## Data structures[](https://pandas.pydata.org/docs/getting_started/overview.html#data-structures "Link to this heading")

|Dimensions|Name|Description|
|---|---|---|
|1|Series|1D labeled homogeneously-typed array|
|2|DataFrame|General 2D labeled, size-mutable tabular structure with potentially heterogeneously-typed column|

### Why more than one data structure?[](https://pandas.pydata.org/docs/getting_started/overview.html#why-more-than-one-data-structure "Link to this heading")

The best way to think about the pandas data structures is as flexible containers for lower dimensional data. For example, DataFrame is a container for Series, and Series is a container for scalars. We would like to be able to insert and remove objects from these containers in a dictionary-like fashion.

Also, we would like sensible default behaviors for the common API functions which take into account the typical orientation of time series and cross-sectional data sets. When using the N-dimensional array (ndarrays) to store 2and 3-dimensional data, a burden is placed on the user to consider the orientation of the data set when writing functions; axes are considered more or less equivalent (except when Cor Fortran-contiguousness matters for performance). In pandas, the axes are intended to lend more semantic meaning to the data; i.e., for a particular data set, there is likely to be a “right” way to orient the data. The goal, then, is to reduce the amount of mental effort required to code up data transformations in downstream functions.

For example, with tabular data (DataFrame) it is more semantically helpful to think of the **index** (the rows) and the **columns** rather than axis 0 and axis 1. Iterating through the columns of the DataFrame thus results in more readable code:

for col in df.columns:
    series = df[col]
    # do something with series

## Mutability and copying of data[](https://pandas.pydata.org/docs/getting_started/overview.html#mutability-and-copying-of-data "Link to this heading")

All pandas data structures are value-mutable (the values they contain can be altered) but not always size-mutable. The length of a Series cannot be changed, but, for example, columns can be inserted into a DataFrame. However, the vast majority of methods produce new objects and leave the input data untouched. In general we like to **favor immutability** where sensible.


## 설치
[Installation — pandas 2.2.2 documentation (pydata.org)](https://pandas.pydata.org/docs/getting_started/install.html)

---
## 참조
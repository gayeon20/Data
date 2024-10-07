---
title: "[Python] 인공지능 (AI; Artificial Intelligence)"
excerpt: 에 대한 문서
categories:
  - AI
tags:
  - AI
  - Scientific-Computing
  - Python
last_modified_at: 2024-03-01T00:00:00-00:00
link: 
상위 항목: "[[python_library|파이썬 라이브러리 (Python Library)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

**하위 항목**
- [[numpy_home|넘파이 (Numpy)]]
- [[pandas_home|판다스 (Pandas)]]

---

> [!NOTE] 대표 패키지
> - 머신 러닝: scikit-laern
> - 배열/선형대수/통계: numpy, scipy
> - 데이터 핸들링: pandas
> - 시각화: matplotlib, seaborn

- AI에서 다양한 데이터의 추출/가공/변환이 중요하며 이는 numpy, pandas를 사용합니다.
- Scikit-learn은 numpy 기반이므로 이에 대한 이해도를 요구합니다.
- Numpy와 Pandas는 다양한 기능이 존재하므로 기본 프레임워크와 중요 기능만 익히고 이후 필요할 때마다 공부하는 것이 효과적입니다.



## 커리큘럼
### 1) 기초
- Python 및 선형대수, 통계 등 기초 학문 포함

#### (1) Python
- [왕초보를 위한 Python: 쉽게 풀어 쓴 기초 문법과 실습 - WikiDocs](https://wikidocs.net/book/2)

#### (2) Numpy
> 기본적인 수치 계산을 위한 라이브러리로, 배열(array)과 행렬(matrix) 연산의 기초를 제공합니다. 데이터 처리와 과학 계산의 기본이 되므로 가장 먼저 익혀야 합니다.


- [What is NumPy? — NumPy v2.0 Manual](https://numpy.org/doc/2.0/user/whatisnumpy.html)
- [NumPy quickstart — NumPy v2.0 Manual](https://numpy.org/doc/2.0/user/quickstart.html)
- [NumPy: the absolute basics for beginners — NumPy v2.0 Manual](https://numpy.org/doc/2.0/user/absolute_beginners.html#)
- [NumPy Features — NumPy Tutorials](https://numpy.org/numpy-tutorials/features.html)

#### (3) Pandas
> 데이터 분석을 위해 사용되며, 특히 데이터프레임(dataframe)과 시리즈(series) 같은 데이터 구조를 제공합니다. Numpy 위에 구축되어 있으며 데이터 조작 및 정제에 매우 유용합니다.

- [10 minutes to pandas — pandas 2.2.2 documentation (pydata.org)](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Essential basic functionality — pandas 2.2.2 documentation (pydata.org)](https://pandas.pydata.org/docs/user_guide/basics.html)
- [Getting started tutorials — pandas 2.2.2 documentation (pydata.org)](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
- [한 권으로 끝내는 <판다스 노트> - WikiDocs](https://wikidocs.net/book/4639)

#### (4) Matplotlib
> 데이터를 시각화하기 위한 라이브러리입니다. Pandas와 함께 사용되어 데이터 분석 결과를 그래프로 표현할 수 있습니다.

- [Quick start guide — Matplotlib 3.9.0 documentation](https://matplotlib.org/stable/users/explain/quick_start.html)
- [Tutorials — Matplotlib 3.9.0 documentation](https://matplotlib.org/stable/tutorials/index.html
- [Matplotlib Tutorial - 파이썬으로 데이터 시각화하기 - WikiDocs](https://wikidocs.net/book/5011)

### 2) 머신 러닝 (면접을 위한 최소 커트 라인)
- 원리, 학습 관련 지식, 머신 러닝 기법 등 이론 기초 공부 필요

#### (1) Scikit-Learn
> 머신 러닝 알고리즘을 구현한 라이브러리로, 분류, 회귀, 클러스터링 등 다양한 머신 러닝 기술을 포함합니다. 기본적인 데이터 처리와 시각화를 익힌 후, 머신 러닝 모델을 구현하는 데 사용합니다.

- 기계 학습을 위한 라이브러리로, 다양한 알고리즘과 데이터 전처리 방법을 배웁니다.
- 분류, 회귀, 군집화 등 다양한 모델을 구현해 봅니다.

- [Getting Started — scikit-learn 1.5.0 documentation](https://scikit-learn.org/stable/getting_started.html)
- [scikit-learn Tutorials — scikit-learn 1.5.0 documentation](https://scikit-learn.org/stable/tutorial/index.html)

### 3) 딥 러닝
- 신경망 등 딥러닝 관련 이론 공부 필요

#### (1) Pytorch
> Pytorch는 딥러닝 모델을 개발하기 위한 프레임워크입니다.

- 딥러닝 라이브러리로, 텐서 연산과 신경망 모델을 학습합니다.
- 기본적인 신경망 구조, 역전파, 모델 훈련 등을 연습합니다.

- [파이토치(PyTorch) 기본 익히기 — 파이토치 한국어 튜토리얼 (PyTorch tutorials in Korean)](https://tutorials.pytorch.kr/beginner/basics/intro.html)의 Pytorch 시작하기 챕터
- [빠른 시작(Quickstart) — 파이토치 한국어 튜토리얼 (PyTorch tutorials in Korean)](https://tutorials.pytorch.kr/beginner/basics/quickstart_tutorial.html)
- [PyTorch로 딥러닝하기: 60분만에 끝장내기 — 파이토치 한국어 튜토리얼 (PyTorch tutorials in Korean)](https://tutorials.pytorch.kr/beginner/deep_learning_60min_blitz.html)
- [torch.nn 이 실제로 무엇인가요? — 파이토치 한국어 튜토리얼 (PyTorch tutorials in Korean)](https://tutorials.pytorch.kr/beginner/nn_tutorial.html)
- [TensorBoard로 모델, 데이터, 학습 시각화하기 — 파이토치 한국어 튜토리얼 (PyTorch tutorials in Korean)](https://tutorials.pytorch.kr/intermediate/tensorboard_tutorial.html)
- [PyTorch로 시작하는 딥 러닝 입문 - WikiDocs](https://wikidocs.net/book/2788)

### 4) 자연어 처리
- AI 중 자연어 처리 분야에 대한 지식 필요

> 컴퓨터 비전, 추천 시스템은 AI에서 다른 분야, 통계적인 내용과 멀어질 가능성이 있고 2024년 기준 자연어 처리가 대세

#### (1) Transformer
> Transformer 모델은 자연어 처리(NLP) 분야에서 매우 강력한 모델 구조로, Pytorch를 통해 구현할 수 있습니다. 이 두 가지는 NLP 또는 다른 고급 딥러닝 애플리케이션에 특히 유용합니다.

- 자연어 처리(NLP) 모델의 한 종류로, 주로 딥러닝과 Pytorch를 활용해 학습합니다.
- BERT, GPT 등의 모델을 이해하고 구현해 봅니다.

- [🤗 Transformers (huggingface.co)](https://huggingface.co/docs/transformers/main/ko/index)에서 튜토리얼 내용까지
- [🤗Transformers (신경망 언어모델 라이브러리) 강좌 - WikiDocs](https://wikidocs.net/book/8056)

#### (2) 종합
- [딥 러닝을 이용한 자연어 처리 입문 - WikiDocs](https://wikidocs.net/book/2155)



### 5) 파이프라인
#### (1) Langchain
> 최근 개발된 도구로, 언어 모델을 더 쉽게 만들고 사용할 수 있게 해줍니다. 이 도구는 특히 자연어 이해와 생성 작업을 쉽게 만들어주며, 앞서 언급한 라이브러리들의 지식을 바탕으로 사용할 수 있습니다.

- 고급 NLP 라이브러리로, 자연어 처리 파이프라인을 구성하는 방법을 배웁니다.
- 다양한 NLP 태스크(질문 응답, 번역 등)를 다루는 법을 학습합니다.

- [Introduction | 🦜️🔗 LangChain](https://python.langchain.com/v0.2/docs/introduction/)의 Tutorial까지
- [<랭체인LangChain 노트> - LangChain 한국어 튜토리얼🇰🇷 - WikiDocs](https://wikidocs.net/book/14314)


### 6) IT 지식
> 실무 때 실제로 사용하게 될 환경, 공부 필요

#### (1) Git
#### (2) AWS


### 심화
> 부족하다고 느껴지는 내용 공부하기

- [00-1. 목적 - Python 데이터 분석 실무 (wikidocs.net)](https://wikidocs.net/21243) (맛보기 정도)
- Numpy: [NumPy fundamentals — NumPy v2.0 Manual](https://numpy.org/doc/stable/user/basics.html)의 내용들
- Pandas: [User Guide — pandas 2.2.2 documentation (pydata.org)](https://pandas.pydata.org/docs/user_guide/index.html)의 내용들
- Matplotlib: [Using Matplotlib — Matplotlib 3.9.0 documentation](https://matplotlib.org/stable/users/index#)의 내용들
- Scikit-Learn: [User Guide — scikit-learn 1.5.0 documentation](https://scikit-learn.org/stable/user_guide.html)
- Pytorch: [PyTorch documentation — PyTorch 2.3 documentation](https://pytorch.org/docs/stable/index.html)
- Transformer: [🤗 Transformers (huggingface.co)](https://huggingface.co/docs/transformers/main/ko/index)의 나머지 내용들 (실무에서 실제로 사용되는 항목)
- LangChain: [How-to guides | 🦜️🔗 LangChain](https://python.langchain.com/v0.2/docs/how_to/) (실무에서 실제로 사용되는 항목)
- 시각화: [Plotly Tutorial - 파이썬 시각화의 끝판왕 마스터하기 - WikiDocs](https://wikidocs.net/book/8909)


---
## 참조
[Google Machine Learning Bootcamp](https://rsvp.withgoogle.com/events/google-machine-learning-bootcamp-kr-2024)
[모집안내 - Naver boostcamp (connect.or.kr)](https://boostcamp.connect.or.kr/guide_ai.html)
[인공지능 과정 - 카카오테크 부트캠프 (goorm.io)](https://ktb.goorm.io/ai)
[DACON : 인공지능 경진대회 플랫폼 데이콘 Data Science AI Competitions - DACON](https://dacon.io/)
[Kaggle: Your Machine Learning and Data Science Community](https://www.kaggle.com/)

---
## 참조
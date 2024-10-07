---
title: "[AI] 사이킷런 (Scikit-Learn)"
excerpt: 에 대한 문서
categories:
  - Scikit-Learn
tags:
  - Software-Development
  - Data
  - AI
  - Machine-Learning
  - Python
  - Scikit-Learn
last_modified_at: 2024-03-01T00:00:00-00:00
link: https://scikit-learn.org/stable/
상위 항목: "[[machine_learning_development|머신 러닝 구현 (Machine Learning Development)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

**하위 항목**
- [[scikit_learn_grammer|사이킷런 문법 (Scikit-Learn Grammer)]]

---
이 가이드의 목적은 `scikit-learn`이 제공하는 몇 가지 주요 기능을 설명하는 것입니다. 머신 러닝 실무(모델 피팅, 예측, 교차 검증 등)에 대한 매우 기본적인 실무 지식이 있다고 가정합니다. 설치 방법은 [설치 안내](https://scikit-learn.org/stable/install.html#installation-instructions)를 참조하세요.

`Scikit-learn`은 지도 학습과 비지도 학습을 지원하는 오픈소스 머신러닝 라이브러리입니다. 또한 모델 피팅, 데이터 전처리, 모델 선택, 모델 평가 및 기타 여러 유틸리티를 위한 다양한 도구를 제공합니다.

## 1. 피팅 및 예측: 추정기 기본 사항 (Fitting and predicting: estimator basics)

- `Scikit-learn`은 [추정자](https://scikit-learn.org/stable/glossary.html#term-estimators)라는 수십 개의 내장된 머신 러닝 알고리즘과 모델을 제공합니다. 각 추정기는 [fit](https://scikit-learn.org/stable/glossary.html#term-fit) 메서드를 사용하여 일부 데이터에 맞출 수 있습니다.
- 다음은 아주 기본적인 데이터에 [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")를 맞추는 간단한 예제입니다:


```python
 from sklearn.ensemble import RandomForestClassifier
 clf = RandomForestClassifier(random_state=0)
 X = [[ 1,  2,  3],  # 2 samples, 3 features
…      [11, 12, 13]]
 y = [0, 1]  # classes of each sample
 clf.fit(X, y)
RandomForestClassifier(random_state=0)
```

- [fit](https://scikit-learn.org/stable/glossary.html#term-fit) 메서드는 일반적으로 2개의 입력을 허용합니다:
	- 샘플 행렬(또는 디자인 행렬) [X](https://scikit-learn.org/stable/glossary.html#term-X). `X`의 크기는 일반적으로 `(n_samples, n_features)`이며, 이는 샘플이 행으로, 특징이 열로 표시됨을 의미합니다.
	- 목표 값 [y](https://scikit-learn.org/stable/glossary.html#term-y)는 회귀 작업의 경우 실수, 분류 작업의 경우 정수(또는 기타 불연속적인 값 집합)입니다. 비지도 학습 작업의 경우 `y`는 지정할 필요가 없습니다. `y`는 일반적으로 `i` 번째 항목이 `X`의 `i` 번째 샘플(행)의 대상에 해당하는 1D 배열입니다.
- 일부 추정기는 희소 행렬과 같은 다른 형식으로도 작동하지만, 일반적으로 `X`와 `y`는 모두 널 배열 또는 이와 동등한 [배열 유사](https://scikit-learn.org/stable/glossary.html#term-array-like) 데이터 유형이 될 것으로 예상됩니다.
- 추정기가 적합하면 새로운 데이터의 목표 값을 예측하는 데 사용할 수 있습니다. 추정자를 다시 훈련할 필요가 없습니다:

```python
 clf.predict(X)  # predict classes of the training data
array([0, 1])
 clf.predict([[4, 5, 6], [14, 15, 16]])  # predict classes of new data
array([0, 1])
```

## 2. 트랜스포머 및 전처리기 (Transformers and pre-processors)

- 머신 러닝 워크플로는 여러 부분으로 구성되는 경우가 많습니다. 일반적인 파이프라인은 데이터를 변환하거나 전치하는 전처리 단계와 목표 값을 예측하는 최종 예측자로 구성됩니다.
- `scikit-learn`에서 전처리기와 변환기는 예측기 객체와 동일한 API를 따릅니다(실제로 모두 동일한 `BaseEstimator` 클래스에서 상속됨). 변환기 객체에는 [predict](https://scikit-learn.org/stable/glossary.html#term-predict) 메서드가 없고, 대신 새로 변환된 샘플 행렬 `X`를 출력하는 [transform](https://scikit-learn.org/stable/glossary.html#term-transform) 메서드가 있습니다:

```python
 from sklearn.preprocessing import StandardScaler
 X = [[0, 15],
…      [1, -10]]
 # scale data according to computed scaling values
 StandardScaler().fit(X).transform(X)
array([[-1.,  1.],
       [ 1., -1.]])
```

- 때로는 다른 기능에 다른 변환을 적용하고 싶을 때가 있는데, [ColumnTransformer](https://scikit-learn.org/stable/modules/compose.html#column-transformer)는 이러한 사용 사례를 위해 설계되었습니다.

## 3. 파이프라인: 전처리기와 예측기 연결하기 (Pipelines: chaining pre-processors and estimators)

- 트랜스포머와 추정자(예측자)를 하나의 통합 객체, 즉 [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")으로 결합할 수 있습니다. 파이프라인은 일반 예측자와 동일한 API를 제공합니다. `fit` 및 `predict`를 사용하여 예측에 맞추고 사용할 수 있습니다. 나중에 살펴보겠지만 파이프라인을 사용하면 데이터 유출, 즉 학습 데이터의 일부 테스트 데이터가 노출되는 것도 방지할 수 있습니다.
- 다음 예제에서는 [홍채 데이터셋을 로드](https://scikit-learn.org/stable/datasets.html#datasets)하고, 이를 훈련 세트와 테스트 세트로 분할한 다음, 테스트 데이터에 대한 파이프라인의 정확도 점수를 계산해 보겠습니다:

```python
 from sklearn.preprocessing import StandardScaler
 from sklearn.linear_model import LogisticRegression
 from sklearn.pipeline import make_pipeline
 from sklearn.datasets import load_iris
 from sklearn.model_selection import train_test_split
 from sklearn.metrics import accuracy_score
…
 # create a pipeline object
 pipe = make_pipeline(
…     StandardScaler(),
…     LogisticRegression()
… )
…
 # load the iris dataset and split it into train and test sets
 X, y = load_iris(return_X_y=True)
 X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
…
 # fit the whole pipeline
 pipe.fit(X_train, y_train)
Pipeline(steps=[('standardscaler', StandardScaler()),
                ('logisticregression', LogisticRegression())])
 # we can now use it like any other estimator
 accuracy_score(pipe.predict(X_test), y_test)
0.97…
```

## 4. 모델 평가 (Model evaluation)
- 일부 데이터에 모델을 적용한다고 해서 보이지 않는 데이터까지 잘 예측할 수 있는 것은 아닙니다. 이는 직접 평가해야 합니다. 방금 데이터 세트를 훈련 세트와 테스트 세트로 분할하는 [`train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split") 도우미를 살펴보았지만, `scikit-learn`은 모델 평가를 위한 다른 많은 도구, 특히 [교차 검증](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)을 제공합니다.
- 여기에서는 [`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate") 도우미를 사용하여 5배 교차 검증 절차를 수행하는 방법을 간략하게 보여드리겠습니다. 폴드에 대해 수동으로 반복하고, 다른 데이터 분할 전략을 사용하고, 사용자 지정 채점 함수를 사용할 수도 있습니다. 자세한 내용은 [사용자 가이드](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)를 참조하세요:

```python
 from sklearn.datasets import make_regression
 from sklearn.linear_model import LinearRegression
 from sklearn.model_selection import cross_validate
…
 X, y = make_regression(n_samples=1000, random_state=0)
 lr = LinearRegression()
…
 result = cross_validate(lr, X, y)  # defaults to 5-fold CV
 result['test_score']  # r_squared score is high because dataset is easy
array([1., 1., 1., 1., 1.])
```

## 5. 자동 매개변수 검색 (Automatic parameter searches)
- 모든 추정기에는 조정할 수 있는 매개변수(문헌에서는 하이퍼 매개변수라고도 함)가 있습니다. 추정기의 일반화 능력은 종종 몇 가지 매개변수에 따라 결정적으로 달라집니다. 예를 들어 [`RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")에는 숲의 나무 수를 결정하는 `n_estimators` 파라미터와 각 나무의 최대 깊이를 결정하는 `max_depth` 파라미터가 있습니다. 이러한 매개변수는 현재 데이터에 따라 달라지기 때문에 정확한 값이 무엇인지 명확하지 않은 경우가 많습니다.
- `Scikit-learn`은 교차 검증을 통해 최적의 파라미터 조합을 자동으로 찾아주는 도구를 제공합니다. 다음 예에서는 [`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV") 객체를 사용하여 랜덤 포레스트의 파라미터 공간을 무작위로 검색합니다. 검색이 끝나면 [`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")는 최적의 파라미터 집합을 장착한 [`RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")로 작동합니다. 자세한 내용은 [사용자 가이드](https://scikit-learn.org/stable/modules/grid_search.html#grid-search)를 참조하세요:

```python
 from sklearn.datasets import fetch_california_housing
 from sklearn.ensemble import RandomForestRegressor
 from sklearn.model_selection import RandomizedSearchCV
 from sklearn.model_selection import train_test_split
 from scipy.stats import randint
…
 X, y = fetch_california_housing(return_X_y=True)
 X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
…
 # define the parameter space that will be searched over
 param_distributions = {'n_estimators': randint(1, 5),
…                        'max_depth': randint(5, 10)}
…
 # now create a searchCV object and fit it to the data
 search = RandomizedSearchCV(estimator=RandomForestRegressor(random_state=0),
…                             n_iter=5,
…                             param_distributions=param_distributions,
…                             random_state=0)
 search.fit(X_train, y_train)
RandomizedSearchCV(estimator=RandomForestRegressor(random_state=0), n_iter=5,
                   param_distributions={'max_depth': …,
                                        'n_estimators': …},
                   random_state=0)
 search.best_params_
{'max_depth': 9, 'n_estimators': 4}

 # the search object now acts like a normal random forest estimator
 # with max_depth=9 and n_estimators=4
 search.score(X_test, y_test)
0.73…
```

> [!NOTE]
> - 실제로는 거의 항상 단일 추정기 대신 [파이프라인을 통한 검색](https://scikit-learn.org/stable/modules/grid_search.html#composite-grid-search)을 원합니다. 주된 이유 중 하나는 파이프라인을 사용하지 않고 전체 데이터 세트에 전처리 단계를 적용한 다음 어떤 종류의 교차 검증을 수행하면 학습 데이터와 테스트 데이터 간의 독립성이라는 기본 가정을 깨뜨리게 되기 때문입니다. 실제로 전체 데이터 세트를 사용하여 데이터를 사전 처리했기 때문에 테스트 세트에 대한 일부 정보를 훈련 세트에서 사용할 수 있습니다. 이로 인해 추정기의 일반화 파워가 과도하게 추정될 수 있습니다(자세한 내용은 이 [Kaggle 게시물](https://www.kaggle.com/alexisbcook/data-leakage)에서 확인할 수 있습니다).
> - 교차 검증 및 검색에 파이프라인을 사용하면 이러한 일반적인 함정에서 크게 벗어날 수 있습니다.


[Installing scikit-learn — scikit-learn 1.5.0 documentation](https://scikit-learn.org/stable/install.html)

---
## 참조


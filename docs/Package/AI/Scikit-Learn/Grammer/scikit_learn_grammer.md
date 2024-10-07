---
title: "[AI] 사이킷런 문법 (Scikit-Learn Grammer)"
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
link: https://scikit-learn.org/stable/user_guide.html
상위 항목: "[[scikit_learn_home|사이킷런 (Scikit-Learn)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

**하위 항목**
- 

---

| 패키지                             | 설명                                        |     |
| ------------------------------- | ----------------------------------------- | --- |
| `sklearn`                       | 로벌 설정을 구성하고 작업 환경에 대한 정보를 얻으세요.           |     |
| `sklearn.base`                  | 든 추정자와 다양한 유틸리티 함수를 위한 베이스 클래스입니다.        |     |
| `sklearn.calibration`           | 측 확률을 보정하는 방법.                            |     |
| `sklearn.cluster`               | 리 사용되는 비지도 클러스터링 알고리즘.                    |     |
| `sklearn.compose`               | 랜스포머로 복합 모델을 구축하기 위한 메타 추정기.              |     |
| `sklearn.covariance`            | 분산을 견고하게 추정하는 방법 및 알고리즘.                  |     |
| `sklearn.cross_decomposition`   | 차 분해를 위한 알고리즘.                            |     |
| `sklearn.datasets`              | 기 있는 데이터셋 및 인공 데이터 생성기를 로드하는 유틸리티.        |     |
| `sklearn.decomposition`         | 렬 분해 알고리즘.                                |     |
| `sklearn.discriminant_analysis` | 형 및 이차 판별 분석.                             |     |
| `sklearn.dummy`                 | 순한 규칙을 구현하는 더미 추정기.                       |     |
| `sklearn.ensemble`              | 류, 회귀 및 이상 탐지를 위한 앙상블 기반 방법.              |     |
| `sklearn.exceptions`            | cikit-learn에서 사용되는 사용자 정의 경고 및 오류.        |     |
| `sklearn.experimental`          | 험적 기능 또는 추정기의 사용을 가능하게 하는 가져오기 가능한 모듈.    |     |
| `sklearn.feature_extraction`    | aw 데이터에서 특성 추출.                           |     |
| `sklearn.feature_selection`     | 성 선택 알고리즘.                                |     |
| `sklearn.gaussian_process`      | 우시안 프로세스 기반 회귀 및 분류.                      |     |
| `sklearn.impute`                | 락된 값 대체를 위한 변환기.                          |     |
| `sklearn.inspection`            | 델 검사를 위한 도구.                              |     |
| `sklearn.isotonic`              | 이터에 대한 단조로운 적합을 얻기 위한 아이소토닉 회귀.           |     |
| `sklearn.kernel_approximation`  | 리에 변환 및 카운트 스케치를 기반으로 한 근사 커널 특성 맵.       |     |
| `sklearn.kernel_ridge`          | 널 릿지 회귀.                                  |     |
| `sklearn.linear_model`          | 양한 선형 모델.                                 |     |
| `sklearn.manifold`              | 이터 임베딩 기법.                                |     |
| `sklearn.metrics`               | 수 함수, 성능 지표, 쌍별 지표 및 거리 계산.               |     |
| `sklearn.mixture`               | 합 모델링 알고리즘                                |     |
| `sklearn.model_selection`       | 델 선택을 위한 도구, 예를 들어 교차 검증 및 하이퍼파라미터 튜닝.    |     |
| `sklearn.multiclass`            | 티클래스 학습 알고리즘.                             |     |
| `sklearn.multioutput`           | 중 출력 회귀 및 분류.                             |     |
| `sklearn.naive_bayes`           | 이브 베이즈 알고리즘.                              |     |
| `sklearn.neighbors`             | 최근접 이웃 알고리즘.                              |     |
| `sklearn.neural_network`        | 경망 기반 모델.                                 |     |
| `sklearn.pipeline`              | 합 추정기를 변환 및 추정기의 체인으로 구성하는 유틸리티.          |     |
| `sklearn.preprocessing`         | 이터 전처리를 위한 스케일링, 중심화, 정규화, 이진화 등 다양한 메서드. |     |
| `sklearn.random_projection`     | 랜덤 프로젝션 변환기.                              |     |
| `sklearn.semi_supervised`       | 준지도 학습 알고리즘.                              |     |
| `sklearn.svm`                   | 서포트 벡터 머신 알고리즘.                           |     |
| `sklearn.tree`                  | 의사 결정 트리 기반 모델을 사용한 분류 및 회귀.              |     |
| `sklearn.utils`                 | 개발을 도와주는 다양한 유틸리티.                        |     |


## 1. `sklearn`
- 글로벌 설정을 구성하고 작업 환경에 대한 정보를 얻으세요.

| 하위 항목                                                                                                                                             | 설명                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`config_context`](https://scikit-learn.org/stable/modules/generated/sklearn.config_context.html#sklearn.config_context "sklearn.config_context") | 글로벌 scikit-learn 구성을 위한 컨텍스트 관리자.                                                                                                                   |
| [`get_config`](https://scikit-learn.org/stable/modules/generated/sklearn.get_config.html#sklearn.get_config "sklearn.get_config")                 | [`set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")로 설정한 구성의 현재 값 검색. |
| [`set_config`](https://scikit-learn.org/stable/modules/generated/sklearn.set_config.html#sklearn.set_config "sklearn.set_config")                 | 글로벌 scikit-learn 구성 설정.                                                                                                                             |
| [`show_versions`](https://scikit-learn.org/stable/modules/generated/sklearn.show_versions.html#sklearn.show_versions "sklearn.show_versions")     | 유용한 디버깅 정보 인쇄"                                                                                                                                      |

## 2. `sklearn.base`
- 모든 추정자와 다양한 유틸리티 함수를 위한 베이스 클래스입니다.

| 하위 항목                                                                                                                                                                                                                                | 설명                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- |
| [`BaseEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")                                                                         | 스킷-학습의 모든 추정자를 위한 베이스 클래스입니다.                 |
| [`BiclusterMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BiclusterMixin.html#sklearn.base.BiclusterMixin "sklearn.base.BiclusterMixin")                                                                     | scikit-learn의 모든 바이클러스터 추정자에 대한 믹스인 클래스입니다.   |
| [`ClassNamePrefixFeaturesOutMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassNamePrefixFeaturesOutMixin.html#sklearn.base.ClassNamePrefixFeaturesOutMixin "sklearn.base.ClassNamePrefixFeaturesOutMixin") | 접두사를 추가하여 자체 이름을 생성하는 트랜스포머용 믹스인 클래스입니다.      |
| [`ClassifierMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#sklearn.base.ClassifierMixin "sklearn.base.ClassifierMixin")                                                                 | 스키킷 학습의 모든 분류자를 위한 믹스인 클래스입니다.                |
| [`ClusterMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClusterMixin.html#sklearn.base.ClusterMixin "sklearn.base.ClusterMixin")                                                                             | scikit-learn의 모든 군집 추정자에 대한 믹스인 클래스입니다.       |
| [`DensityMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.DensityMixin.html#sklearn.base.DensityMixin "sklearn.base.DensityMixin")                                                                             | scikit-learn의 모든 밀도 추정자에 대한 믹스인 클래스입니다.       |
| [`MetaEstimatorMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.MetaEstimatorMixin.html#sklearn.base.MetaEstimatorMixin "sklearn.base.MetaEstimatorMixin")                                                     | scikit-learn의 모든 메타 추정자에 대한 믹스인 클래스입니다.       |
| [`OneToOneFeatureMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.OneToOneFeatureMixin.html#sklearn.base.OneToOneFeatureMixin "sklearn.base.OneToOneFeatureMixin")                                             | 간단한 트랜스포머에 대해 `get_feature_names_out`을 제공합니다. |
| [`OutlierMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.OutlierMixin.html#sklearn.base.OutlierMixin "sklearn.base.OutlierMixin")                                                                             | scikit-learn의 모든 이상값 감지 추정자에 대한 믹스인 클래스입니다.   |
| [`RegressorMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.RegressorMixin.html#sklearn.base.RegressorMixin "sklearn.base.RegressorMixin")                                                                     | scikit-learn의 모든 회귀 추정자에 대한 믹스인 클래스입니다.       |
| [`TransformerMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#sklearn.base.TransformerMixin "sklearn.base.TransformerMixin")                                                             | scikit-learn의 모든 트랜스포머에 대한 믹스인 클래스입니다.        |
| [`clone`](https://scikit-learn.org/stable/modules/generated/sklearn.base.clone.html#sklearn.base.clone "sklearn.base.clone")                                                                                                         | 동일한 매개 변수를 사용하여 새로운 비적합 추정기를 구축합니다.           |
| [`is_classifier`](https://scikit-learn.org/stable/modules/generated/sklearn.base.is_classifier.html#sklearn.base.is_classifier "sklearn.base.is_classifier")                                                                         | 주어진 추정자가 (아마도) 분류자인 경우 True를 반환합니다.           |
| [`is_regressor`](https://scikit-learn.org/stable/modules/generated/sklearn.base.is_regressor.html#sklearn.base.is_regressor "sklearn.base.is_regressor")                                                                             | 주어진 추정자가 (아마도) 회귀자인 경우 True를 반환합니다.           |

## 3. `sklearn.calibration`
- 예측 확률을 보정하는 방법.
> **자세한 내용은 [확률 보정](https://scikit-learn.org/stable/modules/calibration.html#calibration) 섹션을 참조하세요.

| 하위 항목                                                                                                                                                                                                                 | 설명                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| [`CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV") | 등방 회귀 또는 로지스틱 회귀를 사용한 확률 보정.   |
| [`calibration_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.calibration_curve.html#sklearn.calibration.calibration_curve "sklearn.calibration.calibration_curve")                     | 보정 곡선에 대한 실제 확률과 예측 확률을 계산합니다. |

### 1) 시각화 (Visualization)

| 하위 항목                                                                                                                                                                                                 | 설명                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| [`CalibrationDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay "sklearn.calibration.CalibrationDisplay") | 보정 곡선(신뢰도 다이어그램이라고도 함) 시각화. |

## 4. `sklearn.cluster`
- 널리 사용되는 비지도 클러스터링 알고리즘.

> **자세한 내용**은 [클러스터링](https://scikit-learn.org/stable/modules/clustering.html#clustering) 및 [바이클러스터링](https://scikit-learn.org/stable/modules/biclustering.html#biclustering) 섹션을 참조하세요.

| 하위 항목                                                                                                                                                                                                         | 설명                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| [`AffinityPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation "sklearn.cluster.AffinityPropagation")                 | 데이터의 애피니티 전파 클러스터링 수행.            |
| [`AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering") | 병합 클러스터링.                         |
| [`Birch`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch")                                                                         | BIRCH 클러스터링 알고리즘 구현.              |
| [`BisectingKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.BisectingKMeans.html#sklearn.cluster.BisectingKMeans "sklearn.cluster.BisectingKMeans")                                 | 이분 K-평균 클러스터링.                    |
| [`DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN "sklearn.cluster.DBSCAN")                                                                     | 벡터 배열 또는 거리 행렬에서 DBSCAN 클러스터링 수행. |
| [`FeatureAgglomeration`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration "sklearn.cluster.FeatureAgglomeration")             | 특성 병합.                            |
| [`HDBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.HDBSCAN.html#sklearn.cluster.HDBSCAN "sklearn.cluster.HDBSCAN")                                                                 | 계층적 밀도 기반 클러스터링 사용.               |
| [`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans")                                                                     | K-평균 클러스터링.                       |
| [`MeanShift`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MeanShift.html#sklearn.cluster.MeanShift "sklearn.cluster.MeanShift")                                                         | 평면 커널을 사용하는 평균 이동 클러스터링.          |
| [`MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans "sklearn.cluster.MiniBatchKMeans")                                 | 미니 배치 K-평균 클러스터링.                 |
| [`OPTICS`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html#sklearn.cluster.OPTICS "sklearn.cluster.OPTICS")                                                                     | 벡터 배열에서 클러스터링 구조 추정.              |
| [`SpectralBiclustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralBiclustering.html#sklearn.cluster.SpectralBiclustering "sklearn.cluster.SpectralBiclustering")             | 스펙트럼 바이클러스터링 (Kluger, 2003).      |
| [`SpectralClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralClustering.html#sklearn.cluster.SpectralClustering "sklearn.cluster.SpectralClustering")                     | 정규화된 라플라시안의 투영에 클러스터링 적용.         |
| [`SpectralCoclustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.SpectralCoclustering.html#sklearn.cluster.SpectralCoclustering "sklearn.cluster.SpectralCoclustering")             | 스펙트럼 코클러스터링 알고리즘 (Dhillon, 2001). |
| [`affinity_propagation`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.affinity_propagation.html#sklearn.cluster.affinity_propagation "sklearn.cluster.affinity_propagation")             | 데이터의 애피니티 전파 클러스터링 수행.            |
| [`cluster_optics_dbscan`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.cluster_optics_dbscan.html#sklearn.cluster.cluster_optics_dbscan "sklearn.cluster.cluster_optics_dbscan")         | 임의의 엡실론에 대한 DBSCAN 추출 수행.         |
| [`cluster_optics_xi`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.cluster_optics_xi.html#sklearn.cluster.cluster_optics_xi "sklearn.cluster.cluster_optics_xi")                         | Xi-급경사 방법에 따라 클러스터 자동 추출.         |
| [`compute_optics_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.compute_optics_graph.html#sklearn.cluster.compute_optics_graph "sklearn.cluster.compute_optics_graph")             | OPTICS 도달 가능 그래프 계산.              |
| [`dbscan`](https://scikit-learn.org/stable/modules/generated/dbscan-function.html#sklearn.cluster.dbscan "sklearn.cluster.dbscan")                                                                            | 벡터 배열 또는 거리 행렬에서 DBSCAN 클러스터링 수행. |
| [`estimate_bandwidth`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.estimate_bandwidth.html#sklearn.cluster.estimate_bandwidth "sklearn.cluster.estimate_bandwidth")                     | 평균 이동 알고리즘에 사용할 대역폭 추정.           |
| [`k_means`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.k_means.html#sklearn.cluster.k_means "sklearn.cluster.k_means")                                                                 | K-평균 클러스터링 알고리즘 수행.               |
| [`kmeans_plusplus`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.kmeans_plusplus.html#sklearn.cluster.kmeans_plusplus "sklearn.cluster.kmeans_plusplus")                                 | k-means++에 따라 n_clusters 시드 초기화.  |
| [`mean_shift`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.mean_shift.html#sklearn.cluster.mean_shift "sklearn.cluster.mean_shift")                                                     | 평면 커널을 사용하여 데이터의 평균 이동 클러스터링 수행.  |
| [`spectral_clustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.spectral_clustering.html#sklearn.cluster.spectral_clustering "sklearn.cluster.spectral_clustering")                 | 정규화된 라플라시안의 투영에 클러스터링 적용.         |
| [`ward_tree`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.ward_tree.html#sklearn.cluster.ward_tree "sklearn.cluster.ward_tree")                                                         | 특성 행렬 기반의 워드 클러스터링.               |

## 5. `sklearn.compose`
- 트랜스포머로 복합 모델을 구축하기 위한 메타 추정기.
- 이 모듈에는 현재 콘텐츠 외에도 [`파이프라인`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline") 및 [`FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")의 리퍼브 버전이 곧 추가될 예정입니다.

> 자세한 내용은 [파이프라인 및 복합 추정기](https://scikit-learn.org/stable/modules/compose.html#combining-estimators) 섹션을 참조하세요.


| 하위 항목                                                                                                                                                                                                                     | 설명                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")                                     | 배열이나 pandas DataFrame의 열에 변환기를 적용합니다.                                                                                                                                                                                 |
| [`TransformedTargetRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor") | 변환된 목표에 회귀를 수행하는 메타 추정기입니다.                                                                                                                                                                                           |
| [`make_column_selector`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_selector.html#sklearn.compose.make_column_selector "sklearn.compose.make_column_selector")                         | [`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer")와 함께 사용할 열을 선택하는 호출 가능 객체를 만듭니다. |
| [`make_column_transformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.make_column_transformer.html#sklearn.compose.make_column_transformer "sklearn.compose.make_column_transformer")             | 주어진 변환기들로부터 ColumnTransformer를 구성합니다.                                                                                                                                                                                 |

## 6. `sklearn.covariance`
- 공분산을 견고하게 추정하는 방법 및 알고리즘.
- 이들은 특정 지점 집합에서 특징의 공분산과 공분산의 역행렬로 정의된 정밀 행렬을 추정합니다. 공분산 추정은 가우시안 그래프 모델 이론과 밀접하게 관련되어 있습니다.
> 자세한 내용은 [공분산 추정](https://scikit-learn.org/stable/modules/covariance.html#covariance) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                                                          | 설명                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| [`EllipticEnvelope`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EllipticEnvelope.html#sklearn.covariance.EllipticEnvelope "sklearn.covariance.EllipticEnvelope")                     | 가우시안 분포 데이터셋에서 이상치를 감지하는 객체.       |
| [`EmpiricalCovariance`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.EmpiricalCovariance.html#sklearn.covariance.EmpiricalCovariance "sklearn.covariance.EmpiricalCovariance")         | 최대 우도 공분산 추정기.                     |
| [`GraphicalLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLasso.html#sklearn.covariance.GraphicalLasso "sklearn.covariance.GraphicalLasso")                             | l1-패널티 추정기를 사용한 희소 역공분산 추정.        |
| [`GraphicalLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.GraphicalLassoCV.html#sklearn.covariance.GraphicalLassoCV "sklearn.covariance.GraphicalLassoCV")                     | 교차 검증된 l1 패널티 선택을 사용하는 희소 역공분산 추정. |
| [`LedoitWolf`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html#sklearn.covariance.LedoitWolf "sklearn.covariance.LedoitWolf")                                             | Ledoit-Wolf 추정기.                   |
| [`MinCovDet`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.MinCovDet.html#sklearn.covariance.MinCovDet "sklearn.covariance.MinCovDet")                                                 | 최소 공분산 결정 (MCD): 공분산의 견고한 추정기.     |
| [`OAS`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.OAS.html#sklearn.covariance.OAS "sklearn.covariance.OAS")                                                                         | 오라클 근사 축소 추정기.                     |
| [`ShrunkCovariance`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ShrunkCovariance.html#sklearn.covariance.ShrunkCovariance "sklearn.covariance.ShrunkCovariance")                     | 축소된 공분산 추정기.                       |
| [`empirical_covariance`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.empirical_covariance.html#sklearn.covariance.empirical_covariance "sklearn.covariance.empirical_covariance")     | 최대 우도 공분산 추정 계산.                   |
| [`graphical_lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.graphical_lasso.html#sklearn.covariance.graphical_lasso "sklearn.covariance.graphical_lasso")                         | l1-패널티 공분산 추정기.                    |
| [`ledoit_wolf`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ledoit_wolf.html#sklearn.covariance.ledoit_wolf "sklearn.covariance.ledoit_wolf")                                         | 축소된 Ledoit-Wolf 공분산 행렬 추정.         |
| [`ledoit_wolf_shrinkage`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.ledoit_wolf_shrinkage.html#sklearn.covariance.ledoit_wolf_shrinkage "sklearn.covariance.ledoit_wolf_shrinkage") | 축소된 Ledoit-Wolf 공분산 행렬 추정.         |
| [`oas`](https://scikit-learn.org/stable/modules/generated/oas-function.html#sklearn.covariance.oas "sklearn.covariance.oas")                                                                                   | 오라클 근사 축소를 사용한 공분산 추정.             |
| [`shrunk_covariance`](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.shrunk_covariance.html#sklearn.covariance.shrunk_covariance "sklearn.covariance.shrunk_covariance")                 | 대각선에서 축소된 공분산 행렬 계산.               |

## 7. `sklearn.cross_decomposition`
- 교차 분해를 위한 알고리즘.
 > 자세한 내용은 [교차 분해](https://scikit-learn.org/stable/modules/cross_decomposition.html#cross-decomposition) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                                                     | 설명                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| [`CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")                                         | 정준 상관 분석, "Mode B" PLS로도 알려져 있습니다. |
| [`PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")     | 부분 최소 제곱 변환기 및 회귀기.                |
| [`PLSRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression") | PLS 회귀.                            |
| [`PLSSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSSVD.html#sklearn.cross_decomposition.PLSSVD "sklearn.cross_decomposition.PLSSVD")                             | 부분 최소 제곱 SVD.                      |

## 8. `sklearn.datasets`
- 인기 있는 데이터셋 및 인공 데이터 생성기를 로드하는 유틸리티.
> 자세한 내용은 [데이터셋 로딩 유틸리티](https://scikit-learn.org/stable/datasets.html#datasets) 섹션을 참조하십시오.

### 1) 로더

| 하위 항목                                                                                                                                                                                                                                    | 설명                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| [`clear_data_home`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.clear_data_home.html#sklearn.datasets.clear_data_home "sklearn.datasets.clear_data_home")                                                         | 데이터 홈 캐시의 모든 내용을 삭제합니다.                              |
| [`dump_svmlight_file`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.dump_svmlight_file.html#sklearn.datasets.dump_svmlight_file "sklearn.datasets.dump_svmlight_file")                                             | 데이터셋을 svmlight / libsvm 파일 형식으로 덤프합니다.               |
| [`fetch_20newsgroups`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups")                                             | 20개 뉴스그룹 데이터셋의 파일 이름 및 데이터를 로드합니다 (분류).              |
| [`fetch_20newsgroups_vectorized`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html#sklearn.datasets.fetch_20newsgroups_vectorized "sklearn.datasets.fetch_20newsgroups_vectorized") | 20개 뉴스그룹 데이터셋을 로드하고 벡터화합니다 (분류).                     |
| [`fetch_california_housing`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing "sklearn.datasets.fetch_california_housing")                     | 캘리포니아 주택 데이터셋을 로드합니다 (회귀).                           |
| [`fetch_covtype`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_covtype.html#sklearn.datasets.fetch_covtype "sklearn.datasets.fetch_covtype")                                                                 | 코버타입 데이터셋을 로드합니다 (분류).                               |
| [`fetch_kddcup99`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_kddcup99.html#sklearn.datasets.fetch_kddcup99 "sklearn.datasets.fetch_kddcup99")                                                             | kddcup99 데이터셋을 로드합니다 (분류).                           |
| [`fetch_lfw_pairs`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_pairs.html#sklearn.datasets.fetch_lfw_pairs "sklearn.datasets.fetch_lfw_pairs")                                                         | Labeled Faces in the Wild (LFW) 쌍 데이터셋을 로드합니다 (분류).  |
| [`fetch_lfw_people`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_people.html#sklearn.datasets.fetch_lfw_people "sklearn.datasets.fetch_lfw_people")                                                     | Labeled Faces in the Wild (LFW) 사람 데이터셋을 로드합니다 (분류). |
| [`fetch_olivetti_faces`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html#sklearn.datasets.fetch_olivetti_faces "sklearn.datasets.fetch_olivetti_faces")                                     | AT&T의 Olivetti 얼굴 데이터셋을 로드합니다 (분류).                  |
| [`fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")                                                                     | 이름 또는 데이터셋 ID로 openml에서 데이터셋을 가져옵니다.                 |
| [`fetch_rcv1`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_rcv1.html#sklearn.datasets.fetch_rcv1 "sklearn.datasets.fetch_rcv1")                                                                             | RCV1 다중 레이블 데이터셋을 로드합니다 (분류).                        |
| [`fetch_species_distributions`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_species_distributions.html#sklearn.datasets.fetch_species_distributions "sklearn.datasets.fetch_species_distributions")         | Phillips et.의 종 분포 데이터셋 로더.                          |
| [`get_data_home`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.get_data_home.html#sklearn.datasets.get_data_home "sklearn.datasets.get_data_home")                                                                 | scikit-learn 데이터 디렉토리의 경로를 반환합니다.                    |
| [`load_breast_cancer`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer "sklearn.datasets.load_breast_cancer")                                             | 유방암 위스콘신 데이터셋을 로드하고 반환합니다 (분류).                      |
| [`load_diabetes`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes "sklearn.datasets.load_diabetes")                                                                 | 당뇨병 데이터셋을 로드하고 반환합니다 (회귀).                           |
| [`load_digits`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")                                                                         | 숫자 데이터셋을 로드하고 반환합니다 (분류).                            |
| [`load_files`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_files.html#sklearn.datasets.load_files "sklearn.datasets.load_files")                                                                             | 카테고리를 하위 폴더 이름으로 하는 텍스트 파일을 로드합니다.                   |
| [`load_iris`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")                                                                                 | 아이리스 데이터셋을 로드하고 반환합니다 (분류).                          |
| [`load_linnerud`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_linnerud.html#sklearn.datasets.load_linnerud "sklearn.datasets.load_linnerud")                                                                 | 신체 운동 Linnerud 데이터셋을 로드하고 반환합니다.                     |
| [`load_sample_image`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_sample_image.html#sklearn.datasets.load_sample_image "sklearn.datasets.load_sample_image")                                                 | 단일 샘플 이미지의 넘파이 배열을 로드합니다.                            |
| [`load_sample_images`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_sample_images.html#sklearn.datasets.load_sample_images "sklearn.datasets.load_sample_images")                                             | 이미지 조작을 위한 샘플 이미지를 로드합니다.                            |
| [`load_svmlight_file`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_file.html#sklearn.datasets.load_svmlight_file "sklearn.datasets.load_svmlight_file")                                             | svmlight / libsvm 형식의 데이터셋을 희소 CSR 행렬로 로드합니다.        |
| [`load_svmlight_files`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_svmlight_files.html#sklearn.datasets.load_svmlight_files "sklearn.datasets.load_svmlight_files")                                         | SVMlight 형식의 여러 파일에서 데이터셋을 로드합니다.                    |
| [`load_wine`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine "sklearn.datasets.load_wine")                                                                                 | 와인 데이터셋을 로드하고 반환합니다 (분류).                            |


### 2) 샘플 생성기
| 하위 항목                                                                                                                                                                                                                                        | 설명                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| [`make_biclusters`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_biclusters.html#sklearn.datasets.make_biclusters "sklearn.datasets.make_biclusters")                                                             | 바이클러스터링을 위한 상수 블록 대각선 구조 배열을 생성합니다.                |
| [`make_blobs`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")                                                                                 | 클러스터링을 위한 등방성 가우시안 블롭을 생성합니다.                      |
| [`make_checkerboard`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_checkerboard.html#sklearn.datasets.make_checkerboard "sklearn.datasets.make_checkerboard")                                                     | 바이클러스터링을 위한 블록 체커보드 구조 배열을 생성합니다.                  |
| [`make_circles`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")                                                                         | 2차원에서 큰 원이 작은 원을 포함하는 구조를 만듭니다.                    |
| [`make_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")                                             | 무작위 n-클래스 분류 문제를 생성합니다.                            |
| [`make_friedman1`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_friedman1.html#sklearn.datasets.make_friedman1 "sklearn.datasets.make_friedman1")                                                                 | “Friedman #1” 회귀 문제를 생성합니다.                        |
| [`make_friedman2`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_friedman2.html#sklearn.datasets.make_friedman2 "sklearn.datasets.make_friedman2")                                                                 | “Friedman #2” 회귀 문제를 생성합니다.                        |
| [`make_friedman3`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_friedman3.html#sklearn.datasets.make_friedman3 "sklearn.datasets.make_friedman3")                                                                 | “Friedman #3” 회귀 문제를 생성합니다.                        |
| [`make_gaussian_quantiles`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_gaussian_quantiles.html#sklearn.datasets.make_gaussian_quantiles "sklearn.datasets.make_gaussian_quantiles")                             | 등방성 가우시안을 생성하고 분위수에 따라 샘플을 라벨링합니다.                 |
| [`make_hastie_10_2`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_hastie_10_2.html#sklearn.datasets.make_hastie_10_2 "sklearn.datasets.make_hastie_10_2")                                                         | Hastie et al. 2009, 예제 10.2에 사용된 이진 분류 데이터를 생성합니다. |
| [`make_low_rank_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_low_rank_matrix.html#sklearn.datasets.make_low_rank_matrix "sklearn.datasets.make_low_rank_matrix")                                         | 종 모양의 특이값을 가진 대부분 낮은 계급의 행렬을 생성합니다.                |
| [`make_moons`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#sklearn.datasets.make_moons "sklearn.datasets.make_moons")                                                                                 | 서로 겹치는 두 개의 반원 구조를 만듭니다.                           |
| [`make_multilabel_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_multilabel_classification.html#sklearn.datasets.make_multilabel_classification "sklearn.datasets.make_multilabel_classification") | 무작위 다중 레이블 분류 문제를 생성합니다.                           |
| [`make_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")                                                             | 무작위 회귀 문제를 생성합니다.                                  |
| [`make_s_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_s_curve.html#sklearn.datasets.make_s_curve "sklearn.datasets.make_s_curve")                                                                         | S 커브 데이터셋을 생성합니다.                                  |
| [`make_sparse_coded_signal`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_coded_signal.html#sklearn.datasets.make_sparse_coded_signal "sklearn.datasets.make_sparse_coded_signal")                         | 딕셔너리 요소의 희소 결합으로 신호를 생성합니다.                        |
| [`make_sparse_spd_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_spd_matrix.html#sklearn.datasets.make_sparse_spd_matrix "sklearn.datasets.make_sparse_spd_matrix")                                 | 희소 대칭 양의 정수 행렬을 생성합니다.                             |
| [`make_sparse_uncorrelated`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_sparse_uncorrelated.html#sklearn.datasets.make_sparse_uncorrelated "sklearn.datasets.make_sparse_uncorrelated")                         | 희소 비상관 설계로 무작위 회귀 문제를 생성합니다.                       |
| [`make_spd_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_spd_matrix.html#sklearn.datasets.make_spd_matrix "sklearn.datasets.make_spd_matrix")                                                             | 무작위 대칭 양의 정수 행렬을 생성합니다.                            |
| [`make_swiss_roll`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_swiss_roll.html#sklearn.datasets.make_swiss_roll "sklearn.datasets.make_swiss_roll")                                                             | 스위스 롤 데이터셋을 생성합니다.                                 |

## 9. `sklearn.decomposition`
- 행렬 분해 알고리즘.
- 여기에는 PCA, NMF, ICA 등이 포함됩니다. 이 모듈의 대부분의 알고리즘은 차원 축소 기술로 간주될 수 있습니다.
> 자세한 내용은 [신호를 구성 요소로 분해하기 (행렬 분해 문제)](https://scikit-learn.org/stable/modules/decomposition.html#decompositions) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                                                                                           | 설명                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| [`DictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.DictionaryLearning.html#sklearn.decomposition.DictionaryLearning "sklearn.decomposition.DictionaryLearning")                                     | 딕셔너리 학습.                                 |
| [`FactorAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis "sklearn.decomposition.FactorAnalysis")                                                     | 요인 분석 (FA).                              |
| [`FastICA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FastICA.html#sklearn.decomposition.FastICA "sklearn.decomposition.FastICA")                                                                                 | 독립 성분 분석을 위한 빠른 알고리즘 FastICA.            |
| [`IncrementalPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA "sklearn.decomposition.IncrementalPCA")                                                     | 증분 주성분 분석 (IPCA).                        |
| [`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")                                                                         | 커널 주성분 분석 (KPCA).                        |
| [`LatentDirichletAllocation`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html#sklearn.decomposition.LatentDirichletAllocation "sklearn.decomposition.LatentDirichletAllocation")         | 온라인 변분 베이지안 알고리즘을 사용하는 잠재 디리클레 할당 (LDA). |
| [`MiniBatchDictionaryLearning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchDictionaryLearning.html#sklearn.decomposition.MiniBatchDictionaryLearning "sklearn.decomposition.MiniBatchDictionaryLearning") | 미니 배치 딕셔너리 학습.                           |
| [`MiniBatchNMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchNMF.html#sklearn.decomposition.MiniBatchNMF "sklearn.decomposition.MiniBatchNMF")                                                             | 미니 배치 비음수 행렬 분해 (NMF).                   |
| [`MiniBatchSparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.MiniBatchSparsePCA.html#sklearn.decomposition.MiniBatchSparsePCA "sklearn.decomposition.MiniBatchSparsePCA")                                     | 미니 배치 희소 주성분 분석.                         |
| [`NMF`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html#sklearn.decomposition.NMF "sklearn.decomposition.NMF")                                                                                                 | 비음수 행렬 분해 (NMF).                         |
| [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")                                                                                                 | 주성분 분석 (PCA).                            |
| [`SparseCoder`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder "sklearn.decomposition.SparseCoder")                                                                 | 희소 인코딩.                                  |
| [`SparsePCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA "sklearn.decomposition.SparsePCA")                                                                         | 희소 주성분 분석 (SparsePCA).                   |
| [`TruncatedSVD`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD "sklearn.decomposition.TruncatedSVD")                                                             | 절단 SVD를 사용한 차원 축소 (LSA).                 |
| [`dict_learning`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning.html#sklearn.decomposition.dict_learning "sklearn.decomposition.dict_learning")                                                         | 딕셔너리 학습 행렬 분해 문제 해결.                     |
| [`dict_learning_online`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.dict_learning_online.html#sklearn.decomposition.dict_learning_online "sklearn.decomposition.dict_learning_online")                             | 온라인에서 딕셔너리 학습 행렬 분해 문제 해결.               |
| [`fastica`](https://scikit-learn.org/stable/modules/generated/fastica-function.html#sklearn.decomposition.fastica "sklearn.decomposition.fastica")                                                                                              | 빠른 독립 성분 분석 수행.                          |
| [`non_negative_factorization`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.non_negative_factorization.html#sklearn.decomposition.non_negative_factorization "sklearn.decomposition.non_negative_factorization")     | 비음수 행렬 분해 (NMF) 계산.                      |
| [`sparse_encode`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.sparse_encode.html#sklearn.decomposition.sparse_encode "sklearn.decomposition.sparse_encode")                                                         | 희소 인코딩.                                  |


## 10. `sklearn.discriminant_analysis`
- 선형 및 이차 판별 분석.
> 자세한 내용은 [선형 및 이차 판별 분석](https://scikit-learn.org/stable/modules/lda_qda.html#lda-qda) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                                                                                                                           | 설명        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| [`LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")             | 선형 판별 분석. |
| [`QuadraticDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.html#sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis "sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis") | 이차 판별 분석. |




## 11. `sklearn.dummy`
- 단순한 규칙을 구현하는 더미 추정기.
> 자세한 내용은 [평가 지표 및 스코어링: 예측 품질 정량화](https://scikit-learn.org/stable/modules/model_evaluation.html#model-evaluation) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                   | 설명                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| [`DummyClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html#sklearn.dummy.DummyClassifier "sklearn.dummy.DummyClassifier") | DummyClassifier는 입력 특징을 무시하는 예측을 만듭니다. |
| [`DummyRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html#sklearn.dummy.DummyRegressor "sklearn.dummy.DummyRegressor")     | 단순한 규칙을 사용하여 예측을 수행하는 회귀기.             |

## 12. `sklearn.ensemble`
- 분류, 회귀 및 이상 탐지를 위한 앙상블 기반 방법.
> 자세한 내용은 [앙상블: 그래디언트 부스팅, 랜덤 포레스트, 배깅, 투표, 스태킹](https://scikit-learn.org/stable/modules/ensemble.html#ensemble) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                                                                                        | 설명                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| [`AdaBoostClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html#sklearn.ensemble.AdaBoostClassifier "sklearn.ensemble.AdaBoostClassifier")                                                 | AdaBoost 분류기.                      |
| [`AdaBoostRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html#sklearn.ensemble.AdaBoostRegressor "sklearn.ensemble.AdaBoostRegressor")                                                     | AdaBoost 회귀기.                      |
| [`BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier")                                                     | 배깅 분류기.                            |
| [`BaggingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingRegressor.html#sklearn.ensemble.BaggingRegressor "sklearn.ensemble.BaggingRegressor")                                                         | 배깅 회귀기.                            |
| [`ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")                                         | 익스트라 트리 분류기.                       |
| [`ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")                                             | 익스트라 트리 회귀기.                       |
| [`GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")                 | 분류를 위한 그래디언트 부스팅.                  |
| [`GradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html#sklearn.ensemble.GradientBoostingRegressor "sklearn.ensemble.GradientBoostingRegressor")                     | 회귀를 위한 그래디언트 부스팅.                  |
| [`HistGradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier "sklearn.ensemble.HistGradientBoostingClassifier") | 히스토그램 기반 그래디언트 부스팅 분류 트리.          |
| [`HistGradientBoostingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor "sklearn.ensemble.HistGradientBoostingRegressor")     | 히스토그램 기반 그래디언트 부스팅 회귀 트리.          |
| [`IsolationForest`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html#sklearn.ensemble.IsolationForest "sklearn.ensemble.IsolationForest")                                                             | 아이솔레이션 포레스트 알고리즘.                  |
| [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")                                 | 랜덤 포레스트 분류기.                       |
| [`RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")                                     | 랜덤 포레스트 회귀기.                       |
| [`RandomTreesEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#sklearn.ensemble.RandomTreesEmbedding "sklearn.ensemble.RandomTreesEmbedding")                                         | 완전히 무작위 트리의 앙상블.                   |
| [`StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier")                                                 | 최종 분류기가 있는 추정기 스택.                 |
| [`StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor")                                                     | 최종 회귀기가 있는 추정기 스택.                 |
| [`VotingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html#sklearn.ensemble.VotingClassifier "sklearn.ensemble.VotingClassifier")                                                         | 적합되지 않은 추정기에 대한 소프트 보팅/다수결 규칙 분류기. |
| [`VotingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingRegressor.html#sklearn.ensemble.VotingRegressor "sklearn.ensemble.VotingRegressor")                                                             | 적합되지 않은 추정기에 대한 예측 보팅 회귀기.         |



## 13. `sklearn.exceptions`
- scikit-learn에서 사용되는 사용자 정의 경고 및 오류.

| 하위 항목                                                                                                                                                                                                                              | 설명                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| [`ConvergenceWarning`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.ConvergenceWarning.html#sklearn.exceptions.ConvergenceWarning "sklearn.exceptions.ConvergenceWarning")                                 | 수렴 문제를 포착하기 위한 사용자 정의 경고                |
| [`DataConversionWarning`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.DataConversionWarning.html#sklearn.exceptions.DataConversionWarning "sklearn.exceptions.DataConversionWarning")                     | 코드에서 암묵적인 데이터 변환이 발생할 때 사용되는 경고.        |
| [`DataDimensionalityWarning`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.DataDimensionalityWarning.html#sklearn.exceptions.DataDimensionalityWarning "sklearn.exceptions.DataDimensionalityWarning")     | 데이터 차원 문제의 잠재적 문제를 알리기 위한 사용자 정의 경고.    |
| [`EfficiencyWarning`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.EfficiencyWarning.html#sklearn.exceptions.EfficiencyWarning "sklearn.exceptions.EfficiencyWarning")                                     | 비효율적인 계산을 사용자에게 알리기 위해 사용되는 경고.         |
| [`FitFailedWarning`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.FitFailedWarning.html#sklearn.exceptions.FitFailedWarning "sklearn.exceptions.FitFailedWarning")                                         | 추정기 적합 중 오류가 발생했을 때 사용되는 경고 클래스.        |
| [`InconsistentVersionWarning`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.InconsistentVersionWarning.html#sklearn.exceptions.InconsistentVersionWarning "sklearn.exceptions.InconsistentVersionWarning") | 추정기가 일관되지 않은 버전으로 unpickled될 때 발생하는 경고. |
| [`NotFittedError`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.NotFittedError.html#sklearn.exceptions.NotFittedError "sklearn.exceptions.NotFittedError")                                                 | 추정기를 적합하기 전에 사용했을 때 발생하는 예외 클래스.        |
| [`UndefinedMetricWarning`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.UndefinedMetricWarning.html#sklearn.exceptions.UndefinedMetricWarning "sklearn.exceptions.UndefinedMetricWarning")                 | 메트릭이 유효하지 않을 때 사용되는 경고.                 |

## 14. `sklearn.experimental`
- 실험적 기능 또는 추정기의 사용을 가능하게 하는 가져오기 가능한 모듈.

> [!warning] 
> - 실험적인 기능과 추정기는 중단 주기에 해당하지 않습니다. 사용 시 주의하십시오!

| 하위 항목                                                                                                                                                                                                                                   | 설명                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| [`enable_halving_search_cv`](https://scikit-learn.org/stable/modules/generated/sklearn.experimental.enable_halving_search_cv.html#module-sklearn.experimental.enable_halving_search_cv "sklearn.experimental.enable_halving_search_cv") | Successive Halving 탐색-추정기를 활성화합니다. |
| [`enable_iterative_imputer`](https://scikit-learn.org/stable/modules/generated/sklearn.experimental.enable_iterative_imputer.html#module-sklearn.experimental.enable_iterative_imputer "sklearn.experimental.enable_iterative_imputer") | IterativeImputer를 활성화합니다.          |

## 15. `sklearn.feature_extraction`
- Raw 데이터에서 특성 추출.
> 자세한 내용은 [특성 추출](https://scikit-learn.org/stable/modules/feature_extraction.html#feature-extraction) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                                                      | 설명                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| [`DictVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer "sklearn.feature_extraction.DictVectorizer") | 특성-값 매핑 목록을 벡터로 변환합니다.  |
| [`FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher")     | 특성 해싱, 일명 해싱 트릭을 구현합니다. |

### 1) From Image

- 이미지에서 특성을 추출하는 유틸리티.

| 하위 항목                                                                                                                                                                                                                                                                                  | 설명                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| [`image.PatchExtractor`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.PatchExtractor.html#sklearn.feature_extraction.image.PatchExtractor "sklearn.feature_extraction.image.PatchExtractor")                                                     | 이미지 모음에서 패치를 추출합니다.     |
| [`image.extract_patches_2d`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.extract_patches_2d.html#sklearn.feature_extraction.image.extract_patches_2d "sklearn.feature_extraction.image.extract_patches_2d")                                     | 2D 이미지를 패치 모음으로 재구성합니다. |
| [`image.grid_to_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.grid_to_graph.html#sklearn.feature_extraction.image.grid_to_graph "sklearn.feature_extraction.image.grid_to_graph")                                                         | 픽셀 간 연결 그래프.            |
| [`image.img_to_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.img_to_graph.html#sklearn.feature_extraction.image.img_to_graph "sklearn.feature_extraction.image.img_to_graph")                                                             | 픽셀 간 그래디언트 연결 그래프.      |
| [`image.reconstruct_from_patches_2d`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.reconstruct_from_patches_2d.html#sklearn.feature_extraction.image.reconstruct_from_patches_2d "sklearn.feature_extraction.image.reconstruct_from_patches_2d") | 모든 패치로부터 이미지를 재구성합니다.   |

### 2) From Text

- 텍스트 문서에서 특성 벡터를 생성하는 유틸리티.

| 하위 항목                                                                                                                                                                                                                                      | 설명                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------- |
| [`text.CountVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer "sklearn.feature_extraction.text.CountVectorizer")         | 텍스트 문서 모음을 토큰 수의 행렬로 변환합니다.           |
| [`text.HashingVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer") | 텍스트 문서 모음을 토큰 발생 행렬로 변환합니다.           |
| [`text.TfidfTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer "sklearn.feature_extraction.text.TfidfTransformer")     | 카운트 행렬을 정규화된 tf 또는 tf-idf 표현으로 변환합니다. |
| [`text.TfidfVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html#sklearn.feature_extraction.text.TfidfVectorizer "sklearn.feature_extraction.text.TfidfVectorizer")         | 원시 문서 모음을 TF-IDF 특성의 행렬로 변환합니다.       |


## 16. `sklearn.feature_selection`
- 특성 선택 알고리즘.
- 여기에는 단변량 필터 선택 방법 및 재귀적 특성 제거 알고리즘이 포함됩니다.
> 자세한 내용은 [특성 선택](https://scikit-learn.org/stable/modules/feature_selection.html#feature-selection) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                                                                                               | 설명                                  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| [`GenericUnivariateSelect`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.GenericUnivariateSelect.html#sklearn.feature_selection.GenericUnivariateSelect "sklearn.feature_selection.GenericUnivariateSelect")         | 구성 가능한 전략을 사용하는 단변량 특성 선택기.         |
| [`RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE "sklearn.feature_selection.RFE")                                                                                         | 재귀적 특성 제거를 통한 특성 순위 매기기.            |
| [`RFECV`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFECV.html#sklearn.feature_selection.RFECV "sklearn.feature_selection.RFECV")                                                                                 | 교차 검증을 사용한 재귀적 특성 제거를 통한 특성 선택.     |
| [`SelectFdr`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFdr.html#sklearn.feature_selection.SelectFdr "sklearn.feature_selection.SelectFdr")                                                                 | 필터: 추정된 거짓 발견률에 대한 p-값 선택.          |
| [`SelectFpr`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFpr.html#sklearn.feature_selection.SelectFpr "sklearn.feature_selection.SelectFpr")                                                                 | 필터: FPR 테스트를 기반으로 알파 이하의 p-값 선택.    |
| [`SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")                                         | 중요도 가중치를 기반으로 특성을 선택하는 메타 변환기.      |
| [`SelectFwe`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFwe.html#sklearn.feature_selection.SelectFwe "sklearn.feature_selection.SelectFwe")                                                                 | 필터: 가족별 오류율에 해당하는 p-값 선택.           |
| [`SelectKBest`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest "sklearn.feature_selection.SelectKBest")                                                         | 가장 높은 점수를 받은 k개의 특성 선택.             |
| [`SelectPercentile`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile "sklearn.feature_selection.SelectPercentile")                                     | 가장 높은 점수의 백분위수에 따른 특성 선택.           |
| [`SelectorMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectorMixin.html#sklearn.feature_selection.SelectorMixin "sklearn.feature_selection.SelectorMixin")                                                 | 지원 마스크가 주어진 경우 특성 선택을 수행하는 변환기 믹스인. |
| [`SequentialFeatureSelector`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SequentialFeatureSelector.html#sklearn.feature_selection.SequentialFeatureSelector "sklearn.feature_selection.SequentialFeatureSelector") | 순차적 특성 선택을 수행하는 변환기.                |
| [`VarianceThreshold`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.VarianceThreshold.html#sklearn.feature_selection.VarianceThreshold "sklearn.feature_selection.VarianceThreshold")                                 | 모든 저분산 특성을 제거하는 특성 선택기.             |
| [`chi2`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html#sklearn.feature_selection.chi2 "sklearn.feature_selection.chi2")                                                                                     | 각 비음수 특성과 클래스 간의 카이제곱 통계량을 계산합니다.   |
| [`f_classif`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_classif.html#sklearn.feature_selection.f_classif "sklearn.feature_selection.f_classif")                                                                 | 제공된 샘플에 대한 ANOVA F-값을 계산합니다.        |
| [`f_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html#sklearn.feature_selection.f_regression "sklearn.feature_selection.f_regression")                                                     | F-통계량 및 p-값을 반환하는 단변량 선형 회귀 테스트.    |
| [`mutual_info_classif`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_classif.html#sklearn.feature_selection.mutual_info_classif "sklearn.feature_selection.mutual_info_classif")                         | 이산 목표 변수에 대한 상호 정보를 추정합니다.          |
| [`mutual_info_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.mutual_info_regression.html#sklearn.feature_selection.mutual_info_regression "sklearn.feature_selection.mutual_info_regression")             | 연속 목표 변수에 대한 상호 정보를 추정합니다.          |
| [`r_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.r_regression.html#sklearn.feature_selection.r_regression "sklearn.feature_selection.r_regression")                                                     | 각 특성과 목표 간의 피어슨 r을 계산합니다.           |


## 17. `sklearn.gaussian_process`
- 가우시안 프로세스 기반 회귀 및 분류.
> 자세한 내용은 [가우시안 프로세스](https://scikit-learn.org/stable/modules/gaussian_process.html#gaussian-process) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                                                                                            | 설명                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| [`GaussianProcessClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier") | 라플라스 근사를 기반으로 한 가우시안 프로세스 분류 (GPC). |
| [`GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")     | 가우시안 프로세스 회귀 (GPR).                 |

### 1) 커널 (Kernel)

- 연산자로 결합할 수 있으며 가우시안 프로세스에서 사용할 수 있는 커널 집합.

| 하위 항목                                                                                                                                                                                                                                            | 설명                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------ |
| [`kernels.CompoundKernel`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.CompoundKernel.html#sklearn.gaussian_process.kernels.CompoundKernel "sklearn.gaussian_process.kernels.CompoundKernel")             | 다른 커널 집합으로 구성된 커널.                                     |
| [`kernels.ConstantKernel`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.ConstantKernel.html#sklearn.gaussian_process.kernels.ConstantKernel "sklearn.gaussian_process.kernels.ConstantKernel")             | 상수 커널.                                                 |
| [`kernels.DotProduct`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.DotProduct.html#sklearn.gaussian_process.kernels.DotProduct "sklearn.gaussian_process.kernels.DotProduct")                             | 도트-프로덕트 커널.                                            |
| [`kernels.ExpSineSquared`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.ExpSineSquared.html#sklearn.gaussian_process.kernels.ExpSineSquared "sklearn.gaussian_process.kernels.ExpSineSquared")             | Exp-사인-제곱 커널 (주기적 커널).                                 |
| [`kernels.Exponentiation`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Exponentiation.html#sklearn.gaussian_process.kernels.Exponentiation "sklearn.gaussian_process.kernels.Exponentiation")             | Exponentiation 커널은 하나의 기본 커널과 스칼라 매개변수 𝑝를 사용하여 결합합니다. |
| [`kernels.Hyperparameter`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Hyperparameter.html#sklearn.gaussian_process.kernels.Hyperparameter "sklearn.gaussian_process.kernels.Hyperparameter")             | namedtuple 형태로 된 커널 하이퍼파라미터의 명세.                       |
| [`kernels.Kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Kernel.html#sklearn.gaussian_process.kernels.Kernel "sklearn.gaussian_process.kernels.Kernel")                                             | 모든 커널의 기본 클래스.                                         |
| [`kernels.Matern`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Matern.html#sklearn.gaussian_process.kernels.Matern "sklearn.gaussian_process.kernels.Matern")                                             | 마테른 커널.                                                |
| [`kernels.PairwiseKernel`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.PairwiseKernel.html#sklearn.gaussian_process.kernels.PairwiseKernel "sklearn.gaussian_process.kernels.PairwiseKernel")             | sklearn.metrics.pairwise의 커널에 대한 래퍼.                   |
| [`kernels.Product`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Product.html#sklearn.gaussian_process.kernels.Product "sklearn.gaussian_process.kernels.Product")                                         | `Product` 커널은 두 개의 커널 𝑘1과 𝑘2를 사용하여 결합합니다.            |
| [`kernels.RBF`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RBF.html#sklearn.gaussian_process.kernels.RBF "sklearn.gaussian_process.kernels.RBF")                                                         | 방사 기저 함수 커널 (제곱-지수 커널).                                |
| [`kernels.RationalQuadratic`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.RationalQuadratic.html#sklearn.gaussian_process.kernels.RationalQuadratic "sklearn.gaussian_process.kernels.RationalQuadratic") | 유리적 제곱 커널.                                             |
| [`kernels.Sum`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Sum.html#sklearn.gaussian_process.kernels.Sum "sklearn.gaussian_process.kernels.Sum")                                                         | `Sum` 커널은 두 개의 커널 𝑘1과 𝑘2를 사용하여 결합합니다.                |
| [`kernels.WhiteKernel`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.WhiteKernel.html#sklearn.gaussian_process.kernels.WhiteKernel "sklearn.gaussian_process.kernels.WhiteKernel")                         | 화이트 커널.                                                |



## 18. `sklearn.impute`
- 누락된 값 대체를 위한 변환기.
> 자세한 내용은 [누락된 값의 대체](https://scikit-learn.org/stable/modules/impute.html#impute) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                          | 설명                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------- |
| [`IterativeImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer "sklearn.impute.IterativeImputer") | 모든 다른 특성에서 각 특성을 추정하는 다변량 대체기.    |
| [`KNNImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer.html#sklearn.impute.KNNImputer "sklearn.impute.KNNImputer")                         | k-최근접 이웃을 사용하여 누락된 값을 완성하는 대체기.   |
| [`MissingIndicator`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator "sklearn.impute.MissingIndicator") | 누락된 값에 대한 이진 지표.                  |
| [`SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")             | 단순한 전략을 사용하여 누락된 값을 완성하는 단변량 대체기. |



## 19. `sklearn.inspection`
- 모델 검사를 위한 도구.
> 자세한 내용은 [검사](https://scikit-learn.org/stable/inspection.html#inspection) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                                                              | 설명                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`partial_dependence`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.partial_dependence.html#sklearn.inspection.partial_dependence "sklearn.inspection.partial_dependence")                 | 특성의 부분 의존성.                                                                                                                                               |
| [`permutation_importance`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance") | 특성 평가를 위한 순열 중요도 [Rd9e56ef97513-BRE](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#rd9e56ef97513-bre). |

### 1) 시각화 (Visualization)

| 하위 항목                                                                                                                                                                                                                      | 설명               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| [`DecisionBoundaryDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay "sklearn.inspection.DecisionBoundaryDisplay")     | 결정 경계 시각화.       |
| [`PartialDependenceDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.PartialDependenceDisplay.html#sklearn.inspection.PartialDependenceDisplay "sklearn.inspection.PartialDependenceDisplay") | 부분 의존성 플롯 (PDP). |


## 20. `sklearn.isotonic`
- 데이터에 대한 단조로운 적합을 얻기 위한 아이소토닉 회귀.
> 자세한 내용은 [아이소토닉 회귀](https://scikit-learn.org/stable/modules/isotonic.html#isotonic) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                                            | 설명                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------ |
| [`IsotonicRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.IsotonicRegression.html#sklearn.isotonic.IsotonicRegression "sklearn.isotonic.IsotonicRegression")     | 아이소토닉 회귀 모델.                   |
| [`check_increasing`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.check_increasing.html#sklearn.isotonic.check_increasing "sklearn.isotonic.check_increasing")             | y가 x와 단조롭게 상관되어 있는지 여부를 결정합니다. |
| [`isotonic_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.isotonic.isotonic_regression.html#sklearn.isotonic.isotonic_regression "sklearn.isotonic.isotonic_regression") | 아이소토닉 회귀 모델을 풉니다.              |


## 21. `sklearn.kernel_approximation`
- 푸리에 변환 및 카운트 스케치를 기반으로 한 근사 커널 특성 맵.
> 자세한 내용은 [커널 근사화](https://scikit-learn.org/stable/modules/kernel_approximation.html#kernel-approximation) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                                                                                        | 설명                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| [`AdditiveChi2Sampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.AdditiveChi2Sampler.html#sklearn.kernel_approximation.AdditiveChi2Sampler "sklearn.kernel_approximation.AdditiveChi2Sampler")         | Additive chi2 커널의 근사 특성 맵.          |
| [`Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")                                                     | 훈련 데이터의 하위 집합을 사용하여 커널 맵을 근사합니다.    |
| [`PolynomialCountSketch`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.PolynomialCountSketch.html#sklearn.kernel_approximation.PolynomialCountSketch "sklearn.kernel_approximation.PolynomialCountSketch") | 텐서 스케치를 통한 다항식 커널 근사.               |
| [`RBFSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler "sklearn.kernel_approximation.RBFSampler")                                             | 랜덤 푸리에 특성을 사용하여 RBF 커널 특성 맵을 근사합니다. |
| [`SkewedChi2Sampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.SkewedChi2Sampler.html#sklearn.kernel_approximation.SkewedChi2Sampler "sklearn.kernel_approximation.SkewedChi2Sampler")                 | "Skewed chi-squared" 커널의 근사 특성 맵.   |


## 22. `sklearn.kernel_ridge`
- 커널 릿지 회귀.
> 자세한 내용은 [커널 릿지 회귀](https://scikit-learn.org/stable/modules/kernel_ridge.html#kernel-ridge) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                        | 설명        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| [`KernelRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge") | 커널 릿지 회귀. |


## 23. `sklearn.linear_model`
- 다양한 선형 모델.
> 자세한 내용은 [선형 모델](https://scikit-learn.org/stable/modules/linear_model.html#linear-model) 섹션을 참조하십시오.

- 다음 하위 섹션은 대략적인 가이드라인일 뿐입니다. 동일한 추정기가 매개변수에 따라 여러 범주에 속할 수 있습니다.

### 1) 선형 분류기 (Linear classifiers)

| 하위 항목                                                                                                                                                                                                                                        | 설명                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")                                     | 로지스틱 회귀 (일명 로짓, MaxEnt) 분류기.          |
| [`LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")                             | 로지스틱 회귀 CV (일명 로짓, MaxEnt) 분류기.       |
| [`PassiveAggressiveClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveClassifier.html#sklearn.linear_model.PassiveAggressiveClassifier "sklearn.linear_model.PassiveAggressiveClassifier") | 패시브 어그레시브 분류기.                        |
| [`Perceptron`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron "sklearn.linear_model.Perceptron")                                                                     | 선형 퍼셉트론 분류기.                          |
| [`RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")                                                 | 릿지 회귀를 사용하는 분류기.                      |
| [`RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")                                         | 내장 교차 검증이 있는 릿지 분류기.                  |
| [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")                                                         | SGD 훈련을 사용하는 선형 분류기 (SVM, 로지스틱 회귀 등). |
| [`SGDOneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDOneClassSVM.html#sklearn.linear_model.SGDOneClassSVM "sklearn.linear_model.SGDOneClassSVM")                                                     | 확률적 경사 하강법을 사용하여 선형 단일 클래스 SVM 해결.    |

### 2) 고전적 선형 회귀기 (Classical linear regressors)

| 하위 항목                                                                                                                                                                                            | 설명                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------- |
| [`LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression") | 일반 최소 제곱 선형 회귀.                         |
| [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")                                             | l2 정규화가 있는 선형 최소 제곱.                    |
| [`RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")                                     | 내장 교차 검증이 있는 릿지 회귀.                     |
| [`SGDRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html#sklearn.linear_model.SGDRegressor "sklearn.linear_model.SGDRegressor")                 | SGD를 사용하여 정규화된 경험적 손실을 최소화하여 피팅된 선형 모델. |

### 3) 변수 선택이 가능한 회귀기 (Regressors with variable selection)

- 다음 추정기는 변수 선택 피팅 절차가 내장되어 있지만, L1 또는 엘라스틱넷 패널티를 사용하는 모든 추정기도 변수 선택을 수행합니다. 일반적으로 `SGDRegressor` 또는 적절한 패널티를 사용하는 [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier)입니다.

| 하위 항목                                                                                                                                                                                                                                        | 설명                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| [`ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")                                                                     | L1 및 L2 프라이어를 결합한 정규화가 있는 선형 회귀.            |
| [`ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")                                                             | 정규화 경로를 따라 반복 피팅이 있는 엘라스틱넷 모델.              |
| [`Lars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lars.html#sklearn.linear_model.Lars "sklearn.linear_model.Lars")                                                                                             | 최소 각도 회귀 모델(LARS).                          |
| [`LarsCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LarsCV.html#sklearn.linear_model.LarsCV "sklearn.linear_model.LarsCV")                                                                                     | 교차 검증된 최소 각도 회귀 모델.                         |
| [`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")                                                                                         | L1 프라이어를 사용하여 정규화된 선형 모델 (라쏘).              |
| [`LassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html#sklearn.linear_model.LassoCV "sklearn.linear_model.LassoCV")                                                                                 | 정규화 경로를 따라 반복 피팅이 있는 라쏘 선형 모델.              |
| [`LassoLars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html#sklearn.linear_model.LassoLars "sklearn.linear_model.LassoLars")                                                                         | 최소 각도 회귀를 사용하여 피팅된 라쏘 모델.                   |
| [`LassoLarsCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsCV.html#sklearn.linear_model.LassoLarsCV "sklearn.linear_model.LassoLarsCV")                                                                 | LARS 알고리즘을 사용하는 교차 검증된 라쏘 모델.               |
| [`LassoLarsIC`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLarsIC.html#sklearn.linear_model.LassoLarsIC "sklearn.linear_model.LassoLarsIC")                                                                 | 모델 선택을 위해 BIC 또는 AIC를 사용하여 LARS로 피팅된 라쏘 모델. |
| [`OrthogonalMatchingPursuit`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuit.html#sklearn.linear_model.OrthogonalMatchingPursuit "sklearn.linear_model.OrthogonalMatchingPursuit")         | 직교 매칭 추구 모델 (OMP).                          |
| [`OrthogonalMatchingPursuitCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuitCV.html#sklearn.linear_model.OrthogonalMatchingPursuitCV "sklearn.linear_model.OrthogonalMatchingPursuitCV") | 교차 검증된 직교 매칭 추구 모델 (OMP).                   |

### 4) 베이지안 회귀기 (Bayesian regressors)

| 하위 항목                                                                                                                                                                                | 설명           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ |
| [`ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression") | 베이지안 ARD 회귀. |
| [`BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge") | 베이지안 릿지 회귀.  |

### 5) 변수 선택이 가능한 다중 작업 선형 회귀기 (Multi-task linear regressors with variable selection)

- 이 추정기는 희소 계수를 유도하면서 다중 회귀 문제(또는 작업)를 공동으로 피팅합니다. 추론된 계수는 작업 간에 다를 수 있지만 선택된 특성(0이 아닌 계수)에서는 일치하도록 제한됩니다.

| 하위 항목                                                                                                                                                                                                                | 설명                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| [`MultiTaskElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNet.html#sklearn.linear_model.MultiTaskElasticNet "sklearn.linear_model.MultiTaskElasticNet")         | L1/L2 혼합-노름을 정규화로 사용하여 훈련된 다중 작업 엘라스틱넷 모델. |
| [`MultiTaskElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNetCV.html#sklearn.linear_model.MultiTaskElasticNetCV "sklearn.linear_model.MultiTaskElasticNetCV") | 내장 교차 검증이 있는 다중 작업 L1/L2 엘라스틱넷.            |
| [`MultiTaskLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso "sklearn.linear_model.MultiTaskLasso")                             | L1/L2 혼합-노름을 정규화로 사용하여 훈련된 다중 작업 라쏘 모델.    |
| [`MultiTaskLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV "sklearn.linear_model.MultiTaskLassoCV")                     | 내장 교차 검증이 있는 다중 작업 라쏘 모델.                  |

### 6) 이상치에 강한 회귀기 (Outlier-robust regressors)

- Huber 손실을 사용하는 모든 추정기는 이상치에 대해 강력합니다. 예를 들어, `loss='huber'`인 `SGDRegressor`가 있습니다.

| 하위 항목                                                                                                                                                                                                | 설명                                     |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| [`HuberRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.HuberRegressor.html#sklearn.linear_model.HuberRegressor "sklearn.linear_model.HuberRegressor")             | 이상치에 강한 L2 정규화 선형 회귀 모델.               |
| [`QuantileRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.QuantileRegressor.html#sklearn.linear_model.QuantileRegressor "sklearn.linear_model.QuantileRegressor") | 조건부 분위수를 예측하는 선형 회귀 모델.                |
| [`RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")         | RANSAC (RANdom SAmple Consensus) 알고리즘. |
| [`TheilSenRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TheilSenRegressor.html#sklearn.linear_model.TheilSenRegressor "sklearn.linear_model.TheilSenRegressor") | Theil-Sen 추정기: 강건한 다변량 회귀 모델.          |

### 7) 회귀를 위한 일반화 선형 모델 (GLM) (Generalized linear models (GLM) for regression)

- 이 모델은 반응 변수가 정상 분포가 아닌 오류 분포를 가질 수 있도록 허용합니다.

| 하위 항목                                                                                                                                                                                            | 설명                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------- |
| [`GammaRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.GammaRegressor.html#sklearn.linear_model.GammaRegressor "sklearn.linear_model.GammaRegressor")         | 감마 분포를 사용하는 일반화 선형 모델.  |
| [`PoissonRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PoissonRegressor.html#sklearn.linear_model.PoissonRegressor "sklearn.linear_model.PoissonRegressor") | 포아송 분포를 사용하는 일반화 선형 모델. |
| [`TweedieRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.TweedieRegressor.html#sklearn.linear_model.TweedieRegressor "sklearn.linear_model.TweedieRegressor") | 트위디 분포를 사용하는 일반화 선형 모델. |

### 8) 기타 (Miscellaneous)

| 하위 항목                                                                                                                                                                                                                                    | 설명                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| [`PassiveAggressiveRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PassiveAggressiveRegressor.html#sklearn.linear_model.PassiveAggressiveRegressor "sklearn.linear_model.PassiveAggressiveRegressor") | 패시브 어그레시브 회귀기.                            |
| [`enet_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "sklearn.linear_model.enet_path")                                                                     | 좌표 하강법으로 엘라스틱넷 경로를 계산합니다.                 |
| [`lars_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path.html#sklearn.linear_model.lars_path "sklearn.linear_model.lars_path")                                                                     | LARS 알고리즘을 사용하여 최소 각도 회귀 또는 라쏘 경로를 계산합니다. |
| [`lars_path_gram`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lars_path_gram.html#sklearn.linear_model.lars_path_gram "sklearn.linear_model.lars_path_gram")                                                 | 충분 통계 모드의 lars_path.                      |
| [`lasso_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.lasso_path.html#sklearn.linear_model.lasso_path "sklearn.linear_model.lasso_path")                                                                 | 좌표 하강법으로 라쏘 경로를 계산합니다.                    |
| [`orthogonal_mp`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.orthogonal_mp.html#sklearn.linear_model.orthogonal_mp "sklearn.linear_model.orthogonal_mp")                                                     | 직교 매칭 추구 (OMP).                           |
| [`orthogonal_mp_gram`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.orthogonal_mp_gram.html#sklearn.linear_model.orthogonal_mp_gram "sklearn.linear_model.orthogonal_mp_gram")                                 | Gram 직교 매칭 추구 (OMP).                      |
| [`ridge_regression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ridge_regression.html#sklearn.linear_model.ridge_regression "sklearn.linear_model.ridge_regression")                                         | 정규 방정식 방법으로 릿지 방정식을 해결합니다.                |




## 24. `sklearn.manifold`
- 데이터 임베딩 기법.
> 자세한 내용은 [매니폴드 학습](https://scikit-learn.org/stable/modules/manifold.html#manifold) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                                                                | 설명                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| [`Isomap`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap "sklearn.manifold.Isomap")                                                                         | Isomap 임베딩.                   |
| [`LocallyLinearEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.LocallyLinearEmbedding.html#sklearn.manifold.LocallyLinearEmbedding "sklearn.manifold.LocallyLinearEmbedding")         | 국소 선형 임베딩.                    |
| [`MDS`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html#sklearn.manifold.MDS "sklearn.manifold.MDS")                                                                                     | 다차원 척도법.                      |
| [`SpectralEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.SpectralEmbedding.html#sklearn.manifold.SpectralEmbedding "sklearn.manifold.SpectralEmbedding")                             | 비선형 차원 축소를 위한 스펙트럴 임베딩.       |
| [`TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE")                                                                                 | T-분포 확률적 이웃 임베딩.              |
| [`locally_linear_embedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.locally_linear_embedding.html#sklearn.manifold.locally_linear_embedding "sklearn.manifold.locally_linear_embedding") | 데이터에 대한 국소 선형 임베딩 분석 수행.      |
| [`smacof`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.smacof.html#sklearn.manifold.smacof "sklearn.manifold.smacof")                                                                         | SMACOF 알고리즘을 사용하여 다차원 척도법 계산. |
| [`spectral_embedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#sklearn.manifold.spectral_embedding "sklearn.manifold.spectral_embedding")                         | 그래프 라플라시안의 첫 번째 고유벡터에 샘플을 투영. |
| [`trustworthiness`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.trustworthiness.html#sklearn.manifold.trustworthiness "sklearn.manifold.trustworthiness")                                     | 로컬 구조가 얼마나 유지되는지 나타냅니다.       |



## 25. `sklearn.metrics`

- 점수 함수, 성능 지표, 쌍별 지표 및 거리 계산.

> 자세한 내용은 [평가 지표 및 스코어링: 예측 품질 정량화](https://scikit-learn.org/stable/modules/model_evaluation.html#model-evaluation) 및 [쌍별 지표, 친밀도 및 커널](https://scikit-learn.org/stable/modules/metrics.html#metrics) 섹션을 참조하십시오.

### 1) 모델 선택 인터페이스 (Model selection interface)

> 자세한 내용은 [스코어링 매개변수: 모델 평가 규칙 정의](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                             | 설명                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| [`check_scoring`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.check_scoring.html#sklearn.metrics.check_scoring "sklearn.metrics.check_scoring")             | 사용자 옵션에서 스코어러 결정.          |
| [`get_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer.html#sklearn.metrics.get_scorer "sklearn.metrics.get_scorer")                         | 문자열에서 스코어러 가져오기.           |
| [`get_scorer_names`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer_names.html#sklearn.metrics.get_scorer_names "sklearn.metrics.get_scorer_names") | 사용 가능한 모든 스코어러의 이름을 가져옵니다. |
| [`make_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html#sklearn.metrics.make_scorer "sklearn.metrics.make_scorer")                     | 성능 지표 또는 손실 함수에서 스코어러 생성.  |

### 2) 분류 지표 (Classification metrics)

> 자세한 내용은 [분류 지표](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                                                                                         | 설명                                      |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| [`accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score "sklearn.metrics.accuracy_score")                                                                     | 정확도 분류 점수.                              |
| [`auc`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.auc.html#sklearn.metrics.auc "sklearn.metrics.auc")                                                                                                                 | 사다리꼴 규칙을 사용하여 곡선 아래 영역(AUC) 계산.         |
| [`average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html#sklearn.metrics.average_precision_score "sklearn.metrics.average_precision_score")                                 | 예측 점수에서 평균 정밀도(AP) 계산.                  |
| [`balanced_accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html#sklearn.metrics.balanced_accuracy_score "sklearn.metrics.balanced_accuracy_score")                                 | 균형 정확도 계산.                              |
| [`brier_score_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html#sklearn.metrics.brier_score_loss "sklearn.metrics.brier_score_loss")                                                             | 브라이어 점수 손실 계산.                          |
| [`class_likelihood_ratios`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.class_likelihood_ratios.html#sklearn.metrics.class_likelihood_ratios "sklearn.metrics.class_likelihood_ratios")                                 | 이진 분류 긍정 및 부정 가능도 비율 계산.                |
| [`classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report "sklearn.metrics.classification_report")                                         | 주요 분류 지표를 보여주는 텍스트 보고서 작성.              |
| [`cohen_kappa_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html#sklearn.metrics.cohen_kappa_score "sklearn.metrics.cohen_kappa_score")                                                         | 코헨의 카파 계산: 주석자 간 일치도를 측정하는 통계.          |
| [`confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix "sklearn.metrics.confusion_matrix")                                                             | 분류의 정확도를 평가하기 위한 혼동 행렬 계산.              |
| [`d2_log_loss_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_log_loss_score.html#sklearn.metrics.d2_log_loss_score "sklearn.metrics.d2_log_loss_score")                                                         | 𝐷2 점수 함수, 설명된 로그 손실 비율.                |
| [`dcg_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.dcg_score.html#sklearn.metrics.dcg_score "sklearn.metrics.dcg_score")                                                                                         | 할인 누적 이득 계산.                            |
| [`det_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.det_curve.html#sklearn.metrics.det_curve "sklearn.metrics.det_curve")                                                                                         | 다양한 확률 임계값에 대한 오류율 계산.                  |
| [`f1_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score "sklearn.metrics.f1_score")                                                                                             | F1 점수 계산, 균형 F-점수 또는 F-측정으로도 알려져 있습니다.  |
| [`fbeta_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fbeta_score.html#sklearn.metrics.fbeta_score "sklearn.metrics.fbeta_score")                                                                                 | F-베타 점수 계산.                             |
| [`hamming_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hamming_loss.html#sklearn.metrics.hamming_loss "sklearn.metrics.hamming_loss")                                                                             | 평균 해밍 손실 계산.                            |
| [`hinge_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hinge_loss.html#sklearn.metrics.hinge_loss "sklearn.metrics.hinge_loss")                                                                                     | 평균 힌지 손실(정규화되지 않음).                     |
| [`jaccard_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#sklearn.metrics.jaccard_score "sklearn.metrics.jaccard_score")                                                                         | 자카드 유사 계수 점수.                           |
| [`log_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html#sklearn.metrics.log_loss "sklearn.metrics.log_loss")                                                                                             | 로그 손실, 일명 로지스틱 손실 또는 교차 엔트로피 손실.        |
| [`matthews_corrcoef`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.matthews_corrcoef.html#sklearn.metrics.matthews_corrcoef "sklearn.metrics.matthews_corrcoef")                                                         | 매튜스 상관 계수(MCC) 계산.                      |
| [`multilabel_confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.multilabel_confusion_matrix.html#sklearn.metrics.multilabel_confusion_matrix "sklearn.metrics.multilabel_confusion_matrix")                 | 각 클래스 또는 샘플에 대한 혼동 행렬 계산.               |
| [`ndcg_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ndcg_score.html#sklearn.metrics.ndcg_score "sklearn.metrics.ndcg_score")                                                                                     | 정규화된 할인 누적 이득 계산.                       |
| [`precision_recall_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html#sklearn.metrics.precision_recall_curve "sklearn.metrics.precision_recall_curve")                                     | 다양한 확률 임계값에 대한 정밀도-재현율 쌍 계산.            |
| [`precision_recall_fscore_support`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support "sklearn.metrics.precision_recall_fscore_support") | 각 클래스에 대한 정밀도, 재현율, F-측정 및 지원 계산.       |
| [`precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score "sklearn.metrics.precision_score")                                                                 | 정밀도 계산.                                 |
| [`recall_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score "sklearn.metrics.recall_score")                                                                             | 재현율 계산.                                 |
| [`roc_auc_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score "sklearn.metrics.roc_auc_score")                                                                         | 예측 점수에서 수신기 작동 특성 곡선(ROC AUC) 아래 영역 계산. |
| [`roc_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve "sklearn.metrics.roc_curve")                                                                                         | 수신기 작동 특성(ROC) 계산.                      |
|[`top_k_accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.top_k_accuracy_score.html#sklearn.metrics.top_k_accuracy_score "sklearn.metrics.top_k_accuracy_score")|Top-k 정확도 분류 점수.|
|[`zero_one_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.zero_one_loss.html#sklearn.metrics.zero_one_loss "sklearn.metrics.zero_one_loss")|Zero-one 분류 손실.|

### 3) 회귀 메트릭 (Regression metrics)

> 자세한 내용은 [회귀 메트릭](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                                                                                     | 설명                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| [`d2_absolute_error_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_absolute_error_score.html#sklearn.metrics.d2_absolute_error_score "sklearn.metrics.d2_absolute_error_score")                             | 𝐷2 회귀 점수 함수, 절대 오차 설명 비율.  |
| [`d2_pinball_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_pinball_score.html#sklearn.metrics.d2_pinball_score "sklearn.metrics.d2_pinball_score")                                                         | 𝐷2 회귀 점수 함수, 핀볼 손실 설명 비율.  |
| [`d2_tweedie_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.d2_tweedie_score.html#sklearn.metrics.d2_tweedie_score "sklearn.metrics.d2_tweedie_score")                                                         | 𝐷2 회귀 점수 함수, 트위디 편차 설명 비율. |
| [`explained_variance_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html#sklearn.metrics.explained_variance_score "sklearn.metrics.explained_variance_score")                         | 설명된 분산 회귀 점수 함수.            |
| [`max_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.max_error.html#sklearn.metrics.max_error "sklearn.metrics.max_error")                                                                                     | 최대 잔차 오차를 계산하는 메트릭.         |
| [`mean_absolute_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error "sklearn.metrics.mean_absolute_error")                                             | 평균 절대 오차 회귀 손실.             |
| [`mean_absolute_percentage_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_percentage_error.html#sklearn.metrics.mean_absolute_percentage_error "sklearn.metrics.mean_absolute_percentage_error") | 평균 절대 백분율 오차 (MAPE) 회귀 손실.  |
| [`mean_gamma_deviance`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_gamma_deviance.html#sklearn.metrics.mean_gamma_deviance "sklearn.metrics.mean_gamma_deviance")                                             | 평균 감마 편차 회귀 손실.             |
| [`mean_pinball_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_pinball_loss.html#sklearn.metrics.mean_pinball_loss "sklearn.metrics.mean_pinball_loss")                                                     | 분위 회귀를 위한 핀볼 손실.            |
| [`mean_poisson_deviance`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_poisson_deviance.html#sklearn.metrics.mean_poisson_deviance "sklearn.metrics.mean_poisson_deviance")                                     | 평균 포아송 편차 회귀 손실.            |
| [`mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error "sklearn.metrics.mean_squared_error")                                                 | 평균 제곱 오차 회귀 손실.             |
| [`mean_squared_log_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_log_error.html#sklearn.metrics.mean_squared_log_error "sklearn.metrics.mean_squared_log_error")                                 | 평균 제곱 로그 오차 회귀 손실.          |
| [`mean_tweedie_deviance`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_tweedie_deviance.html#sklearn.metrics.mean_tweedie_deviance "sklearn.metrics.mean_tweedie_deviance")                                     | 평균 트위디 편차 회귀 손실.            |
| [`median_absolute_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.median_absolute_error.html#sklearn.metrics.median_absolute_error "sklearn.metrics.median_absolute_error")                                     | 중앙값 절대 오차 회귀 손실.            |
| [`r2_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score "sklearn.metrics.r2_score")                                                                                         | 𝑅2 (결정 계수) 회귀 점수 함수.       |
| [`root_mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_error.html#sklearn.metrics.root_mean_squared_error "sklearn.metrics.root_mean_squared_error")                             | 제곱근 평균 제곱 오차 회귀 손실.         |
| [`root_mean_squared_log_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.root_mean_squared_log_error.html#sklearn.metrics.root_mean_squared_log_error "sklearn.metrics.root_mean_squared_log_error")             | 제곱근 평균 제곱 로그 오차 회귀 손실.      |

### 4) 다중 레이블 순위 메트릭 (Multilabel ranking metrics)

> 자세한 내용은 [다중 레이블 순위 메트릭](https://scikit-learn.org/stable/modules/model_evaluation.html#multilabel-ranking-metrics) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                                                                                                                 | 설명                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [`coverage_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.coverage_error.html#sklearn.metrics.coverage_error "sklearn.metrics.coverage_error")                                                                                             | Coverage error 측정. |
| [`label_ranking_average_precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.label_ranking_average_precision_score.html#sklearn.metrics.label_ranking_average_precision_score "sklearn.metrics.label_ranking_average_precision_score") | 순위 기반 평균 정밀도 계산.   |
| [`label_ranking_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.label_ranking_loss.html#sklearn.metrics.label_ranking_loss "sklearn.metrics.label_ranking_loss")                                                                             | 순위 손실 측정 계산.       |

### 5) 클러스터링 메트릭 (Clustering metrics)
- 클러스터 분석 결과를 위한 평가 메트릭.
	- 지도 평가(supervised evaluation)는 각 샘플에 대한 참 클래스 값을 사용합니다.
	- 비지도 평가(unsupervised evaluation)는 참값을 사용하지 않고 모델 자체의 "품질"을 측정합니다.

> 자세한 내용은 [클러스터링 성능 평가](https://scikit-learn.org/stable/modules/clustering.html#clustering-evaluation) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                                                                                                     | 설명                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| [`adjusted_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_mutual_info_score.html#sklearn.metrics.adjusted_mutual_info_score "sklearn.metrics.adjusted_mutual_info_score")                                 | 두 클러스터링 간의 조정된 상호 정보.             |
| [`adjusted_rand_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html#sklearn.metrics.adjusted_rand_score "sklearn.metrics.adjusted_rand_score")                                                             | 우연을 고려한 Rand 지수.                  |
| [`calinski_harabasz_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.calinski_harabasz_score.html#sklearn.metrics.calinski_harabasz_score "sklearn.metrics.calinski_harabasz_score")                                             | Calinski-Harabasz 점수 계산.          |
| [`cluster.contingency_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cluster.contingency_matrix.html#sklearn.metrics.cluster.contingency_matrix "sklearn.metrics.cluster.contingency_matrix")                                 | 레이블 간의 관계를 설명하는 연관 행렬 빌드.         |
| [`cluster.pair_confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cluster.pair_confusion_matrix.html#sklearn.metrics.cluster.pair_confusion_matrix "sklearn.metrics.cluster.pair_confusion_matrix")                     | 두 클러스터링에서 발생하는 쌍 혼동 행렬.           |
| [`completeness_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.completeness_score.html#sklearn.metrics.completeness_score "sklearn.metrics.completeness_score")                                                                 | 참값을 고려한 클러스터 레이블링의 완전성 메트릭 계산.    |
| [`davies_bouldin_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.davies_bouldin_score.html#sklearn.metrics.davies_bouldin_score "sklearn.metrics.davies_bouldin_score")                                                         | Davies-Bouldin 점수 계산.             |
| [`fowlkes_mallows_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.fowlkes_mallows_score.html#sklearn.metrics.fowlkes_mallows_score "sklearn.metrics.fowlkes_mallows_score")                                                     | 점 집합의 두 클러스터링 간의 유사성 측정.          |
| [`homogeneity_completeness_v_measure`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_completeness_v_measure.html#sklearn.metrics.homogeneity_completeness_v_measure "sklearn.metrics.homogeneity_completeness_v_measure") | 동질성, 완전성 및 V-Measure 점수를 한 번에 계산. |
| [`homogeneity_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_score.html#sklearn.metrics.homogeneity_score "sklearn.metrics.homogeneity_score")                                                                     | 참값을 고려한 클러스터 레이블링의 동질성 메트릭 계산.    |
| [`mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mutual_info_score.html#sklearn.metrics.mutual_info_score "sklearn.metrics.mutual_info_score")                                                                     | 두 클러스터링 간의 상호 정보.                 |
| [`normalized_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.normalized_mutual_info_score.html#sklearn.metrics.normalized_mutual_info_score "sklearn.metrics.normalized_mutual_info_score")                         | 두 클러스터링 간의 정규화된 상호 정보.            |
| [`rand_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.rand_score.html#sklearn.metrics.rand_score "sklearn.metrics.rand_score")                                                                                                 | Rand 지수.                          |
| [`silhouette_samples`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_samples.html#sklearn.metrics.silhouette_samples "sklearn.metrics.silhouette_samples")                                                                 | 각 샘플에 대한 실루엣 계수 계산.               |
| [`silhouette_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#sklearn.metrics.silhouette_score "sklearn.metrics.silhouette_score")                                                                         | 모든 샘플의 평균 실루엣 계수 계산.              |
| [`v_measure_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html#sklearn.metrics.v_measure_score "sklearn.metrics.v_measure_score")                                                                             | 참값을 고려한 V-Measure 클러스터 레이블링.      |

### 6) 바이클러스터링 메트릭 (Biclustering metrics)

> 자세한 내용은 [바이클러스터링 평가](https://scikit-learn.org/stable/modules/biclustering.html#biclustering-evaluation) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                         | 설명                |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [`consensus_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.consensus_score.html#sklearn.metrics.consensus_score "sklearn.metrics.consensus_score") | 두 바이클러스터 집합의 유사성. |

### 7) 거리 메트릭 (Distance metrics)

| 하위 항목                                                                                                                                                                     | 설명                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| [`DistanceMetric`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html#sklearn.metrics.DistanceMetric "sklearn.metrics.DistanceMetric") | 빠른 거리 메트릭 함수용 통합 인터페이스. |

### 8) 쌍별 메트릭 (Pairwise metrics)

- 샘플 집합 간의 쌍별 거리 및 어피니티를 위한 메트릭.
> 자세한 내용은 [쌍별 메트릭, 어피니티 및 커널](https://scikit-learn.org/stable/modules/metrics.html#metrics) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                                                                                                         | 설명                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| [`pairwise.additive_chi2_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.additive_chi2_kernel.html#sklearn.metrics.pairwise.additive_chi2_kernel "sklearn.metrics.pairwise.additive_chi2_kernel")                         | X와 Y의 관측치 간의 가법적 카이제곱 커널 계산. |
| [`pairwise.chi2_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.chi2_kernel.html#sklearn.metrics.pairwise.chi2_kernel "sklearn.metrics.pairwise.chi2_kernel")                                                             | X와 Y 간의 지수적 카이제곱 커널 계산.      |
| [`pairwise.cosine_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_distances.html#sklearn.metrics.pairwise.cosine_distances "sklearn.metrics.pairwise.cosine_distances")                                         | X와 Y의 샘플 간의 코사인 거리 계산.       |
| [`pairwise.cosine_similarity`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html#sklearn.metrics.pairwise.cosine_similarity "sklearn.metrics.pairwise.cosine_similarity")                                     | X와 Y의 샘플 간의 코사인 유사도 계산.      |
| [`pairwise.distance_metrics`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.distance_metrics.html#sklearn.metrics.pairwise.distance_metrics "sklearn.metrics.pairwise.distance_metrics")                                         | 쌍별 거리에 대한 유효 메트릭.            |
| [`pairwise.euclidean_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.euclidean_distances.html#sklearn.metrics.pairwise.euclidean_distances "sklearn.metrics.pairwise.euclidean_distances")                             | 벡터 배열 X와 Y의 각 쌍 간의 거리 행렬 계산. |
| [`pairwise.haversine_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.haversine_distances.html#sklearn.metrics.pairwise.haversine_distances "sklearn.metrics.pairwise.haversine_distances")                             | X와 Y의 샘플 간의 하버사인 거리 계산.      |
| [`pairwise.kernel_metrics`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.kernel_metrics.html#sklearn.metrics.pairwise.kernel_metrics "sklearn.metrics.pairwise.kernel_metrics")                                                 | 쌍별 커널에 대한 유효 메트릭.            |
| [`pairwise.laplacian_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.laplacian_kernel.html#sklearn.metrics.pairwise.laplacian_kernel "sklearn.metrics.pairwise.laplacian_kernel")                                         | X와 Y 간의 라플라시안 커널 계산.         |
| [`pairwise.linear_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.linear_kernel.html#sklearn.metrics.pairwise.linear_kernel "sklearn.metrics.pairwise.linear_kernel")                                                     | X와 Y 간의 선형 커널 계산.            |
| [`pairwise.manhattan_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.manhattan_distances.html#sklearn.metrics.pairwise.manhattan_distances "sklearn.metrics.pairwise.manhattan_distances")                             | X와 Y의 벡터 간의 L1 거리 계산.        |
| [`pairwise.nan_euclidean_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.nan_euclidean_distances.html#sklearn.metrics.pairwise.nan_euclidean_distances "sklearn.metrics.pairwise.nan_euclidean_distances")             | 결측값이 있는 경우 유클리드 거리 계산.       |
| [`pairwise.paired_cosine_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_cosine_distances.html#sklearn.metrics.pairwise.paired_cosine_distances "sklearn.metrics.pairwise.paired_cosine_distances")             | X와 Y 간의 쌍별 코사인 거리 계산.        |
| [`pairwise.paired_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_distances.html#sklearn.metrics.pairwise.paired_distances "sklearn.metrics.pairwise.paired_distances")                                         | X와 Y 간의 쌍별 거리 계산.            |
| [`pairwise.paired_euclidean_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_euclidean_distances.html#sklearn.metrics.pairwise.paired_euclidean_distances "sklearn.metrics.pairwise.paired_euclidean_distances") | X와 Y 간의 쌍별 유클리드 거리 계산.       |
| [`pairwise.paired_manhattan_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.paired_manhattan_distances.html#sklearn.metrics.pairwise.paired_manhattan_distances "sklearn.metrics.pairwise.paired_manhattan_distances") | X와 Y 간의 쌍별 L1 거리 계산.         |
| [`pairwise.pairwise_kernels`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html#sklearn.metrics.pairwise.pairwise_kernels "sklearn.metrics.pairwise.pairwise_kernels")                                         | 배열 X와 선택적 배열 Y 간의 커널 계산.     |
| [`pairwise.polynomial_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.polynomial_kernel.html#sklearn.metrics.pairwise.polynomial_kernel "sklearn.metrics.pairwise.polynomial_kernel")                                     | X와 Y 간의 다항식 커널 계산.           |
| [`pairwise.rbf_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.rbf_kernel.html#sklearn.metrics.pairwise.rbf_kernel "sklearn.metrics.pairwise.rbf_kernel")                                                                 | X와 Y 간의 rbf (가우시안) 커널 계산.    |
| [`pairwise.sigmoid_kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.sigmoid_kernel.html#sklearn.metrics.pairwise.sigmoid_kernel "sklearn.metrics.pairwise.sigmoid_kernel")                                                 | X와 Y 간의 시그모이드 커널 계산.         |
| [`pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances")                                                                     | 벡터 배열 X와 선택적 Y 간의 거리 행렬 계산.  |
| [`pairwise_distances_argmin`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin.html#sklearn.metrics.pairwise_distances_argmin "sklearn.metrics.pairwise_distances_argmin")                                         | 한 점과 점 집합 간의 최소 거리 계산.       |
| [`pairwise_distances_argmin_min`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_argmin_min.html#sklearn.metrics.pairwise_distances_argmin_min "sklearn.metrics.pairwise_distances_argmin_min")                         | 한 점과 점 집합 간의 최소 거리 계산.       |
| [`pairwise_distances_chunked`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_chunked.html#sklearn.metrics.pairwise_distances_chunked "sklearn.metrics.pairwise_distances_chunked")                                     | 선택적 축소와 함께 청크별 거리 행렬 생성.     |

### 9) 플로팅 (Plotting)

> 자세한 내용은 [시각화](https://scikit-learn.org/stable/visualizations.html#visualizations) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                                                     | 설명                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [`ConfusionMatrixDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html#sklearn.metrics.ConfusionMatrixDisplay "sklearn.metrics.ConfusionMatrixDisplay") | 혼동 행렬 시각화.        |
| [`DetCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DetCurveDisplay.html#sklearn.metrics.DetCurveDisplay "sklearn.metrics.DetCurveDisplay")                             | DET 곡선 시각화.       |
| [`PrecisionRecallDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay "sklearn.metrics.PrecisionRecallDisplay") | 정밀도-재현율 시각화.      |
| [`PredictionErrorDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PredictionErrorDisplay.html#sklearn.metrics.PredictionErrorDisplay "sklearn.metrics.PredictionErrorDisplay") | 회귀 모델의 예측 오류 시각화. |
| [`RocCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.RocCurveDisplay.html#sklearn.metrics.RocCurveDisplay "sklearn.metrics.RocCurveDisplay")                             | ROC 곡선 시각화.       |



## 26. `sklearn.mixture`
- 혼합 모델링 알고리즘
> 자세한 내용은 [가우시안 혼합 모델](https://scikit-learn.org/stable/modules/mixture.html#mixture) 섹션을 참조하십시오.

| 하위 항목                                                                                                                                                                                                         | 설명                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| [`BayesianGaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture "sklearn.mixture.BayesianGaussianMixture") | 가우시안 혼합의 변분 베이지안 추정. |
| [`GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")                                 | 가우시안 혼합.             |


## 27. `sklearn.model_selection`
- 모델 선택을 위한 도구, 예를 들어 교차 검증 및 하이퍼파라미터 튜닝.

> 자세한 내용은 [교차 검증: 추정기 성능 평가](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation), [추정기의 하이퍼 파라미터 튜닝](https://scikit-learn.org/stable/modules/grid_search.html#grid-search), 및 [학습 곡선](https://scikit-learn.org/stable/modules/learning_curve.html#learning-curve) 섹션을 참조하십시오.

### 1) 분할기 (Splitters)

| 하위 항목                                                                                                                                                                                                                                 | 설명                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold")                                                     | 중첩되지 않는 그룹을 가진 K-폴드 반복자.           |
| [`GroupShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html#sklearn.model_selection.GroupShuffleSplit "sklearn.model_selection.GroupShuffleSplit")                         | 그룹 셔플 아웃 교차 검증 반복자.                |
| [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold")                                                                         | K-폴드 교차 검증기.                       |
| [`LeaveOneGroupOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html#sklearn.model_selection.LeaveOneGroupOut "sklearn.model_selection.LeaveOneGroupOut")                             | 한 그룹씩 제외하는 교차 검증기.                 |
| [`LeaveOneOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html#sklearn.model_selection.LeaveOneOut "sklearn.model_selection.LeaveOneOut")                                                 | 한 개씩 제외하는 교차 검증기.                  |
| [`LeavePGroupsOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut "sklearn.model_selection.LeavePGroupsOut")                                 | P개의 그룹을 제외하는 교차 검증기.               |
| [`LeavePOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePOut.html#sklearn.model_selection.LeavePOut "sklearn.model_selection.LeavePOut")                                                         | P개씩 제외하는 교차 검증기.                   |
| [`PredefinedSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.PredefinedSplit.html#sklearn.model_selection.PredefinedSplit "sklearn.model_selection.PredefinedSplit")                                 | 사전 정의된 분할 교차 검증기.                  |
| [`RepeatedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedKFold.html#sklearn.model_selection.RepeatedKFold "sklearn.model_selection.RepeatedKFold")                                         | 반복 K-폴드 교차 검증기.                    |
| [`RepeatedStratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html#sklearn.model_selection.RepeatedStratifiedKFold "sklearn.model_selection.RepeatedStratifiedKFold") | 반복 층화 K-폴드 교차 검증기.                 |
| [`ShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit")                                             | 무작위 순열 교차 검증기.                     |
| [`StratifiedGroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html#sklearn.model_selection.StratifiedGroupKFold "sklearn.model_selection.StratifiedGroupKFold")             | 중첩되지 않는 그룹을 가진 층화 K-폴드 반복자.        |
| [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold")                                 | 층화 K-폴드 교차 검증기.                    |
| [`StratifiedShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html#sklearn.model_selection.StratifiedShuffleSplit "sklearn.model_selection.StratifiedShuffleSplit")     | 층화 셔플 교차 검증기.                      |
| [`TimeSeriesSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit "sklearn.model_selection.TimeSeriesSplit")                                 | 시계열 교차 검증기.                        |
| [`check_cv`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.check_cv.html#sklearn.model_selection.check_cv "sklearn.model_selection.check_cv")                                                             | 교차 검증기를 구축하기 위한 입력 검사 유틸리티.        |
| [`train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")                             | 배열 또는 행렬을 무작위 훈련 및 테스트 하위 집합으로 분할. |

### 2) 하이퍼 파라미터 최적화 (Hyper-parameter optimizers)

| 하위 항목                                                                                                                                                                                                                         | 설명                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")                                     | 추정기의 지정된 파라미터 값을 통한 철저한 검색.  |
| [`HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV")         | 점진적 절반 감축을 통한 지정된 파라미터 값 검색. |
| [`HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV") | 하이퍼 파라미터에 대한 무작위 검색.         |
| [`ParameterGrid`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterGrid.html#sklearn.model_selection.ParameterGrid "sklearn.model_selection.ParameterGrid")                                 | 각각의 이산 값들로 구성된 파라미터 그리드.     |
| [`ParameterSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterSampler.html#sklearn.model_selection.ParameterSampler "sklearn.model_selection.ParameterSampler")                     | 주어진 분포로부터 샘플링된 파라미터 생성기.     |
| [`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV")             | 하이퍼 파라미터에 대한 무작위 검색.         |
### 3) 모델 적합 후 튜닝 (Post-fit model tuning)

| 하위 항목                                                                                                                                                                                                                                             | 설명                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| [`FixedThresholdClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.FixedThresholdClassifier.html#sklearn.model_selection.FixedThresholdClassifier "sklearn.model_selection.FixedThresholdClassifier")         | 결정 임계값을 수동으로 설정하는 이진 분류기.        |
| [`TunedThresholdClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TunedThresholdClassifierCV.html#sklearn.model_selection.TunedThresholdClassifierCV "sklearn.model_selection.TunedThresholdClassifierCV") | 교차 검증을 사용하여 결정 임계값을 사후 조정하는 분류기. |

### 4) 모델 검증 (Model validation)

| 하위 항목                                                                                                                                                                                                                             | 설명                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| [`cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict")                     | 각 입력 데이터 포인트에 대한 교차 검증 추정치를 생성합니다.   |
| [`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score")                             | 교차 검증을 통해 점수를 평가합니다.                 |
| [`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate")                                 | 교차 검증을 통해 메트릭을 평가하고 적합/점수 시간을 기록합니다. |
| [`learning_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html#sklearn.model_selection.learning_curve "sklearn.model_selection.learning_curve")                                 | 학습 곡선.                               |
| [`permutation_test_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.permutation_test_score.html#sklearn.model_selection.permutation_test_score "sklearn.model_selection.permutation_test_score") | 순열을 통해 교차 검증 점수의 유의성을 평가합니다.         |
| [`validation_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html#sklearn.model_selection.validation_curve "sklearn.model_selection.validation_curve")                         | 검증 곡선.                               |

### 5) 시각화 (Visualization)

| 하위 항목                                                                                                                                                                                                                             | 설명         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [`LearningCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LearningCurveDisplay.html#sklearn.model_selection.LearningCurveDisplay "sklearn.model_selection.LearningCurveDisplay")         | 학습 곡선 시각화. |
| [`ValidationCurveDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ValidationCurveDisplay.html#sklearn.model_selection.ValidationCurveDisplay "sklearn.model_selection.ValidationCurveDisplay") | 검증 곡선 시각화. |


## 28. `sklearn.multiclass`
- 멀티클래스 학습 알고리즘.
	- one-vs-the-rest / one-vs-all
	- one-vs-one
	- 오류 수정 출력 코드
- 이 모듈에서 제공하는 추정기는 메타 추정기로, 생성자에 기본 추정기를 제공해야 합니다. 예를 들어, 이러한 추정기를 사용하여 이진 분류기나 회귀 분석기를 멀티클래스 분류기로 변환할 수 있습니다. 또한, 이러한 추정기를 멀티클래스 추정기와 함께 사용하여 정확도나 실행 시간 성능이 향상되기를 기대할 수 있습니다.
- scikit-learn의 모든 분류기는 멀티클래스 분류를 구현합니다. 커스텀 멀티클래스 전략을 실험하고자 할 때만 이 모듈을 사용하면 됩니다.
- one-vs-the-rest 메타 분류기는 기본 분류기가 predict_proba 메서드를 구현하는 한, predict_proba 메서드도 구현합니다. 이 메서드는 단일 레이블 및 다중 레이블 케이스 모두에서 클래스 소속 확률을 반환합니다. 다중 레이블 케이스에서는 주어진 샘플이 주어진 클래스에 속할 확률이므로, 단일 레이블 케이스와 달리 주어진 샘플에 대한 모든 가능한 레이블에 대한 확률의 합이 1이 되지 않습니다.
> 자세한 내용은 [멀티클래스 분류](https://scikit-learn.org/stable/modules/multiclass.html#multiclass-classification) 섹션을 참조하세요.

| 하위 항목                                                                                                                                                                                                      | 설명                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| [`OneVsOneClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")         | one-vs-one 멀티클래스 전략.            |
| [`OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")     | one-vs-the-rest (OvR) 멀티클래스 전략. |
| [`OutputCodeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier "sklearn.multiclass.OutputCodeClassifier") | (오류 수정) 출력 코드 멀티클래스 전략.         |

## 29. `sklearn.multioutput`
- 다중 출력 회귀 및 분류.
- 이 모듈에서 제공하는 추정기는 메타 추정기로, 생성자에 기본 추정기를 제공해야 합니다. 메타 추정기는 단일 출력 추정기를 다중 출력 추정기로 확장합니다.
> 자세한 내용은 [다중 레이블 분류](https://scikit-learn.org/stable/modules/multiclass.html#multilabel-classification), [다중 클래스-다중 출력 분류](https://scikit-learn.org/stable/modules/multiclass.html#multiclass-multioutput-classification), 및 [다중 출력 회귀](https://scikit-learn.org/stable/modules/multiclass.html#multioutput-regression) 섹션을 참조하세요.

| 하위 항목                                                                                                                                                                                                             | 설명                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| [`ClassifierChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "sklearn.multioutput.ClassifierChain")                         | 이진 분류기를 체인으로 배열하는 다중 레이블 모델. |
| [`MultiOutputClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier "sklearn.multioutput.MultiOutputClassifier") | 다중 목표 분류.                    |
| [`MultiOutputRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html#sklearn.multioutput.MultiOutputRegressor "sklearn.multioutput.MultiOutputRegressor")     | 다중 목표 회귀.                    |
| [`RegressorChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.RegressorChain.html#sklearn.multioutput.RegressorChain "sklearn.multioutput.RegressorChain")                             | 회귀를 체인으로 배열하는 다중 레이블 모델.     |



## 30. `sklearn.naive_bayes`
- 나이브 베이즈 알고리즘.
- 이 알고리즘들은 강한(나이브) 특성 독립 가정을 적용한 베이즈 정리를 기반으로 한 지도 학습 방법입니다.
> 자세한 내용은 [나이브 베이즈](https://scikit-learn.org/stable/modules/naive_bayes.html#naive-bayes) 섹션을 참조하세요.

| 하위 항목                                                                                                                                                                             | 설명                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| [`BernoulliNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB "sklearn.naive_bayes.BernoulliNB")         | 다변량 베르누이 모델을 위한 나이브 베이즈 분류기.                           |
| [`CategoricalNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.CategoricalNB.html#sklearn.naive_bayes.CategoricalNB "sklearn.naive_bayes.CategoricalNB") | 범주형 특성을 위한 나이브 베이즈 분류기.                                |
| [`ComplementNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.ComplementNB.html#sklearn.naive_bayes.ComplementNB "sklearn.naive_bayes.ComplementNB")     | Rennie et al. (2003)에서 설명된 Complement Naive Bayes 분류기. |
| [`GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")             | 가우시안 나이브 베이즈 (GaussianNB).                             |
| [`MultinomialNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB "sklearn.naive_bayes.MultinomialNB") | 다항 모델을 위한 나이브 베이즈 분류기.                                 |
## 31. `sklearn.neighbors`
- k-최근접 이웃 알고리즘.
> 자세한 내용은 [최근접 이웃](https://scikit-learn.org/stable/modules/neighbors.html#neighbors) 섹션을 참조하세요.

| 하위 항목                                                                                                                                                                                                                                           | 설명                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| [`BallTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html#sklearn.neighbors.BallTree "sklearn.neighbors.BallTree")                                                                                         | 일반화된 N-포인트 문제를 빠르게 해결하기 위한 BallTree. |
| [`KDTree`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "sklearn.neighbors.KDTree")                                                                                                 | 일반화된 N-포인트 문제를 빠르게 해결하기 위한 KDTree.   |
| [`KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")                                         | k-최근접 이웃 투표를 구현하는 분류기.               |
| [`KNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")                                             | k-최근접 이웃을 기반으로 한 회귀.                 |
| [`KNeighborsTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsTransformer.html#sklearn.neighbors.KNeighborsTransformer "sklearn.neighbors.KNeighborsTransformer")                                     | X를 k-최근접 이웃의 (가중) 그래프로 변환.           |
| [`KernelDensity`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html#sklearn.neighbors.KernelDensity "sklearn.neighbors.KernelDensity")                                                                     | 커널 밀도 추정.                            |
| [`LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor")                                                 | 로컬 아웃라이어 팩터(LOF)를 사용한 비지도 이상치 탐지.    |
| [`NearestCentroid`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid "sklearn.neighbors.NearestCentroid")                                                             | 최근접 중심 분류기.                          |
| [`NearestNeighbors`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestNeighbors.html#sklearn.neighbors.NearestNeighbors "sklearn.neighbors.NearestNeighbors")                                                         | 이웃 검색을 구현하는 비지도 학습기.                 |
| [`NeighborhoodComponentsAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NeighborhoodComponentsAnalysis.html#sklearn.neighbors.NeighborhoodComponentsAnalysis "sklearn.neighbors.NeighborhoodComponentsAnalysis") | 이웃 구성 요소 분석.                         |
| [`RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")                     | 주어진 반경 내의 이웃 사이의 투표를 구현하는 분류기.       |
| [`RadiusNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html#sklearn.neighbors.RadiusNeighborsRegressor "sklearn.neighbors.RadiusNeighborsRegressor")                         | 고정된 반경 내의 이웃을 기반으로 한 회귀.             |
| [`RadiusNeighborsTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsTransformer.html#sklearn.neighbors.RadiusNeighborsTransformer "sklearn.neighbors.RadiusNeighborsTransformer")                 | X를 반경 내의 이웃의 (가중) 그래프로 변환.           |
| [`kneighbors_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.kneighbors_graph.html#sklearn.neighbors.kneighbors_graph "sklearn.neighbors.kneighbors_graph")                                                         | X의 점들에 대해 k-이웃의 (가중) 그래프를 계산.        |
| [`radius_neighbors_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.radius_neighbors_graph.html#sklearn.neighbors.radius_neighbors_graph "sklearn.neighbors.radius_neighbors_graph")                                 | X의 점들에 대해 이웃의 (가중) 그래프를 계산.          |
| [`sort_graph_by_row_values`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.sort_graph_by_row_values.html#sklearn.neighbors.sort_graph_by_row_values "sklearn.neighbors.sort_graph_by_row_values")                         | 각 행이 증가하는 값으로 저장되도록 희소 그래프를 정렬.      |

## 32. `sklearn.neural_network`
- 신경망 기반 모델.
> 자세한 내용은 [신경망 모델(지도 학습)](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#neural-networks-supervised) 및 [신경망 모델(비지도 학습)](https://scikit-learn.org/stable/modules/neural_networks_unsupervised.html#neural-networks-unsupervised) 섹션을 참조하세요.

| 하위 항목                                                                                                                                                                                      | 설명                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------- |
| [`BernoulliRBM`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.BernoulliRBM.html#sklearn.neural_network.BernoulliRBM "sklearn.neural_network.BernoulliRBM")     | 베르누이 제한 볼츠만 머신 (RBM). |
| [`MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier") | 다층 퍼셉트론 분류기.          |
| [`MLPRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html#sklearn.neural_network.MLPRegressor "sklearn.neural_network.MLPRegressor")     | 다층 퍼셉트론 회귀기.          |

## 33. `sklearn.pipeline`
- 복합 추정기를 변환 및 추정기의 체인으로 구성하는 유틸리티.
> 자세한 내용은 [파이프라인 및 복합 추정기](https://scikit-learn.org/stable/modules/compose.html#combining-estimators) 섹션을 참조하세요.

| 하위 항목                                                                                                                                                                    | 설명                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [`FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion")     | 여러 변환기 객체의 결과를 연결.                                                                                                                                                                   |
| [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")                     | 데이터 변환기의 시퀀스와 선택적 최종 예측기.                                                                                                                                                            |
| [`make_pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline") | 주어진 추정기들로부터 [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline") 생성.                 |
| [`make_union`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_union.html#sklearn.pipeline.make_union "sklearn.pipeline.make_union")             | 주어진 변환기들로부터 [`FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion") 생성. |

## 34. `sklearn.preprocessing`
- 데이터 전처리를 위한 스케일링, 중심화, 정규화, 이진화 등 다양한 메서드.

> 자세한 내용은 [데이터 전처리](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing) 섹션을 참조하세요.

| 하위 항목                                                                                                                                                                                                           | 설명                                    |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| [`Binarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Binarizer.html#sklearn.preprocessing.Binarizer "sklearn.preprocessing.Binarizer")                                         | 임계값에 따라 데이터를 이진화 (특성 값을 0 또는 1로 설정).  |
| [`FunctionTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer "sklearn.preprocessing.FunctionTransformer") | 임의의 호출 가능 객체로부터 변환기 생성.               |
| [`KBinsDiscretizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer "sklearn.preprocessing.KBinsDiscretizer")             | 연속 데이터를 구간으로 이진화.                     |
| [`KernelCenterer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KernelCenterer.html#sklearn.preprocessing.KernelCenterer "sklearn.preprocessing.KernelCenterer")                     | 임의의 커널 행렬 𝐾를 중심화.                    |
| [`LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")                     | 일대다 방식으로 레이블 이진화.                     |
| [`LabelEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder "sklearn.preprocessing.LabelEncoder")                             | 타겟 레이블을 0과 n_classes-1 사이의 값으로 인코딩.   |
| [`MaxAbsScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MaxAbsScaler.html#sklearn.preprocessing.MaxAbsScaler "sklearn.preprocessing.MaxAbsScaler")                             | 각 특성을 최대 절대값으로 스케일링.                  |
| [`MinMaxScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")                             | 각 특성을 주어진 범위로 스케일링.                   |
| [`MultiLabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer "sklearn.preprocessing.MultiLabelBinarizer") | 반복 가능한 객체와 다중 레이블 형식 간 변환.            |
| [`Normalizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Normalizer.html#sklearn.preprocessing.Normalizer "sklearn.preprocessing.Normalizer")                                     | 샘플을 개별적으로 단위 노름으로 정규화.                |
| [`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder")                         | 범주형 특성을 원-핫 숫자 배열로 인코딩.               |
| [`OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder")                     | 범주형 특성을 정수 배열로 인코딩.                   |
| [`PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")     | 다항식 및 상호 특성 생성.                       |
| [`PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")             | 데이터를 더 가우시안 형태로 만들기 위해 특성별로 파워 변환 적용. |
| [`QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer") | 분위수 정보를 사용하여 특성 변환.                   |
| [`RobustScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler "sklearn.preprocessing.RobustScaler")                             | 이상치에 강한 통계량을 사용하여 특성 스케일링.            |
| [`SplineTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")         | 특성에 대한 단일 변수 B-스플라인 기저 생성.            |
| [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")                     | 평균을 제거하고 단위 분산으로 특성 표준화.              |
| [`TargetEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder")                         | 회귀 및 분류 타겟을 위한 타겟 인코더.                |
| [`add_dummy_feature`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.add_dummy_feature.html#sklearn.preprocessing.add_dummy_feature "sklearn.preprocessing.add_dummy_feature")         | 추가적인 더미 특성으로 데이터셋 보강.                 |
| [`binarize`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.binarize.html#sklearn.preprocessing.binarize "sklearn.preprocessing.binarize")                                             | 배열 또는 scipy.sparse 행렬의 불리언 임계값 처리.    |
| [`label_binarize`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.label_binarize.html#sklearn.preprocessing.label_binarize "sklearn.preprocessing.label_binarize")                     | 일대다 방식으로 레이블 이진화.                     |
| [`maxabs_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.maxabs_scale.html#sklearn.preprocessing.maxabs_scale "sklearn.preprocessing.maxabs_scale")                             | 특성을 -1에서 1 사이의 범위로 스케일링, 희소성을 유지.     |
| [`minmax_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.minmax_scale.html#sklearn.preprocessing.minmax_scale "sklearn.preprocessing.minmax_scale")                             | 각 특성을 주어진 범위로 스케일링.                   |
| [`normalize`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.normalize.html#sklearn.preprocessing.normalize "sklearn.preprocessing.normalize")                                         | 입력 벡터를 개별적으로 단위 노름 (벡터 길이)으로 스케일링.    |
| [`power_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.power_transform.html#sklearn.preprocessing.power_transform "sklearn.preprocessing.power_transform")                 | 데이터를 더 가우시안 형태로 만들기 위한 파라메트릭, 단조 변환.  |
| [`quantile_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.quantile_transform.html#sklearn.preprocessing.quantile_transform "sklearn.preprocessing.quantile_transform")     | 분위수 정보를 사용하여 특성 변환.                   |
| [`robust_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.robust_scale.html#sklearn.preprocessing.robust_scale "sklearn.preprocessing.robust_scale")                             | 축을 따라 데이터셋을 표준화.                      |
| [`scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.scale.html#sklearn.preprocessing.scale "sklearn.preprocessing.scale")                                                         | 축을 따라 데이터셋을 표준화.                      |



## 35. `sklearn.random_projection`
- 랜덤 프로젝션 변환기.
- 랜덤 프로젝션은 데이터의 차원을 줄이는 간단하고 계산 효율적인 방법으로, 약간의 정확도를 희생(추가적인 분산)하여 더 빠른 처리 시간과 작은 모델 크기를 얻습니다.
- 랜덤 프로젝션 행렬의 차원과 분포는 데이터셋의 모든 두 샘플 간의 쌍별 거리를 보존하도록 조정됩니다.
- 랜덤 프로젝션의 효율성 뒤에 있는 주요 이론적 결과는 [존슨-린덴스트라우스 보조정리(위키백과 인용)](https://en.wikipedia.org/wiki/Johnson%E2%80%93Lindenstrauss_lemma)입니다:

> 수학에서 존슨-린덴스트라우스 보조정리는 고차원에서 저차원 유클리드 공간으로 점을 왜곡 없이 임베딩하는 것과 관련된 결과입니다. 이 보조정리는 고차원 공간의 작은 점 집합이 점들 간의 거리를 거의 보존하는 방식으로 훨씬 낮은 차원의 공간에 임베딩될 수 있음을 나타냅니다. 임베딩에 사용되는 맵은 최소한 립시츠 연속(Lipschitz)이며, 심지어 정사영으로도 취할 수 있습니다.

> 자세한 내용은 [랜덤 프로젝션](https://scikit-learn.org/stable/modules/random_projection.html#random-projection) 섹션을 참조하세요.

| 하위 항목                                                                                                                                                                                                                                                               | 설명                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| [`GaussianRandomProjection`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection "sklearn.random_projection.GaussianRandomProjection")                     | 가우시안 랜덤 프로젝션을 통해 차원 축소. |
| [`SparseRandomProjection`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection "sklearn.random_projection.SparseRandomProjection")                             | 희소 랜덤 프로젝션을 통해 차원 축소.   |
| [`johnson_lindenstrauss_min_dim`](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.johnson_lindenstrauss_min_dim.html#sklearn.random_projection.johnson_lindenstrauss_min_dim "sklearn.random_projection.johnson_lindenstrauss_min_dim") | 안전한 랜덤 프로젝션 컴포넌트 수 찾기.  |

## 36. `sklearn.semi_supervised`
- 준지도 학습 알고리즘.
- 이 알고리즘들은 소량의 레이블이 있는 데이터와 대량의 레이블이 없는 데이터를 활용하여 분류 작업을 수행합니다.

> 자세한 내용은 [준지도 학습](https://scikit-learn.org/stable/modules/semi_supervised.html#semi-supervised) 섹션을 참조하세요.

| 하위 항목                                                                                                                                                                                                                             | 설명                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| [`LabelPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation "sklearn.semi_supervised.LabelPropagation")                         | 라벨 전파(classifier) 분류기. |
| [`LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")                                 | 준지도 학습을 위한 라벨 확산 모델.   |
| [`SelfTrainingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.SelfTrainingClassifier.html#sklearn.semi_supervised.SelfTrainingClassifier "sklearn.semi_supervised.SelfTrainingClassifier") | 자기 훈련 분류기.             |

## 37. `sklearn.svm`
- 서포트 벡터 머신 알고리즘.

> 자세한 내용은 [서포트 벡터 머신](https://scikit-learn.org/stable/modules/svm.html#svm) 섹션을 참조하세요.

| 하위 항목                                                                                                                                             | 설명                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [`LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")         | 선형 서포트 벡터 분류.      |
| [`LinearSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html#sklearn.svm.LinearSVR "sklearn.svm.LinearSVR")         | 선형 서포트 벡터 회귀.      |
| [`NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")                         | Nu-서포트 벡터 분류.      |
| [`NuSVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html#sklearn.svm.NuSVR "sklearn.svm.NuSVR")                         | Nu 서포트 벡터 회귀.      |
| [`OneClassSVM`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html#sklearn.svm.OneClassSVM "sklearn.svm.OneClassSVM") | 비지도 이상치 탐지.        |
| [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")                                 | C-서포트 벡터 분류.       |
| [`SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR "sklearn.svm.SVR")                                 | Epsilon-서포트 벡터 회귀. |
| [`l1_min_c`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.l1_min_c.html#sklearn.svm.l1_min_c "sklearn.svm.l1_min_c")             | C의 최저 한계를 반환.      |


## 38. `sklearn.tree`
- 의사 결정 트리 기반 모델을 사용한 분류 및 회귀.
> 자세한 내용은 [의사 결정 트리](https://scikit-learn.org/stable/modules/tree.html#tree) 섹션을 참조하세요.

| 하위 항목                                                                                                                                                                                            | 설명                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- |
| [`DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier") | 의사 결정 트리 분류기.       |
| [`DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")     | 의사 결정 트리 회귀기.       |
| [`ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")             | 극단적으로 무작위화된 트리 분류기. |
| [`ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")                 | 극단적으로 무작위화된 트리 회귀기. |

### 1) 내보내기 (Exporting)

| 하위 항목                                                                                                                                                                | 설명                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| [`export_graphviz`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html#sklearn.tree.export_graphviz "sklearn.tree.export_graphviz") | 의사 결정 트리를 DOT 형식으로 내보내기.      |
| [`export_text`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_text.html#sklearn.tree.export_text "sklearn.tree.export_text")                 | 의사 결정 트리 규칙을 보여주는 텍스트 보고서 작성. |

### 2) 플로팅 (Plotting)

| 하위 항목                                                                                                                                        | 설명            |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| [`plot_tree`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html#sklearn.tree.plot_tree "sklearn.tree.plot_tree") | 의사 결정 트리 그리기. |


## 39. `sklearn.utils`
- 개발을 도와주는 다양한 유틸리티.
> 자세한 내용은 [개발자를 위한 유틸리티](https://scikit-learn.org/stable/developers/utilities.html#developers-utils) 섹션을 참조하세요.

| 하위 항목                                                                                                                                                                                   | 설명                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| [`Bunch`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html#sklearn.utils.Bunch "sklearn.utils.Bunch")                                                         | 키를 속성으로 노출하는 컨테이너 객체.                    |
| [`_safe_indexing`](https://scikit-learn.org/stable/modules/generated/sklearn.utils._safe_indexing.html#sklearn.utils._safe_indexing "sklearn.utils._safe_indexing")                     | 인덱스를 사용하여 X의 행, 항목 또는 열을 반환.             |
| [`as_float_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.as_float_array.html#sklearn.utils.as_float_array "sklearn.utils.as_float_array")                     | 배열 형태를 float 배열로 변환.                     |
| [`assert_all_finite`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.assert_all_finite.html#sklearn.utils.assert_all_finite "sklearn.utils.assert_all_finite")         | X에 NaN 또는 무한대가 포함되어 있으면 ValueError 발생.   |
| [`deprecated`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.deprecated.html#sklearn.utils.deprecated "sklearn.utils.deprecated")                                     | 함수나 클래스를 더 이상 사용되지 않음을 표시하는 데코레이터.       |
| [`estimator_html_repr`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_html_repr.html#sklearn.utils.estimator_html_repr "sklearn.utils.estimator_html_repr") | 추정기의 HTML 표현을 작성.                        |
| [`gen_batches`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.gen_batches.html#sklearn.utils.gen_batches "sklearn.utils.gen_batches")                                 | 0에서 n까지의 `batch_size` 요소를 포함하는 슬라이스 생성기. |
| [`gen_even_slices`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.gen_even_slices.html#sklearn.utils.gen_even_slices "sklearn.utils.gen_even_slices")                 | n까지 균등하게 분할된 `n_packs` 슬라이스 생성기.         |
| [`indexable`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.indexable.html#sklearn.utils.indexable "sklearn.utils.indexable")                                         | 교차 검증을 위한 배열을 인덱싱 가능하게 만듦.               |
| [`murmurhash3_32`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.murmurhash3_32.html#sklearn.utils.murmurhash3_32 "sklearn.utils.murmurhash3_32")                     | 주어진 시드에서 키의 32비트 murmurhash3를 계산.        |
| [`resample`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.resample.html#sklearn.utils.resample "sklearn.utils.resample")                                             | 일관된 방식으로 배열 또는 희소 행렬을 리샘플링.              |
| [`safe_mask`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.safe_mask.html#sklearn.utils.safe_mask "sklearn.utils.safe_mask")                                         | X에 안전하게 사용할 수 있는 마스크 반환.                 |
| [`safe_sqr`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.safe_sqr.html#sklearn.utils.safe_sqr "sklearn.utils.safe_sqr")                                             | 배열과 희소 행렬의 요소별 제곱.                       |
| [`shuffle`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.shuffle.html#sklearn.utils.shuffle "sklearn.utils.shuffle")                                                 | 일관된 방식으로 배열 또는 희소 행렬을 섞기.                |

### 1) 입력 및 파라미터 검증 (Input and parameter validation)

- scikit-learn 추정기 내의 입력 및 파라미터를 검증하는 함수들.

| 하위 항목                                                                                                                                                                                                                       | 설명                                      |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| [`check_X_y`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_X_y.html#sklearn.utils.check_X_y "sklearn.utils.check_X_y")                                                                             | 표준 추정기를 위한 입력 검증.                       |
| [`check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")                                                                     | 배열, 리스트, 희소 행렬 또는 유사한 입력 검증.            |
| [`check_consistent_length`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_consistent_length.html#sklearn.utils.check_consistent_length "sklearn.utils.check_consistent_length")                     | 모든 배열이 일관된 첫 번째 차원을 가지는지 확인.            |
| [`check_random_state`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html#sklearn.utils.check_random_state "sklearn.utils.check_random_state")                                         | 시드를 np.random.RandomState 인스턴스로 변환.     |
| [`check_scalar`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_scalar.html#sklearn.utils.check_scalar "sklearn.utils.check_scalar")                                                                 | 스칼라 파라미터의 타입과 값을 검증.                    |
| [`validation.check_is_fitted`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted")         | 추정기에 대한 is_fitted 검증 수행.                |
| [`validation.check_memory`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_memory.html#sklearn.utils.validation.check_memory "sklearn.utils.validation.check_memory")                     | `memory`가 joblib.Memory 유사한지 확인.        |
| [`validation.check_symmetric`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_symmetric.html#sklearn.utils.validation.check_symmetric "sklearn.utils.validation.check_symmetric")         | 배열이 2D이고, 정사각형이며 대칭인지 확인.               |
| [`validation.column_or_1d`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.column_or_1d.html#sklearn.utils.validation.column_or_1d "sklearn.utils.validation.column_or_1d")                     | 컬럼 또는 1차원 numpy 배열을 평탄화, 그렇지 않으면 오류 발생. |
| [`validation.has_fit_parameter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.has_fit_parameter.html#sklearn.utils.validation.has_fit_parameter "sklearn.utils.validation.has_fit_parameter") | 추정기의 fit 메서드가 주어진 파라미터를 지원하는지 확인.       |

### 2) 메타 추정기 (Meta-estimators)

- 메타 추정기를 위한 유틸리티.

| 하위 항목                                                                                                                                                                                                                   | 설명                              |     |     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | --- | --- |
| [`metaestimators.available_if`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metaestimators.available_if.html#sklearn.utils.metaestimators.available_if "sklearn.utils.metaestimators.available_if") | 검사가 참 값을 반환하는 경우에만 사용할 수 있는 속성. |     |     |

### 3) 클래스 레이블 기반의 가중치 처리 (Weight handling based on class labels)

- 클래스 레이블을 기반으로 가중치를 처리하는 유틸리티.

| 하위 항목                                                                                                                                                                                                                                               | 설명                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| [`class_weight.compute_class_weight`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_class_weight.html#sklearn.utils.class_weight.compute_class_weight "sklearn.utils.class_weight.compute_class_weight")     | 불균형한 데이터셋의 클래스 가중치를 추정합니다.     |
| [`class_weight.compute_sample_weight`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_sample_weight.html#sklearn.utils.class_weight.compute_sample_weight "sklearn.utils.class_weight.compute_sample_weight") | 불균형한 데이터셋의 클래스별 샘플 가중치를 추정합니다. |

### 4) 분류기에서 다중 클래스 타겟 처리 (Dealing with multiclass target in classifiers)

- 분류기에서 다중 클래스/다중 출력 타겟을 처리하는 유틸리티.

| 하위 항목                                                                                                                                                                                                           | 설명                      |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| [`multiclass.is_multilabel`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.is_multilabel.html#sklearn.utils.multiclass.is_multilabel "sklearn.utils.multiclass.is_multilabel")     | `y`가 다중 레이블 형식인지 확인합니다. |
| [`multiclass.type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target") | 타겟으로 표시된 데이터 유형을 결정합니다. |
| [`multiclass.unique_labels`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.unique_labels.html#sklearn.utils.multiclass.unique_labels "sklearn.utils.multiclass.unique_labels")     | 고유한 레이블의 정렬된 배열을 추출합니다. |

### 5) 최적의 수학 연산 수행 (Optimal mathematical operations)

- scikit-learn에서 최적의 수학 연산을 수행하는 유틸리티.

| 하위 항목                                                                                                                                                                                                                                   | 설명                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| [`extmath.density`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.density.html#sklearn.utils.extmath.density "sklearn.utils.extmath.density")                                                                 | 희소 벡터의 밀도를 계산합니다.                        |
| [`extmath.fast_logdet`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.fast_logdet.html#sklearn.utils.extmath.fast_logdet "sklearn.utils.extmath.fast_logdet")                                                 | 정방 행렬의 행렬식을 로그로 계산합니다.                   |
| [`extmath.randomized_range_finder`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_range_finder.html#sklearn.utils.extmath.randomized_range_finder "sklearn.utils.extmath.randomized_range_finder") | A의 범위를 근사하는 직교 행렬을 계산합니다.                |
| [`extmath.randomized_svd`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.randomized_svd.html#sklearn.utils.extmath.randomized_svd "sklearn.utils.extmath.randomized_svd")                                     | 축소된 무작위 SVD를 계산합니다.                      |
| [`extmath.safe_sparse_dot`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.safe_sparse_dot.html#sklearn.utils.extmath.safe_sparse_dot "sklearn.utils.extmath.safe_sparse_dot")                                 | 희소 행렬의 경우를 올바르게 처리하는 도트 제품입니다.           |
| [`extmath.weighted_mode`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.weighted_mode.html#sklearn.utils.extmath.weighted_mode "sklearn.utils.extmath.weighted_mode")                                         | 전달된 배열에서 가중치가 있는 모드(가장 흔한 값)의 배열을 반환합니다. |

### 6) 희소 행렬 및 배열 작업 (Working with sparse matrices and arrays)

- 희소 행렬 및 배열 작업을 위한 유틸리티 모음.

| 하위 항목                                                                                                                                                                                                                                                       | 설명                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| [`sparsefuncs.incr_mean_variance_axis`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.incr_mean_variance_axis.html#sklearn.utils.sparsefuncs.incr_mean_variance_axis "sklearn.utils.sparsefuncs.incr_mean_variance_axis")     | CSR 또는 CSC 행렬의 축을 따라 증가하는 평균 및 분산을 계산합니다. |
| [`sparsefuncs.inplace_column_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_column_scale.html#sklearn.utils.sparsefuncs.inplace_column_scale "sklearn.utils.sparsefuncs.inplace_column_scale")                 | CSC/CSR 행렬의 열을 제자리에서 스케일링합니다.             |
| [`sparsefuncs.inplace_csr_column_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_csr_column_scale.html#sklearn.utils.sparsefuncs.inplace_csr_column_scale "sklearn.utils.sparsefuncs.inplace_csr_column_scale") | CSR 행렬의 열을 제자리에서 스케일링합니다.                 |
| [`sparsefuncs.inplace_row_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_row_scale.html#sklearn.utils.sparsefuncs.inplace_row_scale "sklearn.utils.sparsefuncs.inplace_row_scale")                             | CSR 또는 CSC 행렬의 행을 제자리에서 스케일링합니다.          |
| [`sparsefuncs.inplace_swap_column`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_swap_column.html#sklearn.utils.sparsefuncs.inplace_swap_column "sklearn.utils.sparsefuncs.inplace_swap_column")                     | CSC/CSR 행렬의 두 열을 제자리에서 교환합니다.             |
| [`sparsefuncs.inplace_swap_row`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.inplace_swap_row.html#sklearn.utils.sparsefuncs.inplace_swap_row "sklearn.utils.sparsefuncs.inplace_swap_row")                                 | CSC/CSR 행렬의 두 행을 제자리에서 교환합니다.             |
| [`sparsefuncs.mean_variance_axis`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.mean_variance_axis.html#sklearn.utils.sparsefuncs.mean_variance_axis "sklearn.utils.sparsefuncs.mean_variance_axis")                         | CSR 또는 CSC 행렬의 축을 따라 평균 및 분산을 계산합니다.      |

- Cython으로 작성된 희소 행렬 및 배열 작업을 위한 유틸리티.

| 하위 항목                                                                                                                                                                                                                                                                                           | 설명                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| [`sparsefuncs_fast.inplace_csr_row_normalize_l1`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l1.html#sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l1 "sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l1") | CSR 행렬 또는 배열의 행을 L1 노름으로 제자리에서 정규화합니다. |
| [`sparsefuncs_fast.inplace_csr_row_normalize_l2`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l2.html#sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l2 "sklearn.utils.sparsefuncs_fast.inplace_csr_row_normalize_l2") | CSR 행렬 또는 배열의 행을 L2 노름으로 제자리에서 정규화합니다. |
### 7) 그래프 작업 (Working with graphs)
- 그래프 유틸리티와 알고리즘.

| 하위 항목                                                                                                                                                                                                                                                                       | 설명                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| [`graph.single_source_shortest_path_length`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.graph.single_source_shortest_path_length.html#sklearn.utils.graph.single_source_shortest_path_length "sklearn.utils.graph.single_source_shortest_path_length") | 출발지에서 모든 도달 가능한 노드까지의 최단 경로 길이를 반환합니다. |

### 8) 랜덤 샘플링 (Random sampling)

- 랜덤 샘플링을 위한 유틸리티.

| 하위 항목                                                                                                                                                                                                                                           | 설명              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [`random.sample_without_replacement`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.random.sample_without_replacement.html#sklearn.utils.random.sample_without_replacement "sklearn.utils.random.sample_without_replacement") | 비복원 추출로 정수 샘플링. |

### 9) 배열 작업을 위한 보조 함수 (Auxiliary functions that operate on arrays)

- 배열 작업을 위한 보조 함수 모음.

| 하위 항목                                                                                                                                                                               | 설명                    |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| [`arrayfuncs.min_pos`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.arrayfuncs.min_pos.html#sklearn.utils.arrayfuncs.min_pos "sklearn.utils.arrayfuncs.min_pos") | 배열의 양수 값 중 최소값을 찾습니다. |

### 10) 메타데이터 라우팅 (Metadata routing)

- scikit-learn 추정기 내에서 메타데이터를 라우팅하기 위한 유틸리티.

> 자세한 내용은 [메타데이터 라우팅](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing) 섹션을 참조하세요.

| 하위 항목                                                                                                                                                                                                                                                                   | 설명                                                |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| [`metadata_routing.MetadataRequest`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRequest.html#sklearn.utils.metadata_routing.MetadataRequest "sklearn.utils.metadata_routing.MetadataRequest")                             | 소비자의 메타데이터 요청 정보를 포함합니다.                          |
| [`metadata_routing.MetadataRouter`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MetadataRouter.html#sklearn.utils.metadata_routing.MetadataRouter "sklearn.utils.metadata_routing.MetadataRouter")                                 | 라우터 객체에 대한 메타데이터 라우팅을 저장하고 처리합니다.                 |
| [`metadata_routing.MethodMapping`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.MethodMapping.html#sklearn.utils.metadata_routing.MethodMapping "sklearn.utils.metadata_routing.MethodMapping")                                     | 라우터에 대한 호출자와 피호출자 메서드 간의 매핑을 저장합니다.               |
| [`metadata_routing.get_routing_for_object`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.get_routing_for_object.html#sklearn.utils.metadata_routing.get_routing_for_object "sklearn.utils.metadata_routing.get_routing_for_object") | 주어진 객체에서 `Metadata{Router, Request}` 인스턴스를 가져옵니다. |
| [`metadata_routing.process_routing`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metadata_routing.process_routing.html#sklearn.utils.metadata_routing.process_routing "sklearn.utils.metadata_routing.process_routing")                             | 입력 매개변수를 검증하고 라우팅합니다.                             |

### 11) scikit-learn 객체 발견 (Discovering scikit-learn objects)

- scikit-learn 객체를 발견하기 위한 유틸리티.

| 하위 항목                                                                                                                                                                                               | 설명                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| [`discovery.all_displays`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.discovery.all_displays.html#sklearn.utils.discovery.all_displays "sklearn.utils.discovery.all_displays") | `sklearn`의 모든 디스플레이 목록을 가져옵니다. |

### 12) API 호환성 검사기 (API compatibility checkers)

- scikit-learn API와 추정기의 호환성을 검사하기 위한 다양한 유틸리티.

| 하위 항목                                                                                                                                                                                                                                                                       | 설명                                  |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| [`estimator_checks.check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")                                 | 추정기가 scikit-learn 규칙을 준수하는지 확인합니다.  |
| [`estimator_checks.parametrize_with_checks`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "sklearn.utils.estimator_checks.parametrize_with_checks") | 추정기 검사를 매개변수화하기 위한 Pytest 특정 데코레이터. |

### 13) 병렬 컴퓨팅 (Parallel computing)

- scikit-learn 사용을 위한 [`joblib`](https://joblib.readthedocs.io/en/latest/index.html#module-joblib "(in joblib v1.5.dev0)") 도구의 사용자 지정.

| 하위 항목                                                                                                                                                                           | 설명                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`parallel.Parallel`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.Parallel.html#sklearn.utils.parallel.Parallel "sklearn.utils.parallel.Parallel") | scikit-learn 구성을 전파하는 [`joblib.Parallel`](https://joblib.readthedocs.io/en/latest/generated/joblib.Parallel.html#joblib.Parallel "(in joblib v1.5.dev0)")의 수정 버전. |
| [`parallel.delayed`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel.delayed.html#sklearn.utils.parallel.delayed "sklearn.utils.parallel.delayed")     | 함수의 인수를 캡처하기 위해 사용되는 데코레이터.                                                                                                                                       |


---
## 참조
[API Reference — scikit-learn 1.5.0 documentation](https://scikit-learn.org/stable/api/index.html)
[Examples — scikit-learn 1.5.0 documentation](https://scikit-learn.org/stable/auto_examples/index.html#general-examples)
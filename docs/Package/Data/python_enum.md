---
title: "[Python] enum"
excerpt: 
categories:
  - Python
tags:
  - Python-Data
  - Python-enum
  - Enum
last_modified_at: 2024-03-01T00:00:00-00:00
link: 
상위 항목: "[[python_data|파이썬 데이터 라이브러리 (Python Data Library)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

---
## Auto
`enum.auto()`를 사용할 때의 값 할당에 대해 설명해 드리겠습니다.

`enum.auto()`는 Enum 클래스에서 자동으로 고유한 값을 생성하는 데 사용됩니다. 그러나 여기서 중요한 점은 `ObjectType`이 `str`을 상속받고 있다는 것입니다. 이 경우, `auto()`의 동작이 일반적인 `Enum`과는 다릅니다.

1. 일반적인 `Enum`에서의 `auto()`:
   보통 `auto()`는 정수 값을 자동으로 할당합니다. 첫 번째 멤버에 1을 할당하고, 그 다음부터는 이전 값에 1을 더한 값을 할당합니다.

2. `str`을 상속받은 `Enum`에서의 `auto()`:
   이 경우, `auto()`는 각 멤버의 이름을 문자열 값으로 사용합니다.

따라서, 주어진 코드에서 `ObjectType` Enum의 각 멤버에는 다음과 같은 값이 할당됩니다:

- `ObjectType.TEXT`: `"TEXT"`
- `ObjectType.IMAGE`: `"IMAGE"`
- `ObjectType.INDEX`: `"INDEX"`
- `ObjectType.DOCUMENT`: `"DOCUMENT"`

각 멤버의 값은 해당 멤버의 이름과 동일한 문자열이 됩니다.

이를 확인하기 위해 다음과 같은 코드를 실행할 수 있습니다:

```python
print(ObjectType.TEXT)  # 출력: ObjectType.TEXT
print(ObjectType.TEXT.value)  # 출력: TEXT
print(ObjectType.IMAGE.value)  # 출력: IMAGE
print(ObjectType.INDEX.value)  # 출력: INDEX
print(ObjectType.DOCUMENT.value)  # 출력: DOCUMENT
```

이러한 방식은 Enum 값을 문자열로 직접 사용하고 싶을 때 유용합니다. 예를 들어, 데이터베이스에 저장하거나 API 응답으로 사용할 때 이러한 문자열 값이 더 명확하고 사용하기 쉬울 수 있습니다.

---

## 예제

## 참조

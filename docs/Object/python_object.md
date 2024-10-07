---
title: "[Python] 객체 (Object)"
excerpt: 객체 (Objects)는 파이썬이 데이터(data)를 추상화한 것(abstraction)입니다. 파이썬 프로그램의 모든 데이터는 객체나 객체 간의 관계로 표현됩니다. (폰 노이만(Von Neumann)의 “프로그램 내장식 컴퓨터(stored program computer)” 모델을 따르고, 또 그 관점에서 코드 역시 객체로 표현됩니다.)
categories:
  - Python
tags:
  - Python
  - Object
last_modified_at: 2024-04-11T15:10:55+09:00
link: 
상위 항목: "[[python_home|파이썬 (Python)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

**하위 항목**
- [[python_class|파이썬 클래스 (Python Class)]]
- [[python_function|파이썬 함수 (Python Function)]]
- [[python_variable|파이썬 변수 (Python Variable)]]
---

- _객체 (Objects)_ 는 파이썬이 데이터(data)를 추상화한 것(abstraction)입니다. 파이썬 프로그램의 모든 데이터는 객체나 객체 간의 관계로 표현됩니다. (폰 노이만(Von Neumann)의 “프로그램 내장식 컴퓨터(stored program computer)” 모델을 따르고, 또 그 관점에서 코드 역시 객체로 표현됩니다.)
- 모든 객체에는 아이덴티티, 타입, 값이 있습니다. 객체의 _아이덴티티_ 는 한 번 생성되면 절대 변하지 않으며, 메모리에 있는 객체의 주소라고 생각하면 됩니다. [`is`](https://docs.python.org/ko/3.12/reference/expressions.html#is) 연산자는 두 객체의 ID를 비교하고, [`id()`](https://docs.python.org/ko/3.12/library/functions.html#id "id") 함수는 해당 객체의 ID를 나타내는 정수를 반환합니다.

> **CPython 구현 상세:** CPython 의 경우, `id(x)` 는 `x` 가 저장된 메모리의 주소입니다.

- 객체의 형은 객체가 지원하는 연산들을 정의하고 (예를 들어, “길이를 갖고 있나?”) 그 형의 객체들이 가질 수 있는 가능한 값들을 정의합니다. [`type()`](https://docs.python.org/ko/3.12/library/functions.html#type "type") 함수는 객체의 형(이것 역시 객체다)을 돌려줍니다. 아이덴티티와 마찬가지로, 객체의 _형 (type)_ 역시 변경되지 않습니다.
- 어떤 객체들의 _값_ 은 변경할 수 있습니다. 값을 변경할 수 있는 객체들을 _가변(mutable)_ 이라고 합니다. 일단 만들어진 후에 값을 변경할 수 없는 객체들을 _불변(immutable)_ 이라고 합니다. (가변 객체에 대한 참조를 저장하고 있는 불변 컨테이너의 값은 가변 객체의 값이 변할 때 변경된다고 볼 수도 있습니다; 하지만 저장하고 있는 객체들의 집합이 바뀔 수 없으므로 컨테이너는 여전히 불변이라고 여겨집니다. 따라서 불변성은 엄밀하게는 변경 불가능한 값을 갖는 것과는 다릅니다. 좀 더 미묘합니다.) 객체의 가변성(mutability)은 그것의 형에 의해 결정됩니다; 예를 들어 숫자, 문자열, 튜플(tuple)은 불변이지만, 딕셔너리(dictionary) 와 리스트(list)는 가변입니다.
- 객체는 결코 명시적으로 파괴되지 않습니다; 더 참조되지 않을 때(unreachable) 가비지 수거(garbage collect)됩니다. 구현이 가비지 수거를 지연시키거나 아예 생략하는 것이 허락됩니다 — 아직 참조되는 객체들을 수거하지 않는 이상 가비지 수거가 어떤 식으로 구현되는지는 구현의 품질 문제입니다.

> **CPython 구현 상세:** CPython 은 현재 참조 횟수 계산(reference-counting) 방식을 사용하는데, (선택 사항으로) 순환적으로 연결된 가비지의 지연된 감지가 추가됩니다. 이 방법으로 대부분 객체를 참조가 제거되자마자 수거할 수 있습니다. 하지만 순환 참조가 있는 가비지들을 수거한다는 보장은 없습니다. 순환적 가비지 수거의 제어에 관한 정보는 [`gc`](https://docs.python.org/ko/3.12/library/gc.html#module-gc "gc: Interface to the cycle-detecting garbage collector.") 모듈 문서를 참조하면 됩니다. 다른 구현들은 다른 식으로 동작하고, CPython 도 변경될 수 있습니다. 참조가 제거될 때 즉각적으로 파이널리제이션(finalization)되는 것에 의존하지 말아야 합니다 (그래서 항상 파일을 명시적으로 닫아주어야 합니다).

- 구현의 추적 또는 디버깅 기능을 사용하면 일반적으로 수집할 수 있는 객체가 살아 있을 수 있다는 점에 유의하세요. 또한 [`try`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#try)...[`except`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#except) 문으로 예외를 잡으면 객체가 계속 살아 있을 수 있다는 점에 유의하세요.
- 일부 객체에는 열린 파일이나 창과 같은 "외부" 리소스에 대한 참조가 포함되어 있습니다. 이러한 리소스는 객체가 가비지 수집될 때 해제되는 것으로 이해되지만 가비지 수집이 보장되지 않기 때문에 이러한 객체는 외부 리소스를 해제하는 명시적 방법(일반적으로 `close()` 메서드)을 제공하기도 합니다. 프로그램은 이러한 객체를 명시적으로 닫을 것을 강력히 권장합니다. [`try`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#try)...[`finally`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#finally) 문과 `with`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#with) 문은 이 작업을 편리하게 수행할 수 있는 방법을 제공합니다.
- 어떤 객체들은 다른 객체에 대한 참조를 포함하고 있습니다. 이런 것들을 _컨테이너(container)_ 라고 부릅니다. 튜플, 리스트, 딕셔너리등이 컨테이너의 예입니다. 이 참조들은 컨테이너의 값의 일부입니다. 대부분은, 우리가 컨테이너의 값을 논할 때는, 들어있는 객체들의 아이덴티티 보다는 값을 따집니다. 하지만, 컨테이너의 가변성에 대해 논할 때는 직접 가진 객체들의 아이덴티티만을 따집니다. 그래서, (튜플 같은) 불변 컨테이너가 가변 객체로의 참조를 하고 있다면, 그 가변 객체가 변경되면 컨테이너의 값도 변경됩니다.
- 타입은 객체 동작의 거의 모든 측면에 영향을 미칩니다. 불변 타입의 경우 새로운 값을 계산하는 연산은 실제로 동일한 타입과 값을 가진 기존 객체에 대한 참조를 반환할 수 있지만, 변경 가능한 객체의 경우 이는 허용되지 않습니다. 예를 들어, `a = 1; b = 1` 뒤의 _a_ 와 _b_ 는 구현에 따라 값이 1인 동일한 객체를 참조할 수도 있고 그렇지 않을 수도 있습니다. 이는 [`int`](https://docs.python.org/ko/3.12/library/functions.html#int "int")가 불변 유형이므로 `1`에 대한 참조를 재사용할 수 있기 때문입니다. 이 동작은 사용된 구현에 따라 달라지므로 의존해서는 안 되지만 객체 식별 테스트를 사용할 때 주의해야 할 사항입니다. 그러나 `c = []; d = []` 이후 _c_ 와 _d_ 는 두 개의 서로 다른 고유한 새로 생성된 빈 목록을 참조하도록 보장됩니다. (`e = f = []`는 _동일한_ 객체를 _e_와 _f_ 모두에 할당합니다.)

## 표준형 계층
- 아래에 파이썬에 내장된 형들의 목록이 있습니다. (구현에 따라 C 나 자바나 다른 언어로 작성된) 확장 모듈들은 추가의 형을 정의할 수 있습니다. 파이썬의 미래 버전 역시 형 계층에 형을 더할 수 있는데 (예를 들어, 유리수, 효율적으로 저장된 정수 배열 등등), 표준 라이브러리를 통해 추가될 가능성이 더 크기는 합니다.
- 아래에 나오는 몇몇 형에 대한 설명은 ‘특수 어트리뷰트(special attribute)’ 를 나열하는 문단을 포함합니다. 이것들은 구현에 접근할 방법을 제공하는데, 일반적인 사용을 위한 것이 아닙니다. 정의는 앞으로 변경될 수 있습니다.

### None
- 이 형은 하나의 값만을 갖습니다. 이 값을 갖는 하나의 객체가 존재합니다. 이 객체에는 내장된 이름 `None` 을 통해 접근합니다. 여러 가지 상황에서 값의 부재를 알리는 데 사용됩니다. 예를 들어, 명시적으로 뭔가를 돌려주지 않는 함수의 반환 값입니다. 논리값은 거짓입니다.

### NotImplemented

- 이 유형에는 단일 값이 있습니다. 이 값을 가진 객체가 하나 있습니다. 이 객체는 기본 제공 이름 [`NotImplemented`](https://docs.python.org/ko/3.12/library/constants.html#NotImplemented "NotImplemented")를 통해 액세스됩니다. 숫자 메서드와 풍부한 비교 메서드는 제공된 피연산자에 대한 연산을 구현하지 않는 경우 이 값을 반환해야 합니다. (그러면 인터프리터는 연산자에 따라 반영된 연산 또는 다른 폴백을 시도합니다.) 이 값은 부울 컨텍스트에서 평가되어서는 안 됩니다. 더 자세한 내용은 [산술 연산 구현](https://docs.python.org/ko/3.12/library/numbers.html#implementing-the-arithmetic-operations) 을 참고하십시오.

> 버전 3.9에서 변경: 부울 컨텍스트에서 [`NotImplemented`](https://docs.python.org/ko/3.12/library/constants.html#NotImplemented "NotImplemented")를 평가하는 것은 더 이상 사용되지 않습니다. 현재 참으로 평가하는 동안에는 [`DeprecationWarning`](https://docs.python.org/ko/3.12/library/exceptions.html#DeprecationWarning "DeprecationWarning")을 내보냅니다. 파이썬의 향후 버전에서는 [`TypeError`](https://docs.python.org/ko/3.12/library/exceptions.html#TypeError "TypeError")를 발생시킬 것입니다.

### Ellipsis
- 이 형은 하나의 값만을 갖습니다. 이 값을 갖는 하나의 객체가 존재합니다. 이 객체에는 리터럴 `...` 이나 내장된 이름 `Ellipsis` 을 통해 접근합니다. 논리값은 참입니다.

### [`numbers.Number`](https://docs.python.org/ko/3.12/library/numbers.html#numbers.Number "numbers.Number")
- 이것들은 숫자 리터럴에 의해 만들어지고, 산술 연산과 내장 산술 함수들이 결과로 돌려줍니다. 숫자 객체는 불변입니다; 한 번 값이 만들어지면 절대 변하지 않습니다. 파이썬의 숫자는 당연히 수학적인 숫자들과 밀접하게 관련되어 있습니다, 하지만 컴퓨터의 숫자 표현상의 제약을 받고 있습니다.
- 숫자 클래스의 문자열 표현은 [`__repr__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__repr__ "object.__repr__") 및 [`__str__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__str__ "object.__str__")에 의해 계산되며, 다음과 같은 속성을 가집니다:
  - 클래스 생성자에 전달될 때 원래 숫자 값을 가진 객체를 생성하는 유효한 숫자 리터럴 입니다.
  - 가능하면, 표현은 10진법입니다.
  - 소수점 앞의 단일 0을 제외하고, 선행 0은 표시되지 않습니다.
  - 소수점 뒤의 단일 0을 제외하고, 후행 0은 표시되지 않습니다.
  - 부호는 숫자가 음수일 때만 표시됩니다.

- 파이썬은 정수, 부동 소수점 숫자, 복소수를 구분합니다:

#### [`numbers.Integral`](https://docs.python.org/ko/3.12/library/numbers.html#numbers.Integral "numbers.Integral")
- 이것들은 수학적인 정수 집합(양과 음)에 속하는 요소들을 나타냅니다.

> 정수 표현 규칙은 음수가 포함된 시프트와 마스크 연산에 가장 의미 있는 해석을 제공하기 위한 것입니다.

- 두 가지 종류의 정수가 있습니다:
  
  - 정수 ([`int`](https://docs.python.org/ko/3.12/library/functions.html#int "int"))
  이것은 (가상) 메모리가 허락하는 한, 제약 없는 범위의 숫자를 표현합니다. 시프트(shift)와 마스크(mask) 연산이 목적일 때는 이진 표현이 가정되고, 음수는 일종의 2의 보수(2’s complement)로 표현되는데, 부호 비트가 왼쪽으로 무한히 확장된 것과 같은 효과를 줍니다.
  
  - 불린 ([`bool`](https://docs.python.org/ko/3.12/library/functions.html#bool "bool"))
  이것은 논리값 거짓과 참을 나타냅니다. `False` 와 `True` 두 객체만 불린 형 객체입니다. 불린 형은 int 형의 자식형(subtype)이고, 대부분 상황에서 각기 0과1처럼 동작합니다. 예외는 문자열로 변환되는 경우인데, 각기 문자열 `"False"` 와 `"True"` 가 반환됩니다.

#### [`numbers.Real`](https://docs.python.org/ko/3.12/library/numbers.html#numbers.Real "numbers.Real") ([`float`](https://docs.python.org/ko/3.12/library/functions.html#float "float"))
- 이는 기계 수준의 배정밀도 부동 소수점 숫자를 나타냅니다. 허용되는 범위와 오버플로 처리는 기본 머신 아키텍처(및 C 또는 Java 구현)의 자비에 달려 있습니다. 파이썬은 단정밀도 부동소수점을 지원하지 않으며, 일반적으로 부동소수점을 사용하는 이유인 프로세서 및 메모리 사용량 절감은 파이썬에서 객체를 사용하는 오버헤드에 비해 왜소하므로 두 가지 종류의 부동소수점으로 언어를 복잡하게 만들 이유가 없습니다.

#### [`numbers.Complex`](https://docs.python.org/ko/3.12/library/numbers.html#numbers.Complex "numbers.Complex") ([`complex`](https://docs.python.org/ko/3.12/library/functions.html#complex "complex"))

- 복소수는 한 쌍의 기계 수준 배정밀도 부동소수점 숫자로 표현됩니다. 부동 소수점 숫자와 동일한 주의 사항이 적용됩니다. 복소수 `z`의 실수 부분과 허수 부분은 읽기 전용 속성인 `z.real`과 `z.imag`을 통해 검색할 수 있습니다.

### 시퀀스들
- 이들은 음수가 아닌 숫자로 인덱싱된 유한 정렬 집합을 나타냅니다. 내장 함수 [`len()`](https://docs.python.org/ko/3.12/library/functions.html#len “len”)은 시퀀스의 항목 수를 반환합니다. 수열의 길이가 _n_ 일 때 인덱스 집합은 숫자 0, 1, …, _n_-1을 포함합니다. 시퀀스 _a_ 의 항목 _i_ 는 `a[i]`에 의해 선택됩니다. 기본 제공 시퀀스를 포함한 일부 시퀀스는 시퀀스 길이를 더하여 음수 첨자를 해석합니다. 예를 들어 `a[-2]`는 길이가 `n`인 시퀀스 a의 두 번째에서 마지막 항목인 `a[n-2]`와 같습니다.
- 시퀀스는 조각화도 지원합니다: `a[i:j]`는 _i_ `<=` _k_ `<` _j_ 가 되도록 인덱스 _k_ 를 가진 모든 항목을 선택합니다. 표현식으로 사용될 때 슬라이스는 동일한 유형의 시퀀스입니다. 음수 인덱스에 대한 위의 설명은 음수 슬라이스 위치에도 적용됩니다.
- 어떤 시퀀스는 세 번째 “스텝(step)” 매개변수를 사용하는 “확장 슬라이싱(extended slicing)”도 지원합니다: `a[i:j:k]` 는 `x = i + n*k`, _n_ `>=` `0`, _i_ `<=` _x_ `<` _j_ 를 만족하는 모든 항목 _x_ 를 선택합니다.
- 시퀀스는 불변성에 따라 구분됩니다

#### 불변 시퀀스
- 불변 시퀀스 형의 객체는 일단 만들어진 후에는 변경될 수 없습니다. (만약 다른 객체로의 참조를 포함하면, 그 객체는 가변일 수 있고, 변경될 수 있습니다; 하지만, 불변 객체로부터 참조되는 객체의 집합 자체는 변경될 수 없습니다.)
- 다음과 같은 형들은 불변 시퀀스입니다:
  
  - 문자열(Strings)
  문자열은 유니코드 코드 포인트를 나타내는 값의 시퀀스입니다. `U+0000 - U+10FFFF` 범위의 모든 코드 포인트는 문자열로 표현할 수 있습니다. 파이썬에는 문자 유형이 없으며, 대신 문자열의 모든 코드 포인트는 길이가 `1`인 문자열 객체로 표현됩니다. 내장 함수 [`ord()`](https://docs.python.org/ko/3.12/library/functions.html#ord "ord")는 코드 포인트를 문자열 형식에서 `0 - 10FFFF` 범위의 정수로 변환하고, [`chr()`](https://docs.python.org/ko/3.12/library/functions.html#chr "chr")은 `0 - 10FFFF` 범위의 정수를 해당 길이 `1` 문자열 객체로 변환합니다. [`str.encode()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.encode "str.encode")는 주어진 텍스트 인코딩을 사용하여 [`str`](https://docs.python.org/ko/3.12/library/stdtypes.html#str "str")을 [`bytes`](https://docs.python.org/ko/3.12/library/stdtypes.html#bytes "bytes")로 변환하는 데 사용할 수 있으며, [`bytes.decode()`](https://docs.python.org/ko/3.12/library/stdtypes.html#bytes.decode "bytes.decode")는 반대의 결과를 얻는데 사용할 수 있습니다.
  
  - 튜플(Tuples)
  튜플의 항목은 임의의 파이썬 객체입니다. 두 개 이상의 항목으로 구성되는 튜플은 콤마로 분리된 표현식의 목록으로 만들 수 있습니다. 하나의 항목으로 구성된 튜플(싱글턴,singleton)은 표현식에 콤마를 붙여서 만들 수 있습니다(괄호로 표현식을 묶을 수 있으므로, 표현식 만으로는 튜플을 만들지 않습니다). 빈 튜플은 한 쌍의 빈 괄호로 만들 수 있습니다.
  
  - 바이트열(Bytes)
  바이트열(bytes) 객체는 불변 배열입니다. 항목은 8-비트 바이트인데, 0 <= x < 256 범위의 정수로 표현됩니다. 바이트 객체를 만들 때는 바이트열 리터럴(`b'abc'` 와 같은) 과 내장 [`bytes()`](https://docs.python.org/ko/3.12/library/stdtypes.html#bytes "bytes") 생성자(constructor)를 사용할 수 있습니다. 또한, 바이트열 객체는 [`decode()`](https://docs.python.org/ko/3.12/library/stdtypes.html#bytes.decode "bytes.decode") 메서드를 통해 문자열로 디코딩될 수 있습니다.

#### 가변 시퀀스

- 가변 시퀀스는 만들어진 후에 변경될 수 있습니다. 서브스크립션(subscription)과 슬라이싱은 대입문과 [`del`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#del) (삭제) 문의 대상으로 사용될 수 있습니다.

> [`collection`](https://docs.python.org/ko/3.12/library/collections.html#module-collections "컬렉션: 컨테이너 데이터 타입") 및 [`array`](https://docs.python.org/ko/3.12/library/array.html#module-array "array: 균일하게 입력된 숫자 값의 공간 효율적인 배열.") 모듈은 변경 가능한 시퀀스 타입의 추가 예제를 제공합니다.

- 현재 두 개의 내장 가변 시퀀스형이 있습니다:
  
  - 리스트(Lists)
  리스트의 항목은 임의의 파이썬 객체입니다. 리스트는 콤마로 분리된 표현식을 대괄호 안에 넣어서 만들 수 있습니다. (길이 0이나 1의 리스트를 만드는데 별도의 규칙이 필요 없습니다.)
  
  - 바이트 배열(Byte Arrays)
  바이트 배열(bytearray) 객체는 가변 배열입니다. 내장 [`bytearray()`](https://docs.python.org/ko/3.12/library/stdtypes.html#bytearray "bytearray") 생성자로 만들어집니다. 가변이라는 것(그래서 해싱 불가능하다는 것)을 제외하고, 바이트 배열은 불변 바이트열( [`bytes`](https://docs.python.org/ko/3.12/library/stdtypes.html#bytes "bytes")) 객체와 같은 인터페이스와 기능을 제공합니다.

### 집합 형들(Set types)

- 이것들은 중복 없는 불변 객체들의 순서 없고 유한한 집합을 나타냅니다. 인덱싱할 수 없습니다. 하지만 이터레이트할 수 있고, 내장 함수 [`len()`](https://docs.python.org/ko/3.12/library/functions.html#len "len") 은 집합 안에 있는 항목들의 개수를 돌려줍니다. 집합의 일반적인 용도는 빠른 멤버십 검사(fast membership testing), 시퀀스에서 중복된 항목 제거, 교집합(intersection), 합집합(union), 차집합(difference), 대칭차집합(symmetric difference)과 같은 집합 연산을 계산하는 것입니다.
- 집합의 원소들에는 딕셔너리 키와 같은 불변성 규칙이 적용됩니다. 숫자 형의 경우는 숫자 비교에 관한 일반 원칙이 적용된다는 점에 주의해야 합니다: 만약 두 숫자가 같다고 비교되면(예를 들어, `1` 과 `1.0`), 그중 하나만 집합에 들어갈 수 있습니다.
- 현재 두 개의 내장 집합 형이 있습니다:
  
  - 집합(Sets)
  이것들은 가변 집합을 나타냅니다. 내장 [`set()`](https://docs.python.org/ko/3.12/library/stdtypes.html#set "set") 생성자로 만들 수 있고, `add()` 같은 메서드들을 사용해서 나중에 수정할 수 있습니다.
  
  - 불변 집합(Frozen sets)
  이것들은 불변 집합을 나타냅니다. 내장 [`frozenset()`](https://docs.python.org/ko/3.12/library/stdtypes.html#frozenset "frozenset") 생성자로 만들 수 있습니다. 불변 집합(frozenset)은 불변이고 [해시 가능](https://docs.python.org/ko/3.12/glossary.html#term-hashable) 하므로, 다른 집합의 원소나, 딕셔너리의 키로 사용될 수 있습니다.

### 매핑(Mappings)
- 이것들은 임의의 인덱스 집합으로 인덱싱되는 객체들의 유한한 집합을 나타냅니다. 인덱스 표기법(subscript notation) `a[k]` 는 매핑 `a` 에서 `k` 로 인덱스 되는 항목을 선택합니다; 이것은 표현식에 사용될 수도 있고, 대입이나 [`del`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#del) 문장의 대상이 될 수도 있습니다. 내장 함수 [`len()`](https://docs.python.org/ko/3.12/library/functions.html#len "len") 은 매핑에 포함된 항목들의 개수를 돌려줍니다. 현재 한 개의 내장 매핑 형이 있습니다:

#### 딕셔너리(Dictionaries)

- 이것들은 거의 임의의 인덱스 집합으로 인덱싱되는 객체들의 유한한 집합을 나타냅니다. 키로 사용할 수 없는 것들은 리스트, 딕셔너리나 그 외의 가변형 중에서 아이덴티티가 아니라 값으로 비교되는 것들뿐입니다. 딕셔너리의 효율적인 구현이, 키의 해시값이 도중에 변경되지 않고 계속 같은 값으로 유지되도록 요구하고 있기 때문입니다. 키로 사용되는 숫자 형의 경우는 숫자 비교에 관한 일반 원칙이 적용됩니다: 만약 두 숫자가 같다고 비교되면(예를 들어, `1` 과 `1.0`), 둘 다 같은 딕셔너리 항목을 인덱싱하는데 사용될 수 있습니다.
- 딕셔너리는 삽입 순서를 유지합니다, 키가 딕셔너리에 순차적으로 추가된 순서와 같은 순서로 생성됨을 뜻합니다. 기존 키를 교체해도 순서는 변경되지 않지만, 키를 제거했다가 다시 삽입하면 이전 위치를 유지하는 대신 끝에 추가됩니다.
- 딕셔너리는 가변입니다; `{...}` 표기법으로 만들 수 있습니다 ([딕셔너리 디스플레이](https://docs.python.org/ko/3.12/reference/expressions.html#dict) 섹션을 참고하십시오).
- 확장 모듈 [`dbm.ndbm`](https://docs.python.org/ko/3.12/library/dbm.html#module-dbm.ndbm "dbm.ndbm: The New Database Manager (Unix)") 과 [`dbm.gnu`](https://docs.python.org/ko/3.12/library/dbm.html#module-dbm.gnu "dbm.gnu: GNU database manager (Unix)") 는 추가의 매핑 형을 제공하는데, [`collections`](https://docs.python.org/ko/3.12/library/collections.html#module-collections "collections: Container datatypes") 모듈 역시 마찬가지입니다.

> 버전 3.7에서 변경: 딕셔너리는 3.6 이전의 파이썬 버전에서 삽입 순서를 유지하지 않았습니다. CPython 3.6에서, 삽입 순서가 유지되었지만, 그 시점에는 언어 보증이 아니라 구현 세부 사항으로 간주하였습니다.

### 콜러블(Callable types)

- 이것들은 함수 호출 연산([호출](https://docs.python.org/ko/3.12/reference/expressions.html#calls) 섹션 참고)이 적용될 수 있는 형들입니다:

#### 사용자 정의 함수

- 사용자 정의 함수 객체는 함수 정의를 통해 만들어집니다 ([함수 정의](https://docs.python.org/ko/3.12/reference/compound_stmts.html#function) 섹션 참고). 함수의 형식 매개변수(formal parameter) 목록과 같은 개수의 항목을 포함하는 인자(argument) 목록으로 호출되어야 합니다.

##### 특수 읽기 전용 속성 (Special read-only attributes)

| 어트리뷰트                                                                                                                           | 의미                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| function.__globals__[](https://docs.python.org/ko/3.12/reference/datamodel.html#function.__globals__ "Link to this definition") | 함수가 정의된 모듈의 전역 네임스페이스인 함수의 [전역 변수](https://docs.python.org/ko/3.12/reference/executionmodel.html#naming)를 담고 있는 [`dictionary`](https://docs.python.org/ko/3.12/library/stdtypes.html#dict "딕셔너리")에 대한 참조입니다. |
| function.__closure__[](https://docs.python.org/ko/3.12/reference/datamodel.html#function.__closure__ "Link to this definition") | `None` 또는 함수의 자유 변수에 대한 바인딩을 포함하는 셀의 [`튜플`](https://docs.python.org/ko/3.12/library/stdtypes.html#tuple "튜플")입니다.<br><br>셀 객체는 `cell_contents` 어트리뷰트를 가지고 있습니다. 셀의 값을 읽을 뿐만 아니라 값을 설정하는 데도 사용할 수 있습니다.       |

##### 쓰기 가능한 특수 속성

- 이러한 속성의 대부분은 할당된 값의 유형을 확인합니다:

| 어트리뷰트                                                                                                                                   | 의미                                                                                                                                                                                                                                                                                                                            |
| --------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| function.__doc__[](https://docs.python.org/ko/3.12/reference/datamodel.html#function.__doc__ "Link to this definition")                 | 함수의 설명서 문자열, 사용할 수 없는 경우 `None`입니다. 서브클래스에 의해 상속되지 않습니다.                                                                                                                                                                                                                                                                      |
| function.__name__[](https://docs.python.org/ko/3.12/reference/datamodel.html#function.__name__ "Link to this definition")               | 함수의 이름입니다. 참조하세요: [`__name__ attributes`](https://docs.python.org/ko/3.12/library/stdtypes.html#definition.__name__ "definition.__name__").                                                                                                                                                                                   |
| function.__qualname__[](https://docs.python.org/ko/3.12/reference/datamodel.html#function.__qualname__ "Link to this definition")       | 함수의 [정규화된 이름](https://docs.python.org/ko/3.12/glossary.html#term-qualified-name)입니다. 참조 [`__qualname__ 속성`](https://docs.python.org/ko/3.12/library/stdtypes.html#definition.__qualname__ "definition.__qualname__").<br><br>버전 3.3에 추가되었습니다.                                                                                 |
| function.__module__[](https://docs.python.org/ko/3.12/reference/datamodel.html#function.__module__ "Link to this definition")           | 함수가 정의된 모듈의 이름 또는 (없는 경우) `None`                                                                                                                                                                                                                                                                                              |
| function.__defaults__[](https://docs.python.org/ko/3.12/reference/datamodel.html#function.__defaults__ "Link to this definition")       | 기본값이 있는 매개변수에 대한 기본 [매개변수](https://docs.python.org/ko/3.12/glossary.html#term-parameter) 값을 포함하는 [`tuple`](https://docs.python.org/ko/3.12/library/stdtypes.html#tuple "튜플") 또는 기본값이 없는 매개변수인 경우 `None`입니다.                                                                                                                   |
| function.__code__[](https://docs.python.org/ko/3.12/reference/datamodel.html#function.__code__ "Link to this definition")               | 컴파일된 함수 본문을 나타내는 [코드 객체](https://docs.python.org/ko/3.12/reference/datamodel.html#code-objects)입니다.                                                                                                                                                                                                                           |
| function.__dict__[](https://docs.python.org/ko/3.12/reference/datamodel.html#function.__dict__ "Link to this definition")               | 임의의 함수 속성을 지원하는 네임스페이스입니다. 참조하세요: [`__dict__ attributes`](https://docs.python.org/ko/3.12/library/stdtypes.html#object.__dict__ "object.__dict__").                                                                                                                                                                           |
| function.__annotations__[](https://docs.python.org/ko/3.12/reference/datamodel.html#function.__annotations__ "Link to this definition") | [매개변수](https://docs.python.org/ko/3.12/glossary.html#term-parameter)의 어노테이션을 포함하는 [`dictionary`](https://docs.python.org/ko/3.12/library/stdtypes.html#dict "딕셔너리"). 딕셔너리의 키는 매개변수 이름과 반환 어노테이션에 대한 `'return'`(제공된 경우)입니다. 참조하세요: [어노테이션 모범 사례](https://docs.python.org/ko/3.12/howto/annotations.html#annotations-howto) 참조. |
| function.__kwdefaults__[](https://docs.python.org/ko/3.12/reference/datamodel.html#function.__kwdefaults__ "Link to this definition")   | 키워드 전용 [매개변수](https://docs.python.org/ko/3.12/glossary.html#term-parameter)에 대한 기본값이 포함된 [`dictionary`](https://docs.python.org/ko/3.12/library/stdtypes.html#dict "딕셔너리").                                                                                                                                                   |
| function.__type_params__[](https://docs.python.org/ko/3.12/reference/datamodel.html#function.__type_params__ "Link to this definition") | [일반 함수](https://docs.python.org/ko/3.12/reference/compound_stmts.html#generic-functions)의 [유형 매개변수](https://docs.python.org/ko/3.12/reference/compound_stmts.html#type-params)를 포함하는 [`tuple`](https://docs.python.org/ko/3.12/library/stdtypes.html#tuple "튜플").<br><br>버전 3.12에 추가되었습니다.                                    |

- 함수 객체는 예를 들어 함수에 메타데이터를 첨부하는 데 사용할 수 있는 임의의 속성을 가져오고 설정하는 기능도 지원합니다. 이러한 어트리뷰트를 가져오고 설정하기 위해 일반 어트리뷰트 점 표기법이 사용됩니다.

> **CPython 구현 상세:** CPython의 현재 구현은 사용자 정의 함수에 대한 함수 어트리뷰트만 지원합니다. [내장 함수](https://docs.python.org/ko/3.12/reference/datamodel.html#builtin-functions)의 함수 어트리뷰트는 향후 지원될 수 있습니다.

- 함수의 정의에 대한 추가 정보는 [코드 객체](https://docs.python.org/ko/3.12/reference/datamodel.html#code-objects)([`__code__`](https://docs.python.org/ko/3.12/reference/datamodel.html#function.__code__ "function.__code__") 어트리뷰트를 통해 액세스할 수 있음)에서 검색할 수 있습니다.


#### 인스턴스 메서드(Instance methods)

- 인스턴스 메서드는 클래스, 클래스 인스턴스와 모든 콜러블 객체 (보통 사용자 정의 함수)을 결합합니다.
- 특수 읽기 전용 속성:

|                                                                                                                           |                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| method.__self__[](https://docs.python.org/ko/3.12/reference/datamodel.html#method.__self__ "Link to this definition")     | 메서드가 [바인딩된](https://docs.python.org/ko/3.12/reference/datamodel.html#method-binding) 클래스 인스턴스 객체를 참조합니다.                                                                                                                                                  |
| method.__func__[](https://docs.python.org/ko/3.12/reference/datamodel.html#method.__func__ "Link to this definition")     | 원본 [함수 객체](https://docs.python.org/ko/3.12/reference/datamodel.html#user-defined-funcs)를 참조합니다.                                                                                                                                                           |
| method.__doc__[](https://docs.python.org/ko/3.12/reference/datamodel.html#method.__doc__ "Link to this definition")       | 메서드의 문서([`method.__func__.__doc__`](https://docs.python.org/ko/3.12/reference/datamodel.html#function.__doc__ "function.__doc__")와 동일). 원래 함수에 문서 문자열이 있는 경우 [`string`](https://docs.python.org/ko/3.12/library/stdtypes.html#str "str"), 그렇지 않으면 `None`. |
| method.__name__[](https://docs.python.org/ko/3.12/reference/datamodel.html#method.__name__ "Link to this definition")     | 메서드의 이름([`method.__func__.__name__`](https://docs.python.org/ko/3.12/reference/datamodel.html#function.__name__ "function.__name__"))과 동일합니다.                                                                                                             |
| method.__module__[](https://docs.python.org/ko/3.12/reference/datamodel.html#method.__module__ "Link to this definition") | 메서드가 정의된 모듈의 이름 또는 사용할 수 없는 경우 `None`입니다.                                                                                                                                                                                                                 |
|                                                                                                                           |                                                                                                                                                                                                                                                           |

- 메서드는 기본 [함수 객체](https://docs.python.org/ko/3.12/reference/datamodel.html#user-defined-funcs)의 임의 함수 어트리뷰트에 대한 액세스(설정은 아님)도 지원합니다.
- 사용자 정의 메서드 객체는 클래스의 속성을 가져올 때(아마도 해당 클래스의 인스턴스를 통해) 해당 속성이 사용자 정의 [함수 객체](https://docs.python.org/ko/3.12/reference/datamodel.html#user-defined-funcs) 또는 [`classmethod`](https://docs.python.org/ko/3.12/library/functions.html#classmethod "classmethod") 객체인 경우 생성될 수 있습니다.
- 인스턴스 메소드 객체가 인스턴스 중 하나를 통해 클래스에서 사용자 정의 [함수 객체](https://docs.python.org/ko/3.12/reference/datamodel.html#user-defined-funcs)를 검색하여 생성되는 경우, 그 [`__self__`](https://docs.python.org/ko/3.12/reference/datamodel.html#method.__self__ "method.__self__") 속성이 인스턴스이고 메소드 객체는 _바운드_ 라고 합니다. 새 메서드의 [`__func__`](https://docs.python.org/ko/3.12/reference/datamodel.html#method.__func__ "method.__func__") 속성은 원래 함수 객체입니다.
- 인스턴스 메서드 객체가 클래스 또는 인스턴스에서 [`classmethod`](https://docs.python.org/ko/3.12/library/functions.html#classmethod "classmethod") 객체를 검색하여 생성되면, 그 [`__self__`](https://docs.python.org/ko/3.12/reference/datamodel.html#method.__self__ "method.__self__") 속성은 클래스 자체이고, 그 [`__func__`](https://docs.python.org/ko/3.12/reference/datamodel.html#method.__func__ "method.__func__") 속성은 클래스 메서드의 기초가 되는 함수 객체입니다.
- 인스턴스 메서드 객체가 호출되면 인수 목록 앞에 클래스 인스턴스([`__func__`](https://docs.python.org/ko/3.12/reference/datamodel.html#method.__func__ "method.__func__"))를 삽입하여 기본 함수([`__self__`](https://docs.python.org/ko/3.12/reference/datamodel.html#method.__self__ "method.__self__"))가 호출됩니다. 예를 들어 `C`가 함수 `f()`에 대한 정의를 포함하는 클래스이고 `x`가 `C`의 인스턴스인 경우 `x.f(1)`를 호출하는 것은 `C.f(x, 1)`를 호출하는 것과 동일합니다.
- 인스턴스 메서드 객체가 [`classmethod`](https://docs.python.org/ko/3.12/library/functions.html#classmethod "classmethod") 객체에서 파생된 경우, [`__self__`](https://docs.python.org/ko/3.12/reference/datamodel.html#method.__self__ "method.__self__")에 저장된 "클래스 인스턴스"는 실제로 클래스 자체가 되므로 `x.f(1)` 또는 `C.f(1)`를 호출하는 것은 `f`가 기본 함수인 `f(C,1)`를 호출하는 것과 동일합니다.
- 클래스 인스턴스의 속성인 사용자 정의 함수는 바인딩된 메서드로 변환되지 않으며, 이는 함수가 클래스의 속성인 경우에만 _만_ 발생한다는 점에 유의해야 합니다.

#### 제너레이터 함수(Generator functions)

- [`yield`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#yield) 문([yield 문](https://docs.python.org/ko/3.12/reference/simple_stmts.html#yield) 섹션 참조)을 사용하는 함수 또는 메서드를 _제너레이터 함수_ 라고 합니다. 이러한 함수는 호출되면 항상 함수 본문을 실행하는 데 사용할 수 있는 [이터레이터](https://docs.python.org/ko/3.12/glossary.html#term-iterator) 객체를 반환합니다. 이터레이터의 [`iterator.__next__()`](https://docs.python.org/ko/3.12/library/stdtypes.html#iterator.__next__ "iterator.__next__") 메서드를 호출하면 `yield` 문을 사용하여 값을 제공할 때까지 함수가 실행되도록 합니다. 함수가 [`return`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#return) 문을 실행하거나 끝에서 떨어지면 [`StopIteration`](https://docs.python.org/ko/3.12/library/exceptions.html#StopIteration "StopIteration") 예외가 발생하고 이터레이터가 반환할 값 집합의 끝에 도달한 것입니다.

#### 코루틴 함수(Coroutine functions)

- [`async def`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#async-def) 를 사용해서 정의되는 함수나 메서드를 _코루틴 함수 (coroutine function)_ 라고 부릅니다. 이런 함수를 호출하면 [코루틴](https://docs.python.org/ko/3.12/glossary.html#term-coroutine) 객체를 돌려줍니다. [`await`](https://docs.python.org/ko/3.12/reference/expressions.html#await) 표현식을 비롯해, [`async with`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#async-with) 와 [`async for`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#async-for) 문을 사용할 수 있습니다. [코루틴 객체(Coroutine Objects)](https://docs.python.org/ko/3.12/reference/datamodel.html#coroutine-objects) 섹션을 참조하십시오.

#### 비동기 제너레이터 함수(Asynchronous generator functions)

- [`async def`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#async-def)를 사용하여 정의되고 [`yield`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#yield) 문을 사용하는 함수 또는 메서드를 _비동기 생성자 함수_ 라고 합니다. 이러한 함수가 호출되면 [`async for`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#async-for) 문에서 함수 본문을 실행하는 데 사용할 수 있는 [비동기 이터레이터](https://docs.python.org/ko/3.12/glossary.html#term-asynchronous-iterator) 객체를 반환합니다.
- 비동기 이터레이터의 [`aiterator.__anext__`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__anext__ "object.__anext__") 메서드를 호출하면 [awaitable](https://docs.python.org/ko/3.12/glossary.html#term-awaitable)이 반환되며, 대기 시 [`yield`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#yield) 식을 사용하여 값을 제공할 때까지 실행됩니다. 함수가 빈 [`return`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#return) 문을 실행하거나 끝에서 떨어지면 [`StopAsyncIteration`](https://docs.python.org/ko/3.12/library/exceptions.html#StopAsyncIteration "StopAsyncIteration") 예외가 발생하고 비동기 이터레이터가 산출할 값 집합의 끝에 도달한 것입니다.

#### 내장 함수(Built-in functions)
- 내장 함수 객체는 C 함수를 감싸는 래퍼입니다. 내장 함수의 예로는 [`len()`](https://docs.python.org/ko/3.12/library/functions.html#len "len") 및 [`math.sin()`](https://docs.python.org/ko/3.12/library/math.html#math.sin "math.sin")([`math`](https://docs.python.org/ko/3.12/library/math.html#module-math "math: 수학 함수(sin() 등).")는 표준 내장 모듈입니다). 인수의 수와 유형은 C 함수에 의해 결정됩니다. 특수 읽기 전용 어트리뷰트:
  - '`__doc__`는 함수의 문서 문자열이며, 사용할 수 없는 경우 `None`입니다. [`function.__doc__`](https://docs.python.org/ko/3.12/reference/datamodel.html#function.__doc__ "function.__doc__")를 참조하세요.
  - '`__name__`은 함수의 이름입니다. [`function.__name__`](https://docs.python.org/ko/3.12/reference/datamodel.html#function.__name__ "function.__name__")를 참조하세요.
  - `__self__`는 `None`으로 설정됩니다(하지만 다음 항목 참조).
  - `__module__`은 함수가 정의된 모듈의 이름 또는 사용할 수 없는 경우 `None`입니다. [`function.__module__`](https://docs.python.org/ko/3.12/reference/datamodel.html#function.__module__ "function.__module__")를 참조하세요.

#### 내장 메서드(Built-in methods)

- 이것은 내장 함수의 다른 변장으로, 이번에는 암시적 추가 인수로 C 함수에 전달된 객체를 포함합니다. 내장 메서드의 예로는 _alist_ 가 목록 객체라고 가정할 때 `alist.append()`를 들 수 있습니다. 이 경우 특수 읽기 전용 속성 `__self__`가 _alist_ 로 표시된 객체에 설정됩니다. (이 속성은 [`다른 인스턴스 메서드`](https://docs.python.org/ko/3.12/reference/datamodel.html#method.__self__ "method.__self__")와 동일한 의미를 갖습니다.)

#### 클래스(Classes)

- 클래스는 호출 가능합니다. 이러한 객체는 일반적으로 새 인스턴스를 위한 팩토리 역할을 하지만, [`__new__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__new__ "object.__new__")를 재정의하는 클래스 유형에는 변형이 가능합니다. 호출 인수는 `__new__()`로 전달되며, 일반적인 경우 새 인스턴스를 초기화하기 위해 [`__init__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__init__ "object.__init__")로 전달됩니다.

#### 클래스 인스턴스(Class Instances)

- 임의 클래스의 인스턴스는 해당 클래스에서 [`__call__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__call__ "object.__call__") 메서드를 정의하여 호출 가능하게 만들 수 있습니다.

### 모듈(Modules)

- 모듈은 파이썬 코드의 기본 구성 단위로, [`import`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#import) 문에 의해 호출되거나 [`importlib.import_module()`](https://docs.python.org/ko/3.12/library/importlib.html#importlib.import_module "importlib.import_module") 및 내장 [`__import__()`](https://docs.python.org/ko/3.12/library/functions.html#import__ "__import__") 같은 함수를 호출하여 [import system](https://docs.python.org/ko/3.12/reference/import.html#importsystem)에 의해 만들어집니다. 모듈 객체에는 [`dictionary`](https://docs.python.org/ko/3.12/library/stdtypes.html#dict "dict") 객체에 의해 구현된 네임스페이스가 있습니다(모듈에 정의된 함수의 [`__globals__`](https://docs.python.org/ko/3.12/reference/datamodel.html#function.__globals__ "function.__globals__") 속성에 의해 참조되는 사전입니다). 속성 참조는 이 사전에서 조회로 변환됩니다(예: `m.x`는 `m.__dict__["x"]`와 동일). 모듈 객체에는 모듈을 초기화하는 데 사용되는 코드 객체가 포함되어 있지 않습니다(초기화가 완료되면 필요하지 않으므로).
- 어트리뷰트 대입은 모듈의 이름 공간 딕셔너리를 갱신합니다. 예를 들어, `m.x = 1` 은 `m.__dict__["x"] = 1` 과 같습니다.

미리 정의된(쓰기 가능한) 속성:

> [`__name__`](https://docs.python.org/ko/3.12/reference/import.html#name__ "__name__")
> 
> 모듈의 이름입니다.
> 
> `__doc__`
> 
> 모듈의 문서 문자열, 사용할 수 없는 경우 `없음`입니다.
> 
> [`__file__`](https://docs.python.org/ko/3.12/reference/import.html#file__ “__file__”)
> 
> 모듈이 파일에서 로드된 경우 모듈이 로드된 파일의 경로명입니다. 인터프리터에 정적으로 링크된 C 모듈과 같은 특정 유형의 모듈의 경우 [`__file__`](https://docs.python.org/ko/3.12/reference/import.html#file__ “__file__”) 속성이 누락될 수 있습니다. 공유 라이브러리에서 동적으로 로드된 확장 모듈의 경우 공유 라이브러리 파일의 경로 이름입니다.
> 
> `__annotations__`
> 
> 모듈 본문 실행 중에 수집된 [변수 어노테이션](https://docs.python.org/ko/3.12/glossary.html#term-variable-annotation)이 포함된 사전입니다. 어노테이션 작업 모범 사례에 대한 자세한 내용은 [어노테이션 모범 사례](https://docs.python.org/ko/3.12/howto/annotations.html#annotations-howto)를 참조하세요.

특수 읽기 전용 어트리뷰트들: [`__dict__`](https://docs.python.org/ko/3.12/library/stdtypes.html#object.__dict__ "object.__dict__") 는 딕셔너리로 표현되는 모듈의 이름 공간입니다.

> **CPython 구현 상세:** CPython 이 모듈 딕셔너리를 비우는 방법 때문에, 딕셔너리에 대한 참조가 남아있더라도, 모듈이 스코프를 벗어나면 모듈 딕셔너리는 비워집니다. 이것을 피하려면, 딕셔너리를 복사하거나 딕셔너리를 직접 이용하는 동안은 모듈을 잡아두어야 합니다.

### 사용자 정의 클래스(Custom classes)

- 사용자 정의 클래스 유형은 일반적으로 클래스 정의에 의해 생성됩니다([클래스 정의](https://docs.python.org/ko/3.12/reference/compound_stmts.html#class) 섹션 참조). 클래스에는 사전 객체로 구현된 네임스페이스가 있습니다. 클래스 속성 참조는 이 사전에서 조회로 변환됩니다(예: `C.x`는 `C.__dict__[“x”]`로 변환됨)(속성을 찾는 다른 수단을 허용하는 여러 훅이 있음). 거기에서 속성 이름을 찾을 수 없으면 기본 클래스에서 속성 검색이 계속됩니다. 이 베이스 클래스 검색은 공통 조상으로 되돌아가는 상속 경로가 여러 개 있는 '다이아몬드' 상속 구조가 있는 경우에도 올바르게 작동하는 C3 메서드 해결 순서를 사용합니다. 파이썬에서 사용하는 C3 MRO에 대한 자세한 내용은 [파이썬 2.3 메서드 분해 순서](https://docs.python.org/ko/3.12/howto/mro.html#python-2-3-mro)에서 확인할 수 있습니다.
- 클래스 어트리뷰트 참조(예: `C` 클래스의 경우)가 클래스 메서드 객체를 산출하는 경우, 이는 [`__self__`](https://docs.python.org/ko/3.12/reference/datamodel.html#method.__self__ “method.__self__”) 어트리뷰트가 `C`인 인스턴스 메서드 객체로 변환됩니다. [`staticmethod`](https://docs.python.org/ko/3.12/library/functions.html#staticmethod “staticmethod”) 객체를 반환하는 경우, 정적 메소드 객체로 래핑된 객체로 변환됩니다. 클래스에서 검색된 속성이 실제로 [`__dict__`](https://docs.python.org/ko/3.12/library/stdtypes.html#object.__dict__ “object.__dict__”)에 포함된 속성과 다를 수 있는 다른 방법은 [디스크립터 구현하기](https://docs.python.org/ko/3.12/reference/datamodel.html#descriptors) 섹션을 참조하세요.

- 클래스 어트리뷰트 대입은 클래스의 딕셔너리를 갱신할 뿐, 어떤 경우도 부모 클래스의 딕셔너리를 건드리지는 않습니다.
- 클래스 객체는 클래스 인스턴스를 돌려주도록(아래를 보십시오) 호출될 수 있습니다(위를 보십시오).
- 특수 어트리뷰트들(Special attributes):

> [`__name__`](https://docs.python.org/ko/3.12/library/stdtypes.html#definition.__name__ "definition.__name__")
> 
> 클래스 이름입니다.
> 
> `__module__`
> 
> 클래스가 정의된 모듈의 이름입니다.
> 
> [`__dict__`](https://docs.python.org/ko/3.12/library/stdtypes.html#object.__dict__ “object.__dict__”)
> 
> 클래스의 네임스페이스가 포함된 딕셔너리입니다.
> 
> [`__bases__`](https://docs.python.org/ko/3.12/library/stdtypes.html#class.__bases__ “class.__bases__”)
> 
> 베이스 클래스 목록에서 발생한 순서대로 베이스 클래스를 포함하는 튜플입니다.
> 
> `__doc__`
> 
> 클래스의 설명서 문자열, 정의되지 않은 경우 `None`입니다.
> 
> `__annotations__`
> 
> 클래스 본문 실행 중에 수집된 [변수 어노테이션](https://docs.python.org/ko/3.12/glossary.html#term-variable-annotation)이 포함된 딕셔너리. 변수 어노테이션을 사용하는 모범 사례는 [어노테이션 모범 사례](https://docs.python.org/ko/3.12/howto/annotations.html#annotations-howto)를 참조하세요.
> 
> `__type_params__`
> 
> [제네릭 클래스](https://docs.python.org/ko/3.12/reference/compound_stmts.html#generic-classes)의 [타입 파라미터](https://docs.python.org/ko/3.12/reference/compound_stmts.html#type-params)를 포함하는 튜플입니다.

### 클래스 인스턴스(Class instances)

- 클래스 인스턴스는 클래스 객체를 호출하여 생성됩니다(위 참조). 클래스 인스턴스에는 어트리뷰트 참조가 검색되는 첫 번째 장소인 사전으로 구현된 네임스페이스가 있습니다. 여기서 속성을 찾지 못했지만 인스턴스의 클래스에 해당 이름의 속성이 있는 경우 클래스 속성으로 검색을 계속합니다. 사용자 정의 함수 객체인 클래스 속성이 발견되면 [`__self__`](https://docs.python.org/ko/3.12/reference/datamodel.html#method.__self__ “method.__self__”) 속성이 인스턴스인 인스턴스 메서드 객체로 변환됩니다. 정적 메서드 및 클래스 메서드 객체도 변환됩니다(위의 “클래스” 아래 참조). 인스턴스를 통해 검색된 클래스의 속성이 클래스의 [`__dict__`](https://docs.python.org/ko/3.12/library/stdtypes.html#object.__dict__ “object.__dict__”)에 실제로 저장된 객체와 다를 수 있는 다른 방법에 대해서는 [디스크립터 구현하기](https://docs.python.org/ko/3.12/reference/datamodel.html#descriptors) 섹션을 참조하세요. 클래스 속성을 찾을 수 없고 객체의 클래스에 [`__getattr__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getattr__ “object.__getattr__”) 메서드가 있는 경우 조회를 충족하기 위해 이 메서드가 호출됩니다.
- 어트리뷰트 할당 및 삭제는 인스턴스의 사전만 업데이트하고 클래스의 사전은 업데이트하지 않습니다. 클래스에 [`__setattr__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__setattr__ “object.__setattr__”) 또는 [`__delattr__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__delattr__ “object.__delattr__”) 메서드가 있는 경우 인스턴스 사전을 직접 업데이트하는 대신 이 메서드가 호출됩니다.

어떤 특별한 이름들의 메서드들을 가지면, 클래스 인스턴스는 숫자, 시퀀스, 매핑인 척할 수 있습니다. [특수 메서드 이름들](https://docs.python.org/ko/3.12/reference/datamodel.html#specialnames) 섹션을 보십시오.

특수 어트리뷰트들: [`__dict__`](https://docs.python.org/ko/3.12/library/stdtypes.html#object.__dict__ "object.__dict__") 는 어트리뷰트 딕셔너리입니다; [`__class__`](https://docs.python.org/ko/3.12/library/stdtypes.html#instance.__class__ "instance.__class__") 는 인스턴스의 클래스입니다.

### I/O 객체 (파일 객체라고도 알려져 있습니다)

- [파일 객체](https://docs.python.org/ko/3.12/glossary.html#term-file-object) 는 열린 파일을 나타냅니다. 파일 객체를 만드는 여러 가지 단축법이 있습니다: [`open()`](https://docs.python.org/ko/3.12/library/functions.html#open "open") 내장 함수, [`os.popen()`](https://docs.python.org/ko/3.12/library/os.html#os.popen "os.popen"), [`os.fdopen()`](https://docs.python.org/ko/3.12/library/os.html#os.fdopen "os.fdopen") 과 소켓 객체의 [`makefile()`](https://docs.python.org/ko/3.12/library/socket.html#socket.socket.makefile "socket.socket.makefile") 메서드 (그리고, 아마도 확장 모듈들이 제공하는 다른 함수들이나 메서드들).
- `sys.stdin`, `sys.stdout`, `sys.stderr` 는 인터프리터의 표준 입력, 출력, 에러 스트림으로 초기화된 파일 객체들입니다; 모두 텍스트 모드로 열려서 [`io.TextIOBase`](https://docs.python.org/ko/3.12/library/io.html#io.TextIOBase "io.TextIOBase") 추상 클래스에 의해 정의된 인터페이스를 따릅니다.

### 내부 형(Internal types)

- 인터프리터가 내부적으로 사용하는 몇몇 형들은 사용자에게 노출됩니다. 인터프리터의 미래 버전에서 이들의 정의는 변경될 수 있지만, 완전함을 위해 여기서 언급합니다.

#### 코드 객체(Code objects)

- 코드 객체는 _바이트로 컴파일된(byte-compiled)_ 실행 가능한 파이썬 코드를 나타내는데, 그냥 [바이트 코드](https://docs.python.org/ko/3.12/glossary.html#term-bytecode) 라고도 부릅니다. 코드 객체와 함수 객체 간에는 차이가 있습니다; 함수 객체는 함수의 전역 공간(globals) (함수가 정의된 모듈)을 명시적으로 참조하고 있지만, 코드 객체는 어떤 문맥(context)도 갖고 있지 않습니다; 또한 기본 인자값들이 함수 객체에 저장되어 있지만 코드 객체에는 들어있지 않습니다 (실행 시간에 계산되는 값들을 나타내기 때문입니다). 함수 객체와는 달리, 코드 객체는 불변이고 가변 객체들에 대한 어떤 참조도 (직접 혹은 간접적으로도) 갖고 있지 않습니다.

##### 특수 읽기 전용 속성 (Special read-only attributes)

|   |   |
|---|---|
|codeobject.co_name[](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_name "Link to this definition")|The function name|
|codeobject.co_qualname[](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_qualname "Link to this definition")|The fully qualified function name<br><br>Added in version 3.11.|
|codeobject.co_argcount[](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_argcount "Link to this definition")|The total number of positional [parameters](https://docs.python.org/ko/3.12/glossary.html#term-parameter) (including positional-only parameters and parameters with default values) that the function has|
|codeobject.co_posonlyargcount[](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_posonlyargcount "Link to this definition")|The number of positional-only [parameters](https://docs.python.org/ko/3.12/glossary.html#term-parameter) (including arguments with default values) that the function has|
|codeobject.co_kwonlyargcount[](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_kwonlyargcount "Link to this definition")|The number of keyword-only [parameters](https://docs.python.org/ko/3.12/glossary.html#term-parameter) (including arguments with default values) that the function has|
|codeobject.co_nlocals[](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_nlocals "Link to this definition")|The number of [local variables](https://docs.python.org/ko/3.12/reference/executionmodel.html#naming) used by the function (including parameters)|
|codeobject.co_varnames[](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_varnames "Link to this definition")|A [`tuple`](https://docs.python.org/ko/3.12/library/stdtypes.html#tuple "tuple") containing the names of the local variables in the function (starting with the parameter names)|
|codeobject.co_cellvars[](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_cellvars "Link to this definition")|A [`tuple`](https://docs.python.org/ko/3.12/library/stdtypes.html#tuple "tuple") containing the names of [local variables](https://docs.python.org/ko/3.12/reference/executionmodel.html#naming) that are referenced by nested functions inside the function|
|codeobject.co_freevars[](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_freevars "Link to this definition")|A [`tuple`](https://docs.python.org/ko/3.12/library/stdtypes.html#tuple "tuple") containing the names of free variables in the function|
|codeobject.co_code[](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_code "Link to this definition")|A string representing the sequence of [bytecode](https://docs.python.org/ko/3.12/glossary.html#term-bytecode) instructions in the function|
|codeobject.co_consts[](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_consts "Link to this definition")|A [`tuple`](https://docs.python.org/ko/3.12/library/stdtypes.html#tuple "tuple") containing the literals used by the [bytecode](https://docs.python.org/ko/3.12/glossary.html#term-bytecode) in the function|
|codeobject.co_names[](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_names "Link to this definition")|A [`tuple`](https://docs.python.org/ko/3.12/library/stdtypes.html#tuple "tuple") containing the names used by the [bytecode](https://docs.python.org/ko/3.12/glossary.html#term-bytecode) in the function|
|codeobject.co_filename[](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_filename "Link to this definition")|The name of the file from which the code was compiled|
|codeobject.co_firstlineno[](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_firstlineno "Link to this definition")|The line number of the first line of the function|
|codeobject.co_lnotab[](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_lnotab "Link to this definition")|A string encoding the mapping from [bytecode](https://docs.python.org/ko/3.12/glossary.html#term-bytecode) offsets to line numbers. For details, see the source code of the interpreter.<br><br>버전 3.12부터 폐지됨: This attribute of code objects is deprecated, and may be removed in Python 3.14.|
|codeobject.co_stacksize[](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_stacksize "Link to this definition")|The required stack size of the code object|
|codeobject.co_flags[](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_flags "Link to this definition")|An [`integer`](https://docs.python.org/ko/3.12/library/functions.html#int "int") encoding a number of flags for the interpreter.|

The following flag bits are defined for [`co_flags`](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_flags "codeobject.co_flags"): bit `0x04` is set if the function uses the `*arguments` syntax to accept an arbitrary number of positional arguments; bit `0x08` is set if the function uses the `**keywords` syntax to accept arbitrary keyword arguments; bit `0x20` is set if the function is a generator. See [코드 객체 비트 플래그](https://docs.python.org/ko/3.12/library/inspect.html#inspect-module-co-flags) for details on the semantics of each flags that might be present.

Future feature declarations (`from __future__ import division`) also use bits in [`co_flags`](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_flags "codeobject.co_flags") to indicate whether a code object was compiled with a particular feature enabled: bit `0x2000` is set if the function was compiled with future division enabled; bits `0x10` and `0x1000` were used in earlier versions of Python.

Other bits in [`co_flags`](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_flags "codeobject.co_flags") are reserved for internal use.

If a code object represents a function, the first item in [`co_consts`](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_consts "codeobject.co_consts") is the documentation string of the function, or `None` if undefined.

##### 3.2.13.1.2. Methods on code objects[](https://docs.python.org/ko/3.12/reference/datamodel.html#methods-on-code-objects "Link to this heading")

codeobject.co_positions()[](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_positions "Link to this definition")

Returns an iterable over the source code positions of each [bytecode](https://docs.python.org/ko/3.12/glossary.html#term-bytecode) instruction in the code object.

The iterator returns [`tuple`](https://docs.python.org/ko/3.12/library/stdtypes.html#tuple "tuple")s containing the `(start_line, end_line, start_column, end_column)`. The _i-th_ tuple corresponds to the position of the source code that compiled to the _i-th_ code unit. Column information is 0-indexed utf-8 byte offsets on the given source line.

This positional information can be missing. A non-exhaustive lists of cases where this may happen:

- Running the interpreter with [`-X`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-X) `no_debug_ranges`.
    
- Loading a pyc file compiled while using [`-X`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-X) `no_debug_ranges`.
    
- Position tuples corresponding to artificial instructions.
    
- Line and column numbers that can’t be represented due to implementation specific limitations.
    

When this occurs, some or all of the tuple elements can be [`None`](https://docs.python.org/ko/3.12/library/constants.html#None "None").

Added in version 3.11.

참고

 

This feature requires storing column positions in code objects which may result in a small increase of disk usage of compiled Python files or interpreter memory usage. To avoid storing the extra information and/or deactivate printing the extra traceback information, the [`-X`](https://docs.python.org/ko/3.12/using/cmdline.html#cmdoption-X) `no_debug_ranges` command line flag or the [`PYTHONNODEBUGRANGES`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONNODEBUGRANGES) environment variable can be used.

codeobject.co_lines()[](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.co_lines "Link to this definition")

Returns an iterator that yields information about successive ranges of [bytecode](https://docs.python.org/ko/3.12/glossary.html#term-bytecode)s. Each item yielded is a `(start, end, lineno)` [`tuple`](https://docs.python.org/ko/3.12/library/stdtypes.html#tuple "tuple"):

- `start` (an [`int`](https://docs.python.org/ko/3.12/library/functions.html#int "int")) represents the offset (inclusive) of the start of the [bytecode](https://docs.python.org/ko/3.12/glossary.html#term-bytecode) range
    
- `end` (an [`int`](https://docs.python.org/ko/3.12/library/functions.html#int "int")) represents the offset (exclusive) of the end of the [bytecode](https://docs.python.org/ko/3.12/glossary.html#term-bytecode) range
    
- `lineno` is an [`int`](https://docs.python.org/ko/3.12/library/functions.html#int "int") representing the line number of the [bytecode](https://docs.python.org/ko/3.12/glossary.html#term-bytecode) range, or `None` if the bytecodes in the given range have no line number
    

The items yielded will have the following properties:

- The first range yielded will have a `start` of 0.
    
- The `(start, end)` ranges will be non-decreasing and consecutive. That is, for any pair of [`tuple`](https://docs.python.org/ko/3.12/library/stdtypes.html#tuple "tuple")s, the `start` of the second will be equal to the `end` of the first.
    
- No range will be backwards: `end >= start` for all triples.
    
- The last [`tuple`](https://docs.python.org/ko/3.12/library/stdtypes.html#tuple "tuple") yielded will have `end` equal to the size of the [bytecode](https://docs.python.org/ko/3.12/glossary.html#term-bytecode).
    

Zero-width ranges, where `start == end`, are allowed. Zero-width ranges are used for lines that are present in the source code, but have been eliminated by the [bytecode](https://docs.python.org/ko/3.12/glossary.html#term-bytecode) compiler.

Added in version 3.10.

더 보기

[**PEP 626**](https://peps.python.org/pep-0626/) - Precise line numbers for debugging and other tools.

The PEP that introduced the `co_lines()` method.

codeobject.replace(_**kwargs_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#codeobject.replace "Link to this definition")

Return a copy of the code object with new values for the specified fields.

Added in version 3.8.

#### 3.2.13.2. 프레임 객체(Frame objects)[](https://docs.python.org/ko/3.12/reference/datamodel.html#frame-objects "Link to this heading")

Frame objects represent execution frames. They may occur in [traceback objects](https://docs.python.org/ko/3.12/reference/datamodel.html#traceback-objects), and are also passed to registered trace functions.

##### 3.2.13.2.1. Special read-only attributes[](https://docs.python.org/ko/3.12/reference/datamodel.html#index-64 "Link to this heading")

|   |   |
|---|---|
|frame.f_back[](https://docs.python.org/ko/3.12/reference/datamodel.html#frame.f_back "Link to this definition")|Points to the previous stack frame (towards the caller), or `None` if this is the bottom stack frame|
|frame.f_code[](https://docs.python.org/ko/3.12/reference/datamodel.html#frame.f_code "Link to this definition")|The [code object](https://docs.python.org/ko/3.12/reference/datamodel.html#code-objects) being executed in this frame. Accessing this attribute raises an [auditing event](https://docs.python.org/ko/3.12/library/sys.html#auditing) `object.__getattr__` with arguments `obj` and `"f_code"`.|
|frame.f_locals[](https://docs.python.org/ko/3.12/reference/datamodel.html#frame.f_locals "Link to this definition")|The dictionary used by the frame to look up [local variables](https://docs.python.org/ko/3.12/reference/executionmodel.html#naming)|
|frame.f_globals[](https://docs.python.org/ko/3.12/reference/datamodel.html#frame.f_globals "Link to this definition")|The dictionary used by the frame to look up [global variables](https://docs.python.org/ko/3.12/reference/executionmodel.html#naming)|
|frame.f_builtins[](https://docs.python.org/ko/3.12/reference/datamodel.html#frame.f_builtins "Link to this definition")|The dictionary used by the frame to look up [built-in (intrinsic) names](https://docs.python.org/ko/3.12/reference/executionmodel.html#naming)|
|frame.f_lasti[](https://docs.python.org/ko/3.12/reference/datamodel.html#frame.f_lasti "Link to this definition")|The “precise instruction” of the frame object (this is an index into the [bytecode](https://docs.python.org/ko/3.12/glossary.html#term-bytecode) string of the [code object](https://docs.python.org/ko/3.12/reference/datamodel.html#code-objects))|

##### 3.2.13.2.2. Special writable attributes[](https://docs.python.org/ko/3.12/reference/datamodel.html#index-65 "Link to this heading")

|   |   |
|---|---|
|frame.f_trace[](https://docs.python.org/ko/3.12/reference/datamodel.html#frame.f_trace "Link to this definition")|If not `None`, this is a function called for various events during code execution (this is used by debuggers). Normally an event is triggered for each new source line (see [`f_trace_lines`](https://docs.python.org/ko/3.12/reference/datamodel.html#frame.f_trace_lines "frame.f_trace_lines")).|
|frame.f_trace_lines[](https://docs.python.org/ko/3.12/reference/datamodel.html#frame.f_trace_lines "Link to this definition")|Set this attribute to [`False`](https://docs.python.org/ko/3.12/library/constants.html#False "False") to disable triggering a tracing event for each source line.|
|frame.f_trace_opcodes[](https://docs.python.org/ko/3.12/reference/datamodel.html#frame.f_trace_opcodes "Link to this definition")|Set this attribute to [`True`](https://docs.python.org/ko/3.12/library/constants.html#True "True") to allow per-opcode events to be requested. Note that this may lead to undefined interpreter behaviour if exceptions raised by the trace function escape to the function being traced.|
|frame.f_lineno[](https://docs.python.org/ko/3.12/reference/datamodel.html#frame.f_lineno "Link to this definition")|The current line number of the frame – writing to this from within a trace function jumps to the given line (only for the bottom-most frame). A debugger can implement a Jump command (aka Set Next Statement) by writing to this attribute.|

##### 3.2.13.2.3. Frame object methods[](https://docs.python.org/ko/3.12/reference/datamodel.html#frame-object-methods "Link to this heading")

프레임 객체는 한가지 메서드를 지원합니다:

frame.clear()[](https://docs.python.org/ko/3.12/reference/datamodel.html#frame.clear "Link to this definition")

This method clears all references to [local variables](https://docs.python.org/ko/3.12/reference/executionmodel.html#naming) held by the frame. Also, if the frame belonged to a [generator](https://docs.python.org/ko/3.12/glossary.html#term-generator), the generator is finalized. This helps break reference cycles involving frame objects (for example when catching an [exception](https://docs.python.org/ko/3.12/library/exceptions.html#bltin-exceptions) and storing its [traceback](https://docs.python.org/ko/3.12/reference/datamodel.html#traceback-objects) for later use).

만약 프레임이 현재 실행 중이면 [`RuntimeError`](https://docs.python.org/ko/3.12/library/exceptions.html#RuntimeError "RuntimeError") 예외가 발생합니다.

Added in version 3.4.

#### 3.2.13.3. 트레이스백 객체(Traceback objects)[](https://docs.python.org/ko/3.12/reference/datamodel.html#traceback-objects "Link to this heading")

Traceback objects represent the stack trace of an [exception](https://docs.python.org/ko/3.12/tutorial/errors.html#tut-errors). A traceback object is implicitly created when an exception occurs, and may also be explicitly created by calling [`types.TracebackType`](https://docs.python.org/ko/3.12/library/types.html#types.TracebackType "types.TracebackType").

버전 3.7에서 변경: Traceback objects can now be explicitly instantiated from Python code.

For implicitly created tracebacks, when the search for an exception handler unwinds the execution stack, at each unwound level a traceback object is inserted in front of the current traceback. When an exception handler is entered, the stack trace is made available to the program. (See section [try 문](https://docs.python.org/ko/3.12/reference/compound_stmts.html#try).) It is accessible as the third item of the tuple returned by [`sys.exc_info()`](https://docs.python.org/ko/3.12/library/sys.html#sys.exc_info "sys.exc_info"), and as the [`__traceback__`](https://docs.python.org/ko/3.12/library/exceptions.html#BaseException.__traceback__ "BaseException.__traceback__") attribute of the caught exception.

When the program contains no suitable handler, the stack trace is written (nicely formatted) to the standard error stream; if the interpreter is interactive, it is also made available to the user as [`sys.last_traceback`](https://docs.python.org/ko/3.12/library/sys.html#sys.last_traceback "sys.last_traceback").

For explicitly created tracebacks, it is up to the creator of the traceback to determine how the [`tb_next`](https://docs.python.org/ko/3.12/reference/datamodel.html#traceback.tb_next "traceback.tb_next") attributes should be linked to form a full stack trace.

Special read-only attributes:

|   |   |
|---|---|
|traceback.tb_frame[](https://docs.python.org/ko/3.12/reference/datamodel.html#traceback.tb_frame "Link to this definition")|Points to the execution [frame](https://docs.python.org/ko/3.12/reference/datamodel.html#frame-objects) of the current level.<br><br>Accessing this attribute raises an [auditing event](https://docs.python.org/ko/3.12/library/sys.html#auditing) `object.__getattr__` with arguments `obj` and `"tb_frame"`.|
|traceback.tb_lineno[](https://docs.python.org/ko/3.12/reference/datamodel.html#traceback.tb_lineno "Link to this definition")|Gives the line number where the exception occurred|
|traceback.tb_lasti[](https://docs.python.org/ko/3.12/reference/datamodel.html#traceback.tb_lasti "Link to this definition")|Indicates the “precise instruction”.|

The line number and last instruction in the traceback may differ from the line number of its [frame object](https://docs.python.org/ko/3.12/reference/datamodel.html#frame-objects) if the exception occurred in a [`try`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#try) statement with no matching except clause or with a [`finally`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#finally) clause.

traceback.tb_next[](https://docs.python.org/ko/3.12/reference/datamodel.html#traceback.tb_next "Link to this definition")

The special writable attribute `tb_next` is the next level in the stack trace (towards the frame where the exception occurred), or `None` if there is no next level.

버전 3.7에서 변경: This attribute is now writable

#### 3.2.13.4. 슬라이스 객체(Slice objects)[](https://docs.python.org/ko/3.12/reference/datamodel.html#slice-objects "Link to this heading")

Slice objects are used to represent slices for [`__getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getitem__ "object.__getitem__") methods. They are also created by the built-in [`slice()`](https://docs.python.org/ko/3.12/library/functions.html#slice "slice") function.

특수 읽기 전용 어트리뷰트들: [`start`](https://docs.python.org/ko/3.12/library/functions.html#slice.start "slice.start") 는 하한(lower bound) 입니다; [`stop`](https://docs.python.org/ko/3.12/library/functions.html#slice.stop "slice.stop") 은 상한(upper bound) 입니다; [`step`](https://docs.python.org/ko/3.12/library/functions.html#slice.step "slice.step") 은 스텝 값입니다; 각 값은 생략될 경우 `None` 입니다. 이 어트리뷰트들은 임의의 형이 될 수 있습니다.

슬라이스 객체는 하나의 메서드를 지원합니다.

slice.indices(_self_, _length_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#slice.indices "Link to this definition")

이 메서드는 하나의 정수 인자 _length_ 를 받아서 슬라이스 객체가 길이 _length_ 인 시퀀스에 적용되었을 때 그 슬라이스에 대한 정보를 계산합니다. 세 개의 정수로 구성된 튜플을 돌려줍니다: 이것들은 각각 _start_ 와 _stop_ 인덱스와, _step_ 또는 슬라이스의 스트라이드(stride) 길이입니다. 생략되었거나 범위를 벗어난 인덱스들은 일반적인 슬라이스와 같은 방법으로 다뤄집니다.

#### 3.2.13.5. 스태틱 메서드 객체(Static method objects)[](https://docs.python.org/ko/3.12/reference/datamodel.html#static-method-objects "Link to this heading")

Static method objects provide a way of defeating the transformation of function objects to method objects described above. A static method object is a wrapper around any other object, usually a user-defined method object. When a static method object is retrieved from a class or a class instance, the object actually returned is the wrapped object, which is not subject to any further transformation. Static method objects are also callable. Static method objects are created by the built-in [`staticmethod()`](https://docs.python.org/ko/3.12/library/functions.html#staticmethod "staticmethod") constructor.

#### 3.2.13.6. 클래스 메서드 객체(Class method objects)[](https://docs.python.org/ko/3.12/reference/datamodel.html#class-method-objects "Link to this heading")

A class method object, like a static method object, is a wrapper around another object that alters the way in which that object is retrieved from classes and class instances. The behaviour of class method objects upon such retrieval is described above, under [“instance methods”](https://docs.python.org/ko/3.12/reference/datamodel.html#instance-methods). Class method objects are created by the built-in [`classmethod()`](https://docs.python.org/ko/3.12/library/functions.html#classmethod "classmethod") constructor.

## 3.3. 특수 메서드 이름들[](https://docs.python.org/ko/3.12/reference/datamodel.html#special-method-names "Link to this heading")

A class can implement certain operations that are invoked by special syntax (such as arithmetic operations or subscripting and slicing) by defining methods with special names. This is Python’s approach to _operator overloading_, allowing classes to define their own behavior with respect to language operators. For instance, if a class defines a method named [`__getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getitem__ "object.__getitem__"), and `x` is an instance of this class, then `x[i]` is roughly equivalent to `type(x).__getitem__(x, i)`. Except where mentioned, attempts to execute an operation raise an exception when no appropriate method is defined (typically [`AttributeError`](https://docs.python.org/ko/3.12/library/exceptions.html#AttributeError "AttributeError") or [`TypeError`](https://docs.python.org/ko/3.12/library/exceptions.html#TypeError "TypeError")).

Setting a special method to `None` indicates that the corresponding operation is not available. For example, if a class sets [`__iter__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__iter__ "object.__iter__") to `None`, the class is not iterable, so calling [`iter()`](https://docs.python.org/ko/3.12/library/functions.html#iter "iter") on its instances will raise a [`TypeError`](https://docs.python.org/ko/3.12/library/exceptions.html#TypeError "TypeError") (without falling back to [`__getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getitem__ "object.__getitem__")). [[2]](https://docs.python.org/ko/3.12/reference/datamodel.html#id18)

내장형을 흉내 내는 클래스를 구현할 때, 모방은 모형화하는 객체에 말이 되는 수준까지만 구현하는 것이 중요합니다. 예를 들어, 어떤 시퀀스는 개별 항목들을 꺼내는 것만으로도 잘 동작할 수 있습니다. 하지만 슬라이스를 꺼내는 것은 말이 안 될 수 있습니다. (이런 한가지 예는 W3C의 Document Object Model의 `NodeList` 인터페이스입니다.)

### 3.3.1. 기본적인 커스터마이제이션[](https://docs.python.org/ko/3.12/reference/datamodel.html#basic-customization "Link to this heading")

object.__new__(_cls_[, _..._])[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__new__ "Link to this definition")

클래스 _cls_ 의 새 인스턴스를 만들기 위해 호출됩니다. [`__new__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__new__ "object.__new__") 는 스태틱 메서드입니다 (그렇게 선언하지 않아도 되는 특별한 경우입니다)인데, 첫 번째 인자로 만들려고 하는 인스턴스의 클래스가 전달됩니다. 나머지 인자들은 객체 생성자 표현(클래스 호출)에 전달된 것들입니다. [`__new__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__new__ "object.__new__") 의 반환 값은 새 객체 인스턴스이어야 합니다 (보통 _cls_ 의 인스턴스).

Typical implementations create a new instance of the class by invoking the superclass’s [`__new__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__new__ "object.__new__") method using `super().__new__(cls[, ...])` with appropriate arguments and then modifying the newly created instance as necessary before returning it.

If [`__new__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__new__ "object.__new__") is invoked during object construction and it returns an instance of _cls_, then the new instance’s [`__init__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__init__ "object.__init__") method will be invoked like `__init__(self[, ...])`, where _self_ is the new instance and the remaining arguments are the same as were passed to the object constructor.

만약 [`__new__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__new__ "object.__new__") 가 _cls_ 의 인스턴스를 돌려주지 않으면, 새 인스턴스의 [`__init__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__init__ "object.__init__") 는 호출되지 않습니다.

[`__new__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__new__ "object.__new__") 는 주로 불변형(int, str, tuple과 같은)의 서브 클래스가 인스턴스 생성을 커스터마이즈할 수 있도록 하는 데 사용됩니다. 또한, 사용자 정의 메타 클래스에서 클래스 생성을 커스터마이즈하기 위해 자주 사용됩니다.

object.__init__(_self_[, _..._])[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__init__ "Link to this definition")

([`__new__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__new__ "object.__new__") 에 의해) 인스턴스가 만들어진 후에, 하지만 호출자에게 돌려주기 전에 호출됩니다. 인자들은 클래스 생성자 표현으로 전달된 것들입니다. 만약 베이스 클래스가 [`__init__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__init__ "object.__init__") 메서드를 갖고 있다면, 서브 클래스의 [`__init__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__init__ "object.__init__") 메서드는, 있다면, 인스턴스에서 베이스 클래스가 차지하는 부분이 올바르게 초기화됨을 확실히 하기 위해 명시적으로 호출해주어야 합니다; 예를 들어: `super().__init__([args...])`.

객체를 만드는데 [`__new__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__new__ "object.__new__") 와 [`__init__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__init__ "object.__init__") 가 협력하고 있으므로 ([`__new__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__new__ "object.__new__") 는 만들고, [`__init__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__init__ "object.__init__") 는 그것을 커스터마이즈합니다), [`__init__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__init__ "object.__init__") 가 `None` 이외의 값을 돌려주면 실행시간에 [`TypeError`](https://docs.python.org/ko/3.12/library/exceptions.html#TypeError "TypeError") 를 일으킵니다.

object.__del__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__del__ "Link to this definition")

인스턴스가 파괴되기 직전에 호출됩니다. 파이널라이저 또는 (부적절하게) 파괴자라고 불립니다. 만약 베이스 클래스가 [`__del__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__del__ "object.__del__") 메서드를 갖고 있다면, 자식 클래스의 [`__del__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__del__ "object.__del__") 메서드는, 정의되어 있다면, 인스턴스에서 베이스 클래스가 차지하는 부분을 적절하게 삭제하기 위해, 명시적으로 베이스 클래스의 메서드를 호출해야 합니다.

(권장하지는 않지만!) [`__del__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__del__ "object.__del__") 메서드는 인스턴스에 대한 새로운 참조를 만듦으로써 인스턴스의 파괴를 지연시킬 수 있습니다. 이것을 객체 _부활_ 이라고 부릅니다. 부활한 객체가 파괴될 때 [`__del__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__del__ "object.__del__") 이 두 번째로 호출될지는 구현에 따라 다릅니다; 현재 [CPython](https://docs.python.org/ko/3.12/glossary.html#term-CPython) 구현은 오직 한 번만 호출합니다.

It is not guaranteed that [`__del__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__del__ "object.__del__") methods are called for objects that still exist when the interpreter exits. [`weakref.finalize`](https://docs.python.org/ko/3.12/library/weakref.html#weakref.finalize "weakref.finalize") provides a straightforward way to register a cleanup function to be called when an object is garbage collected.

참고

 

`del x` 는 직접 `x.__del__()` 를 호출하지 않습니다 — 앞에 있는 것은 `x` 의 참조 횟수(reference count)를 하나 감소시키고, 뒤에 있는 것은 `x` 의 참조 횟수가 0 이 될 때 호출됩니다.

**CPython 구현 상세:** It is possible for a reference cycle to prevent the reference count of an object from going to zero. In this case, the cycle will be later detected and deleted by the [cyclic garbage collector](https://docs.python.org/ko/3.12/glossary.html#term-garbage-collection). A common cause of reference cycles is when an exception has been caught in a local variable. The frame’s locals then reference the exception, which references its own traceback, which references the locals of all frames caught in the traceback.

더 보기

 

[`gc`](https://docs.python.org/ko/3.12/library/gc.html#module-gc "gc: Interface to the cycle-detecting garbage collector.") 모듈에 대한 문서.

경고

 

[`__del__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__del__ "object.__del__") 이 호출되는 불안정한 상황 때문에, 이것이 실행 중에 발생시키는 예외는 무시되고, 대신에 `sys.stderr` 로 경고가 출력됩니다. 특히:

- [`__del__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__del__ "object.__del__") 은 (임의의 스레드에서) 임의의 코드가 실행되는 동안 호출될 수 있습니다. [`__del__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__del__ "object.__del__") 이 록을 얻어야 하거나 다른 블로킹 자원을 호출하면, [`__del__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__del__ "object.__del__") 을 실행하기 위해 중단된 코드가 자원을 이미 차지했을 수 있으므로 교착 상태에 빠질 수 있습니다.
    
- [`__del__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__del__ "object.__del__") 은 인터프리터를 종료할 때 실행될 수 있습니다. 결과적으로, 액세스해야 하는 전역 변수(다른 모듈 포함)가 이미 삭제되었거나 `None` 으로 설정되었을 수 있습니다. 파이썬은 이름이 하나의 밑줄로 시작하는 전역 객체가 다른 전역 객체들보다 먼저 삭제됨을 보장합니다; 이것은, 만약 그 전역 객체들에 대한 다른 참조가 존재하지 않는다면, [`__del__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__del__ "object.__del__") 메서드가 호출되는 시점에, 임포트된 모듈들이 남아있도록 확실히 하는 데 도움이 될 수 있습니다.
    

object.__repr__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__repr__ "Link to this definition")

[`repr()`](https://docs.python.org/ko/3.12/library/functions.html#repr "repr") 내장 함수에 의해 호출되어 객체의 “형식적인(official)” 문자열 표현을 계산합니다. 만약 가능하다면, 이것은 같은 (적절한 환경이 주어질 때) 값을 갖는 객체를 새로 만들 수 있는 올바른 파이썬 표현식처럼 보여야 합니다. 가능하지 않다면, `<...쓸모있는 설명...>` 형태의 문자열을 돌려줘야 합니다. 반환 값은 반드시 문자열이어야 합니다. 만약 클래스가 [`__str__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__str__ "object.__str__") 없이 [`__repr__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__repr__ "object.__repr__") 만 정의한다면, [`__repr__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__repr__ "object.__repr__") 은 그 클래스 인스턴스의 “비형식적인(informal)” 문자열 표현이 요구될 때 사용될 수 있습니다.

이것은 디버깅에 사용되기 때문에, 표현이 풍부한 정보를 담고 모호하지 않게 하는 것이 중요합니다.

object.__str__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__str__ "Link to this definition")

[`str(object)`](https://docs.python.org/ko/3.12/library/stdtypes.html#str "str") 와 내장 함수 [`format()`](https://docs.python.org/ko/3.12/library/functions.html#format "format"), [`print()`](https://docs.python.org/ko/3.12/library/functions.html#print "print") 에 의해 호출되어 객체의 “비형식적인(informal)” 또는 보기 좋게 인쇄 가능한 문자열 표현을 계산합니다. 반환 값은 반드시 [문자열](https://docs.python.org/ko/3.12/library/stdtypes.html#textseq) 객체여야 합니다.

이 메서드는 [`__str__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__str__ "object.__str__") 이 올바른 파이썬 표현식을 돌려줄 것이라고 기대되지 않는다는 점에서 [`object.__repr__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__repr__ "object.__repr__") 과 다릅니다: 더 편리하고 간결한 표현이 사용될 수 있습니다.

내장형 [`object`](https://docs.python.org/ko/3.12/library/functions.html#object "object") 에 정의된 기본 구현은 [`object.__repr__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__repr__ "object.__repr__") 을 호출합니다.

object.__bytes__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__bytes__ "Link to this definition")

[bytes](https://docs.python.org/ko/3.12/library/functions.html#func-bytes) 에 의해 호출되어 객체의 바이트열 표현을 계산합니다. 반환 값은 반드시 [`bytes`](https://docs.python.org/ko/3.12/library/stdtypes.html#bytes "bytes") 객체여야 합니다.

object.__format__(_self_, _format_spec_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__format__ "Link to this definition")

[`format()`](https://docs.python.org/ko/3.12/library/functions.html#format "format") 내장 함수, 확대하면, [포맷 문자열 리터럴(formatted string literals)](https://docs.python.org/ko/3.12/reference/lexical_analysis.html#f-strings) 의 계산과 [`str.format()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.format "str.format") 메서드에 의해 호출되어, 객체의 “포맷된” 문자열 표현을 만들어냅니다. _format_spec_ 인자는 요구되는 포맷 옵션들을 포함하는 문자열입니다. _format_spec_ 인자의 해석은 [`__format__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__format__ "object.__format__") 을 구현하는 형에 달려있으나, 대부분 클래스는 포매팅을 내향형들의 하나로 위임하거나, 비슷한 포맷 옵션 문법을 사용합니다.

표준 포매팅 문법에 대해서는 [포맷 명세 미니 언어](https://docs.python.org/ko/3.12/library/string.html#formatspec) 를 참고하면 됩니다.

반환 값은 반드시 문자열이어야 합니다.

버전 3.4에서 변경: `object` 의 __format__ 메서드 자신은, 빈 문자열이 아닌 인자가 전달되면 [`TypeError`](https://docs.python.org/ko/3.12/library/exceptions.html#TypeError "TypeError") 를 발생시킵니다.

버전 3.7에서 변경: 이제 `object.__format__(x, '')` 는 `format(str(x), '')` 가 아니라 `str(x)` 와 동등합니다.

object.__lt__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__lt__ "Link to this definition")

object.__le__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__le__ "Link to this definition")

object.__eq__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__eq__ "Link to this definition")

object.__ne__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__ne__ "Link to this definition")

object.__gt__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__gt__ "Link to this definition")

object.__ge__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__ge__ "Link to this definition")

이것들은 소위 “풍부한 비교(rich comparison)” 메서드입니다. 연산자 기호와 메서드 이름 간의 관계는 다음과 같습니다: `x<y` 는 `x.__lt__(y)` 를 호출합니다, `x<=y` 는 `x.__le__(y)` 를 호출합니다, `x==y` 는 `x.__eq__(y)` 를 호출합니다, `x!=y` 는 `x.__ne__(y)` 를 호출합니다, `x>y` 는 `x.__gt__(y)` 를 호출합니다, `x>=y` 는 `x.__ge__(y)` 를 호출합니다.

A rich comparison method may return the singleton [`NotImplemented`](https://docs.python.org/ko/3.12/library/constants.html#NotImplemented "NotImplemented") if it does not implement the operation for a given pair of arguments. By convention, `False` and `True` are returned for a successful comparison. However, these methods can return any value, so if the comparison operator is used in a Boolean context (e.g., in the condition of an `if` statement), Python will call [`bool()`](https://docs.python.org/ko/3.12/library/functions.html#bool "bool") on the value to determine if the result is true or false.

By default, `object` implements [`__eq__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__eq__ "object.__eq__") by using `is`, returning [`NotImplemented`](https://docs.python.org/ko/3.12/library/constants.html#NotImplemented "NotImplemented") in the case of a false comparison: `True if x is y else NotImplemented`. For [`__ne__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__ne__ "object.__ne__"), by default it delegates to [`__eq__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__eq__ "object.__eq__") and inverts the result unless it is `NotImplemented`. There are no other implied relationships among the comparison operators or default implementations; for example, the truth of `(x<y or x==y)` does not imply `x<=y`. To automatically generate ordering operations from a single root operation, see [`functools.total_ordering()`](https://docs.python.org/ko/3.12/library/functools.html#functools.total_ordering "functools.total_ordering").

사용자 정의 비교 연산자를 지원하고 딕셔너리 키로 사용될 수 있는 [해시 가능](https://docs.python.org/ko/3.12/glossary.html#term-hashable) 객체를 만드는 것에 관한 몇 가지 중요한 내용이 [`__hash__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__hash__ "object.__hash__") 에 관한 문단에 나옵니다.

There are no swapped-argument versions of these methods (to be used when the left argument does not support the operation but the right argument does); rather, [`__lt__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__lt__ "object.__lt__") and [`__gt__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__gt__ "object.__gt__") are each other’s reflection, [`__le__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__le__ "object.__le__") and [`__ge__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__ge__ "object.__ge__") are each other’s reflection, and [`__eq__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__eq__ "object.__eq__") and [`__ne__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__ne__ "object.__ne__") are their own reflection. If the operands are of different types, and the right operand’s type is a direct or indirect subclass of the left operand’s type, the reflected method of the right operand has priority, otherwise the left operand’s method has priority. Virtual subclassing is not considered.

When no appropriate method returns any value other than [`NotImplemented`](https://docs.python.org/ko/3.12/library/constants.html#NotImplemented "NotImplemented"), the `==` and `!=` operators will fall back to `is` and `is not`, respectively.

object.__hash__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__hash__ "Link to this definition")

Called by built-in function [`hash()`](https://docs.python.org/ko/3.12/library/functions.html#hash "hash") and for operations on members of hashed collections including [`set`](https://docs.python.org/ko/3.12/library/stdtypes.html#set "set"), [`frozenset`](https://docs.python.org/ko/3.12/library/stdtypes.html#frozenset "frozenset"), and [`dict`](https://docs.python.org/ko/3.12/library/stdtypes.html#dict "dict"). The `__hash__()` method should return an integer. The only required property is that objects which compare equal have the same hash value; it is advised to mix together the hash values of the components of the object that also play a part in comparison of objects by packing them into a tuple and hashing the tuple. Example:

def __hash__(self):
    return hash((self.name, self.nick, self.color))

참고

 

[`hash()`](https://docs.python.org/ko/3.12/library/functions.html#hash "hash") 는 객체가 정의한 [`__hash__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__hash__ "object.__hash__") 메서드가 돌려주는 값을 [`Py_ssize_t`](https://docs.python.org/ko/3.12/c-api/intro.html#c.Py_ssize_t "Py_ssize_t") 의 크기로 자릅니다(truncate). 이것은 보통 64-bit 빌드에서는 8바이트고, 32-bit 빌드에서는 4바이트입니다. 만약 객체의 [`__hash__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__hash__ "object.__hash__") 가 서로 다른 비트 크기를 갖는 빌드들 사이에서 함께 사용되어야 한다면, 모든 지원할 빌드들에서의 폭을 검사해야 합니다. 이렇게 하는 쉬운 방법은 `python -c "import sys; print(sys.hash_info.width)"` 입니다.

If a class does not define an [`__eq__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__eq__ "object.__eq__") method it should not define a [`__hash__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__hash__ "object.__hash__") operation either; if it defines [`__eq__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__eq__ "object.__eq__") but not [`__hash__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__hash__ "object.__hash__"), its instances will not be usable as items in hashable collections. If a class defines mutable objects and implements an [`__eq__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__eq__ "object.__eq__") method, it should not implement [`__hash__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__hash__ "object.__hash__"), since the implementation of [hashable](https://docs.python.org/ko/3.12/glossary.html#term-hashable) collections requires that a key’s hash value is immutable (if the object’s hash value changes, it will be in the wrong hash bucket).

사용자 정의 클래스는 기본적으로 [`__eq__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__eq__ "object.__eq__") 와 [`__hash__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__hash__ "object.__hash__") 메서드를 갖습니다; 모든 객체는 (자기 자신을 제외하고) 같지 않다고 비교되고, `x.__hash__()` 는 적절한 값을 돌려주어, `x == y` 일 때 `x is y` 와 `hash(x) == hash(y)` 가 동시에 성립할 수 있도록 합니다.

[`__eq__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__eq__ "object.__eq__") 를 재정의하고 [`__hash__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__hash__ "object.__hash__") 를 정의하지 않는 클래스는 [`__hash__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__hash__ "object.__hash__") 가 `None` 으로 설정됩니다. 클래스의 [`__hash__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__hash__ "object.__hash__") 메서드가 `None` 이면, 클래스의 인스턴스는 프로그램이 해시값을 얻으려 시도할 때 [`TypeError`](https://docs.python.org/ko/3.12/library/exceptions.html#TypeError "TypeError") 를 일으키고, `isinstance(obj, collections.abc.Hashable)` 로 검사할 때 해시 가능하지 않다고 올바로 감지됩니다.

만약 [`__eq__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__eq__ "object.__eq__") 를 재정의하는 클래스가 부모 클래스로부터 [`__hash__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__hash__ "object.__hash__") 의 구현을 물려받고 싶으면 인터프리터에게 명시적으로 이렇게 지정해주어야 합니다: `__hash__ = <ParentClass>.__hash__`.

만약 [`__eq__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__eq__ "object.__eq__") 를 재정의하지 않는 클래스가 해시 지원을 멈추고 싶으면, 클래스 정의에 `__hash__ = None` 을 포함해야 합니다. 자신의 [`__hash__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__hash__ "object.__hash__") 을 정의한 후에 직접 [`TypeError`](https://docs.python.org/ko/3.12/library/exceptions.html#TypeError "TypeError") 를 일으키는 경우는 `isinstance(obj, collections.abc.Hashable)` 호출이 해시 가능하다고 잘못 인식합니다.

참고

 

기본적으로, str과 bytes 객체들의 [`__hash__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__hash__ "object.__hash__") 값은 예측할 수 없는 난수값으로 “솔트되어(salted)” 있습니다. 개별 파이썬 프로세스 내에서는 변하지 않는 값으로 유지되지만, 파이썬을 반복적으로 실행할 때는 예측할 수 없게 됩니다.

This is intended to provide protection against a denial-of-service caused by carefully chosen inputs that exploit the worst case performance of a dict insertion, _O_(_n_2) complexity. See [http://ocert.org/advisories/ocert-2011-003.html](http://ocert.org/advisories/ocert-2011-003.html) for details.

해시값의 변경은 집합의 이터레이션 순서에 영향을 줍니다, 파이썬은 이 순서에 대해 어떤 보장도 하지 않습니다 (그리고 보통 32-bit 와 64-bit 빌드 사이에서도 다릅니다).

[`PYTHONHASHSEED`](https://docs.python.org/ko/3.12/using/cmdline.html#envvar-PYTHONHASHSEED) 를 참고하십시오.

버전 3.3에서 변경: 해시 난수 화는 기본적으로 활성화됩니다.

object.__bool__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__bool__ "Link to this definition")

Called to implement truth value testing and the built-in operation `bool()`; should return `False` or `True`. When this method is not defined, [`__len__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__len__ "object.__len__") is called, if it is defined, and the object is considered true if its result is nonzero. If a class defines neither `__len__()` nor `__bool__()`, all its instances are considered true.

### 3.3.2. 어트리뷰트 액세스 커스터마이제이션[](https://docs.python.org/ko/3.12/reference/datamodel.html#customizing-attribute-access "Link to this heading")

클래스 인스턴스의 어트리뷰트 참조(읽기, 대입하기, `x.name` 을 삭제하기)의 의미를 변경하기 위해 다음과 같은 메서드들이 정의될 수 있습니다.

object.__getattr__(_self_, _name_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getattr__ "Link to this definition")

기본 어트리뷰트 액세스가 [`AttributeError`](https://docs.python.org/ko/3.12/library/exceptions.html#AttributeError "AttributeError") 로 실패할 때 호출됩니다 (_name_ 이 인스턴스 어트리뷰트 또는 `self` 의 클래스 트리에 있는 어트리뷰트가 아니라서 [`__getattribute__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getattribute__ "object.__getattribute__") 가 [`AttributeError`](https://docs.python.org/ko/3.12/library/exceptions.html#AttributeError "AttributeError") 를 일으키거나; _name_ 프로퍼티의 [`__get__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__get__ "object.__get__") 이 [`AttributeError`](https://docs.python.org/ko/3.12/library/exceptions.html#AttributeError "AttributeError") 를 일으킬 때). 이 메서드는 (계산된) 어트리뷰트 값을 반환하거나 [`AttributeError`](https://docs.python.org/ko/3.12/library/exceptions.html#AttributeError "AttributeError") 예외를 일으켜야 합니다.

일반적인 메커니즘을 통해 어트리뷰트가 발견되면 [`__getattr__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getattr__ "object.__getattr__") 이 호출되지 않음에 주의해야 합니다 (이것은 [`__getattr__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getattr__ "object.__getattr__") 과 [`__setattr__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__setattr__ "object.__setattr__") 간의 의도된 비대칭입니다). 이렇게 하는 이유는 효율 때문이기도 하고, 그렇게 하지 않으면 [`__getattr__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getattr__ "object.__getattr__") 가 인스턴스의 다른 어트리뷰트에 접근할 방법이 없기 때문이기도 합니다. 적어도 인스턴스 변수의 경우, 어떤 값도 인스턴스 어트리뷰트 딕셔너리에 넣지 않음으로써 (대신에 그것들을 다른 객체에 넣습니다) 완전한 제어인 것처럼 조작할 수 있습니다. 어트리뷰트 액세스를 실제로 완전히 조작하는 방법에 대해서는 아래에 나오는 [`__getattribute__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getattribute__ "object.__getattribute__") 에서 다룹니다.

object.__getattribute__(_self_, _name_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getattribute__ "Link to this definition")

클래스 인스턴스의 어트리뷰트 액세스를 구현하기 위해 조건 없이 호출됩니다. 만약 클래스가 [`__getattr__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getattr__ "object.__getattr__") 도 함께 구현하면, [`__getattribute__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getattribute__ "object.__getattribute__") 가 명시적으로 호출하거나 [`AttributeError`](https://docs.python.org/ko/3.12/library/exceptions.html#AttributeError "AttributeError") 를 일으키지 않는 이상 __getattr__ 는 호출되지 않습니다. 이 메서드는 어트리뷰트의 (계산된) 값을 돌려주거나 [`AttributeError`](https://docs.python.org/ko/3.12/library/exceptions.html#AttributeError "AttributeError") 예외를 일으켜야 합니다. 이 메서드에서 무한 재귀(infinite recursion)가 발생하는 것을 막기 위해, 구현은 언제나 필요한 어트리뷰트에 접근하기 위해 같은 이름의 베이스 클래스의 메서드를 호출해야 합니다. 예를 들어, `object.__getattribute__(self, name)`.

참고

 

This method may still be bypassed when looking up special methods as the result of implicit invocation via language syntax or [built-in functions](https://docs.python.org/ko/3.12/reference/datamodel.html#builtin-functions). See [특수 메서드 조회](https://docs.python.org/ko/3.12/reference/datamodel.html#special-lookup).

특정 민감한 어트리뷰트 액세스의 경우, 인자 `obj`와 `name`으로 [감사 이벤트](https://docs.python.org/ko/3.12/library/sys.html#auditing) `object.__getattr__`을 발생시킵니다.

object.__setattr__(_self_, _name_, _value_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__setattr__ "Link to this definition")

어트리뷰트 대입이 시도될 때 호출됩니다. 일반적인 메커니즘(즉 인스턴스 딕셔너리에 값을 저장하는 것) 대신에 이것이 호출됩니다. _name_ 은 어트리뷰트 이름이고, _value_ 는 그것에 대입하려는 값입니다.

[`__setattr__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__setattr__ "object.__setattr__") 에서 인스턴스 어트리뷰트에 대입하려고 할 때는, 같은 이름의 베이스 클래스의 메서드를 호출해야 합니다. 예를 들어 `object.__setattr__(self, name, value)`

특정 민감한 어트리뷰트 대입의 경우, 인자 `obj`, `name`, `value`로 [감사 이벤트](https://docs.python.org/ko/3.12/library/sys.html#auditing) `object.__setattr__`을 발생시킵니다.

object.__delattr__(_self_, _name_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__delattr__ "Link to this definition")

[`__setattr__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__setattr__ "object.__setattr__") 과 비슷하지만 어트리뷰트를 대입하는 대신에 삭제합니다. 이것은 `del obj.name` 이 객체에 의미가 있는 경우에만 구현되어야 합니다.

특정 민감한 어트리뷰트 삭제의 경우, 인자 `obj`와 `name`으로 [감사 이벤트](https://docs.python.org/ko/3.12/library/sys.html#auditing) `object.__delattr__`을 발생시킵니다.

object.__dir__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__dir__ "Link to this definition")

Called when [`dir()`](https://docs.python.org/ko/3.12/library/functions.html#dir "dir") is called on the object. An iterable must be returned. [`dir()`](https://docs.python.org/ko/3.12/library/functions.html#dir "dir") converts the returned iterable to a list and sorts it.

#### 3.3.2.1. 모듈 어트리뷰트 액세스 커스터마이제이션[](https://docs.python.org/ko/3.12/reference/datamodel.html#customizing-module-attribute-access "Link to this heading")

특수한 이름 `__getattr__` 과 `__dir__` 는 모듈 어트리뷰트에 대한 접근을 사용자 정의하는 데 사용될 수도 있습니다. 모듈 수준의 `__getattr__` 함수는 하나의 인자로 어트리뷰트의 이름을 받아서 계산된 값을 돌려주거나 [`AttributeError`](https://docs.python.org/ko/3.12/library/exceptions.html#AttributeError "AttributeError") 를 발생시켜야 합니다. 일반적인 조회(즉 [`object.__getattribute__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getattribute__ "object.__getattribute__"))를 통해 어트리뷰트가 모듈 객체에서 발견되지 않으면, [`AttributeError`](https://docs.python.org/ko/3.12/library/exceptions.html#AttributeError "AttributeError") 를 일으키기 전에 모듈 `__dict__` 에서 `__getattr__` 을 검색합니다. 발견되면, 어트리뷰트 이름으로 그 함수를 호출하고 결과를 돌려줍니다.

The `__dir__` function should accept no arguments, and return an iterable of strings that represents the names accessible on module. If present, this function overrides the standard [`dir()`](https://docs.python.org/ko/3.12/library/functions.html#dir "dir") search on a module.

모듈 동작(어트리뷰트 설정, 프로퍼티 등)을 보다 세밀하게 사용자 정의하려면, 모듈 객체의 `__class__` 어트리뷰트를 [`types.ModuleType`](https://docs.python.org/ko/3.12/library/types.html#types.ModuleType "types.ModuleType") 의 서브 클래스로 설정할 수 있습니다. 예를 들면:

import sys
from types import ModuleType

class VerboseModule(ModuleType):
    def __repr__(self):
        return f'Verbose {self.__name__}'

    def __setattr__(self, attr, value):
        print(f'Setting {attr}...')
        super().__setattr__(attr, value)

sys.modules[__name__].__class__ = VerboseModule

참고

 

모듈 `__getattr__` 정의와 모듈 `__class__` 설정은 어트리뷰트 액세스 구문을 사용하는 조회에만 영향을 미칩니다 – 모듈 전역에 대한 직접적인 액세스(모듈 내의 코드에 의한 액세스이거나 모듈의 전역 딕셔너리에 대한 참조를 거치거나)는 영향받지 않습니다.

버전 3.5에서 변경: 이제 `__class__` 모듈 어트리뷰트가 쓰기 가능합니다.

Added in version 3.7: `__getattr__` 과 `__dir__` 모듈 어트리뷰트.

더 보기

[**PEP 562**](https://peps.python.org/pep-0562/) - 모듈 __getattr__ 과 __dir__

모듈에 대한 `__getattr__` 과 `__dir__` 함수를 설명합니다.

#### 3.3.2.2. 디스크립터 구현하기[](https://docs.python.org/ko/3.12/reference/datamodel.html#implementing-descriptors "Link to this heading")

다음에 오는 메서드들은 메서드를 가진 클래스(소위 _디스크립터(descriptor)_ 클래스)의 인스턴스가 _소유자(owner)_ 클래스에 등장할 때만 적용됩니다(디스크립터는 소유자 클래스의 딕셔너리나 그 부모 클래스 중 하나의 딕셔너리에 있어야 합니다). 아래의 예에서, “어트리뷰트” 는 이름이 소유자 클래스의 [`__dict__`](https://docs.python.org/ko/3.12/library/stdtypes.html#object.__dict__ "object.__dict__") 의 키로 사용되고 있는 어트리뷰트를 가리킵니다.

object.__get__(_self_, _instance_, _owner=None_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__get__ "Link to this definition")

소유자 클래스(클래스 어트리뷰트 액세스) 나 그 클래스의 인스턴스(인스턴스 어트리뷰트 액세스)의 어트리뷰트를 취하려고 할 때 호출됩니다. 선택적 _owner_ 인자는 소유자 클래스입니다. 반면에 _instance_ 는 어트리뷰트 참조가 일어나고 있는 인스턴스이거나, 어트리뷰트가 _owner_ 를 통해 액세스 되는 경우 None 입니다.

이 메서드는 계산된 어트리뷰트 값을 돌려주거나 [`AttributeError`](https://docs.python.org/ko/3.12/library/exceptions.html#AttributeError "AttributeError") 예외를 일으켜야 합니다.

[**PEP 252**](https://peps.python.org/pep-0252/)는 [`__get__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__get__ "object.__get__")이 하나나 두 개의 인자를 갖는 콜러블이라고 지정합니다. 파이썬 자신의 내장 디스크립터는 이 명세를 지원합니다; 그러나, 일부 제삼자 도구에는 두 인수를 모두 요구하는 디스크립터가 있을 수 있습니다. 파이썬 자신의 [`__getattribute__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getattribute__ "object.__getattribute__") 구현은 필요한지와 관계없이 항상 두 인자를 모두 전달합니다.

object.__set__(_self_, _instance_, _value_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__set__ "Link to this definition")

소유자 클래스의 인스턴스 _instance_ 의 어트리뷰트를 새 값 _value_ 로 설정할 때 호출됩니다.

[`__set__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__set__ "object.__set__")이나 [`__delete__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__delete__ "object.__delete__")를 추가하면 디스크립터 유형이 “데이터 디스크립터(data descriptor)”로 변경됨에 유의하십시오. 자세한 내용은 [디스크립터 호출하기](https://docs.python.org/ko/3.12/reference/datamodel.html#descriptor-invocation)를 참조하십시오.

object.__delete__(_self_, _instance_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__delete__ "Link to this definition")

소유자 클래스의 인스턴스 _instance_ 의 어트리뷰트를 삭제할 때 호출됩니다.

Instances of descriptors may also have the `__objclass__` attribute present:

object.__objclass__[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__objclass__ "Link to this definition")

The attribute `__objclass__` is interpreted by the [`inspect`](https://docs.python.org/ko/3.12/library/inspect.html#module-inspect "inspect: Extract information and source code from live objects.") module as specifying the class where this object was defined (setting this appropriately can assist in runtime introspection of dynamic class attributes). For callables, it may indicate that an instance of the given type (or a subclass) is expected or required as the first positional argument (for example, CPython sets this attribute for unbound methods that are implemented in C).

#### 3.3.2.3. 디스크립터 호출하기[](https://docs.python.org/ko/3.12/reference/datamodel.html#invoking-descriptors "Link to this heading")

In general, a descriptor is an object attribute with “binding behavior”, one whose attribute access has been overridden by methods in the descriptor protocol: [`__get__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__get__ "object.__get__"), [`__set__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__set__ "object.__set__"), and [`__delete__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__delete__ "object.__delete__"). If any of those methods are defined for an object, it is said to be a descriptor.

어트리뷰트 액세스의 기본 동작은 객체의 딕셔너리에서 어트리뷰트를 읽고, 쓰고, 삭제하는 것입니다. 예를 들어 `a.x` 는 `a.__dict__['x']` 에서 시작해서 `type(a).__dict__['x']` 를 거쳐 `type(a)` 의 메타 클래스를 제외한 베이스 클래스들을 거쳐 가는 일련의 조회로 구성됩니다.

그러나, 만약 조회한 값이 디스크립터 메서드를 구현한 객체면, 파이썬은 기본 동작 대신에 디스크립터 메서드를 호출할 수 있습니다. 우선순위 목록의 어느 위치에서 이런 일이 일어나는지는 어떤 디스크립터 메서드가 정의되어 있고 어떤 식으로 호출되는지에 따라 다릅니다.

디스크립터 호출의 시작점은 결합(binding)입니다, `a.x`. 어떻게 인자들이 조합되는지는 `a` 에 따라 다릅니다:

직접 호출

가장 간단하면서도 가장 덜 사용되는 호출은 사용자의 코드가 디스크립터 메서드를 직접 호출할 때입니다: `x.__get__(a)`

인스턴스 결합

객체 인스턴스에 결합하면, `a.x` 는 이런 호출로 변환됩니다: `type(a).__dict__['x'].__get__(a, type(a))`.

클래스 결합

클래스에 결합하면, `A.x` 는 이런 호출로 변환됩니다: `A.__dict__['x'].__get__(None, A)`.

Super 결합

A dotted lookup such as `super(A, a).x` searches `a.__class__.__mro__` for a base class `B` following `A` and then returns `B.__dict__['x'].__get__(a, A)`. If not a descriptor, `x` is returned unchanged.

For instance bindings, the precedence of descriptor invocation depends on which descriptor methods are defined. A descriptor can define any combination of [`__get__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__get__ "object.__get__"), [`__set__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__set__ "object.__set__") and [`__delete__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__delete__ "object.__delete__"). If it does not define `__get__()`, then accessing the attribute will return the descriptor object itself unless there is a value in the object’s instance dictionary. If the descriptor defines `__set__()` and/or `__delete__()`, it is a data descriptor; if it defines neither, it is a non-data descriptor. Normally, data descriptors define both `__get__()` and `__set__()`, while non-data descriptors have just the `__get__()` method. Data descriptors with `__get__()` and `__set__()` (and/or `__delete__()`) defined always override a redefinition in an instance dictionary. In contrast, non-data descriptors can be overridden by instances.

Python methods (including those decorated with [`@staticmethod`](https://docs.python.org/ko/3.12/library/functions.html#staticmethod "staticmethod") and [`@classmethod`](https://docs.python.org/ko/3.12/library/functions.html#classmethod "classmethod")) are implemented as non-data descriptors. Accordingly, instances can redefine and override methods. This allows individual instances to acquire behaviors that differ from other instances of the same class.

[`property()`](https://docs.python.org/ko/3.12/library/functions.html#property "property") 함수는 데이터 디스크립터로 구현됩니다. 이 때문에, 인스턴스는 프로퍼티(property)의 동작을 변경할 수 없습니다.

#### 3.3.2.4. __slots__[](https://docs.python.org/ko/3.12/reference/datamodel.html#slots "Link to this heading")

___slots___ allow us to explicitly declare data members (like properties) and deny the creation of [`__dict__`](https://docs.python.org/ko/3.12/library/stdtypes.html#object.__dict__ "object.__dict__") and ___weakref___ (unless explicitly declared in ___slots___ or available in a parent.)

The space saved over using [`__dict__`](https://docs.python.org/ko/3.12/library/stdtypes.html#object.__dict__ "object.__dict__") can be significant. Attribute lookup speed can be significantly improved as well.

object.__slots__[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__slots__ "Link to this definition")

This class variable can be assigned a string, iterable, or sequence of strings with variable names used by instances. ___slots___ reserves space for the declared variables and prevents the automatic creation of [`__dict__`](https://docs.python.org/ko/3.12/library/stdtypes.html#object.__dict__ "object.__dict__") and ___weakref___ for each instance.

Notes on using ___slots___:

- When inheriting from a class without ___slots___, the [`__dict__`](https://docs.python.org/ko/3.12/library/stdtypes.html#object.__dict__ "object.__dict__") and ___weakref___ attribute of the instances will always be accessible.
    
- Without a [`__dict__`](https://docs.python.org/ko/3.12/library/stdtypes.html#object.__dict__ "object.__dict__") variable, instances cannot be assigned new variables not listed in the ___slots___ definition. Attempts to assign to an unlisted variable name raises [`AttributeError`](https://docs.python.org/ko/3.12/library/exceptions.html#AttributeError "AttributeError"). If dynamic assignment of new variables is desired, then add `'__dict__'` to the sequence of strings in the ___slots___ declaration.
    
- Without a ___weakref___ variable for each instance, classes defining ___slots___ do not support [`weak references`](https://docs.python.org/ko/3.12/library/weakref.html#module-weakref "weakref: Support for weak references and weak dictionaries.") to its instances. If weak reference support is needed, then add `'__weakref__'` to the sequence of strings in the ___slots___ declaration.
    
- ___slots___ are implemented at the class level by creating [descriptors](https://docs.python.org/ko/3.12/reference/datamodel.html#descriptors) for each variable name. As a result, class attributes cannot be used to set default values for instance variables defined by ___slots___; otherwise, the class attribute would overwrite the descriptor assignment.
    
- The action of a ___slots___ declaration is not limited to the class where it is defined. ___slots___ declared in parents are available in child classes. However, child subclasses will get a [`__dict__`](https://docs.python.org/ko/3.12/library/stdtypes.html#object.__dict__ "object.__dict__") and ___weakref___ unless they also define ___slots___ (which should only contain names of any _additional_ slots).
    
- 클래스가 베이스 클래스의 ___slots___ 에 정의된 이름과 같은 이름의 변수를 ___slots___ 에 선언한다면, 베이스 클래스가 정의한 변수는 액세스할 수 없는 상태가 됩니다(베이스 클래스로부터 디스크립터를 직접 조회하는 경우는 예외다). 이것은 프로그램을 정의되지 않은 상태로 보내게 됩니다. 미래에는, 이를 방지하기 위한 검사가 추가될 것입니다.
    
- [`TypeError`](https://docs.python.org/ko/3.12/library/exceptions.html#TypeError "TypeError") will be raised if nonempty ___slots___ are defined for a class derived from a [`"variable-length" built-in type`](https://docs.python.org/ko/3.12/c-api/typeobj.html#c.PyTypeObject.tp_itemsize "PyTypeObject.tp_itemsize") such as [`int`](https://docs.python.org/ko/3.12/library/functions.html#int "int"), [`bytes`](https://docs.python.org/ko/3.12/library/stdtypes.html#bytes "bytes"), and [`tuple`](https://docs.python.org/ko/3.12/library/stdtypes.html#tuple "tuple").
    
- Any non-string [iterable](https://docs.python.org/ko/3.12/glossary.html#term-iterable) may be assigned to ___slots___.
    
- If a [`dictionary`](https://docs.python.org/ko/3.12/library/stdtypes.html#dict "dict") is used to assign ___slots___, the dictionary keys will be used as the slot names. The values of the dictionary can be used to provide per-attribute docstrings that will be recognised by [`inspect.getdoc()`](https://docs.python.org/ko/3.12/library/inspect.html#inspect.getdoc "inspect.getdoc") and displayed in the output of [`help()`](https://docs.python.org/ko/3.12/library/functions.html#help "help").
    
- [`__class__`](https://docs.python.org/ko/3.12/library/stdtypes.html#instance.__class__ "instance.__class__") assignment works only if both classes have the same ___slots___.
    
- [Multiple inheritance](https://docs.python.org/ko/3.12/tutorial/classes.html#tut-multiple) with multiple slotted parent classes can be used, but only one parent is allowed to have attributes created by slots (the other bases must have empty slot layouts) - violations raise [`TypeError`](https://docs.python.org/ko/3.12/library/exceptions.html#TypeError "TypeError").
    
- If an [iterator](https://docs.python.org/ko/3.12/glossary.html#term-iterator) is used for ___slots___ then a [descriptor](https://docs.python.org/ko/3.12/glossary.html#term-descriptor) is created for each of the iterator’s values. However, the ___slots___ attribute will be an empty iterator.
    

### 3.3.3. 클래스 생성 커스터마이제이션[](https://docs.python.org/ko/3.12/reference/datamodel.html#customizing-class-creation "Link to this heading")

Whenever a class inherits from another class, [`__init_subclass__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__init_subclass__ "object.__init_subclass__") is called on the parent class. This way, it is possible to write classes which change the behavior of subclasses. This is closely related to class decorators, but where class decorators only affect the specific class they’re applied to, `__init_subclass__` solely applies to future subclasses of the class defining the method.

_classmethod_ object.__init_subclass__(_cls_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__init_subclass__ "Link to this definition")

이 메서드는 포함하는 클래스의 서브 클래스가 만들어질 때마다 호출됩니다. _cls_ 는 새 서브 클래스입니다. 만약 일반적인 인스턴스 메서드로 정의되면, 이 메서드는 묵시적으로 클래스 메서드로 변경됩니다.

Keyword arguments which are given to a new class are passed to the parent class’s `__init_subclass__`. For compatibility with other classes using `__init_subclass__`, one should take out the needed keyword arguments and pass the others over to the base class, as in:

class Philosopher:
    def __init_subclass__(cls, /, default_name, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.default_name = default_name

class AustralianPhilosopher(Philosopher, default_name="Bruce"):
    pass

기본 구현 `object.__init_subclass__` 는 아무 일도 하지 않지만, 인자가 포함되어 호출되면 예외를 발생시킵니다.

참고

 

메타 클래스 힌트 `metaclass` 는 나머지 형 절차에 의해 소비되고, `__init_subclass__` 로 전달되지 않습니다. 실제 메타 클래스 (명시적인 힌트 대신에) 는 `type(cls)` 로 액세스할 수 있습니다.

Added in version 3.6.

When a class is created, `type.__new__()` scans the class variables and makes callbacks to those with a [`__set_name__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__set_name__ "object.__set_name__") hook.

object.__set_name__(_self_, _owner_, _name_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__set_name__ "Link to this definition")

Automatically called at the time the owning class _owner_ is created. The object has been assigned to _name_ in that class:

class A:
    x = C()  # Automatically calls: x.__set_name__(A, 'x')

If the class variable is assigned after the class is created, [`__set_name__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__set_name__ "object.__set_name__") will not be called automatically. If needed, [`__set_name__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__set_name__ "object.__set_name__") can be called directly:

class A:
   pass

c = C()
A.x = c                  # The hook is not called
c.__set_name__(A, 'x')   # Manually invoke the hook

더 자세한 내용은 [클래스 객체 만들기](https://docs.python.org/ko/3.12/reference/datamodel.html#class-object-creation) 을 참고하십시오.

Added in version 3.6.

#### 3.3.3.1. 메타 클래스[](https://docs.python.org/ko/3.12/reference/datamodel.html#metaclasses "Link to this heading")

기본적으로, 클래스는 [`type()`](https://docs.python.org/ko/3.12/library/functions.html#type "type") 을 사용해서 만들어집니다. 클래스의 바디는 새 이름 공간에서 실행되고, 클래스 이름은 `type(name, bases, namespace)` 의 결과에 지역적으로 연결됩니다.

클래스를 만드는 과정은 클래스 정의 줄에 `metaclass` 키워드 인자를 전달하거나, 그런 인자를 포함한 이미 존재하는 클래스를 계승함으로써 커스터마이즈될 수 있습니다. 다음 예에서, `MyClass` 와 `MySubclass` 는 모두 `Meta` 의 인스턴스입니다.

class Meta(type):
    pass

class MyClass(metaclass=Meta):
    pass

class MySubclass(MyClass):
    pass

클래스 정의에서 지정된 다른 키워드 인자들은 아래에서 설명되는 모든 메타 클래스 연산들로 전달됩니다.

클래스 정의가 실행될 때, 다음과 같은 단계가 수행됩니다.:

- MRO 항목이 결정됩니다;
    
- 적절한 메타 클래스가 결정됩니다;
    
- 클래스 이름 공간이 준비됩니다;
    
- 클래스 바디가 실행됩니다;
    
- 클래스 객체가 만들어집니다.
    

#### 3.3.3.2. MRO 항목 결정하기[](https://docs.python.org/ko/3.12/reference/datamodel.html#resolving-mro-entries "Link to this heading")

object.__mro_entries__(_self_, _bases_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__mro_entries__ "Link to this definition")

If a base that appears in a class definition is not an instance of [`type`](https://docs.python.org/ko/3.12/library/functions.html#type "type"), then an `__mro_entries__()` method is searched on the base. If an `__mro_entries__()` method is found, the base is substituted with the result of a call to `__mro_entries__()` when creating the class. The method is called with the original bases tuple passed to the _bases_ parameter, and must return a tuple of classes that will be used instead of the base. The returned tuple may be empty: in these cases, the original base is ignored.

더 보기

[`types.resolve_bases()`](https://docs.python.org/ko/3.12/library/types.html#types.resolve_bases "types.resolve_bases")

Dynamically resolve bases that are not instances of [`type`](https://docs.python.org/ko/3.12/library/functions.html#type "type").

[`types.get_original_bases()`](https://docs.python.org/ko/3.12/library/types.html#types.get_original_bases "types.get_original_bases")

Retrieve a class’s “original bases” prior to modifications by [`__mro_entries__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__mro_entries__ "object.__mro_entries__").

[**PEP 560**](https://peps.python.org/pep-0560/)

Core support for typing module and generic types.

#### 3.3.3.3. 적절한 메타 클래스 선택하기[](https://docs.python.org/ko/3.12/reference/datamodel.html#determining-the-appropriate-metaclass "Link to this heading")

클래스 정의의 적절한 메타 클래스는 다음과 같이 결정됩니다:

- 베이스와 명시적인 메타 클래스를 주지 않는 경우 [`type()`](https://docs.python.org/ko/3.12/library/functions.html#type "type") 이 사용됩니다;
    
- 명시적인 메타 클래스가 지정되고, 그것이 [`type()`](https://docs.python.org/ko/3.12/library/functions.html#type "type") 의 인스턴스가 _아니면_, 그것을 메타 클래스로 사용합니다;
    
- [`type()`](https://docs.python.org/ko/3.12/library/functions.html#type "type") 의 인스턴스가 명시적인 메타 클래스로 주어지거나, 베이스가 정의되었으면, 가장 많이 파생된 메타 클래스가 사용됩니다.
    

가장 많이 파생된 메타 클래스는 명시적으로 지정된 메타 클래스(있다면)와 지정된 모든 베이스 클래스들의 메타 클래스들(즉, `type(cls)`) 중에서 선택됩니다. 가장 많이 파생된 메타 클래스는 이들 _모두_ 의 서브 타입(subtype)입니다. 만약 어느 것도 이 조건을 만족하지 못한다면, 클래스 정의는 `TypeError` 를 발생시키며 실패합니다.

#### 3.3.3.4. 클래스 이름 공간 준비하기[](https://docs.python.org/ko/3.12/reference/datamodel.html#preparing-the-class-namespace "Link to this heading")

Once the appropriate metaclass has been identified, then the class namespace is prepared. If the metaclass has a `__prepare__` attribute, it is called as `namespace = metaclass.__prepare__(name, bases, **kwds)` (where the additional keyword arguments, if any, come from the class definition). The `__prepare__` method should be implemented as a [`classmethod`](https://docs.python.org/ko/3.12/library/functions.html#classmethod "classmethod"). The namespace returned by `__prepare__` is passed in to `__new__`, but when the final class object is created the namespace is copied into a new `dict`.

만약 메타 클래스에 `__prepare__` 어트리뷰트가 없다면, 클래스 이름 공간은 빈 순서 있는 매핑으로 초기화됩니다.

더 보기

[**PEP 3115**](https://peps.python.org/pep-3115/) - 파이썬 3000 에서의 메타 클래스

`__prepare__` 이름 공간 훅을 도입했습니다

#### 3.3.3.5. 클래스 바디 실행하기[](https://docs.python.org/ko/3.12/reference/datamodel.html#executing-the-class-body "Link to this heading")

클래스 바디는 (대략) `exec(body, globals(), namespace)` 과같이 실행됩니다. 일반적인 [`exec()`](https://docs.python.org/ko/3.12/library/functions.html#exec "exec") 호출과 주된 차이점은 클래스 정의가 함수 내부에서 이루어질 때 어휘 스코핑(lexical scoping) 이 클래스 바디(모든 메서드들을 포함해서)로 하여금 현재와 외부 스코프에 있는 이름들을 참조하도록 허락한다는 것입니다.

하지만, 클래스 정의가 함수 내부에서 이루어질 때조차도, 클래스 내부에서 정의된 메서드들은 클래스 스코프에서 정의된 이름들을 볼 수 없습니다. 클래스 변수는 인스턴스나 클래스 메서드의 첫 번째 매개변수를 통해 액세스하거나 다음 섹션에서 설명하는 묵시적으로 어휘 스코핑된 `__class__` 참조를 통해야 합니다.

#### 3.3.3.6. 클래스 객체 만들기[](https://docs.python.org/ko/3.12/reference/datamodel.html#creating-the-class-object "Link to this heading")

일단 클래스 이름 공간이 클래스 바디를 실행함으로써 채워지면, 클래스 객체가 `metaclass(name, bases, namespace, **kwds)` 을 통해 만들어집니다(여기에서 전달되는 추가적인 키워드 인자들은 `__prepare__` 에 전달된 것들과 같습니다).

이 클래스 객체는 [`super()`](https://docs.python.org/ko/3.12/library/functions.html#super "super") 에 인자를 주지 않는 경우 참조되는 것입니다. `__class__` 는 클래스 바디의 메서드들 중 어느 하나라도 `__class__` 나 `super` 를 참조할 경우 컴파일러에 의해 만들어지는 묵시적인 클로저(closure) 참조입니다. 이것은 인자 없는 형태의 [`super()`](https://docs.python.org/ko/3.12/library/functions.html#super "super") 가 어휘 스코핑 기반으로 현재 정의되고 있는 클래스를 올바르게 찾을 수 있도록 합니다. 반면에 현재의 호출에 사용된 클래스나 인스턴스는 메서드로 전달된 첫 번째 인자에 기초해서 식별됩니다.

**CPython 구현 상세:** CPython 3.6 이상에서, `__class__` 셀(cell)은 클래스 이름 공간의 `__classcell__` 엔트리로 메타 클래스에 전달됩니다. 만약 존재한다면, 이것은 클래스가 올바르게 초기화되기 위해 `type.__new__` 호출까지 거슬러서 전파되어야 합니다. 이렇게 하지 못하면 파이썬 3.8 에서는 [`RuntimeError`](https://docs.python.org/ko/3.12/library/exceptions.html#RuntimeError "RuntimeError")로 이어질 것입니다.

When using the default metaclass [`type`](https://docs.python.org/ko/3.12/library/functions.html#type "type"), or any metaclass that ultimately calls `type.__new__`, the following additional customization steps are invoked after creating the class object:

1. The `type.__new__` method collects all of the attributes in the class namespace that define a [`__set_name__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__set_name__ "object.__set_name__") method;
    
2. Those `__set_name__` methods are called with the class being defined and the assigned name of that particular attribute;
    
3. The [`__init_subclass__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__init_subclass__ "object.__init_subclass__") hook is called on the immediate parent of the new class in its method resolution order.
    

클래스 객체가 만들어진 후에, 클래스 정의에 포함된 클래스 데코레이터들에게 (있다면) 클래스를 전달하고, 그 결과를 클래스가 정의되는 지역 이름 공간에 연결합니다.

`type.__new__` 로 새 클래스가 만들어질 때, 이름 공간 매개변수로 제공되는 객체는 새로 만든 순서 있는 매핑으로 복사되고, 원래의 객체는 버립니다. 새 사본은 읽기 전용 프락시(read-only proxy)로 둘러싸이는데, 이것이 클래스 객체의 [`__dict__`](https://docs.python.org/ko/3.12/library/stdtypes.html#object.__dict__ "object.__dict__") 어트리뷰트가 됩니다.

더 보기

[**PEP 3135**](https://peps.python.org/pep-3135/) - 새 super

묵시적인 __class__ 클로저 참조를 설명합니다

#### 3.3.3.7. 메타 클래스의 용도[](https://docs.python.org/ko/3.12/reference/datamodel.html#uses-for-metaclasses "Link to this heading")

메타 클래스의 잠재적인 용도에는 한계가 없습니다. 탐색 된 몇 가지 아이디어들에는 enum, 로깅, 인터페이스 검사, 자동화된 위임(automatic delegation), 자동화된 프로퍼티(properety) 생성, 프락시(proxy), 프레임웍(framework), 자동화된 자원 로킹/동기화(automatic resource locking/synchronization) 등이 있습니다.

### 3.3.4. 인스턴스 및 서브 클래스 검사 커스터마이제이션[](https://docs.python.org/ko/3.12/reference/datamodel.html#customizing-instance-and-subclass-checks "Link to this heading")

다음 메서드들은 [`isinstance()`](https://docs.python.org/ko/3.12/library/functions.html#isinstance "isinstance") 와 [`issubclass()`](https://docs.python.org/ko/3.12/library/functions.html#issubclass "issubclass") 내장 함수들의 기본 동작을 재정의하는 데 사용됩니다.

특히, 메타 클래스 [`abc.ABCMeta`](https://docs.python.org/ko/3.12/library/abc.html#abc.ABCMeta "abc.ABCMeta") 는 추상 베이스 클래스(Abstract Base Class, ABC)를 다른 ABC를 포함한 임의의 클래스나 형(내장형을 포함합니다)에 “가상 베이스 클래스(virtual base class)”로 추가할 수 있게 하려고 이 메서드들을 구현합니다.

class.__instancecheck__(_self_, _instance_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#class.__instancecheck__ "Link to this definition")

_instance_ 가 (직접적이거나 간접적으로) _class_ 의 인스턴스로 취급될 수 있으면 참을 돌려줍니다. 만약 정의되면, `isinstance(instance, class)` 를 구현하기 위해 호출됩니다.

class.__subclasscheck__(_self_, _subclass_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#class.__subclasscheck__ "Link to this definition")

_subclass_ 가 (직접적이거나 간접적으로) _class_ 의 서브 클래스로 취급될 수 있으면 참을 돌려줍니다. 만약 정의되면, `issubclass(subclass, class)` 를 구현하기 위해 호출됩니다.

이 메서드들은 클래스의 형(메타 클래스)에서 조회된다는 것에 주의해야 합니다. 실제 클래스에서 클래스 메서드로 정의될 수 없습니다. 이것은 인스턴스에 대해 호출되는 특수 메서드들의 조회와 일관성 있습니다. 이 경우 인스턴스는 클래스 자체다.

더 보기

[**PEP 3119**](https://peps.python.org/pep-3119/) - 추상 베이스 클래스의 도입

[`__instancecheck__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#class.__instancecheck__ "class.__instancecheck__") 와 [`__subclasscheck__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#class.__subclasscheck__ "class.__subclasscheck__") 를 통해 [`isinstance()`](https://docs.python.org/ko/3.12/library/functions.html#isinstance "isinstance") 와 [`issubclass()`](https://docs.python.org/ko/3.12/library/functions.html#issubclass "issubclass") 의 동작을 커스터마이징하는 데 필요한 규약을 포함하는데, 이 기능의 동기는 언어에 추상 베이스 클래스 ([`abc`](https://docs.python.org/ko/3.12/library/abc.html#module-abc "abc: Abstract base classes according to :pep:`3119`.") 모듈을 보십시오)를 추가하고자 하는 데 있습니다.

### 3.3.5. 제네릭 형 흉내 내기[](https://docs.python.org/ko/3.12/reference/datamodel.html#emulating-generic-types "Link to this heading")

When using [type annotations](https://docs.python.org/ko/3.12/glossary.html#term-annotation), it is often useful to _parameterize_ a [generic type](https://docs.python.org/ko/3.12/glossary.html#term-generic-type) using Python’s square-brackets notation. For example, the annotation `list[int]` might be used to signify a [`list`](https://docs.python.org/ko/3.12/library/stdtypes.html#list "list") in which all the elements are of type [`int`](https://docs.python.org/ko/3.12/library/functions.html#int "int").

더 보기

[**PEP 484**](https://peps.python.org/pep-0484/) - Type Hints

Introducing Python’s framework for type annotations

[Generic Alias Types](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias)

Documentation for objects representing parameterized generic classes

[제네릭](https://docs.python.org/ko/3.12/library/typing.html#generics), [user-defined generics](https://docs.python.org/ko/3.12/library/typing.html#user-defined-generics) and [`typing.Generic`](https://docs.python.org/ko/3.12/library/typing.html#typing.Generic "typing.Generic")

Documentation on how to implement generic classes that can be parameterized at runtime and understood by static type-checkers.

A class can _generally_ only be parameterized if it defines the special class method `__class_getitem__()`.

_classmethod_ object.__class_getitem__(_cls_, _key_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__class_getitem__ "Link to this definition")

_key_ 에 있는 형 인자에 의한 제네릭 클래스의 특수화를 나타내는 객체를 돌려줍니다.

When defined on a class, `__class_getitem__()` is automatically a class method. As such, there is no need for it to be decorated with [`@classmethod`](https://docs.python.org/ko/3.12/library/functions.html#classmethod "classmethod") when it is defined.

#### 3.3.5.1. The purpose of ___class_getitem___[](https://docs.python.org/ko/3.12/reference/datamodel.html#the-purpose-of-class-getitem "Link to this heading")

The purpose of [`__class_getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__") is to allow runtime parameterization of standard-library generic classes in order to more easily apply [type hints](https://docs.python.org/ko/3.12/glossary.html#term-type-hint) to these classes.

To implement custom generic classes that can be parameterized at runtime and understood by static type-checkers, users should either inherit from a standard library class that already implements [`__class_getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__"), or inherit from [`typing.Generic`](https://docs.python.org/ko/3.12/library/typing.html#typing.Generic "typing.Generic"), which has its own implementation of `__class_getitem__()`.

Custom implementations of [`__class_getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__") on classes defined outside of the standard library may not be understood by third-party type-checkers such as mypy. Using `__class_getitem__()` on any class for purposes other than type hinting is discouraged.

#### 3.3.5.2. ___class_getitem___ versus ___getitem___[](https://docs.python.org/ko/3.12/reference/datamodel.html#class-getitem-versus-getitem "Link to this heading")

Usually, the [subscription](https://docs.python.org/ko/3.12/reference/expressions.html#subscriptions) of an object using square brackets will call the [`__getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getitem__ "object.__getitem__") instance method defined on the object’s class. However, if the object being subscribed is itself a class, the class method [`__class_getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__") may be called instead. `__class_getitem__()` should return a [GenericAlias](https://docs.python.org/ko/3.12/library/stdtypes.html#types-genericalias) object if it is properly defined.

Presented with the [expression](https://docs.python.org/ko/3.12/glossary.html#term-expression) `obj[x]`, the Python interpreter follows something like the following process to decide whether [`__getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getitem__ "object.__getitem__") or [`__class_getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__") should be called:

from inspect import isclass

def subscribe(obj, x):
    """Return the result of the expression 'obj[x]'"""

    class_of_obj = type(obj)

    # If the class of obj defines __getitem__,
    # call class_of_obj.__getitem__(obj, x)
    if hasattr(class_of_obj, '__getitem__'):
        return class_of_obj.__getitem__(obj, x)

    # Else, if obj is a class and defines __class_getitem__,
    # call obj.__class_getitem__(x)
    elif isclass(obj) and hasattr(obj, '__class_getitem__'):
        return obj.__class_getitem__(x)

    # Else, raise an exception
    else:
        raise TypeError(
            f"'{class_of_obj.__name__}' object is not subscriptable"
        )

In Python, all classes are themselves instances of other classes. The class of a class is known as that class’s [metaclass](https://docs.python.org/ko/3.12/glossary.html#term-metaclass), and most classes have the [`type`](https://docs.python.org/ko/3.12/library/functions.html#type "type") class as their metaclass. [`type`](https://docs.python.org/ko/3.12/library/functions.html#type "type") does not define [`__getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getitem__ "object.__getitem__"), meaning that expressions such as `list[int]`, `dict[str, float]` and `tuple[str, bytes]` all result in [`__class_getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__") being called:

>>>

>>> # list has class "type" as its metaclass, like most classes:
>>> type(list)
<class 'type'>
>>> type(dict) == type(list) == type(tuple) == type(str) == type(bytes)
True
>>> # "list[int]" calls "list.__class_getitem__(int)"
>>> list[int]
list[int]
>>> # list.__class_getitem__ returns a GenericAlias object:
>>> type(list[int])
<class 'types.GenericAlias'>

However, if a class has a custom metaclass that defines [`__getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getitem__ "object.__getitem__"), subscribing the class may result in different behaviour. An example of this can be found in the [`enum`](https://docs.python.org/ko/3.12/library/enum.html#module-enum "enum: Implementation of an enumeration class.") module:

>>>

>>> from enum import Enum
>>> class Menu(Enum):
... """A breakfast menu"""
...     SPAM = 'spam'
...     BACON = 'bacon'
...
>>> # Enum classes have a custom metaclass:
>>> type(Menu)
<class 'enum.EnumMeta'>
>>> # EnumMeta defines __getitem__,
>>> # so __class_getitem__ is not called,
>>> # and the result is not a GenericAlias object:
>>> Menu['SPAM']
<Menu.SPAM: 'spam'>
>>> type(Menu['SPAM'])
<enum 'Menu'>

더 보기

[**PEP 560**](https://peps.python.org/pep-0560/) - Core Support for typing module and generic types

Introducing [`__class_getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__"), and outlining when a [subscription](https://docs.python.org/ko/3.12/reference/expressions.html#subscriptions) results in `__class_getitem__()` being called instead of [`__getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getitem__ "object.__getitem__")

### 3.3.6. 콜러블 객체 흉내 내기[](https://docs.python.org/ko/3.12/reference/datamodel.html#emulating-callable-objects "Link to this heading")

object.__call__(_self_[, _args..._])[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__call__ "Link to this definition")

인스턴스가 함수처럼 “호출될” 때 호출됩니다; 이 메서드가 정의되면, `x(arg1, arg2, ...)` 는 대략 `type(x).__call__(x, arg1, ...)`로 번역됩니다.

### 3.3.7. 컨테이너형 흉내 내기[](https://docs.python.org/ko/3.12/reference/datamodel.html#emulating-container-types "Link to this heading")

The following methods can be defined to implement container objects. Containers usually are [sequences](https://docs.python.org/ko/3.12/glossary.html#term-sequence) (such as [`lists`](https://docs.python.org/ko/3.12/library/stdtypes.html#list "list") or [`tuples`](https://docs.python.org/ko/3.12/library/stdtypes.html#tuple "tuple")) or [mappings](https://docs.python.org/ko/3.12/glossary.html#term-mapping) (like [`dictionaries`](https://docs.python.org/ko/3.12/library/stdtypes.html#dict "dict")), but can represent other containers as well. The first set of methods is used either to emulate a sequence or to emulate a mapping; the difference is that for a sequence, the allowable keys should be the integers _k_ for which `0 <= k < N` where _N_ is the length of the sequence, or [`slice`](https://docs.python.org/ko/3.12/library/functions.html#slice "slice") objects, which define a range of items. It is also recommended that mappings provide the methods `keys()`, `values()`, `items()`, `get()`, `clear()`, `setdefault()`, `pop()`, `popitem()`, `copy()`, and `update()` behaving similar to those for Python’s standard [`dictionary`](https://docs.python.org/ko/3.12/library/stdtypes.html#dict "dict") objects. The [`collections.abc`](https://docs.python.org/ko/3.12/library/collections.abc.html#module-collections.abc "collections.abc: Abstract base classes for containers") module provides a [`MutableMapping`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.MutableMapping "collections.abc.MutableMapping") [abstract base class](https://docs.python.org/ko/3.12/glossary.html#term-abstract-base-class) to help create those methods from a base set of [`__getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getitem__ "object.__getitem__"), [`__setitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__setitem__ "object.__setitem__"), [`__delitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__delitem__ "object.__delitem__"), and `keys()`. Mutable sequences should provide methods `append()`, `count()`, `index()`, `extend()`, `insert()`, `pop()`, `remove()`, `reverse()` and `sort()`, like Python standard [`list`](https://docs.python.org/ko/3.12/library/stdtypes.html#list "list") objects. Finally, sequence types should implement addition (meaning concatenation) and multiplication (meaning repetition) by defining the methods [`__add__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__add__ "object.__add__"), [`__radd__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__radd__ "object.__radd__"), [`__iadd__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__iadd__ "object.__iadd__"), [`__mul__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__mul__ "object.__mul__"), [`__rmul__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__rmul__ "object.__rmul__") and [`__imul__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__imul__ "object.__imul__") described below; they should not define other numerical operators. It is recommended that both mappings and sequences implement the [`__contains__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__contains__ "object.__contains__") method to allow efficient use of the `in` operator; for mappings, `in` should search the mapping’s keys; for sequences, it should search through the values. It is further recommended that both mappings and sequences implement the [`__iter__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__iter__ "object.__iter__") method to allow efficient iteration through the container; for mappings, `__iter__()` should iterate through the object’s keys; for sequences, it should iterate through the values.

object.__len__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__len__ "Link to this definition")

Called to implement the built-in function [`len()`](https://docs.python.org/ko/3.12/library/functions.html#len "len"). Should return the length of the object, an integer `>=` 0. Also, an object that doesn’t define a [`__bool__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__bool__ "object.__bool__") method and whose `__len__()` method returns zero is considered to be false in a Boolean context.

**CPython 구현 상세:** In CPython, the length is required to be at most [`sys.maxsize`](https://docs.python.org/ko/3.12/library/sys.html#sys.maxsize "sys.maxsize"). If the length is larger than `sys.maxsize` some features (such as [`len()`](https://docs.python.org/ko/3.12/library/functions.html#len "len")) may raise [`OverflowError`](https://docs.python.org/ko/3.12/library/exceptions.html#OverflowError "OverflowError"). To prevent raising `OverflowError` by truth value testing, an object must define a [`__bool__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__bool__ "object.__bool__") method.

object.__length_hint__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__length_hint__ "Link to this definition")

Called to implement [`operator.length_hint()`](https://docs.python.org/ko/3.12/library/operator.html#operator.length_hint "operator.length_hint"). Should return an estimated length for the object (which may be greater or less than the actual length). The length must be an integer `>=` 0. The return value may also be [`NotImplemented`](https://docs.python.org/ko/3.12/library/constants.html#NotImplemented "NotImplemented"), which is treated the same as if the `__length_hint__` method didn’t exist at all. This method is purely an optimization and is never required for correctness.

Added in version 3.4.

참고

 

슬라이싱은 전적으로 다음에 나오는 세 메서드들에의해 수행됩니다

a[1:2] = b

과 같은 호출은

a[slice(1, 2, None)] = b

로 번역되고, 다른 형태도 마찬가지입니다. 빠진 슬라이스 항목은 항상 `None` 으로 채워집니다.

object.__getitem__(_self_, _key_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getitem__ "Link to this definition")

Called to implement evaluation of `self[key]`. For [sequence](https://docs.python.org/ko/3.12/glossary.html#term-sequence) types, the accepted keys should be integers. Optionally, they may support [`slice`](https://docs.python.org/ko/3.12/library/functions.html#slice "slice") objects as well. Negative index support is also optional. If _key_ is of an inappropriate type, [`TypeError`](https://docs.python.org/ko/3.12/library/exceptions.html#TypeError "TypeError") may be raised; if _key_ is a value outside the set of indexes for the sequence (after any special interpretation of negative values), [`IndexError`](https://docs.python.org/ko/3.12/library/exceptions.html#IndexError "IndexError") should be raised. For [mapping](https://docs.python.org/ko/3.12/glossary.html#term-mapping) types, if _key_ is missing (not in the container), [`KeyError`](https://docs.python.org/ko/3.12/library/exceptions.html#KeyError "KeyError") should be raised.

참고

 

[`for`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#for) 루프는 시퀀스의 끝을 올바로 감지하기 위해, 잘못된 인덱스에 대해 [`IndexError`](https://docs.python.org/ko/3.12/library/exceptions.html#IndexError "IndexError") 가 일어날 것으로 기대하고 있습니다.

참고

 

When [subscripting](https://docs.python.org/ko/3.12/reference/expressions.html#subscriptions) a _class_, the special class method [`__class_getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__") may be called instead of `__getitem__()`. See [__class_getitem__ versus __getitem__](https://docs.python.org/ko/3.12/reference/datamodel.html#classgetitem-versus-getitem) for more details.

object.__setitem__(_self_, _key_, _value_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__setitem__ "Link to this definition")

`self[key]` 로의 대입을 구현하기 위해 호출됩니다. [`__getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getitem__ "object.__getitem__") 과 같은 주의가 필요합니다. 매핑의 경우에는, 객체가 키에 대해 값의 변경이나 새 키의 추가를 허락할 경우, 시퀀스의 경우는 항목이 교체될 수 있을 때만 구현되어야 합니다. 잘못된 _key_ 값의 경우는 [`__getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getitem__ "object.__getitem__") 에서와 같은 예외를 일으켜야 합니다.

object.__delitem__(_self_, _key_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__delitem__ "Link to this definition")

`self[key]` 의 삭제를 구현하기 위해 호출됩니다. [`__getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getitem__ "object.__getitem__") 과 같은 주의가 필요합니다. 매핑의 경우에는, 객체가 키의 삭제를 허락할 경우, 시퀀스의 경우는 항목이 시퀀스로부터 제거될 수 있을 때만 구현되어야 합니다. 잘못된 _key_ 값의 경우는 [`__getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getitem__ "object.__getitem__") 에서와 같은 예외를 일으켜야 합니다.

object.__missing__(_self_, _key_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__missing__ "Link to this definition")

[`dict`](https://docs.python.org/ko/3.12/library/stdtypes.html#dict "dict").[`__getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getitem__ "object.__getitem__") 이 dict 서브 클래스에서 키가 딕셔너리에 없으면 `self[key]` 를 구현하기 위해 호출합니다.

object.__iter__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__iter__ "Link to this definition")

This method is called when an [iterator](https://docs.python.org/ko/3.12/glossary.html#term-iterator) is required for a container. This method should return a new iterator object that can iterate over all the objects in the container. For mappings, it should iterate over the keys of the container.

object.__reversed__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__reversed__ "Link to this definition")

[`reversed()`](https://docs.python.org/ko/3.12/library/functions.html#reversed "reversed") 내장 함수가 역 이터레이션(reverse iteration)을 구현하기 위해 (있다면) 호출합니다. 컨테이너에 있는 객체들을 역 순으로 탐색하는 새 이터레이터 객체를 돌려줘야 합니다.

[`__reversed__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__reversed__ "object.__reversed__") 메서드가 제공되지 않으면, [`reversed()`](https://docs.python.org/ko/3.12/library/functions.html#reversed "reversed") 내장함수는 시퀀스 프로토콜([`__len__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__len__ "object.__len__") 과 [`__getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getitem__ "object.__getitem__"))을 대안으로 사용합니다. 시퀀스 프로토콜을 지원하는 객체들은 [`reversed()`](https://docs.python.org/ko/3.12/library/functions.html#reversed "reversed") 가 제공하는 것보다 더 효율적인 구현을 제공할 수 있을 때만 [`__reversed__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__reversed__ "object.__reversed__") 를 제공해야 합니다.

멤버십 검사 연산자들([`in`](https://docs.python.org/ko/3.12/reference/expressions.html#in) 과 [`not in`](https://docs.python.org/ko/3.12/reference/expressions.html#not-in)) 은 보통 컨테이너에 대한 이터레이션으로 구현됩니다. 하지만, 컨테이너 객체는 더 효율적인 구현을 다음과 같은 특수 메서드를 통해 제공할 수 있습니다. 이 경우 객체는 이터러블일 필요도 없습니다.

object.__contains__(_self_, _item_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__contains__ "Link to this definition")

멤버십 검사 연산자를 구현하기 위해 호출됩니다. _item_ 이 _self_ 에 있으면 참을, 그렇지 않으면 거짓을 돌려줘야 합니다. 매핑 객체의 경우, 키-값 쌍이 아니라 매핑의 키가 고려되어야 합니다.

[`__contains__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__contains__ "object.__contains__") 를 정의하지 않는 객체의 경우, 멤버십 검사는 먼저 [`__iter__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__iter__ "object.__iter__") 를 통한 이터레이션을 시도한 후, [`__getitem__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getitem__ "object.__getitem__") 을 통한 낡은 시퀀스 이터레이션 프로토콜을 시도합니다. [언어 레퍼런스의 이 절](https://docs.python.org/ko/3.12/reference/expressions.html#membership-test-details)을 참고하십시오.

### 3.3.8. 숫자 형 흉내 내기[](https://docs.python.org/ko/3.12/reference/datamodel.html#emulating-numeric-types "Link to this heading")

숫자 형을 흉내 내기 위해 다음과 같은 메서드들을 정의할 수 있습니다. 구현되는 특별한 종류의 숫자에 의해 지원되지 않는 연산들(예를 들어, 정수가 아닌 숫자들에 대한 비트 연산들)에 대응하는 메서드들을 정의되지 않은 채로 남겨두어야 합니다.

object.__add__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__add__ "Link to this definition")

object.__sub__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__sub__ "Link to this definition")

object.__mul__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__mul__ "Link to this definition")

object.__matmul__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__matmul__ "Link to this definition")

object.__truediv__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__truediv__ "Link to this definition")

object.__floordiv__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__floordiv__ "Link to this definition")

object.__mod__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__mod__ "Link to this definition")

object.__divmod__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__divmod__ "Link to this definition")

object.__pow__(_self_, _other_[, _modulo_])[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__pow__ "Link to this definition")

object.__lshift__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__lshift__ "Link to this definition")

object.__rshift__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__rshift__ "Link to this definition")

object.__and__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__and__ "Link to this definition")

object.__xor__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__xor__ "Link to this definition")

object.__or__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__or__ "Link to this definition")

These methods are called to implement the binary arithmetic operations (`+`, `-`, `*`, `@`, `/`, `//`, `%`, [`divmod()`](https://docs.python.org/ko/3.12/library/functions.html#divmod "divmod"), [`pow()`](https://docs.python.org/ko/3.12/library/functions.html#pow "pow"), `**`, `<<`, `>>`, `&`, `^`, `|`). For instance, to evaluate the expression `x + y`, where _x_ is an instance of a class that has an [`__add__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__add__ "object.__add__") method, `type(x).__add__(x, y)` is called. The [`__divmod__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__divmod__ "object.__divmod__") method should be the equivalent to using [`__floordiv__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__floordiv__ "object.__floordiv__") and [`__mod__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__mod__ "object.__mod__"); it should not be related to [`__truediv__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__truediv__ "object.__truediv__"). Note that [`__pow__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__pow__ "object.__pow__") should be defined to accept an optional third argument if the ternary version of the built-in [`pow()`](https://docs.python.org/ko/3.12/library/functions.html#pow "pow") function is to be supported.

If one of those methods does not support the operation with the supplied arguments, it should return [`NotImplemented`](https://docs.python.org/ko/3.12/library/constants.html#NotImplemented "NotImplemented").

object.__radd__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__radd__ "Link to this definition")

object.__rsub__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__rsub__ "Link to this definition")

object.__rmul__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__rmul__ "Link to this definition")

object.__rmatmul__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__rmatmul__ "Link to this definition")

object.__rtruediv__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__rtruediv__ "Link to this definition")

object.__rfloordiv__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__rfloordiv__ "Link to this definition")

object.__rmod__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__rmod__ "Link to this definition")

object.__rdivmod__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__rdivmod__ "Link to this definition")

object.__rpow__(_self_, _other_[, _modulo_])[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__rpow__ "Link to this definition")

object.__rlshift__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__rlshift__ "Link to this definition")

object.__rrshift__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__rrshift__ "Link to this definition")

object.__rand__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__rand__ "Link to this definition")

object.__rxor__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__rxor__ "Link to this definition")

object.__ror__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__ror__ "Link to this definition")

These methods are called to implement the binary arithmetic operations (`+`, `-`, `*`, `@`, `/`, `//`, `%`, [`divmod()`](https://docs.python.org/ko/3.12/library/functions.html#divmod "divmod"), [`pow()`](https://docs.python.org/ko/3.12/library/functions.html#pow "pow"), `**`, `<<`, `>>`, `&`, `^`, `|`) with reflected (swapped) operands. These functions are only called if the left operand does not support the corresponding operation [[3]](https://docs.python.org/ko/3.12/reference/datamodel.html#id19) and the operands are of different types. [[4]](https://docs.python.org/ko/3.12/reference/datamodel.html#id20) For instance, to evaluate the expression `x - y`, where _y_ is an instance of a class that has an [`__rsub__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__rsub__ "object.__rsub__") method, `type(y).__rsub__(y, x)` is called if `type(x).__sub__(x, y)` returns [`NotImplemented`](https://docs.python.org/ko/3.12/library/constants.html#NotImplemented "NotImplemented").

삼 항 [`pow()`](https://docs.python.org/ko/3.12/library/functions.html#pow "pow") 는 [`__rpow__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__rpow__ "object.__rpow__") 를 호출하려고 시도하지 않음에 주의해야 합니다 (그렇게 하려면 코어션 규칙이 너무 복잡해집니다).

참고

 

만약 오른쪽 피연산자의 형이 왼쪽 피연산자의 형의 서브 클래스이고, 그 서브 클래스가 연산의 뒤집힌 메서드의 다른 구현을 제공하면, 이 메서드가 왼쪽 연산자의 뒤집히지 않은 메서드보다 먼저 호출됩니다. 이 동작은 서브 클래스가 조상들의 연산을 재정의할 수 있도록 합니다.

object.__iadd__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__iadd__ "Link to this definition")

object.__isub__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__isub__ "Link to this definition")

object.__imul__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__imul__ "Link to this definition")

object.__imatmul__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__imatmul__ "Link to this definition")

object.__itruediv__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__itruediv__ "Link to this definition")

object.__ifloordiv__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__ifloordiv__ "Link to this definition")

object.__imod__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__imod__ "Link to this definition")

object.__ipow__(_self_, _other_[, _modulo_])[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__ipow__ "Link to this definition")

object.__ilshift__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__ilshift__ "Link to this definition")

object.__irshift__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__irshift__ "Link to this definition")

object.__iand__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__iand__ "Link to this definition")

object.__ixor__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__ixor__ "Link to this definition")

object.__ior__(_self_, _other_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__ior__ "Link to this definition")

These methods are called to implement the augmented arithmetic assignments (`+=`, `-=`, `*=`, `@=`, `/=`, `//=`, `%=`, `**=`, `<<=`, `>>=`, `&=`, `^=`, `|=`). These methods should attempt to do the operation in-place (modifying _self_) and return the result (which could be, but does not have to be, _self_). If a specific method is not defined, or if that method returns [`NotImplemented`](https://docs.python.org/ko/3.12/library/constants.html#NotImplemented "NotImplemented"), the augmented assignment falls back to the normal methods. For instance, if _x_ is an instance of a class with an [`__iadd__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__iadd__ "object.__iadd__") method, `x += y` is equivalent to `x = x.__iadd__(y)` . If [`__iadd__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__iadd__ "object.__iadd__") does not exist, or if `x.__iadd__(y)` returns `NotImplemented`, `x.__add__(y)` and `y.__radd__(x)` are considered, as with the evaluation of `x + y`. In certain situations, augmented assignment can result in unexpected errors (see [덧셈은 작동하는데, 왜 a_tuple[i] += [‘item’]이 예외를 일으킵니까?](https://docs.python.org/ko/3.12/faq/programming.html#faq-augmented-assignment-tuple-error)), but this behavior is in fact part of the data model.

object.__neg__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__neg__ "Link to this definition")

object.__pos__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__pos__ "Link to this definition")

object.__abs__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__abs__ "Link to this definition")

object.__invert__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__invert__ "Link to this definition")

일 항 산술 연산(`-`, `+`, [`abs()`](https://docs.python.org/ko/3.12/library/functions.html#abs "abs"), `~`)을 구현하기 위해 호출됩니다.

object.__complex__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__complex__ "Link to this definition")

object.__int__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__int__ "Link to this definition")

object.__float__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__float__ "Link to this definition")

내장 함수 [`complex()`](https://docs.python.org/ko/3.12/library/functions.html#complex "complex"), [`int()`](https://docs.python.org/ko/3.12/library/functions.html#int "int"), [`float()`](https://docs.python.org/ko/3.12/library/functions.html#float "float")를 구현하기 위해 호출됩니다. 적절한 형의 값을 돌려줘야 합니다.

object.__index__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__index__ "Link to this definition")

[`operator.index()`](https://docs.python.org/ko/3.12/library/operator.html#operator.index "operator.index") 를 구현하기 위해 호출되고, 파이썬이 숫자 객체를 정수 객체로 손실 없이 변환해야 할 때(슬라이싱이나 내장 [`bin()`](https://docs.python.org/ko/3.12/library/functions.html#bin "bin"), [`hex()`](https://docs.python.org/ko/3.12/library/functions.html#hex "hex"), [`oct()`](https://docs.python.org/ko/3.12/library/functions.html#oct "oct") 함수들에서와같이)마다 호출됩니다. 이 메서드의 존재는 숫자 객체가 정수 형임을 가리킵니다. 반드시 정수를 돌려줘야 합니다.

[`__int__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__int__ "object.__int__"), [`__float__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__float__ "object.__float__") 및 [`__complex__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__complex__ "object.__complex__")가 정의되어 있지 않으면, 해당 내장 함수 [`int()`](https://docs.python.org/ko/3.12/library/functions.html#int "int"), [`float()`](https://docs.python.org/ko/3.12/library/functions.html#float "float") 및 [`complex()`](https://docs.python.org/ko/3.12/library/functions.html#complex "complex")는 [`__index__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__index__ "object.__index__")를 사용합니다.

object.__round__(_self_[, _ndigits_])[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__round__ "Link to this definition")

object.__trunc__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__trunc__ "Link to this definition")

object.__floor__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__floor__ "Link to this definition")

object.__ceil__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__ceil__ "Link to this definition")

내장 함수 [`round()`](https://docs.python.org/ko/3.12/library/functions.html#round "round")와 [`math`](https://docs.python.org/ko/3.12/library/math.html#module-math "math: Mathematical functions (sin() etc.).") 함수 [`trunc()`](https://docs.python.org/ko/3.12/library/math.html#math.trunc "math.trunc"), [`floor()`](https://docs.python.org/ko/3.12/library/math.html#math.floor "math.floor"), [`ceil()`](https://docs.python.org/ko/3.12/library/math.html#math.ceil "math.ceil") 을 구현하기 위해 호출됩니다. _ndigits_ 가 `__round__()` 로 전달되지 않는 한, 이 메서드들은 모두 [`Integral`](https://docs.python.org/ko/3.12/library/numbers.html#numbers.Integral "numbers.Integral") (보통 [`int`](https://docs.python.org/ko/3.12/library/functions.html#int "int")) 로 잘린 객체의 값을 돌려줘야 합니다.

The built-in function [`int()`](https://docs.python.org/ko/3.12/library/functions.html#int "int") falls back to [`__trunc__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__trunc__ "object.__trunc__") if neither [`__int__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__int__ "object.__int__") nor [`__index__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__index__ "object.__index__") is defined.

버전 3.11에서 변경: The delegation of [`int()`](https://docs.python.org/ko/3.12/library/functions.html#int "int") to [`__trunc__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__trunc__ "object.__trunc__") is deprecated.

### 3.3.9. with 문 컨텍스트 관리자[](https://docs.python.org/ko/3.12/reference/datamodel.html#with-statement-context-managers "Link to this heading")

_컨텍스트 관리자 (context manager)_ 는 [`with`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#with) 문을 실행할 때 자리 잡는 실행 컨텍스트(context)를 정의하는 객체입니다. 코드 블록의 실행을 위해, 컨텍스트 관리자는 원하는 실행시간 컨텍스트로의 진입과 탈출을 처리합니다. 컨텍스트 관리자는 보통 `with` 문([with 문](https://docs.python.org/ko/3.12/reference/compound_stmts.html#with) 섹션에서 설명합니다)으로 시작되지만, 그들의 메서드를 호출해서 직접 사용할 수도 있습니다.

컨텍스트 관리자의 전형적인 용도에는 다양한 종류의 전역 상태(global state)를 보관하고 복구하는 것, 자원을 로킹(locking)하고 언로킹(unlocking)하는 것, 열린 파일을 닫는 것 등이 있습니다.

컨텍스트 관리자에 대한 더 자세한 정보는 [컨텍스트 관리자 형](https://docs.python.org/ko/3.12/library/stdtypes.html#typecontextmanager) 에 나옵니다.

object.__enter__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__enter__ "Link to this definition")

이 객체와 연관된 실행시간 컨텍스트에 진입합니다. [`with`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#with) 문은 `as` 절로 지정된 대상이 있다면, 이 메서드의 반환 값을 연결합니다.

object.__exit__(_self_, _exc_type_, _exc_value_, _traceback_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__exit__ "Link to this definition")

이 객체와 연관된 실행시간 컨텍스트를 종료합니다. 매개변수들은 컨텍스트에서 벗어나게 만든 예외를 기술합니다. 만약 컨텍스트가 예외 없이 종료한다면, 세 인자 모두 [`None`](https://docs.python.org/ko/3.12/library/constants.html#None "None") 이 됩니다.

만약 예외가 제공되고, 메서드가 예외를 중지시키고 싶으면 (즉 확산하는 것을 막으려면) 참(true)을 돌려줘야 합니다. 그렇지 않으면 예외는 이 메서드가 종료한 후에 계속 진행됩니다.

Note that [`__exit__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__exit__ "object.__exit__") methods should not reraise the passed-in exception; this is the caller’s responsibility.

더 보기

[**PEP 343**](https://peps.python.org/pep-0343/) - “with” 문

파이썬 [`with`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#with) 문에 대한 규격, 배경, 예.

### 3.3.10. Customizing positional arguments in class pattern matching[](https://docs.python.org/ko/3.12/reference/datamodel.html#customizing-positional-arguments-in-class-pattern-matching "Link to this heading")

When using a class name in a pattern, positional arguments in the pattern are not allowed by default, i.e. `case MyClass(x, y)` is typically invalid without special support in `MyClass`. To be able to use that kind of pattern, the class needs to define a ___match_args___ attribute.

object.__match_args__[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__match_args__ "Link to this definition")

This class variable can be assigned a tuple of strings. When this class is used in a class pattern with positional arguments, each positional argument will be converted into a keyword argument, using the corresponding value in ___match_args___ as the keyword. The absence of this attribute is equivalent to setting it to `()`.

For example, if `MyClass.__match_args__` is `("left", "center", "right")` that means that `case MyClass(x, y)` is equivalent to `case MyClass(left=x, center=y)`. Note that the number of arguments in the pattern must be smaller than or equal to the number of elements in ___match_args___; if it is larger, the pattern match attempt will raise a [`TypeError`](https://docs.python.org/ko/3.12/library/exceptions.html#TypeError "TypeError").

Added in version 3.10.

더 보기

[**PEP 634**](https://peps.python.org/pep-0634/) - Structural Pattern Matching

The specification for the Python `match` statement.

### 3.3.11. Emulating buffer types[](https://docs.python.org/ko/3.12/reference/datamodel.html#emulating-buffer-types "Link to this heading")

The [buffer protocol](https://docs.python.org/ko/3.12/c-api/buffer.html#bufferobjects) provides a way for Python objects to expose efficient access to a low-level memory array. This protocol is implemented by builtin types such as [`bytes`](https://docs.python.org/ko/3.12/library/stdtypes.html#bytes "bytes") and [`memoryview`](https://docs.python.org/ko/3.12/library/stdtypes.html#memoryview "memoryview"), and third-party libraries may define additional buffer types.

While buffer types are usually implemented in C, it is also possible to implement the protocol in Python.

object.__buffer__(_self_, _flags_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__buffer__ "Link to this definition")

Called when a buffer is requested from _self_ (for example, by the [`memoryview`](https://docs.python.org/ko/3.12/library/stdtypes.html#memoryview "memoryview") constructor). The _flags_ argument is an integer representing the kind of buffer requested, affecting for example whether the returned buffer is read-only or writable. [`inspect.BufferFlags`](https://docs.python.org/ko/3.12/library/inspect.html#inspect.BufferFlags "inspect.BufferFlags") provides a convenient way to interpret the flags. The method must return a [`memoryview`](https://docs.python.org/ko/3.12/library/stdtypes.html#memoryview "memoryview") object.

object.__release_buffer__(_self_, _buffer_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__release_buffer__ "Link to this definition")

Called when a buffer is no longer needed. The _buffer_ argument is a [`memoryview`](https://docs.python.org/ko/3.12/library/stdtypes.html#memoryview "memoryview") object that was previously returned by [`__buffer__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__buffer__ "object.__buffer__"). The method must release any resources associated with the buffer. This method should return `None`. Buffer objects that do not need to perform any cleanup are not required to implement this method.

Added in version 3.12.

더 보기

[**PEP 688**](https://peps.python.org/pep-0688/) - Making the buffer protocol accessible in Python

Introduces the Python `__buffer__` and `__release_buffer__` methods.

[`collections.abc.Buffer`](https://docs.python.org/ko/3.12/library/collections.abc.html#collections.abc.Buffer "collections.abc.Buffer")

ABC for buffer types.

### 3.3.12. 특수 메서드 조회[](https://docs.python.org/ko/3.12/reference/datamodel.html#special-method-lookup "Link to this heading")

사용자 정의 클래스의 경우, 묵시적인 특수 메서드의 호출은 객체의 인스턴스 딕셔너리가 아닌 객체의 형에 정의되어 있을 때만 올바르게 동작함이 보장됩니다. 이런 동작은 다음과 같은 코드가 예외를 일으키는 원인입니다:

```python
>>> class C:
...     pass
...
>>> c = C()
>>> c.__len__ = lambda: 5
>>> len(c)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'C' has no len()
```

The rationale behind this behaviour lies with a number of special methods such as [`__hash__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__hash__ "object.__hash__") and [`__repr__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__repr__ "object.__repr__") that are implemented by all objects, including type objects. If the implicit lookup of these methods used the conventional lookup process, they would fail when invoked on the type object itself:

```python
>>> 1 .__hash__() == hash(1)
True
>>> int.__hash__() == hash(int)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: descriptor '__hash__' of 'int' object needs an argument
```

클래스의 연결되지 않은 메서드를 호출하려는 이런 식의 잘못된 시도는 종종 ‘메타 클래스 혼란(metaclass confusion)’ 이라고 불리고, 특수 메서드를 조회할 때 인스턴스를 우회하는 방법으로 피할 수 있습니다.

```python
>>> type(1).__hash__(1) == hash(1)
True
>>> type(int).__hash__(int) == hash(int)
True
```

In addition to bypassing any instance attributes in the interest of correctness, implicit special method lookup generally also bypasses the [`__getattribute__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getattribute__ "object.__getattribute__") method even of the object’s metaclass:

```python
>>> class Meta(type):
...     def __getattribute__(*args):
...         print("Metaclass getattribute invoked")
...         return type.__getattribute__(*args)
...
>>> class C(object, metaclass=Meta):
...     def __len__(self):
...         return 10
...     def __getattribute__(*args):
...         print("Class getattribute invoked")
...         return object.__getattribute__(*args)
...
>>> c = C()
>>> c.__len__()                 # Explicit lookup via instance
Class getattribute invoked
10
>>> type(c).__len__(c)          # Explicit lookup via type
Metaclass getattribute invoked
10
>>> len(c)                      # Implicit lookup
10
```

Bypassing the [`__getattribute__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__getattribute__ "object.__getattribute__") machinery in this fashion provides significant scope for speed optimisations within the interpreter, at the cost of some flexibility in the handling of special methods (the special method _must_ be set on the class object itself in order to be consistently invoked by the interpreter).

## 3.4. 코루틴(Coroutines)[](https://docs.python.org/ko/3.12/reference/datamodel.html#coroutines "Link to this heading")

### 3.4.1. 어웨이터블 객체(Awaitable Objects)[](https://docs.python.org/ko/3.12/reference/datamodel.html#awaitable-objects "Link to this heading")

An [awaitable](https://docs.python.org/ko/3.12/glossary.html#term-awaitable) object generally implements an [`__await__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__await__ "object.__await__") method. [Coroutine objects](https://docs.python.org/ko/3.12/glossary.html#term-coroutine) returned from [`async def`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#async-def) functions are awaitable.

참고

 

The [generator iterator](https://docs.python.org/ko/3.12/glossary.html#term-generator-iterator) objects returned from generators decorated with [`types.coroutine()`](https://docs.python.org/ko/3.12/library/types.html#types.coroutine "types.coroutine") are also awaitable, but they do not implement [`__await__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__await__ "object.__await__").

object.__await__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__await__ "Link to this definition")

[이터레이터](https://docs.python.org/ko/3.12/glossary.html#term-iterator) 를 돌려줘야 합니다. [어웨이터블](https://docs.python.org/ko/3.12/glossary.html#term-awaitable) 객체를 구현하기 위해 사용되어야 합니다. 예를 들어, [`asyncio.Future`](https://docs.python.org/ko/3.12/library/asyncio-future.html#asyncio.Future "asyncio.Future") 는 [`await`](https://docs.python.org/ko/3.12/reference/expressions.html#await) 표현식과 호환되기 위해 이 메서드를 구현합니다.

참고

 

The language doesn’t place any restriction on the type or value of the objects yielded by the iterator returned by `__await__`, as this is specific to the implementation of the asynchronous execution framework (e.g. [`asyncio`](https://docs.python.org/ko/3.12/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.")) that will be managing the [awaitable](https://docs.python.org/ko/3.12/glossary.html#term-awaitable) object.

Added in version 3.5.

더 보기

 

[**PEP 492**](https://peps.python.org/pep-0492/) 가 어웨이터블 객체에 대한 더 자세한 정보를 포함하고 있습니다.

### 3.4.2. 코루틴 객체(Coroutine Objects)[](https://docs.python.org/ko/3.12/reference/datamodel.html#coroutine-objects "Link to this heading")

[Coroutine objects](https://docs.python.org/ko/3.12/glossary.html#term-coroutine) are [awaitable](https://docs.python.org/ko/3.12/glossary.html#term-awaitable) objects. A coroutine’s execution can be controlled by calling [`__await__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__await__ "object.__await__") and iterating over the result. When the coroutine has finished executing and returns, the iterator raises [`StopIteration`](https://docs.python.org/ko/3.12/library/exceptions.html#StopIteration "StopIteration"), and the exception’s [`value`](https://docs.python.org/ko/3.12/library/exceptions.html#StopIteration.value "StopIteration.value") attribute holds the return value. If the coroutine raises an exception, it is propagated by the iterator. Coroutines should not directly raise unhandled [`StopIteration`](https://docs.python.org/ko/3.12/library/exceptions.html#StopIteration "StopIteration") exceptions.

코루틴은 다음에 나열하는 메서드들 또한 갖고 있는데, 제너레이터([제너레이터-이터레이터 메서드](https://docs.python.org/ko/3.12/reference/expressions.html#generator-methods) 를 보십시오)의 것들과 닮았습니다. 하지만, 제너레이터와는 달리, 코루틴은 이터레이션을 직접 지원하지는 않습니다.

버전 3.5.2에서 변경: 코루틴을 두 번 await 하면 [`RuntimeError`](https://docs.python.org/ko/3.12/library/exceptions.html#RuntimeError "RuntimeError") 를 일으킵니다.

coroutine.send(_value_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#coroutine.send "Link to this definition")

Starts or resumes execution of the coroutine. If _value_ is `None`, this is equivalent to advancing the iterator returned by [`__await__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__await__ "object.__await__"). If _value_ is not `None`, this method delegates to the [`send()`](https://docs.python.org/ko/3.12/reference/expressions.html#generator.send "generator.send") method of the iterator that caused the coroutine to suspend. The result (return value, [`StopIteration`](https://docs.python.org/ko/3.12/library/exceptions.html#StopIteration "StopIteration"), or other exception) is the same as when iterating over the `__await__()` return value, described above.

coroutine.throw(_value_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#coroutine.throw "Link to this definition")

coroutine.throw(_type_[, _value_[, _traceback_]])

Raises the specified exception in the coroutine. This method delegates to the [`throw()`](https://docs.python.org/ko/3.12/reference/expressions.html#generator.throw "generator.throw") method of the iterator that caused the coroutine to suspend, if it has such a method. Otherwise, the exception is raised at the suspension point. The result (return value, [`StopIteration`](https://docs.python.org/ko/3.12/library/exceptions.html#StopIteration "StopIteration"), or other exception) is the same as when iterating over the [`__await__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__await__ "object.__await__") return value, described above. If the exception is not caught in the coroutine, it propagates back to the caller.

버전 3.12에서 변경: The second signature (type[, value[, traceback]]) is deprecated and may be removed in a future version of Python.

coroutine.close()[](https://docs.python.org/ko/3.12/reference/datamodel.html#coroutine.close "Link to this definition")

코루틴이 자신을 정리하고 종료하도록 만듭니다. 만약 코루틴이 일시 중지 중이면, 이 메서드는 먼저 코루틴이 일시 중지되도록 한 이터레이터의 [`close()`](https://docs.python.org/ko/3.12/reference/expressions.html#generator.close "generator.close") 메서드로 위임합니다(그런 메서드를 가지는 경우). 그런 다음 일시 중지지점에서 [`GeneratorExit`](https://docs.python.org/ko/3.12/library/exceptions.html#GeneratorExit "GeneratorExit") 를 발생시키는데, 코루틴이 즉시 자신을 정리하도록 만듭니다. 마지막으로 코루틴에 실행을 종료했다고 표시하는데, 아직 시작하지조차 않았을 때도 그렇다.

코루틴 객체가 파괴될 때는 위의 프로세스에 따라 자동으로 닫힙니다(closed).

### 3.4.3. 비동기 이터레이터(Asynchronous Iterators)[](https://docs.python.org/ko/3.12/reference/datamodel.html#asynchronous-iterators "Link to this heading")

_비동기 이터레이터_ 는 자신의 `__anext__` 메서드에서 비동기 코드를 호출할 수 있습니다.

비동기 이터레이터는 [`async for`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#async-for) 문에서 사용될 수 있습니다.

object.__aiter__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__aiter__ "Link to this definition")

_비동기 이터레이터_ 객체를 돌려줘야 합니다.

object.__anext__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__anext__ "Link to this definition")

이터레이터의 다음 값을 주는 _어웨이터블_ 을 돌려줘야 합니다. 이터레이션이 끝나면 [`StopAsyncIteration`](https://docs.python.org/ko/3.12/library/exceptions.html#StopAsyncIteration "StopAsyncIteration") 에러를 일으켜야 합니다.

비동기 이터러블 객체의 예:

class Reader:
    async def readline(self):
        ...

    def __aiter__(self):
        return self

    async def __anext__(self):
        val = await self.readline()
        if val == b'':
            raise StopAsyncIteration
        return val

Added in version 3.5.

버전 3.7에서 변경: Prior to Python 3.7, [`__aiter__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__aiter__ "object.__aiter__") could return an _awaitable_ that would resolve to an [asynchronous iterator](https://docs.python.org/ko/3.12/glossary.html#term-asynchronous-iterator).

Starting with Python 3.7, [`__aiter__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__aiter__ "object.__aiter__") must return an asynchronous iterator object. Returning anything else will result in a [`TypeError`](https://docs.python.org/ko/3.12/library/exceptions.html#TypeError "TypeError") error.

### 3.4.4. 비동기 컨텍스트 관리자[](https://docs.python.org/ko/3.12/reference/datamodel.html#asynchronous-context-managers "Link to this heading")

_비동기 컨텍스트 관리자(asynchronous context manager)_ 는 `__aenter__` 와 `__aexit__` 메서드에서 실행을 일시 중지할 수 있는 _컨텍스트 관리자_ 입니다.

비동기 컨텍스트 관리자는 [`async with`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#async-with) 문에서 사용될 수 있습니다.

object.__aenter__(_self_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__aenter__ "Link to this definition")

Semantically similar to [`__enter__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__enter__ "object.__enter__"), the only difference being that it must return an _awaitable_.

object.__aexit__(_self_, _exc_type_, _exc_value_, _traceback_)[](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__aexit__ "Link to this definition")

Semantically similar to [`__exit__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__exit__ "object.__exit__"), the only difference being that it must return an _awaitable_.

비동기 컨텍스트 관리자 클래스의 예:

class AsyncContextManager:
    async def __aenter__(self):
        await log('entering context')

    async def __aexit__(self, exc_type, exc, tb):
        await log('exiting context')

Added in version 3.5.



[바이너리 데이터 서비스 — Python 3.12.5 문서](https://docs.python.org/ko/3/library/binary.html)

---
## 참조

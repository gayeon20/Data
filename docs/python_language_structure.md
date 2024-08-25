---
title: "[Python] 언어 구조 (Language Structure)"
excerpt: 
categories:
  - Python
tags:
  - Python
  - Language-Structure
last_modified_at: 2024-04-11T15:10:55+09:00
link: 
상위 항목: "[[python_home|파이썬 (Python)]]"
---

**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

---
- 파이썬 프로그램은 _파서(parser)_ 에 의해 읽힙니다. 파서의 입력은 _어휘 분석기(lexical analyzer)_ 가 만들어내는 _토큰(token)_ 들의 스트림입니다. 이 장에서는 어휘 분석기가 어떻게 파일을 토큰들로 분해하는지 설명합니다.
- 파이썬은 프로그램 텍스트를 유니코드 코드값으로 읽습니다; 소스 파일의 인코딩은 인코딩 선언을 통해 지정될 수 있고, 기본값은 UTF-8입니다. 자세한 내용은 [**PEP 3120**](https://peps.python.org/pep-3120/) 에 나옵니다. 소스 파일을 디코딩할 수 없을 때는 [`SyntaxError`](https://docs.python.org/ko/3.12/library/exceptions.html#SyntaxError "SyntaxError") 가 발생합니다.

## 줄 구조(Line structure)

파이썬 프로그램은 여러 개의 _논리적인 줄(logical lines)_ 들로 나뉩니다.

### 논리적인 줄

- 논리적인 줄의 끝은 NEWLINE 토큰으로 표현됩니다. 문법이 허락하지 않는 이상 (예를 들어 복합문에서 문장들 사이) 문장은 논리적인 줄 간의 경계를 가로지를 수 없습니다. 논리적인 줄은 명시적이거나 묵시적인 _줄 결합(line joining)_ 규칙에 따라 하나 이상의 _물리적인 줄(physical lines)_ 들로 구성됩니다.

### 물리적인 줄

- 물리적인 줄은 줄의 끝을 나타내는 시퀀스로 끝나는 문자들의 시퀀스입니다. 소스 파일과 문자열에는 플랫폼들의 표준 줄 종료 시퀀스들이 모두 사용될 수 있습니다 - ASCII LF (개행문자)를 사용하는 유닉스 형, ASCII 시퀀스 CR LF(캐리지 리턴 다음에 오는 개행 문자)를 사용하는 윈도우 형, ASCII CR(캐리지 리턴)을 사용하는 예전의 매킨토시 형. 이 형태들은 플랫폼의 종류와 관계없이 동등하게 사용할 수 있습니다. 입력의 끝은 마지막 물리적인 줄의 묵시적 종결자 역할을 합니다.
- 파이썬을 내장할 때는, 소스 코드 문자열은 반드시 줄 종료 문자에 표준 C 관행(ASCII LF를 표현하는 `\n` 문자로 줄이 종료됩니다)을 적용해서 파이썬 API로 전달되어야 합니다.

### 주석
- 주석은 문자열 리터럴에 포함되지 않는 해시 문자(`#`)로 시작하고 물리적인 줄의 끝에서 끝납니다. 묵시적인 줄 결합 규칙이 유효하지 않은 이상, 주석은 논리적인 줄을 종료시킵니다. 주석은 문법이 무시합니다.

### 인코딩 선언

- 파이썬 스크립트의 첫 번 째나 두 번째 줄에 있는 주석이 정규식 `coding[=:]\s*([-\w.]+)` 과 매치되면, 이 주석은 인코딩 선언으로 처리됩니다. 이 정규식의 첫 번째 그룹은 소스 코드 파일의 인코딩 이름을 지정합니다. 인코딩 선언은 줄 전체에 홀로 나와야 합니다. 만약 두 번째 줄이라면, 첫 번째 줄 역시 주석만 있어야 합니다. 인코딩 선언의 권장 형태는 두 개입니다. 하나는

```python
# -*- coding: <encoding-name> -*-
```

인데 GNU Emacs에서도 인식됩니다. 다른 하나는

```python
# vim:fileencoding=<encoding-name>
```

인데 Bram Moolenaar 의 VIM에서 인식됩니다.

- 인코딩 선언을 찾을 수 없는 경우 기본 인코딩은 UTF-8입니다. 파일의 암시적 또는 명시적 인코딩이 UTF-8인 경우 구문 오류가 아닌 초기 UTF-8 바이트 순서 표시(b'xefxbbxbf')가 무시됩니다.
- 인코딩이 선언된 경우 인코딩 이름은 파이썬에서 인식되어야 합니다([표준 인코딩](https://docs.python.org/ko/3.12/library/codecs.html#standard-encodings) 참조). 인코딩은 문자열 리터럴, 주석 및 식별자를 포함한 모든 어휘 분석에 사용됩니다.

### 명시적인 줄 결합
- 둘 이상의 물리적인 줄은 역 슬래시 문자(`\`)를 사용해서 논리적인 줄로 결합할 수 있습니다: 물리적인 줄이 문자열 리터럴이나 주석의 일부가 아닌 역 슬래시 문자로 끝나면, 역 슬래시와 뒤따르는 개행 문자가 제거된 채로, 현재 만들어지고 있는 논리적인 줄에 합쳐집니다. 예를 들어:

```python
if 1900 < year < 2100 and 1 <= month <= 12 \
   and 1 <= day <= 31 and 0 <= hour < 24 \
   and 0 <= minute < 60 and 0 <= second < 60:   # Looks like a valid date
        return 1
```

- 역 슬래시로 끝나는 줄은 주석이 포함될 수 없습니다. 역 슬래시는 주석을 결합하지 못합니다. 역 슬래시는 문자열 리터럴을 제외한 어떤 토큰도 결합하지 못합니다 (즉, 문자열 리터럴 이외의 어떤 토큰도 역 슬래시를 사용해서 두 줄에 나누어 기록할 수 없습니다.). 문자열 리터럴 밖에 있는 역 슬래시가 앞에서 언급한 장소 이외의 곳에 등장하는 것은 문법에 어긋납니다.

### 묵시적인 줄 결합

- 괄호(`()`), 대괄호(`[]`), 중괄호(`{}`)가 사용되는 표현은 역 슬래시 없이도 여러 개의 물리적인 줄로 나눌 수 있습니다. 예를 들어:

```python
month_names = ['Januari', 'Februari', 'Maart',      # These are the
               'April',   'Mei',      'Juni',       # Dutch names
               'Juli',    'Augustus', 'September',  # for the months
               'Oktober', 'November', 'December']   # of the year
```

- 묵시적으로 이어지는 줄들은 주석을 포함할 수 있습니다. 이어지는 줄들의 들여쓰기는 중요하지 않습니다. 중간에 빈 줄이 들어가도 됩니다. 묵시적으로 줄 결합하는 줄 들 간에는 NEWLINE 토큰이 만들어지지 않습니다. 묵시적으로 이어지는 줄들은 삼중 따옴표 된 문자열들에서도 등장할 수 있는데 (아래를 보라), 이 경우는 주석이 포함될 수 없습니다.

### 빈 줄

- 스페이스, 탭, 폼 피드(formfeed) 와 주석만으로 구성된 논리적인 줄은 무시됩니다. (즉 NEWLINE 토큰이 만들어지지 않습니다.) 대화형으로 문장이 입력되는 도중에는 빈 줄의 처리가 REPL 구현에 따라 달라질 수 있습니다. 표준 대화형 인터프리터에서는, 완전히 빈 줄(즉 공백이나 주석조차 없는 것)은 다중 행 문장을 종료시킵니다.

### 들여쓰기

- 논리적인 줄의 제일 앞에 오는 공백(스페이스와 탭)은 줄의 들여쓰기 수준을 계산하는 데 사용되고, 이는 다시 문장들의 묶음을 결정하는 데 사용되게 됩니다.
- 탭은 (왼쪽에서 오른쪽으로) 1~8개의 스페이스로 변환되는데, 치환된 후의 총 스페이스 문자 수가 8의 배수가 되도록 맞춥니다. (유닉스에서 사용되는 규칙에 맞추려는 것입니다.) 첫 번째 비 공백 문자 앞에 나오는 공백의 총수가 줄의 들여쓰기를 결정합니다. 들여쓰기는 역 슬래시를 사용해서 여러 개의 물리적인 줄로 나눠질 수 없습니다; 첫 번째 역 슬래시 이전의 공백이 들여쓰기를 결정합니다.
- 소스 파일이 탭과 스페이스를 섞어 쓰는 경우, 탭이 몇 개의 스페이스에 해당하는지에 따라 다르게 해석될 수 있으면 [`TabError`](https://docs.python.org/ko/3.12/library/exceptions.html#TabError "TabError") 를 일으킵니다.

> **크로스-플랫폼 호환성 유의 사항:** UNIX 이외의 플랫폼에서 편집기들이 동작하는 방식 때문에, 하나의 파일 내에서 들여쓰기를 위해 탭과 스페이스를 섞어 쓰는 것은 현명한 선택이 아닙니다. 다른 플랫폼들에서는 최대 들여쓰기 수준에 제한이 있을 수도 있다는 점도 주의해야 합니다.

- 폼 피드 문자는 줄의 처음에 나올 수 있습니다; 앞서 설명한 들여쓰기 수준 계산에서는 무시됩니다. 페이지 넘김 문자 앞에 공백이나 탭이 있는 경우는 정의되지 않은 효과를 줄 수 있습니다 (가령, 스페이스 수가 0으로 초기화될 수 있습니다).
- 연속된 줄의 들여쓰기 수준은, 스택을 사용해서, 다음과 같은 방법으로 INDENT와 DEDENT 토큰을 만드는 데 사용됩니다.
- 파일의 첫 줄을 읽기 전에 `0` 하나를 스택에 넣습니다(push); 이 값은 다시 꺼내는(pop) 일이 없습니다. 스택에 넣는 값은 항상 스택의 아래에서 위로 올라갈 때 단조 증가합니다. 각 논리적인 줄의 처음에서 줄의 들여쓰기 수준이 스택의 가장 위에 있는 값과 비교됩니다. 같다면 아무런 일도 일어나지 않습니다. 더 크다면 그 값을 스택에 넣고 하나의 INDENT 토큰을 만듭니다. 더 작다면 이 값은 스택에 있는 값 중 하나여야만 합니다. 이 값보다 큰 모든 스택의 값들을 꺼내고(pop), 꺼낸 횟수만큼의 DEDENT 토큰을 만듭니다. 파일의 끝에서, 스택에 남아있는 0보다 큰 값의 개수만큼 DEDENT 토큰을 만듭니다. 여기에 (혼란스럽다 할지라도) 올바르게 들여쓰기 된 파이썬 코드 조각이 있습니다:

```python
def perm(l):
        # Compute the list of all permutations of l
    if len(l) <= 1:
                  return [l]
    r = []
    for i in range(len(l)):
             s = l[:i] + l[i+1:]
             p = perm(s)
             for x in p:
              r.append(l[i:i+1] + x)
    return r
```

다음 예는 여러 가지 들여쓰기 에러를 보여줍니다:

```python
 def perm(l):                       # error: first line indented
for i in range(len(l)):             # error: not indented
    s = l[:i] + l[i+1:]
        p = perm(l[:i] + l[i+1:])   # error: unexpected indent
        for x in p:
                r.append(l[i:i+1] + x)
            return r                # error: inconsistent dedent
```

> 사실, 처음 세 개의 에러는 파서가 감지합니다. 단지 마지막 에러만 어휘 분석기가 감지합니다. — `return r` 의 들여쓰기가 스택에 있는 값과 일치하지 않습니다.

### 토큰 사이의 공백

- 논리적인 줄의 처음과 문자열 리터럴을 제외하고, 공백 문자인 스페이스, 탭, 폼 피드는 토큰을 분리하기 위해 섞어 쓸 수 있습니다. 두 토큰을 붙여 쓸 때 다른 토큰으로 해석될 수 있는 경우만 토큰 사이에 공백이 필요합니다. (예를 들어, ab 는 하나의 토큰이지만, a b 는 두 개의 토큰입니다.)

## 다른 토큰들

- NEWLINE, INDENT, DEDENT 와는 별도로, 다음과 같은 유형의 토큰들이 존재합니다: 
  
  _식별자(identifier)_, _키워드(keyword)_, _리터럴(literal)_, _연산자(operator)_, _구분자(delimiter)_. 
  
- (앞에서 살펴본 줄 종료 이외의) 공백 문자들은 토큰이 아니지만, 토큰을 분리하는 역할을 담당합니다. 모호할 경우, 왼쪽에서 오른쪽으로 읽을 때, 하나의 토큰은 올바르고 가능한 한 최대 길이의 문자열로 구성되는 것을 선호합니다.

## 식별자와 키워드

- 식별자 (_이름(name)_ 이라고도 합니다) 은 다음과 같은 어휘 정의로 기술됩니다.
- 파이썬에서 식별자의 문법은 유니코드 표준 부속서 UAX-31 에 기반을 두는데, 여기에 덧붙이거나 바꾼 내용은 아래에서 정의합니다. 좀 더 상세한 내용은 [**PEP 3131**](https://peps.python.org/pep-3131/) 에서 찾을 수 있습니다.
- ASCII 범위 (U+0001..U+007F) 내에서, 올바른 식별자 문자는 파이썬 2.x 와 같습니다: `A` 에서 `Z` 범위의 대문자와 소문자, 밑줄 `_`, 첫 문자를 제외하고, 숫자 `0` 에서 `9`.
- 파이썬 3.0은 ASCII 범위 밖의 문자들을 도입합니다 ([**PEP 3131**](https://peps.python.org/pep-3131/) 참조). 이 문자들의 경우, [`unicodedata`](https://docs.python.org/ko/3.12/library/unicodedata.html#module-unicodedata "unicodedata: Access the Unicode Database.") 모듈에 포함된 버전의 유니코드 문자 데이터베이스에 따라 분류됩니다.
- 식별자는 길이에 제한이 없고, 케이스(case)는 구분됩니다.

```
identifier   ::=  xid_start xid_continue*
id_start     ::=  <all characters in general categories Lu, Ll, Lt, Lm, Lo, Nl, the underscore, and characters with the Other_ID_Start property>
id_continue  ::=  <all characters in id_start, plus characters in the categories Mn, Mc, Nd, Pc and others with the Other_ID_Continue property>
xid_start    ::=  <all characters in id_start whose NFKC normalization is in "id_start xid_continue*">
xid_continue ::=  <all characters in id_continue whose NFKC normalization is in "id_continue*">
```

- 위에서 언급한 유니코드 카테고리 코드들의 의미는 이렇습니다:
	- _Lu_ - uppercase letters
	- _Ll_ - lowercase letters
	- _Lt_ - titlecase letters
	- _Lm_ - modifier letters
	- _Lo_ - other letters
	- _Nl_ - letter numbers
	- _Mn_ - nonspacing marks
	- _Mc_ - spacing combining marks
	- _Nd_ - decimal numbers
	- _Pc_ - connector punctuations
	- _Other_ID_Start_ - explicit list of characters in [PropList.txt](https://www.unicode.org/Public/15.0.0/ucd/PropList.txt) to support backwards compatibility
	- _Other_ID_Continue_ - 마찬가지
- 모든 식별자는 파서에 의해 NFKC 정규화 형식으로 변환되고, 식별자의 비교는 NFKC 에 기반을 둡니다.
- 유니코드 15.0.0에 유효한 모든 식별자 문자를 나열하는 비규격 HTML 파일은 [https://www.unicode.org/Public/15.0.0/ucd/Derive]에서 찾을 수 있습니다.dCoreProperties.txt](https://www.unicode.org/Public/15.0.0/ucd/DerivedCoreProperties.txt)

### 키워드

- 다음 식별자들은 예약어, 또는 언어의 키워드, 로 사용되고, 일반적인 식별자로 사용될 수 없습니다. 여기 쓰여 있는 것과 정확히 같게 사용되어야 합니다:

```python
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

### 소프트 키워드 (Soft Keywords)
> 버전 3.10에 추가되었습니다.

- 일부 식별자는 특정 상황에서만 예약되어 있습니다. 이를 _소프트 키워드_ 라고 합니다. 식별자 `match`, `case`, `type`, `_`는 특정 문맥에서 구문론적으로 키워드 역할을 할 수 있지만, 이 구분은 토큰화할 때가 아니라 파서 수준에서 이루어집니다.
- 소프트 키워드로서 이러한 이름을 식별자 이름으로 사용하는 기존 코드와의 호환성을 유지하면서 문법에 사용할 수 있습니다.
- `match`, `case`, `_`는 [`match`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#match) 문에서 사용됩니다. `type`은 [`type`](https://docs.python.org/ko/3.12/reference/simple_stmts.html#type) 문에서 사용됩니다.

> 버전 3.12에서 변경: `type`은 이제 소프트 키워드입니다.


### 식별자의 예약 영역
- (키워드와는 별개로) 어떤 부류의 식별자들은 특별한 의미가 있습니다. 이 부류의 식별자들은 시작과 끝의 밑줄 문자 패턴으로 구분됩니다:

`_*`
- `from module import *`에서 가져올 수 없습니다.

`_`
- [`match`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#match) 문 내의 `case` 패턴에서 `_`는 [와일드카드](https://docs.python.org/ko/3.12/reference/compound_stmts.html#wildcard-patterns)를 나타내는 [소프트 키워드](https://docs.python.org/ko/3.12/reference/lexical_analysis.html#soft-keywords)입니다.
- 이와 별도로 대화형 인터프리터는 마지막 평가의 결과를 `_` 변수에 저장합니다. (이 변수는 [`builtins`](https://docs.python.org/ko/3.12/library/builtins.html#module-builtins "builtins")에 저장됩니다: 내장 네임스페이스를 제공하는 모듈.") 모듈에 `print`와 같은 내장 함수와 함께 저장됩니다.)
- 다른 곳에서는 `_`가 일반 식별자입니다. "특별한" 항목의 이름을 지정하는 데 자주 사용되지만 파이썬 자체에는 특별하지 않습니다.

> 이름 `_` 은 종종 국제화(internationalization)와 관련되어 사용됩니다. 이 관례에 관해서는 [`gettext`](https://docs.python.org/ko/3.12/library/gettext.html#module-gettext "gettext: Multilingual internationalization services.") 모듈의 문서를 참조하십시오.

- 사용하지 않는 변수에도 일반적으로 사용됩니다.

`__*__`
- 시스템 정의 이름, 비공식적으로 “던더(dunder)” 이름이라고 알려졌습니다. 이 이름들은 인터프리터와 그 구현(표준 라이브러리를 포함합니다)이 정의합니다. 현재 정의된 시스템 이름은 [특수 메서드 이름들](https://docs.python.org/ko/3.12/reference/datamodel.html#specialnames) 섹션과 그 외의 곳에서 논의됩니다. 파이썬의 미래 버전에서는 더 많은 것들이 정의될 가능성이 큽니다. 어떤 문맥에서건, 명시적으로 문서로 만들어진 사용법을 벗어나는 `__*__` 이름의 _모든_ 사용은, 경고 없이 손상될 수 있습니다.

`__*`
- 클래스-비공개 이름. 이 부류의 이름들을 클래스 정의 문맥에서 사용하면 뒤섞인 형태로 변형됩니다. 부모 클래스와 자식 클래스의 “비공개(private)” 어트리뷰트 간의 이름 충돌을 피하기 위함입니다. [식별자 (이름)](https://docs.python.org/ko/3.12/reference/expressions.html#atom-identifiers) 섹션을 보세요.

## 리터럴 (Literal)
- 리터럴(literal)은 몇몇 내장형들의 상숫값을 위한 표기법입니다.

### 문자열과 바이트열 리터럴

- 문자열 리터럴은 다음과 같은 어휘 정의로 기술됩니다:

```
stringliteral    ::=  [stringprefix](shortstring | longstring)
stringprefix     ::=  "r" | "u" | "R" | "U" | "f" | "F"
                      | "fr" | "Fr" | "fR" | "FR" | "rf" | "rF" | "Rf" | "RF"
shortstring      ::=  "'" shortstringitem* "'" | '"' shortstringitem* '"'
longstring       ::=  "'''" longstringitem* "'''" | '"""' longstringitem* '"""'
shortstringitem  ::=  shortstringchar | stringescapeseq
longstringitem   ::=  longstringchar | stringescapeseq
shortstringchar  ::=  <any source character except "\" or newline or the quote>
longstringchar   ::=  <any source character except "\">
stringescapeseq  ::=  "\" <any source character>
```

```
bytesliteral    ::=  bytesprefix (shortbytes | longbytes)
bytesprefix     ::=  "b" | "B" | "br" | "Br" | "bR" | "BR" | "rb" | "rB" | "Rb" | "RB"
shortbytes      ::=  "'" shortbytesitem* "'" | '"' shortbytesitem* '"'
longbytes       ::=  "'''" longbytesitem* "'''" | '"""' longbytesitem* '"""'
shortbytesitem  ::=  shortbyteschar | bytesescapeseq
longbytesitem   ::=  longbyteschar | bytesescapeseq
shortbyteschar  ::=  <any ASCII character except "\" or newline or the quote>
longbyteschar   ::=  <any ASCII character except "\">
bytesescapeseq  ::=  "\" <any ASCII character>
```

- 이러한 프로덕션에 표시되지 않은 한 가지 구문 제한은 [`stringprefix`](https://docs.python.org/ko/3.12/reference/lexical_analysis.html#grammar-token-python-grammar-stringprefix) 또는 [`bytesprefix`](https://docs.python.org/ko/3.12/reference/lexical_analysis.html#grammar-token-python-grammar-bytesprefix)와 나머지 리터럴 사이에 공백이 허용되지 않는다는 것입니다. 소스 문자 집합은 인코딩 선언에 의해 정의되며, 소스 파일에 인코딩 선언이 지정되지 않은 경우 UTF-8이 됩니다([인코딩 선언](https://docs.python.org/ko/3.12/reference/lexical_analysis.html#encodings) 섹션 참조).
- 일반 영어: 두 유형의 리터럴은 모두 일치하는 작은따옴표(`'`) 또는 큰따옴표(`"`)로 묶을 수 있습니다. 또한 일치하는 작은따옴표 또는 큰따옴표 3개로 묶을 수도 있습니다(일반적으로 _삼중 따옴표 문자열_ 이라고 함). 백슬래시(`\`) 문자는 이스케이프(`\n`) 시 '줄 바꿈'을 의미하는 `n`과 같은 평범한 문자에 특별한 의미를 부여하는 데 사용됩니다. 또한 개행, 백슬래시 자체 또는 따옴표 문자와 같이 특별한 의미를 갖는 문자를 이스케이프하는 데 사용할 수도 있습니다. 예시는 아래의 [이스케이프 시퀀스](https://docs.python.org/ko/3.12/reference/lexical_analysis.html#escape-sequences)를 참조하세요.
- 바이트열(bytes) 리터럴은 항상 `'b'` 나 `'B'` 를 앞에 붙입니다; [`str`](https://docs.python.org/ko/3.12/library/stdtypes.html#str "str") 형의 인스턴스 대신 [`bytes`](https://docs.python.org/ko/3.12/library/stdtypes.html#bytes "bytes") 형의 인스턴스를 만듭니다. 오직 ASCII 문자들만 포함할 수 있습니다. 코드값이 128보다 크거나 같은 값들은 반드시 이스케이핑으로 표현되어야 합니다.
- 문자열 리터럴과 바이트 리터럴 모두 선택적으로 문자 `'r'` 또는 `'R'`을 앞에 붙일 수 있으며, 이러한 구문을 각각 _원시 문자열 리터럴_ 및 _원시 바이트 리터럴_ 이라고 하며 백슬래시를 리터럴 문자로 취급합니다. 따라서 원시 문자열 리터럴에서 `'\U'` 및 `'\u'` 이스케이프는 특별히 처리되지 않습니다.

> 3.3 버전 추가: 날 바이트열 리터럴의 `'br'` 와 같은 의미가 있는 `'rb'` 접두어가 추가되었습니다.

- 파이썬 2.x 와 3.x 에서 동시에 지원하는 코드들의 유지보수를 단순화하기 위해 예전에 사용되던 유니코드 리터럴 (`u'value'`)이 다시 도입되었습니다. 자세한 정보는 [**PEP 414**](https://peps.python.org/pep-0414/) 에 나옵니다.
- `'f'` 나 `'F'` 를 접두어로 갖는 문자열 리터럴은 포맷 문자열 리터럴(_formatted string literal_)입니다; [f-strings](https://docs.python.org/ko/3.12/reference/lexical_analysis.html#f-strings) 을 보세요. `'f'` 는 `'r'` 과 결합할 수 있습니다, 하지만, `'b'` 나 `'u'` 와는 결합할 수 없습니다. 따라서 날 포맷 문자열은 가능하지만, 포맷 바이트열 리터럴은 불가능합니다.
- 삼중 따옴표 된 리터럴에서, 세 개의 이스케이핑 되지 않은 개행 문자와 따옴표가 허락됩니다 (그리고 유지됩니다). 예외는 한 줄에 세 개의 이스케이핑 되지 않은 따옴표가 나오는 것인데, 리터럴을 종료시킵니다. (“따옴표”는 리터럴을 시작하는데 사용한 문자입니다. 즉, `'` 나 `"`)

#### 이스케이프 시퀀스 (Escape sequences)

`'r'` 나 `'R'` 접두어가 붙지 않은 이상, 문자열과 바이트열 리터럴에 포함된 이스케이프 시퀀스는 표준 C에서 사용된 것과 비슷한 규칙으로 해석됩니다. 인식되는 이스케이프 시퀀스는 이렇습니다:

|이스케이프 시퀀스|의미|유의 사항|
|---|---|---|
|`\`<newline>|역 슬래시와 개행 문자가 무시됩니다|(1)|
|`\\`|역 슬래시 (`\`)||
|`\'`|작은따옴표 (`'`)||
|`\"`|큰따옴표 (`"`)||
|`\a`|ASCII 벨 (BEL)||
|`\b`|ASCII 백스페이스 (BS)||
|`\f`|ASCII 폼 피드 (FF)||
|`\n`|ASCII 라인 피드 (LF)||
|`\r`|ASCII 캐리지 리턴 (CR)||
|`\t`|ASCII 가로 탭 (TAB)||
|`\v`|ASCII 세로 탭 (VT)||
|`\_ooo_`|8진수 _ooo_ 로 지정된 문자|(2,4)|
|`\x_hh_`|16진수 _hh_ 로 지정된 문자|(3,4)|

문자열 리터럴에서만 인식되는 이스케이프 시퀀스는:

|이스케이프 시퀀스|의미|유의 사항|
|---|---|---|
|`\N{_name_}`|유니코드 데이터베이스에서 _name_ 이라고 이름 붙여진 문자|(5)|
|`\u_xxxx_`|16-bit 16진수 _xxxx_ 로 지정된 문자|(6)|
|`\U_xxxxxxxx_`|32-bit 16진수 _xxxxxxxx_ 로 지정된 문자|(7)|

유의 사항:

1. 줄 끝에 백슬래시를 추가하여 줄 바꿈을 무시할 수 있습니다:

```python
>>> 'This string will not include \
… backslashes or newline characters.'
'This string will not include backslashes or newline characters.'
```

[큰따옴표로 묶은 문자열](https://docs.python.org/ko/3.12/reference/lexical_analysis.html#strings) 또는 괄호와 [문자열 리터럴 연결](https://docs.python.org/ko/3.12/reference/lexical_analysis.html#string-concatenation)을 사용하여 동일한 결과를 얻을 수 있습니다.

2. 표준 C와 마찬가지로, 최대 세 개의 8진수가 허용됩니다.

> 버전 3.11에서 변경: `0o377`보다 큰 값을 가진 8진수 이스케이프는 [`DeprecationWarning`](https://docs.python.org/ko/3.12/library/exceptions.html#DeprecationWarning "DeprecationWarning")을 생성합니다..

> 버전 3.12에서 변경: `0o377`보다 큰 값을 가진 8진수 이스케이프는 [`구문 경고`](https://docs.python.org/ko/3.12/library/exceptions.html#SyntaxWarning "SyntaxWarning")를 생성합니다. 향후 파이썬 버전에서는 결국 [`구문 에러`](https://docs.python.org/ko/3.12/library/exceptions.html#SyntaxError "구문 에러")가 될 것입니다.

3. 표준 C와는 달리, 정확히 두 개의 16진수가 제공되어야 합니다.
4. 바이트열 리터럴에서, 16진수와 8진수 이스케이프는 지정된 값의 바이트를 표현합니다. 문자열 리터럴에서는, 이 이스케이프는 지정된 값의 유니코드 문자를 표현합니다.
5. 버전 3.3에서 변경: 별칭 [[1]](https://docs.python.org/ko/3.12/reference/lexical_analysis.html#id16) 지원이 추가되었습니다
6. 정확히 4개의 16진수를 필요로 합니다.
7. 이 방법으로 모든 유니코드를 인코딩할 수 있습니다. 정확히 8개의 16진수가 필요합니다.

- 표준 C와는 달리, 인식되지 않는 모든 이스케이프 시퀀스는 문자열에 변경되지 않은 상태로 남게 됩니다. 즉, _역 슬래시가 결과에 남게 됩니다_. (이 동작은 디버깅할 때 쓸모가 있습니다. 이스케이프 시퀀스가 잘못 입력되었을 때, 최종 결과에서 잘못된 부분을 쉽게 인지할 수 있습니다.) 문자열 리터럴에서만 인식되는 이스케이프 시퀀스가, 바이트열 리터럴에서는 인식되지 않는 부류임에 주목하십시오.

> 버전 3.6에서 변경: 인식할 수 없는 이스케이프 시퀀스는 [`DeprecationWarning`](https://docs.python.org/ko/3.12/library/exceptions.html#DeprecationWarning "DeprecationWarning")을 생성합니다.

> 버전 3.12에서 변경: 인식할 수 없는 이스케이프 시퀀스는 [`구문 경고`](https://docs.python.org/ko/3.12/library/exceptions.html#SyntaxWarning "구문 경고")를 생성합니다. 향후 파이썬 버전에서는 결국 [`구문 에러`](https://docs.python.org/ko/3.12/library/exceptions.html#SyntaxError "구문 에러")가 될 것입니다.

- 날 리터럴에서 조차, 따옴표는 역 슬래시로 이스케이프 됩니다. 하지만 역 슬래시가 결과에 남게 됩니다; 예를 들어, `r"\""` 는 올바른 문자열 리터럴인데, 두 개의 문자가 들어있습니다: 역 슬래시와 큰따옴표; `r"\"` 는 올바른 문자열 리터럴이 아닙니다 (날 문자열조차 홀수개의 역 슬래시로 끝날 수 없습니다.). 좀 더 명확하게 말하자면, 날 리터럴은 하나의 역 슬래시로 끝날 수 없습니다(역 슬래시가 뒤에 오는 따옴표를 이스케이프 시키기 때문입니다). 역 슬래시와 바로 뒤에 오는 개행문자는 줄 결합이 _아니라_ 리터럴에 포함되는 두 개의 문자로 인식됨에 주의해야 합니다.

### 문자열 리터럴 이어붙이기

- 여러 개의 문자열이나 바이트열 리터럴을 (공백으로 분리해서) 여러 개 인접해서 나열하는 것이 허락되고, 그 의미는 이어붙인 것과 같습니다. 각 리터럴이 서로 다른 따옴표를 사용해도 됩니다. 그래서, `"hello" 'world'` 는 `"helloworld"` 와 동등합니다. 이 기능은 긴 문자열을 편의상 여러 줄로 나눌 때 필요한 역 슬래시를 줄여줍니다. 각 문자열 단위마다 주석을 붙이는 것도 가능합니다. 예를 들어:

```python
re.compile("[A-Za-z_]"       # letter or underscore
           "[A-Za-z0-9_]*"   # letter, digit or underscore
          )
```

- 이 기능이 문법 수준에서 정의되고는 있지만, 컴파일 시점에 구현됨에 주의해야 합니다. 실행 시간에 문자열 표현을 이어붙이기 위해서는 ‘+’ 연산자를 사용해야 합니다. 리터럴 이어붙이기가 요소별로 다른 따옴표를 사용할 수 있고 (날 문자열과 삼중 따옴표 문자열을 이어붙이는 것조차 가능합니다), 포맷 문자열 리터럴을 보통 문자열 리터럴과 이어붙일 수 있음에 유의해야 합니다.

### f-strings
> 3.6 버전 추가

- 포맷 문자열 리터럴(_formatted string literal_) 또는 _f-문자열 (f-string)_ 은 `'f'` 나 `'F'` 를 앞에 붙인 문자열 리터럴입니다. 이 문자열은 치환 필드를 포함할 수 있는데, 중괄호 `{}` 로 구분되는 표현식입니다. 다른 문자열 리터럴이 항상 상숫값을 갖지만, 포맷 문자열 리터럴은 실행시간에 계산되는 표현식입니다.
- 이스케이프 시퀀스는 일반 문자열 리터럴처럼 디코딩됩니다 (동시에 날 문자열인 경우는 예외입니다). 디코딩 후에 문자열의 내용은 다음과 같은 문법을 따릅니다:

```
f_string          ::=  (literal_char | "{{" | "}}" | replacement_field)*
replacement_field ::=  "{" f_expression ["="] ["!" conversion] [":" format_spec] "}"
f_expression      ::=  (conditional_expression | "*" or_expr)
                       ("," conditional_expression | "," "*" or_expr)* [","]
                     | yield_expression
conversion        ::=  "s" | "r" | "a"
format_spec       ::=  (literal_char | replacement_field)*
literal_char      ::=  <any code point except "{", "}" or NULL>
```

- 중괄호 바깥 부분은 일반 리터럴처럼 취급되는데, 이중 중괄호 `'{{'` 나 `'}}'` 가 대응하는 단일 중괄호로 치환된다는 점만 예외입니다. 하나의 여는 중괄호 `'{'` 는 치환 필드를 시작시키는데, 파이썬 표현식이 뒤따릅니다. 평가 후 표현식 텍스트와 해당 값을 모두 표시하려면 (디버깅에 유용합니다), 표현식 뒤에 등호 `=`를 추가할 수 있습니다. 느낌표 `!` 로 시작하는, 변환(conversion) 필드가 뒤따를 수 있습니다. 포맷 지정자(format specifier)도 덧붙일 수 있는데, 콜론 `':'` 으로 시작합니다. 치환 필드는 닫는 중괄호 `'}'` 로 끝납니다.
- 형식이 지정된 문자열 리터럴의 표현식은 몇 가지 예외를 제외하고 괄호로 둘러싸인 일반 파이썬 표현식처럼 취급됩니다. 빈 표현식은 허용되지 않으며, [`lambda`](https://docs.python.org/ko/3.12/reference/expressions.html#lambda)와 대입 표현식 `:=`는 모두 명시적 괄호로 둘러싸야 합니다. 각 표현식은 형식이 지정된 문자열 리터럴이 나타나는 컨텍스트에서 왼쪽에서 오른쪽 순서로 평가됩니다. 대체 표현식은 작은따옴표 및 큰따옴표로 묶인 f- 문자열 모두에 개행이 포함될 수 있으며 주석을 포함할 수 있습니다. 대체 필드 내부의 `#` 뒤에 오는 모든 것은 주석입니다(닫는 중괄호와 따옴표도 포함). 이 경우 대체 필드는 다른 줄에서 닫아야 합니다.

```python
>>> f"abc{a # This is a comment }"
… + 3}"
'abc5'
```

> 버전 3.7에서 변경: 파이썬 3.7 이전에는, 구현 문제로 인해 포맷 문자열 리터럴의 표현식에서 [`await`](https://docs.python.org/ko/3.12/reference/expressions.html#await) 표현식과 [`async for`](https://docs.python.org/ko/3.12/reference/compound_stmts.html#async-for) 절을 포함하는 컴프리헨션은 유효하지 않았습니다.

> 버전 3.12에서 변경: 파이썬 3.12 이전에는 f- 문자열 대체 필드 안에 주석이 허용되지 않았습니다.

- 등호 기호 `'='`이 제공되면, 출력에는 표현식 텍스트, `'='` 및 평가된 값이 포함됩니다. 여는 중괄호 `'{'` 뒤, 표현식 내, `'='` 뒤의 스페이스는 모두 출력에 유지됩니다. 기본적으로, `'='`은 포맷 지정자가 없는 한 표현식의 [`repr()`](https://docs.python.org/ko/3.12/library/functions.html#repr "repr")을 제공합니다. 포맷이 지정되면 변환 `'!r'`이 선언되지 않는 한 기본적으로 표현식의 [`str()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str "str")이 사용됩니다.

> 3.8 버전 추가: 등호 기호 `'='`.

- 변환(conversion)이 지정되면, 표현식의 결과가 포매팅 전에 변환됩니다. 변환 `'!s'` 는 결과에 [`str()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str "str") 을 호출하고, `'!r'` 은 [`repr()`](https://docs.python.org/ko/3.12/library/functions.html#repr "repr") 을 호출하고, `'!a'` 은 [`ascii()`](https://docs.python.org/ko/3.12/library/functions.html#ascii "ascii") 를 호출합니다.
- 그런 다음 결과는 [`format()`](https://docs.python.org/ko/3.12/library/functions.html#format "format") 프로토콜을 사용하여 포맷됩니다. 형식 지정자는 표현식 또는 변환 결과의 [`__format__()`](https://docs.python.org/ko/3.12/reference/datamodel.html#object.__format__ "object.__format__") 메서드에 전달됩니다. 형식 지정자를 생략하면 빈 문자열이 전달됩니다. 그러면 형식이 지정된 결과가 전체 문자열의 최종 값에 포함됩니다.
- 최상위 형식 지정자는 중첩된 대체 필드를 포함할 수 있습니다. 이러한 중첩된 필드에는 자체 변환 필드와 [형식 지정자](https://docs.python.org/ko/3.12/library/string.html#formatspec)가 포함될 수 있지만 더 깊게 중첩된 대체 필드는 포함되지 않을 수 있습니다. [형식 지정자 미니 언어](https://docs.python.org/ko/3.12/library/string.html#formatspec)는 [`str.format()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.format "str.format") 메서드에서 사용하는 것과 동일합니다.
- 포맷 문자열 리터럴을 이어붙일 수는 있지만, 치환 필드가 여러 리터럴로 쪼개질 수는 없습니다.
  포맷 문자열 리터럴의 예를 들면:

```python
>>> name = "Fred"
>>> f"He said his name is {name!r}."
"He said his name is 'Fred'."
>>> f"He said his name is {repr(name)}."  # repr() is equivalent to !r
"He said his name is 'Fred'."
>>> width = 10
>>> precision = 4
>>> value = decimal.Decimal("12.34567")
>>> f"result: {value:{width}.{precision}}"  # nested fields
'result:      12.35'
>>> today = datetime(year=2017, month=1, day=27)
>>> f"{today:%B %d, %Y}"  # using date format specifier
'January 27, 2017'
>>> f"{today=:%B %d, %Y}" # using date format specifier and debugging
'today=January 27, 2017'
>>> number = 1024
>>> f"{number:#0x}"  # using integer format specifier
'0x400'
>>> foo = "bar"
>>> f"{ foo = }" # preserves whitespace
" foo = 'bar'"
>>> line = "The mill's closed"
>>> f"{line = }"
'line = "The mill\'s closed"'
>>> f"{line = :20}"
"line = The mill's closed   "
>>> f"{line = !r:20}"
'line = "The mill\'s closed" '
```

- 대체 필드 내에서 외부 f- 문자열 인용 유형을 재사용하는 것은 허용됩니다:

```python
>>> a = dict(x=2)
>>> f"abc {a["x"]} def"
'abc 2 def'
```

> 버전 3.12에서 변경: Python 3.12 이전에는 대체 필드 내에서 동일한 인용 유형의 외부 f- 문자열을 재사용할 수 없었습니다.

- 백슬래시도 대체 필드에서 허용되며 다른 컨텍스트와 동일한 방식으로 평가됩니다:

```python
>>> a = ["a", "b", "c"]
>>> print(f"List a contains:\n{"\n".join(a)}")
List a contains:
a
b
c
```

> 버전 3.12에서 변경: 파이썬 3.12 이전에는 f- 문자열 대체 필드 내에서 백슬래시가 허용되지 않았습니다.

- 포맷 문자열 리터럴은 독스트링(docstring)으로 사용될 수 없습니다. 표현식이 전혀 없더라도 마찬가집니다.

```python
>>> def foo():
…     f"Not a docstring"
…
>>> foo.__doc__ is None
True
```

- 포맷 문자열 리터럴 추가에 대한 제안은 [**PEP 498**](https://peps.python.org/pep-0498/) 을 참조하고, 관련된 포맷 문자열 메커니즘을 사용하는 [`str.format()`](https://docs.python.org/ko/3.12/library/stdtypes.html#str.format "str.format") 도 살펴보는 것이 좋습니다.

### 숫자 리터럴

- 숫자 리터럴에는 정수, 부동 소수점 숫자, 허수의 세 가지 유형이 있습니다. 복소수 리터럴은 없습니다(복소수는 실수와 허수를 더하여 형성할 수 있습니다).
- 숫자 리터럴이 부호를 포함하지 않는 것에 주의해야 합니다; `-1` 과 같은 구문은 일 항 연산자 ‘`-`’ 과 리터럴 `1` 로 구성된 표현식입니다.

### 정수 리터럴

- 정수 리터럴은 다음과 같은 어휘 정의로 표현됩니다:

```
integer       ::=  decinteger | bininteger | octinteger | hexinteger
decinteger    ::=  nonzerodigit (["_"] digit)* | "0"+ (["_"] "0")*
bininteger    ::=  "0" ("b" | "B") (["_"] bindigit)+
octinteger    ::=  "0" ("o" | "O") (["_"] octdigit)+
hexinteger    ::=  "0" ("x" | "X") (["_"] hexdigit)+
nonzerodigit  ::=  "1"…"9"
digit         ::=  "0"…"9"
bindigit      ::=  "0" | "1"
octdigit      ::=  "0"…"7"
hexdigit      ::=  digit | "a"…"f" | "A"…"F"
```

- 가용한 메모리에 저장될 수 있는지와는 별개로 정수 리터럴의 길이에 제한은 없습니다.
- 밑줄은 리터럴의 숫자 값을 결정할 때 고려되지 않습니다. 가독성을 높이기 위해 숫자들을 무리 지을 때 쓸모가 있습니다. 밑줄은 숫자 사이나 `0x` 와 같은 진수 지정자(base specifier) 다음에 나올 수 있는데, 한 번에 하나만 사용될 수 있습니다.
- 0 이 아닌 10진수가 0으로 시작할 수 없음에 주의해야 합니다. 3.0 버전 이전의 파이썬에서 사용한 C 스타일의 8진수 리터럴과 혼동되는 것을 막기 위함입니다.
  정수 리터럴의 예를 들면:

```python
7     2147483647                        0o177    0b100110111
3     79228162514264337593543950336     0o377    0xdeadbeef
      100_000_000_000                   0b_1110_0101
```

> 버전 3.6에서 변경: 리터럴에서 숫자들의 그룹을 표현할 목적으로 밑줄을 허락합니다.

### 부동 소수점 리터럴 (Floating-point literals)

- 부동 소수점 리터럴은 다음 어휘 정의로 설명됩니다:

```
floatnumber   ::=  pointfloat | exponentfloat
pointfloat    ::=  [digitpart] fraction | digitpart "."
exponentfloat ::=  (digitpart | pointfloat) exponent
digitpart     ::=  digit (["_"] digit)*
fraction      ::=  "." digitpart
exponent      ::=  ("e" | "E") ["+" | "-"] digitpart
```

- 정수와 지수 부분은 항상 기수 10을 사용하여 해석된다는 점에 유의하세요. 예를 들어 `077e010`은 합법적이며 `77e10`과 같은 숫자를 나타냅니다. 부동 소수점 리터럴의 허용 범위는 구현에 따라 다릅니다. 정수 리터럴과 마찬가지로 밑줄은 숫자 그룹화에 지원됩니다.
  부동 소수점 리터럴의 몇 가지 예입니다:

```python
3.14    10.        1e100    3.14e-10    0e0    3.14_15_93
```

> 버전 3.6에서 변경: 리터럴에서 숫자들의 그룹을 표현할 목적으로 밑줄을 허락합니다.

### 허수 리터럴

허수 리터럴은 다음과 같은 어휘 정의로 표현됩니다:

```
imagnumber ::=  (floatnumber | digitpart) ("j" | "J")
```

- 가상의 리터럴은 실수 부분이 0.0인 복소수를 산출합니다. 복소수는 한 쌍의 부동소수점으로 표현되며, 그 범위에는 동일한 제한이 있습니다. 실수 부분이 0이 아닌 복소수를 만들려면 `(3+4j)`와 같이 부동소수점 숫자를 더하면 됩니다. 가상 리터럴의 몇 가지 예입니다:

```python
3.14j   10.j    10j     j   1e100j   3.14e-10j   3.14_15_93j
```

## 연산자

- 다음과 같은 토큰들은 연산자입니다:

```python
+       -       *       **      /       //      %      @
<<      >>      &       |       ^       ~       :=
<       >       <=      >=      ==      !=
```

## 구분자

- 다음 토큰들은 문법에서 구분자(delimiter)로 기능합니다:

```python
(       )       [       ]       {       }
,       :       .       ;       @       =       ->
+=      -=      *=      /=      //=     %=      @=
&=      |=      ^=      >>=     <<=     **=
```

- 마침표는 실수와 허수 리터럴에서도 등장할 수 있습니다. 연속된 마침표 세 개는 생략부호 리터럴(ellipsis literal)이라는 특별한 의미가 있습니다. 목록 후반의 증분 대입 연산자(augmented assignment operator)들은 어휘적으로는 구분자로 기능하지만, 동시에 연산을 수행합니다.
- 다음의 인쇄되는 ASCII 문자들은 다른 토큰들 일부로서 특별한 의미가 있거나, 그렇지 않으면 어휘 분석기에 유의미합니다:

```python
'       "       #       \
```

- 다음의 인쇄되는 ASCII 문자들은 파이썬에서 사용되지 않습니다. 문자열 리터럴과 주석 이외의 곳에서 사용되는 것은 조건 없는 에러입니다:

```python
$       ?       `
```


---
## 참조
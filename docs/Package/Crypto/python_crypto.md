---
title: "[Python] 암호화 (Crypto)"
excerpt: 
categories:
  - Python
tags:
  - Python
  - Python-Library
  - Crypto
  - Software-Security
last_modified_at: 2024-04-11T15:11:34+09:00
link: 
상위 항목: "[[python_library|파이썬 라이브러리 (Python Library)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`

**하위 항목**
- 

---

다양한 암호화 알고리즘을 구현합니다. 가용성은 설치에 달려있습니다. 유닉스 시스템에서는 [`crypt`](https://docs.python.org/ko/3/library/crypt.html#module-crypt "crypt: The crypt() function used to check Unix passwords. (폐지됨) (Unix)") 모듈을 사용할 수도 있습니다. 다음은 개요입니다:

- [`hashlib` — Secure hashes and message digests](https://docs.python.org/ko/3/library/hashlib.html)
    - [해시 알고리즘](https://docs.python.org/ko/3/library/hashlib.html#hash-algorithms)
    - [Usage](https://docs.python.org/ko/3/library/hashlib.html#usage)
    - [Constructors](https://docs.python.org/ko/3/library/hashlib.html#constructors)
    - [Attributes](https://docs.python.org/ko/3/library/hashlib.html#attributes)
    - [Hash Objects](https://docs.python.org/ko/3/library/hashlib.html#hash-objects)
    - [SHAKE 가변 길이 요약](https://docs.python.org/ko/3/library/hashlib.html#shake-variable-length-digests)
    - [File hashing](https://docs.python.org/ko/3/library/hashlib.html#file-hashing)
    - [키 파생](https://docs.python.org/ko/3/library/hashlib.html#key-derivation)
    - [BLAKE2](https://docs.python.org/ko/3/library/hashlib.html#blake2)
        - [해시 객체 만들기](https://docs.python.org/ko/3/library/hashlib.html#creating-hash-objects)
        - [상수](https://docs.python.org/ko/3/library/hashlib.html#constants)
        - [예](https://docs.python.org/ko/3/library/hashlib.html#examples)
            - [간단한 해싱](https://docs.python.org/ko/3/library/hashlib.html#simple-hashing)
            - [다른 요약 크기 사용하기](https://docs.python.org/ko/3/library/hashlib.html#using-different-digest-sizes)
            - [키 해싱](https://docs.python.org/ko/3/library/hashlib.html#keyed-hashing)
            - [무작위 해싱](https://docs.python.org/ko/3/library/hashlib.html#randomized-hashing)
            - [개인화](https://docs.python.org/ko/3/library/hashlib.html#personalization)
            - [트리 모드](https://docs.python.org/ko/3/library/hashlib.html#tree-mode)
        - [크레딧](https://docs.python.org/ko/3/library/hashlib.html#credits)
- [`hmac` — Keyed-Hashing for Message Authentication](https://docs.python.org/ko/3/library/hmac.html)
- [`secrets` — Generate secure random numbers for managing secrets](https://docs.python.org/ko/3/library/secrets.html)
    - [난수](https://docs.python.org/ko/3/library/secrets.html#random-numbers)
    - [토큰 생성](https://docs.python.org/ko/3/library/secrets.html#generating-tokens)
        - [토큰은 몇 바이트를 사용해야 합니까?](https://docs.python.org/ko/3/library/secrets.html#how-many-bytes-should-tokens-use)
    - [기타 함수](https://docs.python.org/ko/3/library/secrets.html#other-functions)
    - [조리법과 모범 사례](https://docs.python.org/ko/3/library/secrets.html#recipes-and-best-practices)

---
## 참조

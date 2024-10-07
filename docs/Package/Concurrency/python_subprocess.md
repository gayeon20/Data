---
title: "[Python] 서브 프로세스 (Subprocess)"
excerpt: 
categories:
  - Python
tags:
  - Python
  - Python-Library
  - Concurrency
  - Python-subprocess
last_modified_at: 2024-04-11T15:11:34+09:00
link: https://docs.python.org/ko/3/library/subprocess.html
상위 항목: "[[python_concurrency|파이썬 동시 실행 (Python Concurrency)]]"
---
**최초 작성일**: `:::this.file.cday`
**최종 수정일**: `:::this.file.mtime`


---

- [`subprocess`](https://docs.python.org/ko/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.") 모듈은 새로운 프로세스를 생성하고, 그들의 입력/출력/에러 파이프에 연결하고, 반환 코드를 얻을 수 있도록 합니다. 이 모듈은 몇 가지 이전 모듈과 함수를 대체하려고 합니다:

```
os.system
os.spawn*
```

---
## 참조

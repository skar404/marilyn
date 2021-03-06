# Marilyn SDK

[![PyPI](https://img.shields.io/pypi/v/Marilyn.svg)](https://pypi.python.org/pypi/Marilyn)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c678589e9d2049299b94ede88010c1b6)](https://www.codacy.com/app/skar404/marilyn?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=skar404/marilyn&amp;utm_campaign=Badge_Grade)
[![Updates](https://pyup.io/repos/github/skar404/marilyn/shield.svg)](https://pyup.io/repos/github/skar404/marilyn/)
[![Build Status](https://travis-ci.org/skar404/marilyn.svg?branch=master)](https://travis-ci.org/skar404/marilyn)
[![Python 3](https://pyup.io/repos/github/skar404/marilyn/python-3-shield.svg)](https://pyup.io/repos/github/skar404/marilyn/)

> [Marilyn](https://mymarilyn.ru) - система автоматизации интернет-рекламы

Install:
```bash
pip install Marilyn
```

Use SDK:
```python
import Marilyn

marilyn = Marilyn.CoreApi(login='login', password='password', api_key="api-key")

try:
    marilyn.auth()
except Marilyn.exceptions.LoginRequired:
    exit()

method_api = marilyn.get_api()
user_info = method_api.me()
```

Marilyn API - [docs](https://api-doc.mymarilyn.ru/)

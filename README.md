# Marilyn SDK

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

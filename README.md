# Marilyn SDK

> [Merilyn](https://mymarilyn.ru) - система автоматизации интернет-рекламы


Install:
```bash
pip isntall Marilyn
```

Use SKD:
```python
import Marilyn

merilyn = Marilyn.CoreApi(login='login', password='password', api_key="api-key")

try:
    merilyn.auth()
except Marilyn.exceptions.LoginRequired:
    exit()

method_api = merilyn.get_api()
user_info = method_api.me()
```


Merilyn API - [docs](https://api-doc.mymarilyn.ru/)

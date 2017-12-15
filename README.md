# Marilyn SDK

> Merilyn - система автоматизации интернет-рекламы

Use SKD:
```python
from MarilynApi import CoreApi

merilyn = MarilynApi.CoreApi(login='login', password='password', api_key="api-key")

try:
    merilyn.auth()
except MarilynApi.exceptions.LoginRequired:
    exit()

method_api = merilyn.get_api()
user_info = method_api.me()
```


Merilyn API - [docs](https://api-doc.mymarilyn.ru/)
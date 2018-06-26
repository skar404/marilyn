import os
import unittest

import Marilyn

try:
    from .config import login, password, api_url
except Exception:
    login, password, api_url = os.environ['MARILYN_LOGIN'], os.environ['MARILYN_PASSWORD'], os.environ[
        'MARILYN_URL_API']


class TestMarilynBase(unittest.TestCase):
    api_key = ''

    def test_auth(self):
        marilyn = Marilyn.CoreApi(login=login, password=password, url_api=api_url)

        marilyn.auth()

        self.assertIsNotNone(marilyn.api_key)
        self.__class__.api_key = marilyn.api_key

    def test_auth_tests_token(self):
        marilyn = Marilyn.CoreApi(login=login, password=password, api_key=self.__class__.api_key, url_api=api_url)

        marilyn.auth()

        method_api = marilyn.get_api()
        user_info = method_api.me()
        self.assertEqual(user_info['email'], login)

    def test_auth_not_correct_login(self):
        marilyn = Marilyn.CoreApi(login="test@test.ru", password=password, api_key=self.__class__.api_key,
                                  url_api=api_url)

        try:
            marilyn.auth()
        except Marilyn.exceptions.LoginRequired:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_login_is_none(self):
        marilyn = Marilyn.CoreApi(login=None, password=password, api_key=self.__class__.api_key, url_api=api_url)

        try:
            marilyn.auth()
        except Marilyn.exceptions.LoginRequired:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_readme_code(self):
        marilyn = Marilyn.CoreApi(login=login, password=password, api_key=self.__class__.api_key, url_api=api_url)

        marilyn.auth()

        method_api = marilyn.get_api()
        user_info = method_api.me()

        self.assertEqual(user_info['email'], login)

    def test_login_is_not_password(self):
        marilyn = Marilyn.CoreApi(login=login, password=None, api_key=self.__class__.api_key, url_api=api_url)

        marilyn.auth()

        self.assertTrue(True)

    def test_login_is_not_password_and_api_key(self):
        marilyn = Marilyn.CoreApi(login=login, password=None, api_key=None, url_api=api_url)

        try:
            marilyn.auth()
        except Marilyn.exceptions.LoginRequired:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

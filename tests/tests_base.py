import unittest

import Marilyn

from .config import login, password, api_url


class TestMarilynBase(unittest.TestCase):
    api_key = ''

    def test_auth(self):
        merilyn = Marilyn.CoreApi(login=login, password=password, url_api=api_url)

        try:
            merilyn.auth()
        except Marilyn.exceptions.LoginRequired:
            self.assertTrue(False)
        else:
            self.assertIsNotNone(merilyn.api_key)
            self.__class__.api_key = merilyn.api_key

    def test_auth_tests_token(self):
        merilyn = Marilyn.CoreApi(login=login, password=password, api_key=self.__class__.api_key, url_api=api_url)

        try:
            merilyn.auth()
        except Marilyn.exceptions.LoginRequired as err:
            raise err

        method_api = merilyn.get_api()
        user_info = method_api.me()
        self.assertEqual(user_info['email'], login)

    def test_auth_not_correct_login(self):
        merilyn = Marilyn.CoreApi(login="test@test.ru", password=password, api_key=self.__class__.api_key, url_api=api_url)

        try:
            merilyn.auth()
        except Marilyn.exceptions.LoginRequired:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_login_is_none(self):
        merilyn = Marilyn.CoreApi(login=None, password=password, api_key=self.__class__.api_key, url_api=api_url)

        try:
            merilyn.auth()
        except Marilyn.exceptions.LoginRequired:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

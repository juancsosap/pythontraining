# -*- coding:utf-8 -*-
from unittest import TestCase

from service import BasicService

import app


class TestBasicService(TestCase):

    def setUp(self):
        self.app = app.app.test_client(self)

    def test_getinfos(self):
        self.assertEqual(self.app.get('/api/v1/basic/infos').status_code, 200)

    def test_getinfo(self):
        self.assertEqual(self.app.get('/api/v1/basic/infos/1').status_code, 200)

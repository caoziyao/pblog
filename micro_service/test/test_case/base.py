# coding: utf-8

import unittest
from micro_services.api_kuaibiji.service import ApiService

class BaseCase(unittest.TestCase):
    """测试基础类"""

    def __init__(self, *args, **kwargs):
        super(BaseCase, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        """
        测试开始前执行
        :return:
        """
        pass

    def setUp(self):
        app = ApiService().make_app()
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

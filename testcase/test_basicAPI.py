import requests
import json
import unittest
from ECUData import ECUdata
from commonApi import xiaoantech


class Demo_API(unittest.TestCase):

    def setUp(self) -> None:
        # 协议网址
        self.url = xiaoantech.url
        # body参数
        self.params = xiaoantech.C59
        params_json = json.dumps(self.params)
        # 请求头
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        # 获取响应结果
        res = requests.request("post", self.url, data=params_json, headers=headers).json()
        self.devVsn = res["result"]['config']['devVsn']
        self.devName = res["result"]['config']['devName']
        self.coreVersion = res["result"]['config']['coreVersion']

    # 设备名称，版本号，内核版本校验
    def test_devName(self):
        u"""设备名称验证"""
        try:
            self.assertEqual(ECUdata.devName, self.devName)
        except Exception as e:
            print('设备名称错误:', e)
            raise AssertionError("名称不一致")

    def test_devVsn(self):
        u"""版本号验证"""
        try:
            self.assertEqual(ECUdata.devVsn, self.devVsn)
        except Exception as e:
            print('版本号错误:', e)
            raise AssertionError("版本号不一致")

    def test_coreVersion(self):
        u"""内核版本验证"""
        try:
            self.assertEqual(ECUdata.coreVersion, self.coreVersion)
        except Exception as e:
            print('内核版本错误:', e)
            raise AssertionError("内核版本号不一致")

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()

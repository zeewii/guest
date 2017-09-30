#coding=utf-8
import unittest

import requests


#查询发布会接口测试
class GetEventListTest(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/get_event_list/"


    #发布会id为空
    def test_001_get_event_null(self):
        u'''发布会id为空'''
        r = requests.get(self.url, params={'eid':''})
        result = r.json()
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], 'parameter error')

    #发布会id不存在
    def test_002_get_event_error(self):
        u'''发布会id不存在'''
        r = requests.get(self.url, params={'eid':'1000'})
        result = r.json()
        self.assertEqual(result['status'], 10022)
        self.assertEqual(result['message'], 'query result is empty')

    #发布会id为1,查询成功
    def test_003_get_event_success(self):
        u'''发布会id为1,查询成功'''
        r = requests.get(self.url, params={'eid':'1'})
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'success')
        self.assertIn('iphone8', result['data']['name'])
        self.assertEqual(result['data']['start_time'], '2017-09-28T06:00:00')



if __name__ == "__main__":
    unittest.main()
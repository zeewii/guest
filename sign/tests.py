#coding=utf-8
#django单元测试
from django.test import TestCase
from django.contrib.auth.models import User

from sign.models import Event, Guest


# Create your tests here.

#模型测试
class ModelTest(TestCase):

    def setUp(self):
        Event.objects.create(id=1, name="oneplus 3 event", status=True, limit=2000, address='shenzhen', start_time='2016-08-31 02:18:22')
        Guest.objects.create(id=1, event_id=1, realname='alen', phone='13711001101',email='alen@mail.com', sign=False)

    #测试发布会表
    def test_001_event_models(self):
        u'''测试发布会表'''
        result = Event.objects.get(name="oneplus 3 event")
        self.assertEqual(result.address, "shenzhen")
        self.assertTrue(result.status)

    def test_002_guest_models(self):
        u'''测试嘉宾表'''
        result = Guest.objects.get(phone='13711001101')
        self.assertEqual(result.realname, "alen")
        self.assertFalse(result.sign)

#测试index登录首页
class IndexPageTest(TestCase):
    def test_001_index_page_renders_index_template(self):
        u"""断言是否用给定的index.html模版响应"""
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


#测试登录动作
class LoginActionTest(TestCase):

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')

    def test_001_add_author_email(self):
        ''' 测试添加用户 '''
        user = User.objects.get(username="admin")
        self.assertEqual(user.username, "admin")
        self.assertEqual(user.email, "admin@mail.com")

    def test_002_login_action_username_password_null(self):
        ''' 用户名密码为空 '''
        response = self.client.post('/login_action/', {'username': '', 'password': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"username or password error!", response.content)

    def test_003_login_action_username_password_error(self):
        ''' 用户名密码错误 '''
        response = self.client.post('/login_action/', {'username': 'abc', 'password': '123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"username or password error!", response.content)

    def test_004_login_action_success(self):
        ''' 登录成功 '''
        response = self.client.post('/login_action/', data={'username': 'admin', 'password': 'admin123456'})
        self.assertEqual(response.status_code, 302)


#发布会管理
class EventManageTest(TestCase):


    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        Event.objects.create(name="xiaomi5", limit=2000, address='beijing', status=1, start_time='2017-8-10 12:30:00')
        login_user = {'username': 'admin', 'password': 'admin123456'}
        self.client.post('/login_action/', data=login_user)  # 预先登录

    def test_001_add_event_data(self):
        ''' 测试添加发布会 '''
        event = Event.objects.get(name="xiaomi5")
        self.assertEqual(event.address, "beijing")

    def test_002_event_mange_success(self):
        ''' 测试发布会:xiaomi5 '''
        response = self.client.post('/event_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"xiaomi5", response.content)
        self.assertIn(b"beijing", response.content)

    def test_003_event_mange_search_success(self):
        ''' 测试发布会搜索 '''
        response = self.client.post('/search_name/', {"name": "xiaomi5"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"xiaomi5", response.content)
        self.assertIn(b"beijing", response.content)

#嘉宾管理
class GuestManageTest(TestCase):

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        Event.objects.create(id=1,name="xiaomi5", limit=2000, address='beijing', status=1, start_time='2017-8-10 12:30:00')
        Guest.objects.create(realname="alen", phone="13000010",email='alen@mail.com', sign=0, event_id=1)
        login_user = {'username': 'admin', 'password': 'admin123456'}
        self.client.post('/login_action/', data=login_user)  # 预先登录

    def test_001_add_guest_data(self):
        ''' 测试添加嘉宾 '''
        guest = Guest.objects.get(realname="alen")
        self.assertEqual(guest.phone, "13000010")
        self.assertEqual(guest.email, "alen@mail.com")
        self.assertFalse(guest.sign)

    def test_002_event_mange_success(self):
        ''' 测试嘉宾信息: alen '''
        response = self.client.post('/guest_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"alen", response.content)
        self.assertIn(b"13000010", response.content)

    def test_003_guest_mange_search_success(self):
        ''' 测试嘉宾搜索 '''
        response = self.client.post('/guest_search/',{"phone":"13000010"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"alen", response.content)
        self.assertIn(b"13000010", response.content)

#发布会签到
class SignIndexActionTest(TestCase):

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        Event.objects.create(id=1, name="xiaomi5", limit=2000, address='beijing', status=1, start_time='2017-8-10 12:30:00')
        Event.objects.create(id=2, name="oneplus4", limit=2000, address='shenzhen', status=1, start_time='2017-6-10 12:30:00')
        Guest.objects.create(realname="alen", phone="18611001100", email='alen@mail.com', sign=0, event_id=1)
        Guest.objects.create(realname="una", phone="18611001101", email='una@mail.com', sign=1, event_id=2)
        login_user = {'username': 'admin', 'password': 'admin123456'}
        self.client.post('/login_action/', data=login_user)

    def test_001_sign_index_action_phone_null(self):
        ''' 手机号为空 '''
        response = self.client.post('/sign_index_action/1/', {"phone": ""})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"phone error.", response.content)

    def test_002_sign_index_action_phone_or_event_id_error(self):
        ''' 手机号或发布会id错误 '''
        response = self.client.post('/sign_index_action/2/', {"phone": "18611001100"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"event id or phone error.", response.content)

    def test_003_sign_index_action_user_sign_has(self):
        ''' 用户已签到 '''
        response = self.client.post('/sign_index_action/2/', {"phone": "18611001101"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"user has sign in.", response.content)

    def test_004_sign_index_action_sign_success(self):
        ''' 签到成功 '''
        response = self.client.post('/sign_index_action/1/', {"phone": "18611001100"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"sign in success!", response.content)


'''
运行所有用例：
python3 manage.py test

运行sign应用下的所有用例：
python3 manage.py test sign

运行sign应用下的tests.py文件用例：
python3 manage.py test sign.tests

运行sign应用下的tests.py文件中的 GuestManageTest 测试类：
python3 manage.py test sign.tests.GuestManageTest

......


'''

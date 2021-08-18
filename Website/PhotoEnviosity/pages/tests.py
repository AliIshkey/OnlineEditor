from django.contrib.auth.models import User
from django.test import TestCase

class SignInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'adele',
            'password': 'admin@123'}
        User.objects.create_user(**self.credentials)

    def test_signin(self):
        # send sign data
        response = self.client.post('/signin/', self.credentials, follow=True)
        # should be registered in now
        self.assertTrue(response.context['user'].is_active)

class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'Ali',
            'password': 'admin@123'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

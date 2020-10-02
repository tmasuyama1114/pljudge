from django.test import TestCase
from django.core import mail
from allauth.account.forms import LoginForm, SignupForm
from allauth.utils import get_user_model
from django.contrib import auth
from django.urls import reverse
from unittest.mock import patch
from django.contrib.auth import get_user_model
User = get_user_model()
from pljudge.models import Portfolio

class TestSignUp(TestCase):
    def setUp(self):
        self.post_user_data = {
            "email": "test@test.com",
            "password1": "Abc123",
            "password2": "Abc123",
        }

    def test_user_login_page_loads_correctly(self):
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')
        # self.assertContains(response, 'LOGIN')
        self.assertIsInstance(
            response.context['form'], LoginForm
        )

    def test_user_login_page_submission_works(self):
        user1 = User.objects.create_user(
            # self.post_user_data['username'],
            self.post_user_data['email'],
            self.post_user_data['password1']
        )
        user1.save()

        post_data = {
            'login':self.post_user_data['email'],
            'password':self.post_user_data['password1']    
        }

        #ユーザが追加されたか確認
        self.assertTrue(
            User.objects.filter(
                email=self.post_user_data['email']
            ).exists()
        )

        response = self.client.post(
            reverse("account_login"), post_data
        )

        #ログイン状態か
        self.assertTrue(
            auth.get_user(self.client).is_authenticated
        )

        #homeへリダイレクト
        self.assertEqual(response.status_code, 302)

class TestPortfolio(TestCase):
    def setUp(self):
        self.post_user_data = {
            "email": "test@test.com",
            "password1": "Abc123",
            "password2": "Abc123",
        }

        user1 = User.objects.create_user(
            # self.post_user_data['username'],
            self.post_user_data['email'],
            self.post_user_data['password1']
        )
        user1.save()

        post_data = {
            'login':self.post_user_data['email'],
            'password':self.post_user_data['password1']    
        }

    def test_new_portfolio(self):
        self.post_portfolio_data = {
            "ticker": "ZM",
        }

        portfolio = Portfolio.objects.create_portfolio(
            self.post_portfolio_data['ticker'],
        )
        portfolio.save()

        self.assertTrue(
            Portfolio.objects.filter(
                email=self.post_portfolio_data['email']
            ).exists()
        )

        # response = self.client.post(
        #     reverse("pljudge:index"), post_data
        # )
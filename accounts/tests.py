from django.urls import reverse
from django.test import TestCase
from .models import User

class AccountsTestCase(TestCase):
    def test_login_page(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_user_login(self):
        response = self.client.post(reverse('accounts:login'))
        # Добавьте здесь свои проверки, например, assertRedirects

    def test_user_registration(self):
        data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'email': 'test@example.com',
            'firstname': 'John',
            'lastname': 'Doe',
        }
        response = self.client.post(reverse('accounts:register'), data)
        # Проверка на перенаправление после успешной регистрации
        self.assertRedirects(response, reverse('index'))
        # Проверка, что пользователь действительно создан
        self.assertTrue(User.objects.filter(username='testuser').exists())

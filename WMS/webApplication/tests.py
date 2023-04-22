from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import SignUpForm
# Create your tests here.


# Creates a new client and performs the test.
class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse("login")

    def test_login_view_with_invalid_credentials(self):
        username = "testuser"
        password = "testpassword"
        User.objects.create_user(username=username, password=password)
        response = self.client.post(
            self.login_url, {"username": username, "password": "wrongpassword"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "webApplication/login.html")
        self.assertContains(response, "Invalid credentials")


# Test to see if the user is logged out
class LogoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.logout_url = reverse("logout")

    def test_logout_view(self):
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "webApplication/login.html")
        self.assertContains(response, "Logged out")


# Test if pricing is working.
class PricingViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.pricing_url = reverse("pricing")

    def test_pricing_view(self):
        response = self.client.get(self.pricing_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "webApplication/pricing.html")


# Create a test case for the signup view.
class SignUpViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('signup')
        self.valid_data = {
            'username': 'testuser',
            'email': 'testuser@test.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }

    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'webApplication/signup.html')
        self.assertIsInstance(response.context['form'], SignUpForm)

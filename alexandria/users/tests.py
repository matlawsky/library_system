from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignUpPageTests(TestCase):
    def test_url_exists_at_correct_location_signupview(self):
        response = self.client.get("/users/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/signup.html")

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "testuser@email.com",
                "first_name": "Test",
                "second_name": "User",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
        self.assertEqual(get_user_model().objects.all()[0].email, "testuser@email.com")
        self.assertEqual(get_user_model().objects.all()[0].first_name, "Test")
        self.assertEqual(get_user_model().objects.all()[0].second_name, "User")


class HomepageTests(TestCase):
    def test_url_exists_at_correct_loaction(self):
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, 200)


class CRUDTests(TestCase):
    pass

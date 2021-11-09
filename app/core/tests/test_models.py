from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

def sample_user(email = "test@test.com", password = "12345678"):
    return get_user_model().objects.create_user(email,password)


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        email = "aalekhbh@gmail.com"
        password = "12345678"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = "test@TEST.com"
        user = get_user_model().objects.create_user(
            email,
            "12345678"
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '12345678')

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            "test@test.com",
            "12345678"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        tag = models.Tag.objects.create(
            user = sample_user(),
            name = 'Vegan'
        )

        self.assertEquals(str(tag), tag.name)

    def test_ingredient_str(self):
        ingredient = models.Ingredient.objects.create(
            user = sample_user(),
            name = "Cucumber"
        )

        self.assertEqual(str(ingredient), ingredient.name)
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.tests import APITestCase, APIClient


User = get_user_model()


class LyricViewTest(APITestCase):
    def setUp(self):
        self.author = User.objects.create_user(username="test@user.com", password="test@password.strong")
        self.title = "Oceans"
        self.description = "A worship song spirit filled"
        self.content = "Spirit lead where my trust is without borders ..."
        self.composer = "Hillsong United"

        self.lyric_data = {
            "title": self.title,
            "description": self.description,
            "content": self.content,
            "composer": self.composer,
            "author": self.author,
        }

        self.client = APIClient()

        self.field_required_msg = "This field is required."

    def test_lyric_creation(self):
        """
        Tests that lyric is created when required fields are passed
        returns:
        """
        response = self.client.post(reverse("lyric_list"), data=self.lyric_data)
        self.assertEqual(response.status_code, 201)
        lyric = Lyric.objects.first()
        for field in self.lyric_data:
            self.assertEqual(response.json().get(field), exec(f"lyric.{field}"))

    def test_lyric_creation_failed_missing_fields(self):
        """
        Tests that lyric creation fails when some fields are missing
        returns:
        """
        # Missing title
        data = self.lyric_data.copy()
        del data["title"]
        response = self.client.post(reverse("lyric_list"), data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["title"][0], self.field_required_msg)

        with self.assertRaises(Lyric.DoesNotExist):
            Lyric.objects.get(pk=1)
        self.assertEqual(Lyric.objects.count(), 0)

        # Missing author
        data = self.lyric_data.copy()
        del data["author"]
        response = self.client.post(reverse("lyric_list"), data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["author"][0], self.field_required_msg)

        with self.assertRaises(Lyric.DoesNotExist):
            Lyric.objects.get(pk=1)
        self.assertEqual(Lyric.objects.count(), 0)

        # Missing Content
        data = self.lyric_data.copy()
        del data["content"]
        response = self.client.post(reverse("lyric_list"), data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["content"][0], self.field_required_msg)

        with self.assertRaises(Lyric.DoesNotExist):
            Lyric.objects.get(pk=1)
        self.assertEqual(Lyric.objects.count(), 0)

        # Missing composer
        data = self.lyric_data.copy()
        del data["composer"]
        response = self.client.post(reverse("lyric_list"), data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["composer"][0], self.field_required_msg)

        with self.assertRaises(Lyric.DoesNotExist):
            Lyric.objects.get(pk=1)
        self.assertEqual(Lyric.objects.count(), 0)

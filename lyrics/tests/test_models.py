from django.test import TestCase
from django.contrib.auth import get_user_model

from lyrics.models import Lyric


User = get_user_model()


class LyricsModelTest(TestCase):
    def setUp(self):
        self.lyric_author = User.objects.create(username="author@test.com", password="password@test.author")
        self.lyric_data = {
            "title": "Test Lyric Title",
            "description": "Test Lyric description",
            "content": "Test Lyric Content",
            "author": self.lyric_author,
            "composer": "Lyric Composer",
        }

    def test_object_creation(self):
        """
        Test that lyric object can be created and saved in the db
        returns:
        """
        lyric = Lyric.objects.create(**self.lyric_data)
        self.assertEqual(lyric.title, self.lyric_data["title"])
        self.assertEqual(lyric.description, self.lyric_data["description"])
        self.assertEqual(lyric.content, self.lyric_data["content"])
        self.assertEqual(lyric.author, self.lyric_data["author"])
        self.assertEqual(lyric.composer, self.lyric_data["composer"])

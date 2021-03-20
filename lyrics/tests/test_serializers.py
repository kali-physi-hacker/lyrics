from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError

from lyrics.serializers import LyricSerializer
from lyrics.models import Lyric


User = get_user_model()


class LyricSerializerTest(TestCase):
    def setUp(self):
        self.author = User.objects.create(username="author@test.com", password="author@test.password")
        self.lyric_data = {
            "title": "Test Title",
            "description": "Test description",
            "content": "Test Content",
            "composer": "Test Composer",
            "author": self.author,
        }

        self.required_error_msg = "This field is required."

    def test_validation_true(self):
        """
        Tests that serializer is valid if valid and required fields are passed and that data is saved with
        the correct data passed
        returns:
        """
        serializer = LyricSerializer(data=self.lyric_data)
        self.assertTrue(serializer.is_valid())

        # Test save()
        lyric = serializer.save()

        # Test that the data saved == data passed
        for field in self.lyric_data:
            self.assertEqual(eval(f"lyric.{field}"), self.lyric_data.get(field))

        saved_lyric = Lyric.objects.first()

        self.assertEqual(lyric, saved_lyric)

    def test_validation_false_for_required_missing(self):
        """
        Tests that serializer is not valid for required fields that are missing
        returns:
        """
        # Missing title
        data = self.lyric_data.copy()
        del data["title"]

        serializer = LyricSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors.get("title")[0], self.required_error_msg)

        with self.assertRaises(IntegrityError):
            serializer.save()

        # Missing content
        data = self.lyric_data.copy()
        del data["content"]

        serializer = LyricSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors.get("content")[0], self.required_error_msg)

        with self.assertRaises(IntegrityError):
            serializer.save()

        # Missing author
        data = self.lyric_data.copy()
        del data["author"]

        serializer = LyricSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors.get("author")[0], self.required_error_msg)

        with self.assertRaises(IntegrityError):
            serializer.save()

        data = self.lyric_data.copy()
        del data["composer"]

        serializer = LyricSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors.get("composer")[0], self.required_error_msg)

        with self.assertRaises(IntegrityError):
            serializer.save()

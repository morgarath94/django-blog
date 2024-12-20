from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User
import datetime
from blogging.models import Post, Category


class PostTest(TestCase):
    fixtures = [
        "blogging_test_fixture.json",
    ]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a blog title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(actual, expected)


class CategoryTestCase(TestCase):
    def test_string_representation(self):
        expected = "A category"
        category1 = Category(name=expected)
        actual = str(category1)
        self.assertEqual(actual, expected)


class FrontEndTestCase(TestCase):
    fixtures = [
        "blogging_test_fixture.json",
    ]

    def setUp(self):
        self.now = datetime.datetime.now(tz=datetime.timezone.utc)
        self.timedelta = datetime.timedelta(15)
        author = User.objects.get(pk=1)
        for count in range(1, 11):
            post = Post(
                title=f"Post {count} Title", text=f"Post {count} Text", author=author
            )
            if count < 6:
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate
            post.save()

    def test_list_only_published(self):
        resp = self.client.get("/")
        self.assertContains(resp, "Recent Posts")
        for count in range(1, 11):
            title = f"Post {count} Title"
            if count < 6:
                self.assertContains(resp, title, count=1)
            else:
                self.assertNotContains(resp, title)

    # def test_details_only_published(self):
    #     for count in range(1, 11):
    #         title = f"Post {count} Title"
    #         post = Post(title=title)
    #         resp = self.client.get(f"posts/{post.pk}")
    #         if count < 6:
    #             self.assertEqual(resp.status_code, 200)
    #             self.assertContains(resp, title)
    #         else:
    #             self.assertEqual(resp.status_code, 404)

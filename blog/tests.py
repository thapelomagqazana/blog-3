from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Post


class PostListViewTests(TestCase):
    def test_post_list_view(self):
        """
        Test that the post list view returns a 200 status code and uses the correct template.
        """
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post/list.html')


class PostDetailViewTests(TestCase):
    def setUp(self):
        # Create a test post
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author_id=1,
            body='This is a test post body.',
            publish=timezone.now(),
            status=Post.Status.PUBLISHED,
        )

    def test_post_detail_view(self):
        """
        Test that the post detail view returns a 200 status code, uses the correct template, and displays the correct post.
        """
        response = self.client.get(self.post.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post/detail.html')
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.body)

# Add more tests for other views as needed

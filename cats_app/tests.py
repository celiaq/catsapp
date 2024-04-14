from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from cats_app.models import CatPost, Comment


class TestIndexView(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'index.html')

class TestRegisterView(TestCase):

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'register.html')

    def test_register_new_user(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

class TestLoginView(TestCase):

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'login.html')

class TestCreatePostView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_post_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('create_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_post.html')

class TestDeletePostView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = CatPost.objects.create(user=self.user, image='Test Post', comment='This is a test post')

    def test_delete_post_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('delete_photo', kwargs={'post_pk': self.post.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(CatPost.objects.filter(comment='Test Post').exists())

class TestCatPostModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_catpost_creation(self):
        cat_post = CatPost.objects.create(
            user=self.user,
            image='C:/Users/celia/OneDrive/Images/aa.jpg',  # Remplacez 'cat.jpg' par le chemin de l'image
            comment='Test comment'
        )
        self.assertEqual(cat_post.user, self.user)
        self.assertEqual(cat_post.image, 'C:/Users/celia/OneDrive/Images/aa.jpg')
        self.assertEqual(cat_post.comment, 'Test comment')

class TestCommentModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.cat_post = CatPost.objects.create(
            user=self.user,
            image='C:/Users/celia/OneDrive/Images/aa.jpg',  # Remplacez 'cat.jpg' par le chemin de l'image
            comment='Test comment'
        )

    def test_comment_creation(self):
        comment = Comment.objects.create(
            user=self.user,
            photo=self.cat_post,
            text='Test comment'
        )
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.photo, self.cat_post)
        self.assertEqual(comment.text,'Test comment')
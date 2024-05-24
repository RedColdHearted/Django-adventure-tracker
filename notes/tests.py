from django.test import TestCase, Client
from django.urls import reverse

from users.models import User
from .models import Note

class BaseTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        response = self.client.get(reverse('notes:home'))
        self.assertEqual(response.status_code, 200)

    def test_redirect_to_home_view(self):
        response = self.client.get(reverse('redirect_to_home'))
        expected_url = reverse('notes:home')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], expected_url)
        self.assertRedirects(response, expected_url)

class UserTestCases(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = 'notes:login'
        self.user1 = User.objects.create_user(
            username='testuser1', password='password'
        )
        self.user2 = User.objects.create_user(
            username='testuser2', password='password'
        )
        self.profile_url = reverse('notes:profile', kwargs={'pk': self.user1.pk})
    def test_view_accessible_if_logged_in(self):
        self.client.login(username='testuser1', password='password')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)

    def test_can_user_get_others_note(self):
        #test 1
        self.client.login(username=self.user1.username, password='password')

        self.user1_note = Note.objects.create(title='test1',
                                              location='[50, 50]',
                                              description='test1',
                                              user=self.user1)
        self.user2_note = Note.objects.create(title='some title',
                                              location='[50, 50]',
                                              description='some description',
                                              user=self.user2)

        update_url_user2_note = reverse('notes:update-note', kwargs={'uuid': self.user2_note.pk})
        response = self.client.get(update_url_user2_note)
        self.assertEqual(response.status_code, 404)
        self.client.logout()

        #test 2
        self.client.login(username=self.user2.username, password='password')
        update_url_user2_note = reverse('notes:update-note', kwargs={'uuid': self.user1_note.pk})
        response = self.client.get(update_url_user2_note)
        self.assertEqual(response.status_code, 404)
        self.client.logout()

class RegisterViewTest(TestCase):

    def setUp(self):
        # Задаем URL для вьюшки
        self.url = reverse('notes:register')  # не забудьте изменить 'notes:register' на правильный путь вашего URL

    def test_register_view_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')
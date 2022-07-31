from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

new_user = {
    "first_name": "new_first_name",
    "last_name": "new_last_name",
    "username": "new_username",
    "password1": "new_password1",
    "password2": "new_password1",
}


class UsersTest(TestCase):
    fixtures = ['users.json']

    def check_permissions(self, name):
        any_user_id = 1
        # Anonymous try to update/delete someone details
        response = self.client.get(reverse(name, args=[any_user_id]))
        self.assertRedirects(response, reverse('login'))
        # Logged user try to update/delete another user details
        user = User.objects.get(id=7)
        self.client.force_login(user)
        response = self.client.get(reverse(name, args=[any_user_id]))
        self.assertRedirects(response, reverse('users'))

    def create_logged_user(self):
        user = User.objects.create(
            username=new_user['username'],
            password=new_user['password1'],
        )
        self.client.force_login(user)
        return user

    def test_create_page(self):
        response = self.client.get(reverse('create_user'))
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_page(self):
        response = self.client.get(reverse('logout'), follow=True)
        self.assertRedirects(response, reverse('index_page'))

    def test_create_login_logout(self):
        # Create user first
        response = self.client.post(reverse('create_user'), new_user)
        user = User.objects.get(username=new_user['username'])
        self.assertRedirects(response, reverse('login'))
        self.assertEqual(user.username, new_user['username'])
        # Login a new created user
        response = self.client.post(
            reverse('login'), {
                'username': new_user['username'],
                'password': new_user['password1']})
        self.assertRedirects(response, reverse('index_page'))
        # A user logout
        response = self.client.post(reverse('logout'))
        self.assertRedirects(response, reverse('index_page'))

    def test_users_page(self):
        response = self.client.get(reverse('users'))
        users = User.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['user_list'],
            users,
            ordered=False)

    def test_update_page_permission(self):
        self.check_permissions('update_user')

    def test_update(self):
        user = self.create_logged_user()
        response = self.client.get(reverse('update_user', args=[user.id]))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('update_user', args=[user.id]), new_user)
        new_first_name = User.objects.get(id=user.id).first_name
        self.assertNotEqual(user.first_name, new_first_name)

    def test_delete_page_permission(self):
        self.check_permissions('delete_user')

    def test_delete(self):
        user = self.create_logged_user()
        response = self.client.get(reverse('delete_user', args=[user.id]))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('delete_user', args=[user.id]))
        self.assertRedirects(response, reverse('users'))
        with self.assertRaises(ObjectDoesNotExist):
            User.objects.get(id=user.id)

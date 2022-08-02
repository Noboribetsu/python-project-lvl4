from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from task_manager.statuses.models import Status

new_user = {
    "username": "new_username",
    "password": "new_password1",
}


class StatusTest(TestCase):
    fixtures = ['statuses.json']

    def create_logged_user(self):
        user = User.objects.create(
            username=new_user['username'],
            password=new_user['password'],
        )
        self.client.force_login(user)
        return user

    def check_login_requirements(self, url):
        # Check for not logged user
        response = self.client.get(url)
        self.assertRedirects(response, reverse('login'))
        # Create logged user, check for logged user
        self.create_logged_user()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        return response

    def test_statuses_page(self):
        response = self.check_login_requirements(reverse('statuses'))
        # Check that response return QuerySet with statuses from DB
        statuses = Status.objects.all()
        self.assertQuerysetEqual(
            response.context['status_list'], statuses,
            ordered=False)

    def test_create_status_page(self):
        self.check_login_requirements(reverse('create_status'))
        # Create a new status for check
        response = self.client.post(
            reverse('create_status'),
            {'name': 'new_status'})
        self.assertRedirects(response, reverse('statuses'))
        new_status = Status.objects.get(name='new_status')
        self.assertEqual(new_status.name, 'new_status')

    def test_update_status_page(self):
        old_status = Status.objects.all()[0]
        self.check_login_requirements(
            reverse('update_status', args=[old_status.id]))
        response = self.client.post(
            reverse('update_status', args=[old_status.id]),
            {'name': 'updated_name'})
        self.assertRedirects(response, reverse('statuses'))
        new_status = Status.objects.get(id=old_status.id)
        self.assertEqual(new_status.name, 'updated_name')

    def test_delete_status_page(self):
        status = Status.objects.all()[0]
        self.check_login_requirements(
            reverse('delete_status', args=[status.id]))
        response = self.client.post(
            reverse('delete_status', args=[status.id]))
        self.assertRedirects(response, reverse('statuses'))
        with self.assertRaises(ObjectDoesNotExist):
            Status.objects.get(id=status.id)

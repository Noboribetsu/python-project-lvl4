from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from task_manager.labels.models import Label


class LabelTest(TestCase):
    fixtures = [
        'users.json',
        'labels.json',
    ]

    def get_logged_user(self):
        user = User.objects.all()[0]
        self.client.force_login(user)
        return user

    def check_login_requirements(self, url):
        # Check for not logged user
        response = self.client.get(url)
        self.assertRedirects(response, reverse('login'))
        # Get logged user, check for logged user
        self.get_logged_user()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        return response

    def test_labels_page(self):
        response = self.check_login_requirements(reverse('labels'))
        # Check that response return QuerySet with labels from DB
        labels = Label.objects.all()
        self.assertQuerysetEqual(
            response.context['label_list'], labels,
            ordered=False)

    def test_create_label_page(self):
        self.check_login_requirements(reverse('create_label'))
        # Create a new label for check
        response = self.client.post(
            reverse('create_label'),
            {'name': 'new_label'})
        self.assertRedirects(response, reverse('labels'))
        new_label = Label.objects.get(name='new_label')
        self.assertEqual(new_label.name, 'new_label')

    def test_update_label_page(self):
        old_label = Label.objects.all()[0]
        self.check_login_requirements(
            reverse('update_label', args=[old_label.id]))
        response = self.client.post(
            reverse('update_label', args=[old_label.id]),
            {'name': 'updated_name'})
        self.assertRedirects(response, reverse('labels'))
        new_label = Label.objects.get(id=old_label.id)
        self.assertEqual(new_label.name, 'updated_name')

    def test_delete_label_page(self):
        label = Label.objects.all()[0]
        self.check_login_requirements(
            reverse('delete_label', args=[label.id]))
        response = self.client.post(
            reverse('delete_label', args=[label.id]))
        self.assertRedirects(response, reverse('labels'))
        with self.assertRaises(ObjectDoesNotExist):
            Label.objects.get(id=label.id)

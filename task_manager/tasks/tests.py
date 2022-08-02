from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status


class TestTask(TestCase):
    fixtures = [
        'users.json',
        'statuses.json',
        'tasks.json',
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

    def test_tasks_page(self):
        response = self.check_login_requirements(reverse('tasks'))
        tasks = Task.objects.all()
        self.assertQuerysetEqual(
            response.context['task_list'], tasks,
            ordered=False)

    def test_task_detail_page(self):
        task = Task.objects.all()[0]
        self.check_login_requirements(reverse('task_details', args=[task.id]))

    def test_create_task_page(self):
        self.check_login_requirements(reverse('create_task'))
        author = self.get_logged_user().id
        status = Status.objects.all()[0].id
        # Create a new task for check
        response = self.client.post(
            reverse('create_task'),
            {'name': 'create_task', 'status': status, 'author': author}
        )
        self.assertRedirects(response, reverse('tasks'))
        new_task = Task.objects.get(name='create_task')
        self.assertEqual(new_task.name, 'create_task')

    def test_update_task_page(self):
        old_task = Task.objects.all()[0]
        self.check_login_requirements(
            reverse('update_task', args=[old_task.id]))
        new_description = 'add some more details to description'
        response = self.client.post(
            reverse('update_task', args=[old_task.id]),
            {
                'name': old_task.name,
                'description': new_description,
                'status': old_task.status_id,
            })
        self.assertRedirects(response, reverse('tasks'))
        new_status = Task.objects.get(id=old_task.id)
        self.assertEqual(new_status.description, new_description)

    def test_delete_status_page(self):
        user = User.objects.all()[0]
        task = Task.objects.get(author=user)
        self.check_login_requirements(
            reverse('delete_task', args=[task.id]))
        response = self.client.post(
            reverse('delete_task', args=[task.id]))
        self.assertRedirects(response, reverse('tasks'))
        with self.assertRaises(ObjectDoesNotExist):
            Status.objects.get(id=task.id)

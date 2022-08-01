from django.contrib.auth.models import User

"""
    Change method "__str__" of model User.
    Return full name of a user.
"""


def get_user_full_name(self):
    return f'{self.first_name} {self.last_name}'


User.add_to_class("__str__", get_user_full_name)

from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class EmailAuthBackend(object):

    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class EmailBackend(ModelBackend):

    def authenticate(self, **credentials):
        if 'username' in credentials:
            return super(EmailBackend, self).authenticate(**credentials)

        try:
            user = User.objects.get(email=credentials.get('email'))
            if user.check_password(credentials.get('password')):
                return user
        except User.DoesNotExist:
            return None
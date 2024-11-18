#  backend de autenticação personalizado no Django, que permite que os usuários façam login usando o email em vez do nome de usuário padrão
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

Usuario = get_user_model()

class EmailBackend(ModelBackend):
   
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Usuario.objects.get(email=username)
        except Usuario.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
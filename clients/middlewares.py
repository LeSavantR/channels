from urllib.parse import parse_qs

from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
# from rest_framework_simplejwt.tokens import AccessToken


User = get_user_model()

@database_sync_to_async
def get_user(token):
    try:
        return User.objects.filter(username=token).first()
    except:
        return AnonymousUser()
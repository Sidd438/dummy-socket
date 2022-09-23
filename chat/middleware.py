from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden

User = get_user_model()

@database_sync_to_async
def get_user(access_token_str):
    try:
        access_token_obj = AccessToken(access_token_str)
        user_id=access_token_obj['user_id']
        return User.objects.get(id=user_id)
    except Exception as e:
        return None


class TokenAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        headers = dict(scope['headers'])
        if b'authorization' in headers:
            try:
                token_name, token_key = headers[b'authorization'].decode().split()
                if not token_name == 'Bearer':
                    token_key = None
            except ValueError:
                token_key = None
        else:
            token_key = None
        if token_key:
            user = await get_user(token_key)
        else:
            return HttpResponseForbidden("Invalid user")
        if not user:
            return HttpResponseForbidden("Invalid user")
        scope['user'] = user
        return await super().__call__(scope, receive, send)
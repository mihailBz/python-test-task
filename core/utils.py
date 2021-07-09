from rest_framework.authtoken.models import Token


def get_user_by_token(request):
    return Token.objects.get(key=request.auth).user

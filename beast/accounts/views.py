from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from accounts import serializers
from accounts.models import User
from accounts.serializers import UserApiSerializer


class UserMeViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserApiSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)

    # @action(methods=['put'], detail=False, url_path='language')
    # def change_language(self, request, *args, **kwargs):
    #     language = request.data.get('language', None)
    #     if not language:
    #         raise ValidationError('Language parameter not provided.')
    #
    #     try:
    #         Language(language)
    #     except ValueError:
    #         raise ValidationError(f'Language {language} not supported.')

        user = request.user

        user.language = language
        user.save()

        serializer = serializers.UserApiSerializer(user)
        return Response(data=serializer.data)

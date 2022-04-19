from channels.generic.websocket import WebsocketConsumer
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView


def has_permission(*permissions):
    """
    Verifies that the user in the request object has the required permissions
    either from its assigned group or directly assigned permission instance.
    Can be used as a decorator on a DRF ViewSet

    :param permissions: iterable of Django permission
    """
    def has_permission_wrap(func):
        def wrapper(view_self, request, *args, **kwargs):
            # WebSocket
            if issubclass(view_self.__class__, WebsocketConsumer):
                if view_self.scope['user'].has_perms(permissions):
                    return func(view_self, request, *args, **kwargs)
            # HTTP
            if issubclass(view_self.__class__, APIView):
                if request.user.has_perms(permissions):
                    return func(view_self, request, *args, **kwargs)

            raise PermissionDenied()

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__ or None
        return wrapper
    return has_permission_wrap

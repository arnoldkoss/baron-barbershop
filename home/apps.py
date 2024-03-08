from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    AppConfig subclass for the 'home' app.

    This class defines configuration settings for the 'home' app.
    It specifies the default_auto_field and the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    AppConfig subclass for the 'about' app.

    This class defines configuration settings for the 'about' app.
    It specifies the default_auto_field and the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'

from django.apps import AppConfig


class ReservationConfig(AppConfig):
    """
    AppConfig subclass for the 'reservation' app.

    This class defines configuration settings for the 'reservation' app.
    It specifies the default_auto_field and the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reservation'

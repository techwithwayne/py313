# Import AppConfig class from Django's apps module, which is used to configure an app
from django.apps import AppConfig


# Define a custom configuration class for the 'users' app
class UsersConfig(AppConfig):
    # Set the default auto field type to BigAutoField, which will be used for primary keys
    default_auto_field = "django.db.models.BigAutoField"
    
    # Specify the name of the app (this is the Python path to the app's directory)
    name = "users"
    
    # Define the ready method, which is called when the app is fully loaded
    def ready(self):
        # Import the 'signals' module when the app is ready to ensure signals are connected
        import users.signals


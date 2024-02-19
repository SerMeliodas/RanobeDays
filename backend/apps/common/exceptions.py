from django.db.models import Model


class AlreadyExistError(Exception):
    """Raised when the instance of model is already exist in data base"""

    def __init__(self, instance: Model):
        self.message = f"{instance.__class__.__name__} already have \
        the same instance in db"

        super.__init__(self.message)

from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50)
    pass_word = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    create_at = models.CharField(max_length=50)

    class Meta(object):
        db_table = 'user'

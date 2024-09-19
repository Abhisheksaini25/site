from django.db import models

# Create your models here.

class Fun(models.Model):

    email_2 = models.EmailField(max_length=100)

    def __str__(self):
        return self.email_2

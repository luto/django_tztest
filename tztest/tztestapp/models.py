from django.db import models


class Post(models.Model):
    posted = models.DateTimeField()

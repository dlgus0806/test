from django.db import models

class App(models.Model):
    title = models.CharField(max_length=200)
    write = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    
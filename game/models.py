from django.db import models

# Create your models here.


class Submit(models.Model):
    phone_number = models.CharField(blank=False, max_length=64)
    qr_id = models.IntegerField(blank=False)


class Slogan(models.Model):
    text = models.CharField(blank=False, max_length=3000)
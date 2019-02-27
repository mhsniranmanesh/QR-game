from django.db import models

# Create your models here.


class Barcode(models.Model):
    barcode_id = models.IntegerField(blank=False)
    text = models.CharField(blank=False, max_length=256)
    url = models.CharField(blank=True, max_length=256)

    def __str__(self):
        return self.text


class Submit(models.Model):
    phone_number = models.CharField(blank=False, max_length=64)
    barcode_id = models.IntegerField(blank=False)

    def __str__(self):
        return self.phone_number + ' - ' + str(self.barcode_id)


class Slogan(models.Model):
    text = models.CharField(blank=False, max_length=3000)

    def __str__(self):
        return self.text
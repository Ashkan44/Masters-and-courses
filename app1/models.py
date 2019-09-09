from django.db import models
from django.urls import reverse

# Create your models here.


class Master(models.Model):

    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    image = models.ImageField(null=True, blank=True)
    magers = models.CharField(max_length=15000, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    tel = models.IntegerField(max_length=13, null=True, blank=True)
    resome = models.CharField(max_length=15000)
    master_price = models.CharField(max_length=200, null=True, blank=True)
    comments = models.CharField(max_length=15000, null=True, blank=True)
    courses = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse("app1:Master_detail", kwargs={"pk": self.pk})

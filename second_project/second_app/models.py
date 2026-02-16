from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    science = models.IntegerField()
    english = models.IntegerField()
    total = models.IntegerField(blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)
    result = models.CharField(max_length=10)
    content = HTMLField(blank=True, null=True)



    def save(self, *args, **kwargs):
        self.total = self.science + self.english
        self.percentage = self.total / 3
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)
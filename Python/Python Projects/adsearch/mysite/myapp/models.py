from django.db import models

# Create your models here.
class Tag(models.Model):
    tagname = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.tagname

class Advert(models.Model):
    name = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='images/')
    ad_url = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.name

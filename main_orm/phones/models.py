from django.db import models


class Phone(models.Model):
    objects = None
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exist = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return f"{self.id}; {self.name}; {self.price}; {self.image}; {self.release_date}; {self.lte_exist}; {self.slug}"

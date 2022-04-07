from django.db import models
from django.urls import reverse
# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=70)
    rating = models.IntegerField()
    # author = models.CharField(max_length=50)
    year = models.IntegerField(null=True)
    price = models.IntegerField(default=100)
    is_best_selling = models.BooleanField(default=False)
    author = models.CharField(max_length=100, null=True)

    def get_url(self):
        return reverse('book-detail', args=[self.id])

    def __str__(self):
        return f'{self.title} - {self.rating}%'


# python manage.py shell_plus --print-sql

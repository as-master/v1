from django.db import models
from django.urls import reverse
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100, default='Ivanov')
    birth_date = models.IntegerField(null=True)
    death_date = models.IntegerField(default='still alive')

    def __str__(self):
        return f'{self.name}'


class PublishingOffice(models.Model):
    name = models.CharField(max_length=100, default='independant')
    adress = models.CharField(max_length=30, default='Moskov')
    mail = models.CharField(max_length=30, default='zzz@mail.com')

class Book(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'

    CURRENCY_CHOICES = [
        ('E', 'Euros'),
        ('D', 'Dollars'),
        ('R', 'Rubles'),
    ]

    title = models.CharField(max_length=70)
    rating = models.IntegerField()
    # author = models.CharField(max_length=50)
    currency = models.CharField(max_length=2, choices=CURRENCY_CHOICES, default='R')
    year = models.IntegerField(null=True)
    price = models.IntegerField(default=100)
    is_best_selling = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True)
    publishing_offices = models.ManyToManyField(PublishingOffice, null=True)

    def get_url(self):
        return reverse('book-detail', args=[self.id])

    def __str__(self):
        return f'{self.title} - {self.rating}%'





# python manage.py shell_plus --print-sql

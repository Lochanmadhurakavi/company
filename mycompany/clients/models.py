from tkinter import Widget
from django.db import models


# Create your models here.
class Apply(models.Model):
    title_choices = [('Mr', 'Mr'), ('Ms', 'Ms'), ('Mrs', 'Mrs')]
    title = models.CharField(max_length=3, choices=title_choices)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # birth_date = models.DateTimeField()
    # status = [('Single', 'Single'), ('Married', 'Married'), ('Other', 'Other')]
    # martial_status = models.CharField(max_length=10, choices=status)
    # email = models.EmailField()
    # phone_no = models.IntegerField()
    # address_1 = models.CharField(max_length=200)
    # address_2 = models.CharField(max_length=200)
    # city = models.CharField(max_length=200)
    # state = models.CharField(max_length=200)
    # zipcode = models.IntegerField()

    # years = [('0-1 years', '0-1 years'), ('1-2 years', '1-2 years'), ('2-3 years', '2-3 years'), ('3-4 years', '3-4 years'), ('5+ years', '5+ years')]
    # years_present = models.CharField(max_length= 15, choices=years)


    def str(self):
        return self.first_name

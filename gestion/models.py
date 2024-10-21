from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']



class Member(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    blocked = models.BooleanField(default=False)
    def __str__(self):
        return self.lastname + ' ' + self.firstname

    class Meta:
        unique_together = (('firstname', 'lastname'),)
        ordering = ['lastname']


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    loandate = models.DateField(null=True, blank=True)
    available = models.BooleanField(default=True)
    borrower = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name + ' par ' + self.author

    class Meta:
        ordering = ['name']
        unique_together = (('name', 'author'),)


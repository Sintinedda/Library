from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, )
    parution = models.DateField()
    available = models.BooleanField(default=True)
    CAT_CHOICES = {
        'Livre': 'Livre',
        'Cd': 'Cd',
        'Dvd': 'Dvd',
        'Tabletop': 'Tabletop',
    }
    category = models.CharField(choices=CAT_CHOICES, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        unique_together = ('name', 'category')


class Livre(Item):
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' ' + self.author


class Cd(Item):
    interpreter = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' ' + self.interpreter


class Dvd(Item):
    realisator = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' ' + self.realisator


class Tabletop(Item):
    creator = models.CharField(max_length=100)
    available = None

    def __str__(self):
        return self.name + ' ' + self.creator


class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        name = f'{self.firstname} {self.lastname}'
        return name

    class Meta:
        ordering = ['lastname', 'firstname']
        unique_together = ('firstname', 'lastname')


class Loan(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f'{self.member} {self.item} {self.date}'

    class Meta:
        unique_together = ('member', 'item', 'date')
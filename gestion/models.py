from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parution = models.DateField()
    available = models.BooleanField(default=True)
    CAT_CHOICES = {
        ('Livre', 'Livre'),
        ('Cd', 'Cd'),
        ('Dvd', 'Dvd'),
        ('Tabletop', 'Jeu de plateau')
    }
    category = models.TextField(choices=CAT_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Livre(Item):
    author = models.CharField(max_length=100)
    nbpage = models.IntegerField()
    TYPE_BOOKS = {
        ('Roman', 'Roman'),
        ('Nouvelle', 'Nouvelle'),
        ('Fantasy', 'Fantastique'),
        ('Polar', 'Polar'),
        ('Bio', 'Biographie'),
        ('Contes', 'Contes'),
        ('Essai', 'Essai'),
        ('Poésie', 'Poésie'),
        ('Manga', 'Manga'),
        ('Théâtre', 'Théâtre'),
        ('BD', 'Bande dessinée')
    }
    type = models.TextField(choices=TYPE_BOOKS)

    def __str__(self):
        return self.name + ' ' + self.author


class Cd(Item):
    interpreter = models.CharField(max_length=100)
    type = models.TextField('Album', 'Single', 'Compilation')
    STYLE_CHOICES = {
        ('Pop', 'Pop'),
        ('Rock', 'Rock'),
        ('Hip-hop', 'Hip-hop'),
        ('Électro', 'Électro'),
        ('Jazz', 'Jazz'),
        ('Classique', 'Classique'),
        ('Reggae', 'Reggae'),
        ('Rap', 'Rap'),
        ('Country', 'Country'),
        ('Blues', 'Blues'),
        ('Métal', 'Métal')
    }
    style = models.TextField(choices=STYLE_CHOICES)

    def __str__(self):
        return self.name + ' ' + self.interpreter


class Dvd(Item):
    realisator = models.CharField(max_length=100)
    duration = models.TimeField()
    pg = models.IntegerField()
    STYLE_DVD = {
        ('A/A', 'Action/Aventure'),
        ('Comédie', 'Comédie'),
        ('Drame', 'Drame'),
        ('Fantasy', 'Fantastique'),
        ('Guerre', 'Guerre'),
        ('Policier', 'Policier'),
        ('Horreur', 'Horreur'),
        ('Western', 'Western'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Doc', 'Documentaire'),
        ('Anime', 'Dessin animé')
    }
    style = models.TextField(choices=STYLE_DVD)

    def __str__(self):
        return self.name + ' ' + self.realisator


class Tabletop(Item):
    creator = models.CharField(max_length=100)
    nbplayers = models.CharField(max_length=100)
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
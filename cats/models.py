from django.db import models
from datetime import datetime

CHOICES = (
    ('Gray', 'Серый'),
    ('Black', 'Чёрный'),
    ('White', 'Белый'),
    ('Ginger', 'Рыжий'),
    ('Mixed', 'Смешанный'),
)


class Achievement(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Owner(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class FavoriteToy(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Cat(models.Model):
    class Meta:
        db_table = 'cats'
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    birth_year = models.IntegerField(null=True)
    owner = models.ForeignKey(
        Owner, related_name='cats', on_delete=models.CASCADE)
    achievements = models.ManyToManyField(
        Achievement, through='AchievementCat')
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    is_purebred = models.BooleanField(default=False)
    favorite_toy = models.ForeignKey(
        FavoriteToy, on_delete=models.PROTECT, related_name='cats')
    deleted = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

    def delete(self):
        self.deleted = datetime.now()
        self.save()


class AchievementCat(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.achievement} {self.cat}'

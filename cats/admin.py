from django.contrib import admin
from .models import Cat, Owner, AchievementCat, Achievement, FavoriteToy


class CatAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'color', 'birth_year', 'owner',
                    'achievements_cats', 'created', 'changed', 'is_purebred', 'favorite_toy', 'deleted')
    search_fields = ('name',)
    list_filter = ('name',)

    def achievements_cats(self, cats):
        return [achievement.name for achievement in cats.achievements.all()]


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'cats')

    def cats(self, owner):
        return [cat.name for cat in owner.cats.all()]


class AchievementAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


class AchievementCatAdmin(admin.ModelAdmin):
    list_display = ('achievement', 'cat')


class FavoriteToyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'cats')

    def cats(self, toy):
        return [cat.name for cat in toy.cats.all()]


admin.site.register(Cat, CatAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(AchievementCat, AchievementCatAdmin)
admin.site.register(FavoriteToy, FavoriteToyAdmin)

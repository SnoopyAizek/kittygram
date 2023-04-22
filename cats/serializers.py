from rest_framework import serializers
from .models import Cat, Owner, Achievement, AchievementCat, FavoriteToy


class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievement
        fields = ('id', 'name')


class CatSerializer(serializers.ModelSerializer):
    achievements = AchievementSerializer(many=True, required=False)

    class Meta:
        model = Cat
        fields = ('id', 'name', 'color', 'birth_year', 'owner',
                  'achievements', 'created', 'changed', 'is_purebred', 'favorite_toy', 'deleted')

    def create(self, validated_data):
        if 'achievements' not in self.initial_data:
            cat = Cat.objects.create(**validated_data)
            return cat
        achievements = validated_data.pop('achievements')
        cat = Cat.objects.create(**validated_data)
        for achievement in achievements:
            current_achievement, status = Achievement.objects.get_or_create(
                **achievement)
            AchievementCat.objects.create(
                achievement=current_achievement, cat=cat)
        return cat


class OwnerSerializer(serializers.ModelSerializer):
    cats = CatSerializer(many=True, required=False)

    class Meta:
        model = Owner
        fields = ('id', 'first_name', 'last_name', 'cats')


class FavoriteToySerializer(serializers.ModelSerializer):
    cats = CatSerializer(many=True, required=False)

    class Meta:
        model = FavoriteToy
        fields = ('id', 'name', 'cats')

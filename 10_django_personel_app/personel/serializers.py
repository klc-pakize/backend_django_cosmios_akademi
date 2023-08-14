from rest_framework import serializers

from .models import Departman, Personel

from django.utils.timezone import now


class DepartmanSerializer(serializers.ModelSerializer):

    count = serializers.SerializerMethodField()

    class Meta:
        model = Departman
        fields = "__all__"


    def get_count(self, obj):
        return obj.personels.count()
    

class PersonelSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()  # read_only
    user_id = serializers.IntegerField(read_only=True)
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = Personel
        fields = "__all__"

    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        instance = Personel.objects.create(**validated_data)
        return instance
    
    def get_days_since_joined(self, obj):
        return (now() - obj.start_date).days
    

class DepartPersonelSerializer(serializers.ModelSerializer):

    personels = PersonelSerializer(many=True, read_only = True)
    count = serializers.SerializerMethodField()

    class Meta:
        model = Departman
        fields = "__all__"


    def get_count(self, obj):
        return obj.personels.count()
    
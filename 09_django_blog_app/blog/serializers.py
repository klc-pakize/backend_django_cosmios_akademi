from rest_framework import serializers

from .models import Category, Post

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )


class PostSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()  # read_only
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            "category",
            'category_id',
            "status",
            "created_date",
            "updated_date"
        )
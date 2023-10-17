from rest_framework import serializers

from .models import Category, Blog, Comment, Likes, PostViews


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # read_only
    blog = serializers.StringRelatedField()
    blog_id = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'blog',
            'blog_id',
            'content',
            'time_stamp'
        )

    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        instance = Comment.objects.create(**validated_data)
        return instance
    

class LikesSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    blog = serializers.StringRelatedField()
    blog_id = serializers.IntegerField()

    class Meta:
        model = Likes
        fields = (
            'id',
            'user',
            'user_id',
            'blog',
            'blog_id',
        )
        
    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        instance = Likes.objects.create(**validated_data)
        return instance


class PostViewSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    blog = serializers.StringRelatedField()
    blog_id = serializers.IntegerField()

    class Meta:
        model = PostViews
        fields = (
            'id',
            'user',
            'user_id',
            'blog',
            'blog_id',
            'post_view',
            'time_stamp',
        )

    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        instance = PostViews.objects.create(**validated_data)
        return instance


class BlogSerializer(serializers.ModelSerializer):

    cotegory = serializers.StringRelatedField()  # read_only
    cotegory_id = serializers.IntegerField()
    user = serializers.StringRelatedField()
    comment_count = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    post_view = serializers.SerializerMethodField()
    comments = CommentSerializer(many = True, read_only = True)
    likes_n = LikesSerializer(many = True, read_only = True)
    post_views = PostViewSerializer(many = True, read_only = True)




    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'content',
            'image',
            'cotegory',
            'cotegory_id',
            'publish_date',
            'user',
            'user_id',
            'status', 
            'comment_count',
            'comments',
            'likes',
            'likes_n',
            'post_view',
            'post_views',
        )

    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        instance = Blog.objects.create(**validated_data)
        return instance
    
    #! Toplam kaç yorum yapıldığını hesaplar:
    def get_comment_count(self, obj):
        return Comment.objects.filter(blog = obj.id).count()
    
     #! like sayısını hesaplar:
    def get_likes(self, obj):
        return Likes.objects.filter(likes = True, blog = obj.id).count()
    
    #! Blogların görüntülenme sayısını hesaplar:
    def get_post_view(self, obj):
        return PostViews.objects.filter(post_view = True, blog = obj.id).count()
    

class UserBlogSerializer(serializers.ModelSerializer):

    cotegory = serializers.StringRelatedField()  # read_only
    cotegory_id = serializers.IntegerField()
    user = serializers.StringRelatedField()
    comment_count = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    post_view = serializers.SerializerMethodField()
    comments = CommentSerializer(many = True, read_only = True)
    likes_n = LikesSerializer(many = True, read_only = True)
    post_views = PostViewSerializer(many = True, read_only = True)


    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'content',
            'image',
            'cotegory',
            'cotegory_id',
            'publish_date',
            'user',
            'user_id',
            'comment_count',
            'comments',
            'likes',
            'likes_n',
            'post_view',
            'post_views',
        )

    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        instance = Blog.objects.create(**validated_data)
        return instance
    
    #! Toplam kaç yorum yapıldığını hesaplar:
    def get_comment_count(self, obj):
        return Comment.objects.filter(blog = obj.id).count()
    
     #! like sayısını hesaplar:
    def get_likes(self, obj):
        return Likes.objects.filter(likes = True, blog = obj.id).count()
    
    #! Blogların görüntülenme sayısını hesaplar:
    def get_post_view(self, obj):
        return PostViews.objects.filter(post_view = True, blog = obj.id).count()



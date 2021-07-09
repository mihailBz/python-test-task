from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return user

    class Meta:
        model = UserModel
        fields = (
            "id",
            "username",
            "password",
        )


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Post
        fields = (
            "title",
            "link",
            "creation_date",
            "amount_of_upvotes",
            "author",
        )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Comment
        fields = (
            "author",
            "content",
            "creation_date",
        )

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)

from django.contrib.auth import get_user_model
from django.db.models import F

from .models import Post, Comment, User, Upvote
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from .utils import get_user_by_token
from .mixins import EnablePartialUpdateMixin


# # Create your views here.


class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer

    model = get_user_model()
    permissions = [AllowAny]


class PostView(CreateAPIView, ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        author = get_user_by_token(self.request)
        return serializer.save(author=author)


class SinglePostView(EnablePartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(author=get_user_by_token(self.request).id)


class CommentView(CreateAPIView, ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs["post_id"])

    def perform_create(self, serializer):
        author = get_user_by_token(self.request)
        post_id = self.kwargs["post_id"]
        return serializer.save(author=author, post_id=post_id)


class SingleCommentView(EnablePartialUpdateMixin, RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(
            post=self.kwargs["post_id"], author=get_user_by_token(self.request).id
        )


class UpvoteView(APIView):
    def post(self, request, post_id):
        user_id = get_user_by_token(request).id
        if Post.objects.filter(pk=post_id).exists():
            if not Upvote.objects.filter(post_id=post_id, user_id=user_id).exists():
                liked_post = Post.objects.get(pk=post_id)
                liked_post.amount_of_upvotes = F("amount_of_upvotes") + 1
                liked_post.save()

                Upvote.objects.create(
                    post=liked_post, user=User.objects.get(pk=user_id)
                )

                return Response(
                    {"message": "user `{}` upvoted `{}` post".format(user_id, post_id)}
                )
            return Response(
                {
                    "message": "user `{}` already upvoted post `{}`".format(
                        user_id, post_id
                    )
                }
            )
        return Response(status=404)

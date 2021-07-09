from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import PostView, SinglePostView, CommentView, SingleCommentView, UpvoteView

urlpatterns = [
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("signup/", views.CreateUserView.as_view(), name="signup"),
    path("posts/", PostView.as_view(), name="posts"),
    path("posts/<int:pk>/", SinglePostView.as_view(), name="post"),
    path("posts/<int:post_id>/comments/", CommentView.as_view(), name="comments"),
    path(
        "posts/<int:post_id>/comments/<int:pk>/",
        SingleCommentView.as_view(),
        name="comment",
    ),
    path("posts/<int:post_id>/upvotes/", UpvoteView.as_view(), name="upvote"),
]

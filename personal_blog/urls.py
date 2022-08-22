from django.urls import path
from .views import post_detail, post_draft_list, post_list, post_create, post_publish, post_delete, post_edit

urlpatterns = [
    path("", post_list),
    path("post-detail/<int:pk>/", post_detail, name="post-detail"),
    path("post-create/", post_create, name="post-create"),
    path("post-draft-list/", post_draft_list, name="post-draft-list"),
    path("post-publish/<int:pk>/", post_publish, name="post-publish"),
    path("post-delete/<int:pk>/", post_delete, name="post-delete"),
    path("post-edit/<int:pk>/", post_edit, name="post-edit"),
]

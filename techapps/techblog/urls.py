from django.urls import path
app_name = "techblog"

from .views import BlogListView
urlpatterns = [
    # path('post/', PostFieldList.as_view(), name='post'),
    # path('<slug:slug>/', PostListDetials.as_view()),
    # path('<slug:slug>/', CommentsList.as_view()),
    # path('<slug:slug>/send/', CreateComment.as_view()),
    path('blog-list/', BlogListView.as_view(), name="blog-list")
]
 
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.views.generic import TemplateView
from techapps.techblog.models import PostField, Comment


class BlogListView(TemplateView):
    """
    Pagina de quienes somos
    """
    template_name = "techblog/blog-list.html"

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        return context


# class PostFieldList(ListAPIView):
#     """
#     display the list of all the post from database.
#     """
    
#     serializer_class = PostFieldSerializers

#     def get_queryset(self):
#         recent = self.request.query_params.get('recent')
#         if recent == 'true':
#             return PostField.objects.all()[:4]
        
#         return PostField.objects.all()
    
#     @swagger_auto_schema(Response={200: PostFieldSerializers(many=True)})
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)
    
# class PostListDetials(APIView):

#     """
#     details about the information posted 
#     """
#     @swagger_auto_schema(responses={200: PostFieldSerializers(), 404: openapi.Response(description='Not Found')})
#     def get(self, request: Request, slug: str, format=None):
#         post = get_object_or_404(PostField, slug=slug)

#         data = PostFieldSerializers(post).data
#         return Response(data, status=status.HTTP_200_OK)
    
# class CommentsList(APIView):
#     """
#     List of Comments

#     Return a list of all **Comments** that belong to Post with given ``slug``.
#     """

#     @swagger_auto_schema(responses={200: CommentSerializer(many=True), 404: openapi.Response(description='Not Found')})
#     def get(self, request: Request, slug: str, format=None):
#         post = get_object_or_404(PostField, slug=slug)

#         comments = Comment.objects.filter(post_id=post.id)
#         data = CommentSerializer(comments, many=True).data

#         return Response(data, status=status.HTTP_200_OK)


# class CreateComment(APIView):
#     """
#     Create Comment

#     Create comment under the post with given ``slug``.
#     """

#     @swagger_auto_schema(request_body=CreateCommentSerializer(), responses={200: CommentSerializer(), 400: openapi.Response(description='Serializer error', examples={'application/json': CreateCommentSerializer().error_messages}), 403: openapi.Response(description='Forbidden'), 404: openapi.Response(description='Not Found'), 429: openapi.Response(description='Too Many Requests')})
#     def post(self, request: Request, slug: str, format=None):
#         serializer = CreateCommentSerializer(data=request.data)

#         if not self.request.session.exists(self.request.session.session_key):
#             self.request.session.create()

#         # Stop user from spamming comments
#         if self.request.session.has_key('comment_posted'):
#             delta = round((self.request.session['comment_posted'] +
#                            60) - datetime.now().timestamp())

#             if delta > 0:
#                 return Response({'Too Many Requests': f'Please wait {delta} more seconds before sending another comment.'}, status=status.HTTP_429_TOO_MANY_REQUESTS)
#             else:
#                 self.request.session.pop('comment_posted')

#         if serializer.is_valid():
#             if request.user.is_verified:
#                 post = get_object_or_404(PostField, slug=slug, is_public=True)

#                 body = serializer.data.get('body')

#                 comment = Comment(author=request.user, post=post, body=body)
#                 comment.save()

#                 self.request.session['comment_posted'] = datetime.now(
#                 ).timestamp()

#                 return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)

#             return Response({'detail': 'Please activate your account first.'}, status=status.HTTP_403_FORBIDDEN)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

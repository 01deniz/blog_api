from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


# @api_view()
# def posts_list(request):
#     queryset = Post.objects.all()
#     serializer = PostSerializer(queryset, many=True, context={'request': request}) #many-потому что queryset - это лист объектов
#     return Response(data=serializer.data, status=status.HTTP_200_OK) #serializer просто не передавать, применять .data

class PostsListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def get_serializer_context(self):
    #     return {'request': self.request} #если нужен request, к нему можно так обратиться  (APIView)

    # def get(self, request, format=None): #APIView наследование
    #     queryset = Post.objects.all()
    #     serializer = PostSerializer(queryset, many=True, context={'request': request})
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)


class PostDetailsView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreatePostView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data #request.POST в Django, то что пришло от пользователя
        serializer = PostSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        # post.author = request.user
        # post.save()
        serializer = PostSerializer(instance=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdatePostView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DeletePostView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#TODO: FBV
#TODO: CBV
#TODO: CRUD
#TODO: Viewsets
#TODO: Pagination
#TODO: Search
#TODO: Filtering
#TODO: Permission
#TODO: Get aouthor from request

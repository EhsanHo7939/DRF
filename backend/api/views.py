from .permissions import IsSuperUserOrStaffReadOnly_List, IsSuperUserOrStaffReadOnly_Detail, IsAuthorOrReadOnly, IsStaffOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView
# from rest_framework.response import Response
from .serializers import ArticleSerializer, UserSerializer
from django.contrib.auth import get_user_model
from blog.models import Article


# Create your views here.

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ["status", "author"]
    ordering_fields = ["publish", "status"]
    search_fields = [
        "title",
        "content",
        "author__username",
        "author__first_name",
        "author__last_name"
    ]

class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly,)


class UserList(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly_List,)
    filterset_fields = ["is_superuser", "is_staff", "is_active"]


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly_Detail,)


# class RevokeToken(APIView):
#     permission_classes = (IsAuthenticated,)

#     def delete(self, request):
#         request.auth.delete()
#         return Response(status=204)

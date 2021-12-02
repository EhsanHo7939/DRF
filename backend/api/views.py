from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsSuperUserOrStaffReadOnly_List, IsSuperUserOrStaffReadOnly_Detail, IsAuthorOrReadOnly, IsStaffOrReadOnly
from blog.models import Article
from django.contrib.auth.models import User
from .serializers import ArticleSerializer, UserSerializer


# Create your views here.

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly,)


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly_List,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly_Detail,)


class RevokeToken(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        request.auth.delete()
        return Response(status=204)

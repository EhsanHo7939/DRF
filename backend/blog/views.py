from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from .models import Article


# Create your views here.

class ArticleList(ListView):
    def get_queryset(self):
        return Article.objects.filter(status=True)


class ArticleDetail(DetailView):
    def get_object(self):
        return get_object_or_404(
            Article.objects.filter(status=True),
            pk=self.kwargs.get("pk")
            )


class UserList(ListView):
    def get_queryset(self):
        return User.objects.filter(is_active=True)


class UserDetail(DetailView):
    def get_object(self):
        return get_object_or_404(
            User.objects.filter(is_active=True),
            pk=self.kwargs.get("pk")
        )

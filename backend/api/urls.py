from django.urls import path, include
from .views import ArticleList, ArticleDetail, UserList, UserDetail
# from rest_framework.authtoken.views import obtain_auth_token
# from api.views import RevokeToken


app_name = "api"


urlpatterns = [
    path("", ArticleList.as_view(), name="list"),
    path("<int:pk>", ArticleDetail.as_view(), name="detail"),
    path("users/", UserList.as_view(), name="user_list"),
    path("users/<int:pk>", UserDetail.as_view(), name="user_detail"),
    path('auth/', include('dj_rest_auth.urls'), name="authentication"),
    path('auth/registration/', include('dj_rest_auth.registration.urls'), name="registration"),
    # path("token-auth/", obtain_auth_token, name="obtain_token"),
    # path("token-revoke/", RevokeToken.as_view(), name="revoke_token"),
]

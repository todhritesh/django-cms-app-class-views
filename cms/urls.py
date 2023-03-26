from django.urls import path
from .views import *
urlpatterns = [
    path('',PostCategoryListView.as_view(),name="post_category_listview"),
    path('login/',LoginFormView.as_view(),name="login_formview"),
    path('logout/',LogoutView.as_view(),name="logout_view"),
]

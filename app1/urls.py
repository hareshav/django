from django.urls import path
from . import views
urlpatterns=[
    path('', views.index,name='index'),
    path('signup/', views.signup,name="signup"),
    path('signin/', views.signin,name="signin"),
    path('home/', views.home,name="home"),
    path('logout/',views.logoutuser,name="logout"),
    path('home/apply/',views.apply,name="apply"),
    path('home/search/',views.search,name='search'),
]
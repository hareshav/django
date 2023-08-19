from django.urls import path
from . import views
urlpatterns=[
    # path('', views.index,name='index'),
    path('signup/', views.signup,name="signup"),
    path('signin/', views.signin,name="signin"),
    path('', views.home,name="home"),
    path('logout/',views.logoutuser,name="logout"),
    path('apply/',views.apply,name="apply"),
    path('localsearch/',views.searchlocal,name='localsearch'),
    path('remotesearch/',views.searchglobal,name='remotesearch'),
]
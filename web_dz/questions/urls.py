from django.urls import path, include, re_path

from . import views


urlpatterns = [
    path('', views.MainView.as_view(),name="index"),
    re_path(r'^question/(?P<questions_id>[0-9]+)/$', views.question, name="question"),
    path('hot/', views.hot, name="hot" ),
    re_path(r'^tag/(?P<tag_name>\w+)/$', views.tag, name="tag" ),
    path('login/', views.login, name="login" ),
    path('logout/', views.logout, name="logout" ),
    path('register/', views.register, name="register" ),
    path('ask/', views.ask, name="ask" ),
    path('settings/', views.settings, name="settings"),
]
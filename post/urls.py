from django.urls import path
from .views import HomePageView,usauariosView, UpdatePageVienw, DeletePageView
from post.views import CreateView,DetailPageVieW
urlpatterns= [
    path("", HomePageView.as_view(), name = "post"), 
    path("usuarios",usauariosView.as_view(),name="usuarios"),
    path("post/create",CreateView.as_view(),name="create"),
    path("post/detail/<int:pk>",DetailPageVieW.as_view(),name="detail"),

    path("post/detail/<int:pk>/update",UpdatePageVienw.as_view(),name="update"),
    path("post/detail/<int:pk>/",DetailPageVieW.as_view(),name="detail"),
    path("post/detail/<int:pk>/delate",DeletePageView.as_view(),name="delete"),

]


from django.urls import path
from . import views
# from main.views import Page, AddLike, AddLike2Comment

urlpatterns = [
    path('', views.index, name='home' ),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    # path('add_like/<int:id>/', AddLike.as_view(), name='add-like'),
    # path('add_like_to_comment/<int:id>/', AddLike2Comment.as_view(), name='add-like-to-comment'),
    # path('', Page.as_view(), name='the-main-page'),
]

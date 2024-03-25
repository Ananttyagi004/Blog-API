from django.urls import path
from . import views

urlpatterns=[
    path('posts/',views.BlogList.as_view(),name='posts'),
    path('addpost/',views.AddPost.as_view(),name='addpost'),
    path('list/<int:pk>',views.PostDetail.as_view(),name='details')
]
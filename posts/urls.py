from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView
)

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('<path:path>', PostDetailView.as_view(), name='new'),
    path('new', PostCreateView.as_view(), name='new'),

]
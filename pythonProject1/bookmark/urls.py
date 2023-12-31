from django.urls import path
from .views import *

urlpatterns = [
    # http://127.0.0.1/bookmark/???
    # ???
                                        # 템플릿 불러올때 쓰는 이름
    path("", BookmarkListView.as_view(), name='list'),
    path("create/", BookmarkCreateView.as_view(), name='create'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),
    path("update/<int:pk>/",BookmarkUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/",BookmarkDeleteView.as_view(), name='delete'),
]
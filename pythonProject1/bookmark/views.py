import django.views.generic
from django.shortcuts import render

# Create your views here.
# CRUD : Create, Read, Update, Delete
# List

# 클래스형 뷰, 함수형 뷰
# 웹 페이지에 접속한다. -> 페이지를 본다.
# URL을 입력 -> 웹 서버가 뷰를 찾아서 동작시킨다. -> 응답

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from bookmark.models import Bookmark
from django.urls import reverse_lazy

# 상속
class BookmarkListView(ListView):
    # 데이터베이스 즉 모델 지정
    model = Bookmark
class BookmarkCreateView(CreateView):
    model = Bookmark
    # 생성이나 삭제할때는 fields 를 따로 지정해주어야 한다
    fields = ['site_name','url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'
    success_url = reverse_lazy('list')

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')





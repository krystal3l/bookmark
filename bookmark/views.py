from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Bookmark

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.views.generic.detail import DetailView



class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6

class BookmarkCreateView(CreateView):
    model = Bookmark                        # 어떤 모델의 입력을 받을 것인지 결정해야 하기 때문에 model 변수를 생성하고 Bookmark로 설정
    fields = ['site_name', 'url']           # 어떤 필드들을 입력받을 것인지 설정
    success_url = reverse_lazy('list')      # 글쓰기를 완료하고 이동할 페이지
    template_name_suffix = '_create'        # xxxx_create.html이라는 템플릿을 사용하겠다는 의미

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')

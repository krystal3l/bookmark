from django.contrib import admin
from .models import Bookmark    # models.py파일에서 Bookmark라는 모델을 불러오겠다는 의미

admin.site.register(Bookmark)   # 관리자 페이지에서 해당 모델을 관리할 수 있음.
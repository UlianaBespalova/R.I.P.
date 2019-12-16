from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import sys
sys.path.insert (0, "/home/uliana/project")
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path ('', views.index, name="index"),
    path ('hot/', views.hot_questions, name="hot"),
    path ('tag/<tg>/', views.tag_questions, name="tag"),
    path ('question/<int:qid>/', views.question, name="one-question"),
    path ('login/', views.login, name="login"),
    path ('logout/', views.logout, name="logout"),
    path ('signup/', views.signup, name="signup"),
    path ('ask/', views.ask, name="ask"),
    path ('settings/', views.settings, name="settings"),
] #+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#!сортировка по рейтингу
#переименовать в модели связь с лайками
# - рейтинг - должен пересчитывть в момент нажатия лайка
# - возвращать на страницу вопрса
#инстанс - связывает с указанной моедлью, инишиал - связывает через словарь
#теги поправлять не поправлять?
#что-то что я забыла  - в сэйве что-то там сделать
#стоп, так количество ответов яж как-то считаю, почему не считаются лайки
#полетела верстка удалить там скобочку


#!Настройки

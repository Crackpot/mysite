from django.urls import path

from . import views

# 在 polls/urls.py 文件中稍作修改，加上 app_name 设置命名空间
app_name = 'polls'
urlpatterns = [
    ########## 未优化的URLS ##########
    # # ex: /polls/
    # path('', views.index, name='index'),
    # # ex: /polls/5/
    # # the 'name' value as called by the {% url %} template tag
    # path('<int:question_id>/', views.detail, name='detail'),
    # # added the word 'specifics'
    # path('specifics/<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    ########## 优化后的URLS ##########
    path('', views.IndexView.as_view(), name='index'),
    # DetailView 期望从 URL 中捕获名为 "pk" 的主键值，所以我们为通用视图把 question_id 改成 pk 。
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

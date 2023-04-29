from django.urls import path
from . import views

urlpatterns = [
   path('', views.all_news_page, name='all-news-page'),
   path('game/<slug:slug>', views.detail_news_page, name='detail-news-page'),
   path('latest-news/', views.latest_news, name='latest-news'),
   path('about/', views.about_me, name='about')
]

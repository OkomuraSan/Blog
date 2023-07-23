from django.urls import path
from articles.views import home, archive, posts
app_name = 'articles'
urlpatterns = [
    path('', home, name='index'),
    path('page/<int:page>', home, name='paginator'),
    path('archive/', archive, name = "archive"),
    path('archive/<int:category_id>',archive, name = "category"),

]


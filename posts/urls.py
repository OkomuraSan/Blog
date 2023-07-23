from django.urls import path
from articles.views import posts

app_name = 'posts'
urlpatterns = [
path('<int:pk>', posts, name='post'),

]


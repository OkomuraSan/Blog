from django.db import models
from django.contrib.auth.models import User

class ArticlesCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name}"



class Articles(models.Model):
    name = models.CharField("Название статьи", max_length=256)
    descriptipn = models.CharField('Краткое описание статьи',max_length= 512)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='articles_images', null=True, blank=True)
    category = models.ManyToManyField(ArticlesCategory, related_name="artCat")
    views = models.PositiveIntegerField("просмотров", default=0)
    date = models.DateField('Дата публикации')


    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return f"{self.name} | {self.author}"
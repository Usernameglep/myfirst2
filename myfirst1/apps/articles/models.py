import datetime
from django.db import models
from django.db.models import CharField
from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField("Заголовок", max_length =200)
    article_text = models.TextField("Текст")
    article_img = models.CharField("ссылка", max_length =200)
    article_date = models.CharField("года", max_length =20)
    article_view = models.CharField("адрес", max_length=500)

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Alfa_Romeo(models.Model):
    car_title = models.CharField("Название авто", max_length =200)
    car_text = models.TextField("Описание авто")
    car_short_text = models.CharField("краткое описание", max_length=500)
    car_img = models.CharField("адрес фото", max_length =200)
    car_date = models.CharField("года выпуска", max_length =20)
    car_price = models.CharField("цена", max_length =20)

    def __str__(self):
        return self.car_title

    class Meta:
        verbose_name = 'Alfa Romeo'
        verbose_name_plural = 'Alfa Romeo'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name: CharField = models.CharField('имя автора', max_length=50)
    comment_text = models.CharField('текст комментария', max_length=200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комент'
        verbose_name_plural = 'Коменты'

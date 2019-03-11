from django.db import models

class News(models.Model):

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
    
    title = models.CharField("Название новости", max_length=150, db_index=True)
    slug = models.SlugField("Уникальный идентификатор, не повторять, писать слитно, и на англ.", max_length=150, unique=True)
    body = models.TextField("Содержание новости", db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)

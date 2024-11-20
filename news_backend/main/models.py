from django.db import models

class News(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    text = models.TextField(blank=True, null=True, verbose_name='Описание')
    date = models.DateField(blank=True, null=True, verbose_name='Дата')

    class Meta:
        db_table = 'news'
        verbose_name = 'Новости'
        ordering = ("id",)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Post(models.Model):
    """
    Это модель описывает структуру новости в бвзе данных
    """
    title = models.CharField(max_length=1000)
    description = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'информация'

    def __str__(self):
        return f'id:{self.id} {self.title}'
class Comment(models.Model):
    """
    Это модель описывает структуру новости в бвзе данных
    """
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_created=True)

    class Meta:
        verbose_name = 'Комментария'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'id:{self.id} {self.text}'



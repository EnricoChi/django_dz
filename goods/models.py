from django.db import models


class CommonModel(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(
        'Заголовок', max_length=255)
    is_published = models.BooleanField(
        'Опубликовать', default=False)
    created_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True)
    update_date = models.DateTimeField(
        'Дата обновления', auto_now=True, null=True)
    seo_title = models.CharField(
        'SEO Title', max_length=255, blank=True)
    seo_keywords = models.CharField(
        'SEO Keywords', max_length=255, blank=True)
    seo_description = models.CharField(
        'SEO Description', max_length=255, blank=True)
    sorting = models.IntegerField(
        'Сортировка', null=True, blank=True)


class Product(CommonModel):
    text = models.TextField(
        'Текст статьи', blank=True)
    category = models.ManyToManyField(
        'Category', verbose_name='Категории')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title


class Category(CommonModel):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

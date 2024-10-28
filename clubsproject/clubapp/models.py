from django.db import models
from pytils.translit import slugify


class Category(models.Model):
    name = models.CharField("Название категории", max_length=30)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


    def save(self,  *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ClubModels(models.Model):
    title = models.CharField("Ваканс",max_length=14, )
    cources = models.TextField("Курс",max_length=15)
    payment = models.IntegerField("цена",max_length=24)
    place = models.CharField("место",max_length=29, )
    date = models.DateTimeField("дата",auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name = 'выберите категорию')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title



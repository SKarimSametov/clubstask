from django.db import models
from pytils.translit import slugify
from datetime import datetime


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
    cources = models.CharField("Курс",max_length=15)
    payment = models.IntegerField("цена",max_length=24)
    brief_description = models.CharField("краткое описание:", max_length=83, default="None")
    full_description = models.TextField("Описание:", max_length=2200, default="None")
    groups = models.CharField("группы", max_length=500, default="None")
    members = models.IntegerField("участники", default=0)
    seats = models.IntegerField("места", default=0)
    place = models.CharField("место",max_length=29, )
    schedule = models.CharField("график", max_length=2200)
    # date = models.DateTimeField("дата",auto_now_add=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name = 'выберите категорию')
    date = models.DateTimeField("Дата публикации:",default=datetime.now)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title


# title
# cources
# payment
# place
# date

class Guide(models.Model):
    title = models.CharField("Заголовок", max_length=50)
    description = models.TextField("Описание гайда")
    image = models.CharField("URL фото", max_length=500)
    date = models.DateTimeField("Дата публикации:",default=datetime.now)

    class Meta:
        verbose_name = 'ГАйд'
        verbose_name_plural = 'Гайды'

    def __str__(self):
        return self.title

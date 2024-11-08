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
    title = models.CharField("Клуб",max_length=20)
    cources = models.CharField("Курс",max_length=15)
    payment = models.IntegerField("Цена", default="Бесплатно")
    brief_description = models.CharField("Краткое описание:", max_length=83, default="Нету")
    full_description = models.TextField("Описание:", max_length=2200, default="Нету")
    groups = models.CharField("группы", max_length=500, default="Нету")
    members = models.IntegerField("участники", default=0)
    seats = models.IntegerField("места", default=0)
    place = models.CharField("место",max_length=29)
    schedule = models.CharField("график", max_length=2200)
    image = models.CharField("Фото", max_length=10000, default="https://w7.pngwing.com/pngs/537/283/png-transparent-the-columbus-metropolitan-club-service-business-sales-building-none-building-text-service.png")
    # date = models.DateTimeField("дата",auto_now_add=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name = 'выберите категорию')
    date = models.DateTimeField("Дата публикации:",default=datetime.now)

    class Meta:
        verbose_name = 'Клуб'
        verbose_name_plural = 'Клубы'

    def __str__(self):
        return self.title


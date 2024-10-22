import os
from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель. Добавляет флаг is_published."""
    is_published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        abstract = True


class Category(PublishedModel):
    title = models.CharField(
        'Название',
        max_length=256,
        help_text='Уникальное название категории, не более 256 символов'
    )
    output_order = models.PositiveSmallIntegerField(
        'Порядок отображения',
        default=1000,
        help_text='Целое число, чем меньше, тем выше в выборке',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

        ordering = ("title",)

    def __str__(self):
        return self.title


class Pizza(PublishedModel):
    is_on_main = models.BooleanField('На главную', default=False)
    title = models.CharField(
        'Название',
        max_length=256,
        help_text='Уникальное название пиццы, не более 256 символов'
    )
    description = models.TextField(
        'Описание',
    )
    structure = models.TextField(
        'Состав',
    )
    size = models.PositiveSmallIntegerField(
        'Размер, см.',
        default=30,
        help_text='Целое число, по умолчанию 30',
    )
    output_order = models.PositiveSmallIntegerField(
        default=1000,
        verbose_name='Порядок отображения',
        help_text='Целое число, чем меньше, тем выше в выборке',
    )
    price = models.DecimalField(
        'Цена, руб.',
        max_digits=20,
        decimal_places=2,
        help_text='Десятичная дробь(2 знака после запятой), не более 20 знаков',
    )

    category = models.ManyToManyField(
        'Category',
        related_name='pizza',
        verbose_name='Категория',
    )

    image = models.ImageField('Фото', upload_to='pizza')

    def save(self, *args, **kwargs):
        try:
            this_record = Pizza.objects.get(id=self.id)
            if this_record.image != self.image:
                if os.path.isfile(this_record.image.path):
                    os.remove(this_record.image.path)
        except Pizza.DoesNotExist:
            pass

        super(Pizza, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super(Pizza, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'

        ordering = ('output_order', 'title')

    def __str__(self):
        return self.title

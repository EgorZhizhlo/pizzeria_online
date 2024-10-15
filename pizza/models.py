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

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'

        ordering = ('output_order', 'title')

    def __str__(self):
        return self.title

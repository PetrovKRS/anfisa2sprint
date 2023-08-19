from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField(max_length=256,
        verbose_name='Название',
        help_text='Уникальное название категории, не более 256 символов'
    )
    slug = models.SlugField(max_length=64, unique=True,
                            verbose_name='Слаг')
    output_order = models.PositiveSmallIntegerField(
        default=100,
        verbose_name='Порядок отображения'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Topping(PublishedModel):
    title = models.CharField(max_length=256,
        verbose_name='Название',
        help_text='Уникальное название начинки, не более 256 символов'
    )
    slug = models.SlugField(max_length=64, unique=True,
                            verbose_name='Слаг')

    class Meta:
        verbose_name = 'начинка'
        verbose_name_plural = 'Начинки'

    def __str__(self):
        return self.title


class Wrapper(PublishedModel):
    title = models.CharField(max_length=256,
        verbose_name='Название',
        help_text='Уникальное название обёртки, не более 256 символов'
    )

    class Meta:
        verbose_name = 'обертка'
        verbose_name_plural = 'Обертки'

    def __str__(self):
        return self.title


class IceCream(PublishedModel):
    title = models.CharField(max_length=256,
        verbose_name='Название',
        help_text='Уникальное название мороженого, не более 256 символов'
    )
    description = models.TextField(verbose_name='Описание')
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория'
    )
    toppings = models.ManyToManyField(Topping)
    is_on_main = models.BooleanField(default=False,
                                     verbose_name='На главную')

    class Meta:
        verbose_name = 'мороженое'
        verbose_name_plural = 'Мороженое'

    def __str__(self):
        return self.title

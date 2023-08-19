from django.contrib import admin

# Register your models here.
# Из модуля models импортируем модель Category...
from .models import Category, IceCream, Topping, Wrapper

# Этот вариант сработает для всех моделей приложения.
# Вместо пустого значения в админке будет отображена строка "Не задано".
admin.site.empty_value_display = 'Не задано'
categories_count = len(Category.objects.all())
# Подключим вставку сортов мороженого на страницу категории
# =========================================================
class IceCreamInline(admin.StackedInline):
    model = IceCream
    # Параметр extra определяет показывать(1) или нет(0) пустое дополнительное поле ввода
    # при вставке нового элемента
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines = (IceCreamInline,)
    list_display = ('title',)
# =========================================================

# Создаём класс, в котором будем описывать настройки админки:
class IceCreamAdmin(admin.ModelAdmin):
# В этом классе опишем все настройки, какие захотим.
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
    # Чтобы связанные записи можно было перекладывать из одного окошка в другое
    # Указываем, для каких связанных моделей нужно включить такой интерфейс:
    filter_horizontal = ('toppings',)



# Регистрируем новый класс:
# указываем, что для отображения админки модели IceCream
# вместо стандартного класса нужно нужно использовать класс IceCreamAdmin
# Регистрируем кастомное представление админ-зоны
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)

# Регистрируем модели Topping и Wrapper,
# чтобы ими можно было управлять через админку
# (интерфейс админки для этих моделей останется стандартным):
admin.site.register(Topping)
admin.site.register(Wrapper)

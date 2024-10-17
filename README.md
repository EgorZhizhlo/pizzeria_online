## Референсы проекта

### Проект в разработке!!!

# База данных
# Абстрактная модель PublishedModel
    is_published(BooleanField, default=True) - параметр отображения на сайте
## Модель Pizza(PublishedModel): 
    is_on_main(BooleanField, default=False) - параметр отображения на Главной
    title(CharField, max_length=256) - Уникальное название пиццы
    description(TextField, max_length=256) - Описание пиццы
    structure(TextField, max_length=256) - Состав пиццы(в обновлению сделаю связь многие ко многим для точечного поиска)
    size(PositiveSmallIntegerField, default=30) - Размер пиццы(в см)
    output_order(PositiveSmallIntegerField, default=1000) - Параметр ранжировки отображаемых на сайте пицц
    price(DecimalField, max_digits=20, decimal_places=2) - Цена(2 знака после запятой)
    category(ManyToManyField, 'Category') - Поле связи многие ко многим между таблицами Category и Pizza
## Модель Category(PublishedModel)
    title(CharField, max_length=256) - Уникальное название категории
    output_order(PositiveSmallIntegerField, default=1000) - Параметр ранжировки отображения категорий

# Главная страница
![image](https://github.com/user-attachments/assets/88c20f5b-78a2-4c3b-82ac-a8c9ad1c1741)


# Каталог 
![image](https://github.com/user-attachments/assets/c0a651fa-e18d-4dcb-b7f5-de521d7246b5)


# Детализация
![image](https://github.com/user-attachments/assets/3bd645c4-bebb-4d2a-8c07-40e03263a4ec)


# Поиск пицц
### В проекте реализован мультипоиск по названию пиццы, категории, составу, описанию без учета регистра
![image](https://github.com/user-attachments/assets/45f42a0c-0f3e-44c5-9522-a36042e324de)

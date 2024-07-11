from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

# Категории
class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')

    def __str__(self):
        return self.title

    # Умная ссылка
    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Статьи
class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название статьи')
    content = models.TextField(verbose_name='Описание статьи')
    photo = models.ImageField(upload_to='photo/', blank=True, null=True, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изминения')
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', blank=True, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.pk})


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'



# Создать модель Comment
# Котарая знает Статью Пользователя Текст и Дату
# Создать форму для заполнения текста
# Улучшить Детали Статьи чтобы выводить форму, только если зарегестрировать
# Прописать вьюшку для сохранения комментария
# Доработать детали статьи для вывода комментариев
# Сделать куски HTML для вывода формы и комментариев


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')
    text = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profiles/', blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    publisher = models.BooleanField(default=False, verbose_name='Право создания статьи')

    def __str__(self):
        return self.user.username

    def get_photo(self):
        try:
            return self.photo.url
        except:
            return 'https://e7.pngegg.com/pngimages/265/535/png-clipart-computer-icons-silhouette-female-a-new-user-animals-head.png'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'










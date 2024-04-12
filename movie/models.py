from django.db import models
from user.models import MyUser
class Genre(models.Model):
    name = models.CharField(max_length=100) 
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'    

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.first_name + " " + self.last_name}'
    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'    

class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100) 
    def __str__(self):
        return f'{self.first_name + " " + self.last_name}'
    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'    

class Country(models.Model):
    name = models.CharField(max_length=100) 
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'    
        

class Company(models.Model):
    name = models.CharField(max_length=100) 
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Киностудия'
        verbose_name_plural = 'Киностудии'   

class Video(models.Model):
    video_file = models.FileField(upload_to='media/video')
    def __str__(self):
        return f"{self.video_file}"
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

class Image(models.Model):
    file = models.ImageField(upload_to='media/image')
    is_main = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.file}" 
    class Meta:
        verbose_name = 'Обложка'
        verbose_name_plural = 'Обложки'

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.PositiveIntegerField(null = True, blank = True)
    description = models.TextField()
    rating = models.DecimalField(max_digits = 3 , decimal_places = 1, null = True, blank = True)
    genres = models.ManyToManyField(Genre)
    directors = models.ManyToManyField(Director)
    actors = models.ManyToManyField(Actor)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,null = True, blank = True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,null = True, blank = True)
    image = models.ForeignKey(Image, on_delete = models.CASCADE,null = True, blank = True)
    video = models.ForeignKey(Video, on_delete = models.CASCADE,null = True, blank = True)
    created_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)
    is_published = models.BooleanField(default=True)
    user = models.ForeignKey(MyUser, verbose_name ='Пользователь', on_delete = models.CASCADE)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Favorite(models.Model):
    user = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} --> {self.movie}'
    
    class Meta:
        verbose_name = 'Избранный'
        verbose_name_plural = 'Избранныe'

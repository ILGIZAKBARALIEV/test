from django.db import models
from django.db import models




class Books(models.Model):
    GENRE_CHOICES = (
        ("DRAMA", "DRAMA"),
        ("ROMAN", "ROMAN"),
        ("FANTASY", "FANTASY"),
    )
    image = models.ImageField(upload_to='book_images/',verbose_name = 'загрузите фото')
    title =models.CharField(max_length=100,verbose_name= "укажите название книги ")
    description = models.TextField(verbose_name = "укажите описание книги ",blank=True)
    price = models.PositiveIntegerField(verbose_name= "укажите ценну ",default = 200)
    created_at =models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=10,choices=GENRE_CHOICES,default="DRAMA",
                             verbose_name = "выберите жанр")
    time = models.TimeField(verbose_name = "укажите время  ",blank=True)
    times = models.TimeField(verbose_name ="Укажите  время  просмотра ")
    director = models.CharField(max_length = 100, default =" Чынгыз Айтматов")
    trailer = models.URLField(verbose_name ="укажите ссыльку из Youtube")
    author = models.CharField(verbose_name="укажите автора ",max_length=30)
    mail = models.CharField(verbose_name="укажите почту  автора ",max_length=30)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "книгу"
        verbose_name_plural = "книги "
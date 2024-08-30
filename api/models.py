from django.db import models

class Gender(models.IntegerChoices):
    SHOUNEN = 1, 'Shounen'
    ISEKAI = 2, 'Isekai'
    SHOUJO = 3, 'Shoujo'
    SEINEN = 4, 'Seinen'
    ACTION = 5, 'Action'
    THRILLER = 6, 'Thriller'
    ADVENTURE = 7, 'Adventure'
    HORROR = 8, 'Horror'
    FANTASY = 9, 'Fantasy'
    MECHA = 10, 'Mecha'
    OTHERS = 11, 'Others'

class Anime(models.Model):
    name = models.CharField(max_length=50, unique=True)
    gender = models.IntegerField(choices=Gender.choices)
    release_date = models.DateField(null=True, blank=True)
    seasons = models.IntegerField(null=True, blank=True)
    total_episodes = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='anime_images/', null=True, blank=True)
    dttm_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


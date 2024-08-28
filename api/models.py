from django.db import models

class Gender(models.IntegerChoices):
    SHOUNEN = 1, 'Shounen'
    ISEKAI = 2, 'Isekai'
    SHOUJO = 3, 'Shoujo'
    SEINEN = 4, 'Seinen'
    OTHERS = 5, 'Others'

class Anime(models.Model):
    name = models.CharField(max_length=50, unique=True)
    gender = models.IntegerField(choices=Gender.choices)
    release_date = models.DateField()
    seasons = models.IntegerField()
    total_episodes = models.IntegerField()
    image = models.ImageField(upload_to='anime_images/', null=True, blank=True)
    dttm_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


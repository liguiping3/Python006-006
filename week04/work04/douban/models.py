from django.db import models

# Create your models here.
class Film_comments(models.Model):
    # id 自动创建
    stars = models.IntegerField()
    content = models.CharField(max_length=1000)
   
    class Meta:
      db_table = "film_comments" 

from django.db import models

# Create your models here.
class Cars(models.Model):
    mark = models.CharField('Car mark' , max_length=50)
    year = models.IntegerField('Car year')

    def __str__(self):
        return self.mark
    
    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
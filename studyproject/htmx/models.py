from django.db import models

class task(models.Model):
    title = models.CharField(max_length=150)
    status = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title




# Create your models here.

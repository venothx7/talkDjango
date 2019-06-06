from django.db import models

# Create your models here.



class Talk(models.Model):
    id=models.IntegerField(db_index=True, primary_key=True)
    name = models.CharField(max_length=100)
    speaker = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    duration = models.DurationField()

    def __str__(self):
        return self.name
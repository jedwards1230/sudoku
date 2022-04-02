from django.db import models

class Puzzle(models.Model):
    size = models.IntegerField()
    difficulty = models.IntegerField()
    
    row1 = models.CharField(max_length=9)
    row2 = models.CharField(max_length=9)
    row3 = models.CharField(max_length=9)
    row4 = models.CharField(max_length=9)
    row5 = models.CharField(max_length=9)
    row6 = models.CharField(max_length=9)
    row7 = models.CharField(max_length=9)
    row8 = models.CharField(max_length=9)
    row9 = models.CharField(max_length=9)
    
    created_time = models.DateTimeField('time published')
    elapsed_time = models.DateTimeField('time finished')
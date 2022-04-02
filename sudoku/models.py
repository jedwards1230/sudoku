from django.db import models

class Puzzle(models.Model):    
    puzzle = models.TextField(null=True)
    
    size = models.IntegerField()
    difficulty = models.IntegerField()
    
    created_time = models.DateTimeField('time published', null=True)
    elapsed_time = models.DateTimeField('time finished', null=True)
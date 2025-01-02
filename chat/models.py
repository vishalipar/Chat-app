from django.db import models

# Create your models here.

class ChatModel(models.Model):
    room_no = models.CharField(max_length= 100)
    message = models.TextField()
    
    def __str__(self):
        return f'{self.room_no} {self.message}'
    
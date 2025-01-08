from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Review(models.Model):
    movie_title = models.CharField(max_length=255,unique= True)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.movie_title} - {self.rating}/5"

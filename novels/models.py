from django.db import models

# Create your models here.
class Novel(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    summary = models.TextField()
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)  # New!
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
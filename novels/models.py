from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Novel(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    summary = models.TextField()
    content = models.TextField(blank=True)  # Full book content
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)  # New!
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'novel')

    def __str__(self):
        return f"{self.user.username} bookmarked {self.novel.title}"

class ReadingProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    progress = models.FloatField(default=0.0)  # Percentage or position
    last_read = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'novel')

    def __str__(self):
        return f"{self.user.username} progress on {self.novel.title}: {self.progress}%"
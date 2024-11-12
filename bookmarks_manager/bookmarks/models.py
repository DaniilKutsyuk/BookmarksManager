from django.db import models

class Bookmark(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    category = models.CharField(max_length=100, blank=True, null=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.category})"
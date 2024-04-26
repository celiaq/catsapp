from django.db import models
from django.contrib.auth.models import User


class CatPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    image = models.ImageField(upload_to='cats_app/static/cat_photos/', max_length=50)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author_name} - {self.date_added}"
    
    class Meta:
        app_label = "cats_app"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(CatPost, on_delete=models.CASCADE, related_name='comment_photos')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.user.username} - {self.text}"
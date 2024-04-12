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

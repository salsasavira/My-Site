from django.db import models

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment

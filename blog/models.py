from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200]+"..."

    def show_pub_date(self):
        return self.pub_date.strftime('%b %e %Y')

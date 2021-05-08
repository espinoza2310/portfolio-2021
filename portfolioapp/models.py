from django.db import models

# Create your models here.
class Home(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    Tech=models.CharField(max_length=50)
    image=models.ImageField(upload_to='home')
    project_link = models.URLField(max_length=100)
    github_link = models.URLField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='home'
        verbose_name_plural='houses'

    def __srt__(self):
        return self.title()

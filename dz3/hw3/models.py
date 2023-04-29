from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    

class review(models.Model):
    review_text = models.CharField(max_length=200)

    def __str__(self):
        return self.review_text




class PublishedTime(models.Model):
    published_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.published_time



class Post(models.Model):
    author = models.CharField('', max_length=200)
    review = models.CharField('', max_length=200)
    PublishedTime = models.DateTimeField(null=True, blank=True)
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.author
 
    
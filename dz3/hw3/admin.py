from django.contrib import admin
from hw3.models import review, PublishedTime, Post
# Register your models here.

@admin.register(review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_text')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'review', 'PublishedTime','like', 'dislike',)
    search_field = ['author', 'review', 'PublishedTime','like', 'dislike',]

    
@admin.register(PublishedTime)
class PublishedAdmin(admin.ModelAdmin):
    list_display = ('published_time')
